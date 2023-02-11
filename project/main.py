import controller as ctr
import pandas as pd
from tabulate import tabulate

message="""
    1)Insertar un usuario
    2)ver lista de usuarios
    3)eliminar usuarios
    4)actualizar usuarios


"""
global option


def registerUser():
    usuario=input('ingrese el siguiente data usuario: ')
    password=input('ingrese el siguiente data password: ')
    email=input('ingrese el siguiente data email: ')
    fullname=input('ingrese el siguiente data fullname: ')
    tipousuario=input('ingrese el siguiente data tipousuario: ')
    data=(usuario,password,email,fullname,tipousuario)
    try:
        ctr.insertUser(data)
    except Exception as e:
         print("error al ingresar data")
         print(e)

def listUser():
    data=ctr.controllerUser()
    # for row in data:
    #     print(row)
   
    key_list=['ID','USUARIO','PASSWORD','EMAIL','FULLNAME','SCORE','TIPOUSUARIO']
    df=pd.DataFrame(data,columns=key_list)
    print(tabulate(df,headers=key_list,tablefmt='psql'))

def deleteUser():
    id = int(input("INGRESA EL ID: "))
    data = (id,)
    try:
        ctr.deleteUser(data)
    except Exception as e:
         print("error al eliminar data")
         print(e)

def updateUser():
    id = int(input("INGRESA EL ID: "))
    usuario = input("ingrese el usuario:")
    password =input("ingrese la contraseña:")
    email =input("ingrese el email:")
    fullname =  input("ingrese fullname:")
    score  =int(input("ingrese score:"))
    tipo_usuario = input("ingrese el tipousuario:")
    data = (usuario,password,email,fullname,score,tipo_usuario,id)
    try:
        ctr.updateUser(data)
    except Exception as e:
         print("error al actualizar data")
         print(e)




if __name__=='__main__':
    while True:
        option=input('ingrese una opcion: ')
        if option=='1':
            registerUser()
                # listUser()
        elif option == '2':
                # deleteUser()
            listUser()
        elif option == '3':
            deleteUser()
        elif option == '4':
            updateUser()
        else:
            print("error")
            break



