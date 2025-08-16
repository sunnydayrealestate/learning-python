#!/bin/bash
# Add the files to be published
git add .
echo "Enter commit message:"
read commitmsg
git commit -m "$commitmsg"
git push origin main
