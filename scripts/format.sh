#!/bin/bash

############################################################################
# Format all libraries
# Usage: ./scripts/format.sh
############################################################################

CURR_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "${CURR_DIR}")"
bitca_DIR="${REPO_ROOT}/libs/bitca"
bitca_DOCKER_DIR="${REPO_ROOT}/libs/infra/bitca_docker"
bitca_AWS_DIR="${REPO_ROOT}/libs/infra/bitca_aws"
COOKBOOK_DIR="${REPO_ROOT}/cookbook"
source ${CURR_DIR}/_utils.sh

print_heading "Formatting all libraries"
source ${bitca_DIR}/scripts/format.sh
source ${bitca_DOCKER_DIR}/scripts/format.sh
source ${bitca_AWS_DIR}/scripts/format.sh

# Format all cookbook examples
source ${COOKBOOK_DIR}/scripts/format.sh
