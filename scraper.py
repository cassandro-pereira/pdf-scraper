from pdfquery import PDFQuery
import os
import pdfkit

#Use a HTML data to convert later into a pdf file
f = open('test.html', 'w')

html = """
<html>
   <head>
      <title>Hello world!</title>
      <link rel='stylesheet' href='assets/style.css'>
   </head>
   <body>
      <h1>Hello from File!</h1>
      <a href='https://ironpdf.com/python/'><img src='assets/logo.png' /></a>
   </body>
</html>
"""
f.write(html)
f.close

pdfkit.from_file('test.html', 'test.pdf')
pdfkit.from_url('http://google.com', 'example.pdf')

pdf = PDFQuery('example.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)