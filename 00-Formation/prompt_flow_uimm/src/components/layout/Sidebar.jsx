
import React from 'react';
import { useDrag } from 'react-dnd';
import { ROLES, LEVELS, COMMANDS, MODIFIERS } from '../../data/constants';
import * as Icons from 'lucide-react';

// Draggable Item Component
const DraggableItem = ({ item, type }) => {
    const [{ isDragging }, drag] = useDrag(() => ({
        type: type,
        item: { ...item, type },
        collect: (monitor) => ({
            isDragging: !!monitor.isDragging(),
        }),
    }));

    const Icon = Icons[item.icon] || Icons.HelpCircle;

    return (
        <div
            ref={drag}
            className={`btn ${type === 'MODIFIER' ? 'modifier-card' : ''}`} // Add specific class if needed
            style={{
                opacity: isDragging ? 0.5 : 1,
                marginBottom: '8px',
                justifyContent: 'flex-start',
                borderLeft: type === 'COMMAND' ? '3px solid var(--accent-primary)' : '3px solid var(--color-uimm-yellow)',
                cursor: 'grab'
            }}
        >
            <Icon size={16} />
            <span>{item.label}</span>
        </div>
    );
};

const Sidebar = ({ context, setContext }) => {

    const handleContextChange = (field, value) => {
        setContext(prev => ({ ...prev, [field]: value }));
    };

    const toggleSource = (source) => {
        setContext(prev => ({
            ...prev,
            sources: { ...prev.sources, [source]: !prev.sources[source] }
        }));
    };

    return (
        <div style={{ padding: '20px', display: 'flex', flexDirection: 'column', gap: '24px' }}>

            {/* 1. CONTEXTE */}
            <section>
                <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'uppercase', marginBottom: '12px' }}>
                    1. Contexte
                </h3>

                <div style={{ display: 'flex', flexDirection: 'column', gap: '12px' }}>
                    <div className="form-group">
                        <label style={{ display: 'block', fontSize: '0.8rem', marginBottom: '4px' }}>Sujet d'étude</label>
                        <input
                            type="text"
                            value={context.subject}
                            onChange={(e) => handleContextChange('subject', e.target.value)}
                            placeholder="Ex: La sécurité électrique..."
                            style={{
                                width: '100%',
                                padding: '8px',
                                background: 'var(--bg-card)',
                                border: '1px solid var(--border-color)',
                                color: 'white',
                                borderRadius: 'var(--radius-sm)'
                            }}
                        />
                    </div>

                    <div className="form-group">
                        <label style={{ display: 'block', fontSize: '0.8rem', marginBottom: '4px' }}>Rôle</label>
                        <select
                            value={context.role}
                            onChange={(e) => handleContextChange('role', e.target.value)}
                            style={{
                                width: '100%',
                                padding: '8px',
                                background: 'var(--bg-card)',
                                border: '1px solid var(--border-color)',
                                color: 'white',
                                borderRadius: 'var(--radius-sm)'
                            }}
                        >
                            {ROLES.map(role => (
                                <option key={role.id} value={role.id}>{role.label}</option>
                            ))}
                        </select>
                    </div>

                    <div className="form-group">
                        <label style={{ display: 'block', fontSize: '0.8rem', marginBottom: '4px' }}>Niveau Cible</label>
                        <select
                            value={context.level}
                            onChange={(e) => handleContextChange('level', e.target.value)}
                            style={{
                                width: '100%',
                                padding: '8px',
                                background: 'var(--bg-card)',
                                border: '1px solid var(--border-color)',
                                color: 'white',
                                borderRadius: 'var(--radius-sm)'
                            }}
                        >
                            {LEVELS.map(level => (
                                <option key={level.id} value={level.id}>{level.label}</option>
                            ))}
                        </select>
                    </div>
                </div>
            </section>

            {/* 2. SOURCES */}
            <section>
                <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'uppercase', marginBottom: '12px' }}>
                    2. Sources (RAG)
                </h3>
                <div style={{ display: 'flex', gap: '10px' }}>
                    <button
                        className={`btn ${context.sources.includeFiles ? 'btn-primary' : ''}`}
                        onClick={() => toggleSource('includeFiles')}
                        style={{ flex: 1, justifyContent: 'center' }}
                    >
                        Fichiers
                    </button>
                    <button
                        className={`btn ${context.sources.includeWeb ? 'btn-primary' : ''}`}
                        onClick={() => toggleSource('includeWeb')}
                        style={{ flex: 1, justifyContent: 'center' }}
                    >
                        Web
                    </button>
                </div>
            </section>

            {/* 3. PALETTE */}
            <section style={{ flex: 1 }}>
                <h3 style={{ fontSize: '0.9rem', color: 'var(--text-secondary)', textTransform: 'uppercase', marginBottom: '12px' }}>
                    3. Palette
                </h3>

                <div style={{ marginBottom: '16px' }}>
                    <span style={{ fontSize: '0.8rem', color: '#666', display: 'block', marginBottom: '8px' }}>Commandes</span>
                    {COMMANDS.map(cmd => (
                        <DraggableItem key={cmd.id} item={cmd} type="COMMAND" />
                    ))}
                </div>

                <div>
                    <span style={{ fontSize: '0.8rem', color: '#666', display: 'block', marginBottom: '8px' }}>Modificateurs</span>
                    {MODIFIERS.map(mod => (
                        <DraggableItem key={mod.id} item={mod} type="MODIFIER" />
                    ))}
                </div>
            </section>

        </div>
    );
};

export default Sidebar;
