/* SPDX-License-Identifier: Apache-2.0 */
#include <stdint.h>

/* 启动实验观察对象：分别进入 .data 和 .bss。 */
volatile uint32_t initial_value = 7u;
volatile uint32_t loop_count;

static uint32_t mmio_read(uintptr_t address)
{
    return *(volatile uint32_t *)address;
}

static void mmio_write(uintptr_t address, uint32_t value)
{
    *(volatile uint32_t *)address = value;
}

/** @brief 建立教学约定的 PB0 输出与 PC13 上拉输入。 */
static void gpio_init(void)
{
    const uintptr_t rcc_enable = 0x580244E0u;
    const uintptr_t gpio_b = 0x58020400u;
    const uintptr_t gpio_c = 0x58020800u;

    mmio_write(rcc_enable, mmio_read(rcc_enable) | (1u << 1) | (1u << 2));
    (void)mmio_read(rcc_enable);
    mmio_write(gpio_b + 0x18u, 1u << 16);
    mmio_write(gpio_b + 0x04u, mmio_read(gpio_b + 0x04u) & ~1u);
    mmio_write(gpio_b + 0x08u, mmio_read(gpio_b + 0x08u) & ~3u);
    mmio_write(gpio_b + 0x0Cu, mmio_read(gpio_b + 0x0Cu) & ~3u);
    mmio_write(gpio_b, (mmio_read(gpio_b) & ~3u) | 1u);
    mmio_write(gpio_c, mmio_read(gpio_c) & ~(3u << 26));
    mmio_write(gpio_c + 0x0Cu,
               (mmio_read(gpio_c + 0x0Cu) & ~(3u << 26)) | (1u << 26));
}

/** @brief 按住 PC13 按钮时令 PB0 输出高电平；无消抖。 */
int main(void)
{
    gpio_init();
    for (;;) {
        uint32_t input = mmio_read(0x58020810u);
        uint32_t output = (input & (1u << 13)) ? (1u << 16) : 1u;
        mmio_write(0x58020418u, output);
        loop_count++;
    }
}
