import streamlit as st

# Title
st.title("Concept Showcase")

# Concept 1
st.header("Concept 1: Modular and Flexible Design")
st.image("images/concept1.png", caption="Concept 1 Image", se_container_width=True)
st.markdown("""
**Description:**
In this solution, wheels are mounted directly on all machines in the production facility. The wheels allow employees to move the machines freely around the production area without the need for additional equipment. The wheels will be specifically selected to ensure durability and stability, so the machines can be moved easily without the risk of tipping or damage.

**Advantages:**
- **Increased Flexibility:** Machines can be easily moved between workstations or for cleaning and maintenance.
- **Optimized Workflow:** Production and layout can be quickly adapted as needed, providing greater production capacity and more efficient use of space.
- **User-Friendliness:** The wheels make it easy for operators to rearrange the machines without extra tools, minimizing the need for technical knowledge or assistance.
- **Reduced Downtime:** Rapid repositioning of machines enables production to be reconfigured in a shorter time, reducing downtime in the production process.
""")

# Concept 2
st.header("Concept 2: User-Friendly and Automated Design")
st.image("images/concept2.png", caption="Concept 2 Image", se_container_width=True)
st.markdown("""
**Description:**
This option involves a custom-made, stable structure with wheels that can hold two or three smaller machines stacked on top of each other. The structure will ensure that the machines remain stable and secure during transport and use. This solution saves space by stacking the machines while maintaining mobility. The structure can also be easily moved and used in areas where space is limited, making it particularly advantageous for educational environments or smaller production areas.

**Advantages:**
- **Space Saving:** By stacking the machines, multiple units can be placed on a smaller floor area, which is beneficial in space-constrained environments.
- **Improved Transport:** The combined structure with wheels allows multiple machines to be moved at once, saving time and effort.
- **Safety and Stability:** The structure is designed to hold the machines securely in place during transport, minimizing the risk of damage to the machines and personnel.
- **Flexibility in Production:** The structure can be easily integrated into various work environments and rearranged according to production needs.
""")

# Add navigation link
st.markdown("[Go back to the survey](../Pages/survey.py)")
