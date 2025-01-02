function getRandomNumbers() {
    const numbers = [];
    while (numbers.length < 3) {
        const randomNum = Math.floor(Math.random() * 10);
        if (!numbers.includes(randomNum)) {
            numbers.push(randomNum);
        }
    }
    return numbers;
}

const answer = getRandomNumbers();
console.log("Answer:", answer);

let attemptsLeft = 9;

function attemptsDisplay() {
    const attemptsElement = document.getElementById("attempts");
    attemptsElement.textContent = attemptsLeft;
}

function playerInput() {
    const inputs = Array.from(document.querySelectorAll(".input-field"));
    const values = inputs.map(input => input.value.trim());
    if (values.some(value => value === "")) {
        return null;
    }
    return values.map(Number);
}

function displayResult(playerNumbers, strikes, balls) {
    const row = document.createElement("div");
    row.className = "check-result";
    row.style.display = "flex";
    row.style.justifyContent = "space-between";
    row.style.marginBottom = "10px";

    const numbersDiv = document.createElement("div");
    numbersDiv.textContent = playerNumbers.join(" ");
    row.appendChild(numbersDiv);

    const resultDiv = document.createElement("div");

    const separatorDiv = document.createElement("div");
    separatorDiv.textContent = ":";
    separatorDiv.style.margin = "0 10px";
    row.appendChild(separatorDiv);

    if (strikes === 0 && balls === 0) {
        resultDiv.textContent = "O";
        resultDiv.className = "out";
        resultDiv.style.borderRadius = "10px";
        resultDiv.style.padding = "5px 10px";
        resultDiv.style.backgroundColor = "red";
        resultDiv.style.color = "white";
        resultDiv.style.textAlign = "center";
    } else {
        const strikesSpan = document.createElement("span");
        strikesSpan.className = "strike";
        strikesSpan.textContent = "S";
        strikesSpan.style.borderRadius = "10px";
        strikesSpan.style.padding = "5px";
        strikesSpan.style.marginRight = "5px";
        strikesSpan.style.backgroundColor = "green";
        strikesSpan.style.color = "white";

        const strikesText = document.createTextNode(`${strikes} `);

        const ballsSpan = document.createElement("span");
        ballsSpan.className = "ball";
        ballsSpan.textContent = "B";
        ballsSpan.style.borderRadius = "10px";
        ballsSpan.style.padding = "5px";
        ballsSpan.style.marginLeft = "5px";
        ballsSpan.style.backgroundColor = "yellow";
        ballsSpan.style.color = "black";

        const ballsText = document.createTextNode(`${balls} `);

        resultDiv.appendChild(strikesText);
        resultDiv.appendChild(strikesSpan);
        resultDiv.appendChild(ballsText);
        resultDiv.appendChild(ballsSpan);
    }

    row.appendChild(resultDiv);

    return row;
}

function getResult(playerNumbers) {
    let strikes = 0;
    let balls = 0;

    playerNumbers.forEach((num, index) => {
        if (num === answer[index]) {
            strikes++;
        } else if (answer.includes(num)) {
            balls++;
        }
    });

    return { strikes, balls };
}

function resultIMG(isWin) {
    const resultImage = document.getElementById("game-result-img");
    const submitButton = document.querySelector(".submit-button");

    resultImage.src = isWin ? "./success.png" : "./fail.png";
    submitButton.disabled = true;
}

document.querySelector(".submit-button").addEventListener("click", () => {
    const playerNumbers = playerInput();
    if (!playerNumbers) {
        document.querySelectorAll(".input-field").forEach(input => (input.value = ""));
        return;
    }

    const { strikes, balls } = getResult(playerNumbers);

    const resultRow = displayResult(playerNumbers, strikes, balls);
    document.querySelector(".result-display").appendChild(resultRow);

    if (strikes === 3) {
        resultIMG(true);
    } else {
        attemptsLeft--;
        attemptsDisplay();

        if (attemptsLeft === 0) {
            resultIMG(false);
        }
    }

    document.querySelectorAll(".input-field").forEach(input => (input.value = ""));
});

attemptsDisplay();