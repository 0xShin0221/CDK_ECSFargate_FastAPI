from fastapi import FastAPI

openapi_params = {
    "title": "CDK-Fargate-fastAPI",
    "openapi": "3.0.0",
    "version": "1.0",
    "docs_route": "/docs",
}
# cors ,doc
api = FastAPI()


@api.get("/")
def route():
    """Helloworld endpoint.
    ---
    get:
        description: Helloworld
        responses:
            200:
                description: Helloworld
    """
    return {"status": "ok"}
