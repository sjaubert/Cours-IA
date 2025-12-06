import React, { useState, useRef } from 'react';
import Toolbar from './components/Toolbar';
import Editor from './components/Editor';
import Preview from './components/Preview';
import './index.css';

function App() {
  const [markdown, setMarkdown] = useState('# Welcome to Markdown Pro\n\nType some markdown here...\n\nTry **bold** (Ctrl+B), _italic_ (Ctrl+I), or <u>underline</u> (Ctrl+U).\n\nAlso supports LaTeX math:\n\n$$ E = mc^2 $$');
  const editorRef = useRef(null);

  const handleCommand = (type) => {
    const textarea = editorRef.current;
    if (!textarea) return;

    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const text = textarea.value;
    const selection = text.substring(start, end);

    let prefix = '';
    let suffix = '';
    let placeholder = '';

    switch (type) {
      case 'bold':
        prefix = '**';
        suffix = '**';
        placeholder = 'bold text';
        break;
      case 'italic':
        prefix = '_';
        suffix = '_';
        placeholder = 'italic text';
        break;
      case 'underline':
        prefix = '<u>';
        suffix = '</u>';
        placeholder = 'underlined text';
        break;
      case 'latex-inline':
        prefix = '$';
        suffix = '$';
        placeholder = 'math';
        break;
      case 'latex-block':
        prefix = '\n$$\n';
        suffix = '\n$$\n';
        placeholder = 'Content';
        break;
      default:
        return;
    }

    const newText = text.substring(0, start) +
      prefix + (selection || placeholder) + suffix +
      text.substring(end);

    // Update state directly
    setMarkdown(newText);

    // Restore selection/focus after render
    const newSelectionStart = start + prefix.length;
    const newSelectionEnd = newSelectionStart + (selection.length || placeholder.length);

    requestAnimationFrame(() => {
      if (editorRef.current) {
        editorRef.current.value = newText; // Ensure immediate sync if needed by React? 
        // Actually React state update will trigger re-render and value update.
        // But we need to set selection AFTER that.
        editorRef.current.selectionStart = newSelectionStart;
        editorRef.current.selectionEnd = newSelectionEnd;
        editorRef.current.focus();
      }
    });
  };

  return (
    <div className="app-container">
      <header className="header">
        <div className="logo">Markdown Pro</div>
        {/* Placeholder for future features like Save/Load */}
      </header>

      <div className="pane-header">
        <Toolbar onInsert={handleCommand} />
      </div>

      <div className="main-content">
        <div className="pane editor-pane">
          <Editor
            value={markdown}
            onChange={(e) => setMarkdown(e.target.value)}
            onCommand={handleCommand}
            editorRef={editorRef}
          />
        </div>
        <div className="pane preview-pane">
          <Preview markdown={markdown} />
        </div>
      </div>
    </div>
  );
}

export default App;
