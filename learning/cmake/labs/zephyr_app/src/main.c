/* SPDX-License-Identifier: Apache-2.0 */
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>
#ifdef CONFIG_LEARNING_SCALE
#include "scale.h"
#endif

int main(void)
{
#ifdef CONFIG_LEARNING_SCALE
    printk("module result=%d\n", scale_sample(21));
#else
    printk("module disabled\n");
#endif
    return 0;
}
