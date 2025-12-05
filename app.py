import streamlit as st
from data_loaders import load_udemy
from recommender import CourseRecommender

st.set_page_config(page_title="Udemy Course Recommender", layout="wide")
st.title("🎓 Udemy Course Recommendation System")
st.write("AI-powered search using your Udemy dataset.")

# Load Udemy courses
@st.cache_data
def load_data():
    return load_udemy("D:/course_recommendation/udemy_courses.csv")

df = load_data()
recommender = CourseRecommender(df)

query = st.text_input("Enter skill or topic (e.g., Python, ML, Web Development):")
top_n = st.slider("Number of recommendations:", 1, 20, 5)

if st.button("Recommend"):
    if not query.strip():
        st.warning("Please enter a keyword or skill!")
    else:
        results = recommender.recommend(query, top_n)

        st.subheader(f"Top {top_n} Course Recommendations:")
        for i, row in results.reset_index(drop=True).iterrows():
            st.markdown(f"### {i+1}. {row['course_title']}")
            st.write(row['course_description'])

            st.write(f"**Difficulty:** {row['difficulty']}")
            st.write(f"**Reviews:** {row['reviews']}")   # Updated

            st.markdown(f"[🔗 View Course]({row['course_url']})")
            st.markdown("---")

