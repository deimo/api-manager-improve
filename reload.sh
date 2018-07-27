#!/bin/bash

# 重启脚本，使用此脚本，优雅地重启uwsgi

echo "stop ..."

echo `date +%Y-%m-%d\ %H:%M:%S` >> 'log/reload.log'

echo "start ..."
