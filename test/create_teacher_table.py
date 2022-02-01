from pysqlitecipher import sqlitewrapper
import hashlib

tableName = "TeacherList"

print(hashlib.md5(b'test').hexdigest())

# make the object
obj = sqlitewrapper.SqliteCipher(dataBasePath="../data/database.db" , checkSameThread=False , password="B3774405ED2198EDA392267CC1C17C6A6017ABA5870C6777EC86CF17CABE05FB")

colList = [["user", "TEXT"] , ["id" , "TEXT", "PRIMARY KEY"] ,["pass", "TEXT"], ["class", "TEXT"]]
obj.createTable(tableName , colList , makeSecure=True , commit=True)

print(obj.getDataFromTable(tableName , raiseConversionError = True , omitID = False))

insertList = ["Shilaputri", "UG1G001", hashlib.md5(b"shi").hexdigest(), "PHYSICS"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["BrhamaCharini", "UG1G002", hashlib.md5(b"brh").hexdigest(), "ELECTRICAL"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Chandrghanta", "UG1G003", hashlib.md5(b"cha").hexdigest(), "COMPUTERS"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Kooshmanda", "UG1G004", hashlib.md5(b"koo").hexdigest(), "MECHANICAL"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Skanda", "UG1G005", hashlib.md5(b"ska").hexdigest(), "MATHEMATICS"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Katayanin", "UG1G006", hashlib.md5(b"kat").hexdigest(), "PHYSICS LAB"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Kaalaratri", "UG1G007", hashlib.md5(b"kaa").hexdigest(), "CHEMISTRY"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["MahaGowri", "UG1G008", hashlib.md5(b"mah").hexdigest(), "PHYSICS LAAB"]
obj.insertIntoTable(tableName, insertList , commit = True)
insertList = ["Siddidhatri", "UG1G009", hashlib.md5(b"sid").hexdigest(), "COMPUTERS LAB"]
obj.insertIntoTable(tableName, insertList , commit = True)
