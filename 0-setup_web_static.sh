#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static

# Instal nginx web server if not already present
sudo apt update
sudo apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo sh -c 'echo "Hello World!" > /data/web_static/releases/test/index.html'

# Create, delete and recreate symbolic links
target_folder="/data/web_static/releases/test/"
symbolic_folder="/data/web_static/current"

#check if the link exist
if [ -L "$symbolic_folder" ]; then
	rm -f "$symbolic_folder"
fi

ln -s "$target_folder" "$symbolic_folder"

# Change onwership
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration
cat << EOF | sed -i '/server_name .*/r /dev/stdin' /etc/nginx/sites-available/default
	location /hbnb_static {
		alias /data/web_static/current/;
	}

	location /data/web_static/current/ {
		alias /data/web_static/current/;
	}
EOF

# Restart nginx
service nginx restart
