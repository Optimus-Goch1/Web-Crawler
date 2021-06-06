def get_page(page):
    import urllib.request
    with urllib.request.urlopen(page) as response:
        return response.read()


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index= {}
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)

words=get_page('https://xkcd.com/').split()
print(words)
print(len(words))