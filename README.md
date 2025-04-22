DESCRIPTION:

This project is a Flask application that integrates with the Ollama API to provide a chatbot interface. 
Users can send messages via a web form, and the application communicates with a locally hosted Ollama instance (LLaMA 3.1 model) to generate responses. 
The frontend uses Tailwind CSS for styling, and the chat history is displayed dynamically on the page.
Prerequisites

BEFORE RUNNING THE APPLICATION, ENSURE YOU HAVE THE FOLLOWING INSTALLED:

- Python 3.8 or higher

- Ollama (running locally with the LLaMA 3.1 model)

- Git

- A web browser

INSTALLATION:

- Clone the Repository

- git clone https://github.com/your-username/ollama-chatbot.git

- cd ollama-chatbot



SET UP A VIRTUAL ENVIRONMENT:

- python -m venv venv

- On Windows: venv\Scripts\activate


INSTALL DEPENDENCIES

- pip install flask ollama

- Install and Configure Ollama

- Follow the instructions at Ollama's official site to install Ollama.


ENSURE THE LLAMA 3.1 MODEL IS PULLED AND RUNNING:

- ollama run llama3.1

-- Verify that Ollama is accessible at http://localhost:11434.

USAGE:

- Run the Flask Application

-- python chatbot_app.py


ACCESS THE CHATBOT

- Open a web browser and navigate to http://localhost:5000.

- Type a message in the input field and click "Responce" to interact with the chatbot.

- The conversation will appear in the chat box, with user messages in blue and bot responses in green.


PROJECT STRUCTURE

![Screenshot 2025-04-22 152757](https://github.com/user-attachments/assets/2256dfdd-9a10-45f6-a1c0-73faa9b45cf2)


NOTES

- Ensure the Ollama server is running before starting the Flask app.

- The application runs in debug mode by default (debug=True). Disable this in production.

- The Tailwind CSS CDN is used for styling. For production, consider hosting Tailwind locally or using a build process.

CONTRIBUTING:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Commit your changes (git commit -m "Add feature").

4. Push to the branch (git push origin feature-branch).

5. Open a Pull Request.

LICENSE:

This project is licensed under the MIT License.
