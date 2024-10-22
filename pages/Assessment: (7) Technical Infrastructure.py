import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Technical Infrastructure"

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
    "Technological Foundation": [
        "Technology Readiness: We have the necessary technology, expertise, and infrastructure, including standardized formats and secure systems, to successfully implement and integrate an immersive platform into our processes.",
        "Data Standards:Our use case benefits from well-defined data standards, governance, and privacy protections to ensure smooth data sharing and technical security within the immersive platform."
    ],
    "Technological Features": [
        "Interoperability: Ensuring interoperability across platforms, devices, and departments improves our use case by enabling seamless data exchange, collaboration, and operational flexibility.",
        "Real-Time Systems: Our use case benefits from real-time simulations, mapping, and predictive systems that improve quality, efficiency, and decision-making, supported by standardized data formats and protocols.",
        "Sensory Engagement: Our use case benefits from real-time user interactions with objects, avatars, and immersive environments, enhancing engagement and collaboration through diverse sensory inputs.",
        "IoT Integration: Our use case benefits from integrating IoT devices, sensors, and advanced processing technologies that enhance data collection, visualization, and interaction within the immersive platform."
    ],
    "Technological Applicability": [
        "Practical Applicability: We prioritize the practical applicability of the immersive platform, utilizing modern technology to improve processes and operations in a realistic, scalable, and effective manner.",
        "Decentralization: Our use case benefits from operating on decentralized systems and involving stakeholders effectively within the immersive platform.",
        "Automation: Our use case benefits from interdisciplinary collaboration and systematic methodologies that support high-level automation and decision-making."
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("INSERT A REASONABLE DEFINITION.")
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
progress = 7 / 8  # First dimension of eight
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