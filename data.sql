CREATE TABLE courses (
course_id INT(2) NOT NULL PRIMARY KEY AUTO_INCREMENT,
name VARCHAR(50),
pet_type VARCHAR(15),
level VARCHAR(10),
start_date DATE,
start_time time,
duration INT(2),
length INT(1),
trainer VARCHAR(60),
description TINYTEXT
)ENGINE=INNODB;

CREATE TABLE attendee(
attendee_id INT(4) NOT NULL AUTO_INCREMENT PRIMARY KEY,
course_id INT(2),
f_name VARCHAR(15),
l_name VARCHAR(15),
phone_num VARCHAR(15),
email VARCHAR(50),
dob DATE,
FOREIGN KEY(course_id) REFERENCES courses(course_id)
)ENGINE=innodb;

INSERT INTO attendee(attendee_id,course_id,f_name, l_name, phone_num, email, dob)
VALUES
(1,2, "Bob", "Jones", "(317)-217-4591","bob@gmail.com", "1996-12-15"),
(2,2, "Jeff", "Pud", "(345)-594-7761", "pud@gmail.com", "1980-07-01"),
(3,3, "Todd", "Greene", "(317)-841-1855", "todd@gmail.com", "2001-01-01"),
(4,1, "Terry", "Egnater", "(317)-123-3469", "terry@gmail.com", "1988-01-01");


INSERT INTO courses (course_id,name,pet_type,level, start_date, start_time, duration, length, trainer, description) VALUES
(1,"Morning Obedience","Cat","Beginner","2022-11-03","10:23",90,1,"Emily", "Obedience training"),
(2,"Glamour Photography for your Kitty","Cat","Beginner","2022-11-03","09:38",45,2,"Sarah","photos for your cat"),
(3,"Ferret Bueller's Day Off","Cat","Beginner","2022-11-03","00:26",45,1,"Terry","training for ferrets"),
(4,"Mr. Fluffies playday","Ferret","Beginner","2022-10-31","23:36",45,3,"Steven","older dog sessions"),
(5,"Tail Chasers","Cat","Beginner","2022-10-19","12:36",45,1,"Ron","Ron doing Ron activities"),
(6,"tom","Ferret","Beginner","2022-11-01","12:33",45,2,"meg","test"),
(7,"Paulies cracker","Parrot","Beginner","2022-11-03","05:38",45,2,"test1","test1"),
(8,"citty kitty","Cat","Beginner","2022-11-02","13:00",45,3,"meg","hellos"),
(9,"Ferret festival","Ferret","Beginner","3000-01-01","12:17",45,2,"Mary","a whole lot of stuff going on")
;