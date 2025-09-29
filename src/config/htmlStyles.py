import regex


def parseText(text: str) -> str:

    # Horizontal rule is handled in parseLine(), not here

    # Bold: **text**
    text = regex.sub(r"\*{2}(.*?)\*{2}", r"<strong>\1</strong>", text)

    # Italics: *text*
    text = regex.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

    # Strikethrough: ~~text~~
    text = regex.sub(r"\~{2}(.*?)\~{2}", r"<del>\1</del>", text)

    # Inline code: `code`
    text = regex.sub(r"`([^`]+)`", r"<code>\1</code>", text)

    # Links: [text](url)
    text = regex.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', text)

    return text


# Global variable to track code block state
in_code_block = False
code_block_content = []
code_block_language = ""

styles = {
    "#": lambda text: f"<h1>{parseText(text)}</h1>",
    "##": lambda text: f"<h2>{parseText(text)}</h2>",
    "###": lambda text: f"<h3>{parseText(text)}</h3>",
    "####": lambda text: f"<h4>{parseText(text)}</h4>",
    "#####": lambda text: f"<h5>{parseText(text)}</h5>",
    "######": lambda text: f"<h6>{parseText(text)}</h6>",
    "p": lambda text: f"<p>{parseText(text)}</p>",
    "-": lambda text: f"<li>{parseText(text)}</li>",
    "```": lambda text: f"<pre><code class='{text}'>",
}


def parseLine(line: str) -> str:
    global in_code_block, code_block_content, code_block_language
    stripped = line.strip()

    # Handle code blocks
    if stripped.startswith("```"):
        if not in_code_block:
            # Starting code block
            in_code_block = True
            code_block_language = stripped[3:].strip() if len(stripped) > 3 else ""
            code_block_content = []
            return "" 
        else:
            # Ending code block
            in_code_block = False
            code_content = "\n".join(code_block_content)
            result = f'<pre><code class="language-{code_block_language}">{code_content}</code></pre>'
            code_block_content = []
            return result

    if in_code_block:
        code_block_content.append(line) 
        return ""

    # Horizontal rule: ---
    if stripped == "---":
        return "<hr>"

    # List item: - text
    if stripped.startswith("- "):
        return styles["-"](stripped[2:].strip())

    # Headings: #, ##, ### etc.
    parts = stripped.split(" ", 1)
    if len(parts) == 2 and parts[0] in styles:
        return styles[parts[0]](parts[1])

    return f"<p>{parseText(stripped)}</p>"


def htmlHead():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Document</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
        }
        h1, h2, h3, h4, h5, h6 {
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: #2c3e50;
        }
        h1 { font-size: 2em; }
        h2 { font-size: 1.7em; }
        h3 { font-size: 1.4em; }
        p { margin-bottom: 1em; }
        code {
            background-color: #f8f9fa;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            color: #e74c3c;
        }
        pre {
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
            margin: 1em 0;
        }
        pre code {
            background-color: transparent;
            padding: 0;
            color: #333;
            font-size: 14px;
        }
        strong { color: #2c3e50; }
        em { color: #7f8c8d; }
        del { color: #95a5a6; }
        a {
            color: #3498db;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        li {
            margin-bottom: 0.5em;
        }
        ul {
            padding-left: 20px;
        }
        hr {
            border: none;
            border-top: 2px solid #ddd;
            margin: 20px 0;
        }
    </style>
</head>
<body>"""
