
import React, { useState } from 'react';
import Header from './Header';
import Sidebar from './Sidebar';
import Canvas from './Canvas';
import CodePreview from './CodePreview';
import { ROLES, LEVELS } from '../../data/constants';

const Layout = () => {
    // Global State for the Prompt Configuration
    const [context, setContext] = useState({
        subject: '',
        role: ROLES[0].id,
        level: LEVELS[1].id, // Default Niveau IV
        sources: { includeWeb: false, includeFiles: false },
        output: { creativity: 'balanced', density: 'standard' }
    });

    const [workflow, setWorkflow] = useState([]); // List of commands in the sequence

    return (
        <div style={{ height: '100vh', display: 'flex', flexDirection: 'column' }}>
            <Header />

            <main style={{
                flex: 1,
                display: 'grid',
                gridTemplateColumns: '300px 1fr 350px',
                overflow: 'hidden'
            }}>
                {/* Left Panel: Context & Palette */}
                <div style={{ borderRight: '1px solid var(--border-color)', overflowY: 'auto' }}>
                    <Sidebar context={context} setContext={setContext} />
                </div>

                {/* Center Panel: Workflow Canvas */}
                <div style={{ background: '#000', position: 'relative', overflow: 'hidden' }}>
                    <Canvas workflow={workflow} setWorkflow={setWorkflow} />
                </div>

                {/* Right Panel: Output Preview */}
                <div style={{ borderLeft: '1px solid var(--border-color)', background: 'var(--bg-panel)', overflowY: 'auto' }}>
                    <CodePreview context={context} workflow={workflow} />
                </div>
            </main>
        </div>
    );
};

export default Layout;
