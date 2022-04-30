#!/bin/bash
WORKDIR=$HOME/project/graduation
sh $WORKDIR/etc/del.sh
echo "清除暂存文件done\nrun server"
uwsgi --ini $WORKDIR/etc/image_search_uwsgi.ini
