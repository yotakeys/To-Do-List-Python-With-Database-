import sqlite3
import rich
from rich import print
from rich.console import Console
from rich import pretty

pretty.install()
console=Console()

from function.interface import cls,header,garis
from function.command import insert,delete,changestat,changedl

db=sqlite3.connect("tasklist.db")
db.execute('''CREATE TABLE IF NOT EXISTS 
        TUGAS
        (
            TUGAS TEXT NOT NULL,
            DEADLINE TEXT NOT NULL,
            STATUS INT NOT NULL
        )
        ''')

def alltask():
    list=db.execute("SELECT TUGAS,DEADLINE,STATUS FROM TUGAS")
    return list

def main():
    while(1):
        cls()
        header()
        console.print("[bold purple]Your ToDoList : ")
        list=alltask()
        arrname=[]
        arrstat=[]
        i=1
        for cetak in list:
            print(f'{i:3} \t {cetak[0]:40} {cetak[1]:8}',end=" ")
            arrname.append(cetak[0])
            arrstat.append(cetak[2])
            if cetak[2]:
                console.print(":white_check_mark:")
            else:
                console.print(":x:")
            i+=1
        garis()
        console.print("Command (insert/delete/update)   : ",end="")
        command=input()
        if "insert" in command:
            print("Insert Task name                 : ",end="")
            task=input()
            print("Insert Task Deadline (DD/MM/YY)  : ",end="")
            dl=input()
            insert(task,dl)
        elif "delete" in command:
            print("Insert ID , want to delete       : ",end="")
            id=int(input())
            delete(arrname[id-1])
        elif "update" in command:
            print("Choose to update (dl/stat)?      : ",end="")
            choose=input()
            if "dl" in choose:
                print("Insert ID , to change deadline   : ",end="") 
                id=int(input())
                print("Insert new deadline (DD/MM/YY)   : ",end="")
                newdl=input()
                changedl(arrname[id-1],newdl)
            elif "stat" in choose:
                print("Insert ID , to change status     : ",end="") 
                id=int(input())
                changestat(arrname[id-1],arrstat[id-1])
        else:
            console.print("[red]Command Not Valid")
main()
db.close()