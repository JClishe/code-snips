# ==========PROVIDERS==========

provider "aws" {
  alias  = "us-east-1"
  region = "us-east-1"
}

provider "aws" {
  alias  = "us-west-2"
  region = "us-west-2"
}


resource "aws_sns_topic" "topic-us-east" {
  provider = aws.us-east-1
  name     = "topic-us-east"
}

resource "aws_sns_topic" "topic-us-west" {
  provider = aws.us-west-2
  name     = "topic-us-west"
}

#==========VARIABLES==========

variable "my-var" {
    description = "My Test Variable"
    type = string
    default = "Hello"
    validation { # optional validation block
      condition = length(var.my-var) > 4
        error_message = "The string must be more than 4 characters"
    }
    sensitive = false # optional; boolean
}

#  Referece a variable with var.my-var
#  Best practice is to reference variables in a seperate file called terraform.tfvars
#  Base variable types: string, number, bool
#  Complex variable types: list, set, map, object, tuple

#  String type sample:
variable "image_id" {
    type = string
    default = "Hello"
}

#  List type sample:
variable "availabilty_zone_names" {
    type = list(string)
    default = ["us-west-1a"]
}

#  List of objects:
variable "docker_ports" {
    type = list(object({
        internal = number
        external = number
        protocol = string
    }))
    default = [ {
      external = 8300
      internal = 8300
      protocol = "tcp"
    } ]
}

# Outputs
output "instance_ip" {
  description = "VM's private IP"
  value = aws_instance.my-vm.private_ip
}

#==========MODULES==========

module "my-vpc-module" {
  source = "./modules/vpc" # mandatory
  version = "0.0.5"
  region = "us-east-1" # input parameter(s) to pass into the module. Inside the module use var.region to reference this variable
}

#  Allowed parameters within module block: count, for_each, providers, depends_on
#  Module outputs can be inserted back into main code. To access module output:
#  Inside module block:
output "ip_address" {
  value = aws_instance.private_ip
}

#  Back in main code: module.my-vpc-module.ip_address # module.<name of module>.<name of output>

#==========WORKSPACES==========

#If using the default workspace spin up 5 instances. If anything else, spin up 1 instance:
resource "aws_instance" "example" {
  count = terraform.workspace == "default" ? 5 : 1
  #...other arguments
}

#append the active workspace name to a resource name:
resource "aws_s3_bucket" "bucket" {
  bucket = "myxyzbucket-${terraform.workspace}"
  acl = "private"
}
