import React from 'react';
import { useDrop } from 'react-dnd';
import * as Icons from 'lucide-react';

const CanvasItem = ({ item, index, removeStep, addModifier }) => {
    const Icon = Icons[item.icon] || Icons.Circle;

    // Make the Item a drop target for MODIFIERS
    const [{ isOver, canDrop }, drop] = useDrop(() => ({
        accept: 'MODIFIER',
        drop: (modifier, monitor) => {
            // Stop propagation to the canvas to avoid double handling if we nested them
            // But here they are siblings in structure effectively? No, Canvas contains Item.
            // monitor.didDrop() checks if child handled it.
            if (monitor.didDrop()) return;
            addModifier(index, modifier);
        },
        collect: (monitor) => ({
            isOver: !!monitor.isOver(),
            canDrop: !!monitor.canDrop(),
        }),
    }));

    const isActive = isOver && canDrop;

    return (
        <div
            ref={drop}
            style={{
                background: isActive ? 'rgba(255, 203, 5, 0.1)' : 'var(--bg-card)',
                border: isActive ? '1px solid var(--color-uimm-yellow)' : '1px solid var(--border-color)',
                borderRadius: 'var(--radius-md)',
                padding: '16px',
                marginBottom: '10px',
                display: 'flex',
                alignItems: 'center',
                gap: '12px',
                position: 'relative',
                borderLeft: '4px solid var(--accent-primary)',
                transition: 'all 0.2s ease'
            }}
        >
            <div style={{
                width: '32px', height: '32px',
                borderRadius: '50%', background: 'rgba(255,255,255,0.05)',
                display: 'flex', alignItems: 'center', justifyContent: 'center'
            }}>
                <Icon size={18} color="var(--accent-primary)" />
            </div>

            <div style={{ flex: 1 }}>
                <div style={{ fontWeight: '600', fontSize: '1rem' }}>{item.label}</div>
                <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>{item.description}</div>

                {/* Modifiers attached to this command */}
                {item.modifiers && item.modifiers.length > 0 && (
                    <div style={{ display: 'flex', gap: '4px', marginTop: '8px', flexWrap: 'wrap' }}>
                        {item.modifiers.map((mod, i) => (
                            <span key={i} style={{
                                background: 'rgba(255, 203, 5, 0.2)',
                                color: 'var(--color-uimm-yellow)',
                                fontSize: '0.7rem', padding: '2px 6px', borderRadius: '4px',
                                display: 'flex', alignItems: 'center', gap: '4px'
                            }}>
                                {mod.label}
                            </span>
                        ))}
                    </div>
                )}
            </div>

            <button
                onClick={() => removeStep(index)}
                style={{
                    background: 'none', border: 'none', color: '#666', cursor: 'pointer',
                    padding: '4px'
                }}
                title="Retirer"
            >
                <Icons.X size={16} />
            </button>

            {/* Connection Line */}
            <div style={{
                position: 'absolute',
                top: '100%',
                left: '32px',
                width: '2px',
                height: '10px',
                background: 'var(--border-color)',
                zIndex: 0
            }} />
        </div>
    );
};

const Canvas = ({ workflow, setWorkflow }) => {

    const [{ isOver }, drop] = useDrop(() => ({
        accept: 'COMMAND',
        drop: (item, monitor) => {
            // Only handle COMMAND drops here. MODIFIERS are handled by items.
            if (!monitor.didDrop()) {
                addItemToWorkflow(item);
            }
        },
        collect: (monitor) => ({
            isOver: !!monitor.isOver(),
        }),
    }));

    const addItemToWorkflow = (item) => {
        setWorkflow(prev => [...prev, { ...item, modifiers: [] }]);
    };

    const addModifierToItem = (index, modifier) => {
        setWorkflow(prev => {
            const newWorkflow = [...prev];
            const targetItem = { ...newWorkflow[index] };
            // Avoid duplicates
            if (!targetItem.modifiers.find(m => m.id === modifier.id)) {
                targetItem.modifiers = [...targetItem.modifiers, modifier];
            }
            newWorkflow[index] = targetItem;
            return newWorkflow;
        });
    };

    const removeStep = (index) => {
        setWorkflow(prev => prev.filter((_, i) => i !== index));
    };

    return (
        <div
            ref={drop}
            style={{
                height: '100%',
                width: '100%',
                background: isOver ? 'rgba(0, 85, 164, 0.05)' : 'transparent',
                padding: '30px',
                overflowY: 'auto'
            }}
        >
            <div style={{ maxWidth: '800px', margin: '0 auto' }}>
                <h2 style={{
                    textAlign: 'center', color: 'var(--text-secondary)',
                    fontSize: '1rem', marginBottom: '30px', fontWeight: '400'
                }}>
                    WorkFlow Visuel
                </h2>

                {workflow.length === 0 ? (
                    <div style={{
                        border: '2px dashed var(--border-color)',
                        borderRadius: 'var(--radius-lg)',
                        padding: '40px',
                        textAlign: 'center',
                        color: 'var(--text-muted)'
                    }}>
                        <Icons.Layers size={48} style={{ marginBottom: '16px', opacity: 0.5 }} />
                        <p>Glissez des commandes depuis la palette<br />pour construire votre séquence.</p>
                    </div>
                ) : (
                    <div style={{ paddingBottom: '100px' }}>
                        {workflow.map((item, index) => (
                            <CanvasItem
                                key={index}
                                item={item}
                                index={index}
                                removeStep={removeStep}
                                addModifier={addModifierToItem}
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Canvas;
