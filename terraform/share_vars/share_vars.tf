locals {
    env = "${terraform.workspace}"

    MY_IP_env =  {
        default    = "75.201.89.133/32"
        staging    = "75.201.89.133/32"
        production = "75.201.89.133/32"
}
    my_ip = "${lookup(local.MY_IP_env, local.env)}"

    keypair_env =  {
        default     = "project-apps"
        staging     = "project-apps"
        production  = "project-apps"
}
    keypair = "${lookup(local.keypair_env, local.env)}"
}

#OUTPUTS
output "env_suffix" {
    value = local.env
}

output "my_ip" {
    value = local.my_ip
}

output "keypair" {
    value = local.keypair
}