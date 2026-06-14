# AI Learning Assistant

## Overview

AI Learning Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to learn from multiple content sources such as PDFs, PowerPoint presentations, websites, and YouTube videos.

The system extracts content, generates embeddings, stores them in a FAISS vector database, and uses Google Gemini to answer user questions with source citations.

---

## Features

* PDF Upload and Processing
* PowerPoint (PPT/PPTX) Upload and Processing
* Website URL Content Extraction
* YouTube Transcript Processing
* Semantic Search using FAISS
* Google Gemini-powered Question Answering
* Source Citations
* Multi-source Retrieval
* Interactive React Frontend

---

## Tech Stack

### Frontend

* React.js
* Axios
* React Markdown

### Backend

* FastAPI
* Google Gemini API
* FAISS
* Sentence Transformers
* PyMuPDF
* python-pptx
* BeautifulSoup
* YouTube Transcript API

---

## Project Architecture

1. User uploads PDF, PPT, Website URL, or YouTube URL.
2. Content is extracted and split into chunks.
3. Sentence Transformers generate embeddings.
4. Embeddings are stored in FAISS.
5. User asks a question.
6. Relevant chunks are retrieved from FAISS.
7. Gemini generates an answer using retrieved context.
8. Sources are displayed with the answer.

---

## Folder Structure

AI-Learning-Assistant

├── backend

│   ├── main.py

│   ├── utils/

│   ├── uploads/

│   └── vector_store/

│

├── frontend

│   ├── src/

│   ├── public/

│   └── package.json

│

└── README.md

---

## Installation

### Backend

```bash
cd backend

pip install -r requirements.txt

uvicorn main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm start
```

---

## Usage

1. Upload a PDF or PPT file.
2. Add a Website URL.
3. Add a YouTube URL.
4. Ask questions about the uploaded content.
5. View AI-generated answers with citations.

---

## Future Enhancements

* Quiz Generation
* Course Creation
* User Authentication
* Learning Analytics Dashboard
* Multi-language Support

---

## Author

Kaushal Saha

B.Tech Data Science

Malla Reddy University
