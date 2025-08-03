#!/bin/bash

uv run prefect work-pool create --type docker my-docker-pool
uv runprefect work-pool start --pool my-docker-pool
uv run ./orchestrator/orchestration.py