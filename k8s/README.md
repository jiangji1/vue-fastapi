# k8s 部署（模板）

这些清单是**可运行的参考模板**，你需要按你的镜像仓库、域名与密钥进行替换。

## 结构

- `namespace.yaml`: 命名空间
- `api-*.yaml`: 后端（FastAPI）配置、密钥、部署、服务、Ingress
- `frontend-*.yaml`: 前端（Vue 静态站点）部署、服务、Ingress
- `mysql-*.yaml`: **可选** MySQL（StatefulSet + PVC）。生产更建议用托管 MySQL

## 快速使用（kubectl）

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/
```

## 你必须改的地方

- **镜像**：
  - `api-deployment.yaml` 里的 `image: your-registry/f1-api:latest`
  - `frontend-deployment.yaml` 里的 `image: your-registry/f1-frontend:latest`
- **JWT 密钥**：`api-secret.yaml` 里的 `JWT_SECRET`
- **域名**：
  - `api-ingress.yaml` 的 `host: api.example.com`
  - `frontend-ingress.yaml` 的 `host: admin.example.com`

## Ingress 控制器说明

这些 Ingress 使用 `nginx` 风格注解；如果你用的是 Traefik / APISIX / ALB，请按你集群的 IngressController 调整。

