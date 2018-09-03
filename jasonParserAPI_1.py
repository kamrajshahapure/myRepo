import urllib.request, json, os

headers = {'Authorization': 'API Key'}

q = urllib.request.Request('http://localhost:3000/api/alerts/3') #Grafana URL
q.add_header('Authorization', 'API Key') #Grafana API Key
with urllib.request.urlopen(q) as url:
    data = json.loads(url.read().decode())
    print(data['State'])

if data['State'] == "alerting":
    print ("inside If")
    os.system('docker start cadvisor')
else:
    print ("inside else")
