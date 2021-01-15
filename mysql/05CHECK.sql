create table student2(
	id int primary key auto_increment,
    name varchar(20),
    age int
);
drop table student2;
desc student2;
select * from student2;
delete from student2;
insert into student2 values(null,'Tom4',20);
alter table student2 modify name varchar(20) unique;
alter table student2 modify age int not null;