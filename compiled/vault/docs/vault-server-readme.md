# Documentation for vault-server on vault

|||
| --- | ---- |
| **Component name** | vault-server |
| **Application** | Not Defined |
| **Replicas** | 1 |
| **Image** | vault:1.4.0 |

| ENV | VALUE |
| --- | -----  |
|HOSTNAME | UNMATCHED {'fieldRef': {'fieldPath': 'metadata.name'}}|
|HOST_IP | UNMATCHED {'fieldRef': {'fieldPath': 'status.hostIP'}}|
|POD_IP | UNMATCHED {'fieldRef': {'fieldPath': 'status.podIP'}}|
|SKIP_CHOWN | true|
|SKIP_SETCAP | true|
|VAULT_ADDR | http://127.0.0.1:8200|
|VAULT_API_ADDR | http://$(POD_IP):8200|
|VAULT_CLUSTER_ADDR | https://$(HOSTNAME).vault-server:8201|
|VAULT_K8S_NAMESPACE | UNMATCHED {'fieldRef': {'fieldPath': 'metadata.namespace'}}|
|VAULT_K8S_POD_NAME | UNMATCHED {'fieldRef': {'fieldPath': 'metadata.name'}}|
