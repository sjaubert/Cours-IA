const chatHistory = document.getElementById('chat-history');
const codeDisplay = document.getElementById('code-display');

const scenarios = {
    report: {
        userMessage: "Analyse le fichier 'logs.csv' et génère un rapport PDF avec un graphique des erreurs par jour.",
        aiResponse: "Bien sûr. Je vais utiliser Pandas pour l'analyse et Matplotlib pour le graphique. Voici le plan :\n1. Charger 'logs.csv'.\n2. Convertir les dates.\n3. Agréger les erreurs par jour.\n4. Générer le PDF.",
        code: `import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# 1. Chargement des données
df = pd.read_csv('logs.csv')

# 2. Traitement
df['date'] = pd.to_datetime(df['timestamp'])
daily_errors = df[df['status'] == 'ERROR'].groupby(df['date'].dt.date).size()

# 3. Graphique
plt.figure(figsize=(10, 6))
daily_errors.plot(kind='bar', color='red')
plt.title('Erreurs par Jour')
plt.savefig('chart.png')

# 4. Génération PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Rapport d'Incidents", ln=1, align='C')
pdf.image('chart.png', x=10, y=30, w=190)
pdf.output("rapport.pdf")

print("Rapport généré avec succès !")`
    },
    fix: {
        userMessage: "Le script plante avec une erreur : 'FileNotFoundError: [Errno 2] No such file or directory: 'logs.csv''.",
        aiResponse: "Ah, je vois. Le fichier 'logs.csv' n'est pas trouvé. Je vais ajouter une vérification de l'existence du fichier et créer un fichier factice pour le test si nécessaire.",
        code: `import pandas as pd
import os

# CORRECTION : Vérification du fichier
file_path = 'logs.csv'

if not os.path.exists(file_path):
    print(f"Attention : {file_path} introuvable.")
    print("Création d'un fichier de test...")
    # Création données factices
    with open(file_path, 'w') as f:
        f.write("timestamp,status\\n2023-10-01 10:00:00,OK\\n2023-10-01 11:00:00,ERROR")

# Suite du script...
df = pd.read_csv(file_path)
print("Données chargées.")`
    }
};

function addMessage(text, sender) {
    const div = document.createElement('div');
    div.className = `message ${sender}`;
    div.textContent = text;
    chatHistory.appendChild(div);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function typeCode(code) {
    codeDisplay.innerHTML = '';
    let i = 0;
    const speed = 10; // ms per char

    function type() {
        if (i < code.length) {
            let char = code.charAt(i);
            if (char === '\n') {
                codeDisplay.innerHTML += '<br>';
            } else if (char === ' ') {
                codeDisplay.innerHTML += '&nbsp;';
            } else {
                codeDisplay.innerText += char;
            }
            
            // Simple syntax highlighting hack (very basic)
            codeDisplay.innerHTML = codeDisplay.innerHTML
                .replace(/import/g, '<span class="keyword">import</span>')
                .replace(/from/g, '<span class="keyword">from</span>')
                .replace(/def/g, '<span class="keyword">def</span>')
                .replace(/print/g, '<span class="function">print</span>')
                .replace(/#.*/g, '<span class="comment">$&</span>');

            i++;
            chatHistory.scrollTop = chatHistory.scrollHeight; // Keep scrolling if code pushes layout
            setTimeout(type, speed);
        }
    }
    type();
}

// Better syntax highlighting approach for the final block
function highlightCode(code) {
    return code
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/\b(import|from|def|class|if|else|return|while|for|in)\b/g, '<span class="keyword">$1</span>')
        .replace(/\b(print|len|range|open)\b/g, '<span class="function">$1</span>')
        .replace(/(['"])(.*?)\1/g, '<span class="string">$1$2$1</span>')
        .replace(/#.*/g, '<span class="comment">$&</span>');
}

function runScenario(type) {
    const scenario = scenarios[type];
    if (!scenario) return;

    // Clear previous state
    codeDisplay.innerHTML = '<span class="comment">// En attente...</span>';
    
    // 1. User Message
    addMessage(scenario.userMessage, 'user');

    // 2. AI Thinking Delay
    setTimeout(() => {
        // 3. AI Response
        addMessage(scenario.aiResponse, 'ai');
        
        // 4. Code Generation
        setTimeout(() => {
            // Use the simple typing effect, then replace with highlighted HTML at the end
            let i = 0;
            codeDisplay.innerHTML = '';
            const interval = setInterval(() => {
                codeDisplay.textContent += scenario.code[i];
                codeDisplay.scrollTop = codeDisplay.scrollHeight;
                i++;
                if (i >= scenario.code.length) {
                    clearInterval(interval);
                    // Apply highlighting at the end
                    codeDisplay.innerHTML = highlightCode(scenario.code);
                }
            }, 10);
        }, 1000);

    }, 800);
}
