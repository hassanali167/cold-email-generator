# 📧 Cold Email Generator

The **Cold Email Generator** is a Python-based web application that helps you generate personalized cold emails using your portfolio data. Built with Gradio for the user interface and integrated with vector databases and document handling tools, this tool streamlines the outreach process for professionals.

## 🚀 Features

- 🔍 Automatically analyzes your portfolio data (CSV format)
- 🧠 Uses vector embeddings to personalize emails
- 🔐 Environment variable for secure API key handling
- 📄 Generates professional cold emails for outreach
- 🌐 Easy-to-use web interface with Gradio
- 🐳 Dockerized for seamless deployment

---

## 📁 Project Structure

cold-email-generator/
├── app/
│ ├── main.py # Entry point with Gradio interface
│ ├── chains.py # Logic for generating email responses
│ ├── portfolio.py # Handles parsing of your portfolio
│ ├── utils.py # Helper functions
│ ├── my_portfolio.csv # Sample portfolio file
│ ├── requirements.txt # Python dependencies
│ ├── Dockerfile # Docker setup
│ └── .env (you create this) # Store your API key securely
├── vectorstore/ # Chroma DB vector storage
├── Docx/ # Documentation and diagrams
├── email_generator.ipynb # Notebook version for testing
└── requirements.txt # Top-level dependencies



---

## 🧰 Installation & Running (Without Docker)

### Prerequisites

- Python 3.10+
- `pip` package manager

### Setup

1. Clone the repository:
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator/app

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate

3.Install dependencies:
pip install -r requirements.txt

4.Set up your .env file in the app/ directory:
Create a file named .env
Add your Groq API key like this:
GROQ_API_KEY=your_groq_api_key_here

5.Run the app:
python main.py
