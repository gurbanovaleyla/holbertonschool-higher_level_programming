#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(csv_filename):
    try:
        data_list = []

        with open(csv_filename, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                data_list.append(row)

        with open("data.json", "w") as jsonfile:
            json.dump(data_list, jsonfile)

        return True

    except FileNotFoundError:
        return False

    except Exception:
        return False
