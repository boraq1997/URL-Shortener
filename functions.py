import filesImports as fi

def shorten(longUrl):
    shortener = fi.pyshorteners.Shortener()
    shortUrl = shortener.tinyurl.short(longUrl)
    return shortUrl