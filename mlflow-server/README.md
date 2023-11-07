# Helm Charts for MLFlow

[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/mlflow-server)](https://artifacthub.io/packages/search?repo=mlflow-server)

## Introduction

- This Helm chart deploy mlflow-tracking-server in a Kubernetes cluster
- The source code of all Helm charts can be found on GitHub: https://github.com/mlops-for-all/helm-charts/tree/main/mlflow

## Prerequisites

- Kubernetes v1.17 ~ v1.21
- Helm v3
- **DB Instance for MLflow Backend Store**
- **Object Storage Instance for MLflow Artifacts Store**

## Quick Start

### Add Helm Repository

```
helm repo add mlops-for-all https://mlops-for-all.github.io/helm-charts
helm repo update
```

### Helm Install

```
helm install --create-namespace --namespace mlflow-system mlflow-server mlops-for-all/mlflow-server
```

You may need to set several values with `helm install` `--set option` or `--set-file option`.

You can find default configuration of values.yaml [here](https://github.com/mlops-for-all/helm-charts/blob/main/mlflow/chart/values.yaml).

## References

- https://github.com/cetic/helm-mlflow
- https://github.com/at-gmbh/docker-mlflow-server
- https://github.com/lightbend/ML-metadata-tutorial

## License

Apache license
