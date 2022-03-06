#!/bin/bash


if [[ $(docker ps) == *"django-server"* ]]; then
  docker stop django-server

fi