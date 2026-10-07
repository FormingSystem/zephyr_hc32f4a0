/* Copyright The Zephyr HC32F4A0 Contributors
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stdbool.h>
#include <stdio.h>
#include <zephyr/console/console.h>
#include <zephyr/sys/util.h>

#include "usb_stdio.h"

static bool previous_cr;

static int stdin_get(FILE *stream)
{
	ARG_UNUSED(stream);

	for (;;) {
		int c = console_getchar();

		if (c < 0) {
			return _FDEV_ERR;
		}
		/* Accept CR, LF and CRLF terminal line endings as one newline. */
		if (previous_cr && c == '\n') {
			previous_cr = false;
			continue;
		}
		previous_cr = (c == '\r');
		return previous_cr ? '\n' : c;
	}
}

int usb_stdio_init(void)
{
	int ret = console_init();

	if (ret != 0) {
		return ret;
	}

	/* Picolibc's public FILE initializer supplies the missing input callback.
	 * stdout/stderr already use Zephyr's CONFIG_STDOUT_CONSOLE routing.
	 * This is application glue, not a portable ISO C or Zephyr console API.
	 */
	*stdin = (FILE)FDEV_SETUP_STREAM(NULL, stdin_get, NULL, _FDEV_SETUP_READ);
	return 0;
}
