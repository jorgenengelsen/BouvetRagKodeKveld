# Notebook samling for RAG kodekveld

Requirements:
- Python 3.10 (eller nyere)

## Oppsett på windows

- Naviger til katalogen du har installert python (Winpython) f.eks C:\[...]\python\WPy64-39100
- start WinPython Command Prompt.exe (winpython cmd)
- Naviger til katalogen \BouvetRagKodekveld (skriv f.eks "cd C:[....]\GitHub\BouvetRagKodeKveld")

- Lag et venv (optional):
I winpython cmd skriv python -m venv .venv

- I winpython cmd skriv ".venv\Scripts\activate" for å aktivere venv 
- I winpyton command prompt skriv "pip install -r requirements.txt" for å installere nødvendige pakker

- I winpyton command promt skriv "copy .env.template .env"


- Fyll inn nødvendige secrets i `.env`.
(åpne i f.eks. notepad og lim inn mottatte secrets)



## Oppsett på linux/mac

### Python / Jupyter miljø
Lag et venv (optional):
``` bash
python -m venv .venv
```

Aktiver venv:
```bash
source .venv/bin/activate
```

Installer pakker:
```bash
pip install -r requirements.txt
```


### Miljøvariabler

Kopier env template:
```bash
cp .env.template .env
```

Fyll inn nødvendige secrets i `.env`.