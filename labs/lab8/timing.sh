#!/bin/bash



cat ../json-practice/aviation.json | jq -r '.[0:6] | .[].receiptTime'
