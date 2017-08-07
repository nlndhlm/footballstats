import urllib.request

#downloads files from football-data.co.uk
def download_data(url, ofile):
    urllib.request.urlretrieve (url, ofile)
