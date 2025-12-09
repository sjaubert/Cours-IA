import React from 'react';
import { Bold, Italic, Underline, Code, FunctionSquare } from 'lucide-react';

const Toolbar = ({ onInsert }) => {
    return (
        <div className="toolbar">
            <button
                className="toolbar-btn"
                onClick={() => onInsert('bold')}
                title="Bold (Ctrl+B)"
            >
                <Bold size={18} />
            </button>
            <button
                className="toolbar-btn"
                onClick={() => onInsert('italic')}
                title="Italic (Ctrl+I)"
            >
                <Italic size={18} />
            </button>
            <button
                className="toolbar-btn"
                onClick={() => onInsert('underline')}
                title="Underline (Ctrl+U)"
            >
                <Underline size={18} />
            </button>
            <div style={{ width: '1px', height: '24px', background: 'var(--border-color)', margin: '0 0.5rem' }} />
            <button
                className="toolbar-btn"
                onClick={() => onInsert('latex-inline')}
                title="Inline Math ($...$)"
            >
                <FunctionSquare size={18} />
            </button>
            <button
                className="toolbar-btn"
                onClick={() => onInsert('latex-block')}
                title="Block Math ($$...$$)"
            >
                <Code size={18} />
            </button>
        </div>
    );
};

export default Toolbar;
