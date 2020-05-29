import mysql.connector

mydb = mysql.connector.connect(
  host="mysql",
  user="userHS1",
  passwd="hhwEuNbp3DOUvaAn"
  database="sampledb"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE todo (item varchar)")
mycursor.execute("INSERT INTO todo (item) VALUES ('apples', 'bananas', 'cherries')")

mycursor.execute("SELECT * FROM todo")

for x in mycursor:
  print(x)

