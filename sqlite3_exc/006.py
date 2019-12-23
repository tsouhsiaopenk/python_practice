import sqlite3


def menu():
    while True:
        print("1,添加数据")
        print("2,查询数据")
        print("3,删除数据库列表")
        print("0,退出系统")
        x = int(input("请输入选择："))
        if x == 1:
            insert()
        elif x == 2:
            select()
        elif x == 3:
            delete()
        elif x == 0:
            break
        else:
            print("非法输入")


def create():
    conn = sqlite3.connect("myData.db")
    cursor = conn.cursor()
    sql ='''Create table student(id  int,
                                  name text,
                                  gender text)'''
    cursor.execute(sql)
    cursor.close()
    conn.close()


def insert():
    print("请输入myDate数据库的窗体数据")
    conn = sqlite3.connect("myData.db")
    cursor = conn.cursor()
    while True:
        new_id = int(input("请输入id："))
        new_name = input("请输入name：")
        new_gender = input("请输入gender:")
        x = (new_id, new_name, new_gender)
        sql = '''insert into student VALUES (?,?,?)'''
        cursor.execute(sql, x)
        conn.commit()
        again = input("继续（y/n）?")
        if again[0].lower() == 'n':
            break

    # cursor.execute(sql)
    cursor.close()
    conn.close()


def select():
    conn = sqlite3.connect("myData.db")
    cursor = conn.cursor()
    results = cursor.execute("select * from student")
    """                                                                                                                                                  
    for record in results:
        print("id = ", record[0])
        print("name = ", record[1])
        print("gender = ", record[2])
    """
    allstudents = results.fetchall()
    for student in allstudents:
        print(student)
    cursor.close()
    conn.close()


def delete():
    conn = sqlite3.connect("myData.db")
    #new_id= int(input("请输入要删除学生的编号:"))
    cursor = conn.cursor()
    sql = '''DELETE
            from student
            where id = 1'''
    results = cursor.execute(sql)
    conn.commit()       # 更新数据库

    results = cursor.execute("select name from student")
    allstudents = results.fetchall()
    for student in allstudents:
        print(student)
    cursor.close()
    conn.close()


def main():
    menu()

if __name__ == '__main__':
    main()