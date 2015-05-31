# Vertica

# Setting up an EC2 instance

Create a pre-configured Vertica 7.1.1 AMI on EC2. Once created, install Vertica 
as follows:

'''
ssh -i identity-file.pem dbadmin@ipaddress
sudo /opt/vertica/sbin/install\_vertica --dba-user-password-disabled --point-to-point --hosts localhost
'''

Once installed, logout and log back into the instance. Create a new database
called 'tpch' interactively by starting 'adminTools':

'''
/opt/vertica/bin/adminTools
'''

(Go to Configuration Menu -> Create Database and follow the steps).


