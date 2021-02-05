from xml.sax import ContentHandler, make_parser

class MyHandler(ContentHandler):
	def __init__(self):
		"initialization"
		pass

	def startDocument(self):
	"Called when the parser is on the first element"
		pass

	def startElement(self, name, attrs):
	"Called when the parser encouters a tag opening"
		pass

	def endElement(self, name):
	"Called when the parser encouters a tag closing"
		pass

	def characters(self, chrs, offset, length):
	"Called when the parser encouters data in an element"
		pass

	def endDocument(self):
	"Called when the parser encouters the very last element"
		pass

doc = MyHandler()
saxparser = make_parser()
saxparser.setContentHandler(doc)

def load(filename):
	datasource = open(filename, "r")
	saxparser.parse(datasource)

def dump(root, filename):
	pass

import unittest

class TestParser(unittest.TestCase):
	def testLoading(self):
		load("data/test.xmi")

if __name__ == '__main__':
	unittest.main()
