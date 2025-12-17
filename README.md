# Gemini API Function Calling Demo

This project demonstrates how to use the Google Gemini API (specifically the `gemini-2.5-flash` model) to perform **Function Calling**. 

## Prerequisites

* Python 3.8 or higher
* A Google Cloud/AI Studio account with access to the Gemini API.
* [SDK Documentation](https://github.com/googleapis/python-genai)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: If `requirements.txt` is missing, run: `pip install google-genai python-dotenv`)*

## Configuration

**Important:** This project requires a valid Gemini API key. Never commit your API key directly to GitHub.

1.  **Get your API Key:**
    Visit [Google AI Studio](https://aistudio.google.com/) to generate a new API key.

2.  **Set up environment variables:**
    Create a file named `.env` in the root directory of the project.

3.  **Add your key to the file:**
    Open `.env` and add the following line:
    ```text
    GEMINI_API_KEY=your_actual_api_key_here
    ```

## Usage

Run the script using Python:

```bash
python main.py
