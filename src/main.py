from flask import Flask, abort
from config.htmlStyles import parseLine, htmlHead
from config.mdConfig import get_page_config, generate_css_from_config
import os

app = Flask(__name__)


@app.route("/<filename>", methods=["GET"])
def main(filename):
    file_path = f"src/md/{filename}.md"

    if not os.path.exists(file_path):
        abort(404)
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            md_content = file.read()

        lines = md_content.splitlines()
        html_content = ""

        for line in lines:
            if line.strip():
                html_content += "\n" + parseLine(line)

        # Get page configuration
        page_config = get_page_config()
        css_styles = generate_css_from_config(page_config)
        background = page_config.get("background", "#ffffff")

        # Wrap content with HTML structure and custom styles
        full_html = f"""<!DOCTYPE html>
                        <html>
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>{filename}</title>
                            <style>
                        {css_styles}
                            </style>
                        </head>
                        <body style="background-color: {background};">
                        {html_content}
                        </body>
                        </html>
                    """

        return full_html

    except FileNotFoundError:
        abort(404)
    except Exception as e:
        app.logger.error(f"Error processing file {filename}: {str(e)}")
        abort(500)


if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
