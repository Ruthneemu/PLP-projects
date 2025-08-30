/************** PART 1: Variables and Conditionals **************/

// Variable declarations
let age = 20;
let name = "Alice";

// Conditional example
if (age >= 18) {
    document.getElementById("conditional-output").textContent = name + " is an adult.";
} else {
    document.getElementById("conditional-output").textContent = name + " is a minor.";
}

/************** PART 2: Functions **************/

// Function 1: Greeting function
function greetUser(userName) {
    return "Hello, " + userName + "!";
}

document.getElementById("greet-btn").addEventListener("click", function() {
    let greeting = greetUser(name);
    document.getElementById("greet-output").textContent = greeting;
});

// Function 2: Sum of two numbers
function sumNumbers(a, b) {
    return a + b;
}

document.getElementById("sum-btn").addEventListener("click", function() {
    let total = sumNumbers(5, 10);
    document.getElementById("sum-output").textContent = "5 + 10 = " + total;
});

/************** PART 3: Loops **************/

// Loop 1: for loop iterating over an array
let fruits = ["Apple", "Banana", "Mango"];
let fruitsList = document.getElementById("fruits-list");
for (let i = 0; i < fruits.length; i++) {
    let li = document.createElement("li");
    li.textContent = fruits[i];
    fruitsList.appendChild(li);
}

// Loop 2: while loop counting numbers
let numbersList = document.getElementById("numbers-list");
let count = 1;
while (count <= 5) {
    let li = document.createElement("li");
    li.textContent = "Number " + count;
    numbersList.appendChild(li);
    count++;
}

/************** PART 4: DOM Interactions **************/

// Interaction 1: Update text based on input
document.getElementById("update-btn").addEventListener("click", function() {
    let input = document.getElementById("user-input").value;
    document.getElementById("dom-output").textContent = input;
});

// Interaction 2: Change background color dynamically
document.getElementById("user-input").addEventListener("input", function() {
    document.body.style.backgroundColor = "#f0f0f0";
});

// Interaction 3: Toggle a class on click
document.getElementById("greet-btn").addEventListener("click", function() {
    document.getElementById("greet-output").classList.toggle("highlight");
});
