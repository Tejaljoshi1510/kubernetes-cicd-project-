
#!/bin/bash

set -e

echo "=================================="
echo " Deploying Kubernetes applications"
echo "=================================="

echo ""
echo "1. Checking Kubernetes connection..."
kubectl cluster-info

echo ""
echo "2. Deploying stateless application (Nginx)..."
kubectl apply -f kubernetes/stateless/

echo ""
echo "3. Deploying stateful application (PostgreSQL)..."
kubectl apply -f kubernetes/stateful/

echo ""
echo "4. Waiting for Nginx deployment..."
kubectl rollout status deployment/nginx-deployment --timeout=120s

echo ""
echo "5. Waiting for PostgreSQL..."
kubectl rollout status statefulset/postgres --timeout=180s

echo ""
echo "6. Checking Pods..."
kubectl get pods

echo ""
echo "7. Checking Services..."
kubectl get services

echo ""
echo "8. Checking Persistent Volume Claims..."
kubectl get pvc

echo ""
echo "Deployment completed successfully!"
