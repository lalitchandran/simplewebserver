from http.server import HTTPServer,BaseHTTPRequestHandler

content = """
<!doctype html>
<html>
<head>
<title> COMPETITIVE ANALYSIS OF SOFTWARE</title>
</head>
<body>
<table border ="2" cellspacing ="10" cellpadding = "6" align = "Center">
<caption> ANIMATION SOFTWARE </caption>

<tr>
<th> criteria </th>
<th> after effects </th>
<th> animate </th>
<th> blender </th>
<th> max  </th>
</tr>
<tr>
<td> revenue </td>
<td> 3 </td>
<td> 2 </td>
<td> 2 </td>
<td> 3 </td>
</tr>
<tr>
<td> market share </td>
<td> 3 </td>
<td> 2 </td>
<td> 1 </td>
<td> 1 </td>
</tr>
<tr>
<td> product quality </td>
<td> 3 </td>
<td> 2 </td>
<td> 1 </td>
<td> 2 </td>
</tr>

</table>
</body>
</html>
"""

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):

        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()
