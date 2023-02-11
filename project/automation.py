import openpyxl
import pandas as pd
from tabulate import tabulate
import os
import db

def insertData():
    compra_dolar = float(input("ingrese valor compra:"))
    venta_dolar = float(input("ingrese valor venta:"))
    fecha = input("ingrese valor fecha:")
    data = (compra_dolar,venta_dolar,fecha)
    query="INSERT INTO CAMBIO_DOLAR VALUES(NULL,?,?,?)"
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    cursor.execute(query,data).fetchall()
    conn.con.commit()
    print("data insertada")


def readData():
    conn=db.Conection('tienda.db')
    cursor=conn.getCursor()
    query="SELECT * FROM CAMBIO_DOLAR"
    result = cursor.execute(query).fetchall()
    key_list=['ID','COMPRA DOLAR','VENTA DOLAR','FECHA']
    df=pd.DataFrame(result,columns=key_list)
    print(tabulate(df,headers=key_list,tablefmt='psql'))
    print("desea generar un reporte ?")
    b=input("si")
    if (b =='si'):
        df.to_excel('Historico_Dolar.xlsx',sheet_name='hoja1',index=False)
    



def updateData():
    id = int(input("INGRESA EL ID: "))
    if(id > 0):
        compra_dolar = float(input("ingrese valor compra:"))
        venta_dolar = float(input("ingrese valor venta:"))
        fecha = input("ingrese valor fecha:")
        data = (compra_dolar,venta_dolar,fecha,id)
        query="UPDATE CAMBIO_DOLAR SET COMPRA_DOLAR=?,VENTA_DOLAR=?,FECHA =? WHERE ID = ? "
        conn=db.Conection('tienda.db')
        cursor=conn.getCursor()
        result=cursor.execute(query,data).fetchall()
        conn.con.commit()
        print("data actualizada!")
        # print(result)
    else:
        print("Se require un ID")
   



while True:
    message="""
            1)Mostrar registros
            2)Insertar data:
           
            3)Actualizar data del dolar
                3.1) Generar un reporte
            """
    print(message)
    a=int(input('ingrese la tarea a realizar: '))
    if(a==1):
        readData()
    elif(a==2):
        insertData()
        readData()
    elif(a==3):
        updateData()
        readData()
    #     insertData()
    #     readData()
    # elif(a==2):
    #     updateData()
    #     readData()
    else:
        break
