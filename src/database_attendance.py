from telnetlib import STATUS
from pysqlitecipher import sqlitewrapper
import hashlib
from datetime import date
import datetime
import time

# make the object
obj = sqlitewrapper.SqliteCipher(dataBasePath="../data/attendance.db" , checkSameThread=False , password="B3774405ED2198EDA392267CC1C17C6A6017ABA5870C6777EC86CF17CABE05FB")

def create_record(srn, cls, status, query = ""):
    # Create a list of the record that is to be appended to the database
    try:
        obj.insertIntoTable(str(date.today()), [class_no(), srn, cls, status, query], commit = True)
        print(obj.getDataFromTable(str(date.today()) , raiseConversionError = True , omitID = False))
    except Exception as e:
        print("15:", e)
        if str(e).find("no such table in data base"):
            colList = [["Class NO", "TEXT"], ["SRN", "TEXT"], ["CLASS", "TEXT"], ["STATUS", "TEXT"], ["QUERY", "TEXT"]]
            obj.createTable(str(date.today()), colList , makeSecure=True , commit=True)
            obj.insertIntoTable(str(date.today()), [class_no(), srn, cls, status, query], commit = True)
        else:
            raise e

# TODO: Write a replace function that takes in arguments, SRN, Status and Query 
# def replace_record(d_time, srn, cls, status, query = ""):

def class_no( ):
    t = int(time.strftime("%H")) * 3600 + int(time.strftime("%M")) * 60
    if(time_sec(8, 10) < t & t > time_sec(8, 45)):
        return 1
    elif (t > time_sec(9, 10) & time_sec(9, 45) < t):
        return 2 
    elif (t > time_sec(10, 35) & time_sec(11, 5) < t):
        return 3
    elif (t > time_sec(11, 35) & time_sec(12, 15) < t):
        return 4
    elif (t > time_sec(13, 20) & time_sec(14, 0)< t):
        return 5
    return t

def time_sec(h, m):
    return h * 60 * 60 + m * 60



