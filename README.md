# llm-cli

**llm-cli** is a local, terminal-based interface to interact with the Mistral large language model via [Ollama](https://ollama.com).  
It provides a fast and minimal CLI experience similar to ChatGPT, but fully offline.

---

## Features

- Local-only usage (no API key or internet required)
- Interactive chat interface in your terminal
- Built on top of Mistral and Ollama
- Simple command: just type `llm` to start chatting
- Clean and minimal structure (modular, editable, Pythonic)

---

## Installation

### Requirements

- Python 3.8+
- [Ollama](https://ollama.com) installed with the Mistral model:
  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ollama run mistral
  ```

### Setup

```bash
git clone git@github.com:rattus-digitalis/llm-cli.git
cd llm-cli
./install
```

Then run:

```bash
source .venv/bin/activate
llm
```

---

## Usage

Once inside the interactive shell:

```bash
>>> quelle est la commande bash pour voir les ports ouverts ?
```

To exit:

```bash
>>> exit
```

---

## Project Structure

```
llm-cli/
├── llm/
│   ├── __init__.py
│   ├── api.py        # Handles interaction with Ollama/Mistral
│   └── cli.py        # Main CLI loop
├── setup.py          # Installation configuration
├── install           # Installer script (venv + symlink)
└── README.md
```

---

## License

MIT License
