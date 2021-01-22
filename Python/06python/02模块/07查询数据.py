import pymysql

if __name__ == '__main__':
    try:
        db = pymysql.connect(host='localhost',port=3306,user='root',password='root',database='db1',charset='utf8')
        cursor = db.cursor()
        sql = '''
            SELECT * FROM person;
        '''
        cursor.execute(sql)

        result = cursor.fetchall()
        # print(result)
        for row in result:
            id = row[0]
            name = row[1]
            age = row[2]
            sex = row[3]
            income = row[4]
            print('id:%d, name:%s, age:%d, sex:%c, income:%.2f' %(id,name,age,sex,income))
            print(f'id:{id}, name:{name},age:{age},sex:{sex},income:{income}')

    except Exception as e:
        print(e)
    finally:
        db.close()