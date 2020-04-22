import xmlschema
from pprint import pprint

FRAB_Schema = xmlschema.XMLSchema('xml/schedule.xsd')

pprint(FRAB_Schema.to_dict('xml/schedule.xml'))





