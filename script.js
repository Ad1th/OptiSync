// Declare Supabase variable
let supabase = null;

// Function to initialize Supabase dynamically
function initializeSupabase() {
  if (!supabase) {
    const supabaseUrl = "https://jtixnghmborsqjtfxljd.supabase.co"; // Replace with your Supabase URL
    const supabaseAnonKey =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imp0aXhuZ2htYm9yc3FqdGZ4bGpkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Mzg1NzkyOTQsImV4cCI6MjA1NDE1NTI5NH0.RqjJXgh5khmPH8wktQ6DIMJWW5czjPVJmog2F4KB5fk"; // Replace with your Supabase Anon Key

    // Ensure the global `supabase` object from the CDN is available
    if (window.supabase) {
      supabase = window.supabase.createClient(supabaseUrl, supabaseAnonKey);
      console.log("Supabase client initialized:", supabase);
    } else {
      console.error("Supabase library not loaded!");
      alert("Failed to load Supabase. Please check your setup.");
    }
  }
}

// Function to log in with Google OAuth
async function loginWithGoogle() {
  initializeSupabase(); // Ensure Supabase is initialized before usage

  try {
    const { data, error } = await supabase.auth.signInWithOAuth({
      provider: "google",
      options: {
        queryParams: {
          access_type: "offline", // Request offline access for refresh tokens
          prompt: "consent", // Force user consent every time
        },
      },
    });

    if (error) {
      console.error("Login failed:", error.message);
      alert("Login failed. Please try again.");
      return;
    }

    console.log("Login successful:", data);
    alert("Login successful! Redirecting...");
    // Redirect user after successful login (optional)
    window.location.href = "index2.html"; // Replace with your desired page
  } catch (err) {
    console.error("Error during Google login:", err);
  }
}

// Function to log out
async function logOut() {
  initializeSupabase(); // Ensure Supabase is initialized before usage

  try {
    const { error } = await supabase.auth.signOut();
    if (error) {
      console.error("Logout failed:", error.message);
      alert("Logout failed. Please try again.");
      return;
    }
    alert("You have been logged out.");
  } catch (err) {
    console.error("Error during logout:", err);
  }
}

// Event listener for the "Sign in" button
document.querySelector(".signin").addEventListener("click", async function () {
  console.log("Sign-in button clicked");
  await loginWithGoogle();
});

document.addEventListener("DOMContentLoaded", () => {
  const submitButton = document.querySelector(".submitButton");
  if (!submitButton) return console.error("Submit button not found!");

  submitButton.addEventListener("click", async (event) => {
    event.preventDefault();
    console.log("Submit button clicked!");

    // Capture input values
    const data = {
      powerConsumption: document.querySelector(".input1")?.value.trim(),
      millSize: document.querySelector(".input2")?.value.trim(),
      numberOfMachines: document.querySelector("#textBox")?.value.trim(),
      numberOfEmployees: document.querySelector(".input3")?.value.trim(),
      location: document.querySelector(".input4")?.value.trim(),
      machineDescription: document.querySelector(".input5")?.value.trim(),
    };

    // Check if any field is empty
    if (Object.values(data).some((value) => !value)) {
      return alert("Please fill in all fields before submitting.");
    }

    console.log("Submitting data:", data);

    try {
      const response = await fetch("http://127.0.0.1:5000/api", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });

      if (!response.ok) throw new Error(`Server error: ${response.status}`);

      const result = await response.json();
      console.log("Server response:", result);
      document.getElementById("reversedText").innerText = result.message;
    } catch (error) {
      console.error("Error submitting data:", error);
      alert("An error occurred. Please try again.");
    }
  });
});

// Event listener for the "Energy Insights" button
let btn = document.querySelector(".energy");
btn.addEventListener("click", function () {
  if (window.location.pathname.includes("index.html")) {
    window.location.href = "insights.html";
  }
});

let btn2 = document.querySelector(".aboutus");
btn2.addEventListener("click", function () {
  // if (window.location.pathname.includes("index.html")) {
  //   window.location.href = "aboutus.html";
  // }
  window.location.href = "aboutus.html";
});
let btn3 = document.querySelector(".calc");
btn3.addEventListener("click", function () {
  // if (window.location.pathname.includes("index.html")) {
  //   window.location.href = "aboutus.html";
  // }
  window.location.href = "insights.html";
});
let btn4 = document.querySelector(".robots");
btn4.addEventListener("click", function () {
  // if (window.location.pathname.includes("index.html")) {
  //   window.location.href = "aboutus.html";
  // }
  window.location.href = "metrics.html";
});
let btn5 = document.querySelector(".logout");
btn5.addEventListener("click", function () {
  // if (window.location.pathname.includes("index.html")) {
  //   window.location.href = "aboutus.html";
  // }
  window.location.href = "index.html";
});
////////////////////////////////////////////////////////////////////////

// Select solution buttons, solution containers, and overlay
const solnbtn = document.querySelector(".soln");
const solbar = document.querySelector(".solution-inner");
const overlay = document.querySelector(".overlay");
const resource = document.querySelector(".resource");
const resbtn = document.querySelector(".entrp");

// Toggle solution container visibility

// Hide the solution container and overlay when clicking outside

solnbtn.addEventListener("click", (event) => {
  event.stopPropagation(); // Prevent immediate closing
  solbar.classList.toggle("visible");
});

// Hide solbar when clicking outside
document.addEventListener("click", (event) => {
  if (!solbar.contains(event.target) && !solnbtn.contains(event.target)) {
    solbar.classList.remove("visible");
  }
});

resbtn.addEventListener("click", (event) => {
  event.stopPropagation(); // Prevent immediate closing
  resource.classList.toggle("visible");
});

// Hide solbar when clicking outside
document.addEventListener("click", (event) => {
  if (!solbar.contains(event.target) && !solnbtn.contains(event.target)) {
    solbar.classList.remove("visible");
  }
});
document.addEventListener("click", (event) => {
  if (!resource.contains(event.target) && !resbtn.contains(event.target)) {
    resource.classList.remove("visible");
  }
});

// Typing animation
const textElement = document.querySelector(".text-overlay");

// Split the text where you want a line break
const fullText = "Revolutionizing Energy,\nOne Watt at a Time";
const textArray = fullText.split("\n"); // Splitting into two lines

let lineIndex = 0; // Track which line is being typed
let charIndex = 0; // Track character index

function typeWriter() {
  if (charIndex < textArray[lineIndex].length) {
    textElement.innerHTML += textArray[lineIndex].charAt(charIndex); // Add characters one by one
    charIndex++;
    setTimeout(typeWriter, 100);
  } else {
    // Move to next line after a small delay
    if (lineIndex < textArray.length - 1) {
      setTimeout(() => {
        textElement.innerHTML += "<br>"; // Insert line break
        lineIndex++;
        charIndex = 0;
        typeWriter();
      }, 500); // Delay before typing next line
    }
  }
}

// Function to restart typing animation properly
function restartTyping() {
  textElement.innerHTML = ""; // Clear text *before* restarting
  lineIndex = 0;
  charIndex = 0;
  typeWriter();
}

// Start typing animation when the page loads
window.onload = function () {
  textElement.innerHTML = ""; // Ensure text is cleared when the page loads
  typeWriter();
  setInterval(restartTyping, fullText.length * 100 + 2000); // Restart animation properly
};
