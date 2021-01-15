#insert int 表名(列名,列名) values(数据,数据)
insert into student(id,name,age) values(3,'Tom',10);

select * from student;
insert into student values(1,'Tom',10,100.00,'2021-1-14','2021-1-14 12:12:12');
desc student;
#取消安全模式
set sql_safe_updates = 0;

#update 表名 set 列名 = 数据 where 条件;
#不带条件会更新所有行
update student set age = 18 where id = 1;
#删除 delete from 表名 where 条件;
delete from student where id=1;

#不带条件删除所有数据
delete from student;