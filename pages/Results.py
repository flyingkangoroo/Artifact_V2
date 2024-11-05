import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to plot an interactive radar chart
def plot_interactive_radar(categories, values, title="Radar Chart"):
    fig = go.Figure()

    values += values[:1]  # Close the radar chart loop
    categories += categories[:1]  # Close the radar chart loop

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Assessment Score',
        line=dict(color='blue')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 5],
                tickfont=dict(color='darkred')  # Change the color of the numbers to make them more visible
            )
        ),
        showlegend=False,
        title=title
    )

    st.plotly_chart(fig)

# Ensure responses exist in session_state
if 'responses' in st.session_state:
    responses = st.session_state.responses

    # List of all dimensions that should appear in the chart
    all_dimensions = [
        "Accessibility",
        "Use Case Specifics",
        "Business & Economy",
        "Collaboration & Interaction",
        "Presence",
        "Simulation & Modeling",
        "Technical Infrastructure"
    ]

    # Allow users to customize the weight for each dimension
    st.sidebar.header("Customize Weights for Each Dimension")
    dimension_weights = {}
    for dimension in all_dimensions:
        dimension_weights[dimension] = st.sidebar.slider(
            f"Weight for {dimension}", min_value=0.0, max_value=2.0, value=1.0, step=0.1
        )

    # Pre-fill all dimensions with a default score of 3 (neutral)
    categories = all_dimensions.copy()
    values = [3] * len(all_dimensions)

    # Replace the default values with actual scores if available and apply weights
    for i, dimension in enumerate(all_dimensions):
        if dimension in responses and isinstance(responses[dimension], dict) and 'overall' in responses[dimension]:
            original_score = responses[dimension]['overall']
            weight = dimension_weights[dimension]
            
            # Adjust the score based on weighting logic
            if original_score > 3:
                # For positive scores, amplify the score with the weight
                values[i] = min(original_score * weight, 5)  # Ensure the max value does not exceed 5
            elif original_score < 3:
                # For negative scores, apply a dampening factor, keeping it low or reducing further
                values[i] = original_score * (1 - (weight / 2))
            else:
                # Neutral scores remain neutral regardless of weight
                values[i] = original_score

    # Explanation about weighting
    st.write("""
        ### Customizing Weights for Dimensions
        You have the ability to adjust the weights for each dimension using the sliders in the sidebar. This feature allows you to place more importance on certain aspects of your use case, depending on your business needs and priorities. For instance, if **Collaboration** is crucial to your operations, you can increase its weight to see how it affects the overall readiness of your use case for an immersive platform. Adjusting these weights helps provide a more tailored and strategic assessment outcome.
        
        Note: If a dimension receives a low score but is marked as very important, it will be weighted down even more to emphasize that it is a critical area that needs attention before proceeding with an immersive transformation. If the dimension is marked as less important, it will have a reduced impact on the final assessment but will not improve artificially.
    """)

    # Radar chart for the results
    st.subheader("Results - Radar Chart for Overall Dimensions")
    plot_interactive_radar(categories, values, title="Weighted Dimension Averages")

    # Calculate the final readiness score as a weighted average of all dimensions
    weighted_sum = sum(values[i] * dimension_weights[dimension] for i, dimension in enumerate(all_dimensions))
    total_weight = sum(dimension_weights.values())
    if total_weight == 0:
        final_readiness_score = 0  # Prevent division by zero if all weights are zero
    else:
        final_readiness_score = weighted_sum / total_weight

    # Display the final readiness score
    st.write("""
        ### Final Readiness Score
        The final readiness score represents an overall assessment of your use case's suitability for immersive transformation, taking into account the importance you assigned to each dimension. 
        \n 
        ***WARNING:*** This score represents only an average value. This score is influenced by your personalized weights.
    """)
    st.metric(label="Final Readiness Score", value=f"{final_readiness_score:.2f} / 5")

    
else:
    st.write("No responses found. Please complete the assessment first.")
