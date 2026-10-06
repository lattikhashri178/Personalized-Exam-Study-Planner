import fitz
import pytesseract


def extract_text_from_pdf(pdf_path):

    document = fitz.open(pdf_path)

    text = ""

    for page in document:

        # First try normal PDF text
        page_text = page.get_text()

        if page_text.strip():
            text += page_text
        else:
            # If PDF is scanned, use OCR
            pix = page.get_pixmap()
            image = pix.pil_image()

            text += pytesseract.image_to_string(image)

        text += "\n"

    document.close()

    return text