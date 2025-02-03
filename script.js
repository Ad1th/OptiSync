document.getElementById("submitButton").addEventListener("click", function () {
  const textValue = document.getElementById("textBox").value;
  fetch("http://localhost:8000/submit", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ text: textValue }),
  })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error("Error:", error));
});
/*
document.querySelector("energy").addEventListener("click", function () {
  if (window.location.pathname.includes("index.html")) {
    window.location.href = "insights.html";
  }
});
*/
let btn = document.querySelector(".energy");

btn.addEventListener("click", function () {
  if (window.location.pathname.includes("index.html")) {
    window.location.href = "insights.html";
  }
});
