import streamlit as st

def display_summary(responses):
    # List of all dimensions
    all_dimensions = [
        "Identity & Reputation",
        "Presence",
        "Social Interactions",
        "Collaboration",
        "Accessibility",
        "Economy & Transactions",
        "Technology, Structure & Ecosystems",
        "Simulation & Modelling"
    ]

    # Extract scores from responses
    summary_values = {}
    for dimension in all_dimensions:
        if dimension in responses and isinstance(responses[dimension], dict) and 'overall' in responses[dimension]:
            summary_values[dimension] = responses[dimension]['overall']
        else:
            summary_values[dimension] = None  # Default for missing data

    # Display the summary
    st.subheader("Summary of Results")

    for dimension in all_dimensions:
        score = summary_values[dimension]
        st.write(f"**{dimension}:** {score if score is not None else 'No data'}")

        if score is not None:
            if score < 2:
                st.write("This indicates a potential area for improvement. Consider focusing on strategies to enhance this dimension.")
            elif 2 <= score < 4:
                st.write("This score suggests a neutral position; there may be strengths to build upon as well as areas that could be improved.")
            else:
                st.write("This reflects a strong position. Maintain and leverage these strengths to enhance overall performance.")

# Ensure responses exist in session_state
if 'responses' in st.session_state:
    responses = st.session_state.responses
    display_summary(responses)
else:
    st.write("No responses found. Please complete the assessment first.")