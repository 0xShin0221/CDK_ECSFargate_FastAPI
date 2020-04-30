from aws_cdk import (core, aws_ecr as ecr)


class ECRStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        ecr_repository = ecr.Repository(
            self,
            id='CdkFargateFastAPI',
            repository_name='cdk-fargate-fastapi'
        )