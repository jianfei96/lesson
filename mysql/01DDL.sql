# 显示所有数据库
show databases;
#创建数据库alter
create database db1;
#查询编码方式
show create database db1;

create database db2;
#删除数据库
drop database db2;
#使用数据库
use db1;
#查询当前使用数据库
select database();