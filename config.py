# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)
import os

if 'RDS_HOSTNAME' in os.environ:
    hostname = os.environ['RDS_HOSTNAME']
    db_name = os.environ['RDS_DB_NAME']
    port = os.environ['RDS_PORT']
    username = os.environ['RDS_USERNAME']
    password = os.environ['RDS_PASSWORD']
else:
    hostname = 'flaskdemodb.cbipfyg2jf5b.rds.cn-northwest-1.amazonaws.com.cn'
    db_name = 'flaskdemo'
    port = '3306'
    username = 'flask'
    password = 'Test12345'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + username + ':' + password + '@' + hostname + ':' + port + '/' + db_name
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:Test12345@flaskdemodb.cbipfyg2jf5b.rds.cn-northwest-1.amazonaws.com.cn:3306/flaskdemo'

# Uncomment the line below if you want to work with a local DB
#SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True
SECRET_KEY = 'dsaf0897sfdg45sfdgfdsaqzdf98sdf0a'
