#! /usr/bin/env python

import sys

from lxml import etree

def validate(xmlparser, xmlfilename):
   try:
      with open(xmlfilename, 'r') as fp:
         etree.fromstring(fp.read(), xmlparser)
      return True
   except etree.XMLSchemaError:
      return False

schema_file = '../planet/planet.xsd'

with open(schema_file, 'r') as fp:
   schema_root = etree.XML(fp.read())

schema = etree.XMLSchema(schema_root)
xmlparser = etree.XMLParser(schema=schema)

filenames = sys.argv
filenames.pop(0)

if not filenames:
   print "No files to validate"
   sys.exit(0)

for filename in filenames:
   try:
      if not validate(xmlparser, filename):
         print "%s is not valid" % filename
      else:
         print "%s is valid" % filename
   except etree.XMLSyntaxError as ex:
      print "%s is not valid" % filename
      print "Reason: %s" % str(ex)
