const submitBtn = document.getElementById("submit");
const resultDiv = document.getElementById("result");

submitBtn.addEventListener("click", async () => {
    const goal = document.getElementById("goal").value;
    if (!goal) return alert("Please enter a goal");

    resultDiv.textContent = "Processing...";

    try {
        const res = await fetch("http://localhost:5000/api/goal", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ goal })
        });
        const data = await res.json();
        if (data.result) {
            resultDiv.textContent = data.result;
        } else if (data.error) {
            resultDiv.textContent = "Error: " + data.error;
        }
    } catch (err) {
        resultDiv.textContent = "Error connecting to agent API: " + err;
    }
});
