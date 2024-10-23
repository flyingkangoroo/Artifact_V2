import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Collaboration"

# Initialize session state for storing responses if not already done
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Ensure the current dimension is initialized in the session state correctly
if dimension not in st.session_state.responses or isinstance(st.session_state.responses[dimension], int):
    # If dimension is missing or stored incorrectly as an int, initialize it properly
    st.session_state.responses[dimension] = {
        "questions": {},  # For storing individual question responses
        "overall": 3  # Default overall score (can be updated later)
    }

# Example questions for this dimension
subdimensions = {
    "Collaboration": [
        "Collaborative Virtual Environments: Our use case benefits from immersive virtual environments that simulate corporate settings, include collaborative spaces, and enable multi-party remote collaboration when real-world interactions are not feasible.",
        "Co-Creation: Our use case benefits from enabling users to generate content, participate in co-creation activities, and personalize their work environments, enhancing learning and engagement through shared and collaborative experiences."
    ],
    "Collaborative Information Layers": [
        "Seamless Interaction: Our use case benefits from interoperability across platforms, seamless connectivity between users and systems, and the ability to interact with digital objects in real time, enhancing collaboration and communication.",
        "Sensory Feedback: Simulating face-to-face interactions and providing sensory feedback, such as body language and eye contact, enhances user engagement and collaboration in our use case.",
        "Teamwork: Our use case benefits from incorporating additional layers of information and testing team collaboration in a risk-free, virtual environment."
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension assesses whether current collaborative processes could be enhanced through immersive technologies. It explores how the transition to a virtual environment could support remote teamwork, co-creation, and real-time interaction. It also considers the platform's ability to replicate real-world communication dynamics, such as body language and sensory feedback, which could lead to more effective and engaging collaboration between teams or partners across locations.")
subdimension_scores = []
all_answered = True  # A flag to track if all questions are answered

for subdimension, questions in subdimensions.items():
    st.subheader(subdimension)
    scores = []
    for question in questions:
        # Generate a unique key for each question
        question_key = f"{dimension}-{subdimension}-{question}"

        # Check if this question already has a saved answer in st.session_state.responses[dimension]['questions']
        if question_key in st.session_state.responses[dimension]["questions"]:
            saved_answer = st.session_state.responses[dimension]["questions"][question_key]
            initial_index = saved_answer - 1  # Convert saved score back to index (1-5 to 0-4)
        else:
            initial_index = 2  # Default to 'Neutral'

        # Display the radio button with the previously selected value (if available)
        score = st.radio(
            question,
            ('Strongly Disagree', 'Somewhat Disagree', 'Neutral', 'Somewhat Agree', 'Strongly Agree'),
            index=initial_index, key=question_key
        )

        score_value = {'Strongly Disagree': 1, 'Somewhat Disagree': 2, 'Neutral': 3, 'Somewhat Agree': 4, 'Strongly Agree': 5}
        scores.append(score_value[score])

        # Store the selected answer in session_state under 'questions'
        st.session_state.responses[dimension]["questions"][question_key] = score_value[score]

    # Calculate the average score for the subdimension
    subdimension_average = np.mean(scores)
    subdimension_scores.append(subdimension_average)

# Calculate the overall score for the dimension by averaging subdimension scores
overall_dimension_score = np.mean(subdimension_scores)
st.session_state.responses[dimension]['overall'] = overall_dimension_score

# Display progress
progress = 4 / 8  # First dimension of eight
st.progress(progress)

# Alert if not all questions are answered (optional)
if not all_answered:
    st.warning("Some questions are not answered. You can continue, but it is recommended to answer all questions.")

# Navigation buttons
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page using the sidebar.")

if col2.button("Next"):
    st.write("Navigate to the next page using the sidebar.")
