# Agentic AI Bootcamp

Course overview and materials for the Agentic AI Bootcamp.

## Structure

- `week-01/` — Intro, prompting, agents
  - `main.py` — starter script
  - `requirements.txt` — dependencies
  - `.env.example` — template for required environment variables
  - `basic/` — tokenization example

## Setup

### 1. Install `uv`

`uv` is a fast Python package/venv manager.

```bash
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Verify it installed:

```bash
uv --version
```

### 2. Create and activate a virtual environment

```bash
cd week-01
uv venv
```

Activate it:

```bash
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# macOS / Linux
source .venv/bin/activate
```

### 3. Install dependencies

```bash
uv pip install -r requirements.txt
```

### 4. Configure environment variables

Copy the example file and fill in your own key:

```bash
# Windows
copy .env.example .env

# macOS / Linux
cp .env.example .env
```

Then edit `.env` and set:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Run the project

```bash
python main.py
```
