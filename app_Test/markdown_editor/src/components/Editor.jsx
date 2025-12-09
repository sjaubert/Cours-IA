import React, { useCallback } from 'react';

/**
 * Editor component - Markdown text editor with keyboard shortcuts
 * Optimized with React.memo to prevent unnecessary re-renders
 */
const Editor = React.memo(({ value, onChange, onCommand, editorRef }) => {
    // Memoize keyboard shortcut handler
    const handleKeyDown = useCallback((e) => {
        // Shortcuts
        if (e.ctrlKey || e.metaKey) {
            if (e.key === 'b') {
                e.preventDefault();
                onCommand('bold');
            } else if (e.key === 'i') {
                e.preventDefault();
                onCommand('italic');
            } else if (e.key === 'u') {
                e.preventDefault();
                onCommand('underline');
            } else if (e.key === 's') {
                e.preventDefault();
                onCommand('save');
            }
        }
    }, [onCommand]);

    return (
        <textarea
            ref={editorRef}
            className="editor-textarea"
            value={value}
            onChange={onChange}
            onKeyDown={handleKeyDown}
            placeholder="# Welcome to Markdown Pro...

Start typing your markdown here!

**Bold**, *italic*, ~~strikethrough~~

- Lists
- Are
- Easy

```javascript
// Code blocks with syntax highlighting
const hello = 'world';
```

Inline math: $E = mc^2$

Block math:
$$
\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}
$$"
            spellCheck="false"
        />
    );
});

Editor.displayName = 'Editor';

export default Editor;
