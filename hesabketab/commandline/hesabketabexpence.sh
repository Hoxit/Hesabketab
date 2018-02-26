#!/bin/bash 
TOKEN=2000
BASE_URL=http://localhost:6006
curl --data "token=$TOKEN&amount=$1&text=$2" $BASE_URL/submit/expense/
