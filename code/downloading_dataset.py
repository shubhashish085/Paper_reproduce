import requests

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/reprocessed.hungarian.data'

r = requests.get(url,allow_redirects = True)

open('/home/antu/dataset.data','wb').write(r.content)


