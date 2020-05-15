# ECS fargate stacks by CDK with fastAPI

[![MIT License](https://badgen.now.sh/badge/License/MIT/blue)](https://github.com/sintaro/CDK_ECSFargate_FastAPI/blob/master/LICENSE.md)
[![sintaro](https://badgen.now.sh/badge/by/sintaro/purple)](https://github.com/sintaro)


## Requirements


## Architecture

- **Python**,
- Basic **Python** pipenv  `./Pipfile`
- Backend with FastAPI `./backend`
- **Docker** using `./docker/api/Dockerfile` and docker-coompose in `./docker/docker-compose`
- **Infrastructure as Code** using [AWS Cloud Development Kit][cdk] in `./stacks`
- Pipenv scripts 

``` text:Pipfile
start
docker_build
docker_run
docker_compose_up

# ECR deploy image scripts
tagged_image
push_to_ecr
deploy_image_ecr
deploy_ecr_stack
deploy_ecs_stack

# CDK scripts
cdk
cdk_ls
cdk_diff
cdk_doctor
```

## Usage

Specified these to environment like .env file

`$ touch > .env`

```sh title=.envに記載
REPOSITORY_IMAGE=XXXXX-ecr-image
ECR_STACK_NAME=xxxxxxxxxxx
ECS_STACK_NAME=xxxxxxxxxxx
PORT=XXXX
ACCOUNT=XXXXXX
AWS_REGION=XXXXXX
AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXXXXX
AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXXXXXX
ROLE_ARN=arn:aws:iam::XXXXXXXXXXXXXXXXXXX:role/ecsTaskExecutionRole
ECR_REGISOTRY=XXXXXXXXXX.dkr.ecr.XXXXXXXXXXXXXXXX.amazonaws.com/XXXXXXXXXXXXXXXX:latest
```