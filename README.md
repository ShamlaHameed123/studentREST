# studentREST

Prerequisites
--------------
1. Python3.6.1
2. Pip3

Create database students in postgresql
--------------------------------------
1. sudo -u postgres psql
2. create database students; 
3. CREATE USER students WITH PASSWORD 'students'; 
4. ALTER ROLE students SET client_encoding TO 'utf8'; 
5. ALTER ROLE students SET default_transaction_isolation TO 'read committed'; 
6. ALTER ROLE students SET timezone TO 'UTC';
7. GRANT ALL PRIVILEGES ON DATABASE students TO students; 
8. Restore the dump with the command psql students<student.sql
9. \q

Flow
-----
1. git clone git@github.com:ShamlaHameed123/studentREST.git
2. Run pip3 install -r requirements.txt
3. cd students
4. python3 manage.py makemigrations
5. python3 manage.py migrate
6. In SQL management studio, execute stored procedure script data.sql to populate the table with 100 records
7. Run python3 manage.py runserver // Runs the backend server at port 8000 by default
8. Database used is PostgreSQL, db name:students

REST API Endpoints
-------------------
1. List students: http://127.0.0.1:8000/student/api/list
2. Add student: http:127.0.0.1:8000/student/api/create 
3. Update student: http:127.0.0.1:8000/student/api/student-id
4. Delete student: http:127.0.0.1:8000/student/api/student-id/delete
