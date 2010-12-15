#!/bin/sh
#rst2xml --output-encoding=UTF-8 resume.rst resume.xml
#./rst2xml2latex.py resume.xml | nkf -e >resume.tex
rst2latex --output-encoding=UTF-8 --documentoption=11 --section-numbering resume.rst |nkf -e >resume.tex
platex resume
dvips resume
ps2pdf resume.ps
