# Pathlib -> arra való, hogy a fájl- és mappaútvonalakat ne nyers stringként kezeljük
from pathlib import Path

CURRENT_FILE = Path(__file__).resolve()
CURRENT_DIR = CURRENT_FILE.parent

# jelenleg futó fájl (basics.py) ->  resolve(): absolút pathé alakítás -> .parent/parents[2]: felfelé lépkedés a pathen
PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
INPUT_DIR = DATA_DIR / "input"
OUTPUT_DIR = DATA_DIR / "output"

# Adott file elérés
PRACTICE_FILE = Path(__file__).resolve().parent / "practice.py"

# létezik egyáltalán ilyen fájl?
print(PRACTICE_FILE.exists())

# file-e
print(PRACTICE_FILE.is_file())

# mappa-e
print(PRACTICE_FILE.is_dir())


# mappa létrehozás, ha még nincs
# parents = True -> és a pathban levő parent mappákat is
# exist_ok = True -> ha létezik, hagyja
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


print(PRACTICE_FILE)