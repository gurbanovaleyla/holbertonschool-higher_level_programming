from task_00_basic_serialization import (
    serialize_and_save_to_file,
    load_and_deserialize
)

data = {
    "name": "Leyla",
    "age": 26
}

serialize_and_save_to_file(data, "data.json")

loaded = load_and_deserialize("data.json")

print(loaded)
