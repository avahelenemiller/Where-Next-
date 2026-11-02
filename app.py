import streamlit as st
from where_next import destinations

st.set_page_config(
    page_title="Where Next?",
    page_icon="✈️",
    layout="centered"
)

st.markdown("""
<style>
/* Discover button */
.stButton > button {
    background-color: #17324D 
    color: white 
    font-weight: 700 
    border: none 
}

.stButton > button p {
    color: white 
}

/* Whole page */
.stApp {
    background-color: #F7F5F0;
}

/* Main content area */
.block-container {
    max-width: 900px;
    padding-top: 3rem;
    padding-bottom: 4rem;
}

/* Main title */
h1 {
    font-size: 58px 
    font-weight: 800 
    letter-spacing: -2px;
    color: #17324D;
}

/* Headings */
h2, h3 {
    color: #17324D;
}

/* Normal text */
p, label {
    color: #334E68 
}

/* Dropdown boxes */
div[data-baseweb="select"] > div {
    background-color: white;
    border-radius: 14px;
    border: 1px solid #D9E2EC;
}

/* Find destination button */
.stButton > button {
    background-color: #17324D;
    color: white;
    border: none;
    border-radius: 14px;
    padding: 0.8rem 1.8rem;
    font-size: 18px;
    font-weight: 600;
}

.stButton > button:hover {
    background-color: #244F73;
    color: white;
    border: none;
}

/* Result success box */
div[data-testid="stAlert"] {
    border-radius: 16px;
}
.stButton > button {
    background-color: #17324D 
    color: #FFFFFF 
    font-weight: 700 
}

.stButton > button p {
    color: #FFFFFF 
}

</style>
""", unsafe_allow_html=True)

st.title("✈️ Where Next?")
st.write("Find your perfect travel destination")

st.subheader("Tell us about your ideal holiday")

budget = st.selectbox(
    "What's your budget?",
    ["Budget", "Mid", "Luxury"]
)

climate = st.selectbox(
    "What climate do you prefer?",
    ["Warm", "Temperate", "Cool"]
)

holiday_type = st.selectbox(
    "What kind of holiday do you want?",
    ["Relaxing", "City", "Adventure"]
)

activities = st.multiselect(
    "What activities do you enjoy?",
    [
        "Swimming",
        "Surfing",
        "Walking",
        "Shopping",
        "Food",
        "Culture",
        "Hiking",
        "Skiing",
        "Nature",
        "Snorkelling",
        "Beach",
        "Sightseeing"
    ]
)
if st.button("Discover My Destination!"):

    best_destination = None
    best_score = -1

    for destination in destinations:
        score = 0

        if budget.lower() == destination["budget"]:
            score += 1

        if climate.lower() == destination["climate"]:
            score += 1

        if holiday_type.lower() == destination["holiday_type"]:
            score += 1

        for activity in activities:
            if activity.lower() in destination["activities"]:
                score += 1

        if score > best_score:
            best_score = score
            best_destination = destination

    st.success(f"🌍 Your best match is {best_destination['name']}!")
    st.write(f"⭐ You matched {best_score} preferences.")
    st.subheader("Why this destination suits you")

    st.write(f"💰 Budget: {best_destination['budget'].title()}")
    st.write(f"☀️ Climate: {best_destination['climate'].title()}")
    st.write(f"🏝️ Holiday style: {best_destination['holiday_type'].title()}")
    st.write(f"🎯 Activities: {', '.join(best_destination['activities']).title()}")

