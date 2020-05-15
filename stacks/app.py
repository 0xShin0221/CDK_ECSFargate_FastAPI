#!/usr/bin/env python3
import os

from aws_cdk import core

from cdk.ecs_stack import ECSStack
from cdk.ecr_stack import ECRStack

app = core.App()
ECRStack(app, os.environ["ECR_STACK_NAME"])
ECSStack(app, os.environ["ECS_STACK_NAME"])

app.synth()
