# StudyBuddy AI
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/DRPatel75/StudyBuddyStreamlit)

StudyBuddy AI is a versatile, AI-powered learning companion built with Streamlit and powered by the Groq API with the Llama 3.3 model. It's designed to assist students by providing quick answers, detailed explanations, quizzes, and flashcards on any topic.

![StudyBuddy AI Screenshot](https://raw.githubusercontent.com/DRPatel75/StudyBuddyStreamlit/main/app_screenshot.png)

## Features

StudyBuddy AI offers four core features to enhance your learning experience:

*   **❓ Ask a Question**: Get quick, accurate answers to any study-related question.
*   **📖 Explain a Topic**: Receive detailed explanations of complex topics, broken down into simple terms with key points and real-life examples.
*   **📝 Generate Quiz**: Create multiple-choice quizzes on any subject to test your knowledge. You can specify the number of questions.
*   **🃏 Generate Flashcards**: Instantly generate digital flashcards with questions on the front and answers on the back to aid in memorization.

## Tech Stack

*   **Frontend**: [Streamlit](https://streamlit.io/)
*   **AI/Inference**: [Groq API](https://groq.com/)
*   **Language Model**: Llama 3.3 70B

## Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites

*   Python 3.8 or later
*   A Groq API Key. You can get one from the [Groq Console](https://console.groq.com/keys).

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/DRPatel75/StudyBuddyStreamlit.git
    cd StudyBuddyStreamlit
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Configuration

The application requires your Groq API key to function. It's configured to read the key from Streamlit's secrets management.

1.  Create a directory named `.streamlit` in the root of the project folder.
2.  Inside the `.streamlit` directory, create a file named `secrets.toml`.
3.  Add your Groq API key to the `secrets.toml` file as shown below:

    ```toml
    # .streamlit/secrets.toml

    GROQ_API_KEY="your_groq_api_key_here"
    ```

## Usage

Once the installation and configuration are complete, you can run the Streamlit application.

1.  Navigate to the project's root directory in your terminal.
2.  Run the following command:
    ```bash
    streamlit run app.py
    ```
3.  The application will open in your default web browser.
4.  Use the sidebar to select a feature, enter your topic or question, and click the button to generate a response from the AI.
