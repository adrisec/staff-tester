<? PHP

if(isset($_GET["id"])){
	?>
		<!DOCTYPE html>
		<html>
			<head>
				<title>WRONG CHOICE</title>
			</head>
			<body>
				<p>You have been victim of a phishing attack made by your own company and you have clicked on a fake link</p>
				<p>You need more information about this type of attacks to don't been cheated by any real criminal</p>
				<p>If you are interested, you can read more about this attacks <a href="https://www.forcepoint.com/cyber-edu/phishing-attack">here</a></p>
			</body>
		</html>


	<? PHP

	/*Here maybe you can add some connection to a database to keep a log of users who have clicked using the id param*/
	
} else {
	print("<h1>404 ERROR - NOT FOUND</h1>");
}

?>