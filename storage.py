# SCHOOL MANAGEMENT SYSTEM
# LIBRARY: storage


# IMPORT LIBRARIES
import string
import hashlib
import random
import base64


# GLOBAL VARIABLES
initialized = False
path = ""
current = open("data/_tmp.sdata", "w")
current.close()


# FUNCTIONS

# Initializes storage
def init(folder):
    global path
    global initialized
    if not initialized:
        if not folder.endswith("/"):
            folder = folder + "/"
        path = folder
        initialized = True

# Encrypts a text
def encrypt(text):
    pattern = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234/")
    enc = base64.b64encode(text.encode())
    enc = enc.decode()
    enc = enc.translate(pattern)
    return enc

# Decrypts a text
def decrypt(text):
    pattern = str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm5678901234/")
    dec = text.translate(pattern)
    dec = base64.b64decode(dec.encode())
    dec = dec.decode()
    return dec

# Logs in
def login(sid, pwd):
    global current
    try:
        student = open(path + encrypt(sid) + ".sdata", "r")
        password = student.read(64)
        hashed = hashlib.sha256(pwd.encode()).hexdigest()
        if hashed == password:
            current = student
            return 0 # OK
        return 2 # Wrong Password
    except IOError:
        return 1 # Student data doesn't exist

# Logs out
def logout():
    current.close()
    
# Creates an account
def createID(sid, pwd, name, c):
    try:
        try:
            student = open(path + encrypt(sid) + ".sdata", "r")
            return 1 # ID already exist
        except IOError:
            student = open(path + encrypt(sid) + ".sdata", "w")
            student.write(hashlib.sha256(pwd.encode()).hexdigest())
            student.write("\n" + encrypt(name))
            student.write("\n" + encrypt(c))
            for _ in range(49):
                student.write("\n")
            student.close()
            return 0 # OK
    except IOError:
        return 1 # Runtime error

# Creates an account manually
def createRaw(sid, data):
    try:
        try:
            student = open(path + encrypt(sid) + ".sdata", "r")
            return 1 # ID already exist
        except IOError:
            student = open(path + encrypt(sid) + ".sdata", "w")
            student.write(hashlib.sha256(data[0].encode()).hexdigest())
            for x in range(51):
                student.write("\n" + encrypt(data[x + 1]))
            student.close()
            return 0 # OK
    except IOError:
        return 1 # Runtime error

# Changes password
def changePassword(sid, oldPwd, newPwd, admin=False):
    global current
    try:
        if admin == True:
            current = open(path + encrypt(sid) + ".sdata", "r")
            current.seek(64)
            tmp = current.read()
            student = open(path + encrypt(sid) + ".sdata", "w")
            student.write(hashlib.sha256(newPwd.encode()).hexdigest())
            student.write(tmp)
            student.close()
            return 0 # OK
        current.seek(0)
        password = current.read(64)
        hashed = hashlib.sha256(oldPwd.encode()).hexdigest()
        if hashed == password:
            current.seek(64)
            tmp = current.read()
            student = open(path + encrypt(sid) + ".sdata", "w")
            student.write(hashlib.sha256(newPwd.encode()).hexdigest())
            student.write(tmp)
            student.close()
            return 0 # OK
        return 2 # Wrong password
    except IOError:
        return 1 # Runtime error

# Returns line data
def getLine(sid, line=1):
    tmp = open(path + encrypt(sid) + ".sdata", "r")
    if line == 1:
        return decrypt(tmp.readline())
    for _ in range(line - 1):
        tmp.readline()
    return decrypt(tmp.readline())

# Sets line data
def setLine(sid, data, line=1):
    try:
        tmp = open(path + encrypt(sid) + ".sdata", "r")
        tmp1 = ""
        tmp2 = ""
        if line == 1:
            tmp.readline()
            tmp1 = tmp.read()
            tmp.close()
            tmp = open(path + encrypt(sid) + ".sdata", "w")
            tmp.write(hashlib.sha256(data.encode()).hexdigest() + "\n")
            tmp.write(tmp1)
            return 0 # OK
        elif line == 52:
            for _ in range(51):
                tmp1 = tmp1 + tmp.readline()
            tmp.close()
            tmp = open(path + encrypt(sid) + ".sdata", "w")
            tmp.write(tmp1)
            tmp.write(encrypt(data))
            tmp.close()
            return 0 # OK
        else:
            for _ in range(line - 1):
                tmp1 = tmp1 + tmp.readline()
            tmp.readline()
            tmp2 = tmp.read()
            tmp = open(path + encrypt(sid) + ".sdata", "w")
            tmp.write(tmp1)
            tmp.write(encrypt(data) + "\n")
            tmp.write(tmp2)
            tmp.close()
            return 0 # OK
    except IOError:
        return 1 # Student doesn't exist


    
# Returns the manual data edit guide
def getLinesHelp():
    global path
    tmp = open("lines.txt", "r")
    return decrypt(tmp.read())

# Returns student name
def getName():
    current.seek(0)
    current.readline()
    return decrypt(current.readline())

# Returns student class
def getClass():
    current.seek(0)
    current.readline()
    current.readline()
    return decrypt(current.readline())

# Returns student exam result
def getExamResult():
    current.seek(0)
    result = []
    for _ in range(3):
        current.readline()
    for _ in range(40):
        result.append(decrypt(current.readline()))
    return result

# Returns student cocurriculum result
def getCocurriculum():
    current.seek(0)
    co = []
    for _ in range(43):
        current.readline()
    for _ in range(9):
        co.append(decrypt(current.readline()))
    return co