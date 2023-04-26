server {
    listen 80;
    server_name elasticsearch.localhost;

    location / {
        proxy_pass http://elasticsearch:9200;
    }
}

server {
    listen 80;
    server_name elasticvue.localhost;

    location / {
        proxy_pass http://elasticvue:8080;
    }
}

server {
    listen 80;
    server_name flask.localhost;

    location / {
        proxy_pass http://flask:5000;
    }
}
