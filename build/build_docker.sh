#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
cp ../requirements.txt ../check_installation.py .
docker build -t ghcr.io/datakami/llamaindex-workshop .
