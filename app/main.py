from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = pickle.load(open("models/model.pkl", "rb"))
le_edu = pickle.load(open("models/le_edu.pkl", "rb"))
le_interest = pickle.load(open("models/le_interest.pkl", "rb"))
le_diff = pickle.load(open("models/le_diff.pkl", "rb"))
le_output = pickle.load(open("models/le_output.pkl", "rb"))

def map_inputs(interest, level, goal):
    if level == "Beginner":
        exp, math, logic = 0, 4, 5
    elif level == "Intermediate":
        exp, math, logic = 1, 6, 7
    else:
        exp, math, logic = 3, 8, 9

    if goal == "Competitive":
        ps = 85
    elif goal == "Job":
        ps = 70
    else:
        ps = 60

    return exp, math, logic, ps

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/predict")
def predict(interest: str, level: str, goal: str):

    exp, math, logic, ps = map_inputs(interest, level, goal)

    edu_enc = le_edu.transform([level])[0]
    int_enc = le_interest.transform([interest])[0]
    diff_enc = le_diff.transform(["Medium"])[0]

    features = pd.DataFrame([{
        "Age": 20,
        "Education": edu_enc,
        "Math_Skill": math,
        "Logic_Skill": logic,
        "Experience": exp,
        "Interest": int_enc,
        "Problem_Solving": ps,
        "Difficulty": diff_enc
    }])

    probs = model.predict_proba(features)[0]
    top_indices = probs.argsort()[-2:][::-1]

    top_languages = le_output.inverse_transform(top_indices)
    top_scores = probs[top_indices] * 100

    return {
        "top_1": {"language": top_languages[0], "confidence": round(top_scores[0], 2)},
        "top_2": {"language": top_languages[1], "confidence": round(top_scores[1], 2)}
    }