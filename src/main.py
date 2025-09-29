from flask import Flask, abort
from config.htmlStyles import parseLine, htmlHead
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

        # Wrap content with HTML structure
        full_html = htmlHead() + html_content + "\n</body>\n</html>"
        return full_html

    except FileNotFoundError:
        abort(404)
    except Exception as e:
        app.logger.error(f"Error processing file {filename}: {str(e)}")
        abort(500)

if __name__ == "__main__":
    app.run("0.0.0.0", 3000)
