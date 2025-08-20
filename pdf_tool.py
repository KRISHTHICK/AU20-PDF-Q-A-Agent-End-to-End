import os
from pypdf import PdfReader

class PDFTool:
    """Tool to extract text from a PDF file."""

    def __init__(self):
        self.text = ""

    def load_pdf(self, file_path: str) -> str:
        if not os.path.exists(file_path):
            return "❌ File not found."

        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        
        self.text = text.strip()
        return "✅ PDF loaded successfully."

    def get_text(self) -> str:
        return self.text if self.text else "⚠️ No PDF loaded yet."
