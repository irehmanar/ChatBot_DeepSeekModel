# LangChain Demo with DeepSeek API

This repository demonstrates the integration of LangChain with the Streamlit framework to build an interactive chatbot powered by the Ollama LLM ("deepseek-r1:1.5b" model). The app allows users to input queries and receive dynamic responses in real-time.

---

## Features

- **LangChain Framework**: Efficiently manages custom prompts and LLM interactions.
- **Ollama DeepSeek Model**: Uses the "deepseek-r1:1.5b" model for generating high-quality responses.
- **Streamlit Interface**: Provides a user-friendly web app for interacting with the chatbot.
- **Environment Variable Management**: Secures API keys and configuration via a `.env` file.
- **LangSmith Tracking**: Tracks interactions for debugging and performance monitoring.

---

## Setup Instructions

### Prerequisites

- Python 3.8+
- Git installed on your system
- An API key for LangSmith (if applicable)

### Installation

1. Clone the repository:
   ```bash
   git clone <REPOSITORY_URL>
   cd <REPOSITORY_NAME>
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate # On Windows: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add the following:
   ```env
   LANGCHAIN_API_KEY=<your_langchain_api_key>
   ```

5. If using virtual environment, it will create folder (e.g., `chatbot_env`), ensure it is ignored in `.gitignore`:
   ```
   chatbot_env/
   ```

---

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser at `http://localhost:8501`.

3. Enter a query in the input field to interact with the LLM.

---

## File Structure

```
|-- app.py                # Main Streamlit application file
|-- .env                  # Environment variables (not included in Git)
|-- chatbot_env/          # Custom folder for local configurations (ignored in Git)
|-- requirements.txt      # Dependencies for the project
|-- README.md             # Project documentation
```

---

## Notes

- Ensure `.env` or `chatbot_env/` is added to `.gitignore` to protect sensitive data.
- The application uses the LangChain `ChatPromptTemplate` to format user queries effectively.

---

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

---

