import boto3 as boto
import time
import webbrowser

ec2 = boto.resource('ec2')
ec2Client = boto.client('ec2')

userData = """#!/bin/bash
    sudo apt-get update
    sudo apt-get install curl
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo docker pull amanbudhrani17/covid19-tracker:latest
    sudo docker run -p 80:8085 -d amanbudhrani17/covid19-tracker"""

instances = ec2.create_instances(
    ImageId='ami-062df10d14676e201',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    SecurityGroupIds=['sg-0be20a02fc1ed1440'],
    UserData=userData
)

instance_id = instances[0].id
print("Launching new instance")

waiter = ec2Client.get_waiter('instance_running')
waiter.wait(InstanceIds=[instance_id])
print("Instance running now, instance id : %s" % instance_id)

# Fetch instance details
reservations = ec2Client.describe_instances()["Reservations"]

time.sleep(100)

for reservation in reservations:
    instance = reservation["Instances"][0]
    if instance["InstanceId"] == instance_id:
        dns = instance["PublicDnsName"]
        time.sleep(20)
        print(dns)