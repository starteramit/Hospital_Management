#!C:\Python27\python.exe
print "Content-Type:text/html\n\n"
print """
<html>
<head>
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
<h1 style="text-decoration:underline;font-weight:bold;text-align:center;color:white;font-family:Gabriola;font-size:40px;">CHANGE PASSWORD</h1>
<form action="changepasscode.py" method="post">
<b style="color:white;font-family:Gabriola;font-size:20px;">Email Id</b>
<input type="email" name="email" class="form-control" required/>
<br/>
<b style="color:white;font-family:Gabriola;font-size:20px;">Enter Old Password</b>
<input type="password" class="form-control" name="opass" required/>
<br/>
<b style="color:white;font-family:Gabriola;font-size:20px;">Enter New Password</b>
<input type="password" class="form-control" name="npass" required/>
<br/>
<b style="color:white;font-family:Gabriola;font-size:20px;">Confirm Password</b>
<input type="password" class="form-control" name="cpass" required/>
<br/>
<button class="btn btn-info form-control">Change Password</button>
</form>
</div>
</div>
</div>
</div>
</body>
</html>
"""