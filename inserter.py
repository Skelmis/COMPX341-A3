import os
from pathlib import Path

base: Path = Path(".")
for file_path in base.rglob("*.ts"):
    if not os.path.isfile(os.path.join(".", file_path)):
        continue

    print(file_path)
    with open(os.path.join(".", file_path), "r+") as f:
        content = f.read()
        f.seek(0, 0)
        f.write("// Ethan McKee-Harris - ID 1536943\n"+content)