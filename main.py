import xmlschema
from pprint import pprint

FRAB_Schema = xmlschema.XMLSchema('xsd/schedule.xsd')

pprint(FRAB_Schema.to_dict('xml/schedule.xml'))





