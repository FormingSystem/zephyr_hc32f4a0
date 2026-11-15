# SPDX-License-Identifier: Apache-2.0
zephyr_library()
zephyr_library_sources_ifdef(CONFIG_GPIO_HC32 drivers/gpio/gpio_hc32.c)
zephyr_library_sources_ifdef(CONFIG_UART_HC32 drivers/serial/uart_hc32.c)
