from aws_cdk import core as cdk
from dotenv import load_dotenv

from stack.cognito_stack import CognitoStack

app = cdk.App()
project = app.node.try_get_context("project")
stage = app.node.try_get_context("stage")
load_dotenv(f".env.{stage}")

CognitoStack(app, f"{project}-{stage}-cognito")

app.synth()
