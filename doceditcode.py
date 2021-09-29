#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
e=data.getvalue('email')
g=data.getvalue('a')
sp=data.getvalue('special')
ex=data.getvalue('ex')
f=data.getvalue('fee')
ad=data.getvalue('text')
t=data.getvalue('time')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
q="update tbl_doctor set name='"+n+"',fname='"+fn+"',gender='"+g+"',specialization='"+sp+"',experience='"+ex+"',fees='"+f+"',address='"+ad+"',timing='"+t+"' where email='"+e+"'"
cur=con.cursor()
a=cur.execute(q)
if a==1:
 print "<script>alert('Updated');window.location.href='dprofile.py';</script>"
else:
 print "<script>alert('Not Updated');window.location.href='dprofile.py';</script>"