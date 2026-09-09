# SPDX-FileCopyrightText: Copyright The Zephyr HC32F4A0 Contributors
# SPDX-License-Identifier: Apache-2.0

set(HC32_DDL_DIR ${ZEPHYR_BASE}/modules/hal/xhsc/hc32_ddl/hc32f4a0)

zephyr_include_directories(
  .
  ${HC32_DDL_DIR}/soc
  ${HC32_DDL_DIR}/drivers/inc
)
zephyr_compile_definitions(HC32F4A0 USE_DDL_DRIVER XTAL_VALUE=12000000UL)
# Use one DDL configuration even for vendor headers with same-directory includes.
zephyr_compile_options(-include "${CMAKE_CURRENT_SOURCE_DIR}/hc32_ll_conf.h")

# Compile the required DDL components without the vendor vector/reset handlers.
zephyr_sources(
  soc.c
  reset_hook.S
  ${HC32_DDL_DIR}/soc/system_hc32f4a0.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_clk.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_efm.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_fcg.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_gpio.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_icg.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_pwc.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_sram.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_usart.c
  ${HC32_DDL_DIR}/drivers/src/hc32_ll_utility.c
)

zephyr_linker_sources(ROM_START SORT_KEY 0x1icg icg.ld)
set(SOC_LINKER_SCRIPT
    ${ZEPHYR_BASE}/include/zephyr/arch/arm/cortex_m/scripts/linker.ld
    CACHE INTERNAL ""
)
