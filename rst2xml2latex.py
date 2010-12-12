# -*- coding: utf-8 -*-
#!/usr/bin/env python
from xml.dom.minidom import parse
import sys

dom = parse(sys.argv[1])
elements = dom.getElementsByTagName("section")
for element in elements:
	if element.parentNode.nodeName == "section":
		if element.parentNode.parentNode.nodeName == "section":
			print "subsubsection ",
		else:
			print "subsection ",
	else:
		print "section ",
	print element.getAttributeNode("names").nodeValue
