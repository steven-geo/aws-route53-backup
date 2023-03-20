#!/bin/bash

################################################################################
# Default Variables
################################################################################
export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-us-east-1}"

# SAM CONFIGURATION - This Bucket must already exist
export SAM_BUCKET_NAME="" # sam artefact location
export SAM_BUCKET_PREFIX="app-route53-backup" # prefix (without leading/trailing '/')

# APP CONFIGURATION
export APP_STACKNAME="app-route53-backup"
export APP_BUCKETNAME=""
export APP_BUCKETPREFIX="route53"
export APP_LOGRETENTION=30
