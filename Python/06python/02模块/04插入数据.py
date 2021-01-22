import pymysql

if __name__ == '__main__':
    try:
        db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='db1',charset='utf8')
        cursor = db.cursor()
        sql = '''
            insert into person values (1,'tom',20,'M',200000)
        '''
        count = cursor.execute(sql)
        db.commit()
        print('count: %d' %count)
    except Exception as e:
        print(e)
    finally:
        db.close()