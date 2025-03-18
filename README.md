# NiceGUI Sample with AI Chat

A sample application demonstrating NiceGUI capabilities with OpenAI Agent integration.

Repository: https://github.com/noricha-vr/nicegui-sample

## Features

- **Counter Page** - Simple interactive counter demonstration
- **AI Chat Assistant** - Chat interface powered by OpenAI with web search capabilities
- **Responsive UI** - Clean interface built with NiceGUI

## Prerequisites

- Python 3.9+
- Docker and Docker Compose (for containerized deployment)
- OpenAI API key

## Setup

### Local Development

1. Clone the repository:
   ```
   git clone https://github.com/noricha-vr/nicegui-sample.git
   cd nicegui-sample
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your-api-key-here
   ```

5. Run the application:
   ```
   python main.py
   ```

## Usage

1. Open your browser and navigate to http://localhost:8081
2. The application will open on the Counter page
3. Use the navigation links to switch between Counter and Chat pages
4. On the Chat page, you can interact with the AI assistant which has web search capabilities

## Project Structure

- `main.py` - Application entry point and configuration
- `countup.py` - Counter page implementation
- `chat.py` - AI chat assistant implementation
- `agents.py` - Agent SDK implementation (not shown in the code samples)

## Development Environment

- M1 Mac
- Docker Compose

## License

Copyright (c) 2025 noricha-vr

This project is licensed under the MIT License. See the LICENSE file for details.
