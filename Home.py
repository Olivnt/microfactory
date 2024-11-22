import streamlit as st
  st.image("Pictures/ucl.png", caption="UCL", use_container_width=True)


# Home Page

st.title("Microfactory for Plant-Based Yogurt Production")
st.subheader("Showcasing Sustainable and Modular Food Production")

# Project Overview
st.header("Project Overview")
st.write("""
Our microfactory is a compact, flexible, and modular solution for producing plant-based yogurt.
Designed for educational purposes, it integrates sustainability, automation, and ease of use 
to teach and inspire students and aspiring producers.
""")

# Key Features
st.header("Key Features")
st.write("""
- **Sustainability**: Designed with eco-friendly materials and processes.
- **Modular Design**: Components can be replaced or customized easily.
- **User-Friendly**: Suitable for both beginners and experienced producers.
- **Automation**: Equipped with PLC control and a digital twin for real-time data tracking.
""")

# Placeholder for Image

st.header(" Concept after survey")

st.image("Pictures/ucl.png", caption="UCL", use_container_width=True)

# Target Audience
st.header("Target Audience")
st.write("""
- Educational Institutions: Schools and universities for teaching sustainable production.
- Small Producers: Entrepreneurs looking to venture into plant-based yogurt production.
- Researchers: Exploring new methods and technologies in food production.
""")

# Interactive Section
st.header("Interactive Section")
option = st.selectbox(
    "Which aspect of the microfactory excites you the most?",
    ["Sustainability", "Modularity", "Automation", "Educational Value"]
)
st.write(f"You selected: {option}")

# Contact Information
st.header("Contact Us")
st.write("For more information, please contact us at: [info@microfactory.com](mailto:info@microfactory.com)")


    

    
