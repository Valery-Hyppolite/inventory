

locals {
    env = "${terraform.workspace}"

    keypair_env =  {
        default     = ""
        staging     = ""
        production  = ""
}
    keypair = "${lookup(local.keypair_env, local.env)}"
}

#OUTPUTS
output "env_suffix" {
    value = local.env
}

output "keypair" {
    value = local.keypair
}