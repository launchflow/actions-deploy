"""GitHub Action for LaunchFlow Deploy."""
import os
from subprocess import check_call

VERSION = os.getenv("INPUT_VERSION", default="")
ENVIRONMENT = os.environ["INPUT_ENVIRONMENT"]
PROJECT = os.environ["INPUT_PROJECT_ID"]
DKEY = os.environ["INPUT_DKEY"]
WORKING_DIR = os.environ["INPUT_WORKING_DIR"]
CLI_VERSION = os.getenv("INPUT_CLI_VERSION", None)

if CLI_VERSION is not None:
    cmd = f"pip install launchflow=={CLI_VERSION}"
else:
    cmd = "pip install launchflow"
check_call(cmd, shell=True)
cmd = (
    "launch deployments update-environment "
    f"--environment={ENVIRONMENT} --project-id={PROJECT} --dkey={DKEY}"
)
check_call(cmd, shell=True, cwd=WORKING_DIR)
