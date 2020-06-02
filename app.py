import mysql.connector, os

mydb = mysql.connector.connect(
  host=os.environ.get('MYSQL_HOST'),
  user=os.environ.get('MYSQL_USER'),
  passwd=os.environ.get('MYSQL_PASSWORD'),
  database=os.environ.get('MYSQL_DATABASE')
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE todo (item varchar)")
mycursor.execute("INSERT INTO todo (item) VALUES ('apples', 'bananas', 'cherries')")

mycursor.execute("SELECT * FROM todo")

for x in mycursor:
  print(x)

