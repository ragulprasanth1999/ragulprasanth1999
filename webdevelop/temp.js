function convert() {
    // Get the input value
    const inputValue = parseFloat(document.getElementById("input1").value);

    // Get the selected conversion type
    const toFahrenheit = document.getElementById("tofarenheat").checked;
    
    // Convert temperature based on selected type
    let result;
    if (toFahrenheit) {
        // Convert Celsius to Fahrenheit
        result = (inputValue * 9/5) + 32;
    } else {
        // Convert Fahrenheit to Celsius
        result = (inputValue - 32) * 5/9;
    }

    // Display the result
    document.getElementById("result").innerText = result.toFixed(2);
}
