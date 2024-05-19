# 💬 Local LLMBot

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
  - [Windows](#windows)
  - [macOS](#macos)
  - [Linux](#linux)
- [Usage](#usage)
  - [Running the Streamlit App](#running-the-streamlit-app)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Local LLMBot is a chat application built with Streamlit and the Ollama API to simulate a chat with a local language model. The app provides an intuitive interface for managing multiple chat sessions and interacting with the model.

## Features
- Create and manage multiple chat sessions
- Generate responses using the Ollama model
- Intuitive user interface for displaying chat history
- Sidebar for chat session management

## Installation

### Prerequisites
- Python 3.7 or higher
- `pip` package manager

### Install Ollama

Before installing the required Python dependencies, ensure you have Ollama installed and properly configured.

1. **Install Ollama**

    Follow the official instructions from the [Ollama Offical Website](https://ollama.com/) to install the `ollama3` package.

2. **Configure Ollama**
  
    ```bash
    ollama run llama3
    ```

### Install LLAMA3 ChatBot

1. **Clone the Repository**
    ```bash
    git clone https://github.com/Kevoyuan/LLAMA3.git
    cd LocalLLMBot
    ```

2. **Create and Activate Virtual Environment**
    ```bash
    python -m venv llama3
    .\llama3\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Streamlit App

1. **Activate the Virtual Environment**

    Windows:
    ```bash
    .\llama3\Scripts\activate
    ```

    macOS/Linux:
    ```bash
    source llama3/bin/activate
    ```

2. **Run the Streamlit App**
    ```bash
    streamlit run app.py
    ```

3. **Access the App**
    Open your web browser and navigate to `http://localhost:8501`.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.
<!-- 
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details. -->
