#!/usr/bin/env python3

from aws_cdk import core

from cdk.ecr_stack import ECRStack
from cdk.ecs_stack import ECSStack

app = core.App()
ECRStack(app, "cdk-fargate-fast-api-ecr")
ECSStack(app,"cdk-fargate-fast-api-ecs")
app.synth()
