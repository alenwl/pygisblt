import pymysql
import json
import os
from xml.etree import ElementTree


class network_config_generator():

    def __init__(self):
        # Config map defines these parameters as env
        self.TEMPLATE_NETWORK_CONFIG = os.environ.get('TEMPLATE_NETWORK_CONFIG')

    def test(self):
        tree = ElementTree.parse(self.TEMPLATE_NETWORK_CONFIG)
        root = tree.getroot()
        return(str(root))

    def generate(self):
        tree = ElementTree.parse(self.TEMPLATE_NETWORK_CONFIG)
        root = tree.getroot()
        xml_str = ElementTree.tostring(root,encoding='utf-8')
        return xml_str