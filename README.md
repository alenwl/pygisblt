## testing web api with postman
GET to http://pygisblt-enwl-iccp-api.192.168.99.100.nip.io/api?type=
Type could be rcc,iccp or network_config
add API-Key to header and client-id

## on openshift
minishift start

once started deploy last version from github

oc start-build pygisblt -n enwl-iccp-api

# Note
Error from server (Forbidden): services is forbidden: User "developer" cannot list services in the namespace "myproject": no RBAC policy matched

this is fixed with 
oc adm policy add-cluster-role-to-user edit developer --as system:admin

# To switch project
oc project enwl-iccp-api




# deploy docker container
minishift docker-env
eval $(minishift docker-env)
docker save pygisblt:latest > pygisblt_docker.tar
docker load < ~/pygisblt/pygisblt_docker.tar
oc get svc docker-registry -n default
docker login -u $(oc whoami) -p $(oc whoami -t) 172.30.1.1:5000
docker tag pygisblt 172.30.1.1:5000/gis-blt-gen/pygisblt
docker push 172.30.1.1:5000/gis-blt-gen/pygisblt
oc new-app pygisblt --name=pygisblt
oc expose svc/pygisblt