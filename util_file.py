__author__ = 'AbuZahedJony'

'''
    Write content into file
'''
def write_to_file(fileName, content):
    f = open(fileName, 'w')
    f.write(content)
    f.close()

'''
    Read content into file
'''
def read_from_file(fileName):
    f = open(fileName, 'r')
    content = f.read()
    f.close()
    return content

'''
    Backup file "fileName" into "newFile"
'''
def backup_file(fileName, newName):
    s = read_from_file(fileName)
    write_to_file(newName, s)