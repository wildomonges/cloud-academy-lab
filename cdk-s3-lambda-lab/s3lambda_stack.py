
from aws_cdk import(
    core as cdk,
    aws_iam as _iam,
    aws_lambda as _lambda,
    aws_s3 as _s3
)
         
class S3LambdaStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        # The code that defines your stack goes here
        # Use an existing IAM Role
        lambda_role = _iam.Role.from_role_arn(
            self,
            "role",
            "arn:aws:iam::415903314720:role/LambdaBasicRole",
            mutable=False
        )

        # create s3 bucket
        bucket = _s3.Bucket(
            self,
            "s3_bucket",
            access_control=_s3.BucketAccessControl.PUBLIC_READ_WRITE,
            public_read_access=True
        )

        # create lambda function
        function = _lambda.Function(
            self,
            "lambda_function",
            runtime=_lambda.Runtime.PYTHON_3_7,
            handler="lambda-handler.main",
            code=_lambda.Code.asset("./lambda"),
            role=lambda_role,
            environment={
                'bucket_name': bucket.bucket_name
            }
        )
