from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Title</title>
  <style>
  .large {
    color: blue;
    text-align: center;
  }
  </style>
  </head>
  <body>
    <h1 class="large">I will change colored and be centralized</h1>
    <p id="p1">paragraph one</p>
    <p id="p2" style="">paragraph two</p>
  <div><a href='http://blog.castman.net' style="font-size:200%;">I am a enlarged hyperlink</a></div>
  </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
print(soup)
# <html>
# <head>
# <title>Title</title>
# <style>
# .large {
#   color:blue;
#   text-align: center;
# }
# </style>
# </head>
# <body>
# <h1 class="large" style="">I will change colored and be centralized</h1>
# <p id="p1">paragraph one/p>
# <p id="p2" style="">paragraph two</p>
# <div><a href="http://blog.castman.net" style="font-size:200%;">I am a enlarged hyperlink</a></div>
# </body>
# </html>

soup.find('p')            # get the first <p> </p> block
# <p id="p1">paragraph one</p>

soup.find('p', id='p2')   # get the first <p> </p> block and id="p2"
# <p id="p2" style="">paragraph two</p>

soup.find(id='p2')        # get the first id="p2" block
# <p id="p2" style="">paragraph two</p>

soup.find_all('p')        # get all <p> </p> blocks
# [<p id="p1">paragraph one</p>, <p id="p2" style="">paragraph two</p>]

soup.find('h1', 'large')  # get the first <h1> block, and class="large"
# <h1 class="large" style="">I will change colored and be centralized</h1>

paragraphs = soup.find_all('p')
for p in paragraphs:
    print(p['id'], p.text)
# p1 paragraph one
# p2 paragraph two

a = soup.find('a')
print(a['href'], a['style'], a.text)
# http://blog.castman.net font-size:200%; I am a enlarged hyperlink

print(soup.find('h1')['class'])  # class can have many values, so return a list
# ['large']

print(soup.find(id='p1').get('style'))  # None
