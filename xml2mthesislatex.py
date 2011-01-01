#!/usr/bin/python -S
# -*- coding: utf-8 -*-
from xml.dom.minidom import parse
import sys

def parse_paragraph(e):
	for element in e.childNodes:
		if element.nodeName == "citation_reference":
			print "[%s]"%(element.getAttribute('refid')),
		elif element.nodeName == "footnote_reference":
			print "\\footnote{%s}"%(element.getAttribute("ids")),
		elif element.nodeName == "#text":
			print element.data,
	print "\n"

def parse_bullet_list(e):
	print u"\\begin{itemize}"
	for item in e.childNodes:
		print u"\\item ",
		parse_paragraph(item.firstChild)
	print u"\\end{itemize}"

def parse_figure(e):
	if e.firstChild.nodeName == 'image':
		print """
\\begin{figure}[!ht]
\\centering 
\\includegraphics[scale=.%s]{%s}
\\caption{%s}
\\end{figure}
"""%(e.firstChild.getAttribute('scale'), e.firstChild.getAttribute("uri"), e.childNodes[1].firstChild.data)

def parse_in_section(e):
	for element in e.childNodes:
		if element.nodeName == "paragraph":
			parse_paragraph(element)
		elif element.nodeName == "bullet_list":
			parse_bullet_list(element)
		elif element.nodeName == "figure":
			parse_figure(element)

def parse_section(dom):
	elements = dom.getElementsByTagName("section")
	for element in elements:
		if element.parentNode.nodeName == "section":
			if element.parentNode.parentNode.nodeName == "section":
				s = u"\\subsubsection{"
			else:
				s = u"\\subsection{"
		else:
			s = u"\\section{"
		s += element.firstChild.firstChild.data + u"}"
		print s
		parse_in_section(element)

def parse_citation(dom):
	print "\\begin{thebibliography}{99}"
	elements = dom.getElementsByTagName("citation")
	for e in elements:
		print "\\bibitem{%s} %s"%(e.childNodes[0].firstChild.data,e.childNodes[1].firstChild.data)
	print "\\end{thebibliography}"
sys.setdefaultencoding('UTF-8')
dom = parse(sys.argv[1])
f = file("header.tex", "r")
print f.read()
f.close()
parse_section(dom)
parse_citation(dom)
f = file("footer.tex", "r")
print f.read()
f.close()
