const timeDisplay = document.getElementById('time-display');
const startBtn = document.getElementById('start-btn');
const resetBtn = document.getElementById('reset-btn');
const modeBtns = document.querySelectorAll('.mode-btn');
const circle = document.querySelector('.progress-ring__circle');
const radius = circle.r.baseVal.value;
const circumference = radius * 2 * Math.PI;

circle.style.strokeDasharray = `${circumference} ${circumference}`;
circle.style.strokeDashoffset = circumference;

let timeLeft = 25 * 60;
let initialTime = 25 * 60;
let timerId = null;
let isRunning = false;

function setProgress(percent) {
    const offset = circumference - (percent / 100) * circumference;
    circle.style.strokeDashoffset = offset;
}

function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    timeDisplay.textContent = `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;

    const percent = (timeLeft / initialTime) * 100;
    // Invert progress for countdown effect (full at start, empty at end)
    // Actually, let's make it empty as it goes.
    // strokeDashoffset = circumference means empty. 0 means full.
    // We want it full at start (offset 0) and empty at end (offset circumference).
    // So offset should go from 0 to circumference.
    // Formula: offset = circumference * (1 - percent/100) where percent is remaining time %

    const offset = circumference * (1 - (timeLeft / initialTime));
    circle.style.strokeDashoffset = offset;
}

function startTimer() {
    if (isRunning) {
        pauseTimer();
        return;
    }

    isRunning = true;
    startBtn.textContent = 'Pause';
    document.body.classList.remove('timer-finished');

    timerId = setInterval(() => {
        timeLeft--;
        updateDisplay();

        if (timeLeft <= 0) {
            clearInterval(timerId);
            isRunning = false;
            startBtn.textContent = 'Démarrer';
            timeLeft = 0;
            updateDisplay();
            document.body.classList.add('timer-finished');
            // Visual pulse is handled by CSS class
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(timerId);
    isRunning = false;
    startBtn.textContent = 'Reprendre';
}

function resetTimer() {
    pauseTimer();
    timeLeft = initialTime;
    startBtn.textContent = 'Démarrer';
    document.body.classList.remove('timer-finished');
    updateDisplay();
    // Reset circle to full
    circle.style.strokeDashoffset = 0;
}

function switchMode(e) {
    const mode = e.target.dataset.mode;

    modeBtns.forEach(btn => btn.classList.remove('active'));
    e.target.classList.add('active');

    switch (mode) {
        case 'pomodoro':
            initialTime = 25 * 60;
            document.documentElement.style.setProperty('--primary-color', '#8FBC8F'); // Sage
            break;
        case 'shortBreak':
            initialTime = 5 * 60;
            document.documentElement.style.setProperty('--primary-color', '#D8BFD8'); // Thistle
            break;
        case 'longBreak':
            initialTime = 15 * 60;
            document.documentElement.style.setProperty('--primary-color', '#87CEEB'); // Sky Blue (soft)
            break;
    }

    resetTimer();
}

startBtn.addEventListener('click', startTimer);
resetBtn.addEventListener('click', resetTimer);
modeBtns.forEach(btn => btn.addEventListener('click', switchMode));

// Initialize
circle.style.strokeDashoffset = 0; // Start full
updateDisplay();
