#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
e=data.getvalue('email')
m=data.getvalue('number')
ms=data.getvalue('msg')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_contact(name,email,mobileno,message,date) values('"+n+"','"+e+"','"+m+"','"+ms+"',curdate())"
cur=con.cursor()
a=cur.execute(query)
if a==1:
	print "<script>alert('Contact Information Send Successfully');window.location.href='index.html';</script>"
else:
	print "<script>alert('Contact Information Send Not  Successfully');window.location.href='contact.py';</script>"