import os
import json


def FetchConfigs():
    config_path = os.path.join(os.path.dirname(__file__), "../../.md.config")

    if not os.path.exists(config_path):
        return get_default_config()

    try:
        with open(config_path, "r", encoding="utf-8") as file:
            content = file.read()

            if content.startswith("config = "):
                json_content = content[9:]
                return json.loads(json_content)
            else:
                return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Error loading config: {e}")
        return get_default_config()


def get_default_config():
    return {
        "server": {"port": 3000, "host": "0.0.0.0", "debug": False},
        "pages": {
            "default": {
                "background": "#ffffff",
                "styles": {
                    "body": {
                        "font-family": "Arial, sans-serif",
                        "line-height": "1.6",
                        "margin": "0 auto",
                        "max-width": "800px",
                        "padding": "20px",
                    }
                },
                "customCSS": "",
            }
        },
        "global": {"theme": "default", "responsive": True, "darkMode": False},
    }


def get_page_config(page_path="default"):
    config = FetchConfigs()
    pages = config.get("pages", {})

    if page_path in pages:
        return pages[page_path]
    elif "default" in pages:
        return pages["default"]
    else:
        return (
            next(iter(pages.values()))
            if pages
            else get_default_config()["pages"]["default"]
        )


def get_server_config():
    config = FetchConfigs()
    server_config = config.get("server", {})
    default_server = get_default_config()["server"]

    return {
        "port": server_config.get("port", default_server["port"]),
        "host": server_config.get("host", default_server["host"]),
        "debug": server_config.get("debug", default_server["debug"]),
    }


def generate_css_from_config(page_config):
    css = ""
    styles = page_config.get("styles", {})

    for selector, properties in styles.items():
        css += f"{selector} {{\n"
        for prop, value in properties.items():
            css += f"    {prop}: {value};\n"
        css += "}\n\n"

    # Add custom CSS
    custom_css = page_config.get("customCSS", "")
    if custom_css:
        css += custom_css + "\n"

    return css
