import pymysql
if __name__ == '__main__':
    try:
        db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='db1',charset='utf8')
        cursor = db.cursor()
        #如果person表存在则删除
        count1 = cursor.execute("drop table if exists person")
        sql = '''
            create table person (
                id int,
                name varchar(20),
                age int,
                sex char(1),
                income float
            )
        '''
        count2 = cursor.execute(sql)
        print('count1: %d, count2: %d' %(count1,count2))

    except Exception as identifier:
        print(identifier)
    finally:
        db.close()