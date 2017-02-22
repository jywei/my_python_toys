def get_articles(dom, date):
    soup = BeautifulSoup(dom, 'html.parser')

    articles = []  # sace post content
    divs = soup.find_all('div', 'r-ent')
    for d in divs:
        if d.find('div', 'date').string == date:  # post date is correct
            # get num of pushes
            push_count = 0
            if d.find('div', 'nrec').string:
                try:
                    push_count = int(d.find('div', 'nrec').string)  # string to int
                except ValueError:  # if fails，push_count == 0
                    pass

            # get post link and title
            if d.find('a'):  # post exists
                href = d.find('a')['href']
                title = d.find('a').string
                articles.append({
                    'title': title,
                    'href': href,
                    'push_count': push_count
                })
    return articles
