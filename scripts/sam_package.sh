#!/bin/bash
set -euxo pipefail

# shellcheck disable=SC1091
. "scripts/prj_vars.sh"

################################################################################
# Install Dependencies
################################################################################
mkdir -p sam/build
# only grab packages when lambda required
pip3 install --no-cache-dir -r sam/requirements.txt -t sam/build/
cp sam/route53-function/*.py sam/build/

################################################################################
# Lambda Package
################################################################################
sam package \
    --template-file 'sam/backuproute53.yml' \
    --output-template-file 'sam/packaged.yml' \
    --s3-bucket "$SAM_BUCKET_NAME" \
    --s3-prefix "$SAM_BUCKET_PREFIX"
