#!/bin/bash


start_build(){
    sudo rm -r $BUILD_FOLDER
    create_dir_not_present $BUILD_FOLDER
    sudo cp -r app $BUILD_FOLDER
    sudo cp -r test $BUILD_FOLDER
}


pre_build(){
    read_config; 
    echo "Opening $BEAMUP_BUILD_PATH/$PROJECT_NAME"
    cd $BEAMUP_BUILD_PATH/$PROJECT_NAME
    echo $BUILD_FOLDER
    start_build
}