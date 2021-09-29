#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
id=data.getvalue('id')
pt=data.getvalue('patname')
ad=data.getvalue('date')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_appointment(docid,patname,status,appointdate,date) values('"+id+"','"+pt+"','Confirm','"+ad+"',curdate())"
cur=con.cursor()
a=cur.execute(query)
con.commit()
con.close()
if a==1:
	print "<script>alert('Appointment Data Inserted');window.location.href='pprofile.py';</script>"
else:
	print "<script>alert('Appointment Data Not Inserted');window.location.href='appoint.py';</script>"