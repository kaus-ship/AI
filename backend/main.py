from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter

import os

from utils.pdf_parser import extract_pdf_text
from utils.ppt_parser import extract_ppt_text
from utils.web_parser import extract_web_text
from utils.youtube_parser import extract_youtube_text

from utils.embeddings import get_embeddings
from utils.retrieval import save_index, retrieve
from utils.llm import ask_llm

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)

documents = []
chat_history = []

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)


class URLInput(BaseModel):
    url: str


class Question(BaseModel):
    question: str


def rebuild_vector_store():

    all_chunks = []

    for doc in documents:

        chunks = splitter.split_text(
            doc["text"]
        )

        for chunk in chunks:

            all_chunks.append(
                {
                    "source": doc["source"],
                    "reference": doc["reference"],
                    "text": chunk
                }
            )

    if len(all_chunks) == 0:
        return

    embeddings = get_embeddings(
        [x["text"] for x in all_chunks]
    )

    save_index(
        embeddings,
        all_chunks
    )


@app.get("/")
def home():

    return {
        "message": "AI Learning Assistant Running"
    }


@app.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(path, "wb") as f:
        f.write(await file.read())

    pages = extract_pdf_text(path)

    documents.extend(pages)

    rebuild_vector_store()

    return {
        "message": "PDF uploaded successfully",
        "pages": len(pages)
    }


@app.post("/upload-ppt")
async def upload_ppt(
    file: UploadFile = File(...)
):

    path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(path, "wb") as f:
        f.write(await file.read())

    slides = extract_ppt_text(path)

    documents.extend(slides)

    rebuild_vector_store()

    return {
        "message": "PPT uploaded successfully",
        "slides": len(slides)
    }


@app.post("/add-website")
def add_website(
    data: URLInput
):

    website_data = extract_web_text(
        data.url
    )

    documents.extend(
        website_data
    )

    rebuild_vector_store()

    return {
        "message": "Website added successfully"
    }


@app.post("/add-youtube")
def add_youtube(
    data: URLInput
):

    youtube_data = extract_youtube_text(
        data.url
    )

    documents.extend(
        youtube_data
    )

    rebuild_vector_store()

    return {
        "message": "YouTube video added successfully"
    }


@app.get("/sources")
def get_sources():

    return {
        "total_sources": len(documents),
        "sources": documents
    }


@app.post("/ask")
def ask_question(
    data: Question
):

    if len(documents) == 0:

        return {
            "answer":
            "Please upload at least one source first."
        }

    retrieved_chunks = retrieve(
        data.question,
        5
    )

    context = "\n\n".join(
        [
            item["text"]
            for item in retrieved_chunks
        ]
    )

    citations = []

    for item in retrieved_chunks:

        citations.append(
            f"{item['source']} - {item['reference']}"
        )

    history = "\n".join(
        [
            f"Q: {item['q']}\nA: {item['a']}"
            for item in chat_history
        ]
    )

    answer = ask_llm(
        data.question,
        context,
        history
    )

    chat_history.append(
        {
            "q": data.question,
            "a": answer
        }
    )

    return {
        "answer": answer,
        "sources": list(
            set(citations)
        )
    }