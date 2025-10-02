# README

## Installation

To use this project, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/CodeByNavin/.md-html.git
   ```
2. Navigate to the project directory:
   ```
   cd .md-html
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main script:
   ```
   python src/main.py
   ```
2. Access the application in your web browser at `http://localhost:3000/<filename>`, where `<filename>` is the name of the Markdown file you want to view (e.g., `http://localhost:3000/test`).

## Configuration

### .md.config File

The `.md.config` file allows you to customize the styling of your rendered Markdown files. Place this file in the root directory of your project.

#### Basic Structure

```javascript
config = {
    "pages": {
        "default": {
            "background": "#ffffff",
            "styles": {
                "body": {
                    "font-family": "Arial, sans-serif",
                    "line-height": "1.6",
                    "margin": "0 auto",
                    "max-width": "800px",
                    "padding": "20px"
                },
                "h1": {
                    "color": "#333",
                    "border-bottom": "2px solid #eee"
                },
                "code": {
                    "background-color": "#f4f4f4",
                    "padding": "2px 4px",
                    "border-radius": "3px"
                }
            },
            "customCSS": ""
        }
    },
    "global": {
        "theme": "default",
        "responsive": true,
        "darkMode": false
    }
}
```

#### Page-Specific Styling

You can create different styles for different pages:

```javascript
config = {
    "server": {
        "port": 3000,
        "host": "0.0.0.0",
        "debug": false
    },
    "pages": {
        "default": { /* default styles */ },
        "blog": {
            "background": "#f8f9fa",
            "styles": {
                "body": {
                    "font-family": "Georgia, serif",
                    "max-width": "700px"
                }
            }
        },
        "documentation": {
            "background": "#ffffff",
            "styles": {
                "code": {
                    "background-color": "#282c34",
                    "color": "#abb2bf"
                }
            }
        }
    }
}
```

#### Configuration Options

- **`background`**: Page background color
- **`styles`**: CSS styles for HTML elements (body, h1, h2, code, pre, blockquote, etc.)
- **`customCSS`**: Additional custom CSS rules
- **`global.theme`**: Theme selection
- **`global.responsive`**: Enable/disable responsive design
- **`global.darkMode`**: Enable/disable dark mode support

The system will automatically apply the appropriate styles based on your configuration when rendering Markdown files.