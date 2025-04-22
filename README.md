Description:

This project is a Flask application that integrates with the Ollama API to provide a chatbot interface. Users can send messages via a web form, and the application communicates with a locally hosted Ollama instance (LLaMA 3.1 model) to generate responses. The frontend uses Tailwind CSS for styling, and the chat history is displayed dynamically on the page.
Prerequisites

Before running the application, ensure you have the following installed:

Python 3.8 or higher

Ollama (running locally with the LLaMA 3.1 model)

Git

A web browser

Installation:

Clone the Repository

git clone https://github.com/your-username/ollama-chatbot.git

cd ollama-chatbot



Set Up a Virtual Environment

python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate


Install Dependencies

pip install flask ollama

Install and Configure Ollama

Follow the instructions at Ollama's official site to install Ollama.


Ensure the LLaMA 3.1 model is pulled and running:

ollama pull llama3.1

ollama run llama3.1

Verify that Ollama is accessible at http://localhost:11434.

Usage

Run the Flask Application

python chatbot_app.py


Access the Chatbot

Open a web browser and navigate to http://localhost:5000.

Type a message in the input field and click "Responce" to interact with the chatbot.

The conversation will appear in the chat box, with user messages in blue and bot responses in green.


Project Structure

ollama-chatbot/

├── chatbot_app.py      # Flask application code

├── templates/

│   └── chat.html       # HTML template for the chat interface

├── README.md           # Project documentation

└── venv/               # Virtual environment (not tracked in Git)

Notes

Ensure the Ollama server is running before starting the Flask app.

The application runs in debug mode by default (debug=True). Disable this in production.

The Tailwind CSS CDN is used for styling. For production, consider hosting Tailwind locally or using a build process.

Contributing

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m "Add feature").

Push to the branch (git push origin feature-branch).

Open a Pull Request.

License

This project is licensed under the MIT License.
