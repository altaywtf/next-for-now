#Server Configuration
This document contains detailed information about the server configuration of Next For Now.

We are planning to use LEMP (Linux - nginx - MySQL - Python) stack on Next For Now.

---

##Operating System
ubuntu 14.04

---

##Web Server
####nginx Configuration

<pre>
server {
	listen 80;
	server_name nextfornow.com;
}

location / {
	proxy_pass http://127.0.0.1:8000;
	proxy_set_header Host $host;
	proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
}

location /static/ {
	autoindex on;
	alias /home/altay/nextfornow/src/static/;
}

location /media/ {
	autoindex on;
	alias /home/altay/
}

# Cache Assets

location ~* /.(?:jpg|jpeg|gif|png|ico|cur|gz|svg|svgz|mp4|ogg|ogv|webm|htc)$ {
	expires 1M;
	access_log off;
	add_header Cache-Control "public";
}

# Cache CSS and Javascript

location ~*/.(?:css|js)$ {
	expires 1M;
	access_log off;
	add_header Cache_Control "public";
}

</pre>

---

##Database Server
MySQL

---

##Web Application
Django web framework, written with Python.

---