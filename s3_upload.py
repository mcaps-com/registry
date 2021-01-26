"""
deploy react to aws-s3


#https://s3-ap-southeast-1.amazonaws.com/app.rapidtrade.io/index.html
#http://app.rapidtrade.io.s3-website.ap-southeast-1.amazonaws.com/
curl --head http://app.rapidtrade.io/static/js/3.33e86af0.chunk.js
"""

import logging
import boto3
from botocore.exceptions import ClientError
import os
import sys
import boto3

app_bucket = "registry.mcaps.com"
region = 'ap-southeast-1'
s3_client = boto3.client('s3',region_name = region)

def upload_file(file_name, bucket, object_name):
    """
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    try:
        print("upload_file: filename, bucketname, object\n ",
              file_name, bucket, object_name)
        #response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL':'public-read', 'ContentType': 'text/html'})
        #eargs = {'ACL': 'public-read', 'ContentType': 'text/html'}
        eargs = {'ACL': 'public-read'}
        print(eargs)

        response = s3_client.upload_file(
            file_name, bucket, object_name, ExtraArgs=eargs)
        if response == None:
            print("ok")
        #s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
        else:
            print("response ", response)
    except ClientError as e:
        print("error ",e)

def upload_index(bucket):
    try:
        file_name = "./build/index.html"        
        object_name = "index.html"
        print ("upload_file: filename, bucketname, object\n ",file_name, bucket, object_name)
        eargs = {'ACL':'public-read', 'ContentType': 'text/html'}
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs=eargs)
        if response == None:
            print ("ok")
        #s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')
        else:
            print ("response ",response )
    except ClientError as e:
        print("error ",e)        


def create_bucket(bucket_name, region=None):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def list_buckets():
    response = s3.list_buckets()
    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        #print(f'  {bucket["Name"]}')
        print(f'  {bucket}')


def list_files(bucket):
    print("*** list s3 files *** \n\n")
    s3 = boto3.resource('s3')
    for key in s3_client.list_objects(Bucket=bucket)['Contents']:
        #print(key['Key'])
        print(key)
        s3_object_key = key['Key']
        o = s3.Object(bucket, s3_object_key)
        #print (o.last_modified,o.content_encoding)
        print (o.content_type)


def upload_dir(bucket, wdir):
    # enumerate local files recursively
    print("upload to bucket %s" % bucket, wdir)
    for root, dirs, files in os.walk(wdir):
        for filename in files:
            print ("upload ", filename)
            # construct the full local path
            local_path = os.path.join(root, filename)

            s3_path = os.path.relpath(local_path, wdir)

            try:
                print('=> %s' % (s3_path))
                #s3_client.head_object(Bucket=bucket, Key=s3_path)

                eargs = {'ACL': 'public-read'}
                # #figure out content type
                # if filename == "index.html":
                #     eargs['ContentType'] = 'text/html'
                # elif ".js" in filename:
                #     eargs['ContentType'] = 'application/javascript'
                # elif ".css" in filename:
                #     eargs['ContentType'] = 'text/css'            

                response = s3_client.upload_file(
                    local_path, bucket, s3_path, ExtraArgs=eargs)
                if response:
                    print("response ", response)
            except Exception as e:
                print("error %s..." % e)

def show_objects(bucket):
    objects = s3_client.list_objects(Bucket=app_bucket) #, Prefix="")
    kk = {'Objects' : []}
    print (len(objects))
    kk['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects.get('Contents', [])]]
    print (kk)

def delete_contents(bucket):
    objects_to_delete = s3_client.list_objects(Bucket=bucket) #, Prefix="")

    delete_keys = {'Objects' : []}
    delete_keys['Objects'] = [{'Key' : k} for k in [obj['Key'] for obj in objects_to_delete.get('Contents', [])]]
    print (delete_keys)
    print (len(delete_keys.keys()))
    if len(delete_keys.keys()) > 1:
        s3_client.delete_objects(Bucket=app_bucket, Delete=delete_keys)


if __name__=='__main__':
    #upload_index(rt_bucket)
    wdir = os.path.join(os.getcwd(),"tokens")    
    upload_dir(app_bucket, wdir)
    
    #list_files(app_bucket)
    #show_objects(app_bucket)

    