async function sendCode() {
    const code = document.getElementById("codeInput").value;
    const resultBox = document.getElementById("result");
    resultBox.textContent = "Analyzing code...";

    const response = await fetch("http://127.0.0.1:8000/explain", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ code: code })
    });

    const data = await response.json();
    resultBox.textContent = data.result;
}
