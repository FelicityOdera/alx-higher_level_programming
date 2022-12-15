#!/bin/bash
#display content using curl

curl "$1" | wc -c
