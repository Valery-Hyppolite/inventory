
module "share_vars" {
    source = "../share_vars"

  
}
#CREATE A  VPC
resource "aws_vpc" "project_vpc" {
  cidr_block       = "10.0.0.0/16"
  enable_dns_hostnames = true
  tags = {
    Name = "main_project_vpc${module.share_vars.env_suffix}"
  }
}

# CREATE TWO PUBLIC SUBNETS FOR THE VPC
# WHEN CREATING A SUBNET, A ROUTE TABLE BY DEFAULT IS CREATED AND THE ASSOCIATED SUBNETS ARE ADDED TO IT. 
# NO NEED TO CREATE A ROUTE TABLE UNLESS ONE WANTS TO DO THAT FOR SPECIFIC REASONS.
resource "aws_subnet" "public_project_subnet1" {
  vpc_id                    = aws_vpc.project_vpc.id
  cidr_block                = "10.0.1.0/24"
  map_public_ip_on_launch   = true
  availability_zone         = "us-east-1a"  
  tags = {
    Name                    = "public_subnet-1${module.share_vars.env_suffix}"
  }
}

resource "aws_subnet" "public_project_subnet2" {
  vpc_id                    = aws_vpc.project_vpc.id
  cidr_block                = "10.0.2.0/24"
  availability_zone         = "us-east-1b"  
  map_public_ip_on_launch   = true
  tags = {
    Name                = "public_subnet-2${module.share_vars.env_suffix}"
  }
}

#CREATE AN INTERNET GATEWAY
#WHEN CREATING AN INTERNET GATEWAY, IF VPC ID IS PROVIDED, THE INTERNET GATEWAY WILL BE ATTTACHED TO THE VPC DURING CREATION.
#NO ADDTIONAL ATTACHEMENT CONFIGURATION IS NEEDED.
resource "aws_internet_gateway" "project_gw" {
  vpc_id = aws_vpc.project_vpc.id

  tags = {
    Name = "project_gw${module.share_vars.env_suffix}"
  }
}

#GET THE MAIN ROUTE TABLE ASSOCIATED WITH THE VPC
# DATA IS USE TO GET ATTRIBUTES FROM A RESOURCE ALREADY CREATED ON AWS
data "aws_vpc" "selected" {
  id = aws_vpc.project_vpc.id
}

# CREATE ROUTE TO ROUTE-TABLE
# ADD GW TO ROUTE TABLE TO ALLOW TRAFFIC TO THE INTERNET
resource "aws_route" "route" {
  route_table_id            = data.aws_vpc.selected.main_route_table_id
  destination_cidr_block    = "0.0.0.0/0"
  gateway_id                = aws_internet_gateway.project_gw.id
}

#OUTPUT THE PUBLIC SUBNETS FOR THE CREATION OF THE EC2 INSTANCE
output "public_subnet1_output" {
   value = aws_subnet.public_project_subnet1.id
}

output "vpc_id_output" {
  value = aws_vpc.project_vpc.id
}

#IF YOU WANT TO OUTPUT TWO SUBNETS
# output "public_subnets_output" {
#    value = [aws_subnet.public_project_subnet1, aws_subnet.public_project_subnet2]
# }
