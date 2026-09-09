<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32 板级组件

本目录属于仓库内完整 Zephyr 源码树。UYUP 板级实现位于
[`uyup/uyup_rpi_a/`](uyup/uyup_rpi_a/)，使用 hardware model v2，
提供 `board.yml`、Kconfig、DTS、defconfig、平台元数据和 pyOCD runner。
目标名称为 **`uyup_rpi_a/hc32f4a0pitb`**。

UYUP-RPI-A-2.5 采用 HC32F4A0PITB / LQFP100，具有 2 MiB Flash 和
512 KiB 主 SRAM。初始配置由板载 **12 MHz XTAL 直接提供系统时钟，不启用 PLL**。
未引出的引脚按 NC 处理，并由封装 DTS 的保留范围及 GPIO 驱动掩码共同限制。

| 板级功能 | 配置 |
| --- | --- |
| 控制台 | USART1，TX PA9、RX PA10，115200 8N1，polling |
| `led0` / `led1` | PD10 蓝灯 / PE15 绿灯，均低有效 |
| `sw0` / `sw1` | PA3 / PE2，内部上拉、低有效，gpio-keys 使用 polling |
| 调试 | 板载 CMSIS-DAP 2.x / WinUSB，10 MHz SWD |

pyOCD runner 显式加载仓库根目录的 `debug/pyocd.yaml`，同时指定项目根目录，
使用户脚本中的 SRAM 地址修正在烧录和 GDB server 两条入口中均可解析。
板载 DAP 的一根 USB 线提供调试与串口输出。使用外部调试器前，按硬件记录
停用板载 DAP：关电、按住复位、开电、松开复位；完整操作两次，橙灯不闪表示停用。

默认构建入口是 `python scripts/project.py build`，源码和基础依赖均在本仓库。
构建通过不等于实板运行通过；SWD、下载、串口和 LED 验收另行记录。
板级事实统一见 [`../docs/hardware.md`](../docs/hardware.md)。
