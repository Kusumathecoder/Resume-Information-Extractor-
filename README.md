# 📄 Resume Information Extractor (JSON Output Parser)

## 🚀 Project Overview

This project extracts structured information from an unstructured resume PDF using:

- LangChain
- Ollama (Local LLM)
- JsonOutputParser
- Pydantic Schema Validation

The system converts raw resume text into structured JSON format.

---

## 🎯 Objective

Extract the following fields from a resume:

```json
{
  "name": "",
  "email": "",
  "skills": [],
  "experience_years": 0,
  "education": []
}
```

---

## 🏗️ Project Architecture

PDF Resume  
↓  
PyPDFLoader  
↓  
Prompt Template + Format Instructions  
↓  
Ollama Local Model (llama3)  
↓  
JsonOutputParser  
↓  
Structured JSON Output  

---

## 🛠️ Tech Stack

- Python
- LangChain
- Ollama (Local LLM)
- Pydantic
- PyPDF

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone <your-repo-url>
cd assignment2
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv rag_env
rag_env\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Setup Ollama

Install Ollama from:

https://ollama.com

Pull the model:

```bash
ollama pull llama3
```

Make sure Ollama is running:

```bash
ollama run llama3
```

Press Ctrl + C after confirmation.

---

## ▶️ Run the Project

Place your resume PDF in the project folder.

Then run:

```bash
python main.py
```

---

## 📤 Example Output

```json
{
  "name": "John Doe",
  "email": "johndoe@gmail.com",
  "skills": ["Python", "Machine Learning", "SQL"],
  "experience_years": 2,
  "education": ["B.Tech in Computer Science"]
}
```

---

## ✨ Features

- Structured JSON output using JsonOutputParser
- Schema validation with Pydantic
- Local LLM (no API key required)
- PDF resume support
- Error handling included

---

## 📚 Learning Outcomes

- Implemented structured prompting with format instructions
- Used JsonOutputParser for reliable JSON extraction
- Integrated Ollama local LLM with LangChain
- Extracted text from PDF using PyPDFLoader
- Built modular and production-ready LLM pipeline

---

## 👩‍💻 Author

Kusuma M  
B.E CSE (AI & ML)  
Siddaganga Institute of Technology

