/* SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors */
/* SPDX-License-Identifier: Apache-2.0 */

#include <stdbool.h>

#include <zephyr/devicetree.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

#define LED0_NODE DT_ALIAS(led0)
#define HEARTBEAT_INTERVAL_MS 1000

#if defined(CONFIG_GPIO) && DT_NODE_HAS_STATUS(LED0_NODE, okay) && \
	DT_NODE_HAS_PROP(LED0_NODE, gpios)
#include <zephyr/drivers/gpio.h>

static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED0_NODE, gpios);
#define HAS_LED0 1
#else
#define HAS_LED0 0
#endif

int main(void)
{
#if HAS_LED0
	bool led_ready = gpio_is_ready_dt(&led);
	int err;

	if (led_ready) {
		err = gpio_pin_configure_dt(&led, GPIO_OUTPUT_INACTIVE);
		if (err != 0) {
			printk("LED0 configuration failed: %d\n", err);
			led_ready = false;
		}
	} else {
		printk("LED0 controller is not ready\n");
	}
#else
	printk("LED0 is unavailable; console heartbeat enabled\n");
#endif

	printk("HC32F4A0 bringup ready on %s\n", CONFIG_BOARD_TARGET);

	while (true) {
#if HAS_LED0
		if (led_ready) {
			err = gpio_pin_toggle_dt(&led);
			if (err != 0) {
				printk("LED0 toggle failed: %d\n", err);
				led_ready = false;
			}
		}
#endif
		printk("Heartbeat on %s\n", CONFIG_BOARD_TARGET);
		k_msleep(HEARTBEAT_INTERVAL_MS);
	}

	return 0;
}
