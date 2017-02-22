from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Titile</title>
  <style>
  .large {
    color: blue;
    text-align: center;
  }
  </style>
  </head>
  <body>
    <h1 class="large">Colored and Centered Title</h1>
    <p id="p1">Paragraph One</p>
    <p id="p2" style="">Paragraph Two</p>
    <div>
      <a href='http://blog.castman.net' style="font-size:200%;">Enhanced hyperlink</a>
    </div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)

soup.find('p')            # Return the first <p> </p> block
# <p id="p1">Paragraph One</p>

soup.find('p', id='p2')   # Return the first <p> </p> block and id="p2"
# <p id="p2" style="">Paragraph Two</p>

soup.find(id='p2')        # Return the first id="p2" block
# <p id="p2" style="">Paragraph Two</p>

soup.find_all('p')        # Return all <p> </p> block
# [<p id="p1">Paragraph One</p>, <p id="p2" style="">Paragraph Two</p>]

soup.find('h1', 'large')  # Find first <h1> block and class="large"
# <h1 class="large" style="">Colored and Centered Title</h1>

paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p['id'], p.text)
# p1 Paragraph One
# p2 Paragraph Two

a = soup.find('a')
print(a['href'], a['style'], a.text)
# http://blog.castman.net font-size:200%; Enhanced hyperlink

print(soup.find('h1')['class'])  # class could have nultiple values, so it will return a list of ['large']

print(soup.find(id='p1')['style'])      # error, there is no <p id="p1"> for style
print(soup.find(id='p1').get('style'))  # None
