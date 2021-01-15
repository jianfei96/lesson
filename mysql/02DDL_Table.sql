#create table 表名(列名 数据类型,列名 数据类型);
create table student(
	id int,
    name varchar(20),
    age int,
    score double(5,2),
    birthday date,
    insert_time timestamp
);

show tables;
select * from student;

#复制表
create table student2 like student;
#查询当前数据库所有表
show tables;
#查询表的结构，列名，约束
describe student2;
#重命名表名
alter table student2 rename student3;

#添加一列
alter table student3 add color varchar(5);
desc student3;
#重命名 name -> username
alter table student3 change name username varchar(20);
#删除列
alter table student3 drop color;
drop table student3;