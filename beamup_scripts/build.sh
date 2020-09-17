#!/bin/bash


start_build(){
    create_dir_not_present $BUILD_FOLDER
    sudo cp -r app $BUILD_FOLDER/app
}


pre_build(){
    read_config; 
    echo "Opening $BEAMUP_BUILD_PATH/$PROJECT_NAME"
    cd $BEAMUP_BUILD_PATH/$PROJECT_NAME
    echo $BUILD_FOLDER
    start_build
}