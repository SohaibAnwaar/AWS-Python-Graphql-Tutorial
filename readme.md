# Task
Deploy a simple application on [AWS lambda](https://aws.amazon.com/lambda/) using [APP-SYNC Dynamo DB GraphQL](https://aws.amazon.com/appsync/), [Elastic CACHE](https://aws.amazon.com/elasticache/)


### Flow
1. Make an api to save data into Appsync db
2. Get a data from Appsync db
3. Get from App-sync in parallel store it in Elastic cache
4. Make 2nd get request if present in Elastic cache get it from elastic
5. cache else make request to app-sync db
6. Deploy the api code in lambda function.



![image](attachments/task_architecture.png)

## File Structure

```.
├── DockerFile -> Docker file to make binaries for lambda function
├── app_sync.py -> Handler to process app_sync requests
├── attachments -> Git readme attachments
├── aws_config.py -> Environment variables (Secure way)
├── elastic_cache.py -> Aws Elastic cache handler
├── main.py -> Main file to interact with lambda and aws
├── readme.md 
└── requirements.txt -> All of the requirements
```

## Making AppSync 
1. Go to AWS AppSync 
2. Create api
3. Build from Scratch
![image](attachments/app_sync1.png)
4. Give your appname (MyCar)
5. Edit Schema
![image](attachments/app_sync2.png)
6. Create Resources
![image](attachments/app_sync3.png)
7. Give your schema in the box
```sql
type MyCustomType {
	id: ID!
	name: String!
	content: String!
	price: Int
	rating: Float
}
```
8. Got at the bottom of the page and create
9. Go to the queries section
![image](attachments/app_sync4.png)
10. Check your schema by query
![image](attachments/app_sync5.png)
11. If you want to set and get data through python see file [app_sync.py](app_sync.py)



## Deployment on AWS lambda

We need to deploy our code onto the lambda server. Lets see how to deploy things on aws lamba functions. 



We need docker to install get the requirements.txt packages first, becaues we cannot install our requirements.txt on lambda aws. So lets do it with the help of docker. Because for-example if you are working on windows machine and lambda server you made is of linux your windows binaries will not work on lambda linux server thats why we are using docker to make binaries. 


Steps to add python packages in AWS lambda layers
Step 1: Go to the AWS management console.

Step 2: Click on create function.
![image](attachments/Hnetcomimage1.png)

Step 3: Create a lambda function named “mylambda”

Step 4: Choose Python 3.9 and x86_64 architecture and click on create a function

![image](attachments/11.png)

Step 5: Now try importing the requests module in your lambda function. So, create an event named “myevent” by clicking the down arrow on the test button.
![image](attachments/event.png)
![image](attachments/4.png)

Step 6: Deploy the function.
![image](attachments/31.png)
![image](attachments/41.png)

To create a lambda layer we need to create a zip file containing all the dependencies for the ‘requests’ package and upload it to our layer. To create this zip file we will make use of docker.

Why docker?
Since lambda uses the Amazon Linux environment, if you are using windows and create a zip file of dependencies it might not work while you run your lambda function. After you finish setting up docker, open the command prompt and run:

Make a file name ```DockerFile```
Put the following code in ```DockerFile```

```bash
FROM amazonlinux:2.0.20191016.0
RUN yum install -y python37 && \
    yum install -y python3-pip && \
    yum install -y zip && \
    yum clean all
RUN python3.7 -m pip install --upgrade pip && \
    python3.7 -m pip install virtualenv
```


``` bash
# Build docker image with file
docker build -t lambdalayer:latest -f DockerFile .
# Run docker
docker run -it --name lambdalayer lambdalayer:latest bash
# Install nano
yum update and yum install nano
# Nano requirements.txt file paste your requirements.txt here
nano requirements.txt
# Install packages
pip install -r requirements.txt
# Make virtual environment
python3.7 -m venv virtualenv
# Activate environment
source virtualenv/bin/activate
# Install requirements
pip install -r requirements.txt -t ./python
# Zip packages binaries
zip -r python.zip ./python/
# exit docker
exit
# Copy binaries
docker cp lambdalayer:python.zip ~/Desktop/

```

Step 7: Now add layers
![image](attachments/lambda1.png)
Create layer
![image](attachments/lambda2.png)
![image](attachments/lambda3.png)

Step 8:
Go to confrigation of lambda functioon
![image](attachments/lambda5.png)

Go to function url to get a url to access lambda
![image](attachments/lambda4.png)
Now from the function url you can access your lambda function
![image](attachments/results.png)


# Get Car list 
Click here to get car lists [GET](https://c477w2xrfn5m5sdudfummhdg2q0kbalf.lambda-url.us-east-1.on.aws/)


