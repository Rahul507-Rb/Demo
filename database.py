import mysql.connector
Info = mysql.connector.connect(
    host ="localhost",
    user = "root",
    passwd ="",
    db ="rahul"
)
cursor = Info.cursor()



def loginAdmin(data):
    try:
        cursor.execute('SELECT * FROM `student` WHERE `admin` = %s AND `password` = %s',data)
      
        return cursor.fetchone()
    except Exception as e:
        print(e)
        return False
    
    
def registerUser(data):
    try:
        cursor.execute('INSERT INTO `demo` (`name`, `username`, `password`) VALUES (%s, %s, %s)', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    

def getUsers():
    try:
        cursor.execute('SELECT * FROM `demo`')
        return cursor.fetchall()
    except Exception as e:
        print(e)
        return []
    

def delUser(id):
    try:
        cursor.execute('DELETE FROM `demo` WHERE `id` = %s', id)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False
    
def updateUser(data):
    try:
        cursor.execute('UPDATE `demo` SET `name` = %s, `username` = %s,`password`=%s WHERE `id` = %s', data)
        Info.commit()
        return True
    except Exception as e:
        print(e)
        return False

    

