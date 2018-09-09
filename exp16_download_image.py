import random ;
import urllib.request ;

def download_web_image(url):
    filenum=random.randrange(1,30);
    image_directory = "C:\\Users\\N51254\\Pictures\\Saved Pictures"
    fullpath=image_directory + "\\"+ "downloaded_web_image" + str(filenum)+'.jpg';
    urllib.request.urlretrieve(url,fullpath);

download_web_image("https://lh4.googleusercontent.com/-fMi4Bq3MbKs/WvJ85cJyDQI/AAAAAAAGQfo/hl4KM5vD7k8GQ6QptKJZRXGiwKo11rAAACLIBGAYYCw/w542-h360-k-no/")    
