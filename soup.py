import requests

url = 'http://fpp.local/uploadfile.php' + '/jqupload.php'

files = {
    'file':
        ('add3.fseq', open('add3.fseq', 'rb'))
}


data = {'myfile': open('add3.fseq', 'rb')}

data_two = {'Content-Disposition': 'form-data; name="myfile"; filename="add1.fseq"',
            'Content-Type': 'application/octet-stream'}

r = requests.post(url, data=data_two, files=data)