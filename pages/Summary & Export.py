import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from textwrap import shorten
from fpdf import FPDF
import tempfile
import os

# Function to create a new detailed breakdown page
def detailed_breakdown_page():
    st.title("Detailed Dimension Breakdown")
    st.write("Below, you'll find a deeper analysis of each dimension with a breakdown of individual subdimensions.")

    if 'responses' not in st.session_state:
        st.write("No responses found. Please complete the assessment first.")
        return

    responses = st.session_state.responses
    all_dimensions = [
        "Accessibility",
        "Use Case Specifics",
        "Business & Economy",
        "Collaboration",
        "Presence",
        "Simulation & Modelling",
        "Technical Infrastructure",
        "Identity & Reputation"
    ]

    detailed_info = []
    charts = []

    # Display bar charts for each dimension's subdimension score (without weights)
    for dimension in all_dimensions:
        if dimension in responses and isinstance(responses[dimension], dict) and 'questions' in responses[dimension]:
            subdimensions = responses[dimension]['questions']
            st.subheader(f"{dimension} Breakdown")

            # Shorten subdimension names for visualization purposes by extracting the part after the first dash
            sub_names = [key.split('-', 1)[-1].split(':', 1)[0].strip() for key in subdimensions.keys()]
            sub_scores = list(subdimensions.values())

            # Collecting information for PDF export
            detailed_info.append((dimension, sub_names, sub_scores))

            # Plotting each subdimension using matplotlib
            fig, ax = plt.subplots()
            ax.barh(sub_names, sub_scores, color='darkblue')
            ax.set_xlabel('Score')
            ax.set_xlim(0, 5)
            ax.set_title(f"Subdimension Scores for {dimension}")

            st.pyplot(fig)
            # Save figure for PDF
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
                chart_path = tmp_file.name
                plt.savefig(chart_path)
                charts.append((dimension, chart_path))

    st.write("### Download Report")
    st.write("If you want to save your report for this use case you can download the detailed assessment by pressing the following button. Use these charts to understand specific areas of strength or those requiring improvement.")

    # Button to export results as PDF
    if st.button("Export Detailed Breakdown as PDF"):
        create_pdf_report(detailed_info, charts)

# Function to create a PDF report of the detailed breakdown
def create_pdf_report(detailed_info, charts):
    # Create radar plot for PDF export
    responses = st.session_state.responses
    all_dimensions = [
        "Accessibility",
        "Use Case Specifics",
        "Business & Economy",
        "Collaboration",
        "Presence",
        "Simulation & Modelling",
        "Technical Infrastructure",
        "Identity & Reputation"
    ]
    dimension_weights = st.session_state.get('dimension_weights', {dimension: 1.0 for dimension in all_dimensions})  # Use weights from session_state if available
    values = [responses[dimension]['overall'] if 'overall' in responses[dimension] else 3 for dimension in all_dimensions]
    weighted_sum = sum(values[i] * dimension_weights[dimension] for i, dimension in enumerate(all_dimensions))
    total_weight = sum(dimension_weights.values())
    final_readiness_score = weighted_sum / total_weight if total_weight != 0 else 0

    # Radar plot for the final readiness score
    # Apply the manager-defined weights to the radar values
    weighted_values = [values[i] * dimension_weights[dimension] for i, dimension in enumerate(all_dimensions)]
    # Ensure values do not exceed 5
    weighted_values = [min(5, value) for value in weighted_values]
    categories = all_dimensions + [all_dimensions[0]]  # Close the radar chart loop
    radar_values = weighted_values + [weighted_values[0]]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    ax.fill(angles, radar_values, color='darkblue', alpha=0.25)
    ax.plot(angles, radar_values, color='darkblue', linewidth=2)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(all_dimensions, fontsize=10)
    ax.set_title("Weighted Dimension Averages")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
        radar_chart_path = tmp_file.name
        plt.savefig(radar_chart_path)
    
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Title Page
    pdf.add_page()
    pdf.set_font("Arial", 'B', size=20)
    pdf.cell(200, 20, txt="IIP-Assessment Model Results", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("Arial", 'I', size=14)
    pdf.cell(200, 10, txt="Evaluating Your Business Use Case for Immersive Platform Readiness", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt="The Industrial Immersive Platform (IIP) Assessment Model is designed to evaluate the readiness of a business use case for transformation into an immersive environment. This report provides a detailed breakdown of the subdimension results, offering insights that contribute to the overall readiness score.")
    pdf.ln(20)
    pdf.image(radar_chart_path, x=15, w=180)
    pdf.ln(20)

    # Adding Final Readiness Score
    pdf.set_font("Arial", 'B', size=16)
    pdf.cell(200, 10, txt="Final Readiness Score", ln=True, align='C')
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Overall Readiness Score: {final_readiness_score:.2f} / 5", ln=True, align='C')
    pdf.ln(20)

    # Adding Detailed Results
    for (dimension, sub_names, sub_scores), (chart_dimension, chart_path) in zip(detailed_info, charts):
        pdf.add_page()
        pdf.set_font("Arial", 'B', size=16)
        pdf.cell(200, 10, txt=f"{dimension} - Detailed Breakdown", ln=True, align='C')
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        for sub_name, sub_score in zip(sub_names, sub_scores):
            pdf.cell(200, 8, txt=f"- {sub_name}: Score - {sub_score}", ln=True)
        pdf.ln(10)
        # Add the corresponding chart to the PDF
        pdf.image(chart_path, x=15, w=180)
        pdf.ln(10)

    # Save the PDF to a temporary file and offer it for download
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        pdf.output(tmp_file.name)
        with open(tmp_file.name, 'rb') as f:
            st.download_button(label="Download PDF Report", data=f.read(), file_name="detailed_breakdown_report.pdf", mime="application/pdf")

    # Clean up the temporary chart files
    if os.path.exists(radar_chart_path):
        os.remove(radar_chart_path)
    for _, chart_path in charts:
        if os.path.exists(chart_path):
            os.remove(chart_path)

# Main application logic
detailed_breakdown_page()