# Deepseek Chat UI

Deepseek R1 is an open source model that is on par with most commercial models in benchmarks. While it is available in their own app, you have to agree to their license agreement, you can run it on your system. If you prefer a web based interface, I have created this for you.

## Setup

### Install Ollama

We are using the Ollama backend for this. You can find the instruction to install on your platform on the ollama [site](https://ollama.com/download)

Add the DeepSeek R1 model you want to use to your environment variables.

```bash
export R1_VARIANT=deepseek-r1:7b #add the variant you want to work with on locally.
```

For Windows,

```powershell
env:R1_VARIANT=deepseek-r1:7b
```

If you do not set your variant, it will default to `deepseek-r1:1.5b`. That is the simplest variant with the lowest hardware requirements.

If you are low on memory, you can use the 1.5b variant. Press `ctrl+d` or `control+d` to get out of the cli interface.

**NOTE**: If you haven't downloaded the model locally, the app will download it for you. However, the file sizes can be quite large, so you may have to wait.


You need to run ollama as a server.

```bash
ollama serve
```

**NOTE**: You might get `Error: listen tcp 127.0.0.1:11434: bind: address already in use`. Usually this means that ollama server is already running. Otherwise check the processes on your system.

### Python Setup
Right now I don't have a release method, so you will have to clone the project locally to your device. Navigate to the folder you want to install and run these commands.

```bash
git clone https://github.com/muddi900/deepseek-local-chat
cd deepseek-local-chat
```

Create a virtualenv, I am using version 3.12, but it should be usable for 3.10+:

```bash
python3.12 -m venv venv
```

I am using Chainlit to build the UI and ollama as a backend

```bash
pip install -r requirements.txt
```

## Run

Running it is quite simple. If you are in the `deepseek-local-chat` folder:

```bash
chainlit run main.py   
```

