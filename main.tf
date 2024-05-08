provider "aws" {
  region = "eu-west-3"
}

resource "aws_emr_cluster" "Spark_Cluster" {
  name          = "SparkCluster01"
  release_label = "emr-7.1.0"
  applications  = ["Hadoop", "Hive", "JupyterEnterpriseGateway", "Livy", "Spark"]
  service_role = "arn:aws:iam::031131961798:role/service-role/AmazonEMR-ServiceRole-20240505T140225"
  log_uri       = "s3://aws-logs-031131961798-eu-west-3/elasticmapreduce"

  ec2_attributes {
    instance_profile                 = "arn:aws:iam::031131961798:instance-profile/EmrEc2S3Full"
    subnet_id                        = "subnet-00508a1e4ac0faf28"
    emr_managed_master_security_group = "sg-01ceb80944ffa01d6"
    emr_managed_slave_security_group  = "sg-0852ccf141b26f385"
  }

  
  master_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 1
    name           = "Primaire"
  }

  core_instance_group {
    instance_type  = "m5.xlarge"
    instance_count = 2
    name           = "Unité principale et unité de tâches"
  }

#  task_instance_group {
#    instance_type  = "m5.xlarge"
#    instance_count = 1
#    name           = "Tâche - 1"
#  }

  scale_down_behavior = "TERMINATE_AT_TASK_COMPLETION"
  auto_termination_policy {
    idle_timeout = 3600
  }
}

output "cluster_id" {
  value = aws_emr_cluster.Spark_Cluster.id
}

output "master_public_dns" {
  value = aws_emr_cluster.Spark_Cluster.master_public_dns
}

