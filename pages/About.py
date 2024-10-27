import streamlit as st

# Set page title and layout
st.set_page_config(page_title="About the IIP-Assessment Model", layout="centered")

# Page title
st.title("About the IIP-Assessment Model")

# Introduction section
st.markdown("""
### Overview

The **IIP-Assessment Model** is part of a prototype developed during a **Master's Thesis**. This model evaluates the feasibility of business use-cases that may benefit from **Industrial Immersive Platforms (IIPs)**, like those found in the **Industrial Metaverse**.

This tool was constructed as part of a research project aimed at exploring how businesses can leverage industriyl immersive platforms (IIP) to optimize their operations. It combines several research approaches, including literature reviews and qualitative interviews, to create a practical and academically informed framework.

---

### Methodology

The construction of this model follows a **Design Science Research (DSR)** methodology. This approach is commonly used to create and evaluate artifacts (such as models and tools) that solve real-world problems. The DSR methodology used here involved the following key stages:

1. **Problem Identification**: 
   The lack of structured approaches for evaluating the viability of immersive platforms in industrial settings was identified as a gap in current research and practice.

2. **Objectives of the solution**: 
   requires preparing and conducting a systematic literature review (SLR) that intends to establish a design foundation for the artifact's dimensions. By identifying over 262 unique characteristics that affect the viability of different use-cases, we created the foundation for our IIP-Assessment Model.

3. **Construction of the artifact**: 
   We aim to make sense of the findings from the SLR by using **Grounded Theory** and the Gioia-Methodology to identify Core- and Subdimensions, and with that create the IIP-Assessment Model. 
            
4. **Evaluation Cycle**: 
   We validated the IIP-Assessment model through 20 Interviews with knowledgable industry experts. This process allowed the refinement of the dimensions and ensured the relevance for real businesses.

5. **Communication Stage**:
   inally, the results gathered during the evaluation phase are used to create a definitive product & publish the results. 

---

### Prototype Disclaimer

Please note that this is a **prototype**. While it has been designed with rigorous academic backing, further validation and testing are required before it can be fully implemented in an industrial setting.

---
""")

# Add a "continue" button to return to the main page or assessment
if st.button("continue with Assessment"):
    st.write("You can navigate using the sidebar.")
