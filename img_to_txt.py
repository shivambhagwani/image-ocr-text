import json
import shutil
import requests

# Provide your username and license code
LicenseCode = 'DE10F8DD-EA5C-4620-BFE2-5CBD49B7069D'
UserName =  'sbhagwani'

try:
	import requests
except ImportError:
	print("You need the requests library to be installed in order to use this sample.")
	print("Run 'pip install requests' to fix it.")

	exit()

RequestUrl = "http://www.ocrwebservice.com/restservices/processDocument?language=english&gettext=true&outputformat=txt"

FilePath = "sample.png"

with open(FilePath, 'rb') as image_file:
    image_data = image_file.read()
    
r = requests.post(RequestUrl, data=image_data, auth=(UserName, LicenseCode))

if r.status_code == 401:
    #Please provide valid username and license code
    print("Unauthorized request")
    exit()

# Decode Output response
jobj = json.loads(r.content)

ocrError = str(jobj["ErrorMessage"])

if ocrError != '':
        #Error occurs during recognition
        print ("Recognition Error: " + ocrError)
        exit()

file_response = requests.get(jobj["OutputFileUrl"], stream=True)
with open("outputDoc.txt", 'wb') as output_file:
  shutil.copyfileobj(file_response.raw, output_file)