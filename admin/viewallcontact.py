#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head> 
<title>View All Contact</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href="css/bootstrap.min.css"  type="text/css" rel="stylesheet"/>
<link href="css/bootstrap-theme.min.css" type="text/css" rel="stylesheet"/>
<link href="css/font-awesome.min.css" type="text/css" rel="stylesheet"/>
<link href="../csscode/code.css" type="text/css" rel="stylesheet"/>	
<link href="../csscode/style.css" type="text/css" rel="stylesheet"/>	
<script src="js/jquery-2.1.0.min.js"></script>
<script src="js/bootstrap.min.js"></script>
</head>
<body>
<div class="container-fluid">
<div class="row"></div>
<div class="row" style="background-image:url('../images/abc.jpg');height:835px;">

<div class="container-fluid">
  <div class="col-sm-3">
    <nav class="col-sm-2 d-none d-md-block bg-light sidebar"style="background-image:url('../images/admin.jpg')">
      <div class="sidebar-sticky">
	  <div class="row" align="center"><img src="../images/user.png" style="width:180px;height:150px;"/></div>
        <ul class="nav flex-column">
          <li class="nav-item">
            <a class="nav-link active" href="admin.py" style="color:blue;text-align:center;font-size:25px;font-family:Javanese Text;font-weight:bold;text-decoration:underline;">
              <span data-feather="home"></span>
              ADMIN PANEL <span class="sr-only">(current)</span>
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="viewalldoctor.py" style="color:black;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="file"></span>
              View All Doctors
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="viewallpatient.py" style="color:black;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="shopping-cart"></span>
             View All Patients
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="viewappoint.py" style="color:black;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="users"></span>
              View All Appointments
            </a>
          </li>
          <li class="nav-item"><a class="nav-link" href="viewallcontact.py" style="color:black;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="bar-chart-2"></span>
              View All ContactUs
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="logout.py" style="color:black;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
              <span data-feather="layers"></span>
              Logout
            </a>
          </li>
        </ul>

       
        </ul>
      </div>
    </nav>
</div>
<div class="col-sm-6" >
<h1 style="text-decoration:underline;font-weight:bold;text-align:center;color:white;font-family:Gabriola;font-size:40px;">CONTACT RECORDS</h1>
<table border="1" style="font-weight:bold;	border:1px solid white;color:white;height:200px;width:900px;font-family:Javanese Text">
<tr>
<th style="text-align:center">CONTACT ID</th>
<th style="text-align:center">NAME</th>
<th style="text-align:center">EMAIL</th>
<th style="text-align:center">MOBILE NO</th>
<th style="text-align:center">MESSAGE</th>
<th style="text-align:center">DATE</th>
</tr>
"""
import MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
query="select * from tbl_contact"
cur=con.cursor()
cur.execute(query)
res=cur.fetchall()
for row in res:
	print "<tr style='text-align:center'><td>",row[0],"</td>"
	print "<td>",row[1],"</td>"
	print "<td>",row[2],"</td>"
	print "<td>",row[3],"</td>"
	print "<td>",row[4],"</td>"
	print "<td>",row[5],"</td></tr>"
print """
</table>
</div>
</div>	
</div>
</div>
</body>
</html>
"""