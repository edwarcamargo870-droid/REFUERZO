"""INTEGRANTES
BRAYAN RAFAEL MEDINA MADIEDO
EDWAR JOSE PARRA CAMARGO 
ANDRES RUEDA
"""
Productos=[{
"papas" : 2500,
"gaseosa":  3000,
"galletas": 1800,
"chocolate": 2200,
"jugo": 2800
}]         
print("------------------------------------------------------")   
print("Menu principal:")
print("1.Ver productos disponibles")
print("2.Agregar producto al carrito")
print("3.Ver el carrito de compras")
print("4.Pagar y salir")
print("5.salir sin comprar")
opcion = int(input("ingrese la opcion: "))

print("------------------------------------------------")
while True:
     if opcion == 1:
        print("productos", Productos)
        break   
     elif opcion == 2:
        print("que producto desea agregar")
        Productos=input("producto: ")
        n1=input("cantidad: ")
        if Productos== "salir":
         print ("productos", Productos)
         print("total:", len(Productos),"productos")   
         

       
        
        
