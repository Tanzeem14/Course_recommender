import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CourseRecommender:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy().fillna("")

        # Combine text fields for recommendation
        self.df["combined"] = (
            self.df["course_title"].astype(str) + " " +
            self.df["course_description"].astype(str)
        )

        self._build_model()

    def _build_model(self):
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.matrix = self.vectorizer.fit_transform(self.df["combined"])
        self.similarity = cosine_similarity(self.matrix)

    def recommend(self, query: str, top_n: int = 10):
        q_vec = self.vectorizer.transform([query])
        sims = cosine_similarity(q_vec, self.matrix).flatten()

        ranked = sims.argsort()[::-1]
        results = self.df.iloc[ranked].copy()
        results["score"] = sims[ranked]

        return results.head(top_n)
