import MySQLdb as mdb    
    
def connectToDB():
    try:
        db = mdb.connect('180.232.102.12', 'aids', '', 'aids-system')

    except mdb.Error as e:
        print('Connection failed!')
        sys.exit(1)
    
    return (db)