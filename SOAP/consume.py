from zeep import Client
#

client=Client('https://www.dataaccess.com/webservicesserver/NumberConversion.wso?WSDL')

result= client.service.NumberToWords(5)

print(result)
#ni soap_server.py
#pip install pysimplesoap
#from http.server import HTTPServer
#from pysimplesoap.server import SoapDispatcher, SOAPHanler