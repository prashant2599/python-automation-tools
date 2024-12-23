#!/bin/bash

echo | openssl s_client -servername google.com -connect google.com:443 2>/dev/null | openssl x509 -noout -dates