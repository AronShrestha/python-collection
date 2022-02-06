import mysql.connector as connection
import pandas as pd



class Model_diary:
    """
    It's a simple model for storing your data
    """
    tasks = {}
    def work(self):
        print('I am there')

class View():
    def setup(self,controller):
        controller.ask_input()
        controller.show()
        

    

class Controller():
    def __init__(self,model,view) -> None:
        self.model = model
        self.view =  view
    
    def start(self):
        try :
            mydb =  connection.connect(host='localhost',database='Aron',user='root',passwd='root',use_pure=True)
                
            query = "Create table if not exists dairy (Day Varchar(10), Task Varchar(300))"
        
            cursor =  mydb.cursor()
            cursor.execute(query)
            mydb.close()

        except Exception as e:
            mydb.close()
            print(str(e))

        self.view.setup(self)


    
    def ask_input(self)->None:
        days=['sunday','monday','tuesday','wedbesday','thursday','friday','saturday']
        day = input("Enter the day")
        if day.casefold() not in days:
            raise Exception (day,"is not a valid day")
 
        task = input("Enter the task") 
        self.model.tasks[day.casefold()] =task
        self.model.work()


    def show(self) :
      print(self.model.tasks)


    

d1 = Controller(Model_diary(),View())
d1.start()