# Copyright The zephyr_hc32f4a0 Contributors
# SPDX-License-Identifier: Apache-2.0

# Pass both options through tool-opt so they apply to flash and GDB server.
# The user script in this project config is relative to the project root.
board_runner_args(pyocd
  "--target=hc32f4a0xi"
  "--frequency=10000000"
  "--tool-opt=--project=${ZEPHYR_BASE}"
  "--tool-opt=--config=${ZEPHYR_BASE}/debug/pyocd.yaml"
)
include(${ZEPHYR_BASE}/boards/common/pyocd.board.cmake)
