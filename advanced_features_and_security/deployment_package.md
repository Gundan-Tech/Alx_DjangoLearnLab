# Deployment Configuration for HTTPS

To support the Django HTTPS settings, the production web server (Nginx) must be configured with an SSL certificate (e.g., via Let's Encrypt).

### Nginx Configuration Snippet:

server {
listen 80;
server_name yourdomain.com;
return 301 https://$host$request_uri; # Redirect HTTP to HTTPS
}

server {
listen 443 ssl;
server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme; # Crucial for Django's SECURE_SSL_REDIRECT
    }

}
