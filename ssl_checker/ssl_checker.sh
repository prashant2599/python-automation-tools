#!/bin/bash

echo | openssl s_client -servername medflick.com -connect medflick.com:443 2>/dev/null | openssl x509 -noout -dates