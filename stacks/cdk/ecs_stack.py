import os
from dotenv import load_dotenv

from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
)

load_dotenv()

ROLE_ARN = os.environ["ROLE_ARN"]
ECR_REGISOTRY = os.environ["ECR_REGISOTRY"]


class ECSStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self, "CDKFargateVpc", max_azs=2)

        cluster = ecs.Cluster(self, "CDKFargateCluster", vpc=vpc)

        role = iam.Role.from_role_arn(self, "CDKFargateECSTaskRole", ROLE_ARN)
        image = ecs.ContainerImage.from_registry(ECR_REGISOTRY)
        task_definition = ecs.FargateTaskDefinition(
            scope=self, id="CDKFargateECSTask", execution_role=role, task_role=role
        )

        port_mapping = ecs.PortMapping(container_port=8080, host_port=8080)
        task_definition.add_container(
            id="CDKFargateContainer", image=image
        ).add_port_mappings(port_mapping)
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "CDKFargateService", cluster=cluster, task_definition=task_definition,
        )

        core.CfnOutput(
            self,
            "CDKFargateLoadBalancerDNS",
            value=fargate_service.load_balancer.load_balancer_dns_name,
        )
