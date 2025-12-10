
export const ROLES = [
    { id: 'formateur', label: 'Formateur', icon: 'GraduationCap' },
    { id: 'expert', label: 'Expert Technique', icon: 'Wrench' },
    { id: 'mentor', label: 'Mentor', icon: 'UserCheck' },
    { id: 'evaluateur', label: 'Évaluateur', icon: 'ClipboardCheck' },
    { id: 'ing_pedago', label: 'Ingénieur Pédago.', icon: 'PenTool' },
    { id: 'manager', label: 'Manager', icon: 'UserPlus' },
    { id: 'qualite', label: 'Responsable Qualité', icon: 'ShieldCheck' },
];

export const LEVELS = [
    { id: 'niveau_3', label: 'Niveau III (CAP)', value: 'Niveau III' },
    { id: 'niveau_4', label: 'Niveau IV (Bac Pro)', value: 'Niveau IV' },
    { id: 'niveau_5', label: 'Niveau V (BTS)', value: 'Niveau V' },
    { id: 'fc', label: 'Formation Continue', value: 'Formation Continue' },
];

export const COMMANDS = [
    { id: 'sequence', label: 'Séquence Pédago.', icon: 'BookOpen', description: 'Créer une séance complète' },
    { id: 'etude_cas', label: 'Étude de Cas', icon: 'Briefcase', description: 'Scénario professionnel réaliste' },
    { id: 'quiz', label: 'QCM / Quiz', icon: 'HelpCircle', description: 'Vérification des acquis' },
    { id: 'feedback', label: 'Feedback', icon: 'MessageCircle', description: 'Analyse et retour critique' },
    { id: 'synthese', label: 'Synthèse', icon: 'FileText', description: 'Résumé structuré' },
    { id: 'roleplay', label: 'Jeu de Rôle', icon: 'Users', description: 'Simulation d’entretien/situation' },
];

export const MODIFIERS = [
    { id: 'no_yapping', label: 'Direct (No Yapping)', command: '/NO-YAPPING', icon: 'Zap' },
    { id: 'table', label: 'Format Tableau', command: '/FORMAT-TABLE', icon: 'Table' },
    { id: 'json', label: 'Format JSON', command: '/FORMAT-JSON', icon: 'Code' },
    { id: 'concise', label: 'Concis (<150 mots)', command: '/LIMIT-150-WORDS', icon: 'Minimize2' },
    { id: 'tone_formal', label: 'Ton Formel', command: '/FORMAL-TONE', icon: 'Tie' },
];
