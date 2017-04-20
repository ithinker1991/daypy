


fff = 'fdsf'

# print fff.__name__


def fff():
    pass



class jj(object):
    pass

print jj.__name__

print fff.func_name



def cache(func):
    saved = {}

    def wrapper(url):
        if url in saved:
            return saved[url]
        else:
            page = func(url)
            saved[url] = page
            return page
    return wrapper

@cache
def web_lookup(url):
    import urllib
    return urllib.urlopen(url).read()