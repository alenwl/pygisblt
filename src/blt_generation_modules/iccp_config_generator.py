import pymysql
import threading
import json
import xml.etree.ElementTree as ET


class iccp_config_generator():

    def __init__(self):
        pass

    def test(self):
        tree = ET.parse('/opt/app-root/src/xml/ICCP_config_empty.xml')
        root = tree.getroot()
        print(root.findall("."))
        return(str(tree))