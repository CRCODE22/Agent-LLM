# Agent-LLM

Agent-LLM is a versatile Python application that leverages AI language models for task management and problem-solving. Boasting both short-term and long-term memory capabilities, it recalls previous interactions and context. The application can browse the web, write its own commands, and more. Supporting various AI providers like [OpenAI](https://openai.com/), [Google Bard](https://bard.google.com), [Oobabooga Text Generation Web UI](https://github.com/oobabooga/text-generation-webui), and [llama.cpp](https://github.com/ggerganov/llama.cpp), Agent-LLM is both flexible and adaptable to diverse use cases.

⚠️ **This project is under active development and may still have issues.** We appreciate your understanding and patience. If you encounter any problems, please first check the open issues. If your issue is not listed, kindly create a new issue detailing the error or problem you experienced. Thank you for your support!

## Key Features

- Efficient management of long-term and short-term memory
- Easily pluggable commands for extended functionality
- Compatibility with multiple AI providers
- Web browsing capabilities
- Command execution and code evaluation
- Customizable plugin system with prompts for various AI models
- Docker support for seamless deployment
- Integration with Huggingface for audio-to-text conversion
- Support for interacting with Twitter, GitHub, Google, DALL-E, and more growing fast.
- Voice options for text-to-speech, including Brian TTS, Mac OS TTS, and ElevenLabs

## Web Application Features

The frontend web application of Agent-LLM provides an intuitive and interactive user interface for users to:

- Manage agents: View the list of available agents, add new agents, delete agents, and switch between agents.
- Set objectives: Input objectives for the selected agent to accomplish.
- Start tasks: Initiate the task manager to execute tasks based on the set objective.
- Instruct agents: Interact with agents by sending instructions and receiving responses in a chat-like interface.
- Available commands: View the list of available commands and click on a command to insert it into the objective or instruction input boxes.
- Dark mode: Toggle between light and dark themes for the frontend.

The frontend is built using React and Material-UI and communicates with the backend through API endpoints.

## Installation and Setup

1. Clone the repository.
```
git clone https://github.com/Josh-XT/Agent-LLM
```
2. Install the required Python packages:
```
pip install -r requirements.txt
```
3. Configure the necessary environment variables in the `.env` file using `.env.example` as a template.
4. Launch Agent-LLM using Docker Compose (recommended) or by running the `main.py` script.

### Docker Setup (Recommended)

To launch the project using Docker Compose:

1. Install Docker and Docker Compose on your system.
2. Access the project's root folder.
3. Execute the following command to build and activate the containers for both the Flask backend server and the frontend React application:
```
docker-compose up
```

Access the web interface at http://localhost

### Local Setup (Alternative)

To run Agent-LLM without Docker:


1. Set up and run the frontend:
   1. Head to the `frontend` folder.
   2. Execute the following command to install the necessary dependencies:
   ```
   npm install
   ```
   3. In a separate terminal, navigate to the project's root folder and run the following command to activate the Flask backend server:
   ```
   python app.py
   ```
   4. Return to the `frontend` folder and run the following command to initiate the frontend React application:
   ```
   npm start
   ```

## Configuration

Agent-LLM utilizes a `.env` configuration file to store AI language model settings, API keys, and other options. Use the supplied `.env.example` as a template to create your personalized `.env` file. Configuration settings include:

- **INSTANCE CONFIG**: Set the agent name, objective, and initial task.
- **AI_PROVIDER**: Choose between OpenAI, llama.cpp, or Oobabooga for your AI provider.
- **AI_PROVIDER_URI**: Set the URI for custom AI providers such as Oobabooga Text Generation Web UI (default is http://127.0.0.1:7860).
- **LLAMACPP_PATH**: Set the path to the llama binary if llamacpp is not in the llama folder of the project.
- **COMMANDS_ENABLED**: Enable or disable command extensions.
- **MEMORY SETTINGS**: Configure short-term and long-term memory settings.
- **AI_MODEL**: Specify the AI model to be used (e.g., gpt-3.5-turbo, gpt-4, text-davinci-003, vicuna, etc.).
- **AI_TEMPERATURE**: Set the AI temperature (leave default if unsure).
- **MAX_TOKENS**: Set the maximum number of tokens for AI responses (default is 2000).
- **WORKING_DIRECTORY**: Set the agent's working directory.
- **EXTENSIONS_SETTINGS**: Configure settings for OpenAI, Huggingface, Selenium, Twitter, and GitHub.
- **VOICE_OPTIONS**: Choose between Brian TTS, Mac OS TTS, or ElevenLabs for text-to-speech.

For a detailed explanation of each setting, refer to the `.env.example` file provided in the repository.

## API Endpoints

Agent-LLM provides several API endpoints for managing agents, setting objectives, managing tasks, and more. The following are the available API endpoints:

1. **Add Agent**: `/api/add_agent` (POST)

   Adds a new agent with the given agent name.

2. **Delete Agent**: `/api/delete_agent` (DELETE)

   Deletes an existing agent with the given agent name.

3. **Get Agents**: `/api/get_agents` (GET)

   Retrieves a list of all available agents.

4. **Get Chat History**: `/api/get_chat_history` (GET)

   Retrieves the chat history of an agent with the given agent name.

5. **Instruct**: `/api/instruct` (POST)

   Sends an instruction prompt to the agent and receives a response.

6. **Set Objective**: `/api/set_objective` (POST)

   Updates the agent's current objective.

7. **Add Initial Task**: `/api/add_initial_task` (POST)

   Adds an initial task for the agent to execute.

8. **Execute Next Task**: `/api/execute_next_task` (GET)

   Executes the next task in the agent's task list and returns the result.

9. **Create Task**: `/api/create_task` (POST)

   Creates a new task based on the given objective, result, task description, and task list.

10. **Prioritize Tasks**: `/api/prioritize_tasks` (POST)

    Prioritizes tasks in the agent's task list based on the given task ID.

11. **Execute Task**: `/api/execute_task` (POST)

    Executes a specific task based on the given objective and task.

To learn more about the API endpoints and their usage, visit the API documentation at http://localhost:5000/api/docs when running the application locally, or http://localhost/api/docs if running with Docker.

## Extending Functionality

### Commands

To introduce new commands, generate a new Python file in the `commands` folder and define a class inheriting from the `Commands` class. Implement the desired functionality as methods within the class and incorporate them into the `commands` dictionary.

### AI Providers

To switch AI providers, adjust the `AI_PROVIDER` setting in the `.env` file. The application is compatible with OpenAI, Oobabooga Text Generation Web UI, and llama.cpp. To support additional providers, create a new Python file in the `provider` folder and implement the required functionality.

### Building Prompts for Plugin System

Agent-LLM employs a plugin system with customizable prompts for instructing various AI models. These prompts are stored in the `model-prompts` folder and are categorized by model name. Each model has five prompt types:

1. model-prompts/{model}/execute.txt
2. model-prompts/{model}/priority.txt
3. model-prompts/{model}/system.txt
4. model-prompts/{model}/task.txt
5. model-prompts/{model}/script.txt

For a comprehensive explanation of prompt formats and usage, refer to the [PROMPTS.md](PROMPTS.md) file.

## Project Structure

The project is organized into several folders:

- `commands`: Stores pluggable command modules for enhancing Agent-LLM's functionality.
- `frontend`: Contains frontend code for Agent-LLM's web interface.
- `model-prompts`: Houses prompt templates for the various AI models used by Agent-LLM.
- `provider`: Holds the implementations for the supported AI providers.

## Acknowledgments

This project was inspired by and utilizes code from the following repositories:

- [babyagi](https://github.com/yoheinakajima/babyagi)
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)

Please consider exploring and contributing to these projects as well.

## Contributing

We welcome contributions to Agent-LLM! If you're interested in contributing, please check out the open issues, submit pull requests, or suggest new features. To stay updated on the project's progress, follow [@Josh_XT](https://twitter.com/Josh_XT) on Twitter.

## Usage

Run Agent-LLM using Docker Compose (recommended) or by running the `main.py` script. The application will load the initial task and objective from the configuration file and begin task execution. As tasks are completed, Agent-LLM will generate new tasks, prioritize them, and continue working through the task list.
