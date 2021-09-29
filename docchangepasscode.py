#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
import cgi,MySQLdb
data=cgi.FieldStorage()
e=data.getvalue('email')
op=data.getvalue('oldpass')
newp=data.getvalue('newpass')
cp=data.getvalue('cpass')
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()

st="false"
query="select password from tbl_doctor where email='"+e+"'"
cur.execute(query)
res=cur.fetchall()
qe=""
for r in res:
	qe=r[0]
	st="true"
if newp==cp and op==qe and st=="true":
	q="update tbl_doctor set password='"+newp+"' where email='"+e+"'"
	n=cur.execute(q)
	if n==1:
		print "<script>alert('Password Updated');window.location.href='index.html';</script>"
	else:
		print "<script>alert('Password Not Updated');window.location.href='docchangepass.py';</script>"
else:
	print "<script>alert('New Password or Old Password or Status Is Not Correct');window.location.href='docchangepass.py';</script>"


