// État des paramètres
const state = {
    maxTokens: 500,
    temperature: 0.7,
    topP: 0.9,
    topK: 40,
    frequencyPenalty: 0.0,
    presencePenalty: 0.0,
    stopSequences: []
};

// Presets de configuration
const presets = {
    factual: {
        maxTokens: 500,
        temperature: 0.2,
        topP: 0.9,
        topK: 40,
        frequencyPenalty: 0.0,
        presencePenalty: 0.0,
        stopSequences: []
    },
    balanced: {
        maxTokens: 500,
        temperature: 0.7,
        topP: 0.9,
        topK: 40,
        frequencyPenalty: 0.2,
        presencePenalty: 0.0,
        stopSequences: []
    },
    creative: {
        maxTokens: 3000,
        temperature: 1.2,
        topP: 0.95,
        topK: 40,
        frequencyPenalty: 0.7,
        presencePenalty: 0.4,
        stopSequences: []
    },
    code: {
        maxTokens: 1500,
        temperature: 0.2,
        topP: 0.9,
        topK: 40,
        frequencyPenalty: 0.0,
        presencePenalty: 0.0,
        stopSequences: ['```']
    },
    json: {
        maxTokens: 200,
        temperature: 0.0,
        topP: 1.0,
        topK: 40,
        frequencyPenalty: 0.0,
        presencePenalty: 0.0,
        stopSequences: ['}']
    }
};

// Initialisation au chargement de la page
document.addEventListener('DOMContentLoaded', () => {
    initializeSliders();
    initializePresets();
    initializeApiKey();
    initializeGenerateButton();
    initializeCopyConfigButton();
});

// Initialiser les sliders
function initializeSliders() {
    // Max Tokens
    const maxTokensSlider = document.getElementById('maxTokens');
    const maxTokensValue = document.getElementById('maxTokensValue');
    maxTokensSlider.addEventListener('input', (e) => {
        state.maxTokens = parseInt(e.target.value);
        maxTokensValue.textContent = state.maxTokens;
    });

    // Temperature
    const temperatureSlider = document.getElementById('temperature');
    const temperatureValue = document.getElementById('temperatureValue');
    temperatureSlider.addEventListener('input', (e) => {
        state.temperature = parseFloat(e.target.value);
        temperatureValue.textContent = state.temperature.toFixed(1);
    });

    // Top-P
    const topPSlider = document.getElementById('topP');
    const topPValue = document.getElementById('topPValue');
    topPSlider.addEventListener('input', (e) => {
        state.topP = parseFloat(e.target.value);
        topPValue.textContent = state.topP.toFixed(2);
    });

    // Top-K
    const topKSlider = document.getElementById('topK');
    const topKValue = document.getElementById('topKValue');
    topKSlider.addEventListener('input', (e) => {
        state.topK = parseInt(e.target.value);
        topKValue.textContent = state.topK;
    });

    // Frequency Penalty
    const frequencyPenaltySlider = document.getElementById('frequencyPenalty');
    const frequencyPenaltyValue = document.getElementById('frequencyPenaltyValue');
    frequencyPenaltySlider.addEventListener('input', (e) => {
        state.frequencyPenalty = parseFloat(e.target.value);
        frequencyPenaltyValue.textContent = state.frequencyPenalty.toFixed(1);
    });

    // Presence Penalty
    const presencePenaltySlider = document.getElementById('presencePenalty');
    const presencePenaltyValue = document.getElementById('presencePenaltyValue');
    presencePenaltySlider.addEventListener('input', (e) => {
        state.presencePenalty = parseFloat(e.target.value);
        presencePenaltyValue.textContent = state.presencePenalty.toFixed(1);
    });

    // Stop Sequences
    const stopSequencesInput = document.getElementById('stopSequences');
    stopSequencesInput.addEventListener('input', (e) => {
        const value = e.target.value.trim();
        state.stopSequences = value ? value.split(',').map(s => s.trim()).filter(s => s) : [];
    });
}

// Initialiser les boutons de preset
function initializePresets() {
    const presetButtons = document.querySelectorAll('.preset-btn');
    presetButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const presetName = btn.dataset.preset;
            applyPreset(presetName);

            // Mettre à jour l'état actif des boutons
            presetButtons.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
        });
    });
}

// Appliquer un preset
function applyPreset(presetName) {
    const preset = presets[presetName];
    if (!preset) return;

    // Mettre à jour l'état
    Object.assign(state, preset);

    // Mettre à jour les sliders
    document.getElementById('maxTokens').value = state.maxTokens;
    document.getElementById('maxTokensValue').textContent = state.maxTokens;

    document.getElementById('temperature').value = state.temperature;
    document.getElementById('temperatureValue').textContent = state.temperature.toFixed(1);

    document.getElementById('topP').value = state.topP;
    document.getElementById('topPValue').textContent = state.topP.toFixed(2);

    document.getElementById('topK').value = state.topK;
    document.getElementById('topKValue').textContent = state.topK;

    document.getElementById('frequencyPenalty').value = state.frequencyPenalty;
    document.getElementById('frequencyPenaltyValue').textContent = state.frequencyPenalty.toFixed(1);

    document.getElementById('presencePenalty').value = state.presencePenalty;
    document.getElementById('presencePenaltyValue').textContent = state.presencePenalty.toFixed(1);

    document.getElementById('stopSequences').value = state.stopSequences.join(', ');
}

// Initialiser la gestion de la clé API
function initializeApiKey() {
    const apiKeyInput = document.getElementById('apiKey');
    const toggleBtn = document.getElementById('toggleApiKey');

    // Charger la clé depuis sessionStorage
    const savedKey = sessionStorage.getItem('gemini_api_key');
    if (savedKey) {
        apiKeyInput.value = savedKey;
    }

    // Sauvegarder la clé dans sessionStorage
    apiKeyInput.addEventListener('input', (e) => {
        sessionStorage.setItem('gemini_api_key', e.target.value);
    });

    // Toggle visibilité
    toggleBtn.addEventListener('click', () => {
        if (apiKeyInput.type === 'password') {
            apiKeyInput.type = 'text';
        } else {
            apiKeyInput.type = 'password';
        }
    });
}

// Initialiser le bouton de génération
function initializeGenerateButton() {
    const generateBtn = document.getElementById('generateBtn');
    generateBtn.addEventListener('click', async () => {
        await generateResponse();
    });
}

// Initialiser le bouton de copie de configuration
function initializeCopyConfigButton() {
    const copyBtn = document.getElementById('copyConfigBtn');
    copyBtn.addEventListener('click', () => {
        copyConfiguration();
    });
}

// Générer une réponse avec l'API Gemini
async function generateResponse() {
    const apiKey = document.getElementById('apiKey').value.trim();
    const prompt = document.getElementById('prompt').value.trim();
    const outputDiv = document.getElementById('output');
    const generateBtn = document.getElementById('generateBtn');

    // Validation
    if (!apiKey) {
        showError('Veuillez entrer votre clé API Gemini.');
        return;
    }

    if (!prompt) {
        showError('Veuillez entrer un prompt.');
        return;
    }

    // Désactiver le bouton et afficher le spinner
    generateBtn.disabled = true;
    generateBtn.textContent = 'Génération en cours...';
    outputDiv.innerHTML = '<div class="spinner"></div>';
    outputDiv.classList.add('loading');

    const startTime = Date.now();

    try {
        // Construire la requête pour l'API Gemini
        const url = `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${apiKey}`;

        const requestBody = {
            contents: [{
                parts: [{
                    text: prompt
                }]
            }],
            generationConfig: {
                temperature: state.temperature,
                topP: state.topP,
                topK: state.topK,
                maxOutputTokens: state.maxTokens,
            }
        };

        // Ajouter les stop sequences si définies
        if (state.stopSequences.length > 0) {
            requestBody.generationConfig.stopSequences = state.stopSequences;
        }

        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const endTime = Date.now();
        const duration = ((endTime - startTime) / 1000).toFixed(2);

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error?.message || 'Erreur lors de l\'appel à l\'API');
        }

        const data = await response.json();

        // Extraire la réponse
        const generatedText = data.candidates?.[0]?.content?.parts?.[0]?.text || 'Aucune réponse générée';
        const tokenCount = estimateTokens(generatedText);

        // Afficher la réponse
        displayResponse(generatedText, tokenCount, duration);

    } catch (error) {
        console.error('Erreur:', error);
        showError(`Erreur: ${error.message}`);
    } finally {
        generateBtn.disabled = false;
        generateBtn.textContent = 'Générer la Réponse';
        outputDiv.classList.remove('loading');
    }
}

// Afficher la réponse
function displayResponse(text, tokenCount, duration) {
    const outputDiv = document.getElementById('output');
    const tokenCountSpan = document.getElementById('tokenCount');
    const generationTimeSpan = document.getElementById('generationTime');

    outputDiv.innerHTML = `<p>${text.replace(/\n/g, '<br>')}</p>`;
    tokenCountSpan.textContent = `Tokens: ~${tokenCount}`;
    generationTimeSpan.textContent = `Temps: ${duration}s`;
}

// Afficher une erreur
function showError(message) {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = `<div class="error">${message}</div>`;
}

// Estimer le nombre de tokens (approximation)
function estimateTokens(text) {
    // Approximation simple: 1 token ≈ 4 caractères
    return Math.ceil(text.length / 4);
}

// Copier la configuration actuelle
function copyConfiguration() {
    const config = {
        max_tokens: state.maxTokens,
        temperature: state.temperature,
        top_p: state.topP,
        top_k: state.topK,
        frequency_penalty: state.frequencyPenalty,
        presence_penalty: state.presencePenalty,
        stop_sequences: state.stopSequences
    };

    const configText = JSON.stringify(config, null, 2);

    // Copier dans le presse-papiers
    navigator.clipboard.writeText(configText).then(() => {
        // Feedback visuel
        const btn = document.getElementById('copyConfigBtn');
        const originalText = btn.textContent;
        btn.textContent = 'Configuration copiée !';
        setTimeout(() => {
            btn.textContent = originalText;
        }, 2000);
    }).catch(err => {
        console.error('Erreur lors de la copie:', err);
        alert('Impossible de copier la configuration');
    });
}
