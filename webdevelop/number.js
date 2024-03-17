const max = 100;
const min = 1;
const answer = Math.floor(Math.random() * (max - min + 1)) + min;
let attempt = 0;
let running = true;
let guess;

while (running) {
    guess = window.prompt(`Enter a number between ${min} and ${max}`);
    guess = Number(guess);

    if (isNaN(guess)) {
        window.alert("Please enter a valid number.");
    } else if (guess > max || guess < min) {
        window.alert(`Please enter a number between ${min} and ${max}.`);
    } else {
        attempt += 1;

        if (answer > guess) {
            window.alert("You entered a lower value.");
        } else if (answer < guess) {
            window.alert("You entered a higher value.");
        } else {
            window.alert(`You entered the correct value with ${attempt} attempts.`);
            running = false;
        }
    }
}
