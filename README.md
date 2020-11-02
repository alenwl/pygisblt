# pygisblt
testing hooks

# web api
curl -H "API-Key:ander" http://pygisblt-gis-blt-gen.192.168.99.100.nip.io/api

this will return xml with iccp,rcc or network config

# on openshift
minishift start

once started deploy last version from github

oc start-build pygisblt -n gis-blt-gen