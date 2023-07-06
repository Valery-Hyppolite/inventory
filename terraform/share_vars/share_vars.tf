

locals {
    env = "${terraform.workspace}"

}

#OUTPUTS
output "env_suffix" {
    value = local.env
}