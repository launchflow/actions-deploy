# LaunchFlow actions-deploy

A GitHub action for deploying deployments to an [environment](https://docs.launchflow.com/launchflow-cloud/user-guides/environments) in LaunchFlow. This action can be used to create or update a deployment running in one environment. For instance you can use this action to deploy the code in your repository to a `dev` environment. If a deployment is already running in the environment it will updated it

## Prerequisites

- Create a [LaunchFlow project](https://docs.launchflow.com/launchflow-cloud/user-guides/projects)
- Create [an environment]((https://docs.launchflow.com/launchflow-cloud/user-guides/environments)) in your LaunchFlow project

## Usage

The below is an example for deploying to a `dev` environment. This will take the code checked out in your action and deploy it to the `dev` environment. You need to provide the environment name, the deployment key for the `dev` environment, and the project ID the environment lives in. We recommend storing the project ID and deployment key as secrets in your repository.

```yaml
on:
  workflow_dispatch:

name: Release Dev
concurrency: dev
jobs:
  release-prod:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: "write"
    environment: dev
    steps:
      - uses: "actions/checkout@v3"

      - name: Set up Python 3.10
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"

      - name: Release Dev
        uses: launchflow/actions-deploy@v1
        with:
          project_id: ${{ secrets.LAUNCHFLOW_PROJECT_ID }}
          environment_name: dev
          deployment_key: ${{ secrets.LAUNCHFLOW_PROD_DEPLOYMENT_KEY }}

```

## Configuration

| Input                 | Description                                                                                                                                                         |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| project_id            | The LaunchFlow project to deploy to. Should be of the format `project_XXXXXX`                                                                                       |
| environment_name | The environment to deploy your application to (e.g. `dev`).     |
| deployment_key        | The LaunchFlow deployment key of the environment you are deploying to used for authentication. This key is initially generated when you create your environment. |
| launchflow_cli_version        | The version of the LaunchFlow CLI to use. Defaults to the latest version. |