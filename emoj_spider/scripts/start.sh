#!/usr/bin/env bash

timestamp=`date +%Y_%m_%d_%H_%M_%S`
date=`date +%Y_%m_%d`

user_path=${HOME}
log_date_path="${user_path}/logs/emoj/${date}"
project_env_path="${user_path}/.pyenv/versions/2.7.9/envs/emoj/"
project_path="${user_path}/code/emoj"

if [ ! -d ${log_date_path} ]; then
  mkdir -p ${log_date_path}
fi

params="$@"
debug_string="DEBUG=False"

if [[ ${params} == ${debug_string} ]]; then
    echo "production"
    cd "${project_path}/current"
else
    echo "development"
    cd "${project_path}"
fi

nohup  "${project_env_path}/bin/scrapy crawl zhuangbi" > "${log_date_path}/zhuangbi_${timestamp}.log" 2>&1 &
nohup  "${project_env_path}/bin/scrapy crawl doutula" > "${log_date_path}/doutula_${timestamp}.log" 2>&1 &

