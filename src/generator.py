import random
import pandas as pd

def generate_data(n=300):
    data = []

    for _ in range(n):
        age = random.randint(18, 25)
        education = random.choice(["Beginner", "Intermediate", "Advanced"])
        math_skill = random.randint(1, 10)
        logic_skill = random.randint(1, 10)
        experience = random.randint(0, 3)
        interest = random.choice(["Web", "AI", "App", "Competitive"])
        problem_solving = random.randint(40, 100)
        difficulty = random.choice(["Easy", "Medium", "Hard"])

        score = {
            "Python": 0,
            "JavaScript": 0,
            "Java": 0,
            "C++": 0
        }

        if interest == "AI":
            score["Python"] += 3
        if interest == "Web":
            score["JavaScript"] += 3
        if interest == "App":
            score["Java"] += 3
        if interest == "Competitive":
            score["C++"] += 3

        score["Python"] += (logic_skill + problem_solving) / 20
        score["C++"] += (math_skill + logic_skill) / 15
        score["JavaScript"] += experience / 2
        score["Java"] += experience / 2

        recommended = max(score, key=score.get)

        data.append([
            age, education, math_skill, logic_skill,
            experience, interest, problem_solving,
            difficulty, recommended
        ])

    columns = [
        "Age", "Education", "Math_Skill", "Logic_Skill",
        "Experience", "Interest", "Problem_Solving",
        "Difficulty", "Recommended_Language"
    ]

    df = pd.DataFrame(data, columns=columns)
    df.to_csv("data/dataset.csv", index=False)

    print("✅ Dataset generated successfully!")

if __name__ == "__main__":
    generate_data()