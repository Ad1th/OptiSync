async function getPrediction() {
    document.getElementById("predictionResult").innerText = "Calculating... Please wait.";

    let inputData = {
        Power_Consumption_kW: parseFloat(document.getElementById("power").value),
        Machines: parseInt(document.getElementById("machines").value),
        Num_Employees: parseInt(document.getElementById("employees").value),
        Timestamp: parseFloat(document.getElementById("timestamp").value),
        Mill_Size_Medium: document.getElementById("mill_medium").checked,
        Mill_Size_Small: document.getElementById("mill_small").checked,
        Mill_Size_Large: document.getElementById("mill_large").checked,
        Location_Ankleshwar: document.getElementById("ankleshwar").checked,
        Location_Silvassa: document.getElementById("silvassa").checked,
        Location_Surat: document.getElementById("surat").checked,
        Location_Vapi: document.getElementById("vapi").checked
    };

    console.log("Sending data to API:", inputData);  // ✅ Debugging log

    try {
        let response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST", // ✅ Ensure this is POST
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(inputData)
        });

        console.log("Response status:", response.status);  // ✅ Debugging log

        let result = await response.json();
        console.log(result.prediction);
        if (result.error) {
            document.getElementById("predictionResult").innerText = `❌ Error: ${result.error}`;
        } else {
            document.getElementById("predictionResult").innerText =
                "Predicted Bill Amount: ₹" + result.prediction;
        }
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("predictionResult").innerText = "❌ Error fetching prediction.";
    }
}