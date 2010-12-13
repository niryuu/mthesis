#!/usr/bin/python -S
# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
import sys

def parse_paragraph(e):
	print e.firstChild.data + "\n"

def parse_bullet_list(e):
	print u"\\begin{itemize}"
	for item in e.childNodes:
		print u"\\item " + item.firstChild.firstChild.data
	print u"\\end{itemize}"

def parse_in_section(e):
	for element in e.childNodes:
		if element.tagName == "paragraph":
			parse_paragraph(element)
		elif element.tagName == "bullet_list":
			parse_bullet_list(element)

def parse_section(dom):
	elements = dom.getElementsByTagName("section")
	for element in elements:
		if element.parentNode.nodeName == "section":
			if element.parentNode.parentNode.nodeName == "section":
				s = u"\\subsection{"
			else:
				s = u"\\section{"
		else:
			s = u"\\chapter{"
		s += element.firstChild.firstChild.data + u"}"
		print s
		parse_in_section(element)

sys.setdefaultencoding('UTF-8')
dom = parse(sys.argv[1])
parse_section(dom)
