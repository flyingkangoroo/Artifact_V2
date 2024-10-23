import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Presence"

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
    "Realism through multisensory immersion": [
        "Realism: Our use case benefits from integrating realistic human factors, such as postures, gestures, and facial expressions, along with multisensory experiences like spatial and haptic feedback, to create a realistic or pseudo-natural environment that mirrors real-world scenarios, enhancing the user experience and improving outcomes.",
        "Realistic Interaction: Our use case benefits from integrating multiple senses (sight, sound, and touch), tactile sensations, and force feedback in a photorealistic and immersive environment, where users interact naturally with real-time movements, gestures, and spatial information."
    ],
    "User Stimulation": [
        "User Experience: Our use case benefits from providing immersive and interactive environments that simulate real-world experiences, offering easy navigation and a seamless user experience.",
        "Emotional Engagement: Our use case benefits from adding sensory layers and stimuli that enhance emotional engagement and learning, while focusing on user experience, usability, and creating meaningful real-world effects in the virtual environment."
    ],
    "Realism through interaction": [
        "Social Interaction: Our use case benefits from enabling real-time social interactions and collaboration within the IIP, where users can contribute to a shared virtual space and have control over their interactions with the virtual environment and other users.",
        "Dynamic Interaction: Our use case benefits from providing real-time feedback and dynamic, immersive interactions within the IIP, enhancing user engagement and creating more meaningful virtual experiences.",
        "Natural and Authentic Interactions: Our use case benefits from facilitating natural and authentic interactions within the IIP, where sensors enable eye contact, gestures, and facial expressions, contributing to a more immersive and realistic experience."
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Presence examines the potential for immersive technologies to create more engaging and realistic experiences. It focuses on whether integrating multisensory elements, such as visual, auditory, or tactile feedback, could enhance user immersion and emotional engagement. This dimension looks at how real-world dynamics—such as human interactions, spatial awareness, and social cues—can be recreated in a virtual space to improve engagement and outcomes in tasks, training, or communication.")
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
progress = 5 / 8  # First dimension of eight
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