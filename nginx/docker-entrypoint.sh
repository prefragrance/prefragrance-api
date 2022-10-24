chmod +x /wait-for-it.sh
/wait-for-it.sh webapp:8000 --timeout=0 -- nginx -g 'daemon off;'

sudo usermod -a -G docker $USER[sudo]
