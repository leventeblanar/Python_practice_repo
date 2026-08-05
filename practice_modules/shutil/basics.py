# Shutil - fájlokat/mappákat tudunk kezelni

from pathlib import Path
import shutil

source = Path("order.json")
destination = Path("backup/order.json")

destination.parent.mkdir(parents=True, exist_ok=True)

# shutil.copy(source, destination) # fájl másolás
# shutil.copy2(source, destination) # fájl másolás metaadatokkal
# shutil.move("order.json", "backup/order.json") # áthelyezés

# Mappa törlése
temp_dir = Path("temp")

if temp_dir.exists():
    shutil.rmtree(temp_dir)

# Mappa teljes másolása
shutil.copytree("data", "data_backup", dirs_exist_ok=True)

