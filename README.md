# Sms-Checker API

This is a copy of the sms-analyzer available on https://www.yotpo.com/sms-analyzer/

Steps to run the app:
- open terminal
- install requirements by executing > `pip install -r requirements.txt`
- run the api by executing > `python main.py`
- you can use the app sending GET requests to the address http://127.0.0.1:5000/sms-checker with the right json data

This is an sms test json data example : 
````
{
    "sms" : "{SiteName}: Hi {FirstName}👋, you left {SiteName} without your purchase! Grab it now at 10% off, before items sell out: {AbandonedCheckoutUrl}. Reply STOP to opt-out"
}
````

This api is deployed and can be tested on :

http://sms-checker-api.herokuapp.com/sms-checker

