import pymysql
import json
from xml.etree import ElementTree


class rcc_generator():

    def __init__(self):
        # Parameters stored in /opt/app-root/src/json/blt_parameters.json
        db_parameters = json.load(open('/opt/app-root/src/json/blt_parameters.json'))
        self.TEMPLATE_RCC = db_parameters['TEMPLATE_RCC']

    def test(self):
        tree = ElementTree.parse(self.TEMPLATE_RCC)
        root = tree.getroot()
        return(str(root))

    def generate(self):
        tree = ElementTree.parse(self.TEMPLATE_RCC)
        root = tree.getroot()
        xml_str = ElementTree.tostring(root,encoding='utf-8')
        return xml_str