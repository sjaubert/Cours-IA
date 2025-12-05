// Game State
const state = {
    player1Time: 300, // seconds
    player2Time: 300,
    initialTime: 300,
    increment: 3, // seconds
    activePlayer: null, // 1, 2, or null (not started/paused)
    timerInterval: null,
    isPaused: false,
    gameActive: false // true if game has started and not finished
};

// DOM Elements
const p1Container = document.getElementById('player1-container');
const p2Container = document.getElementById('player2-container');
const p1Display = document.getElementById('player1-time');
const p2Display = document.getElementById('player2-time');
const btnBlitz = document.getElementById('btn-blitz');
const btnRapid1 = document.getElementById('btn-rapid1');
const btnRapid2 = document.getElementById('btn-rapid2');
const btnPause = document.getElementById('btn-pause');
const btnReset = document.getElementById('btn-reset');

// Audio (Optional, simple beep using Web Audio API could be added, but keeping it silent for now as per req)

// Initialization
function init() {
    updateDisplay();
    setActiveModeBtn(btnBlitz);
    setupEventListeners();
}

// Time Formatting
function formatTime(seconds) {
    const m = Math.floor(seconds / 60);
    const s = Math.floor(seconds % 60);
    // Optional: Show tenths of seconds if under 10 seconds?
    // For now standard MM:SS
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
}

function updateDisplay() {
    p1Display.textContent = formatTime(state.player1Time);
    p2Display.textContent = formatTime(state.player2Time);
}

// Core Logic
function startClock(player) {
    if (state.timerInterval) clearInterval(state.timerInterval);

    state.activePlayer = player;
    state.isPaused = false;
    state.gameActive = true;

    updateVisuals();

    state.timerInterval = setInterval(() => {
        if (state.activePlayer === 1) {
            state.player1Time -= 0.1;
            if (state.player1Time <= 0) flagFall(1);
        } else {
            state.player2Time -= 0.1;
            if (state.player2Time <= 0) flagFall(2);
        }
        // We update display every second usually, but for smoother feel maybe every 100ms?
        // Let's stick to updating text every second to avoid flickering, or just update on integer change
        // Actually, let's keep internal time precise and display rounded
        updateDisplay();
    }, 100);
}

function switchTurn() {
    if (!state.gameActive) {
        // If game hasn't started, start it.
        // Usually Black starts clock, so White moves first.
        // If P1 is White (bottom), P2 (Black) should be active first?
        // Let's assume whoever clicks their clock starts the OTHER person's clock.
        // If I click P1 clock, it means I made a move (or I'm ready), so P2 starts.
        return;
    }

    if (state.isPaused) return;

    // Add increment to the player who JUST finished
    if (state.activePlayer === 1) {
        state.player1Time += state.increment;
        startClock(2);
    } else if (state.activePlayer === 2) {
        state.player2Time += state.increment;
        startClock(1);
    }
}

function pauseClock() {
    if (!state.gameActive) return;

    if (state.isPaused) {
        // Resume
        startClock(state.activePlayer);
        btnPause.innerHTML = '⏸';
    } else {
        // Pause
        clearInterval(state.timerInterval);
        state.isPaused = true;
        p1Container.classList.remove('active');
        p2Container.classList.remove('active');
        btnPause.innerHTML = '▶';
    }
}

function resetGame() {
    clearInterval(state.timerInterval);
    state.player1Time = state.initialTime;
    state.player2Time = state.initialTime;
    state.activePlayer = null;
    state.gameActive = false;
    state.isPaused = false;
    p1Container.classList.remove('active', 'flagged');
    p2Container.classList.remove('active', 'flagged');
    btnPause.innerHTML = '⏸';
    updateDisplay();
}

function setMode(minutes, increment, btn) {
    state.initialTime = minutes * 60;
    state.increment = increment;
    setActiveModeBtn(btn);
    resetGame();
}

function flagFall(player) {
    clearInterval(state.timerInterval);
    state.gameActive = false;
    state.activePlayer = null;
    if (player === 1) {
        state.player1Time = 0;
        p1Container.classList.add('flagged');
    } else {
        state.player2Time = 0;
        p2Container.classList.add('flagged');
    }
    updateDisplay();
}

// Visuals
function updateVisuals() {
    p1Container.classList.remove('active');
    p2Container.classList.remove('active');

    if (state.activePlayer === 1) p1Container.classList.add('active');
    if (state.activePlayer === 2) p2Container.classList.add('active');
}

function setActiveModeBtn(activeBtn) {
    [btnBlitz, btnRapid1, btnRapid2].forEach(b => b.classList.remove('active-mode'));
    if (activeBtn) activeBtn.classList.add('active-mode');
}

// Event Listeners
function setupEventListeners() {
    // Click on clock areas
    p1Container.addEventListener('click', () => {
        if (!state.gameActive && !state.activePlayer) {
            // First start: If P1 clicks, P2 starts
            startClock(2);
        } else if (state.activePlayer === 1) {
            switchTurn();
        }
    });

    p2Container.addEventListener('click', () => {
        if (!state.gameActive && !state.activePlayer) {
            // First start: If P2 clicks, P1 starts
            startClock(1);
        } else if (state.activePlayer === 2) {
            switchTurn();
        }
    });

    // Buttons
    btnBlitz.addEventListener('click', () => setMode(5, 3, btnBlitz));
    btnRapid1.addEventListener('click', () => setMode(10, 5, btnRapid1));
    btnRapid2.addEventListener('click', () => setMode(15, 10, btnRapid2));
    btnPause.addEventListener('click', pauseClock);
    btnReset.addEventListener('click', resetGame);

    // Keyboard Shortcuts
    document.addEventListener('keydown', (e) => {
        // Prevent default for space to avoid scrolling
        if (e.code === 'Space') e.preventDefault();

        switch (e.key.toLowerCase()) {
            case ' ':
                if (!state.gameActive && !state.activePlayer) {
                    // Start game (default to P1 starts if space pressed initially?)
                    // Or maybe just ignore? Let's start P1 for simplicity
                    startClock(1);
                } else {
                    switchTurn();
                }
                break;
            case 'p':
                pauseClock();
                break;
            case 'r':
                resetGame();
                break;
            case '1':
            case '&': // AZERTY support
                setMode(5, 3, btnBlitz);
                break;
            case '2':
            case 'é': // AZERTY support
                setMode(10, 5, btnRapid1);
                break;
            case '3':
            case '"': // AZERTY support
                setMode(15, 10, btnRapid2);
                break;
        }
    });
}

// Run
init();
