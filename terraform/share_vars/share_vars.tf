
#ACCESS VARIABLES FROM .ENV FILE
data "external" "load_env" {
  program = ["python", "-c", "import dotenv; dotenv.load_dotenv('.env')"]
}

data "external" "key_pair" {
  program = ["python", "-c", "import os; print(os.getenv(''))"]
}


locals {
    env = "${terraform.workspace}"

    keypair_env =  {
        default     = data.external.key_pair.result
        staging     = data.external.key_pair.result
        production  = data.external.key_pair.result
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