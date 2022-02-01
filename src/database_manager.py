from pysqlitecipher import sqlitewrapper
import hashlib

# make the object
obj = sqlitewrapper.SqliteCipher(dataBasePath="../data/database.db" , checkSameThread=False , password="B3774405ED2198EDA392267CC1C17C6A6017ABA5870C6777EC86CF17CABE05FB")

def get_name(srn, person):
    db_out = obj.getDataFromTable(person + "List" , raiseConversionError = True , omitID = False)[1]
    for x in  db_out:
        if x[2] == srn:
            return x[1]
    return ""

def get_pass(srn):
    db_out = obj.getDataFromTable("TeacherList" , raiseConversionError = True , omitID = False)[1]
    for x in  db_out:
        if x[2] == srn:
            print(x)
            return x[3]  

def get_class(srn):
    db_out = obj.getDataFromTable("TeacherList" , raiseConversionError = True , omitID = False)[1]
    for x in  db_out:
        if x[2] == srn:
            print(x)
            return x[4] 