""" Backup from Route53 to S3 Bucket """
import sys
import json
from os import getenv
from datetime import datetime
import boto3
import botocore

route53 = boto3.client('route53')
s3 = boto3.client('s3')

def main(event, context):
    """ Perform Route53 backup to S3 """
    del event
    del context
    error_occured = False
    # Get Per run Environment
    s3bucketname = getenv('S3BucketName', '')
    s3bucketprefix = getenv('S3BucketPrefix', '/')
    date = datetime.today().strftime('%Y-%m-%d')
    # Attempt to list all route53 zones
    try:
        zones = route53.list_hosted_zones_by_name()
        num_zones = len(zones['HostedZones'])
        print(f"Backing up {num_zones} route53 zones.")
    except botocore.exceptions.ClientError as error:
        print(f"Unable to obtain list of Route53 zones: {error}")
        sys.exit(1)
    # Exit if no S3 Bucket specified
    if s3bucketname == '':
        print("No S3 Bucket Specified - Exiting...")
        sys.exit(2)
    # Loop through zones and dump to S3
    for zone in zones['HostedZones']:
        print(f"Processing Zone {zone['Name']}...", end='')
        try:
            zone_id = zone['Id'].split("/hostedzone/",1)[1]
            zone_name = str(zone['Name']).strip('.')
            route53_records = route53.list_resource_record_sets(HostedZoneId=zone_id, MaxItems='9999')
            route53_records_json = json.dumps(route53_records, indent=4)
            zonefilename = s3bucketprefix + zone_name + "_" + zone_id + "_" + date + ".json"
            s3.put_object(Bucket=s3bucketname, Key=zonefilename, Body=route53_records_json)
            print(f" Completed: s3://{s3bucketname}/{zonefilename}")
        except botocore.exceptions.ClientError as error:
            print("\nERROR on zone: " + zone_name + " (" + zone_id + ")")
            print(error)
            error_occured = True
        except ValueError as error:
            print("\nERROR on zone: " + zone_name + " (" + zone_id + ")")
            print(error)
            error_occured = True
    if error_occured:
        print("Exiting with an error status due to one or more errors")
        sys.exit(10)
    else:
        print("Route53 Backup Completed Successfully.")

