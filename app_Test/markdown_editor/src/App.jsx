import React, { useState, useRef, useEffect, useLayoutEffect, useCallback } from 'react';
import { saveAs } from 'file-saver';
import Toolbar from './components/Toolbar';
import Editor from './components/Editor';
import Preview from './components/Preview';
import './index.css';

const STORAGE_KEY = 'markdown-editor-content';

// Initial example content with LaTeX
const INITIAL_CONTENT = `# Welcome to Markdown Pro 🚀

Type some markdown here and see it rendered in real-time!

## Features

- **Bold** (Ctrl+B), *italic* (Ctrl+I), and <u>underline</u> (Ctrl+U)
- Syntax highlighting for code blocks
- LaTeX math support (inline and block)
- Auto-save to localStorage
- Export to HTML or Markdown

## Code Example

\`\`\`javascript
function fibonacci(n) {
  if (n <= 1) return n;
  return fibonacci(n - 1) + fibonacci(n - 2);
}

console.log(fibonacci(10)); // 55
\`\`\`

## Math Examples

Inline math: The famous equation $E = mc^2$ shows mass-energy equivalence.

Block math:
$$
\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}
$$

Matrix notation:
$$
\\begin{bmatrix}
a & b \\\\
c & d
\\end{bmatrix}
\\begin{bmatrix}
x \\\\
y
\\end{bmatrix}
=
\\begin{bmatrix}
ax + by \\\\
cx + dy
\\end{bmatrix}
$$

Summation:
$$
\\sum_{i=1}^{n} i = \\frac{n(n+1)}{2}
$$

---

Start editing to see the magic! ✨`;

function App() {
  // Load content from localStorage or use initial content
  const [markdown, setMarkdown] = useState(() => {
    const saved = localStorage.getItem(STORAGE_KEY);
    return saved || INITIAL_CONTENT;
  });

  const editorRef = useRef(null);
  const selectionRef = useRef({ start: 0, end: 0 });
  const shouldRestoreSelection = useRef(false);

  // Auto-save to localStorage whenever markdown changes
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      localStorage.setItem(STORAGE_KEY, markdown);
    }, 1000); // Debounce for 1 second

    return () => clearTimeout(timeoutId);
  }, [markdown]);

  // Memoized command handler
  const handleCommand = useCallback((type) => {
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
      // Text Formatting
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

      // Headings
      case 'h1':
        prefix = '# ';
        suffix = '';
        placeholder = 'Heading 1';
        break;
      case 'h2':
        prefix = '## ';
        suffix = '';
        placeholder = 'Heading 2';
        break;
      case 'h3':
        prefix = '### ';
        suffix = '';
        placeholder = 'Heading 3';
        break;

      // Lists & Quotes
      case 'ul':
        prefix = '- ';
        suffix = '';
        placeholder = 'List item';
        break;
      case 'ol':
        prefix = '1. ';
        suffix = '';
        placeholder = 'List item';
        break;
      case 'quote':
        prefix = '> ';
        suffix = '';
        placeholder = 'Quote text';
        break;
      case 'code-block':
        prefix = '\n```\n';
        suffix = '\n```\n';
        placeholder = 'code here';
        break;

      // Math Basic
      case 'latex-inline':
        prefix = '$';
        suffix = '$';
        placeholder = 'E = mc^2';
        break;
      case 'latex-block':
        prefix = '\n$$\n';
        suffix = '\n$$\n';
        placeholder = '\\int_{-\\infty}^{\\infty} e^{-x^2} dx = \\sqrt{\\pi}';
        break;
      case 'fraction':
        prefix = '$\\frac{';
        suffix = '}$';
        placeholder = 'a}{b';
        break;
      case 'sqrt':
        prefix = '$\\sqrt{';
        suffix = '}$';
        placeholder = 'x';
        break;
      case 'power':
        prefix = '$x^{';
        suffix = '}$';
        placeholder = 'n';
        break;
      case 'subscript':
        prefix = '$x_{';
        suffix = '}$';
        placeholder = 'i';
        break;

      // Math Advanced
      case 'sum':
        prefix = '$\\sum_{';
        suffix = '}$';
        placeholder = 'i=1}^{n';
        break;
      case 'integral':
        prefix = '$\\int_{';
        suffix = '}$';
        placeholder = 'a}^{b';
        break;
      case 'product':
        prefix = '$\\prod_{';
        suffix = '}$';
        placeholder = 'i=1}^{n';
        break;
      case 'limit':
        prefix = '$\\lim_{';
        suffix = '}$';
        placeholder = 'x \\to \\infty';
        break;

      // Structures
      case 'matrix':
        prefix = '\n$$\n\\begin{bmatrix}\n';
        suffix = '\n\\end{bmatrix}\n$$\n';
        placeholder = 'a & b \\\\\nc & d';
        break;
      case 'vector':
        prefix = '$\\vec{';
        suffix = '}$';
        placeholder = 'v';
        break;
      case 'cases':
        prefix = '\n$$\nf(x) = \\begin{cases}\n';
        suffix = '\n\\end{cases}\n$$\n';
        placeholder = 'x^2 & \\text{if } x \\geq 0 \\\\\n-x & \\text{if } x < 0';
        break;

      // Greek Letters & Symbols
      case 'alpha':
        prefix = '$\\alpha$';
        suffix = '';
        placeholder = '';
        break;
      case 'beta':
        prefix = '$\\beta$';
        suffix = '';
        placeholder = '';
        break;
      case 'theta':
        prefix = '$\\theta$';
        suffix = '';
        placeholder = '';
        break;
      case 'pi':
        prefix = '$\\pi$';
        suffix = '';
        placeholder = '';
        break;
      case 'infinity':
        prefix = '$\\infty$';
        suffix = '';
        placeholder = '';
        break;

      // File Operations
      case 'save':
        // Manual save (already auto-saving, but provide feedback)
        localStorage.setItem(STORAGE_KEY, markdown);
        console.log('💾 Saved!');
        return;
      case 'export-html':
        exportAsHTML();
        return;
      case 'export-md':
        exportAsMarkdown();
        return;
      case 'clear':
        if (confirm('Are you sure you want to clear all content?')) {
          setMarkdown('');
          localStorage.removeItem(STORAGE_KEY);
          console.log('🗑️ Cleared!');
        }
        return;
      default:
        return;
    }

    const newText = text.substring(0, start) +
      prefix + (selection || placeholder) + suffix +
      text.substring(end);

    // Update markdown state
    setMarkdown(newText);

    // Store selection for restoration after render
    const newSelectionStart = start + prefix.length;
    const newSelectionEnd = newSelectionStart + (selection.length || placeholder.length);
    selectionRef.current = { start: newSelectionStart, end: newSelectionEnd };

    // Flag that we need to restore selection after this update
    shouldRestoreSelection.current = true;
  }, [markdown]);

  // Restore selection after markdown update ONLY when needed
  // Using useLayoutEffect to run synchronously before browser paint
  useLayoutEffect(() => {
    if (shouldRestoreSelection.current && editorRef.current && selectionRef.current) {
      const { start, end } = selectionRef.current;
      editorRef.current.setSelectionRange(start, end);
      editorRef.current.focus();
      shouldRestoreSelection.current = false; // Reset flag
    }
  });

  // Export as HTML
  const exportAsHTML = useCallback(() => {
    const htmlContent = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Export</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.25/dist/katex.min.css">
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            max-width: 800px;
            margin: 2rem auto;
            padding: 2rem;
            line-height: 1.6;
            color: #333;
        }
        code { background: #f4f4f4; padding: 0.2em 0.4em; border-radius: 3px; }
        pre { background: #f4f4f4; padding: 1rem; border-radius: 6px; overflow-x: auto; }
        blockquote { border-left: 4px solid #38bdf8; padding-left: 1rem; color: #666; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 0.5rem; }
        th { background: #f4f4f4; }
    </style>
</head>
<body>
    <div id="content"></div>
    <script type="module">
        import { marked } from 'https://cdn.jsdelivr.net/npm/marked@11.0.0/+esm';
        import katex from 'https://cdn.jsdelivr.net/npm/katex@0.16.25/+esm';
        
        const markdown = ${JSON.stringify(markdown)};
        
        // Simple LaTeX rendering
        let processed = markdown.replace(/\\$\\$([^$]+)\\$\\$/g, (match, latex) => {
            try {
                return katex.renderToString(latex, { displayMode: true });
            } catch (e) {
                return match;
            }
        });
        
        processed = processed.replace(/\\$([^$]+)\\$/g, (match, latex) => {
            try {
                return katex.renderToString(latex, { displayMode: false });
            } catch (e) {
                return match;
            }
        });
        
        document.getElementById('content').innerHTML = marked.parse(processed);
    </script>
</body>
</html>`;

    const blob = new Blob([htmlContent], { type: 'text/html;charset=utf-8' });
    saveAs(blob, 'markdown-export.html');
    console.log('📥 Exported as HTML!');
  }, [markdown]);

  // Export as Markdown
  const exportAsMarkdown = useCallback(() => {
    const blob = new Blob([markdown], { type: 'text/markdown;charset=utf-8' });
    saveAs(blob, 'document.md');
    console.log('📥 Exported as Markdown!');
  }, [markdown]);

  return (
    <div className="app-container">
      <header className="header">
        <div className="logo">Markdown Pro</div>
        <div className="header-actions">
          <button
            className="header-btn"
            onClick={() => handleCommand('export-html')}
            title="Export as HTML"
          >
            📥 HTML
          </button>
          <button
            className="header-btn"
            onClick={() => handleCommand('export-md')}
            title="Export as Markdown"
          >
            📥 MD
          </button>
          <button
            className="header-btn clear-btn"
            onClick={() => handleCommand('clear')}
            title="Clear all content"
          >
            🗑️ Clear
          </button>
        </div>
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
