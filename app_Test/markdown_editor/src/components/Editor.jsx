import React, { useRef } from 'react';

const Editor = ({ value, onChange, onCommand, editorRef }) => {

    const handleKeyDown = (e) => {
        // Shortcuts
        if (e.ctrlKey) {
            if (e.key === 'b') {
                e.preventDefault();
                onCommand('bold');
            } else if (e.key === 'i') {
                e.preventDefault();
                onCommand('italic');
            } else if (e.key === 'u') {
                e.preventDefault();
                onCommand('underline');
            }
        }
    };

    return (
        <textarea
            ref={editorRef}
            className="editor-textarea"
            value={value}
            onChange={onChange}
            onKeyDown={handleKeyDown}
            placeholder="# Welcome to Markdown Pro..."
            spellCheck="false"
        />
    );
};

export default Editor;
