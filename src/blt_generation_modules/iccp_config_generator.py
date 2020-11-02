import pymysql
import threading
import json
import xml.etree.ElementTree as ET


class iccp_config_generator():

    def __init__(self):
        # Parameters stored in /opt/app-root/src/json/blt_parameters.json
        db_parameters = json.load(open('/opt/app-root/src/json/blt_parameters.json'))
        self.TEMPLATE_ICCP_CONFIG = db_parameters['TEMPLATE_ICCP_CONFIG']

    def test(self):
        tree = ET.parse(self.TEMPLATE_ICCP_CONFIG)
        root = tree.getroot()
        return(self.TEMPLATE_ICCP_CONFIG) 