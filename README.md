# AI Poem Generator

# Introduction 
This project is a AI Poem Generator built on Flask and React. It allows you to generate a poem based on the prompt from user.

## Overview
The CRUX API Analyzer is designed to help users get an insight into their websites' stats. It provides a User Interface which is built on React where a user can provide URLS, filter them and sort them. It uses Google Chrome CRUX API for fetching the data.



## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python
- Flask

### Installation

1. Clone this repository(backend):

```bash
git clone https://github.com/ManiYaswanth/AI-Poem-Backend
```

2. Install dependencies:
Use Virtual Environment and install dependencies

```bash
pip3 install -r requirements.txt
```
Configure the .env file with OpenAI API key
OPENAI_API_KEY = your-api-key

3. Navigate to the project directory:

```bash
cd app/
```

4. Run the application:

```bash
python3 main.py
```
The application will be accessible at http://localhost:5000

5. Clone the frontend repository
```bash
git clone https://github.com/ManiYaswanth/AI-Poem-Frontend
```

6. In the project directory of frontend application install dependencies
```bash
npm install
```
7. Start the development server
```bash
npm start
```
The application will be accessible at http://localhost:3000

## Usage
On the User Interface type a input (Your idea for a poem) and submit. The poem is generated by AI
and filled up on the UI, along with pie chart for emotion analysis.

## Note
Download the VADER lexicon if you haven't already
```python
nltk.download('vader_lexicon') 
```

## Contribute
Contributions are welcome! Feel free to open issues and pull requests.