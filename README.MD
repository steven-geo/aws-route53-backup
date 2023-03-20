# Daily AWS Route53 Backup to S3 Bucket

See the blog for full details: [https://blog.hardtechnology.net/2023/03/20/route53-backup.html](https://blog.hardtechnology.net/2023/03/20/route53-backup.html)


This repo is a serverless function to perform a backup of all route53 Zones into an S3 bucket on a daily basis

It is built on the AWS Serverless framework, this will need to be installed and setup prior to begining this deployment

Refer to here for OS specific setup:
[https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started.html)

---
## **DEPLOYMENT**

Clone this repo

Edit the ```./scripts/prj_var.sh``` file to customise the SAM and APP Configuration parameters. Set the appropriate SAM Artefact bucket (SAM_BUCKET_NAME), Route53 Bucket Location (APP_BUCKETNAME), prefix path to place the backups under in this bucket (APP_BUCKETPREFIX) and log retention days (as per CloudWatch requirements).

At a minimum the two bucket names must be specified.

From the root of the git repository run the ```./scripts/sam_package.sh```, then the ```./scripts/sam_deploy.sh``` script to deploy the AWS Serverless Template and create the CloudFormation stack.
