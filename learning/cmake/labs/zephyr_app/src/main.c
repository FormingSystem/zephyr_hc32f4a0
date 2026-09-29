/* SPDX-License-Identifier: Apache-2.0 */
#include <zephyr/kernel.h>
#include <zephyr/sys/printk.h>
#ifdef CONFIG_LEARNING_SCALE
#include "scale.h"
#endif

int main(void)
{
#ifdef CONFIG_LEARNING_SCALE
    /* 只有实现参与构建时，才保留这条调用。 */
    printk("module result=%d\n", scale_sample(21));
#else
    /* 关闭时仍有完整的应用路径，不引用 scale_sample。 */
    printk("module disabled\n");
#endif
    return 0;
}
