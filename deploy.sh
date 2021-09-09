#!/usr/bin/env bash

gcloud beta functions deploy test-function --project pgsinglestory \
                                           --region us-west2 \
                                           --set-secrets 'app_store_secret=lovelife-ios-app-store-secret:latest' \
                                           --runtime python39 \
                                           --entry-point verify \
                                           --trigger-http \
                                           --allow-unauthenticated \
                                           --security-level secure-always
