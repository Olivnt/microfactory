import streamlit as st

# Sidebar Navigation
page = st.sidebar.selectbox("Navigate", ["Home", "About"])

# Home Page
if page == "Home":
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
    st.header("Visual Representation")
    st.write("Image Placeholde")
    st.image("microfactory/ull.png", caption="UCL", use_container_width=True)
    
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

# About Page
elif page == "About":
    st.title("About Us")
    
    # About Olivier
   
    st.write ("OLivier")
   

   
    st.write(""""I have a strong background in IT, specializing in programming """.encode("utf-8", errors="replace").decode("utf-8"))

    st.header("Abdullah")

    st.write("""   Abdullah is a talented product designer with a focus on creating functional and visually
    appealing solutions. . """.encode("utf-8", errors="replace").decode("utf-8"))
    
