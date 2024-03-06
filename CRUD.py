class Crud:
    libro = dict()
    def create_collection(db):
        input_collection = input("Introduce un nombre para la nueva colección: ")
        nombre_coleccion_existente =db.list_collection_names()
        for coleccion in nombre_coleccion_existente:
            if coleccion == input_collection:
                print("Colección ya existente.")
                break
            else:
                db.create_collection(input_collection)
                print(f"Colección {input_collection} creada con éxito.")
                break
    
    def show_list_collection(db):
        nombre_coleccion_existente =db.list_collection_names()
        print("Lista de colecciones:")
        for coleccion in nombre_coleccion_existente:
            print(coleccion)
    
    def create_file_json_collection(db):
        nombre_coleccion_existente =db.list_collection_names()
        for coleccion in nombre_coleccion_existente:
            if coleccion == nombre_coleccion_existente:
                print("Nombre del fichero existente.")
            else:
                for coleccion in nombre_coleccion_existente:
                    print(coleccion)
                print()
                nombre_coleccion = input("Escriba el nombre de la colección en la que desea crear el fichero: ")
                if nombre_coleccion == "Libros":
                    input_autor = input("Nombre del autor: ")
                    input_titulo = input("Titulo del libro: ")
                    input_editorial = input("Editorial: ")
                    input_fecha_salida = input("Fecha salida: ")
                    libro = {"Autor": f"{input_autor}", "Titulo": f"{input_titulo}", "Editorial": f"{input_editorial}", "Fecha salida": f"{input_fecha_salida}"}
                    db.get_collection(f"{nombre_coleccion}").insert_one(libro)
                    print(f"Libro cuyo autor : {input_autor}, titulo: {input_titulo}, editorial: {input_editorial}, fehca de salida: {input_fecha_salida} creado con éxito en la base de datos.")
                    break
                elif nombre_coleccion == "Películas":
                    pass
                else:
                    print("Colección no encontrada.")
    
    def update_file_json_collection(db):
        nombre_coleccion_existente = db.list_collection_names()
        for e in nombre_coleccion_existente:
            print(e)
        input_collection_selected = input("Escriba la colección en la que se encuentra el fichero que desea modificar: ")
        
        try:
            item_coleccion_existente = db.get_collection(f"{input_collection_selected}").find()
            input_item_selected = input("Escriba el id del fichero a modificar: ")  
            for item in item_coleccion_existente:                       
                if str(item["_id"]) == input_item_selected: 
                    print(item)
            # --- Acceso a un elemento específico de una colección ---
                    input_element_update = input("Especifique el párametro a modificar: ")
                    try:
                        input_valor_parametro = input(f"Escriba el nuevo valor del parametro {input_element_update}: ")
                        valor_actual = {f"{input_element_update}": item[f"{input_element_update}"]}
                        valor_nuevo = {"$set": {f"{input_element_update}": f"{input_valor_parametro}"}}
                        db.get_collection(f"{input_collection_selected}").update_one(valor_actual, valor_nuevo)
                        print("Valor actualizado")
                        
            # --- Actualización de un parametro especifico de la colección ---
                    except Exception as e:
                        print(e)
                    finally:
                        db.client.close()
        except Exception as e:
            print(e)
    
    def delete_file_collection(db):
        nombre_coleccion_existente = db.list_collection_names()
       
        for collecion in nombre_coleccion_existente:
            print(collecion)
        input_collection_selected = input("Escriba la colección en la que desea eliminar el fichero: ") 
        item_coleccion_existente = db.get_collection(f"{input_collection_selected}").find()
        try:
            for coleccion in nombre_coleccion_existente:
                if coleccion == input_collection_selected:
                    input_select_file = input("Escriba el id del fichero que desea eliminar: ")
                    for item in item_coleccion_existente:
                        if str(item["_id"]) == input_select_file:
                            print(item)
                            db.get_collection(f"{input_collection_selected}").delete_one(item)
                            print("Fichero eliminado.")
                            
        except Exception as e:
            print(e)
                

