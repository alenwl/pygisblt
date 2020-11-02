import pymysql
import threading
import json
import xml.etree.ElementTree as ET


class iccp_config_generator():

    def __init__(self):
        pass

    def test(self):
        return "All ok with this module"
        tree = ET.parse('/opt/app-root/src/xml/ICCP_config_emppty.xml')
        root = tree.getroot()
        return root.tag