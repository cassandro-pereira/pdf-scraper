from pdfquery import PDFQuery
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

pdfkit.from_url('test.html', 'test.pdf')

pdfg = PDFQuery('test.pdf')
pdfg.load()

text_elementsg = pdfg._elements
print("Elements from pdf file - locally generated")
print(text_elementsg)

print('Enter the url create a pdf and look for text elements such as: http://ig.com.br: ', end='')
test_url = input()
pdfkit.from_url(test_url, 'example.pdf')

pdf = PDFQuery('example.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)
