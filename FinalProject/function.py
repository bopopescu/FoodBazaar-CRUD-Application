

import pymysql

def connection():
    conn = pymysql.connect(host="localhost",
                           user = "root",
                           passwd = "",
                           db = "fooddb",cursorclass=pymysql.cursors.DictCursor)
    c = conn.cursor()

    return c, conn

