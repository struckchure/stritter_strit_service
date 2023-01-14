#!/usr/bin/env bash

set -e

docker build . -f build/python/Dockerfile -t struckchure/stritter_strit_service:$@
docker build . -f build/python/Dockerfile -t struckchure/stritter_strit_service:latest

docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_strit_service:$@
docker build . -f build/python/Dockerfile -t ghcr.io/struckchure/stritter_strit_service:latest
