import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Simulation & Modelling"

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
    "Simulation Use-Cases": [
        "Risk Reduction: Our use case benefits from virtual environments that replicate physical processes, reducing operational risks and ensuring safety for dangerous or high-risk activities that can be safely simulated.",
        "Hands-On: Our use case benefits from immersive simulations that support hands-on work, facilitate a fail-fast approach, and convey specialized knowledge through high immersion and interactive overlays.",
        "Training: Our use case involves tasks that would benefit from simulation for practice, training, and risk mitigation, overcoming physical, geographical, or time constraints, and enhancing real-world application understanding.",
        "Virtual-Real Synchronization: Our use case would benefit from real-time monitoring and synchronization between physical systems and digital environments, enabling precise control and timely updates.",
    ],
    "Immersive Process Optimization": [
        "Process Optimization: Our use case benefits from optimizing production processes through digital models that reduce downtime, scrap, and resource waste.",
        "Immersive Collaboration: Our use case benefits from enabling users to collaborate and interact with others and 3D objects in a simulated environment to develop new capabilities and meet user needs.",
        "Virtual Experience Transformation: We aim to transform our real-world use case into a virtual or immersive experience to enhance accessibility, knowledge sharing, and collaboration among users."
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension evaluates the potential for simulating real-world processes and scenarios in an immersive environment. It looks at whether the use case could benefit from virtual environments to reduce risks, enhance hands-on training, or optimize complex operations through modeling. It also assesses how closely the digital simulation can synchronize with real-world systems, enabling real-time monitoring, control, or predictive decision-making, all of which can improve efficiency and safety.")
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
progress = 6 / 8  # First dimension of eight
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