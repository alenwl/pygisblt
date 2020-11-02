import pymysql
import threading
import json
from xml.etree import ElementTree


class iccp_config_generator():

    def __init__(self):
        # Parameters stored in /opt/app-root/src/json/blt_parameters.json
        db_parameters = json.load(open('/opt/app-root/src/json/blt_parameters.json'))
        self.TEMPLATE_ICCP_CONFIG = db_parameters['TEMPLATE_ICCP_CONFIG']

    def test(self):
        tree = ElementTree.parse(self.TEMPLATE_ICCP_CONFIG)
        root = tree.getroot()
        return(str(root))

    def generate(self):
        tree = ElementTree.parse(self.TEMPLATE_ICCP_CONFIG)
        root = tree.getroot()
        xml_str = ElementTree.tostring(root,encoding='unicode')
        return xml_str