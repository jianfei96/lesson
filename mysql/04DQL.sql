CREATE TABLE student3 ( id INT, -- 编 号
NAME VARCHAR(20), -- 姓 名
age INT, -- 年 龄
sex VARCHAR(5), -- 性 别
address VARCHAR(100), -- 地 址
math INT, -- 数 学
english INT -- 英 语
);
INSERT INTO student3(id,NAME,age,sex,address,math,english) VALUES (1,'ma',55,'m','tokyo',66,78),(2,'maha',45,'w','ikebukulo',98,87),(3,'mahu',55,'m','mejiro',56,77),(4,'qiaoben',20,'w','tokyo',76,65),(5,'qiaoben',20,'m','nara',86,NULL),(6,'liu',57,'m','ikebukulo',99,99),(7,'mad',22,'w','akamabane',99,99),(8,'de',18,'m','tokyo',56,65);

select * from student3;
#查询指定列的数据
select name,age from student3;
#条件查询
select * from student3 where id = 1;
select age from student3 where name='ma';
select address from student3;
#去重
select distinct address from student3;
select math,math+10 from student3;
select math,math+10 as eng from student3;
select math+english,math+english as '总成绩' from student3;
select (math+english),(math+english) as '总成绩' from student3;
#范围之间查询
select math from student3 where math between 80 and 90;
#in（集合） 集合不连续的数据
select * from student3 where id in (1,3,5);
#模糊查询
select * from student3 where name like 'ma%';
select * from student3 where name like 'ma_';#只能有三位

#and or
select * from student3 where age > 35 and sex='m';
select * from student3 where age > 35 or sex='m';
#select * from student3 where age > 35 or sex='m' order by age;
#select * from student3 where age > 35 or sex='m' order by age desc;

#排序 
select * from student3 order by age desc;
select * from student3 order by age asc;
