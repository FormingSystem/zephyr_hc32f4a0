/* SPDX-License-Identifier: Apache-2.0 */
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>

#if defined(CONFIG_APP_GREETING)
#include <app_greeting/greeting.h>
#endif

int main(void)
{
#if defined(CONFIG_APP_GREETING)
	printk("%s\n", app_greeting_message());
#else
	printk("Greeting component is disabled\n");
#endif

	return 0;
}
