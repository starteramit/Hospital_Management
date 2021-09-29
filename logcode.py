#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "hello"
import cgi,MySQLdb
data=cgi.FieldStorage()
who=data.getvalue('select')
#print who
e=data.getvalue('email')
#print e
p=data.getvalue('password')
#print p
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
if who=="Doctor":
 query="select * from tbl_doctor where email='"+e+"' and password='"+p+"'"
 cur=con.cursor()
 a=cur.execute(query)
 if a==1:
  print "<script>alert('Doctor Login Successfully!!!');window.location.href='dprofile.py?id="+e+"';</script>"
 else:
  print "<script>alert('Doctor Not Login Succesfully!!');window.location.href='login.py';</script>"
if who=="Patient":
 query="select * from tbl_patient where email='"+e+"' and password='"+p+"'"
 cur=con.cursor()
 a=cur.execute(query)
 if a==1:
  print "<script>alert('Patient Login Successfully!!!');window.location.href='pprofile.py?id="+e+"';</script>"
 else:
  print "<script>alert('Patient Not Login Succesfully!!');window.location.href='login.py';</script>"
