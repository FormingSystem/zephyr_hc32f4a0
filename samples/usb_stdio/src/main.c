/* Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <ctype.h>
#include <stdio.h>
#include <zephyr/drivers/gpio.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/kernel.h>

#include "usb_stdio.h"

static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios);
static const struct device *const console = DEVICE_DT_GET(DT_CHOSEN(zephyr_console));

static void heartbeat(struct k_work *work);
K_WORK_DELAYABLE_DEFINE(heartbeat_work, heartbeat);

static void heartbeat(struct k_work *work)
{
	ARG_UNUSED(work);
	(void)gpio_pin_toggle_dt(&led);
	(void)k_work_reschedule(&heartbeat_work, K_MSEC(500));
}

/* Consume the entire line, including malformed or overlong input, so the
 * next scanf does not repeatedly encounter the same invalid character.
 */
static bool finish_line(void)
{
	bool whitespace_only = true;
	int c;

	while ((c = getchar()) != '\n' && c != EOF) {
		if (!isspace((unsigned char)c)) {
			whitespace_only = false;
		}
	}
	return whitespace_only && c != EOF;
}

int main(void)
{
	int ret = usb_stdio_init();

	if (ret != 0) {
		return ret;
	}
	if (gpio_is_ready_dt(&led) && gpio_pin_configure_dt(&led, GPIO_OUTPUT_INACTIVE) == 0) {
		(void)k_work_reschedule(&heartbeat_work, K_NO_WAIT);
	}

	/* Opening USB1 with DTR enables interaction; LED work remains runnable. */
	for (;;) {
		uint32_t dtr = 0;

		(void)uart_line_ctrl_get(console, UART_LINE_CTRL_DTR, &dtr);
		if (dtr != 0) {
			break;
		}
		k_msleep(20);
	}

	printf("USB1 stdio ready: enter an integer, then Enter.\n");
	printf("Maximum 9 characters including sign; terminal local echo required.\n");
	for (;;) {
		int value;
		int count;
		bool valid_tail;

		printf("number> ");
		fflush(stdout);
		/* The width bounds conversion to values representable by int. */
		count = scanf("%9d", &value);
		valid_tail = finish_line();
		if (count == 1 && valid_tail) {
			printf("value=%d, twice=%d\n", value, value * 2);
		} else {
			fprintf(stderr, "Invalid input: one integer, at most 9 characters.\n");
			clearerr(stdin);
			k_msleep(10);
		}
	}
}
