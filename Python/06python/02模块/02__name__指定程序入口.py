import pymysql


if __name__ == '__main__':
    try:
        # 1.链接MySQL数据库
        db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='db1',charset='utf8')
        # print(db)

        # 2.获取游标对象
        cursor = db.cursor()

        # 3.使用游标对象执行sql语句
        cursor.execute("select version()")

        # 4.获取查询到的数据
        data = cursor.fetchone()

        # 5.输出数据
        print('version is : %s' %data)

    except Exception as e:
        print(e)
    finally:
         # 6.关闭数据连接对象
        db.close()