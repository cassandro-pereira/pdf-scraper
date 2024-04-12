from pdfquery import PDFQuery
import os
import pdfkit

#Use a HTML data to convert later into a pdf file
f = open('test.html', 'w')

html = """
  <html>
      <head>
        <meta name="pdfkit-page-size" content="Legal"/>
        <meta name="pdfkit-orientation" content="Landscape"/>
      </head>
      Hello World!
      </html>
"""
f.write(html)
f.close

pdfkit.from_string(html, 'out.pdf')
pdfkit.from_file('test.html', 'test.pdf')
pdfkit.from_url('http://ig.com.br', 'example.pdf')

pdf = PDFQuery('example.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)