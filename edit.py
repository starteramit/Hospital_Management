#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head> 
<title>Patient Profile Page</title>
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
            <a class="nav-link" href="" style="color:blue;text-align:center;font-size:25px;font-family:Gabriola;font-weight:bold;text-decoration:underline;">
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
<div class="col-sm-6" >
"""
import cgi,MySQLdb
con=MySQLdb.connect("127.0.0.1","root","","sgpgi",3306)
data=cgi.FieldStorage()
em=data.getvalue('id')
cur=con.cursor()
q="select * from tbl_patient where email='"+em+"'"
cur.execute(q)
res=cur.fetchall()
for r in res:
 print"""
 <html>
 <head>
 </head>
 <body>
 <form action="editcode.py" method="post">
 <b style="color:white;font-family:Gabriola;font-size:20px;">Name</b>
 """
 print '<input type="text" name="name" class="form-control" value="'+r[1]+'"/>'
 print """
 <br/>
 <b style="color:white;font-family:Gabriola;font-size:20px;">Fname</b>
 """
 print '<input type="text" name="fname" class="form-control" value="'+r[2]+'"/>'
 print """
 <br/>
 <b style="color:white;font-family:Gabriola;font-size:20px;">Email</b>
 """
 print '<input type="email" name="email" class="form-control" value="'+r[3]+'"/>'
 print """
 <br/>
 
 <b style="color:white;font-family:Gabriola;font-size:20px;">Gender</b>
 """
 m=""
 f=""
 if r[5]=="male":
  m="checked"
 if r[5]=="female":
  f="checked"
 print '<input type="radio" name="a" value="male"'+m+'/><b style="color:white;font-family:Gabriola;font-size:20px;">Male</b>' 
 print '<input type="radio" name="a" value="female"'+f+'/><b style="color:white;font-family:Gabriola;font-size:20px;">Female</b>'
 print """
 <br/>
 <br/>
 <b style="color:white;font-family:Gabriola;font-size:20px;">Mobile No</b>
 """
 print '<input type="number" name="number"  class="form-control" value="'+r[6]+'"/>'
 print """
 <br/>
 <b style="color:white;font-family:Gabriola;font-size:20px;">Address</b>
 """
 print '<input type="text" name="text" class="form-control" value="'+r[7]+'"/>'
 print """
 <br/>
 <b style="color:white;font-family:Gabriola;font-size:20px;">Date</b>
 """
 print '<input type="date" value="'+r[8]+'" class="form-control" name="date"/>'
 print """
 <br/>
 <button class="btn btn-info form-control">Update</button>
 </form>
 </div>
 </div>
 </div>
 </div>
 </body>
 </html>
"""