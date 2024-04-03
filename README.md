ef getAllData():
    #json-server storage/producto.json -b 4501 
    peticion= requests.get("http://154.38.171.54:5008/productos")
    data= peticion.json()
    return data

def getProductCodigo(codigo):
    peticion= requests.get(f"http://154.38.171.54:5008/productos/{codigo}")
    return[peticion.json()] if peticion.ok else []
funciones para llamar

print(tabulate(getAllProcuctoPrecio(), headers="keys", tablefmt = 'rounded_grid'))
para imprimir


if (__name__=='__main__'):
    while True:
            print("""

       
   
          0. Salir
          1. Cliente
          2. Oficina
          3. Empleados
          4. Pago
          5. Pedidos 
          6. producto
          
          """)
            opcion = int(input("\n Seleccione unas de las opciones: "))
            
            if(opcion==1):
                menuCliente()
            elif(opcion==2):
                menuOficina()
            elif(opcion==3):
                menuEmpleado()
            elif(opcion==4):
                menuPago()
            elif(opcion==5):
                menuPedido()
            elif(opcion==6):
                menuProducto()  
            elif(opcion==0):
                break           
    
            # try:
            #      opcion = int(input("\n Seleccione unas de las opciones: "))
            
            # except ValueError as error:
            #      print("Error generado"+error)

            
                 
            
            # finally:



            # if(opcion==1):
            #     cliente.menu()
            # elif(opcion==2):
            #     oficina.menu()
            # elif(opcion==3):
            #     empleado.menu()
            # elif(opcion==4):
            #     pago.menu()
            # elif(opcion==5):
            #     pedido.menu()
            # elif(opcion==6):
            #     menuProducto()  
            # elif(opcion==0):
            #     break           


# -----codigo para agragar ids----
             
            

# with open("storage/pedido.json", "r") as f:
#     fichero = f.read()
#     data = json.loads(fichero)
#     for i, val in enumerate(data):
#         data[i]["id"] = (i+1)
#     data = json.dumps(data, indent=4).encode("utf-8")
#     with open("storage/pedido.json", "wb+") as f1:
#         f1.write(data)
#         f1.close()


def postProducto():
    while True:
        producto = {
            "codigo producto": obtener_entrada("Ingrese el codigo del producto (XX-99): ", validar_codigo),
                "nombre producto": obtener_entrada("Ingrese el nombre del producto: ", validar_nombre),
                "gama_producto": obtener_entrada("Ingrese la gama del producto: ", validar_gama),
                "descripcion producto": obtener_entrada("Ingrese la descripcion del producto: ", validar_descripcion),
                "Dimensiones": obtener_entrada("Ingrese la dimension 11/99: ", validar_dimensiones),
                "Proveedor": obtener_entrada("Ingrese el proveedor: ", validar_proveedor),
                "cantidad_en_stock": input("Ingrese el stock del producto: "),
                "precio_venta": input("Ingrese el precio de venta: "),
                "precio_proveedor": input("Ingrese el precio del proveedor: ")
    }
        try:

            
                
            peticion= requests.post("http://154.38.171.54:5008/productos", data=json.dumps(producto))
            res = peticion.json()
            res["mensaje"]="Producto Guardado"
            print(tabulate([res], headers="keys", tablefmt="github"))
            input("Precione una tecla para continuar.....")
            break
        except Exception as error:
            print(error)

def deleteProducto(id):
    data = gP.getProductCodigo(id)
    if(len(data)):
        peticion = requests.delete(f"http://154.38.171.54:5008/productos/{id}")
        if(peticion.status_code == 204):
            data.append({"message": "producto eliminado correctamente"})
            return {
                "body": data, 
                "status": peticion.status_code,
            }
    else:
        return {
            "body":[{
                "message":"producto no encontrado",
                "id": id
            }],
            "status": 400,
        }
"codigo producto": input("Ingrese el nuevo código del producto (FF-99): "),
        "nombre producto": input("Ingrese el nuevo nombre del producto: "),
        "gama_producto": input("Ingrese la nueva gama del producto: "),
        "descripcion producto": input("Ingrese la nueva descripción del producto : "),
        "Dimensiones": input("Ingrese la nueva dimensión (XX/XX): "),
        "Proveedor": input("Ingrese el nuevo proveedor: "),
        "cantidad_en_stock": int(input("Ingrese el nuevo stock del producto: ")),
        "precio_venta": int(input("Ingrese el nuevo precio de venta: ")),
        "precio_proveedor": int(input("Ingrese el nuevo precio del proveedor: "))

def updateProducto(id):
    producto = {
        val
    }

    producto_existente = gP.getProductCodigo(id)
    if not producto_existente:
        return {"mensaje": "Producto no encontrado"}

    producto_actualizado = {**producto_existente[0], **producto}


    peticion = requests.put(f"http://http://154.38.171.54:5008/productos/{id}", data=json.dumps(producto_actualizado))
    res = peticion.json()

    if peticion.status_code == 200:
        res["mensaje"] = "Producto actualizado correctamente"
    else:
        res["mensaje"] = "Error al actualizar el producto"
    
    return [res]
