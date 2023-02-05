variable "aws_region" {
  default = "us-east-2"
}

variable "lambda_function_name" {
  default = "IGTIexecutaEMRaovivo"
}

variable "key_pair_name" {
  default = "ib-igti-teste"
}

variable "airflow_subnet_id" {
  default = "subnet-0a07ba75ae65acf1f"
}

variable "vpc_id" {
  default = "vpc-0ce10b7f24294a55d"
}