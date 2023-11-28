"""GitHub Action for Ruff."""
import os
import re
import sys
from subprocess import check_call

VERSION = os.getenv("INPUT_VERSION", default="")
ENVIRONMENT = os.environ["INPUT_ENVIRONMENT"]
PROJECT = os.environ["INPUT_PROJECT_ID"]
DKEY = os.environ["INPUT_DKEY"]
WORKING_DIR = os.environ["INPUT_WORKING_DIR"]

version_specifier = ""
if VERSION != "":
    if not re.match(r"v?\d\.\d{1,3}\.\d{1,3}$", VERSION):
        print("VERSION does not match expected pattern")
        sys.exit(1)
    version_specifier = f"=={VERSION}"

req = f"ruff{version_specifier}"

cmd = "pip install launchflow"
check_call(cmd, shell=True)
cmd = (
    "launch deployments update-environment "
    f"--environment={ENVIRONMENT} --project-id={PROJECT} --dkey={DKEY}"
)
check_call(cmd, shell=True, cwd=WORKING_DIR)
