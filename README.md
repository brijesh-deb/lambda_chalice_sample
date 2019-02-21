# lambda_chalice_sample
#### Install Chalice
- pip install chalice
- chalice --version
#### Create Chalice project
- Go to folder where project is to be created
- *chalice new-project*
- Enter name of project
- New project directory is created
#### Local test
- Go to project directory
- *chalice local*
- *curl -x GET http://localhost:8000 *
#### Deploy on AWS Lambda
- Set AWS credential in ~/.aws/config
```
  [default]
		output = json
		aws_access_key_id=<your-access-key-id>
		aws_secret_access_key=<your-secretaccess-key-id>
		region = us-east-1
 ```
- Go to project folder
  - *Chalice deploy*
	- Once deployed, Lambda ARN and Rest API URL will be displayed
	- *curl -x GET <Rest API URL>*
	- Check deployment
		○ Go to AWS Console > Lambda > Functions > New lambda function should be listed

