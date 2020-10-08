import pymongo
from pymongo import MongoClient
cluster = MongoClient("mongodb+srv://tedgiggles:020203@cluster0.vtvm9.mongodb.net/test?retryWrites=true&w=majority")
db = cluster ["test"]
collection = db ["test"]
post1 = {"day": "monday",
         "subject1": "Дискретная математика",
         "subject2": "Алгебра и геометрия",
         "subject3": "Алгебра и геометрия",
         "subject4": "Нет пары",
         "subject5": ""}
post2 = {"day": "tuesday",
         "subject1": "АСД",
         "subject2": "None/АСД",
         "subject3": "Нет пары",
         "subject4": "Нет пары",
         "subject5": "Нет пары"}
post3 = {"day": "wednesday",
         "subject1": "Украинский/Мат Анализ",
         "subject2": "Дискретная математика",
         "subject3": "ФП",
         "subject4": "tim",
         "subject5": "Нет пары"}
post4 = {"day": "thursday",
         "subject1": "Нет пары",
         "subject2": "АП",
         "subject3": "None/Украинский язык",
         "subject4": "Программирование",
         "subject5": "Нет пары"}

post5 = {"day": "friday",
         "subject1": "Физика",
         "subject2": "Физика",
         "subject3": "Математический Анализ",
         "subject4": "Математический Анализ",
         "subject5": "Нет пары"}
#collection.insert_many([post1,post2,post3,post4,post5])

#results = collection.find({"day":"monday"})
#for result in results:
#    print(result["subject1"])
#   print(result["subject2"])
#   print(result["subject3"])


#results = collection.find_one({})
#for x in results:
#    print(results)

#results = collection.delete_one({"id": 0})
#удалить запись


#collection.update_many({"id": 0}, {"$set":{"name":"Bill"} } )



