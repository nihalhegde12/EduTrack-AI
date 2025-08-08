import streamlit as st
from utils.resume_parser import extract_text_from_pdf, extract_skills
from utils.course_recommender import recommend_courses, recommend_internships

st.set_page_config(page_title="EduTrack AI", layout="wide")
st.title("🎓 EduTrack AI - Personalized Learning & Internship Recommender")

uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("🔍 Extracting information..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        skills = extract_skills(resume_text)

    st.subheader("🧠 Extracted Skills")
    if skills:
        st.write(", ".join(skills))
    else:
        st.write("No skills detected. Please enter manually.")

    st.subheader("🎯 Select Your Areas of Interest")
    interests = st.multiselect("Choose your interests", [
        "Data Science", "Web Development", "AI/ML", "Cybersecurity",
        "Cloud Computing", "Mobile App Development", "UI/UX Design", "Blockchain"
    ])

    if st.button("🚀 Get Recommendations"):
        all_keywords = list(set(skills + interests))

        if all_keywords:
            st.subheader("📘 Recommended Free Courses")
            course_links = recommend_courses(all_keywords)
            for course in course_links:
                st.markdown(f"✅ [{course['title']}]({course['link']})")

            st.subheader("🧑‍💻 Free Internship Opportunities")
            internships = recommend_internships(all_keywords)
            for intern in internships:
                st.markdown(f"🔗 [{intern['title']}]({intern['link']})")
        else:
            st.warning("Please upload a resume or select areas of interest.")
