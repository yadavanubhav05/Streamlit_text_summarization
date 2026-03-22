# Streamlit Text Summarization App

A simple web application built with Streamlit that uses Google's Gemini AI to summarize text input by users.

## Features

- **Text Summarization**: Enter any text and get a concise summary in English (max 20 words)
- **AI-Powered**: Utilizes Google's Gemini Pro model for high-quality summarization
- **User-Friendly Interface**: Clean Streamlit UI for easy text input and output display
- **Configurable Parameters**: Optimized model settings for consistent, concise summaries

## Requirements

- Python 3.14 or higher
- Google AI API key (Gemini API access)
- Required Python packages:
  - `streamlit`
  - `google-generativeai`
  - `python-dotenv`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yadavanubhav05/Streamlit_text_summarization.git
   cd Streamlit_text_summarization
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or if using the pyproject.toml:
   ```bash
   pip install .
   ```

3. Set up your Google AI API key:
   - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a `.env` file in the root directory:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run Streamlit/summarization_streamlit.py
   ```

2. Open your browser to the provided local URL (usually `http://localhost:8501`)

3. Enter text in the text area and click "Summarize" or just wait for automatic processing

4. View the summarized text below

## Project Structure

```
.
├── main.py                 # Basic Python script (placeholder)
├── pyproject.toml          # Project configuration
├── README.md              # This file
├── .gitignore             # Git ignore rules
└── Streamlit/
    ├── summarization_streamlit.py  # Main Streamlit app
    └── gemini_models.py            # Script to list available Gemini models
```

## Configuration

The app uses the following Gemini model settings for optimal summarization:
- Model: `models/gemini-pro-latest`
- Temperature: 0.01 (for consistency)
- Max output tokens: 50
- Top-p: 0.1

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source. Please check the license file if available.