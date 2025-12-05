import pandas as pd

def load_udemy(csv_path="udemy_courses.csv"):
    df = pd.read_csv(csv_path)

    print("Loaded Udemy dataset:")
    # print(df.head())

    # Map columns to unified format
    df = df.rename(columns={
        "course_title": "course_title",
        "url": "course_url",
        "level": "difficulty",
        "subject": "subject"
    })

    # Udemy dataset has NO course description → we create one
    df["course_description"] = (
        df["course_title"] 
        + " teaches essential skills in " 
        + df["subject"] 
        + ". It covers practical concepts with hands-on examples."
    )

    df["reviews"] = df["num_reviews"]   # Use actual Udemy review count

    df["platform"] = "Udemy"

    df_final = df[[
        "platform",
        "course_title",
        "course_description",
        "difficulty",
        "reviews",
        "course_url"
    ]]

    return df_final
