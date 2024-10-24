import streamlit as st
import numpy as np

# Define the current dimension
dimension = "Business & Economy"

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
    "Resources": [
        "Resources: We have the financial and operational resources necessary to develop, implement, and manage an immersive platform.",
        "Technology: We have the necessary technology, technical expertise, and infrastructure to successfully implement and support an immersive platform.",
        "Budget: We have the budget and expect a positive cost-benefit ratio, with significant resource savings, through the integration of an immersive platform.",
        "Performance: We can enhance performance, reduce failure rates, and mitigate risks through the integration of an immersive platform, with confidence in the quality of our data.",
        "Data: We have the necessary data to develop and operate an industrial immersive platform."
    
    ],
    "Operations": [
        "Operational Flexibility: Our use-case benefits from enhancing operational flexibility and making better decisions by leveraging real-time data and IIP-based simulations.",
        "Safe Environments: We want to improve our training processes and workforce performance by using safe, cost-effective simulations of unique or expensive materials within an IIP.",
        "Decentralized Operations: Our use-case would benefit from decentralized operations, overcoming geographical restrictions and enabling direct peer-to-peer transactions through a blockchain-based IIP."
        ],
    "Business Expansion": [
        "New Business Models: Our use-case benefits from the development of new business models and opportunities, such as virtual goods, digital ownership, and additional distribution channels through an IIP.",
        "Virtual Retail: The integration of an IIP could enable new virtual retail channels and consumer products, offering our use-case opportunities for growth.",
        "Expanding Customer Reach: Our use-case would benefit from expanding our brand exposure to new customers and offering new communication channels with existing consumers through a virtual environment.",
        "Enhanced Problem Solving: Our use-case can address difficult or impossible real-life problems (e.g., dangerous tasks, space limitations) through the enhanced capabilities provided by an IIP."
        ]
}

# Collect responses
st.title(f"Assessing the Dimension: {dimension}")
st.write("This dimension evaluates the financial viability and operational benefits of adapting a business case to an immersive platform. It considers whether the investment would yield measurable improvements, such as cost efficiency, resource savings, or new revenue streams. Additionally, it looks at whether the use case could support new business models, such as virtual goods or decentralized operations, and whether there is sufficient infrastructure and budget to ensure a successful transformation.")
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
progress = 3 / 8  # First dimension of eight
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