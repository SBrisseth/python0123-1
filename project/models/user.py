import db

class ModelUser():
    def __init__(self):
        print('model user')
        self.db=db.Conection('tienda.db')

    def getUser(self):
        cursor=self.db.getCursor()
        data=cursor.execute('SELECT * FROM  USUARIOS').fetchall()
        return data

    def insertUser(self,data):
        inserSentence="INSERT INTO USUARIOS(USUARIO,PASSWORD,EMAIL,FULLNAME,SCORE,TIPOUSUARIO) VALUES(?,?,?,?,0,?)"
        cursor=self.db.getCursor()
        cursor.execute(inserSentence,data)
        self.db.con.commit()
        print('data insertada')

    def deleteUser(self,data):
        deletSentence ="DELETE FROM USUARIOS WHERE ID = ? "
        cursor=self.db.getCursor()
        cursor.execute(deletSentence,data)
        self.db.con.commit()
        print('data eliminada')

    def updateUser(self,data):
        updateSentence ="UPDATE USUARIOS SET USUARIO =?,PASSWORD =?,EMAIL=?,FULLNAME=?,SCORE=?, TIPOUSUARIO=? WHERE ID = ? "
        cursor=self.db.getCursor()
        cursor.execute(updateSentence,data)
        self.db.con.commit()
        print('data actualizada')

