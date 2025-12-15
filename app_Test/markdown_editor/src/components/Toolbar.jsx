import React from 'react';
import { 
    Bold, Italic, Underline, Code, FunctionSquare,
    Heading1, Heading2, Heading3, List, ListOrdered,
    Quote, FileCode, Sigma, Radical, Superscript, Subscript,
    BoxSelect, PieChart, Infinity, Plus, Minus, X, Divide
} from 'lucide-react';

const Toolbar = ({ onInsert }) => {
    return (
        <div className="toolbar">
            {/* Text Formatting Section */}
            <div className="toolbar-section">
                <span className="toolbar-label">Format</span>
                <div className="toolbar-group">
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
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Headings Section */}
            <div className="toolbar-section">
                <span className="toolbar-label">Titres</span>
                <div className="toolbar-group">
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('h1')}
                        title="Heading 1"
                    >
                        <Heading1 size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('h2')}
                        title="Heading 2"
                    >
                        <Heading2 size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('h3')}
                        title="Heading 3"
                    >
                        <Heading3 size={18} />
                    </button>
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Lists & Quotes */}
            <div className="toolbar-section">
                <span className="toolbar-label">Listes</span>
                <div className="toolbar-group">
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('ul')}
                        title="Unordered List"
                    >
                        <List size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('ol')}
                        title="Ordered List"
                    >
                        <ListOrdered size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('quote')}
                        title="Blockquote"
                    >
                        <Quote size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('code-block')}
                        title="Code Block"
                    >
                        <FileCode size={18} />
                    </button>
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Math Basic */}
            <div className="toolbar-section">
                <span className="toolbar-label">Math</span>
                <div className="toolbar-group">
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
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('fraction')}
                        title="Fraction \frac{a}{b}"
                    >
                        <span style={{ fontSize: '14px', fontWeight: 'bold' }}>a/b</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('sqrt')}
                        title="Square Root \sqrt{x}"
                    >
                        <Radical size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('power')}
                        title="Power x^{n}"
                    >
                        <Superscript size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('subscript')}
                        title="Subscript x_{n}"
                    >
                        <Subscript size={18} />
                    </button>
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Math Advanced */}
            <div className="toolbar-section">
                <span className="toolbar-label">Calcul</span>
                <div className="toolbar-group">
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('sum')}
                        title="Summation \sum"
                    >
                        <Sigma size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('integral')}
                        title="Integral \int"
                    >
                        <span style={{ fontSize: '16px', fontWeight: 'bold' }}>∫</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('product')}
                        title="Product \prod"
                    >
                        <span style={{ fontSize: '16px', fontWeight: 'bold' }}>∏</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('limit')}
                        title="Limit \lim"
                    >
                        <span style={{ fontSize: '12px', fontWeight: 'bold' }}>lim</span>
                    </button>
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Structures */}
            <div className="toolbar-section">
                <span className="toolbar-label">Structures</span>
                <div className="toolbar-group">
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('matrix')}
                        title="Matrix 2x2"
                    >
                        <BoxSelect size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('vector')}
                        title="Vector"
                    >
                        <span style={{ fontSize: '14px', fontWeight: 'bold' }}>→v</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('cases')}
                        title="Piecewise Function"
                    >
                        <span style={{ fontSize: '14px', fontWeight: 'bold' }}>{'{}'}</span>
                    </button>
                </div>
            </div>

            <div className="toolbar-divider" />

            {/* Greek Letters */}
            <div className="toolbar-section">
                <span className="toolbar-label">Symboles</span>
                <div className="toolbar-group">
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('alpha')}
                        title="Alpha α"
                    >
                        <span style={{ fontSize: '16px' }}>α</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('beta')}
                        title="Beta β"
                    >
                        <span style={{ fontSize: '16px' }}>β</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('theta')}
                        title="Theta θ"
                    >
                        <span style={{ fontSize: '16px' }}>θ</span>
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('pi')}
                        title="Pi π"
                    >
                        <PieChart size={18} />
                    </button>
                    <button
                        className="toolbar-btn"
                        onClick={() => onInsert('infinity')}
                        title="Infinity ∞"
                    >
                        <Infinity size={18} />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default Toolbar;
