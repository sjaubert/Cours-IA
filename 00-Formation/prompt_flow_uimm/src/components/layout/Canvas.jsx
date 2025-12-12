import React, { useRef } from 'react';
import { useDrop, useDrag } from 'react-dnd';
import * as Icons from 'lucide-react';

const CanvasItem = ({ item, index, removeStep, addModifier, moveStep, removeModifier, updateStep }) => {
    // Robust fallback: try item.icon, then HelpCircle, then generic Circle.
    // Ensure we always have a valid component.
    const Icon = Icons[item.icon] ? Icons[item.icon] : (Icons.HelpCircle || Icons.Circle || Icons.Box);
    const ref = useRef(null);

    // Make the item draggable for reordering
    const [{ isDragging }, drag] = useDrag({
        type: 'WORKFLOW_ITEM',
        item: { index },
        collect: (monitor) => ({
            isDragging: monitor.isDragging()
        })
    });

    // Accept drops from other workflow items for reordering
    const [{ isOverReorder }, dropReorder] = useDrop({
        accept: 'WORKFLOW_ITEM',
        hover: (draggedItem) => {
            if (draggedItem.index !== index) {
                moveStep(draggedItem.index, index);
                draggedItem.index = index;
            }
        },
        collect: (monitor) => ({
            isOverReorder: monitor.isOver() && monitor.getItemType() === 'WORKFLOW_ITEM'
        })
    });

    // Accept drops of MODIFIERS
    const [{ isOver, canDrop }, dropModifier] = useDrop(() => ({
        accept: 'MODIFIER',
        drop: (modifier, monitor) => {
            if (monitor.didDrop()) return;
            addModifier(index, modifier);
        },
        collect: (monitor) => ({
            isOver: !!monitor.isOver(),
            canDrop: !!monitor.canDrop(),
        }),
    }));

    const isActive = isOver && canDrop;

    // Combine refs for both drag and drop
    drag(dropReorder(dropModifier(ref)));

    return (
        <div
            ref={ref}
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
                transition: 'all 0.2s ease',
                opacity: isDragging ? 0.5 : 1,
                cursor: 'grab'
            }}
        >
            {/* Drag handle icon */}
            <div style={{
                color: '#666',
                cursor: 'grab',
                display: 'flex',
                alignItems: 'center'
            }}>
                <Icons.GripVertical size={16} />
            </div>

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
                        {item.modifiers.map((mod, modIndex) => (
                            <span key={modIndex} style={{
                                background: 'rgba(255, 203, 5, 0.2)',
                                color: 'var(--color-uimm-yellow)',
                                fontSize: '0.7rem', padding: '2px 8px', borderRadius: '4px',
                                display: 'flex', alignItems: 'center', gap: '4px'
                            }}>
                                {mod.label}
                                <button
                                    onClick={() => removeModifier(index, modIndex)}
                                    style={{
                                        background: 'none',
                                        border: 'none',
                                        color: 'var(--color-uimm-yellow)',
                                        cursor: 'pointer',
                                        padding: '0',
                                        marginLeft: '2px',
                                        display: 'flex',
                                        alignItems: 'center',
                                        opacity: 0.7,
                                        fontSize: '0.9rem',
                                        fontWeight: 'bold'
                                    }}
                                    title="Retirer ce modificateur"
                                >
                                    ×
                                </button>
                            </span>
                        ))}
                    </div>
                )}

                {/* Custom Instruction Input */}
                <textarea
                    placeholder="Instructions spécifiques (ex: Durée 15min, Format Tableau, Ton humoristique...)"
                    value={item.customInstructions || ''}
                    onChange={(e) => updateStep(index, { customInstructions: e.target.value })}
                    style={{
                        width: '100%',
                        marginTop: '12px',
                        padding: '8px',
                        background: 'rgba(255, 255, 255, 0.03)',
                        border: '1px solid var(--border-color)',
                        borderRadius: '4px',
                        color: 'var(--text-primary)',
                        fontSize: '0.85rem',
                        resize: 'vertical',
                        minHeight: '60px',
                        fontFamily: 'inherit'
                    }}
                />
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

    const moveStep = (fromIndex, toIndex) => {
        setWorkflow(prev => {
            const updated = [...prev];
            const [removed] = updated.splice(fromIndex, 1);
            updated.splice(toIndex, 0, removed);
            return updated;
        });
    };

    const updateStep = (index, updates) => {
        setWorkflow(prev => {
            const updated = [...prev];
            updated[index] = { ...updated[index], ...updates };
            return updated;
        });
    };

    const removeModifier = (stepIndex, modifierIndex) => {
        setWorkflow(prev => {
            const updated = [...prev];
            const step = { ...updated[stepIndex] };
            step.modifiers = step.modifiers.filter((_, i) => i !== modifierIndex);
            updated[stepIndex] = step;
            return updated;
        });
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
                                moveStep={moveStep}
                                removeModifier={removeModifier}
                                updateStep={updateStep} // Pass the update function
                            />
                        ))}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Canvas;
