import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Identity & Reputation"

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

subdimensions = {
    "Personalization": [
        "Customization: Our use-case benefits from the customization of products/services to meet the individual needs of customers/users.",
        "Individual Needs: The identity and individual characteristics of our customers/users are crucial for tailoring our products/services.",
        "Hyper-Personalization: We see hyper-personalization and personalized digital tools as opportunities to offer tailored services, products, and production management solutions. "
    ],
    "Sociability": [
        "Engagement: Our use-case can improve customer/user engagement by fostering social interaction and communication through virtual environments, such as avatars or simulated face-to-face interaction.",
        "Shared Experience: Our use-case benefits from allowing users with similar interests to share experiences, advice, and emotional responses in a virtual environment.",
        "Inclusion: Incorporating inclusive and empathetic virtual experiences aligns with societal goals and could enhance our use-case." 
    ],
    "Users": [
        "User Motivation: Our use-case can benefit from creating a social platform where users share their experiences, thereby attracting potential users.",
        "Segmentation: We consider user diversity and segment users into specific groups to provide personalized strategies for our use-case.",
        "Virtual Identity: Providing users with unique virtual identities to conduct social activities (learning, working, socializing) could enhance our use-case."
    ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("Focuses on how important the support of creation, management, and evolution of user identities, and the creation and maintenance of the users virtual reputation within the virtaul environment is. This includes degrees of immersion, personalization, and multiple forms of interaction and collaboration.")
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
progress = 8 / 8  # Fourth dimension of eight
st.progress(progress)

# Alert if not all questions are answered (optional)
if not all_answered:
    st.warning("Some questions are not answered. You can continue, but it is recommended to answer all questions.")

# Navigation buttons
col1, col2 = st.columns([1, 1])

if col1.button("Previous"):
    st.write("Navigate to the previous page.")

if col2.button("Next"):
    st.write("Navigate to the next page.")