# Pipeline

## MinIO
```bash
helm install --create-namespace --set resources.requests.memory=512Mi --set replicas=1 --set persistence.enabled=false --set mode=standalone --set rootUser=mlops,rootPassword=mlops123 --generate-name minio/minio
```

## Mlflow
```bash
helm install postgresql-ha ./postgresql-ha -n postgresql --create-namespace
```

```bash
helm install mlflow-system ./mlflow-server -n mlflow-system --create-namespace
```

## Kubeflow pipeline 설치

```bash
export PIPELINE_VERSION=2.0.1

kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"

kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io

kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic-pns?ref=$PIPELINE_VERSION"
```

## Kubeflow pipelines port-forward

```bash
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8443:80
```