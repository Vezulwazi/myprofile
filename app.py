

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

        I am a strong communicator with proven ability to support **multiple projects**,
        document processes clearly, and collaborate effectively in **hybrid and remote teams**.
        """)

    st.markdown("---")

    m1, m2, m3 = st.columns(3)
    m1.metric("Education Level", "Honours Physics")
    m2.metric("Planned MSc", "2026")
    m3.metric("Core Focus", "Data & Research")

    # ---------------- EDUCATION ----------------
    st.markdown("### 🎓 Education")
    st.markdown("""
    - **BSc Honours in Physics** – North-West University  
    - **BSc in Physics & Computer Science** – North-West University  
    - **Planned MSc in Physics (2026)** – North-West University  
    """)

    # ---------------- TECHNICAL SKILLS ----------------
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
    - Data privacy principles (confidentiality, integrity, access control)
    - Risk identification and mitigation
    - Audit-style documentation and reporting
    - Role-based access and least-privilege concepts
    """)

    # ---------------- PROJECTS ----------------
    st.markdown("### 🧪 Academic & Technical Projects")

    st.markdown("""
    **Astrophysics Data Analysis Project**
    - Processed and analysed large observational datasets using Python
    - Applied strict data validation and integrity checks
    - Documented methodologies and results for academic review
    - Worked within ethical and governance frameworks for research data

    **Python-Based Application / Chatbot Project**
    - Developed a Python application to process structured user input
    - Implemented logical controls to manage data flow and usage
    - Produced technical documentation for maintainability
    - Collaborated in a feedback-driven development environment
    """)

    # ---------------- EXPERIENCE ----------------
    st.markdown("### 💼 Experience")

    st.markdown("""
    **Supplemental Instruction (SI) Facilitator – North-West University**
    - Delivered structured training sessions to diverse student groups
    - Communicated complex technical concepts clearly and effectively
    - Supported academic programs through reporting and coordination
    - Reinforced awareness of academic standards, policies, and compliance
    """)

    # ---------------- PROFESSIONAL SKILLS ----------------
    st.markdown("### 🤝 Professional Skills")

    st.markdown("""
    - Time management and prioritisation  
    - Stakeholder communication  
    - Documentation and reporting  
    - Remote and hybrid collaboration  
    - Process improvement mindset  
    - High attention to detail and integrity  
    """)

    # ---------------- ADDITIONAL INFO ----------------
    st.markdown("### ℹ️ Additional Information")

    st.markdown("""
    - South African Citizen  
    - Eligible for **2026 Graduate Programmes**  
    - Strong interest in **cybersecurity, data privacy, and risk management**  
    """)

# ---------------- PUBLICATIONS ----------------
elif section == "Publications":

    st.header("📄 Publications")
    uploaded_file = st.file_uploader("Upload Publications CSV", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No publications uploaded yet.")

# ---------------- PROJECTS ----------------
elif section == "Projects":

    st.header("🧪 Projects Overview")
    st.info("See detailed project descriptions in the Profile section.")

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