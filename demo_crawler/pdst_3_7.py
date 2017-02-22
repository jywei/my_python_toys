page = get_web_page('https://www.ptt.cc/bbs/Beauty/index.html')
if page:
    date = time.strftime("%m/%d").lstrip('0')
    current_articles = get_articles(page, date)
    for post in current_articles:
        print(post)
