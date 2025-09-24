# Start the local HTTP server and open the web UI in the default browser
py -3 -m http.server 8000 --bind 127.0.0.1 | Out-Null &
Start-Sleep -Seconds 1
Start-Process "http://127.0.0.1:8000/web/"
