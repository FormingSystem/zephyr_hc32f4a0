/* SPDX-License-Identifier: Apache-2.0 */
#include <stdint.h>

/** @brief 对计数值做一次增加，再限制上界。 */
uint32_t cap_count(uint32_t count, uint32_t limit)
{
    uint32_t next = count + 1u;
    return next > limit ? limit : next;
}

/** @brief 通过指针读取状态并写回，用于观察加载和存储。 */
void increment_word(volatile uint32_t *count)
{
    *count = *count + 1u;
}
