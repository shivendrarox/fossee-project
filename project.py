import pymysql.cursors

#askDate is the function asking the date for determining a calendar month
def askDate():
      print("Please enter the date in yyyy-mm-dd format")
      date=input()
      return date


# function to connect to the database
def connectToDB():
      connection = pymysql.connect(host='localhost',
                                   user='root',
                                   password='1234',
                                   db='exp',
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)
      return connection

# function to create table of database exp
def makeTables():
      connection=connectToDB()
      try:
            with connection.cursor() as cursor:
                        table_user="""CREATE TABLE user
                                    (
                                          Pk_User_Id INT AUTO_INCREMENT,
                                          Name VARCHAR(40) NOT NULL,
                                          PRIMARY KEY(Pk_User_Id)
                                    )"""
                        table_tutorial_detail="""CREATE TABLE tutorial_detail
                                               (
                                                     Pk_Tutorial_Id INT PRIMARY KEY AUTO_INCREMENT,
                                                     TutorialName VARCHAR(70),
                                                     Fk_User_Id INT,
                                                     ExpectedDate DATE,
                                                     ActualDate DATE,
                                                     Deadline DATE,
                                                     FOREIGN KEY (Fk_User_Id)
                                                     REFERENCES user(Pk_User_Id)
                                                )"""
                        table_foss="""CREATE TABLE foss
                                    (
                                                      Pk_Foss_Id INT AUTO_INCREMENT,
                                                      UserName VARCHAR(70),
                                                      NoOfTutorials INT DEFAULT 10,
                                                      Fk_User_Id INT,
                                                      submission INT DEFAULT 1,
                                                      SubmissionDate DATE,
                                                      PRIMARY KEY (Pk_Foss_Id),
                                                      FOREIGN KEY (Fk_User_Id)
                                                      REFERENCES user(Pk_User_Id)
                                          )"""
                        table_payment="""CREATE TABLE payment
                                          (
                                                  Pk_Payment_Id INT PRIMARY KEY AUTO_INCREMENT,
                                                  Ammount INT NOT NULL DEFAULT 1000,
                                                  Fk_User_Id INT,
                                                  FOREIGN KEY	 (Fk_User_Id)
                                                  REFERENCES user(Pk_User_Id)
                                          )"""
                        cursor.execute(table_user)
                        cursor.execute(table_foss)
                        cursor.execute(table_tutorial_detail)
                        cursor.execute(table_payment)
                        connection.commit()
      finally:
            connection.close()

makeTables()#Do NOT call this if you are already having tables ready

#Inserting some sample data to test the functionality
def insertData():
      connection=connectToDB()
      try:
            with connection.cursor() as cursor:
                  #
                  cursor.execute("INSERT INTO user(Name) VALUES ('Shivendra Singh')")
                  cursor.execute("INSERT INTO user(Name) VALUES ('Virendra Singh')")
                  cursor.execute("INSERT INTO user(Name) VALUES ('Deepak Shukla')")
                  cursor.execute("INSERT INTO user(Name) VALUES ('Dev Singh')")
                  cursor.execute("INSERT INTO user(Name) VALUES ('Om Pathe')")
                  cursor.execute("INSERT INTO user(Name) VALUES ('Sujeet Patidar')")
                  #
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to C++',1,'2018-03-15','2018-03-15','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to Java',1,'2018-03-15','2018-03-26','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to Python',2,'2018-03-15','2018-03-01','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to Git',3,'2018-03-15','2018-03-25','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to ruby',4,'2018-03-15','2018-03-20','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Intro to C',4,'2018-03-15','2018-03-24','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Blender Basics',5,'2018-03-11','2018-02-20','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Android Basics',6,'2018-03-15','2018-03-23','2018-03-25')")
                  cursor.execute("INSERT INTO tutorial_detail(TutorialName,Fk_User_Id,ExpectedDate,ActualDate,Deadline) VALUES ('Easy iOS',5,'2018-03-11','2018-02-19','2018-03-25')")
                  #
                  cursor.execute("""INSERT INTO payment (Fk_User_Id)
                                    SELECT Fk_User_Id FROM tutorial_detail
                                    WHERE ActualDate<=Deadline""")
                  #
                  cursor.execute("""INSERT INTO foss(Fk_User_Id,UserName,SubmissionDate)
                                    SELECT t.Fk_User_Id,u.Name,t.ActualDate FROM tutorial_detail t,user u
                                    WHERE t.Fk_User_Id=u.Pk_User_Id AND t.ActualDate<=t.Deadline""")
                  connection.commit()
      finally:
            connection.close()

insertData()#Do NOT call this if you are already having some sample data ready

#function For task: Display a list of tutorials contributed with expected submission date and actual submission date for one calendar month.
def displayTutorialList():
      connection=connectToDB()
      print("Displaying a list of tutorials contributed with expected submission date and actual submission date for one calendar month by given date.")
      #dateToUse is the variable storing the date for determining a calendar month
      dateToUse=askDate()
      try:
            with connection.cursor() as cursor:
                  sql="SELECT TutorialName,ExpectedDate, ActualDate FROM tutorial_detail WHERE ActualDate BETWEEN(DATE(%s)-INTERVAL 1 MONTH) AND DATE(%s)"
                  cursor.execute(sql, (dateToUse,dateToUse))
                  result = cursor.fetchall()
                  for (row) in result:
                        print("Tutorial Name:",row["TutorialName"],"\tExpected Date:",row["ExpectedDate"],"\tActual Date:",row["ActualDate"])
      finally:
            connection.close()
            
displayTutorialList()

#function for task: Write a program to count the number of published tutorials that each contributor has submitted in one calendar month.
def countNoOfTutorials():
      connection=connectToDB()
      print("counting the number of published tutorials that each contributor has submitted in one calendar month by given date.")
      #dateToUse is the variable storing the date for determining a calendar month
      dateToUse=askDate()
      try:
          with connection.cursor() as cursor:
              sql="""SELECT  UserName,SUM(submission)
                  FROM    foss
                  WHERE SubmissionDate BETWEEN(DATE(%s)-INTERVAL 1 MONTH) AND DATE
                  (%s)
                  GROUP BY    UserName"""
              cursor.execute(sql, (dateToUse,dateToUse))
              result = cursor.fetchall()
              for (row) in result:
                  print("User Name:",row["UserName"],"\tPublished Tutorials:",row["SUM(submission)"])
      finally:
          connection.close()

countNoOfTutorials()

# function for task: Multiply the total number of tutorials by Rs.1000.
# and for the task: Calculate the final payment amount for each contributor and display it in a list.
def paymentForEachContributor():
      # In this func we are doing task no 4 and 5
      print("Multiplying no. of tuts. by 1000 and calculating final payment for each contributor")
      #dateToUse is the variable storing the date for determining a calendar month
      dateToUse=askDate()
      connection=connectToDB()
      try:
          with connection.cursor() as cursor:
              # Read a single record
              sql="""SELECT u.Name,SUM(submission)*1000 AS'Final Paymnet In Rs.'
                  FROM    foss,user u
                  WHERE Fk_User_Id=Pk_User_Id
                  GROUP BY    Fk_User_ID"""
              cursor.execute(sql)
              result = cursor.fetchall()
              for (row) in result:
                  print("User Name:",row["Name"],"\tFinal Paymnet In Rs.:",row["Final Paymnet In Rs."])
      finally:
          connection.close()

paymentForEachContributor()

#Just an extra utility for fun!!! :-)
def totalAmmount():
      print("\nJust an extra utility for fun!!! :-)")
      print("Summing up the required money to be paid to all contributors")
      connection=connectToDB()
      try:
          with connection.cursor() as cursor:
              # Read a single record
              sql="""SELECT SUM(Ammount) AS'Total Ammount For Contributors Rs.'
                  FROM payment"""
              cursor.execute(sql)
              result = cursor.fetchall()
              for (row) in result:
                  print("Total Ammount For Contributors Rs.: ",row["Total Ammount For Contributors Rs."])
      finally:
          connection.close()
totalAmmount()#try it?!!!
