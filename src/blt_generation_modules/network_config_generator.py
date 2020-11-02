import pymysql
import json
from xml.etree import ElementTree


class network_config_generator():

    def __init__(self):
        # Parameters stored in /opt/app-root/src/json/blt_parameters.json
        db_parameters = json.load(open('/opt/app-root/src/json/blt_parameters.json'))
        self.TEMPLATE_NETWORK_CONFIG = db_parameters['TEMPLATE_NETWORK_CONFIG']

    def test(self):
        tree = ElementTree.parse(self.TEMPLATE_NETWORK_CONFIG)
        root = tree.getroot()
        return(str(root))

    def generate(self):
        tree = ElementTree.parse(self.TEMPLATE_NETWORK_CONFIG)
        root = tree.getroot()
        xml_str = ElementTree.tostring(root,encoding='utf-8')
        return xml_str