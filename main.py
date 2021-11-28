from troposphere import Ref, Template
import troposphere.ec2 as ec2
template = Template()
instance = ec2.Instance("myinstance")
instance.ImageId = "ami-951945d0"
instance.InstanceType = "t1.micro"
template.add_resource(instance)




import yaml
file = open("template.yml", "w")
yaml.dump(template.to_dict(), file)
file.close()

print("Starting taskcat")
import os
os.system("taskcat test run")