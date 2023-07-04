#!/bin/bash
sudo yum update -y
sudo yum install git -y
sudo yum install -y docker
sudo systemctl enable docker.service
sudo systemctl start docker.service
sudo usermod -aG docker ec2-user
sudo curl -SL https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


docker run hello-world > /home/ec2-user/docker-resp.txt
docker-compose --version >> /home/ec2-user/docker-resp.txt
git --version >> /home/ec2-user/docker-resp.txt