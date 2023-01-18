import boto3


def create_ec2_instance():
    try:
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId='ami-076e3a557efe1aa9c',
            MinCount=1,
            MaxCount=1,
            InstanceType='t2.micro',
            KeyName='Machine_key'
        )
    except Exception as e:
        print(e)


create_ec2_instance()
