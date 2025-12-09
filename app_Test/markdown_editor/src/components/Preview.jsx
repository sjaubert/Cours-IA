import React, { useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { vscDarkPlus } from 'react-syntax-highlighter/dist/esm/styles/prism';
import 'katex/dist/katex.min.css';

/**
 * Preview component - Displays rendered Markdown with LaTeX support
 * Optimized with React.memo to prevent unnecessary re-renders
 */
const Preview = React.memo(({ markdown }) => {
    // Memoize the rendered markdown to avoid re-parsing on every render
    const renderedContent = useMemo(() => {
        return (
            <ReactMarkdown
                remarkPlugins={[remarkMath, remarkGfm]}
                rehypePlugins={[
                    [rehypeKatex, {
                        strict: false,
                        trust: true,
                        throwOnError: false,
                        errorColor: '#cc0000',
                        macros: {
                            "\\RR": "\\mathbb{R}",
                            "\\NN": "\\mathbb{N}",
                            "\\ZZ": "\\mathbb{Z}",
                            "\\QQ": "\\mathbb{Q}",
                            "\\CC": "\\mathbb{C}"
                        }
                    }],
                    rehypeRaw
                ]}
                components={{
                    // Custom code block renderer with syntax highlighting
                    code({ node, inline, className, children, ...props }) {
                        const match = /language-(\w+)/.exec(className || '');
                        const language = match ? match[1] : '';

                        return !inline && language ? (
                            <SyntaxHighlighter
                                style={vscDarkPlus}
                                language={language}
                                PreTag="div"
                                customStyle={{
                                    margin: '1rem 0',
                                    borderRadius: '6px',
                                    fontSize: '0.9em'
                                }}
                                {...props}
                            >
                                {String(children).replace(/\n$/, '')}
                            </SyntaxHighlighter>
                        ) : (
                            <code className={className} {...props}>
                                {children}
                            </code>
                        );
                    }
                }}
            >
                {markdown}
            </ReactMarkdown>
        );
    }, [markdown]);

    return (
        <div className="preview-content">
            <div className="markdown-preview">
                {renderedContent}
            </div>
        </div>
    );
});

Preview.displayName = 'Preview';

export default Preview;
