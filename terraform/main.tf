# Define provider (AWS)
provider "aws" {
  region  = "us-east-1"
  profile = "devvalou"
}

module "vpc_module" {
    source = "./vpc_module"
}

module "security_group_module" {
    source = "./security_group_module"
    vpc_id = module.vpc_module.vpc_id_output
}

module "ec2_module" {
    source            = "./ec2_module"
    public_subnet1    = module.vpc_module.public_subnet1_output
    security_group_id = module.security_group_module.security_group_output
    key_pair          = var.key_pair
}
