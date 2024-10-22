import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to plot radar chart
def plot_radar(categories, values, title="Radar Chart"):
    N = len(categories)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values += values[:1]  # Ensure the plot closes at the last point
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    ax.fill(angles, values, color='blue', alpha=0.25)
    ax.plot(angles, values, color='blue', linewidth=2)

    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1', '2', '3', '4', '5'])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, fontsize=10)
    ax.set_title(title)

    return fig

# Ensure responses exist in session_state
if 'responses' in st.session_state:
    responses = st.session_state.responses

    # List of all dimensions that should appear in the chart
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

    # Pre-fill all dimensions with a default score of 3 (neutral)
    categories = all_dimensions
    values = [3] * len(all_dimensions)

    # Replace the default values with actual scores if available
    for i, dimension in enumerate(all_dimensions):
        if dimension in responses and isinstance(responses[dimension], dict) and 'overall' in responses[dimension]:
            values[i] = responses[dimension]['overall']

    # Radar chart for the results
    st.subheader("Results - Spider Web Chart for Overall Dimensions")
    fig = plot_radar(categories, values, title="Dimension Averages")
    st.pyplot(fig)
else:
    st.write("No responses found. Please complete the assessment first.")