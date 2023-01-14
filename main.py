import sqlite3


con = sqlite3.connect('data.db')
cur = con.cursor()

cur.execute("""CREATE TABLE if not exists persons(
            id INTEGER primary key autoincrement,
            name TEXT,
            birthdate TEXT
            )
            """)

cur.execute("""CREATE TABLE if not exists employees(
            id INTEGER primary key autoincrement,
            position TEXT,
            salary INTEGER
            )
            """)

cur.execute("""CREATE TABLE if not exists contacts(
            id INTEGER primary key autoincrement,
            type TEXT,
            value INTEGER
            )
            """)
con.commit()



# cur.execute("""
#     INSERT INTO persons(name, birthdate) VALUES
#         ('Johny', '5.01.2023'),
#         ('Nick', '10.01.2023'),
#         ('Mike', '11.01.2023')
# """)
# con.commit()
#
# cur.execute("""
#     INSERT INTO employees(position, salary) VALUES
#         ('QA', 1500 ),
#         ('Dev', 2000),
#         ('PM', 2200)
# """)
#
# cur.execute("""
#     INSERT INTO contacts(type, value) VALUES
#         ('mob', 444333222 ),
#         ('mob', 444333221),
#         ('phone', 444333220)
# """)

con.commit()




if __name__ == '__main__':
    res = cur.execute("SELECT * FROM persons",)
    print(res.fetchall())

    res1 = cur.execute("""SELECT persons.id, employees.id, contacts.id
                        FROM persons
                        INNER JOIN employees, contacts ON persons.id=employees.id and persons.id=contacts.id""")
    print(res1.fetchall())

    res2 = cur.execute("""SELECT contacts.type, contacts.value, employees.position
                        FROM contacts
                        FULL JOIN employees ON contacts.id=employees.id""")
    print(res2.fetchall())

    res3 = cur.execute("""SELECT employees.position, contacts.type, contacts.value
                        WHERE emplyees.id = 1
                        FROM contacts
                        FULL JOIN employees ON contacts.id=employees.id""")
                        
    print(res3.fetchall())




