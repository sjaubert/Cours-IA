
import React from 'react';
import * as Icons from 'lucide-react';
import { ROLES, LEVELS } from '../../data/constants';

const CodePreview = ({ context, workflow }) => {

    const generatePrompt = () => {
        // 1. Role & Context
        const activeRole = ROLES.find(r => r.id === context.role)?.label || context.role;
        const activeLevel = LEVELS.find(l => l.id === context.level)?.value || context.level;

        let output = `/initier_contexte_éducatif {\n`;
        output += `  "role": "${activeRole}",\n`;
        output += `  "niveau": "${activeLevel}",\n`;
        output += `  "sujet": "${context.subject || 'NON DÉFINI'}"\n`;
        output += `}\n\n`;

        output += `/configurer_sources_données {\n`;
        output += `  "web_search": ${context.sources.includeWeb},\n`;
        output += `  "fichiers_locaux": ${context.sources.includeFiles}\n`;
        output += `}\n\n`;

        // 3. Output Settings
        output += `/reglages_sortie {\n`;
        output += `  "creativite": "${context.output?.creativity || 'balanced'}",\n`;
        output += `  "densite": "${context.output?.density || 'standard'}"\n`;
        output += `}\n\n`;

        // 3. Sequence
        output += `/SÉQUENCE_EXECUTION {\n`;

        if (workflow.length === 0) {
            output += `  // En attente de commandes...\n`;
        } else {
            workflow.forEach((step, index) => {
                const stepName = `PHASE_${index + 1}`;
                const commandName = step.label.toUpperCase().replace(/ /g, '_');

                let modifiersStr = '';
                if (step.modifiers && step.modifiers.length > 0) {
                    modifiersStr = ' ' + step.modifiers.map(m => m.command).join(' ');
                }

                output += `  ${stepName}: [${commandName}]${modifiersStr}\n`;
            });
        }
        output += `}\n`;

        return output;
    };

    const copyToClipboard = () => {
        navigator.clipboard.writeText(generatePrompt());
        // Could add toaster notification here
    };

    const openInGemini = () => {
        const prompt = generatePrompt();
        const encodedPrompt = encodeURIComponent(prompt);
        // Check URL length (browsers typically support up to 2000 chars)
        const url = `https://aistudio.google.com/app/prompts/new_freeform?q=${encodedPrompt}`;
        if (url.length > 2000) {
            // Fallback: copy and open
            navigator.clipboard.writeText(prompt);
            window.open('https://aistudio.google.com/app/prompts/new_freeform', '_blank');
        } else {
            window.open(url, '_blank');
        }
    };

    const openInChatGPT = () => {
        const prompt = generatePrompt();
        navigator.clipboard.writeText(prompt);
        window.open('https://chat.openai.com/', '_blank');
    };

    const openInClaude = () => {
        const prompt = generatePrompt();
        navigator.clipboard.writeText(prompt);
        window.open('https://claude.ai/new', '_blank');
    };

    return (
        <div style={{ height: '100%', display: 'flex', flexDirection: 'column' }}>
            <div style={{
                padding: '16px', borderBottom: '1px solid var(--border-color)',
                display: 'flex', justifyContent: 'space-between', alignItems: 'center',
                flexWrap: 'wrap', gap: '8px'
            }}>
                <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Sortie Prompt</span>
                <div style={{ display: 'flex', gap: '6px', flexWrap: 'wrap' }}>
                    <button
                        className="btn"
                        onClick={copyToClipboard}
                        style={{ fontSize: '0.8rem', padding: '6px 12px', display: 'flex', alignItems: 'center', gap: '4px' }}
                        title="Copier le prompt"
                    >
                        <Icons.Copy size={14} />
                        Copier
                    </button>
                    <button
                        className="btn btn-primary"
                        onClick={openInGemini}
                        style={{ fontSize: '0.8rem', padding: '6px 12px' }}
                        title="Ouvrir dans Google AI Studio avec le prompt"
                    >
                        Gemini
                    </button>
                    <button
                        className="btn"
                        onClick={openInChatGPT}
                        style={{ fontSize: '0.8rem', padding: '6px 12px' }}
                        title="Copier le prompt et ouvrir ChatGPT"
                    >
                        ChatGPT
                    </button>
                    <button
                        className="btn"
                        onClick={openInClaude}
                        style={{ fontSize: '0.8rem', padding: '6px 12px' }}
                        title="Copier le prompt et ouvrir Claude"
                    >
                        Claude
                    </button>
                </div>
            </div>

            <div style={{ flex: 1, padding: '0', position: 'relative' }}>
                <textarea
                    readOnly
                    value={generatePrompt()}
                    style={{
                        width: '100%',
                        height: '100%',
                        background: 'var(--bg-panel)',
                        color: '#a6accd', // Monokai-ish text
                        border: 'none',
                        outline: 'none',
                        padding: '20px',
                        fontFamily: 'Consolas, Monaco, "Andale Mono", monospace',
                        fontSize: '0.9rem',
                        resize: 'none',
                        lineHeight: '1.5'
                    }}
                />
            </div>
        </div>
    );
};

export default CodePreview;
