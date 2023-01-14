#!/usr/bin/env bash

set -e

docker push struckchure/stritter_strit_service:$@
docker push struckchure/stritter_strit_service:latest

docker push ghcr.io/struckchure/stritter_strit_service:$@
docker push ghcr.io/struckchure/stritter_strit_service:latest
