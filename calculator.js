// Get input values from the user
const principal = parseFloat(document.getElementById("initial-investment").value);
const rate = parseFloat(document.getElementById("interest-rate").value);
const years = parseFloat(document.getElementById("investment-years").value);

// Calculate simple interest
const interest = (principal * rate * years) / 100;

// Display the result
const resultElement = document.getElementById("result");
resultElement.innerHTML = `The interest is $${interest.toFixed(2)}`;
