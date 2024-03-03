#!/bin/bash

response=$(curl -sSL -X GET "${API_URL%/}/hello/github-actions-backup-1")

          if echo "$response" | jq -e '.message' > /dev/null; then
            echo "The 'message' field exists in the JSON response."
          else
            echo "The 'message' field does not exist in the JSON response."
            exit 1
          fi