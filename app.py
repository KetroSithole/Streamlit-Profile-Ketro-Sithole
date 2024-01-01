import streamlit as st

# Set page title and icon
st.set_page_config(
    page_title="Ketro Sithole - BI Analyst Portfolio",
    page_icon=":bar_chart:",
)

# Sidebar with user information
st.sidebar.title("Ketro Sithole")
st.sidebar.subheader("Data Commons Research Assistant & Business Intelligence Professional")
st.sidebar.info(
    "Proven Track Record | Six-time Hackathon Winner | Top 15 South African Young Geeks 2023\n"
    "1st Place - Final Year IT Project, University of Pretoria"
)

# Navigation
menu = ["Home", "Projects", "About"]
choice = st.sidebar.selectbox("Menu", menu)

# Home page
if choice == "Home":
    st.title("Welcome to My BI Analyst Portfolio")
    st.write(
        "I am passionate about transforming data into actionable insights. Explore my projects and expertise below."
    )

# Projects page
elif choice == "Projects":
    st.title("My Projects")
    st.subheader("1. Sales Forecasting Dashboard")
    st.write(
        "Developed an interactive dashboard using Power BI to analyze sales trends and forecast future sales."
    )

    st.subheader("2. Sentiment Analysis of Customer Feedback")
    st.write(
        "Used Natural Language Processing (NLP) techniques to analyze customer feedback and determine sentiment scores."
    )

    # Add more projects as needed

# About page
elif choice == "About":
    st.title("About Me")
    st.write(
        "Data Commons Research Assistant & Business Intelligence Professional with a proven track record of innovation and problem-solving. "
        "I am a six-time Hackathon winner and recognized as one of the Top 15 South African Young Geeks in 2023. "
        "I achieved 1st Place in the Final Year IT Project during my degree at the University of Pretoria."
    )

    st.subheader("Education")
    st.write("- Degree: Computer Science & Information Sciences")
    st.write("- University: University of Pretoria")

    st.subheader("Interests")
    st.write("- Cloud Computing")
    st.write("- Artificial Intelligence")
    st.write("- E-learning")

    st.subheader("Connect with Me")
    st.write("[GitHub](https://github.com/KetroSithole)")
    st.write("[LinkedIn](https://www.linkedin.com/in/ketro-sithole-76b8b1165/)")

# Add more sections/pages as needed

# Footer
st.sidebar.markdown(
    """
    **Connect with Me:**
    [LinkedIn](https://www.linkedin.com/in/ketro-sithole-76b8b1165/) | [GitHub](https://github.com/KetroSithole)
    """
)
