#!/usr/bin/env bash
source ./manual_docker.conf
source ./util_function.sh
cd ..
build_image ${local_image} docker/Dockerfile .