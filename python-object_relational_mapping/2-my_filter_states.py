#!/usr/bin/python3
"""Lists states filtered by user input."""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    cursor = connection.cursor()
    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id"
            .format(argv[4]))

    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()
    connection.close()
