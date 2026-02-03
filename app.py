import streamlit as st

# ---------------- Page Configuration ----------------
st.set_page_config(
    page_title="Bonolo Angele Rentsi Profile | CSS 2026",
    page_icon="🧠",
    layout="wide"
)

# ---------------- Sidebar ----------------
st.sidebar.title("🔍 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "About Me",
        "Research Interests",
        "Research Projects",
        "Publications & Reviews",
        "Skills & Tools",
        "Contact"
    ]
)

# ---------------- Header ----------------
st.markdown(
    """
    <h1 style='text-align: center; color: #D62828;'>Researcher Profile</h1>
    <h3 style='text-align: center;'>Data Science • Machine Learning • AI Research</h3>
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
        I am a **Data Science researcher** with experience in **machine learning, deep learning,
        explainable AI (XAI), and applied AI systems**.

        My work focuses on solving real-world problems using data-driven and ethical AI approaches,
        particularly in **healthcare, recommender systems, and speech analytics**.
        """
    )

    st.info(
        "This Streamlit app was created for the **CSS 2026 Streamlit Cloud assignment**."
    )

# ---------------- About Me ----------------
elif section == "About Me":
    st.subheader("👨‍🎓 About Me")

    st.write(
        """
        I am a data science researcher with hands-on experience in building, training,
        and evaluating machine learning and deep learning models.
        I have worked extensively on **medical image analysis**, **audio-based emotion detection**,
        and **recommendation systems**.

        My academic work emphasizes **model performance, interpretability, fairness, and real-world applicability**.
        """
    )

# ---------------- Research Interests ----------------
elif section == "Research Interests":
    st.subheader("🔬 Research Interests")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            - AI for Healthcare & Disease Detection  
            - Deep Learning (CNNs, RNNs, LSTM, GRU, Vision Transformers)  
            - Medical Image Analysis  
            - Speech & Audio Signal Processing  
            """
        )

    with col2:
        st.markdown(
            """
            - Explainable AI (Grad-CAM, LIME, SHAP)  
            - Fairness & Bias Mitigation in AI  
            - Federated Learning  
            - Model Optimization & Transfer Learning  
            """
        )

# ---------------- Research Projects ----------------
elif section == "Research Projects":
    st.subheader("🧪 Research & Academic Projects")

    st.markdown(
        """
        **🔹 Monkeypox Detection Using Deep Learning**  
        Conducted an in-depth comparative study using CNNs, Vision Transformers,
        and transfer learning models on multiple Monkeypox datasets.
        Applied explainability techniques such as **Grad-CAM and LIME**, and explored
        fairness, mobile optimization, and federated learning.

        **🔹 Pneumonia Detection Using AI Systems**  
        Studied AI-driven approaches for detecting pneumonia using medical data,
        focusing on accuracy, robustness, and clinical relevance.

        **🔹 Emotion Detection from Speech**  
        Built emotion recognition systems using **LSTM, GRU, and CNN-RNN hybrid models**.
        Applied audio data augmentation and extracted features such as **MFCC, chroma,
        delta, and prosodic features**.

        **🔹 Recommendation Systems**  
        Developed content-based, collaborative, and hybrid recommendation systems
        using real-world datasets (movies, products, and drug reviews).

        **🔹 ETL & Data Analytics Pipelines**  
        Designed ETL pipelines using Python, Pandas, and SQLite to clean, transform,
        and analyze large datasets, including Slurm-based data processing workflows.
        """
    )

# ---------------- Publications & Reviews ----------------
elif section == "Publications & Reviews":
    st.subheader("📚 Publications & Literature Reviews")

    st.write(
        """
        - Literature Review on **Optimization for Online Learning**
        - Comprehensive Review of **Deep Learning Approaches for Monkeypox Detection**
        - Comparative Analysis of CNNs vs Vision Transformers in Medical Imaging
        - Review of Explainable AI Techniques for Healthcare Applications
        """
    )

    st.warning("Some works are part of ongoing or academic submissions.")

# ---------------- Skills & Tools ----------------
elif section == "Skills & Tools":
    st.subheader("🛠️ Skills & Tools")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            **Programming & Data**
            - Python  
            - Pandas, NumPy  
            - SQL, SQLite  

            **Machine Learning**
            - Scikit-learn  
            - Model Evaluation & Metrics  
            - Imbalanced Data Handling  
            """
        )

    with col2:
        st.markdown(
            """
            **Deep Learning & AI**
            - TensorFlow, Keras  
            - CNNs, RNNs, LSTM, GRU  
            - Vision Transformers  

            **Deployment & Visualization**
            - Streamlit, Flask  
            - Matplotlib, Seaborn  
            - Model Explainability (XAI)  
            """
        )

# ---------------- Contact ----------------
elif section == "Contact":
    st.subheader("📬 Contact Information")

    st.markdown(
        """
        📧 **Email:** 202219880@spu.ac.za 
        📱 **Phone:** +27 75 460 5318 
        📍 **Location:** Kimberley, South Africa  
        """
    )

    st.success(
        "Open to research collaboration, academic discussions, and data science projects."
    )

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
