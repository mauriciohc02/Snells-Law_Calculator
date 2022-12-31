#!/bin/bash


CONTAINER_NAME="Snells-Law_Calculator"
IMAGE_NAME="mauriciohc/snells-law:latest"
DOCKER_RUN_PARAMS="-e "DISPLAY" --network host -v $(pwd)/plots:/home/Snells-Law_Calculator/plots:rw --name $CONTAINER_NAME $IMAGE_NAME"


function is_docker_install() {
    # Verify if the whole script can be run by checking if Docker is installed
    if ! [[ $(docker version 2>/dev/null) ]]
    then
        echo "Install Docker in order to run this script successfully"
        exit 1
    fi
}


function is_docker_compose_install() {
    # Verify if some of these commands do exist
    if [[ $(docker compose version 2>/dev/null) ]]
    then
        echo "Running $CONTAINER_NAME with Docker Compose"
        return 1
    elif [[ $(docker-compose --version 2>/dev/null) ]]
    then
        echo "Running $CONTAINER_NAME with Docker-Compose"
        return 2
    else
        echo "Running $CONTAINER_NAME just with Docker"
        return 3
    fi
}


function run_container() {
    # Based on is_docker_compose_install(), choose which commands will use
    is_docker_compose_install
    case "$?" in
        1)
            docker compose up &>/dev/null
            docker compose down &>/dev/null
            ;;
        2)
            docker-compose up &>/dev/null
            docker-compose down &>/dev/null
            ;;
        3)
            docker run --rm $DOCKER_RUN_PARAMS &>/dev/null
            ;;
    esac
}


is_docker_install
xhost +local:* &>/dev/null
run_container
echo "$CONTAINER_NAME Container has been stopped and removed"
xhost -local:* &>/dev/null

exit 0
