helm upgrade --install rancher rancher-latest/rancher \
                                             --namespace cattle-system \
                                             --set hostname=rancher.mertyakan.com \
                                             --set bootstrapPassword=admin
