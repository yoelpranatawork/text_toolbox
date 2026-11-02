# Text Toolbox

A lightweight desktop application built with Python and Tkinter that provides useful text manipulation, cleaning, and developer utilities in one place.

Text Toolbox is designed to make everyday text-processing tasks easier through a simple graphical interface, without relying on external websites or online services.

## Features

### 1. Case Conversion

Quickly change the letter case of your text.

- **UPPERCASE** – Converts all letters to uppercase.
- **lowercase** – Converts all letters to lowercase.
- **Title Case** – Capitalizes the first letter of each word.
- **Sentence Case** – Capitalizes the first character of the text.
- **Invert Case** – Swaps uppercase letters to lowercase and vice versa.

### 2. Text Cleaning

Clean and normalize your text with various utilities.

- **Remove Leading/Trailing Spaces** – Removes leading and trailing spaces or tabs from each line.
- **Remove Extra Spaces** – Removes consecutive spaces while preserving leading and trailing spaces.
- **Remove Blank Lines** – Removes empty or whitespace-only lines.
- **Remove Duplicate Lines** – Removes duplicate lines while preserving their original order.
- **Remove Special Characters** – Removes characters other than letters, numbers, spaces, tabs, and line breaks.
- **Remove Digits** – Removes all numeric digits.
- **Remove Tabs** – Removes tab characters.
- **Normalize to ASCII** – Converts supported Unicode characters into ASCII equivalents and removes unsupported characters.
- **Normalize Line Endings** – Converts line endings into one of three formats:
  - Windows (`CRLF`)
  - Unix (`LF`)
  - Classic Mac (`CR`)

### 3. Developer Tools

Useful utilities for common development tasks.

- **Minify Python Code** – Removes comments and docstrings from Python code using the Abstract Syntax Tree (AST).
- **Base64 Encode** – Encodes text into Base64 format.
- **Base64 Decode** – Decodes Base64-encoded text.
- **Format JSON** – Validates and pretty-prints JSON with indentation.
- **URL Encode** – Encodes text for use in URLs.
- **URL Decode** – Decodes URL-encoded text.

### 4. Additional Features

- Side-by-side input and output text areas.
- Live character, word, and line counters.
- Copy output to clipboard.
- Select all input or output text.
- Replace input with processed output.
- Clear both text areas.
- Automatically enables or disables processing buttons depending on input content.
- Simple and intuitive graphical user interface.

## Requirements

- Python 3.9 or later.
- Tkinter (usually included with Python).

No additional Python packages are required to run the application.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yoelpranatawork/text_toolbox.git
```

### 2. Navigate to the project directory

```bash
cd textoolbox
```

### 3. Run the application

```bash
python app.py
```

The Text Toolbox window should open.

## Usage

1. Launch the application using `python app.py`.
2. Enter or paste your text into the **Input** area.
3. Choose a tool from one of the available categories:
   - Case Conversion
   - Text Cleaning
   - Developer Tools
4. The processed result will appear in the **Output** area.
5. Use the available action buttons to copy, select, replace, or clear text.

## Project Structure

```text
textoolbox/
│
├── core/
│   ├── case_tools.py
│   ├── cleaner_tools.py
│   └── developer_tools.py
│
├── app.py
├── gui.py
├── LICENSE
└── requirements.txt
```

### File Descriptions

| File / Directory | Description |
|---|---|
| `core/` | Contains the application's text-processing utilities. |
| `case_tools.py` | Case conversion functions. |
| `cleaner_tools.py` | Text cleaning and normalization functions. |
| `developer_tools.py` | Developer utilities, including Base64, JSON, URL encoding, and Python code minification. |
| `app.py` | Application entry point. |
| `gui.py` | Tkinter graphical user interface. |
| `LICENSE` | Project license information. |
| `requirements.txt` | Optional build dependencies. |

## Dependencies

The application uses Python standard-library modules:

- `tkinter` – Graphical user interface.
- `unicodedata` – Unicode normalization.
- `base64` – Base64 encoding and decoding.
- `json` – JSON parsing and formatting.
- `ast` – Python code parsing.
- `urllib.parse` – URL encoding and decoding.

No third-party packages are needed to run the application.

## Building an Executable

Text Toolbox can be packaged into a standalone executable using PyInstaller.

### 1. Install PyInstaller

```bash
pip install -r requirements.txt
```

### 2. Build the application

```bash
pyinstaller --onefile --windowed --name "Text Toolbox" app.py
```

### 3. Locate the executable

After the build completes, the generated executable will be available in the `dist/` directory.

**Note:** The executable is generated for the operating system on which PyInstaller is running. Build separately for each target operating system.

## License

This project is licensed under the **PolyForm Noncommercial License 1.0.0**.

You are free to use, modify, and distribute this software for noncommercial purposes, subject to the terms and conditions of the license.

**Commercial use requires a separate written licensing agreement with the copyright holder.**

If you are interested in using Text Toolbox for commercial purposes, please contact the copyright holder to discuss commercial licensing.

See the [LICENSE](LICENSE) file for the complete license terms.

Official license:
https://polyformproject.org/licenses/noncommercial/1.0.0/

## Disclaimer

Text Toolbox is provided **"AS IS" and "AS AVAILABLE"**, without any warranties or guarantees of any kind, express or implied.

The author makes no guarantees regarding the accuracy, reliability, suitability, or fitness of the application for any particular purpose.

There is no obligation to provide future updates, improvements, maintenance, technical support, bug fixes, or continued development. The author reserves the right to discontinue development or support at any time without prior notice.

Users are solely responsible for how they use this application and for any consequences resulting from its use. The author does not endorse or assume responsibility for any misuse of the application, including any unlawful, unethical, or otherwise questionable activities carried out using it.

To the fullest extent permitted by applicable law, the author shall not be held liable for any direct, indirect, incidental, consequential, or other damages arising from the use of, inability to use, or misuse of this application.

By using this application, you acknowledge and accept these limitations.

## Acknowledgments

Built with Python and Tkinter.

---

**Text Toolbox** – Simple, practical, and convenient text utilities in one application.
