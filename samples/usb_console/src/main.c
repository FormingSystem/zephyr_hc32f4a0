/*
 * Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/logging/log.h>
#include <zephyr/sys/printk.h>

LOG_MODULE_REGISTER(hc32_usb_console, LOG_LEVEL_INF);

static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios);
static const struct device *const console = DEVICE_DT_GET(DT_CHOSEN(zephyr_console));

int main(void)
{
	uint32_t sequence = 0;
	int64_t next_heartbeat = 0;
	bool led_ready = gpio_is_ready_dt(&led);

	if (!device_is_ready(console)) {
		return -ENODEV;
	}
	if (led_ready && gpio_pin_configure_dt(&led, GPIO_OUTPUT_INACTIVE) != 0) {
		led_ready = false;
	}

	/* USB is initialized by Zephyr's cdc-acm-console snippet. Do not block
	 * board execution waiting for a host to open the COM port.
	 */
	for (;;) {
		uint32_t dtr = 0;
		unsigned char c;

		(void)uart_line_ctrl_get(console, UART_LINE_CTRL_DTR, &dtr);
		if (k_uptime_get() >= next_heartbeat) {
			if (led_ready) {
				(void)gpio_pin_toggle_dt(&led);
			}
			if (dtr != 0) {
				LOG_INF("USB1 CDC ACM heartbeat %u, uptime %lld ms", sequence,
					(long long)k_uptime_get());
			}
			sequence++;
			next_heartbeat = k_uptime_get() + 1000;
		}
		/* Echo host input to exercise both OUT and IN endpoints. */
		while (dtr != 0 && uart_poll_in(console, &c) == 0) {
			uart_poll_out(console, c);
		}
		k_msleep(10);
	}
}
