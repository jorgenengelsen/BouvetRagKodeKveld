# Notebook samling for RAG kodekveld


## Oppsett

###Git
- Clon repoet 
- lag din egen branch og sjekk ut branchen


### Python / Jupyter miljø
Requirements:
- Python 3.10 (eller nyere)

- Naviger til katalogen du har installert python (Winpython) f.eks C:\[...]\python\WPy64-39100
- start WinPython Command Prompt.exe
- Naviger til katalogen \BouvetRagKodekveld (skriv f.eks "cd C:[....]\GitHub\BouvetRagKodeKveld")


Lag et venv (optional):
``` bash
python -m venv .venv
```
I winpython cmd skriv python -m venv .venv

Aktiver venv:
```bash
source .venv/bin/activate
```
- I winpython cmd skriv ".venv\Scripts\activate"

Installer pakker:
```bash
pip install -r requirements.txt
```
- I winpyton command prompt skriv "pip install -r requirements.txt"

### Miljøvariabler

Kopier env template:
```bash
cp .env.template .env
```
- I winpyton command promt skriv "copy .env.template .env"


Fyll inn nødvendige secrets i `.env`.