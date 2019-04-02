"""
This the Home page of Food Bazaar Application which performs uploading,insertion,deletion and update on csv dataset  file.
Name:Rohan Anand 
Date:2018-11-10
"""

import csv
import os
import codecs
import csv
import function
from flask import Flask,render_template,redirect, url_for, request
from datetime import datetime
from FinalProject import app


@app.route('/')
@app.route('/home')

# defines home function which renders the home page 
def home():
 
    #firstline=True
    #with open('Uploads/dataset.csv', 'r') as csvfile:
     

    #    csvReader = csv.reader(codecs.open('Uploads/dataset.csv', 'rU', 'utf-16'))
    #    for ReadLine in csvReader:
    #        if firstline:
    #            firstline = False
    #            continue
                
    #        Record=ReadLine
    #        #print(Record)
    #        Start=1

    #        for i in Record:
    #            p=i
    #            words = [p.replace('\t','#') for word in p]
    #            m1=str(words[0])
    #            #print(m1)
    #            r1=m1.split('#')
    #            #print(m1.count("#"))

    #            if(m1.count("#")==5):

    #                    print "A1",r1[0]
    #                    print "A2",r1[1]
    #                    print "A3",r1[2]
    #                    print "A4",r1[3]
    #                    print "A5",r1[4]
    #                    print "A6",r1[5]

    #            if(m1.count("#")==4):

                    
    #                    print "A1",r1[0]
    #                    print "A2",r1[1]
    #                    print "A3",r1[2]
    #                    print "A4",r1[3]
    #                    print "A5",r1[4]

    #            if(m1.count("#")==0):

    #                    print "A5",r1[0]
                        
    #            if(m1.count("#")==1):

    #                    print "A5",r1[0]
    #                    print "A6",r1[1]

    #            if(m1.count("#")==2):

    #                    print "A5",r1[0]
    #                    print "A5",r1[1] 
    #                    print "A6",r1[2]
                                
    #            if(m1.count("#")==3):

    #                    print "A5",r1[0]
    #                    print "A5",r1[1] 
    #                    print "A5",r1[2]
    #                    print "A6",r1[3]
                            
               
    #            if(m1.count("#")==9):    
                        
    #                    print "A6",r1[0]
    #                    print "A7",r1[1]
    #                    print "A8",r1[2]
    #                    print "A9",r1[3]
    #                    print "A10",r1[4]
    #                    print "A11",r1[5]
    #                    print "A12",r1[6]
    #                    print "A13",r1[7]
    #                    print "A14",r1[8]
    #                    print "A15",r1[9]
    #                    print "A16",r1[10]
                                  
    #            if(m1.count("#")==10):    
                        
    #                    print "A6",r1[0]
    #                    print "A7",r1[1]
    #                    print "A8",r1[2]
    #                    print "A9",r1[3]
    #                    print "A10",r1[4]
    #                    print "A11",r1[5]
    #                    print "A12",r1[6]
    #                    print "A13",r1[7]
    #                    print "A14",r1[8]
    #                    print "A15",r1[9]
    #                    print "A16",r1[10]
                       


                #print r1[6],"G"
                #print r1[7],"H"
           
       # print data_list


    return render_template(
        'index.html',
        title='Statup Page',
        year=datetime.now().year,
    )

@app.route('/login')
# defines login function which renders the Login page
def login():
    """Renders the login page."""
    return render_template(
        'login.html',
        title='Member Login',
        year=datetime.now().year,
        message='Your Login page.'
    )

@app.route('/logincheck',methods = ['POST'])
# defines logincheck function to request username and password
def logincheck():
     Username=""
     Password=""

     Username = request.form['Username']
     Password = request.form['Pass']
     Match=""

     if Username == "Admin" and Password=="123":
           return render_template(
        'home.html',
        title='Home Page',
        year=datetime.now().year,
    )
     else:
            return render_template(
        'login.html',
        title='Login Page',
        year=datetime.now().year,
    )
       
 

@app.route('/upload')
# defines Upload function which renders the Upload  page 
def upload():  
    """Renders the upload page."""
    return render_template(
        'upload.html',
        title='Upload CSV File',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/readContents',methods = ['POST'])
# defines redwrite function to read the data
def ReadWrite():
      firstline = True    
      fileupload=""
      tabYear=""
      tabCountry=""
      tabDGUID=""
      tabFood_categories=""
      tabCommodity=""
      tabUOM="";
      tabUOM_ID=""
      tabSCALAR_FACTOR=""
      tabSCALAR_FACTORID=""
      tabVECTOR=""
      tabCOORDINATE=""
      tabVALUE=""
      tabSTATUS=""
      tabSYMBOL="";
      tabTERMINATED=""
      tabDECIMALS=""
      fileupload = request.files['DataFileUpload']
      f = os.path.join(app.config['UPLOAD_FOLDER'], fileupload.filename)
      fileupload.save(f)

      #csvReader = csv.reader(codecs.open('file.csv', 'rU', 'utf-16'))
      Start=1;
      firstline=True
      with open('Uploads/'+fileupload.filename, 'r') as csvfile:
        csvReader = csv.reader(codecs.open('Uploads/'+fileupload.filename, 'rU', 'utf-16'))


        for ReadLine1 in csvReader:
            if firstline:
                firstline = False
                continue
                
            Record=ReadLine1
            for i in Record:
                p=i
                words = [p.replace('\t','#') for word in p]
                m1=str(words[0])
                r1=m1.split('#')

                if(m1.count("#")==5):
                        tabYear=r1[0]
                        tabCountry=r1[1]
                        tabDGUID=r1[2]
                        tabFood_categories=r1[3]
                        tabCommodity=r1[4]
                        tabUOM=r1[5]

                if(m1.count("#")==4):
                        tabYear=r1[0]
                        tabCountry=r1[1]
                        tabDGUID=r1[2]
                        tabFood_categories=r1[3]
                        tabCommodity=r1[4]
                        #tabUOM=r1[5]

                if(m1.count("#")==0):
                        tabCommodity=tabCommodity+","+r1[0]
                        
                if(m1.count("#")==1):
                        tabCommodity=tabCommodity+","+r1[0]
                        tabUOM=r1[1]
                if(m1.count("#")==2):
                        tabCommodity=tabCommodity+","+r1[0]+","+r1[1]
                        tabUOM=r1[2]
                if(m1.count("#")==3):
                        tabCommodity=tabCommodity+","+r1[0]+","+r1[1]+","+r1[2]
                        tabUOM=r1[3]


                if(m1.count("#")==10): 
                        
                        tabUOM=tabUOM+","+r1[0]
                        tabUOM_ID=r1[1]
                        tabSCALAR_FACTOR=r1[2]
                        tabSCALAR_FACTORID=r1[3]
                        tabVECTOR=r1[4]
                        tabCOORDINATE=r1[5]
                        tabVALUE=r1[6]
                        tabSTATUS=r1[7]
                        tabSYMBOL=r1[8]
                        tabTERMINATED=r1[9]
                        tabDECIMALS=r1[10]

                if(m1.count("#")==10): 
                        
                        tabUOM=tabUOM+","+r1[0]
                        tabUOM_ID=r1[1]
                        tabSCALAR_FACTOR=r1[2]
                        tabSCALAR_FACTORID=r1[3]
                        tabVECTOR=r1[4]
                        tabCOORDINATE=r1[5]
                        tabVALUE=r1[6]
                        tabSTATUS=r1[7]
                        tabSYMBOL=r1[8]
                        tabTERMINATED=r1[9]
                        tabDECIMALS=r1[10]
                        try:
                            c, conn =function.connection()
                            sql = "insert into recordtbl(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,ColumnVALUE,ColumnSTATUS,SYMBOL,ColumnTERMINATED,DECIMALS) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                            #sql = "insert into recordtbl(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,ColumnVALUE,ColumnSTATUS,SYMBOL,ColumnTERMINATED,DECIMALS) values(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS)"
                            c.execute(sql,(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS))
                            conn.commit()
                            conn.close()
                        except Exception as e:
                            return()
                    
                
                

        return redirect("view")
    

     

@app.route('/view')
# defines view  function which renders the about page 
def view():  
    """Renders the about page."""

    try:
        c, conn =function.connection()
       
        sql = "select * from recordtbl order by ID desc limit 20"
        c.execute(sql)
        rows = c.fetchall()
       
    except Exception as e:
        return(str(e))

    conn.commit()
    conn.close()
    return render_template(
        'view.html',
        title='Inserted Data View',
        year=datetime.now().year,
        message='Your application description page.',result=rows, content_type='application/json'
    )

@app.route('/insert')
# defines insert function which renders the insert page 
def insert():  
    """Renders the insert page."""
    return render_template(
        'insert.html',
        title='Insert',
        year=datetime.now().year,
        message='Insert Food Data Here.'
    )

@app.route('/insertdata',methods = ['POST'])
# defines insertFooddate which inserts fooddata into the database
def insertFooddata():
     tabYear=""
     tabCountry=""
     tabDGUID=""
     tabFood_categories=""
     tabCommodity=""
     tabUOM="";
     tabUOM_ID=""
     tabSCALAR_FACTOR=""

     tabSCALAR_FACTORID=""
     tabVECTOR=""
     tabCOORDINATE=""
     tabVALUE=""
     tabSTATUS=""
     tabSYMBOL="";
     tabTERMINATED=""
     tabDECIMALS=""


     tabYear = request.form['Year']
     tabCountry = request.form['Country']
     tabDGUID = request.form['DGUID']
     tabFood_categories = request.form['FoodCategory']


     tabCommodity = request.form['Commodity']
     tabUOM = request.form['UOM']
     tabUOM_ID = request.form['UOM_ID']
     tabSCALAR_FACTOR = request.form['SCALAR_FACTOR']

     tabSCALAR_FACTORID = request.form['SCALAR_FACTORID']
     tabVECTOR = request.form['VECTOR']
     tabCOORDINATE = request.form['COORDINATE']
     tabVALUE = request.form['VALUE']

     tabSTATUS = request.form['STATUS']
     tabSYMBOL = request.form['SYMBOL']
     tabTERMINATED = request.form['TERMINATED']
     tabDECIMALS = request.form['Decimal']
     
     try:


        c, conn =function.connection()
       
        sql = "insert into recordtbl(REF_DATE,GEO,DGUID,Food_categories,Commodity,UOM,UOM_ID,SCALAR_FACTOR,SCALAR_ID,VECTOR,COORDINATE,ColumnVALUE,ColumnSTATUS,SYMBOL,ColumnTERMINATED,DECIMALS) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        """arg=(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS)"""
        c.execute(sql,(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS))

        conn.commit()
        conn.close()
       
     except Exception as e:
        return(str(e))



     return render_template(
        'isuccess.html',
        title='Login Page',
        year=datetime.now().year,
      )

@app.route('/edit/<int:id>', methods=['GET','POST'])
# defines edit which renders the edit page
def edit(id):
    """Renders the edit page."""
    try:
        c, conn =function.connection()
        sql = "select * from recordtbl where ID=%s"
        c.execute(sql,id)
        rows = c.fetchall()
       
    except Exception as e:
        return(str(e))

    conn.commit()
    conn.close()


    return render_template(
        'Edit.html',
        title='Edit Data',
        year=datetime.now().year,
        message='Modify Data',result=rows, content_type='application/json'
    )

@app.route('/updatedata',methods = ['POST'])
# defines updateFooddata function to update the data.
def updateFooddata():
     RecID=""
     tabYear=""
     tabCountry=""
     tabDGUID=""
     tabFood_categories=""
     tabCommodity=""
     tabUOM="";
     tabUOM_ID=""
     tabSCALAR_FACTOR=""

     tabSCALAR_FACTORID=""
     tabVECTOR=""
     tabCOORDINATE=""
     tabVALUE=""
     tabSTATUS=""
     tabSYMBOL="";
     tabTERMINATED=""
     tabDECIMALS=""

     RecID = request.form['ID']
     tabYear = request.form['Year']
     tabCountry = request.form['Country']
     tabDGUID = request.form['DGUID']
     tabFood_categories = request.form['FoodCategory']


     tabCommodity = request.form['Commodity']
     tabUOM = request.form['UOM']
     tabUOM_ID = request.form['UOM_ID']
     tabSCALAR_FACTOR = request.form['SCALAR_FACTOR']

     tabSCALAR_FACTORID = request.form['SCALAR_FACTORID']
     tabVECTOR = request.form['VECTOR']
     tabCOORDINATE = request.form['COORDINATE']
     tabVALUE = request.form['VALUE']

     tabSTATUS = request.form['STATUS']
     tabSYMBOL = request.form['SYMBOL']
     tabTERMINATED = request.form['TERMINATED']
     tabDECIMALS = request.form['Decimal']
     
     try:
        c, conn =function.connection()
       
        sql = "update recordtbl set REF_DATE=%s,GEO=%s,DGUID=%s,Food_categories=%s,Commodity=%s,UOM=%s,UOM_ID=%s,SCALAR_FACTOR=%s,SCALAR_ID=%s,VECTOR=%s,COORDINATE=%s,ColumnVALUE=%s,ColumnSTATUS=%s,SYMBOL=%s,ColumnTERMINATED=%s,DECIMALS=%s where ID=%s"
        """arg=(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS)"""
        c.execute(sql,(tabYear,tabCountry,tabDGUID,tabFood_categories,tabCommodity,tabUOM,tabUOM_ID,tabSCALAR_FACTOR,tabSCALAR_FACTORID,tabVECTOR,tabCOORDINATE,tabVALUE,tabSTATUS,tabSYMBOL,tabTERMINATED,tabDECIMALS,RecID))

        conn.commit()
        conn.close()
       
     except Exception as e:
        return(str(e))



     return render_template(
        'usuccess.html',
        title='Login Page',
        year=datetime.now().year,
      )
@app.route('/del/<int:id>', methods=['GET','POST'])
# defines delete which renders the dsuccess page 
def delete(id):
    """Renders the dsuccess page."""
    try:
        c, conn =function.connection()
        sql = "delete from recordtbl where ID=%s"
        c.execute(sql,id)
        conn.commit()
        conn.close()
       
    except Exception as e:
        return(str(e))
      


    return render_template(
        'dsuccess.html',
        title='deleted Data',
        year=datetime.now().year,
        message='Delted Data'
    )

@app.route('/logout')
# defines logut function which renders the insert page 
def logout():  
    """Renders the logout page."""
    return render_template(
        'logout.html',
        title='Logout',
        year=datetime.now().year,
        message='Back to Login.'
    )