#!/usr/bin/env bash
source ./manual_docker.conf
source ./util_function.sh
push_image ${local_image} ${remote_image}
