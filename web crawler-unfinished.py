def union(a,b):
    os=get_next_target(page)
    if url:
        links.append(url)
        page=page[endpos:]
    else:
        break
    return links


def add_to_index(index,keyword,url):
    for entry in index:
        if entry[0] == keyword and not url in entry[1]:
            entry[1].append(url)
    return index.append([keyword,[url]])


def lookup(index,keyword):
    for entry in index:
        if entry[0]==keyword:
            return entry[1]
    return[]

def add_page_to_index(index,url,content):
    words=content.split()
    for word in words:
        add_to_index(index,word,url)


def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl:
        page = tocrawl.pop()
        if page not in crawled:
            content=get_all_links(page)
            add_page_to_index
            add_page_to_index(index,page,content)
    return index

def make_big_index(size):
    index=[]
    letters=['a','a','a','a','a']
        while len(index)< size:
        word=make_string(letters)






