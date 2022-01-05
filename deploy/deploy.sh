yum update
yum install python3-pip python3-dev git
sudo amazon-linux-extras install nginx1
cd /opt/
git clone https://github.com/jptalukdar/web-honeypot.git -- web 
cd web
chown -R ec2-user .
chmod 770 .
python3 -m venv venv
source ./venv/bin/activate
pip3 install gunicorn
pip3 install -r requirements.txt
cp build/webhen.service /etc/systemd/system/
systemctl daemon-reload
systemctl start webhen


https://github.com/jptalukdar/web-honeypot.git