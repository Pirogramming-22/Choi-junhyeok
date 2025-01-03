let timer;
let elapsedTime = 0;
let running = false;

const timeDisplay = document.querySelector(".time h1");
const recordField = document.querySelector(".record_field-bottom");

function formatTime(ms) {
    const totalSeconds = Math.floor(ms / 1000);
    const seconds = String(totalSeconds % 60).padStart(2, "0");
    const milliseconds = String(Math.floor((ms % 1000) / 10)).padStart(2, "0");
    return `${seconds}:${milliseconds}`;
}

function updateTimer() {
    elapsedTime += 10;
    timeDisplay.textContent = formatTime(elapsedTime);
}

function addRecord() {
    if (elapsedTime > 0) {
        const recordDiv = document.createElement("div");
        recordDiv.className = "record";

        recordDiv.innerHTML = `
            <div class="check">
                <button class="check_button">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-check2" viewBox="0 0 16 16">
                        <path d="M13.854 3.646a.5.5 0 0 1 0 .708l-7 7a.5.5 0 0 1-.708 0l-3.5-3.5a.5.5 0 1 1 .708-.708L6.5 10.293l6.646-6.647a.5.5 0 0 1 .708 0"/>
                    </svg>
                </button>
            </div>
            <h3 class="record_time">${formatTime(elapsedTime)}</h3>
            <button class="delete_button">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-trash3-fill" viewBox="0 0 16 16">
                    <path d="M11 1.5v1h3.5a.5.5 0 0 1 0 1h-.538l-.853 10.66A2 2 0 0 1 11.115 16h-6.23a2 2 0 0 1-1.994-1.84L2.038 3.5H1.5a.5.5 0 0 1 0-1H5v-1A1.5 1.5 0 0 1 6.5 0h3A1.5 1.5 0 0 1 11 1.5m-5 0v1h4v-1a.5.5 0 0 0-.5-.5h-3a.5.5 0 0 0-.5.5M4.5 5.029l.5 8.5a.5.5 0 1 0 .998-.06l-.5-8.5a.5.5 0 1 0-.998.06m6.53-.528a.5.5 0 0 0-.528.47l-.5 8.5a.5.5 0 0 0 .998.058l.5-8.5a.5.5 0 0 0-.47-.528M8 4.5a.5.5 0 0 0-.5.5v8.5a.5.5 0 0 0 1 0V5a.5.5 0 0 0-.5-.5"/>
                </svg>
            </button>
        `;

        const checkButton = recordDiv.querySelector(".check_button");
        checkButton.addEventListener("click", () => {
            const svg = checkButton.querySelector("svg");
            if (svg.getAttribute("fill") === "black") {
                svg.setAttribute("fill", "green");
            } else {
                svg.setAttribute("fill", "black");
            }
        });

        const deleteButton = recordDiv.querySelector(".delete_button");
        deleteButton.addEventListener("click", () => {
            const checkSvg = recordDiv.querySelector(".check_button svg");
            if (checkSvg.getAttribute("fill") === "green") {
                recordDiv.remove();
            } else {
                alert("기록을 선택 후 삭제해주세요.");
            }
        });

        recordField.appendChild(recordDiv);
    }
}

document.querySelector(".start_button").addEventListener("click", () => {
    if (!running) {
        running = true;
        timer = setInterval(updateTimer, 10);
    }
});

document.querySelector(".stop_button").addEventListener("click", () => {
    if (running) {
        running = false;
        clearInterval(timer);
        addRecord();
    }
});

document.querySelector(".lap_button").addEventListener("click", () => {
    if (running) {
        addRecord();
    }
});

document.querySelector(".reset_button").addEventListener("click", () => {
    running = false;
    clearInterval(timer);
    elapsedTime = 0;
    timeDisplay.textContent = "00:00";
});

document.querySelector(".check_all_button").addEventListener("click", () => {
    const records = document.querySelectorAll(".record .check_button svg");
    const checkAllButtonSvg = document.querySelector(".check_all_button svg");

    const allSelected = Array.from(records).every((svg) => svg.getAttribute("fill") === "green");

    if (allSelected) {
        records.forEach((svg) => svg.setAttribute("fill", "black"));
        checkAllButtonSvg.setAttribute("fill", "black");
    } else {
        records.forEach((svg) => svg.setAttribute("fill", "green"));
        checkAllButtonSvg.setAttribute("fill", "green");
    }
});

document.querySelector(".delete_button").addEventListener("click", () => {
    const records = document.querySelectorAll(".record");
    let deleted = false;

    records.forEach((record) => {
        const svg = record.querySelector(".check_button svg");
        if (svg.getAttribute("fill") === "green") {
            record.remove();
            deleted = true;
        }
    });

    if (!deleted) {
        alert("기록을 선택 후 삭제해주세요.");
    }

    const remainingRecords = document.querySelectorAll(".record .check_button svg");
    const checkAllButtonSvg = document.querySelector(".check_all_button svg");

    if (remainingRecords.length === 0 || Array.from(remainingRecords).some((svg) => svg.getAttribute("fill") === "black")) {
        checkAllButtonSvg.setAttribute("fill", "black");
    }
});