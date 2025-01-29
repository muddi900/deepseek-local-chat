# Deepseek Chat UI

Deepseek R1 is an open source model that is on par with most commercial models in benchmarks. While it is available in their own app, you have to agree to their license agreement, you can run it on your system. If you prefer a web based interface, I have created this for you.

## Setup

### Install Ollama

We are using the Ollama backend for this. You can find the instruction to install on your platoform on the ollama site(TKaddlink)

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

