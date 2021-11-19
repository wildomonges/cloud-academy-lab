#!/usr/bin/env python3
import os

from aws_cdk import core as cdk
from s3lambda.s3lambda_stack import S3LambdaStack
         
app = cdk.App()
S3LambdaStack(app, "S3LambdaStack")
         
app.synth()