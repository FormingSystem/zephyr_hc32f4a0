<!--
SPDX-FileCopyrightText: Copyright The Zephyr Project Contributors
SPDX-License-Identifier: Apache-2.0
-->

# HC32F4A0 板级启动示例

本示例使用仓库内的完整 Zephyr 源码，默认目标为
`uyup_rpi_a/hc32f4a0pitb`。程序打印实际 `CONFIG_BOARD_TARGET`，每秒输出心跳，
并在 GPIO 和 `led0` 可用时翻转 LED。GPIO 初始化或操作失败会输出错误，
随后继续提供控制台心跳；没有 LED 的平台也可以运行。

UYUP-RPI-A-2.5 的控制台使用 USART1 PA9/PA10、115200 8N1，`led0` 为低有效的
PD10 蓝灯。初始时钟采用板载 **12 MHz XTAL 直驱，不启用 PLL**。芯片为
HC32F4A0PITB / LQFP100，具有 2 MiB Flash 和从 `0x1FFE0000` 开始的
512 KiB 主 SRAM；未引出的引脚保持 NC，不纳入可访问的 GPIO 掩码。

在仓库根目录执行：

```powershell
. .\scripts\Enter-Environment.ps1
python scripts/project.py build
```

入口直接调用 CMake，使用本仓库的源码、CMSIS 和 HC32 DDL，不依赖旁边的
Zephyr 源码或 west 工作区。HC32 产物位于 `build/bringup/zephyr/`；
`build --pristine` 使用 `cmake --fresh` 重新配置。

将 HC32 固件下载并运行后，预期控制台包含以下内容；这是验收条件，不是已完成的实板结果：

```text
HC32F4A0 bringup ready on uyup_rpi_a/hc32f4a0pitb
Heartbeat on uyup_rpi_a/hc32f4a0pitb
```

主机软件回归使用 Cortex-M4 QEMU `mps2/an386`：

```powershell
python scripts/project.py build --board mps2/an386
python scripts/project.py test
```

MPS2 编译输出位于 `build/mps2/`。测试入口直接运行仓库内的 Twister，输出位于
`build/twister/`，匹配 `HC32F4A0 bringup ready on mps2/an386` 后结束仿真。
`tests.yaml` 分别登记 HC32 的 `build_only` 检查和 MPS2 的 QEMU 控制台测试。

QEMU 运行只验证软件回归。HC32 的物理 SWD、12 MHz 时钟、串口、LED 和
SysTick 运行结果仍需接板验证，并记录在项目移植状态中。
