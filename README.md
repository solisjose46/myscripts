# myscripts
Collection of web scraping scripts to make life easier

# getimages.py
I am building a fully functional ecommerce site, and it is essentially a clone of the url in the script.
I wanted to collect the images found under /gallery. Script.js is responsible for fetching the images, so I just made
get request for the script and extracted any .jpg links from it.

# getlinks.py
Similar to the script above, but I just wanted a list of the urls of the images I needed.

# pngtoico.py
Used PIL library to convert png to ico.

# renderandscrape.py
My first attempt to scrape website of images. Some images are only loaded when in the viewport, so the rest of the page
needed to rendered. requests_html use of Chromium made that possible.
