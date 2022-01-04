import json
import pytest

from aws_cdk import core
from sample-python.sample_python_stack import SamplePythonStack


def get_template():
    app = core.App()
    SamplePythonStack(app, "sample-python")
    return json.dumps(app.synth().get_stack("sample-python").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
