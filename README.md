# Deepseek Chat UI

Deepseek R1 is an open source model that is on par with most commercial models in benchmarks. While it is available in their own app, you have to agree to their license agreement, you can run it on your system. If you prefer a web based interface, I have created this for you.

## Setup

### Install Ollama

We are using the Ollama backend for this. You can find the instruction to install on your platform on the ollama [site](https://ollama.com/download)

Install the deepseek model locally and run it for testing

```bash
ollama run deepseek-r1:7b
```
I am running it on a laptop with on 16 gigs of memory and a simple GPU, so I am running the 7b variant. If you have a high-end gpu with a large memory size, you can use higher-end variants. 

If you are low on memory, you can use the 1.5b variant. Press `ctrl+d` or `control+d` to get out of the cli interface.


You need to run ollama as a server.

```bash
ollama serve
```

**NOTE**: You might get `Error: listen tcp 127.0.0.1:11434: bind: address already in use`. Usually this means that ollama server is already running. Otherwise check the processes on your system.

### Python Setup

Create a virtualenv, I am using version 3.12, but it should be usable for 3.10+:

```bash
python3.12 -m venv venv
```

I am using Chainlit to build the UI and black for code formatting


```bash
pip install chainlit black
```

or 

```bash
pip install -r requirements.txt
```

## Run

Running it is quite simple:

```bash
chainlit run main.py   
```

![image](screenshot.png)

It will only answer the hardcoded questions from the thoughtful AI dataset. You can check it out in [main.py](main.py)

