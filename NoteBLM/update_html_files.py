import re
import os

def remove_emojis_and_add_header(filepath, has_slides=False):
    """Remove emojis and add UIMM header to HTML file"""
    
    # Read file
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Emoji pattern (comprehensive)
    emoji_pattern = re.compile(
        r'[\U00010000-\U0010ffff]|'
        r'[\u2600-\u26ff\u2700-\u27bf\ufe00-\ufe0f]|'
        r'[\U0001f1e6-\U0001f1ff\U0001f300-\U0001f64f\U0001f680-\U0001f6ff]|'
        r'[\u2011-\u26ff\U0001f900-\U0001f9ff\U0001f600-\U0001f64f]',
        re.UNICODE
    )
    
    # Count emojis
    emojis_found = len(re.findall(emoji_pattern, content))
    print(f"{os.path.basename(filepath)}: Found {emojis_found} emojis")
    
    # Remove emojis
    content_no_emoji = emoji_pattern.sub('', content)
    
    # Add UIMM header CSS if not present
    if '.uimm-header' not in content_no_emoji:
        # Find the closing of style tag
        style_close_pos = content_no_emoji.find('</style>')
        if style_close_pos != -1:
            uimm_css = '''
        .uimm-header {
            background: white;
            padding: 20px 40px;
            display: flex;
            align-items: center;
            gap: 20px;
            border-bottom: 3px solid #0066a1;
        }

        .uimm-header img {
            height: 80px;
            width: auto;
        }

        .uimm-header h2 {
            color: #0066a1;
            font-size: 1.8em;
            margin: 0;
            border: none;
            padding: 0;
        }
    '''
            content_no_emoji = content_no_emoji[:style_close_pos] + uimm_css + content_no_emoji[style_close_pos:]
    
    # Add UIMM header HTML
    if has_slides:
        # For presentation with slides - add after presentation div
        if '<div class="presentation">' in content_no_emoji and '<!-- UIMM Header' not in content_no_emoji:
            header_html = '''<div class="presentation">
        <!-- UIMM Header -->
        <div class="uimm-header" style="position: fixed; top: 0; left: 0; right: 0; z-index: 1000;">
            <img src="logo_uimm_placeholder.jpg" alt="Logo UIMM">
            <h2>Pôle Formation UIMM - CVDL</h2>
        </div>

        '''
            content_no_emoji = content_no_emoji.replace('<div class="presentation">', header_html)
    else:
        # For regular pages - add after container opening
        if '<div class="container">' in content_no_emoji and '<!-- UIMM Header' not in content_no_emoji:
            header_html = '''<div class="container">
        <!-- UIMM Header -->
        <div class="uimm-header">
            <img src="logo_uimm_placeholder.jpg" alt="Logo UIMM">
            <h2>Pôle Formation UIMM - CVDL</h2>
        </div>

        '''
            content_no_emoji = content_no_emoji.replace('<div class="container">', header_html)
    
    # Write back
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content_no_emoji)
    
    print(f"{os.path.basename(filepath)}: Updated successfully!")
    return emojis_found

# Process all HTML files
files_to_process = [
    ('presentation_notebooklm.html', True),  # has slides
    ('scenario_tp_notebooklm.html', False),
    ('ressources_documentaires.html', False)
]

total_emojis = 0
for filename, has_slides in files_to_process:
    filepath = os.path.join(r'c:\Users\s.jaubert\projets\Cours-IA\NoteBLM', filename)
    if os.path.exists(filepath):
        count = remove_emojis_and_add_header(filepath, has_slides)
        total_emojis += count
    else:
        print(f"File not found: {filename}")

print(f"\n=== TOTAL: Removed {total_emojis} emojis from {len(files_to_process)} files ===")
