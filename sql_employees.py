import sqlite3

conn = sqlite3.connect('employees.db')
cur = conn.cursor()

cur.execute(
    """
        CREATE TABLE IF NOT EXISTS employees (
            
            id PRIMARY KEY NOT NULL,
            name VARCHAR,
            job_id TEXT,
            department_id INTEGER,
            salary INTEGER,
            time_work INTEGER,
            manager_id INTEGER

        )

    """
)

conn.commit()

cur.execute(
    """
        CREATE TABLE IF NOT EXISTS emp_salary (

            id PRIMARY KEY NOT NULL,
            name_employees TEXT
            salary_employees INTEGER

        )

    """
)

conn.commit()

more_users = [
    ('Peter', 'It_prog', '4', '7000', '08:45', '56'), ('Olga', '002', '6', '3000', '08:07', '52'),
    ('David', '003', '4', '4000', '08:54', '55'), ('Yann', 'It_prog', '3', '2000', '08:34', '456'),
    ('Leonn', '005', '7', '5000', '08:34', '35'), ('David', '006', '6', '6000', '08:59', '503')]

emp = [
    ('David', '2000'), ('Olga', '3000'), ('Yan', '3500'),
    ('Georgi', '4000'), ('Vasia', '5500'), ('Piter', '3400'), ('Evgeni', '2600')]

cur.executemany("INSERT INTO employees VALUES(?, ?, ?, ?, ?, ?);", more_users)
conn.commit()

cur.executemany("INSERT OR REPLACE INTO emp_salary VALUES(?, ?);", emp)
conn.commit()

cur.execute("SELECT * FROM employees;")
one_result = cur.fetchone()
print(one_result)

cur.execute("SELECT * FROM employees;")
two_result = cur.fetchmany(1)
print(two_result)

cur.execute("SELECT * FROM employees;")
all_results = cur.fetchall()
print(all_results)

cur.execute("SELECT * FROM employees WHERE name = 'David';")
cur.execute("SELECT * FROM employees WHERE job_id = 'It_prog';")
print(cur.fetchall())

cur.execute("SELECT name FROM employees WHERE department_id = '4' AND salary > '3000' ;")
print(cur.fetchall())

cur.execute("SELECT name FROM employees;")
elem = cur.fetchall()
print(elem)

cur.execute(
    "SElECT manager_id, department_id, name, MAX (salary),MAX (time_work) FROM employees ORDER BY manager_id DESC;")
elem_1 = cur.fetchall()
print(elem_1)

cur.execute(
    "SElECT manager_id, department_id, name, MIN (salary), MIN (time_work),MAX (salary), MAX (time_work) FROM employees ORDER BY manager_id DESC;")
elem_2 = cur.fetchall()
print(elem_2)

a = cur.execute("SELECT * FROM emp_salary;")
a = cur.fetchall()
print(a)


g = cur.execute(
    "SELECT manager_id FROM employees INER JOIN emp_salary ON employees.manager_id = emp_salary.salary_employees WHERE manager_id >5 AND SUM (emp_salary.salary_employees) > 50000 ; ")
g = cur.fetchall()
print(g)

q = cur.execute("SELECT name FROM employees WHERE LIKE '%a';")
q = cur.fetchall()
print(q)

o = cur.execute("SELECT name FROM employees WHERE LIKE '%n%n%';")
o = cur.fetchall()
print(o)
