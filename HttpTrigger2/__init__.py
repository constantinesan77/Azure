import azure.functions as func
from os import environ as env


def main(req: func.HttpRequest) -> func.HttpResponse:

    superSecretApiKey = env.get("superSecretApiKey")

    return func.HttpResponse(
            superSecretApiKey, 
            status_code=200
    )


