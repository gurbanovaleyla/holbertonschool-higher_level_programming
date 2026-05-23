#!/usr/bin/python3
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
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id"

    cursor.execute(
            query, (argv[4],))

    records = cursor.fetchall()
    for record in records:
        print(record)

    cursor.close()
    connection.close()
