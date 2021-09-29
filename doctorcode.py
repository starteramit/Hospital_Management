#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
n=data.getvalue('name')
fn=data.getvalue('fname')
e=data.getvalue('email')
p=data.getvalue('password')
g=data.getvalue('a')
s=data.getvalue('special')
exp=data.getvalue('experience')
f=data.getvalue('fee')
ad=data.getvalue('address')
a=data.getvalue('at')
sum=data.getvalue('sum')
#print sum
tot=data.getvalue('t')
#print tot
#print a
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="insert into tbl_doctor(name,fname,email,password,gender,specialization,experience,fees,address,timing,date) values('"+n+"','"+fn+"','"+e+"','"+p+"','"+g+"','"+s+"','"+exp+"','"+f+"','"+ad+"','"+a+"',curdate())"
cur=con.cursor()
if sum==tot:
 a=cur.execute(query)
 if a==1:
  print "<script>alert('Doctors Registered Successfully');window.location.href='login.py';</script>"
 else:
  print "<script>alert('Doctors  Not Registered Successfully');window.location.href='doctor.py';</script>"
else:
 print "<script>alert('Invalid Captcha???');window.location.href='doctor.py';</script>"