# Usage of the application

```
docker compose up -d
cd Terraform
terraform apply -auto-approve
aws --endpoint-url=http://localhost:4566 lambda invoke --function-name test_lambda --payload $(echo -n '{"test": "event"}' | base64) response.json
```