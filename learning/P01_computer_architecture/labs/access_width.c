/* SPDX-License-Identifier: Apache-2.0 */
#include <stdint.h>

/** @brief 读取第二个字节，返回零扩展后的 32 位值。 */
uint32_t read_byte(const volatile uint8_t *bytes)
{
    return bytes[1];
}

/** @brief 读取第二个 32 位元素。 */
uint32_t read_word(const volatile uint32_t *words)
{
    return words[1];
}

/** @brief 只修改第二个字节。 */
void write_byte(volatile uint8_t *bytes, uint8_t value)
{
    bytes[1] = value;
}
