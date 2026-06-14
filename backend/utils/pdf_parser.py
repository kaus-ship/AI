import fitz

def extract_pdf_text(path):

    doc = fitz.open(path)

    pages = []

    for i, page in enumerate(doc):

        text = page.get_text()

        pages.append(
            {
                "source": "PDF",
                "reference": f"Page {i+1}",
                "text": text
            }
        )

    return pages