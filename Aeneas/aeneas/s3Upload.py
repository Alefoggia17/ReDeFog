#!/usr/bin/env python3
from curses import echo
import boto3 # AWS utility
import sys # System utility to accept command line arguements

#########################################################################################################################
# CSC4006 - Research And Development Project
# Developed by: Jonathan McChesney (MEng Computer Games Development)
# Queen's University Belfast
#
# Component: s3Upload.py
#
# Purpose: This component uploads an asset to an S3 bucket.
#
#########################################################################################################################

# Create an S3 client
s3 = boto3.client('s3')

# set input parameters
filename = sys.argv[1] # input filename
output = sys.argv[2] # output filename
bucket_name = 'csc4006benchbucketale' # S3 bucket name

# Uploads the given file using a managed uploader, which will split up large
# files automatically and upload parts in parallel.
import sys
print("Versione di python:", sys.version)
s3.upload_file(filename, bucket_name, output)
