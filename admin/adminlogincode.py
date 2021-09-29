#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "hello"
import cgi,MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
#print e
pwd=data.getvalue('password')
#print p
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select * from tbl_admin where email='"+e+"'"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
p=""
for r in res:
	p=r[2]
if pwd==p:
 print "<script>alert('Admin Login Successfully!!!');window.location.href='admin.py';</script>"
else:
 print "<script>alert('Login Failed!!');window.location.href='index.html';</script>"

