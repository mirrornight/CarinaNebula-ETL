#!/usr/bin/env bash

build_image(){
    if [[ $# != 3 ]]; then
        echo "Usage : build_image image_name dockerfile context_path"
        exit 0
    fi
    image_name=$1
    dockerfile=$2
    context_path=$3
    cp -r ~/.ssh .
    docker build -t ${image_name} -f ${dockerfile} ${context_path}
    build_success=$?
    rm -rf .ssh
    if [[ ${build_success} -eq 0 ]]; then
        echo "Build ### ${image_name} ### success!"
    else
        echo "Build ### ${image_name} ### failed!"
        exit 1
    fi
}

push_image(){
    local_image=$1
    if [[ $2 ]];then
	    remote_image=$2
	    docker tag ${local_image} ${remote_image}
        docker push ${remote_image}
    else
        docker push ${local_image}
    fi
}

check_build_success(){
    if [[ $# != 1 ]]; then
        echo "Usage : check_build_success image"
        exit 0
    fi
    image=$1
    if [[ "$(docker images -q ${image} 2> /dev/null)" == "" ]]; then
        echo "Build ### ${image} ### failed"
        exit 1
    else
        echo "Build ### ${image} ### completed"
    fi
}