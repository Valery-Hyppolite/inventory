#!/bin/bash

#INSTALL YUM, GIT, AND DOCKER. THESES PACKAGES ARE NEEDED TO RUN GIT AND DOCKER
sudo yum update -y
sudo yum install git -y
sudo yum install -y docker

#ENABLE AND START DOCKER
sudo systemctl enable docker.service
sudo systemctl start docker.service

# CREATE A USER FOR DOCKER
sudo usermod -aG docker ec2-user

#INSTALL DOCKER-COMPOSE
sudo curl -SL https://github.com/docker/compose/releases/download/v2.19.0/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

#SET EXECUTABLE PERMISSION TO THE DOCKER-COMPOSE FILE
sudo chmod +x /usr/local/bin/docker-compose

#TEST DOCKER, DOCKER-COMPOSER, AND GIT TO MAKE SURE THEY ARE INSTALLED AND OUTPUT THE RESPONSE TO A FILE CALLED DOCKER-RESP.TXT
docker run hello-world > /home/ec2-user/docker-resp.txt
docker-compose --version >> /home/ec2-user/docker-resp.txt
git --version >> /home/ec2-user/docker-resp.txt