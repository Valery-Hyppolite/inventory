
module "share_vars" {
    source = "../share_vars"
  
}

#CREATE TWO VARIABLES FOR TO TAKE INPUTS FROM OTHER MODULES
variable "public_subnet1" {}
variable "security_group_id" {}

#CREATE EC2 INSTANCE
resource "aws_instance" "web_inventory" {
  ami                       = "ami-0715c1897453cabd1"
  instance_type             = "t2.micro"
  subnet_id                 = var.public_subnet1
  vpc_security_group_ids    = [var.security_group_id]
  associate_public_ip_address = "true"
  key_name                  = var.key_pair
  user_data                 = file("${path.module}/user_data.sh")        

  tags = {
    Name = "web_inventory-project-test_${module.share_vars.env_suffix}"
  }
}