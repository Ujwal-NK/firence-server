import socket
import mail
import database_manager as dbms
import json
import database_attendance as dbas
import hashlib
import datetime

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

port = 8060

server.bind(("", port))
server.listen(1)

client, addr = server.accept()
print(client, addr)

auth = True
while auth:
    data = client.recv(1024).decode()
    if (data == hashlib.md5((str(datetime.datetime.today())[:14]).encode()).hexdigest()):
        auth = False
        client.send("AUTH: OK".encode())

while(True):
    data = client.recv(1024 * 2).decode()
    if data == "SHUTDOWN":
        break

    data = json.loads(data)
    print("Client Data:", data)
    return_msg = "ERROR: Bad Request"

    print("Data ID:", data['ID'])
    
    try:
        r_true = False
        if "RPES" in data['ID']:
            r_true = True
            data["ID"] = data["ID"].replace("RPES", "PES")
        if "PES" in data['ID']:
            try:
                # dbms.get_name(data['ID'] ,"Student")
                print("Found student record", data["STATUS"])
                if "+" in data['STATUS']:
                    print("Marking the Student as present:", data['ID'])
                    dbas.create_record(data['ID'], data["CLASS"], data['STATUS'])
                    return_msg = dbms.get_name(data['ID'] ,"Student")
                    if r_true:
                        return_msg = "OK"
                elif "-" in data['STATUS']:
                    print("Marking the student as absent:", data['ID'])
                    dbas.create_record(data['ID'], data["CLASS"], data['STATUS'])
                    return_msg = "OK"
                elif "r" in data['STATUS']:
                    print("Reporting the student:", data['STATUS'])
                    print("Reson: ", data['QUERY'])
                    print("Reported by:", dbms.get_name(data['TEACHER'], "Teacher"))
                    dbas.create_record(data['ID'], data["CLASS"], data['STATUS'], data['QUERY'])
                    mail.report(data['ID'],data['QUERY'], dbms.get_name(data['TEACHER'], "Teacher"))
                    return_msg = "OK"
            except Exception as e:
                print(e)
                return_msg = "NOTIFY"
        elif "UG" in data['ID']:
            try:
                data['STATUS']
                return_msg = "NOTIFY"
            except Exception:
                print("Teacher Login")
                if dbms.get_pass(data['ID']) == data['PASS']:
                    print("Login Success:", data['ID'])
                    return_msg = dbms.get_class(data['ID'])
                else:
                    print("Login Failed")
                    return_msg = "AUTH_FAIL"
    except Exception as e:
        if str(e).find("string") == -1:
            print(e)

    try:
        client.send(return_msg.encode())
        print("Responding with:", return_msg)
    except Exception as e:
        print(e)
        # x = 1