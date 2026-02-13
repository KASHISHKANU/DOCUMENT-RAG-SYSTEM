# 🚀 Policy Document RAG Assistant

AI Engineer Intern – Take Home Assignment

# 📌 Overview
This project implements a Retrieval-Augmented Generation (RAG) based question-answering assistant that answers user queries using internal company policy documents.

# The goal is to demonstrate:
- Strong prompt engineering
- Proper RAG architecture
- Grounded, hallucination-free answers
- Clear reasoning and evaluation

The assistant retrieves relevant policy information and generates answers strictly grounded in retrieved context.

# 🎯 Problem Statement

Given a set of company policy documents (Refund, Cancellation, Shipping policies), the system:
Retrieves relevant information from documents
Generates accurate and grounded answers
Avoids hallucinations
Uses clear and structured prompts

# 🧱 Architecture Overview

Policy PDFs
     ↓
PDF Loader
     ↓
Text Chunking
     ↓
Embeddings (SentenceTransformer)
     ↓
FAISS Vector Store
     ↓
Semantic Retrieval (Top-K)
     ↓
Cross-Encoder Reranking
     ↓
Prompt Template
     ↓
Gemini LLM
     ↓
Grounded Answer

# 📂 Project Structure

rag-policy-assistant/
│
├── dataset/
│   ├── refund_policy.pdf
│   ├── cancellation_policy.pdf
│   └── shipping_policy.pdf
│
├── src/
│   ├── config.py
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retriever.py
│   ├── prompts.py
│   ├── rag_pipeline.py
│   ├── evaluator.py
│   └── main.py
│
├── .env
├── requirements.txt
└── README.md

# ⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <https://github.com/KASHISHKANU/DOCUMENT-RAG-SYSTEM>
cd rag-policy-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Gemini API Key
Create .env file:
GEMINI_API_KEY=your_api_key_here

4️⃣ Run the Project
python src/main.py

# 📄 Dataset & Data Preparation

- Policy documents are stored as PDFs inside:
dataset/
       Data Preparation Steps
       Load PDFs using pypdf
       Extract text

- Clean and split into chunks
🔹 Chunking Strategy
Chunk Size: 400 words
Overlap: 80 words

- Reasoning:
Keeps semantic meaning intact
Improves retrieval accuracy
Prevents context loss
Fits within LLM context window

This size provided a good balance between retrieval precision and contextual completeness.

# 🧠 RAG Pipeline

- Embeddings
Model: all-MiniLM-L6-v2
Generates dense semantic vectors

- Vector Store
FAISS (IndexFlatL2)
Fast similarity search
Lightweight & simple for small datasets

- Retrieval
Semantic top-K retrieval (k=3)
Retrieved chunks passed to the LLM as context

⭐ Reranking (Retrieval Improvement)

After performing initial semantic retrieval using FAISS, a reranking step is applied to improve relevance before passing context to the LLM.

- Why Reranking?
Vector similarity search retrieves semantically similar chunks, but the top results are not always the most precise for the user’s query.
To improve grounding quality, a second-stage reranker is used.

- Approach Used
A Cross-Encoder reranker is applied after FAISS retrieval:
FAISS retrieves Top-K relevant chunks.
Each (query, chunk) pair is scored using a cross-encoder.
Chunks are reordered based on relevance scores.
Only the highest-ranked chunks are passed to Gemini.

# ✨ Prompt Engineering
Prompt engineering was treated as a core focus of this assignment.

# 🟡 Initial Prompt (Version 1)
Answer using the provided context.

Context:
{context}

Question:
{question}

- Issues Observed
Sometimes verbose
No structure
Weak hallucination control

# 🟢 Improved Prompt (Final Version)
You are a strict company policy assistant.

RULES:
1. Answer ONLY using the given context.
2. Do NOT guess or add extra information.
3. If answer is not found, say:
   "Information not available in policy documents."
4. Use bullet points.
5. Mention source policy.

# Improvements Made

- Explicit anti-hallucination rules
- Structured output format
- Clear fallback behavior
- Better grounding to retrieved context

🧪 Evaluation
- A small evaluation set was created containing:
Answerable questions
Partially answerable questions
Unanswerable questions

# Example Evaluation Questions
Question	Type
1. How do I request a refund?	Answerable
2. Can I cancel after shipping?	Partial
3. Do you provide insurance?	Unanswerable
4. How long does delivery take?	Answerable

# Evaluation Rubric
Score	Meaning
✅	 Accurate & grounded
⚠️	  Partial / unanswerable handled correctly
❌	 Weak or unclear

Sample Results
Question	            Accuracy	Hallucination Avoidance	  Clarity
Refund policy	         ✅	                ✅	           ✅
Cancellation	         ✅	                ✅	           ✅
Insurance	              ⚠️	                 ✅	            ✅

⚠️ Edge Case Handling
The system safely handles:

1️⃣ No Relevant Retrieval
Returns:
No relevant policy found.

2️⃣ Outside Knowledge Base
LLM instructed to respond:
Information not available in policy documents.
This prevents hallucination.

⚖️ Key Design Trade-Offs

Why FAISS?
-Fast
-Lightweight
-Minimal setup
-Ideal for small datasets
-Why Semantic Retrieval?

Keyword search fails when wording changes.
Embeddings capture meaning rather than exact words.

Why Strict Prompting?
Prompt constraints significantly reduced hallucinations and improved grounding consistency.

🏆 What I’m Most Proud Of
- Clean modular RAG architecture
- Prompt iteration improving answer quality
- Grounded responses with explicit hallucination control
- Clear evaluation methodology

🔧 What I Would Improve With More Time
- Retrieval confidence scoring
- Hybrid retrieval (semantic + keyword)
- Automatic source citation mapping
- Logging & tracing for debugging
- Add Different Models and make proper pipeline and save model with best performance and use it for Answers 

🧠 Tech Stack

# Core
- Python

# LLM
- Google Gemini (Gemini API) – Response generation

# Retrieval & NLP
- SentenceTransformers (MiniLM) – Semantic embeddings
- Cross-Encoder (MS MARCO MiniLM) – Reranking for retrieval precision
- FAISS – Vector similarity search

# Data Processing
- PyPDF – Policy document parsing
- NumPy – Vector computation

👨‍💻 Author
Mr Kashish Raj