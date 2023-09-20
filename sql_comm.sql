insert into profile 
values (2, 'Первый', 'О первом');

select * from profile

create TABLE profile(
	prof_id serial NOT NULL PRIMARY KEY,
	prof_name varchar(20) NOT NULL,
	prof_content text
)