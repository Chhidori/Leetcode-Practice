# ozell-calltools-integrations
### Calltools Integration with Salesforce enables us to create an activity on a lead in salesforce when a disposition action takes place in Calltools. And also, lead fields updated with the data recieved from the calltools.
### 

## To install in your local machine
* ### Open your Terminal.
* ### Navigate to a drive where you want to clone your repository.
* ### Create a directory.
### Run the below command after navigating to the created directory.
```
git clone git@github.com:fun-book/ozell-web-scraping-app.git
```
### After cloning, open the folder in VS code.
* ### Create a virtual Environment
## For Linux
### If pip is not in your system
```
sudo apt-get install python-pip
```
### Then install virtualenv
```
$ pip install virtualenv
```
### To Create a virtual environment,
```
$ virtualenv <your_virtualenv_name>
```
> ### After this command, a folder named <your_virtualenv_name> will be created. You can name anything to it. 

### To activate the virtual environment,
```
$ source <your_virtualenv_name>/bin/activate
```
### To Deactivate,
```
$ deactivate
```
## For Windows
### To Install virtualenv,
```
> pip install virtualenv
```
### Now in which ever directory you are, this line below will create a virtualenv there,
```
> virtualenv <your_virtualenv_name>
```
> ### After this command, a folder named <your_virtualenv_name> will be created. You can name anything to it. 

### To activate the virtual environment,
```
> <your_virtualenv_name>\Scripts\activate
```
### To deactivate,
```
$ deactivate 
```
### After activating the environment install the requirements using below command,
```
> pip install -r requirements.txt
```
## To set the Environment Variable for our own salesforce credentials,
* ### Open the terminal
* ### To get Salesforce Client_id and CLient secret, [Follow](https://docs.microfocus.com/UCMDB/11.0/cp-docs/docs/eng/doc_lib/Content/Remedyforce_CreateConnectedApps.htm)
### To set salesforce Client_Id
```
set salesforce_api_client_id=<your_client_id>
```
### To  set salesforce Client Secret
```
set salesforce_api_client_id=<your_client_secret>
```
### To set salesforce Username
```
set salesforce_api_username=<your_username>
```
### To set salesforce Password
```
set salesforce_api_password=<your_password>
```
### To set Salesforce auth_url
```
set salesforce_auth_url=<salesforce_auth_url>
```
## To run the app,
``` 
> flask run 
```
### Open the below link in Postman,
```
http://127.0.0.1:5000/call-disposition
```
### Send the below json in request body
### sample request
```
{    
    "salesforce_id": "00Q8D000003wCQDUA2",    
    "call_disposition": "1060",
    "Comments":"Testing Sellernotes fields update in Lead Object"
}
```

### To run the Flask in debug mode
### create a file named ``` .flaskenv ``` and include the lines below,
```
FLASK_APP=app
FLASK_ENV=development
FLASK_DEBUG=True
```





