import streamlit as st
import pandas as pd
from data_fetcher import fetch_csv
from analytics import top_m_crops_for_state, compare_avg_rainfall

# Load CSV once
crop_df = fetch_csv(r"sample.csv")
rain_df = fetch_csv(r"sample.csv")  # Using same sample for rainfall

st.title("Crops & Climate Analytics for Indian States")

q = st.text_input("Ask a question about Crops & Climate in Indian states:")

# Normalize state names from CSV
all_states = [s.strip() for s in crop_df['State'].unique()]

if st.button("Run"):
    q_lower = q.lower()
    matched_states = []

    # Detect states in query
    for state in all_states:
        if state.lower() in q_lower:
            matched_states.append(state)

    # Remove duplicates
    matched_states = list(dict.fromkeys(matched_states))

    # Decide which states to compare
    if len(matched_states) >= 2:
        state_x, state_y = matched_states[0], matched_states[1]
    elif len(matched_states) == 1:
        state_x, state_y = matched_states[0], matched_states[0]
    else:
        st.write("Here is a sample analysis of the states.")
        state_x, state_y = "Haryana", "Tamil Nadu"

    # Use years present in the CSV
    years = crop_df['Year'].unique().tolist()

    # Compute top crops
    topx = top_m_crops_for_state(crop_df, state_x, years, m=3)
    topy = top_m_crops_for_state(crop_df, state_y, years, m=3)

    st.subheader(f"Top crops in {state_x}")
    st.dataframe(topx)

    st.subheader(f"Top crops in {state_y}")
    st.dataframe(topy)

    # Compute average rainfall
    avg_rainfall = compare_avg_rainfall(rain_df, [state_x, state_y], years)
    st.subheader("Average annual rainfall (mm)")
    st.write(avg_rainfall)

    # Show provenance
    st.subheader("Data provenance")
    st.write({
        "crop_dataset": "sample.csv",
        "rainfall_dataset": "sample.csv"
    })
