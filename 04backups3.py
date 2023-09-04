import boto3

# create s3 backet
boto3.setup_default_session(profile_name='default')
s3 = boto3.resource('s3')

# is exist bucket?
bucket_name = 'masashi-bucket-20230904'
if s3.Bucket(bucket_name).creation_date is None:
    s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': 'ap-northeast-1'})

# upload csv file to s3
s3.Bucket(bucket_name).upload_file('横浜市.csv', '横浜市.csv')
