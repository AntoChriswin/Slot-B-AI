% Facts
teaches(teacher1, subject1, course_code101).
teaches(teacher2, subject2, course_code102).
teaches(teacher3, subject1, course_code103).

enrolled(student1, course_code101).
enrolled(student2, course_code101).
enrolled(student1, course_code102).
enrolled(student3, course_code103).

% Rules
student_in_subject(Student, Subject) :-
    enrolled(Student, CourseCode),
    teaches(_, Subject, CourseCode).

students_in_subject(Subject, Students) :-
    setof(Student, student_in_subject(Student, Subject), Students).

teacher_for_subject(Teacher, Subject) :-
    teaches(Teacher, Subject, _).

% Queries
% Find all students enrolled in a specific subject
% students_in_subject(subject1, Students).

% Find the teacher for a specific subject
% teacher_for_subject(Teacher, subject1)
