#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
#print "book code"
import cgi,MySQLdb
data=cgi.FieldStorage()
spec=data.getvalue('spec')
#print spec	
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select * from tbl_doctor where specialization='"+spec+"'"
#print query
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
#now make the table 
print """
<table border='1'>
<tr>
<th>Doctor Name</th>
<th>speciality</th>
<th>Timing</th>
<th>Fees</th>
<th>BOOK Now</th>
</tr>
"""

for r in res:
 print  "<tr>"
 print "<td>",r[1],"</td>"
 print "<td>",r[6],"</td>"
 print "<td>",r[10],"</td>"
 print "<td>",r[8],"</td>"
 print "<td><a href='appoint.py?did="+str(r[0])+"'>Book</a></td>"
 print "</tr>"
print """
</table>"""



