# 🤖 AI Chatbot — Ollama + Llama + Streamlit

A lightweight, locally running AI chatbot built with **Python, Streamlit, Ollama, and Llama**. The application provides a simple conversational interface where users can interact with a locally hosted Large Language Model (LLM) without relying on external AI APIs.

## ✨ Overview

This project demonstrates how a locally hosted LLM can be integrated into a Python web application to create an interactive AI chatbot.

The application uses **Ollama** to run the Llama model locally, while **Streamlit** provides the user interface and Python handles the application logic and communication with the model.

### 🔄 Application Flow

```text
User
  ↓
Streamlit Chat Interface
  ↓
Python Application Logic
  ↓
Ollama API
  ↓
Llama LLM
  ↓
Generated Response
  ↓
Streamlit UI
```

## 🚀 Features

* 💬 Interactive chat interface
* 🧠 Local Llama LLM inference using Ollama
* 🔒 Local model execution without sending conversations to an external AI API
* ⚡ Real-time response generation
* 🐍 Python-based application logic
* 🌐 Streamlit web interface
* 🗂️ Conversation history management
* 🔧 Modular project structure
* 🐛 Error handling and debugging for model/API responses

## 🛠️ Tech Stack

| Technology     | Purpose                  |
| -------------- | ------------------------ |
| **Python**     | Application logic        |
| **Streamlit**  | Web-based chat interface |
| **Ollama**     | Local LLM runtime        |
| **Llama**      | Language model           |
| **Git/GitHub** | Version control          |

## 📁 Project Structure

```text
ai-chatbot/
│
├── app.py
│
├── src/
│   └── service.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

> The exact structure may vary depending on the current implementation.

## ⚙️ How It Works

### 1. User Input

The user enters a message through the Streamlit chat interface.

### 2. Conversation Management

The application maintains the conversation history and sends the relevant messages to the model.

### 3. Ollama Integration

Python communicates with the locally running Ollama service and sends the conversation to the selected Llama model.

### 4. Llama Response

The Llama model processes the input and generates a response.

### 5. Response Display

The generated response is returned to the Python application and displayed through the Streamlit interface.

## 📋 Prerequisites

Before running the project, install:

* Python 3.9+
* Ollama
* Git

You also need to download a compatible Llama model through Ollama.

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install and run Ollama

Install Ollama and make sure the Ollama service is running.

Pull the Llama model you want to use:

```bash
ollama pull llama3
```

> If your project uses a different Llama model, replace `llama3` with the model name configured in your application.

### 5. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

## 💻 Example Interaction

```text
User:
What is artificial intelligence?

AI Chatbot:
Artificial intelligence refers to computer systems capable
of performing tasks that normally require human intelligence,
such as understanding language, recognizing patterns and
generating responses.
```

## 🧩 Key Learning Outcomes

Through this project, I explored:

* Integrating a Large Language Model into a Python application
* Working with locally hosted AI models
* Communicating with an LLM through Ollama
* Building interactive interfaces with Streamlit
* Managing conversation state
* Handling model/API responses
* Debugging integration issues
* Structuring an AI application into separate components
* Using AI-assisted development workflows

## 🔮 Future Improvements

Possible future improvements include:

* 📄 PDF/document-based question answering
* 🧠 Retrieval-Augmented Generation (RAG)
* 💾 Persistent conversation storage
* 👤 Multiple user sessions
* 🎙️ Voice input and output
* 🌐 Multilingual conversations
* ⚙️ Model selection from the UI
* 📊 Conversation analytics
* 🔐 User authentication

## 🎯 Project Purpose

This project was created to explore practical **AI application development** and understand how Large Language Models can be integrated into real-world software products.

Rather than relying entirely on cloud-based AI APIs, the project demonstrates a workflow using a **locally hosted LLM**, providing an opportunity to experiment with AI development, application integration, debugging, and user-interface design.

## 👨‍💻 Author

**Your Name**

* GitHub: https://github.com/marlan-s
* LinkedIn: https://linkedin.com/in/marlan-s

---

⭐ If you found this project useful, consider giving the repository a star!
