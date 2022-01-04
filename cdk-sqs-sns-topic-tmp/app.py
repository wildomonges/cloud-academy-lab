#!/usr/bin/env python3

from aws_cdk import core

from sample_python.sample_python_stack import SamplePythonStack


app = core.App()
SamplePythonStack(app, "sample-python")

app.synth()
