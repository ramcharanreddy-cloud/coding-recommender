import pickle

# 🔷 Load model + encoders
model = pickle.load(open("models/model.pkl", "rb"))
le_edu = pickle.load(open("models/le_edu.pkl", "rb"))
le_interest = pickle.load(open("models/le_interest.pkl", "rb"))
le_diff = pickle.load(open("models/le_diff.pkl", "rb"))
le_output = pickle.load(open("models/le_output.pkl", "rb"))


# 🔷 Smart User Input (Simple UX)
def get_user_input():
    print("=== Coding Recommendation System ===")
    interest = input("Interest (Web/AI/App/Competitive): ").capitalize()
    level = input("Skill Level (Beginner/Intermediate/Advanced): ").capitalize()
    goal = input("Goal (Job/Learning/Competitive): ").capitalize()
    return interest, level, goal


# 🔷 Convert simple input → full features
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


# 🔷 Prediction flow
def predict():
    interest, level, goal = get_user_input()

    exp, math, logic, ps = map_inputs(interest, level, goal)

    # Encode
    edu_enc = le_edu.transform([level])[0]
    int_enc = le_interest.transform([interest])[0]
    diff_enc = le_diff.transform(["Medium"])[0]

    # Feature order MUST match training
    features = [[20, edu_enc, math, logic, exp, int_enc, ps, diff_enc]]

    # Predict
    prediction = model.predict(features)
    result = le_output.inverse_transform(prediction)[0]

    print("\n🔥 Recommended Language:", result)


if __name__ == "__main__":
    predict()