function getIcon(lang) {
    if (lang === "Python") return "🐍";
    if (lang === "Java") return "☕";
    if (lang === "C++") return "💻";
    if (lang === "JavaScript") return "⚡";
    return "💡";
}

async function getData() {
    let interest = document.getElementById("interest").value;
    let level = document.getElementById("level").value;
    let goal = document.getElementById("goal").value;

    let url = `https://coding-recommender.onrender.com/predict?interest=${interest}&level=${level}&goal=${goal}`;

    document.getElementById("loading").style.display = "block";
    document.getElementById("result").style.display = "none";

    try {
        let res = await fetch(url);
        let data = await res.json();

        document.getElementById("loading").style.display = "none";
        document.getElementById("result").style.display = "block";

        document.getElementById("topResult").innerHTML =
            `${getIcon(data.top_1.language)} <b>${data.top_1.language}</b>
             <span class="badge">${data.top_1.confidence}%</span>`;

        document.getElementById("secondResult").innerHTML =
            `${getIcon(data.top_2.language)} ${data.top_2.language}
             <span class="badge">${data.top_2.confidence}%</span>`;

    } catch (error) {
        console.error(error);
        document.getElementById("loading").innerText = "❌ Error loading data";
    }
}