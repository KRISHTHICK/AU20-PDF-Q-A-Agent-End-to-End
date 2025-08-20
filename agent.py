import os
from pdf_tool import PDFTool

# If you want OpenAI
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# If you want Ollama
import ollama

class PDFQAAgent:
    def __init__(self):
        self.pdf_tool = PDFTool()

    def load_pdf(self, file_path: str) -> str:
        return self.pdf_tool.load_pdf(file_path)

    def answer_question(self, question: str) -> str:
        context = self.pdf_tool.get_text()
        if not context:
            return "⚠️ Please load a PDF first."

        # ---- Option 1: Using Ollama ----
        response = ollama.chat(
            model="llama3",  # or another model installed
            messages=[
                {"role": "system", "content": "You are a helpful assistant answering questions from a PDF."},
                {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
            ]
        )
        return response['message']['content']

        # ---- Option 2: Using OpenAI (Uncomment if using OpenAI) ----
        # response = client.chat.completions.create(
        #     model="gpt-4o-mini",
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant answering questions from a PDF."},
        #         {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        #     ]
        # )
        # return response.choices[0].message.content
