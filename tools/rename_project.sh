#!/bin/bash

echo "New project name:"
read $project_name

grep --exclude-dir={.git/, tools/} -rl ../ project_name
# xargs sed -i 's/project_name/'"$$project_name"'/g'

