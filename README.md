# AU20-PDF-Q-A-Agent-End-to-End
Ai Agent

🔹 How to Run

Save the files in pdf_qa_agent/.

Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py


Upload any PDF → Ask questions → Get answers 🎯

🔹 Explanation

pdf_tool.py → Extracts text from uploaded PDFs.

agent.py → Manages PDF + queries an LLM (Ollama/OpenAI).

app.py → User interface with Streamlit.

requirements.txt → Ensures reproducibility.
