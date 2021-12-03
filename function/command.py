import sqlite3

def insert(tugas,dl):
    db=sqlite3.connect("tasklist.db")
    scriptins ="INSERT INTO TUGAS (TUGAS,DEADLINE,STATUS) VALUES(?,?,?);"
    status=0
    db.execute(scriptins,(tugas,dl,status))
    db.commit()
    db.close()

def delete(tugas):
    db=sqlite3.connect("tasklist.db")
    scriptdel="DELETE FROM TUGAS where TUGAS =?"
    db.execute(scriptdel,(tugas,))
    db.commit()
    db.close()

def changestat(tugas,stat):
    db=sqlite3.connect("tasklist.db")
    if stat:
        scriptupd="UPDATE TUGAS set STATUS = 0 where TUGAS=?"
    else:
        scriptupd="UPDATE TUGAS set STATUS = 1 where TUGAS=?"
    db.execute(scriptupd,(tugas,))
    db.commit()
    db.close()

def changedl(tugas,newdl):
    db=sqlite3.connect("tasklist.db")
    scriptupd="UPDATE TUGAS set DEADLINE = ? where TUGAS=?"
    db.execute(scriptupd,(newdl,tugas))
    db.commit()
    db.close()