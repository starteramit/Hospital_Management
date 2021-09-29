#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
e=data.getvalue('email')
p=data.getvalue('password')
g=data.getvalue('a')
m=data.getvalue('number')
ad=data.getvalue('address')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_patient(name,fname,email,password,gender,mobileno,address,date) values('"+n+"','"+fn+"','"+e+"','"+p+"','"+g+"','"+m+"','"+ad+"',curdate())"
cur=con.cursor()
a=cur.execute(query)
if a==1:
	print "<script>alert('Patient Registered Successfully');window.location.href='login.py';</script>"
else:
	print "<script>alert('Doctors  Not Registered Successfully');window.location.href='patient.py';</script>"