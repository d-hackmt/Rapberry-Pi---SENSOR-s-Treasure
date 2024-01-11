import json
location_req_url='http://api.ipstack.com/103.51.95.183?access_key=fcdaeccb61637a12fdf64626569efab0'
r = requests.get(location_req_url)
location_obj = json.loads(r.text)
        
lat = location_obj['latitude']
lon = location_obj['longitude']
latitude = lat
longitude = lon
print(str(latitude))
print(str(longitude))
msg ="Bridge Overloaded....Here I attached mylocation:Latitude is:"+str(latitude)+"Langitude is:"+str(longitude)
def sms_send():
    url="https://www.fast2sms.com/dev/bulk"
    params={
  
        "authorization":"fvaKUPuNimZCWE8MOpB9YjLGs4nyeg6lzRqS71JXH5QFw3cktDIm3puGNrOFLP2Bq0AzjDfsWtVCTe6x",
        "sender_id":"SMSINI",
        "message":msg,
        "language":"english",
        "route":"p",
        "numbers":"9607181257"
    }
    rs=requests.get(url,params=params)