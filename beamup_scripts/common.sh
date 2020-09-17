#!/bin/bash

activate_virtual_environment(){
    echo -e "\n >>> Activating virtual environment >>>"
    source ../venv/bin/activate
}

# enter_to_project_folder(){
#     cd $PROJECT_NAME
# }

start_nginx(){
    #start the nginx
    sudo /etc/init.d/nginx start
}

restart_nginx(){
    #restart nginx
    sudo /etc/init.d/nginx restart
}

update_supervisor(){
    echo -e "\n >>> Updating Supervisor >>>"
    sudo supervisorctl reread
    sudo supervisorctl update
}

restart_supervisor(){
    echo -e "\n>>>>>=Restarting Server>>>>>="
    sudo supervisorctl restart $PROJECT_NAME
    echo -e ">>>>>=Server Restarted>>>>>==\n"
}

restart_all_server(){
  restart_nginx
  restart_supervisor
}

check_for_environment_variable(){
    if [ -z "$URL" ]
    then
        echo "please provide a URL for deployment...."
        exit 1
    fi
    if [ -z "$DEPLOY_PORT" ]
    then
        echo "please provide a PORT for deployment...."
        exit 1
    fi
}







# create_dir_not_present(){
#   dir=$1
#   if [[ ! -e $dir ]]; then
#     mkdir $dir
#   else
#     echo "$dir already exists"
# fi
# }





# delete_project(){
#   echo -e "\n >>> Deleting Project >>>"
#   sudo rm /etc/supervisor/conf.d/$PROJECT_NAME".conf"
#   update_supervisor
#   sudo rm /etc/nginx/sites-enabled/$PROJECT_NAME
#   sudo rm /etc/nginx/sites-available/$PROJECT_NAME
#   restart_nginx
#   sudo rm -rfv $DEPLOY_PATH
#   sudo rm -rfv $BACKUP_PATH
#   sudo rm -rfv $DB_PATH
#   echo -e "\n >>> $PROJECT_NAME is deleted :( >>>"
# }




