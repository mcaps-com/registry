import boto3
from botocore.exceptions import ClientError

app_bucket = "registry.mcaps.com"
region = 'ap-southeast-1'
s3_client = boto3.client('s3',region_name = region)

def create_bucket(bucket_name):
    """Create an S3 bucket
    :param bucket_name: Bucket to create
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        print(e)
        return False
    return True

def list_obj(bucket):
    print ("list objects")
    for obj in bucket.objects.all():
        print(obj)
        key = obj.key
        #file_url = '%s/%s/%s' % (s3_client.meta.endpoint_url.name, bucket, key)
        bname = "https://s3.ap-southeast-1.amazonaws.com/registry.mcaps.com"
        file_url = '%s/%s' % (bname, key)
        print (file_url)
        #obj.delete()

#create_bucket(app_bucket)
#bucket = s3_client.Bucket(app_bucket)

s3 = boto3.resource('s3') 
bucket = s3.Bucket(app_bucket)
list_obj(bucket)

#response = s3_client.upload_file(local_path, bucket, s3_path, ExtraArgs=eargs)

#bucket.delete()



