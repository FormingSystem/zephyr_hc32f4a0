<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32 SoC 组件

树内实现位于 [`xhsc/hc32f4a0/`](xhsc/hc32f4a0/)，采用 Zephyr hardware model v2。
SoC 为 `hc32f4a0pitb`，系列为 `hc32f4a0`，厂商族为 `xhsc`；
`SOC_HC32F4A0PITB` 选择 Cortex-M4、FPU、Zephyr SysTick 与启动钩子。
板目标为 `uyup_rpi_a/hc32f4a0pitb`。

| 区域 | 起始地址 | 大小 |
| --- | --- | --- |
| 内部 Flash | `0x00000000` | 2 MiB |
| 主 SRAM | `0x1FFE0000` | 512 KiB |
| 备份 SRAM | `0x200F0000` | 4 KiB |

主 SRAM 结束地址为 `0x2005FFFF`，包括 SRAMH 和 SRAM1..4；备份 SRAM 不并入默认 RAM。
主 SRAM 起点不满足单个 512 KiB ARMv7-M MPU 区域的对齐要求，因此首版关闭 MPU
和硬件栈保护，后续需提供正确的多区域映射再启用。

启动复用 Zephyr 的 reset、向量表、数据初始化和 SysTick 实现，SoC 提供正确返回的
reset hook 与时钟初始化 hook。向量规模为 144 个外部 IRQ，NVIC 优先级为 4 位。
Flash **`0x400`** 处的 ICG 配置由 `icg.ld` 固定并保留，不使用厂商独立启动文件。

UYUP 首版由 **12 MHz XTAL 直驱，不启用 PLL**，系统频率、总线分频和存储器等待周期
在 SoC 初始化中配套设置，保持 Zephyr 的 VTOR/FPU 状态。HC32 DDL 位于仓库内
`modules/hal/xhsc/`，SoC CMake 只编译需要的源文件并使用项目配置。

外设中断源到 NVIC 槽位的路由尚未实现；当前 UART 与 GPIO 使用 polling 或直接读写。
完整向量表和编译结果不能证明物理中断、时钟或板卡已经运行，实板结果需单独验收。
