import json
import mysql.connector


conn = mysql.connector.connect(user='ridwan', password='4hay',
                              host='10.1.72.5',database='billingsystem')
 
class create_dict(dict): 
    def __init__(self): 
        self = dict() 
           
    def add(self, key, value): 
        self[key] = value
 
mydict = create_dict()
cursor = conn.cursor()
cursor.execute("SELECT * FROM m_user")
result = cursor.fetchall()
 
for row in result:
    mydict.add(row[0],({"id":row[8],"fullname":row[1],"email":row[6]}))
 
data_json = json.dumps(mydict, indent=2, sort_keys=True)
print(data_json)
