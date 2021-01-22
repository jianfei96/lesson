import pymysql

if __name__ == '__main__':
    try:
        db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='db1',charset='utf8')
        cursor = db.cursor()
        sql = '''
            update person set age = age + 1 where sex = '%c'
        '''%('M')
        count = cursor.execute(sql)
        db.commit()
        print('count: %d' %count)
    except Exception as e:
        print(e)
    finally:
        db.close()