# generate CA certificate
openssl req -newkey rsa:2048 -nodes -keyout CA_private.pem -x509 -subj "/CN=MY_CA" -days 365 -out CA_cert.crt


openssl genrsa -out client.pem 1024
openssl req -new -key client.pem -out client.csr -subj "/CN=client"
openssl x509  -req -days 3650 -in client.csr -CA CA_cert.crt -CAkey CA_private.pem  -CAcreateserial -out client.crt

openssl genrsa -out server.pem 1024
openssl req -new -key server.pem -out server.csr -subj "/CN=server"
openssl x509  -req -days 3650 -in server.csr -CA CA_cert.crt -CAkey CA_private.pem  -CAcreateserial -out server.crt

