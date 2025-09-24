# Serve static site using a minimal web server
FROM nginx:alpine
COPY web /usr/share/nginx/html
EXPOSE 80
