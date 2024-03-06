#conect to database mongodb

from pymongo import MongoClient
from CRUD import Crud


try:
    app = MongoClient("mongodb://localhost:27017")
    db = app.admin
    result = db.command('serverStatus')
    print("Base de Datos en ejecución.")
    while True:
        print("Selecciona la acción que desea ejecutar:")
        print("1- Crear colección nueva")
        print("2- Mostrar colecciones")
        print("3- Añadir elemento a una colección")
        print("4- Actualizar parametro de un elemento de una colección")
        print("5- Eliminar elemento de una colección")
        print("0 - Salir")
        input_data = input("Elije acción: ")
        print()
        if input_data == "1":
            Crud.create_collection(db)
        elif input_data == "2":
            Crud.show_list_collection(db)
        elif input_data == "3":
            Crud.create_file_json_collection(db)
        elif input_data == "4":
            Crud.update_file_json_collection(db)
        elif input_data == "5":
            Crud.delete_file_collection(db)
        elif input_data == "0":
            db.client.close()
            print("Base de datos finalizada.")
            break
except Exception  as e:
    print(e)
