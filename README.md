Project 1:
Install Python Flask application on VM
Step 1: Create CloudSQL, Connect to it

Step 2: Create Table by using the below sql:
   CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    email VARCHAR(100)
);

Step 3: Create a GCE VM and install python , python dependencies to run the app which are flask and pymysql 

Step 4: Create Image of the VM 

Step 5: Create VM Template and Create Managed Instance Group 
Use the below statup script to run the app in Template
#! /bin/bash
sudo python3 /home/nagababugcp/flask-app/app.py
EOF

Step 6: Create Load Balancer and take the public Ip and hit from the browser. 

Project 2:
Install Python Flask application on GKE
Step 1 & 2 are same as above 

Step 3: Create GKE cluster 

Step 4: Create docker image by using the Dockerfile 
docker build -t flask-app . 

Step 5: Create artificat registry and create a repo 
Go to setup instructions and execute the configure-docker command and authenticate with the artifact registry. 
Example: gcloud auth configure-dockerus-central1-docker.pkg.dev

Step 6: Tag the image created with the artificat registry
Example: docker tag nginx us-central1-docker.pkg.dev/demo1-424506/demo-reg/nginx-image
demo1-424506 -- Project Id 
demo-reg  -- Repo name 
nginx-image -- Image name

Step 7: Push the docker image to the artificat registry
docker push nginx us-central1-docker.pkg.dev/demo1-424506/demo-reg/nginx-image

Step 8: Install kubectl 
sudo apt-get install kubectl

Step 9: Install GKE plugin 
sudo apt-get install google-cloud-cli-gke-gcloud-auth-plugin

Step 10: Connect to GKE cluster 
gcloud container clusters get-credentials Cluster-Name --region=us-central1

Step 11:
Create the deployment and service as given in the k8 directorty 
