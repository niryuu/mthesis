#!/bin/sh
#rst2xml --output-encoding=UTF-8 resume.rst resume.xml
#./xml2mthesislatex.py resume.xml | nkf -e >resume.tex
#rst2latex --output-encoding=UTF-8 --documentoption=11 --section-numbering resume.rst |nkf -e >resume.tex
platex resume
platex resume
dvipdfmx resume
pdftotext resume.pdf
#git commit -a -m 'modified'
#git push
