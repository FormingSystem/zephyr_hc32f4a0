<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# SoC 组件

此目录已通过模块设置注册为外部 SoC root。当前未实现 HC32 SoC，
没有 `soc.yml` 或可选的 `SOC_HC32F4A0` 配置。

实现目录预留为 `soc/xhsc/hc32f4a0/`，使用 Zephyr hardware model v2，
提供 `soc.yml`、`soc.h`、`Kconfig.soc`、`Kconfig`、`CMakeLists.txt`、
必要的启动代码与链接配置。设备系列名采用 `hc32f4a0`，封装和容量单独描述。

HC32F4A0PITB 的移植内存依据：

| 区域 | 起始地址 | 大小 |
| --- | --- | --- |
| 内部 Flash | `0x00000000` | 2 MiB |
| 系统 SRAM | `0x1FFE0000` | 512 KiB |
| 备份 SRAM | `0x200F0000` | 4 KiB |

系统 SRAM 结束地址为 `0x2005FFFF`，不能把 512 KiB 全部从
`0x20000000` 起布局。备份 SRAM 不并入默认系统 RAM。

首次启动还需落实 NVIC 中断源选择、SysTick、启动钩子以及 Flash `0x400`
处的 ICG 配置段。外部 `hal_xhsc` 自带启动钩子和 `SystemInit`，接入时必须
审查调用顺序与链接布局，避免和 Zephyr SoC 代码重复定义。

主晶振频率属于板级事实，UYUP 本板为 12 MHz。不得直接沿用 HAL 的 8 MHz
默认值或旧 UYUP 模板的 24 MHz 假设；初始启动先使用经过确认的保守时钟。
