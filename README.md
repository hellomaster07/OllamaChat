![model](https://github.com/user-attachments/assets/6132ab39-fa13-443f-8af2-4f8c608266c6)
<h1>DESCRIPTION:</h1>

This project is a Flask application that integrates with the Ollama API to provide a chatbot interface. 
Users can send messages via a web form, and the application communicates with a locally hosted Ollama instance (LLaMA 3.1 model) to generate responses. 
The frontend uses Tailwind CSS for styling, and the chat history is displayed dynamically on the page.
Prerequisites

<h2>BEFORE RUNNING THE APPLICATION, ENSURE YOU HAVE THE FOLLOWING INSTALLED:</h2>

- Python 3.8 or higher

- Ollama (running locally with the LLaMA 3.1 model)

- Git

- A web browser

<h2>INSTALLATION:</h2>

- Clone the Repository

- git clone https://github.com/your-username/ollama-chatbot.git

- cd ollama-chatbot



<h2>SET UP A VIRTUAL ENVIRONMENT:</h2>

- python -m venv venv

- On Windows: venv\Scripts\activate


<h2>INSTALL DEPENDENCIES:</h2>

- pip install flask ollama

- Install and Configure Ollama

- Follow the instructions at Ollama's official site to install Ollama.


<h2>ENSURE THE LLAMA 3.1 MODEL IS PULLED AND RUNNING:</h2>

- ollama run llama3.1

-- Verify that Ollama is accessible at http://localhost:11434.

<h2>USAGE:</h2>

- Run the Flask Application

-- python chatbot_app.py


<h2>ACCESS THE CHATBOT</h2>

- Open a web browser and navigate to http://localhost:5000.

- Type a message in the input field and click "Responce" to interact with the chatbot.

- The conversation will appear in the chat box, with user messages in blue and bot responses in green.


<h2>PROJECT STRUCTURE</h2>

![Screenshot 2025-04-22 152757](https://github.com/user-attachments/assets/2256dfdd-9a10-45f6-a1c0-73faa9b45cf2)


<h2>NOTES</h2>

- Ensure the Ollama server is running before starting the Flask app.

- The application runs in debug mode by default (debug=True). Disable this in production.

- The Tailwind CSS CDN is used for styling. For production, consider hosting Tailwind locally or using a build process.

<h2>CONTRIBUTING:</h2>

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Commit your changes (git commit -m "Add feature").

4. Push to the branch (git push origin feature-branch).

5. Open a Pull Request.

<h2>LICENSE:</h2>

This project is licensed under the MIT License.
