async function getPrediction() {
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

    try {
        let response = await fetch("http://localhost:8001/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(inputData)
        });

        let result = await response.json();
        document.getElementById("predictionResult").innerText = 
            "Predicted Bill Amount: " + result.prediction;
    } catch (error) {
        console.error("Error:", error);
        document.getElementById("predictionResult").innerText = "Error fetching prediction.";
    }
}
