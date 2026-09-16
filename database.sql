CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    student_number TEXT NOT NULL UNIQUE,
    programme TEXT NOT NULL
);

INSERT INTO students (name, student_number, programme)
VALUES
('Jafet Kuutondokwa', '225081601', 'Bachelor of Computing - Computer Science');
