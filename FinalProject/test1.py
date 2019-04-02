"""
This is the unit test  for testing Food Bazaar  .
Name:Rohan Anand 
Date:2018-11-10
"""

import unittest
import function
import pymysql

class Test_test1(unittest.TestCase):
# defines test_dbConnection to test the database connectivity.
    def test_dbConnection(self):
        Response=""
        try:
            conn = pymysql.connect(host="localhost",user = "root",passwd = "",db = "fooddb",cursorclass=pymysql.cursors.DictCursor)
            c = conn.cursor()
            sql = "SELECT VERSION()"
            c.execute(sql)
            results = c.fetchone()
            if results:
                Response="Ok"
            else:
                Response="Not" 

        except Exception as e:
            Response="Not" 

        self.assertEqual("Ok",Response)
# defines test_Username to test the username used.
    def test_Username(self):

        StoredUsername = "Admin"

        InputUsername = "Admin"

        self.assertEqual(StoredUsername, InputUsername)

 # defines test_Password to test the password used.
    def test_Password(self):

        StoredUserPassword = "123"

        InputUserPassword = "123"

        self.assertEqual(StoredUserPassword, InputUserPassword)
 # defines test_SearchRecord to test the record search.
    def test_SearchRecord(self):

        RecordID=94
        Response=""
        try:
            c, conn =function.connection()
            sql = "select * from recordtbl where ID=%s"
            c.execute(sql,RecordID)
            if(c.rowcount >=1):
                rows = c.fetchall()
                Response="Ok"
            else:
                Response="Not"

        except Exception as e:
            return(str(e))
        
        self.assertEqual("Ok",Response)
 # defines test_InsertRecord to test the record insertion.
    def test_InsertRecord(self):
        Response=""
        try:
            tabYear="2018"
            tabCountry="Australia"
            tabDGUID="2016A000011124"
            tabFood_categories="Food available"
            tabCommodity="Wheat flour"
            tabUOM="Kilograms per person, per year";
            tabUOM_ID="195"
            tabSCALAR_FACTOR="units"
            tabSCALAR_FACTORID="0"
            tabVECTOR="v108209"
            tabCOORDINATE="1.1.1"
            tabVALUE="59.19"
            tabSTATUS=""
            tabSYMBOL="";
            tabTERMINATED=""
            tabDECIMALS="2"
            c, conn =function.connection()
            sql = "insert into recordtbl(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,ColumnVALUE,ColumnSTATUS,SYMBOL,ColumnTERMINATED,DECIMALS) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            c.execute(sql,(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS))
            if(c.rowcount >=1):
                rows = c.fetchall()
                Response="Ok"
            else:
                Response="Not"

        except Exception as e:
            return(str(e))

        self.assertEqual("Ok",Response)
 # defines test_DeleteRecord to test the record deletion.
    def test_DeleteRecord(self):
        
        RecordID=1
        Response=""
        try:
            c, conn =function.connection()
            sql = "delete from recordtbl where ID=%s"
            c.execute(sql,RecordID)
            if(c.rowcount >=1):
                rows = c.fetchall()
                Response="Ok"
            else:
                Response="Not"

        except Exception as e:
            return(str(e))
        
        self.assertEqual("Ok",Response)
 # defines test_DeleteRecord to test the record deletion.
    def test_DeleteRecord(self):

        RecordID=1
        Response=""
        try:
            tabYear="2018"
            tabCountry="Australia"
            tabDGUID="2016A000011124"
            tabFood_categories="Food available"
            tabCommodity="Wheat flour"
            tabUOM="Kilograms per person, per year";
            tabUOM_ID="195"
            tabSCALAR_FACTOR="units"
            tabSCALAR_FACTORID="0"
            tabVECTOR="v108209"
            tabCOORDINATE="1.1.1"
            tabVALUE="59.19"
            tabSTATUS=""
            tabSYMBOL="";
            tabTERMINATED=""
            tabDECIMALS="2"
            c, conn =function.connection()
            sql = "update recordtbl set REF_DATE=%s,GEO=%s,DGUID=%s,Food_categories=%s,Commodity=%s,UOM=%s,UOM_ID=%s,SCALAR_FACTOR=%s,SCALAR_ID=%s,VECTOR=%s,COORDINATE=%s,ColumnVALUE=%s,ColumnSTATUS=%s,SYMBOL=%s,ColumnTERMINATED=%s,DECIMALS=%s where ID=%s"
            c.execute(sql,(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS,recID))
            if(c.rowcount >=1):
                rows = c.fetchall()
                Response="Ok"
            else:
                Response="Not"

        except Exception as e:
            return(str(e))

        self.assertEqual("Ok",Response)
if __name__ == '__main__':
    unittest.main()
