from aws_cdk import (
    # Duration,
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw
    aws_s3 as s3
    # aws_sqs as sqs,
)
from constructs import Construct

class LambdaAppStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        # example resource
        # queue = sqs.Queue(
        #     self, "LambdaAppQueue",
        #     visibility_timeout=Duration.seconds(300),
        # )
        hello_function = _lambda.Function(self, "WelcomeHandler",
                              runtime=_lambda.Runtime.PYTHON_3_8,
                              handler="welcome.handler",
                          #   code=_lambda.Code.from_asset(path.join(__dirname, 'lambda-api'))
                              code=_lambda.Code.from_asset('lambda-api')
                              )
        apigw.LambdaRestApi(
            self,'Endpoint',
            handler = hello_function
            )

