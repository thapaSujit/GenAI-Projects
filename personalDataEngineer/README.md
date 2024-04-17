# Personal Data Engineer
Personal Data Engineer is a chat application powered by Langchain, Faiss DB, Flask, and OpenAI LLM for answering questions related to data engineering. It utilizes a combination of natural language processing and deep learning techniques to provide accurate and timely responses to user inquiries.

# Features
1. Interactive chat interface for asking questions about data engineering.
2. Integration with Langchain for natural language understanding.
3. Utilization of Faiss DB for vector storage and retrieval.
4. Integration with OpenAI LLM for generating relevant responses based on user queries.

# Installation:
1. Prerequisites: Ensure you have Python (3.x) and pip installed on your system.
2. Clone the Repository: Use git clone https://github.com/thapaSujit/GenAI-Projects/tree/main/personalDataEngineer to clone this project.
3. Create Virtual Environment (Optional): It's recommended to create a virtual environment to isolate project dependencies. You can use tools like venv or virtualenv for this purpose.
4. Install Dependencies: Navigate to the project directory and run pip install -r requirements.txt to install the required libraries.

# Usage:

Start the Application: Run python app.py to launch the chatbot server.
Access the Chatbot: Open http://localhost:8080/ in your web browser to interact with the Personal Data Engineer chatbot.


# Dependencies:

- Flask
- PyPDF2 (likely used for PDF handling)
- Langchain libraries:
- langchain_openai
- langchain_core
- langchain_community
- langchainhub
- langserve
- uvicorn
- sse_starlette
- Faiss-cpu

# Code Structure:
The project has the following main file structure:

- `data (folder)`: Contains the source PDF document (de.pdf) used for training the chatbot's knowledge base.
- `static (folder)`: Contains the CSS file (style.css) that styles the chatbot's web interface.
- `templates (folder, based on Flask conventions)`: Contains the HTML template (index.html) that defines the chatbot's user interface.
- `app.py (main script)`: This Python script handles the core logic of the chatbot application.
- `src (folder)`: Contains utility functions used for data processing and vector database creation.
    - `utils.py`: This file contains functions for loading PDFs, splitting documents, and creating a FAISS vector database.
- `requirements.txt`: This file lists the required Python libraries and their versions for project dependencies.
- `setup.py`: This file is used for packaging the project and can be used with tools like pip for distribution.
src Folder and utils.py:
