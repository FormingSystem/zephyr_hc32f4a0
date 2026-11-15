<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32 Zephyr 驱动组件

HC32 驱动已经接入本仓库 Zephyr 源码树的对应 CMake/Kconfig。
当前实现服务于 `uyup_rpi_a/hc32f4a0pitb` 的基础启动：

| 文件 | 当前接口 |
| --- | --- |
| [`serial/uart_hc32.c`](serial/uart_hc32.c) | USART1 `poll_in`、`poll_out` 和错误状态检查；PA9/PA10、115200 8N1 |
| [`gpio/gpio_hc32.c`](gpio/gpio_hc32.c) | 输入、输出、内部上拉、开漏、端口读取和掩码写入、置位、清零、翻转 |

绑定使用 `xhsc,hc32-uart` 和 `xhsc,hc32-gpio`。UART 根据 devicetree 的端口、
引脚和波特率初始化，并限制到已实现的 USART1 PA9/PA10 组合；不支持的配置返回错误。
GPIO 同时检查 devicetree 保留范围和 LQFP100 封装掩码，NC 引脚不能配置或写入。
低有效语义由 Zephyr GPIO API 处理，原始端口读写保持物理电平含义。

驱动使用仓库内 `modules/hal/xhsc/` 的 DDL，由 SoC CMake 选择所需源文件。
SoC 负责 **12 MHz XTAL 直驱、不启用 PLL** 的时钟初始化；UART 根据实际外设时钟
设置波特率，不套用旧模板的 24 MHz 参数。

当前不支持 UART 中断/异步/DMA、GPIO 中断和外设中断路由；下拉、开源等未支持的
GPIO 模式不会被静默模拟。其他外设仍需独立实现驱动及 binding。

`python scripts/project.py build` 构建真实 HC32 目标；
`python scripts/project.py test` 运行 MPS2 QEMU 软件回归。上述检查不替代
HC32 实板的串口、GPIO、时钟和中断验收。
