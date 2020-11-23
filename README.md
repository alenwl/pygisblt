## testing web api with postman
GET to http://pygisblt-gis-blt-gen.192.168.99.100.nip.io/api?type=
Type could be rcc,iccp or network_config
add API-Key to header

## on openshift
minishift start

once started deploy last version from github

oc start-build pygisblt -n gis-blt-gen

# Note
Error from server (Forbidden): services is forbidden: User "developer" cannot list services in the namespace "myproject": no RBAC policy matched

this is fixed with 
oc adm policy add-cluster-role-to-user edit developer --as system:admin

# To switch project
oc project gis-blt-gen