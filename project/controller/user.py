import models.user as md


def controllerUser():
    user=md.ModelUser()
    data=user.getUser()
    return data

def insertUser(data):
    user=md.ModelUser()
    user.insertUser(data)

def deleteUser(data):
    user=md.ModelUser()
    user.deleteUser(data)

def updateUser(data):
    user=md.ModelUser()
    user.updateUser(data)
