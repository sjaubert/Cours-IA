
import React from 'react';
import logo from '../../assets/logo_uimm_placeholder.jpg';

const Header = () => {
    return (
        <header style={{
            height: '60px',
            background: 'var(--bg-panel)',
            borderBottom: '1px solid var(--border-color)',
            display: 'flex',
            alignItems: 'center',
            padding: '0 20px',
            justifyContent: 'space-between'
        }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '16px' }}>
                <img
                    src={logo}
                    alt="Pôle Formation UIMM"
                    style={{ height: '50px', borderRadius: '4px' }}
                />
                <div>
                    <h1 style={{ margin: 0, fontSize: '1.2rem', fontWeight: 600 }}>PromptFlow Pôle Formation UIMM-CVDL</h1>
                    <span style={{ fontSize: '0.8rem', color: 'var(--text-secondary)' }}>Studio de Création Pédagogique</span>
                </div>
            </div>

            <div style={{ display: 'flex', gap: '8px' }}>
                {/* Actions header if needed */}
            </div>
        </header>
    );
};

export default Header;
