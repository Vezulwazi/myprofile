import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Denzel Muwanazi | Research & Data Profile",
    page_icon="🔭",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("🔍 Navigation")
section = st.sidebar.radio(
    "Go to",
    [
        "Profile",
        "Publications",
        "Projects",
        "Research Analytics",
        "STEM Data",
        "Contact"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("**Field:** Physics | Data Science")
st.sidebar.markdown("**Institution:** North-West University")
st.sidebar.markdown("🔭 Astrophysics • Data • Security & Governance")

# ---------------- PROFILE ----------------
if section == "Profile":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("Profile Photo")
        uploaded_photo = st.file_uploader(
            "Upload your profile photo",
            type=["jpg", "jpeg", "png"]
        )

        if uploaded_photo:
            st.image(
                uploaded_photo,
                caption="Denzel Muwanazi",
                use_column_width=True
            )
        else:
            st.info("Upload a profile photo to display it here.")

    with col2:
        st.title("Denzel Muwanazi")
        st.subheader("Physics • Data Analysis • Research Governance")

        st.markdown("""
        **BSc Physics and Computer Science graduate** and **BSc Honours Physics graduate**
        from **North-West University**, with **planned MSc Physics studies starting in 2026**.

        I have a strong foundation in **data analysis, programming, and research governance**,
        with a growing interest in **cybersecurity, data privacy, and risk management**.
        I am experienced in handling **sensitive datasets**, building **analytical tools in Python**,
        and operating within **structured, compliance-driven environments**.
        """)

    st.markdown("---")

    m1, m2, m3 = st.columns(3)
    m1.metric("Education Level", "Honours Physics")
    m2.metric("Planned MSc", "2026")
    m3.metric("Core Focus", "Data & Research")

    st.markdown("### 🎓 Education")
    st.markdown("""
    - **BSc Honours in Physics** – North-West University (2025)  
    - **BSc in Physics & Computer Science** – North-West University (2024)  
    - **Planned MSc in Physics (2026)** – North-West University  
    """)

    st.markdown("### 🛠 Technical Skills")
    st.markdown("""
    **Programming & Data**  
    - Python (data analysis, automation, scripting)  
    - SQL (basic querying and data handling)  
    - Data cleaning, validation, and reporting  

    **Data Visualisation & Tools**  
    - Microsoft Excel (advanced formulas, analysis)  
    - Power BI (basic dashboards and reporting)  
    - Microsoft 365 (Word, PowerPoint, Teams)  

    **Security & Governance Exposure**  
    - Data privacy principles  
    - Risk identification and mitigation  
    - Audit-style documentation  
    - Role-based access and least-privilege concepts  
    """)

# ---------------- PUBLICATIONS ----------------
elif section == "Publications":

    st.header("📄 Research & Publications")

    st.subheader("Honours Research Project")
    st.markdown("""
    **Title:** Astrophysical Data Analysis of Star Clusters  
    **Supervisor:** Prof. Markus Böttcher – North-West University  

    **Research Summary:**  
    This project focused on analysing astronomical observational datasets using Python.
    The study involved cleaning, validating, and statistically analysing photometric data
    from star clusters to determine cluster properties such as age, distance, and stellar
    distributions. Strict data integrity and documentation practices were applied throughout
    the research to ensure reproducibility and compliance with academic research standards.

    **Key Contributions:**
    - Developed Python scripts for automated data cleaning and validation
    - Generated colour-magnitude diagrams (CMDs) and performed isochrone fitting
    - Analysed stellar population distributions
    - Produced structured research documentation and reporting
    """)

    st.subheader("Conference & Report Outputs")
    st.markdown("""
    - Honours Research Dissertation (2025)
    - Internal departmental research presentations
    """)

# ---------------- PROJECTS ----------------
elif section == "Projects":

    st.header("🧪 Academic & Technical Projects")

    st.markdown("""
    ### Astrophysics Data Analysis Project
    - Processed large observational datasets using Python
    - Applied statistical modelling techniques
    - Performed error analysis and uncertainty estimation
    - Generated professional scientific reports

    ### Python-Based Application / Chatbot Project
    - Built a Python application using NLP libraries
    - Designed logical control flows for structured conversations
    - Implemented data validation and logging
    - Produced technical documentation

    ### Research Data Governance Project
    - Implemented structured data management workflows
    - Ensured compliance with academic data governance standards
    - Developed reporting frameworks

    ### Personal Data Science Portfolio
    - Data analysis dashboards using Streamlit
    - Python automation tools
    - Statistical modelling notebooks
    """)

# ---------------- ANALYTICS ----------------
elif section == "Research Analytics":

    st.header("📊 Research Output Trends")

    years = np.arange(2019, 2026)
    outputs = np.random.randint(1, 6, len(years))

    chart = pd.DataFrame({
        "Year": years,
        "Outputs": outputs
    }).set_index("Year")

    st.line_chart(chart)

# ---------------- STEM DATA ----------------
elif section == "STEM Data":

    st.header("🧪 STEM Data Explorer")

    physics = pd.DataFrame({
        "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study"],
        "Energy (MeV)": [4.2, 1.5, 2.9, 3.4]
    })

    st.dataframe(physics, use_container_width=True)
    st.bar_chart(physics.set_index("Experiment"))

# ---------------- CONTACT ----------------
elif section == "Contact":

    st.header("📬 Contact & Links")

    st.markdown("""
    **📧 Email:** denzel.muwanazi@gmail.com  
    **🔗 LinkedIn:** https://www.linkedin.com/in/denzel-muwanazi  
    **💻 GitHub:** https://github.com/vezulwazi  
    **📍 Location:** South Africa  
    """)

    st.success("Open to MSc / PhD pathways, graduate programmes, and research collaborations.")
