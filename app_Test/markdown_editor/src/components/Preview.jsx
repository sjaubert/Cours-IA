import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import rehypeRaw from 'rehype-raw';
import 'katex/dist/katex.min.css';

const Preview = ({ markdown }) => {
    return (
        <div className="preview-content">
            <div className="markdown-preview">
                <ReactMarkdown
                    remarkPlugins={[remarkMath]}
                    rehypePlugins={[rehypeKatex, rehypeRaw]}
                >
                    {markdown}
                </ReactMarkdown>
            </div>
        </div>
    );
};

export default Preview;
