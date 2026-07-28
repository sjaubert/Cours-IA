
export const ROLES = [
    { id: 'formateur', label: 'Formateur', icon: 'GraduationCap' },
    { id: 'expert', label: 'Expert Technique', icon: 'Wrench' },
    { id: 'evaluateur', label: 'Évaluateur', icon: 'ClipboardCheck' },
    { id: 'ing_pedago', label: 'Ingénieur Pédago.', icon: 'PenTool' },
    { id: 'manager', label: 'Manager', icon: 'UserPlus' },
    { id: 'qualite', label: 'Responsable Qualité', icon: 'ShieldCheck' },
];

export const LEVELS = [
    { id: 'niveau_3', label: 'Niveau III (CAP)', value: 'Niveau III' },
    { id: 'niveau_4', label: 'Niveau IV (Bac Pro)', value: 'Niveau IV' },
    { id: 'niveau_5', label: 'Niveau V (BTS)', value: 'Niveau V' },
    { id: 'bachelor', label: 'Bachelor', value: 'Bachelor' },
    { id: 'ingenieur', label: 'Ingénieur', value: 'Ingénieur' },
    { id: 'fc', label: 'Formation Continue', value: 'Formation Continue' },
];

export const COMMANDS = [
    { id: 'sequence', label: 'Séquence Pédago.', icon: 'BookOpen', description: 'Créer une séance complète' },
    { id: 'etude_cas', label: 'Étude de Cas', icon: 'Briefcase', description: 'Scénario professionnel réaliste' },
    { id: 'quiz', label: 'QCM / Quiz', icon: 'HelpCircle', description: 'Vérification des acquis' },
    { id: 'feedback', label: 'Feedback', icon: 'MessageCircle', description: 'Analyse et retour critique' },
    { id: 'synthese', label: 'Synthèse', icon: 'FileText', description: 'Résumé structuré' },
    { id: 'roleplay', label: 'Jeu de Rôle', icon: 'Users', description: 'Simulation dentretien/situation' },
    { id: 'objectifs', label: 'Objectifs SMART', icon: 'Target', description: 'Objectifs Spécifiques/Mesurables' },
    { id: 'evaluation', label: 'Évaluation', icon: 'Award', description: 'Grille dévaluation compétences' },
    { id: 'plan_formation', label: 'Plan de Formation', icon: 'Map', description: 'Parcours de formation structuré' },
    { id: 'certification', label: 'Certification', icon: 'ShieldCheck', description: 'Validation des acquis professionnels' },
    { id: 'mindmap', label: 'Carte Mentale', icon: 'BookOpen', description: 'Visualisation structurée des concepts' },
];

export const MODIFIERS = [
    { id: 'no_yapping', label: 'Direct (No Yapping)', command: '/NO-YAPPING', icon: 'Zap' },
    { id: 'table', label: 'Format Tableau', command: '/FORMAT-TABLE', icon: 'Table' },
    { id: 'json', label: 'Format JSON', command: '/FORMAT-JSON', icon: 'Code' },
    { id: 'concise', label: 'Concis (<150 mots)', command: '/LIMIT-150-WORDS', icon: 'Minimize2' },
    { id: 'tone_formal', label: 'Ton Formel', command: '/FORMAL-TONE', icon: 'Tie' },
    { id: 'bullets', label: 'Puces Uniquement', command: '/BULLETS-ONLY', icon: 'List' },
    { id: 'steps', label: 'Étapes (1,2,3)', command: '/STEP-BY-STEP', icon: 'ListOrdered' },
    { id: 'examples', label: '+ Exemples', command: '/ADD-EXAMPLES', icon: 'Lightbulb' },
    { id: 'add_quiz', label: '+ Quiz', command: '/ADD-QUIZ', icon: 'CheckSquare' },
    { id: 'sources', label: 'Citer Sources', command: '/CITE-SOURCES', icon: 'Link' },
    { id: 'highlight', label: 'Gras/Mise en avant', command: '/HIGHLIGHT', icon: 'Bold' },
    { id: 'no_emoji', label: 'No Emoji', command: '/NO-EMOJI', icon: 'Ban' },
    { id: 'casual', label: 'Ton Cool', command: '/CASUAL-TONE', icon: 'Smile' },
    { id: 'code_only', label: 'Code Seul', command: '/CODE-ONLY', icon: 'Terminal' },
    { id: 'time_limit', label: 'Temps Limité', command: '/TIME-LIMIT', icon: 'Clock' },
    { id: 'custom_format', label: 'Format Spécifique', command: '/CUSTOM-FORMAT', icon: 'Layout' },
    { id: 'rich_context', label: 'Contexte Riche', command: '/RICH-CONTEXT', icon: 'BookOpen' },
];
