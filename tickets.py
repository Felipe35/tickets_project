import sqlite3
# Studen Name: Andres Felipe Penaranda
# Assigment Number: 5
#======Recursive Functions=====

def inputString():
    return "Please Enter:\n \t\t |Actual mph| - |Posted mph| - |Age values|\nFallow by space: "

def checkMph(data):
    for row in data:
        if row[1] > row[2]:
             mph = row[1] - row[2]   
        else:
             mph = 0        
        print("%-5d %-15d %-10s %-5s %-10s" % (row[0], row[2], mph,row[3], row[4]))

def ids(data):
   for i in data:
        yield i[0]
        
#======Recursive Functions=====

def addTicket(cur,conn):

    while True:
        try:
            actMph, potMph, age = [int(actMph) for actMph in input(inputString()).split()]
            offSex = input("Enter violator sex: ").lower()

            if offSex.isdigit() == False and offSex in ['male','female']:
                offSex = offSex.capitalize()
                data = (None, actMph, potMph, age, offSex)
                sql = "INSERT INTO tickets VALUES (?, ?, ?, ?, ?) "
                question = input("Save your changes to this file? y/n: ")
                

                if question == 'y':
                    cur.execute(sql, data)
                    conn.commit()
                    print("Save success!")
                    break
                elif question == 'n':
                    print("Than you!")
                    break
            else:
                print("Please enter only gender (male/female)")
        except ValueError:
            print("Please enter only integer numbers")    


def displayAllTickets(cur):
    sql = "SELECT * FROM tickets"
    cur.execute(sql)

    results = cur.fetchall()

    if results:
        printStuff(results)
    else:
        print('No data found')

    print()

def displayTickestsByGender(cur):
    
    violator_sex = input("Enter user gender: ").lower()
    data = (violator_sex.capitalize(), )
    
    sql = "SELECT * FROM tickets WHERE violator_sex = ?"

    cur.execute(sql,data)
    results = cur.fetchall()

    if results and violator_sex in ['male','female']:
        printStuff(results)
    else:
        print("Name no found")
        print()
   


def deletTicket(cur,conn):
   
    while True:
        try:
           
            askId = int(input("Enter ID ticket to delete or type: 0  to exit."))
           
            sql = "SELECT * FROM tickets"
            cur.execute(sql)
            results = cur.fetchall()
            myIdList = ids(results)
            myIdList = list(myIdList)

            if askId in list(myIdList):
                sql = f"DELETE FROM tickets WHERE tid = {askId}"
                cur.execute(sql)
                conn.commit()
                print("Record has been deleted succesfully ")
                break
            elif askId == 0:
                print("Thanks Goodbye!")
                break
            else:
                print("ID is not found")
                continue
        except:
            print("Please insert only digits.")
            continue
            



def printStuff(data):
    print("%-5s %-15s %-10s %-5s %-10s" % ('idT','Posted MPH','MPH Over','Age','Violator Sex'))
    checkMph(data)
    print()


def main():
    conn = sqlite3.connect('tickets5.db')
    cur = conn.cursor()
    
    while True:
        print("""
            1. Display all Tickets
            2. Add a Ticket
            3. Filter by Offender Sex
            4. Delete record
            5. Save & Exit
        """)

        opt = input("Enter choice: 1, 2, 3, 4, or 5:  ")

        if opt == "1":
            displayAllTickets(cur)
        elif opt == "2":
            addTicket(cur,conn)   
        elif opt == "3":
            displayTickestsByGender(cur)
        elif opt == "4":
            deletTicket(cur,conn)
        elif opt == "5":
            print()
            print("Goodbye!")
            if conn:
                conn.close
            break
        else:
            print('invalid')

main()


