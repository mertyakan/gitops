helm upgrade --install argocd argo/argo-cd \
                                             --namespace argocd \
                                             --create-namespace \
                                             --set global.domain=argocd.mertyakan.com \
                                             --set server.ingress.enabled=true \
                                             --set server.ingress.ingressClassName=nginx \
                                             --set server.ingress.annotations."nginx\.ingress\.kubernetes\.io/force-ssl-redirect"="true" \
                                             --set server.ingress.annotations."cert-manager\.io/cluster-issuer"="letsencrypt-prod" \
                                             --set server.ingress.tls=true \
                                             --set server.ingress.tlsSecretName=argocd-tls \
                                             --set server.extraArgs="{--insecure}"
