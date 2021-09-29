#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head> 
<title>Dr. Profile Page</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css"  type="text/css" rel="stylesheet"/>
<link href="css/bootstrap-theme.min.css" type="text/css" rel="stylesheet"/>
<link href="css/font-awesome.min.css" type="text/css" rel="stylesheet"/>
<link href="csscode/code.css" type="text/css" rel="stylesheet"/>	
<link href="csscode/style.css" type="text/css" rel="stylesheet"/>	
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</head>
<body>
<div class="container-fluid">
<div class="row"></div>
<div class="row" style="background-image:url('images/ab.jpg');height:835px;">

<div class="container-fluid">
  <div class="col-sm-3">
    <nav class="col-sm-2 d-none d-md-block bg-light sidebar"style="background-color:#ffc85d;">
      <div class="sidebar-sticky">
	  <div class="row" align="center"><img src="images/user.png" style="width:180px;height:150px;"/></div>
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="pprofile.py" style="color:black;text-align:center;font-size:25px;font-family:Javanese Text;font-weight:bold;text-decoration:underline;">
              <span data-feather="home"></span>
              PATIENT PROFILE <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="book.py" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="file"></span>
              Book Appointment
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="myappoint.py" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="shopping-cart"></span>
             My Appointment
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="users"></span>
              Update Profile
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="changepass.py" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="bar-chart-2"></span>
              Change Password
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="logout.py" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="layers"></span>
              Logout
            </a>
          </li>
        </ul>

       
        </ul>
      </div>
    </nav>
</div>
<div class="col-sm-6">
<table border="1" style="font-weight:bold;	border:1px solid white;color:white;height:200px;width:900px;font-family:Javanese Text">
"""
import cgi,MySQLdb
data=cgi.FieldStorage()
em=data.getvalue('id')
#print em
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
cur=con.cursor()
q="select * from tbl_patient where email='"+em+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print "<tr><td>Name</td><td>",r[1],"</td></tr>"
 print "<tr><td>Father Name</td><td>",r[2],"</td></tr>"
 print "<tr><td>Email</td><td>",r[3],"</td></tr>"
 print "<tr><td>Gender</td><td>",r[5],"</td></tr>"
 print "<tr><td>Mobile No</td><td>",r[6],"</td></tr>"
 print "<tr><td>Address</td><td>",r[7],"</td></tr>"
 print "<tr><td>Date</td><td>",r[8],"</td></tr>"
 print "<tr><td colspan='2' align='center'><a href='edit.py?id="+em+"'>Edit Profile</a></td></tr>"
print """
</table>
</div>	
</div>
</div>
</div>
</body>
</html>
"""