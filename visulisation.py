import  matplotlib.pyplot as plt
import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Student_Data"
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()
select_query="""
select * from student_performence
"""
cursor.execute(select_query)
records = cursor.fetchall()
print(cursor)
print(records)

x=[]
y=[]
for i in records:
    x.append(i[1])
    y.append(i[2])
print(x)
print(y)
# x=records['roll_number']
# y=records['percentage']

#plt.plot(x,y)
plt.title("Percentages of students")
plt.xlabel("Names")
plt.ylabel("Performence")
#plt.bar(x,y)
cols=['c','m','r','b']
slices=y
#plt.pie(y,labels=x,colors=cols,startangle=90,shadow=True,explode=(0,0,0,0),autopct='%.1f')
plt.title('Pie Plot')
plt.scatter(x,y)
plt.grid(True)
plt.show()

