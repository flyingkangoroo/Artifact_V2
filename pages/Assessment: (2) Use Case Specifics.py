import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Use Case Specifics"

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
    "Added Value": [
        "Added Value: The integration of an immersive platform significantly enhances our use-case, adding value through new layers of information, improved simulations, or enhanced user experiences.",
        "Strategy: We have a well defined use-case’s strategy for integrating an immersive platform, with clear goals and a concept that maximizes the platform’s potential value."
    ],
    "Corporate Readiness": [
        "Culture: The integration of an immersive platform alignes with our company's culture, strategy, and goals, while remaining within the moral and ethical guidelines of our country.",
        "Corporate Readiness: Our organizational culture is ready to adopt an immersive platform, accepting the technology and being open to new ideas.",
        "Political Environment: The integration of an immersive platform is possible within the current social discourse and governmental regulatory premises."
        ],
    "Product & User Specifics": [
        "Ease of Integration: Our use case already has technological connections in place, making the integration of immersive platforms straightforward and beneficial and users would benefit from learning through immersive environments rather than relying solely on numbers and data.",
        "User Readiness: Our users are tech-savvy, capable of translating immersive experiences into real-world contexts, and ready for a digital transformation that enhances their job performance without compromising service quality or user experience",
        "User Satisfaction: Our use case benefits from enhancing customer satisfaction through improved user engagement, experience-oriented services, and transparency, as well as by offering services that better meet user needs.",
        "Customer Journey: Our use case ensures a seamless customer experience on the immersive platform, while incorporating user feedback and understanding their needs in the current use case."
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
progress = 2 / 8  # First dimension of eight
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