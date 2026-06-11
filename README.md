# 📚 StudyBuddy AI

An AI-powered learning assistant built using **Streamlit** and **Groq (Llama 3.3)** to help students learn more effectively. StudyBuddy AI provides instant explanations, answers academic questions, generates quizzes, and creates flashcards to make studying interactive and engaging.

---

## 🚀 Features

* ❓ **Ask Questions**

  * Get instant answers to academic questions.

* 📖 **Explain Topics**

  * Understand complex concepts in simple language with examples.

* 📝 **Quiz Generator**

  * Generate multiple-choice quizzes on any topic.
  * Improved readable quiz format.

* 🃏 **Flashcard Generator**

  * Create interactive flashcards for quick revision.
  * Click-to-reveal answers for better learning.

* 🎨 **User-Friendly Interface**

  * Modern and responsive UI built with Streamlit.

---

## 🛠️ Technologies Used

* **Frontend:** Streamlit
* **Programming Language:** Python
* **AI Model:** Llama 3.3 (70B Versatile)
* **API Provider:** Groq
* **Version Control:** Git & GitHub
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```text
StudyBuddyStreamlit/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── secrets.toml
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DRPatel75/StudyBuddyStreamlit.git
cd StudyBuddyStreamlit
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.streamlit/secrets.toml` file and add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

### 4. Run the Application

```bash
streamlit run app.py
```

---

## ☁️ Deployment

This project can be deployed easily using **Streamlit Cloud**.

1. Push the project to GitHub.
2. Sign in to Streamlit Cloud.
3. Connect the GitHub repository.
4. Add the `GROQ_API_KEY` in Streamlit Secrets.
5. Deploy the application.

---

## 🎯 Problem Statement

Students often struggle to understand complex concepts while studying. Searching online can provide lengthy or irrelevant results, and teachers may not always be available. There is a need for a tool that can explain topics in simple terms, answer questions instantly, and generate quizzes or flashcards on demand using AI.

---

## 💡 Proposed Solution

StudyBuddy AI is designed to serve as an intelligent learning companion by:

* Providing instant academic assistance.
* Explaining difficult topics in simple language.
* Generating quizzes for self-assessment.
* Creating flashcards for effective revision.
* Enhancing self-learning experiences using AI.

---

## 🔮 Future Scope

* PDF Upload and Notes Summarization
* Voice-Based Interaction
* Multi-language Support
* Personalized Study Recommendations
* Progress Tracking Dashboard

---

## 👨‍💻 Developer

**Divyakumar Patel**

Capstone Project – StudyBuddy AI

---

## 📄 License

This project is developed for educational and academic purposes.
