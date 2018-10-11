import urllib.request, urllib.parse, urllib.error
import json

serviceurl = 'https://api.punkapi.com/v2/beers'

while True:
    beer_name = input('Enter a beer name: ')
    if len(beer_name) < 1: break

    url = serviceurl + "?" + urllib.parse.urlencode(
        {'beer_name': beer_name})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    

    print(json.dumps(js, indent=4))
    
    for beer in js:
       print("Beer name:", beer['name'])
       print("Tagline:", beer['tagline'])
     
