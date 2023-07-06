module "share_vars" {
    source = "../share_vars"
  
}

#create a variable to take in the vpc_id as an input from the vpc module. 
variable "vpc_id" {}    

#CREATE A SECURITY GROUP, ALLOW EGRESS TO EVERYWHERE, INGRESS TO PORT 80,443 AND 22.
resource "aws_security_group" "project_sgrp" {
  name        = "project_sgrp${module.share_vars.env_suffix}"
  description = "Allow TLS inbound traffic"
  vpc_id      = var.vpc_id

  ingress {
    description      = "port 443"
    from_port        = 443
    to_port          = 443
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  ingress {
    description      = "prot 80"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  ingress {
    description      = "port 22"
    from_port        = 22
    to_port          = 22
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
  }

  tags = {
    Name = "project_sgrp${module.share_vars.env_suffix}"
  }

}

#OUTPUT THE SECURITY GROUP FOR THE CREATION OF THE EC2 INSTANCE
output "security_group_output" {
  value = aws_security_group.project_sgrp.id
}