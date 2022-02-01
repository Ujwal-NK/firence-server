from pysqlitecipher import sqlitewrapper
import hashlib

tableName = "StudentList"

print(hashlib.md5(b'test').hexdigest())

# make the object
obj = sqlitewrapper.SqliteCipher(dataBasePath="../data/database.db" , checkSameThread=False , password="B3774405ED2198EDA392267CC1C17C6A6017ABA5870C6777EC86CF17CABE05FB")

colList = [["user", "TEXT"] , ["id" , "TEXT", "PRIMARY KEY"] ,["CLASS", "TEXT"],]
obj.createTable(tableName , colList , makeSecure=True , commit=True)

print(obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False))

insertList = ["Keshava", "PES1G001", "A1"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Narayana", "PES1G002", "A2"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Madhava", "PES1G003", "B1"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Govinda", "PES1G004", "B2"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Vishnu", "PES1G005", "C4"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Madhusudana", "PES1G006", "D3"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Trivikrama", "PES1G007", "E4"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Vaamana", "PES1G008", "F4"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Shreedara", "PES1G009", "E8"]
obj.insertIntoTable(tableName, insertList , commit = True)
