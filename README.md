### README for AI Response Generator Project

# AI Response Generator

This project provides a script to generate AI responses for user prompts stored in an input file. It uses Google Generative AI to generate responses, saves the responses in a Markdown file, and then converts the Markdown file to a PDF.

## Features

- Reads user prompts from `input.txt`.
- Generates AI responses using Google Generative AI.
- Saves the prompts and responses in a formatted Markdown file (`output.md`).
- Converts the Markdown file to a PDF (`output.pdf`).

## Prerequisites

- Python 3.x
- `google-generativeai` library
- `markdown` library
- `pdfkit` library
- `wkhtmltopdf` installed on your system

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ai-response-generator.git
   cd ai-response-generator
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install google-generativeai markdown pdfkit
   ```

3. **Install `wkhtmltopdf`**:
   - **On Linux**:
     ```bash
     sudo apt update
     sudo apt install wkhtmltopdf
     ```
   - **On macOS**:
     ```bash
     brew install wkhtmltopdf
     ```
   - **On Windows**:
     Download the installer from [wkhtmltopdf.org](https://wkhtmltopdf.org/downloads.html) and follow the installation instructions. Ensure the executable is added to your system PATH.

## Configuration

1. **Set Up Google Generative AI**:
   - Obtain an API key from Google Generative AI.
   - Set the environment variable `GOOGLE_API_KEY` with your API key:
     ```bash
     export GOOGLE_API_KEY='your_api_key_here'
     ```

## Usage

1. **Prepare Input File**:
   - Create an `input.txt` file with user prompts separated by `----`.
     ```
     Prompt 1 text
     ----
     Prompt 2 text
     ----
     Prompt 3 text
   

2. **Run the Script**:
   - Execute the script to generate responses and create the output files:
     ```bash
     python generate_ai_responses.py
     ```

3. **Output Files**:
   - `output.md`: A Markdown file with user prompts and AI responses.
   - `output.pdf`: A PDF file converted from the Markdown file.

