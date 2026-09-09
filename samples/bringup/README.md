<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# 工程组件启动示例

示例自动加载本仓库的 Zephyr module，使用
`CONFIG_HC32F4A0_PORT_MODULE=y` 验证 Kconfig 集成。
它打印实际 `CONFIG_BOARD_TARGET`、每秒输出心跳，并在 `CONFIG_GPIO` 已启用且
devicetree 有可用 `led0` 时配置和翻转 LED。GPIO 初始化或操作失败会输出错误，
之后继续提供控制台心跳；没有 LED 的平台也可以运行。

当前可验证平台为 Cortex-M4 QEMU `mps2/an386`，这不代表 HC32 实板已经支持。
目标 HC32F4A0PITB 为 2 MiB Flash、512 KiB 系统 SRAM、12 MHz 板载主晶振，
其 SoC、时钟和驱动仍需实现。

在已激活的 Zephyr west 工作区中，从本仓库目录运行：

```powershell
west build -b mps2/an386 samples/bringup -d build/bringup
west build -d build/bringup -t run
```

控制台包含：

```text
HC32F4A0 bringup module ready on mps2/an386
Heartbeat on mps2/an386
```

交互运行会持续输出心跳。由当前工具提供的停止操作结束 QEMU。
自动验证使用 Twister 的控制台匹配，匹配启动行后自动结束仿真：

```powershell
west twister -T samples/bringup -p mps2/an386 --outdir build/twister-bringup
```

该验证覆盖模块发现、配置、编译、链接、QEMU 启动和串口输出，不访问实板，
也不验证 HC32 GPIO、PLL、下载器或物理 UART。
