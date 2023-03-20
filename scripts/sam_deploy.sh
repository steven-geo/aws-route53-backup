#!/bin/bash
set -euxo pipefail

# shellcheck disable=SC1091
. "scripts/prj_vars.sh"

################################################################################
# SAM Deploy
################################################################################

sam deploy --template-file 'sam/packaged.yml' \
    --stack-name "$APP_STACKNAME" \
    --capabilities CAPABILITY_NAMED_IAM \
    --parameter-overrides \
      "S3BucketName"="${APP_BUCKETNAME}" \
      "S3BucketPrefix"="${APP_BUCKETPREFIX}" \
      "LogRetention"="${APP_LOGRETENTION}" \
    --debug
