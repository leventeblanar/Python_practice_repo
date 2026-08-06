import tempfile
from pathlib import Path
import json
import shutil


def example_1():
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        test_file = temp_path / "test.json"
        test_file.write_text('{"status": "ok"}', encoding="utf-8")

        print(test_file.read_text(encoding="utf-8"))

def example_2():
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", delete=True) as file:
        file.write("Hello temp file")
        print(file.name)

def example_3():

    output_file = Path("output/flattened_orders.json")

    data = [
        {"order_id": "ORD-1", "total": 1000}
    ]

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        temp_output = temp_path / "flattened_orders.json"

        with temp_output.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        shutil.move(temp_output, output_file)