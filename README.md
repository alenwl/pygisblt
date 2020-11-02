## testing web api with postman
GET to http://pygisblt-gis-blt-gen.192.168.99.100.nip.io/api?type=
Type could be rcc,iccp or network_config
add API-Key to header

## on openshift
minishift start

once started deploy last version from github

oc start-build pygisblt -n gis-blt-gen