import streamlit as st
from groq import Groq

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="StudyBuddy AI",
    page_icon="📚",
    layout="wide"
)

# -------------------------
# Groq API Key
# -------------------------
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("Please add your GROQ_API_KEY in Streamlit Secrets.")
    st.stop()


# -------------------------
# Function to Get Response
# -------------------------
def get_response(prompt):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are StudyBuddy AI, a helpful and friendly learning assistant for students."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.5,
            max_tokens=1024
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {e}"


# -------------------------
# Title
# -------------------------
st.title("📚 StudyBuddy AI")
st.markdown("### Your AI-Powered Learning Companion")

st.write(
    "Ask questions, understand concepts, generate quizzes, "
    "and create flashcards instantly."
)

# -------------------------
# Sidebar
# -------------------------
feature = st.sidebar.selectbox(
    "Choose Feature",
    [
        "Ask a Question",
        "Explain a Topic",
        "Generate Quiz",
        "Generate Flashcards"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info(
    "Built using Streamlit + Groq + Llama 3.3"
)

# -------------------------
# Ask Question
# -------------------------
if feature == "Ask a Question":

    st.header("❓ Ask Any Study Question")

    question = st.text_area(
        "Enter your question:",
        height=150
    )

    if st.button("Get Answer"):

        if question.strip():

            with st.spinner("Thinking..."):

                answer = get_response(question)

            st.success("Answer Generated")
            st.write(answer)

        else:
            st.warning("Please enter a question.")


# -------------------------
# Explain Topic
# -------------------------
elif feature == "Explain a Topic":

    st.header("📖 Explain a Topic")

    topic = st.text_input("Enter Topic Name:")

    if st.button("Explain"):

        if topic.strip():

            prompt = f"""
            Explain the topic '{topic}' in simple language for students.

            Include:
            1. Definition
            2. Key Points
            3. Real-life Examples
            4. Summary
            """

            with st.spinner("Generating explanation..."):

                explanation = get_response(prompt)

            st.success("Explanation Ready")
            st.write(explanation)

        else:
            st.warning("Please enter a topic.")


# -------------------------
# Quiz Generator
# -------------------------
elif feature == "Generate Quiz":

    st.header("📝 Quiz Generator")

    topic = st.text_input("Enter Quiz Topic:")

    num_questions = st.slider(
        "Number of Questions",
        min_value=3,
        max_value=10,
        value=5
    )

    if st.button("Generate Quiz"):

        if topic.strip():

            prompt = f"""
Generate {num_questions} multiple-choice questions about {topic}.

Format EXACTLY like this:

Question: ...
A) ...
B) ...
C) ...
D) ...
Answer: A

Separate each question with ---
"""

            with st.spinner("Generating Quiz..."):
                quiz = get_response(prompt)

            st.success("Quiz Generated!")

            questions = quiz.split("---")

            for i, q in enumerate(questions, 1):
                st.markdown(f"### Question {i}")

                lines = q.strip().split("\n")

                for line in lines:
                    line = line.strip()

                    if line.startswith("Answer:"):
                        st.info(f"✅ {line}")
                    else:
                        st.write(line)

                st.divider()

        else:
            st.warning("Please enter a topic.")

# -------------------------
# Flashcard Generator
# -------------------------
elif feature == "Generate Flashcards":

    st.header("🃏 Flashcard Generator")

    topic = st.text_input("Enter Flashcard Topic:")

    number = st.slider(
        "Number of Flashcards",
        min_value=5,
        max_value=15,
        value=10
    )

    if st.button("Generate Flashcards"):

        if topic.strip():

            prompt = f"""
Create {number} flashcards about {topic}.

Format EXACTLY like this:

Front: Question
Back: Answer

Separate each flashcard with ---
"""

            with st.spinner("Generating Flashcards..."):
                flashcards = get_response(prompt)

            st.success("Flashcards Ready!")

            cards = flashcards.split("---")

            for i, card in enumerate(cards, 1):

                front = ""
                back = ""

                for line in card.split("\n"):

                    if line.startswith("Front:"):
                        front = line.replace("Front:", "").strip()

                    elif line.startswith("Back:"):
                        back = line.replace("Back:", "").strip()

                if front and back:
                    with st.expander(f"🃏 Flashcard {i}: {front}"):
                        st.write(back)

        else:
            st.warning("Please enter a topic.")