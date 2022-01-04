from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)


class SamplePythonStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "SamplePythonQueue",
            visibility_timeout=core.Duration.seconds(300),
            retention_period=core.Duration.days(1)
        )

        topic = sns.Topic(
            self, "SamplePythonTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
