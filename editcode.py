#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
e=data.getvalue('email')
g=data.getvalue('a')
m=data.getvalue('number')
ad=data.getvalue('text')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
q="update tbl_patient set name='"+n+"',fname='"+fn+"',gender='"+g+"',mobileno='"+m+"',address='"+ad+"' where email='"+e+"'"
cur=con.cursor()
a=cur.execute(q)
if a==1:
 print "<script>alert('Updated');window.location.href='pprofile.py';</script>"
else:
 print "<script>alert('Not Updated');window.location.href='pprofile.py';</script>"