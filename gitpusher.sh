#!/bin/bash
git add -A
echo "Enter commit message:"
read commitmsg
git commit -m "$commitmsg"
git push origin main
