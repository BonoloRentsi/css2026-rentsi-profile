import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Researcher Profile | CSS 2026",
    page_icon="📊",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("🔍 Navigation")
section = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Research Interests", "Projects", "Publications", "Contact"]
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style='text-align: center; color: #2C7BE5;'>Researcher Profile</h1>
    <h3 style='text-align: center;'>Data Science | Machine Learning | AI Research</h3>
    <hr>
    """,
    unsafe_allow_html=True
)

# ---------------- Home ----------------
if section == "Home":
    st.subheader("👋 Welcome")
    st.write(
        """
        Welcome to my researcher profile page.  
        This page showcases my academic background, research interests, 
        projects, and contributions in **Data Science, Machine Learning, and AI-driven systems**.
        """
    )

    st.info(
        "This Streamlit app was created as part of the **CSS 2026 Streamlit Cloud assignment**."
    )

# ---------------- About Me ----------------
elif section == "About Me":
    st.subheader("👨‍🎓 About Me")
    st.write(
        """
        I am a data science researcher with strong interests in applied machine learning,
        deep learning, and intelligent systems. My work focuses on developing
        data-driven solutions for real-world problems, particularly in healthcare,
        recommendation systems, and predictive analytics.
        """
    )

    st.markdown("**Skills:**")
    st.markdown(
        """
        - Python, Pandas, NumPy  
        - Machine Learning & Deep Learning  
        - Data Visualization  
        - ETL Pipelines  
        - Streamlit & Flask
        """
    )

# ---------------- Research Interests ----------------
elif section == "Research Interests":
    st.subheader("🔬 Research Interests")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            - Artificial Intelligence in Healthcare  
            - Explainable AI (XAI)  
            - Deep Learning (CNNs, RNNs, Transformers)  
            - Medical Image & Signal Analysis
            """
        )

    with col2:
        st.markdown(
            """
            - Recommendation Systems  
            - Data Ethics & Fairness  
            - Federated Learning  
            - Model Optimization
            """
        )

# ---------------- Projects ----------------
elif section == "Projects":
    st.subheader("🛠️ Selected Projects")

    st.markdown(
        """
        **🔹 Pneumonia Detection Using AI**  
        Developed deep learning models to detect pneumonia from medical data, 
        improving diagnostic accuracy.

        **🔹 Movie Recommendation System**  
        Built a hybrid recommendation system using collaborative and content-based filtering.

        **🔹 Emotion Detection from Audio**  
        Designed CNN-RNN models for speech emotion recognition using audio features.

        **🔹 ETL & Data Analytics Pipelines**  
        Created end-to-end data pipelines for cleaning, transforming, and analyzing large datasets.
        """
    )

# ---------------- Publications ----------------
elif section == "Publications":
    st.subheader("📚 Publications & Academic Work")

    st.write(
        """
        - Literature review on **Optimization for Online Learning**
        - Research analysis on **AI-driven disease detection systems**
        - Comparative studies on **Machine Learning and Deep Learning models**
        """
    )

    st.warning("Full publication list available upon request.")

# ---------------- Contact ----------------
elif section == "Contact":
    st.subheader("📬 Contact Information")

    st.markdown(
        """
        📧 **Email:** xabisomemani@example.com  
        📱 **Phone:** +27 00 000 0000  
        📍 **Location:** Johannesburg, South Africa
        """
    )

    st.success("Feel free to reach out for research collaboration or academic discussions.")

# ---------------- Footer ----------------
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px;'>
    © 2026 | Researcher Profile | Built with Streamlit
    </p>
    """,
    unsafe_allow_html=True
)
