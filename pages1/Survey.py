import streamlit as st
import pandas as pd
import os

# File to store survey responses
survey_file = "survey_responses.csv"

# Initialize session state to track voting
if "voted" not in st.session_state:
    st.session_state["voted"] = False

# Check if the user has already voted
if st.session_state["voted"]:
    st.warning("You have already submitted your response.")
else:
    st.title("Design Preference Survey")

    # Survey form
    st.header("Final Rating and Preference")
    rating_1 = st.slider("Rate Picture 1 (1 to 5)", 1, 5, key="rating_1")
    rating_2 = st.slider("Rate Picture 2 (1 to 5)", 1, 5, key="rating_2")
    preference = st.radio("Which design do you prefer?", ["Picture 1", "Picture 2"], key="preference")
    preference_reason = st.text_area("Reason for Preference", key="preference_reason")

    if st.button("Submit"):
        # Save the response
        data = {
            "Rating_1": rating_1,
            "Rating_2": rating_2,
            "Preference": preference,
            "Preference_Reason": preference_reason,
        }
        df = pd.DataFrame([data])

        # Check if the survey file exists and append data
        if os.path.exists(survey_file):
            existing_data = pd.read_csv(survey_file)
            df = pd.concat([existing_data, df], ignore_index=True)

        # Save the updated data to CSV
        df.to_csv(survey_file, index=False)

        # Mark the session as voted
        st.session_state["voted"] = True
        st.success("Your response has been recorded!")
