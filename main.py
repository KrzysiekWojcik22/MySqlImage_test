import mysql.connector


mydb = mysql.connector.connect(
host='localhost',
user='root',
password='KrzysiekmySql12',
database="sql-kurs"
)

MyCursor = mydb.cursor()



def InsertBlob(FilePath):
    with open(FilePath, "rb") as File:
        BinaryData = File.read()
        SQLStatement = "INSERT INTO IMAGES (PHOTO) VALUES (%s)"
        MyCursor.execute(SQLStatement, (BinaryData, ))
        mydb.commit()

def RetrieveBlob(ID):
    SQLStatement2 = "SELECT * FROM Images where id = '{0}'"
    MyCursor.execute(SQLStatement2.format(str(ID)))
    MyResult = MyCursor.fetchone()[1]
    StoreFilePatch="ImageOutputs/img{0}.jpg.".format(str(ID))
    print(MyResult)
    with open(StoreFilePatch, "wb") as File:
        File.write(MyResult)
        File.close()

print("1. Insert Image\n2. Read Image")
MenuInput = input()

if int(MenuInput) == 1:
    UserFilePath = input("Enter File Path :")
    InsertBlob(UserFilePath)
elif int(MenuInput) == 2:
    UserIDChoice = input("Enter ID:")
    RetrieveBlob(UserIDChoice)
