---
id: learning.zephyr-docs.kconfig-reference.page-41
title: "`boards/Kconfig`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第41章\_`boards/Kconfig`配置项参考

本章翻译官方 Kconfig 数据库中 `boards/Kconfig` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BOARD"></a>

## 41.1 `CONFIG_BOARD`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

保存开发板名称（Board Name），用于定位源码树中与开发板相关的文件，位于 `boards/` 下。查找 `linker.ld` 时先查开发板目录；如果未找到，则在 `soc/<arch>/<family>/<series>` 中查找链接器文件（Linker File）。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"boards"
```

**定义位置（Location）**：[`boards/Kconfig:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L3)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_DEPRECATED_RELEASE"></a>

## 41.2 `CONFIG_BOARD_DEPRECATED_RELEASE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此隐藏选项在开发板配置中设置，指明将在哪个 Zephyr 发布版本（Release）移除该开发板配置。设置后，对该开发板进行任何构建都会生成醒目的弃用警告（Deprecation Warning）。为某个 `BOARD` 添加此选项时，请遵循[官方 API 生命周期文档中的弃用说明](https://docs.zephyrproject.org/latest/develop/api/api_lifecycle.html#deprecated)。

**类型（Type）**：字符串（String），`string`。

**定义位置（Location）**：[`boards/Kconfig:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L32)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_HAS_TIMING_FUNCTIONS"></a>

## 41.3 `CONFIG_BOARD_HAS_TIMING_FUNCTIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果开发板提供获取时间戳（Timestamp）和周期计数（Cycle Count）的自定义方法，应选择此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`boards/Kconfig:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L188)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_REQUIRES_SERIAL_BACKEND_CDC_ACM"></a>

## 41.4 `CONFIG_BOARD_REQUIRES_SERIAL_BACKEND_CDC_ACM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

表示开发板只能使用 CDC ACM UART 作为日志（Logging）或命令行（Shell）的后端，没有其他可用方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`boards/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

<a id="CONFIG_BOARD_REVISION"></a>

## 41.5 `CONFIG_BOARD_REVISION`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

如果 `BOARD` 设置了修订版本字段（Revision Field），则此值为该修订版本；否则为空字符串。例如，为 `plank@foo` 构建时，此值为 `foo`；为 `plank` 构建时，此值为空字符串。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`boards/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_BOARD_SERIAL_BACKEND_CDC_ACM"></a>

## 41.6 `CONFIG_BOARD_SERIAL_BACKEND_CDC_ACM`

**提示（Prompt）**：开发板使用 USB CDC ACM UART 作为串口后端（Serial Backend）

**说明（Help）**

在启动时配置并初始化 USB 协议栈（USB Stack）和 CDC ACM UART，将其用作日志（Logging）或命令行（Shell）的后端。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BOARD_REQUIRES_SERIAL_BACKEND_CDC_ACM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`boards/Kconfig:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_BOARD_REQUIRES_SERIAL_BACKEND_CDC_ACM`](P041_boards_Kconfig_配置项参考.md#CONFIG_BOARD_REQUIRES_SERIAL_BACKEND_CDC_ACM)。

<a id="CONFIG_BOARD_TARGET"></a>

## 41.7 `CONFIG_BOARD_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

包含所用开发板的完整目标字符串（Board Target），包括名称（Name）、修订版本（Revision）、片上系统（SoC）、集群（Cluster）和变体（Variant）。例如，为 `nrf5340dk/nrf5340/cpuapp` 构建时，此值为 `nrf5340dk/nrf5340/cpuapp`。

**类型（Type）**：字符串（String），`string`。

**默认值（Defaults）**

```text
"boards@/" if "" != ""
"boards/"
```

**定义位置（Location）**：[`boards/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top）

<a id="CONFIG_ESPRESSIF_QEMU_TARGET"></a>

## 41.8 `CONFIG_ESPRESSIF_QEMU_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

乐鑫 QEMU 构建的隐藏标记（Hidden Marker），由 `CONFIG_ESPRESSIF_QEMU` 选择。开发板文件使用此符号启用 `espressif_qemu` 仿真平台，即将其纳入 `SUPPORTED_EMU_PLATFORMS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ESPRESSIF_QEMU
```

**定义位置（Location）**：[`boards/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_ESPRESSIF_QEMU`](P044_boards_espressif_配置项参考.md#CONFIG_ESPRESSIF_QEMU)。

<a id="CONFIG_QEMU_DEVICE_LOADER"></a>

## 41.9 `CONFIG_QEMU_DEVICE_LOADER`

**提示（Prompt）**：QEMU 设备加载器（Device Loader）

**说明（Help）**

启用后，QEMU 使用设备加载器（Device Loader）功能加载 ELF 文件，而不是使用 `-kernel` 选项。在 RISC-V 等某些架构上，QEMU 的设计是加载 ELF 中的最低地址，而不是其中的入口点（Entry Point）。此选项启用 `board.cmake` 层的相应逻辑，使用 `-device,loader` 代替 `-kernel` 进行加载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET
```

**定义位置（Location）**：[`boards/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)。

<a id="CONFIG_QEMU_EXTRA_FLAGS"></a>

## 41.10 `CONFIG_QEMU_EXTRA_FLAGS`

**提示（Prompt）**：QEMU 额外标志（Extra Flags）

**说明（Help）**

向 QEMU 传递额外的参数列表以设置设备，例如使用 `-serial tcp:127.0.0.1:5678,server`，为 Zephyr GDB 调试桩（GDBstub）分配串行接口。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`boards/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)。

<a id="CONFIG_QEMU_GDBSERVER_LISTEN_DEV"></a>

## 41.11 `CONFIG_QEMU_GDBSERVER_LISTEN_DEV`

**提示（Prompt）**：QEMU gdbserver 监听设备（Listen Device）

**说明（Help）**

作为 QEMU 的 `-gdb` 选项参数传入。默认值等同于 `-s`，后者是 `-gdb tcp::1234` 的简写。空值会完全省略 `-gdb` 参数，从而允许通过 `QEMU_EXTRA_FLAGS` 环境变量等其他来源注入该参数。更多信息参阅应用开发文档和／或 QEMU 调用文档（Invocation Documentation）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET
```

**默认值（Defaults）**

```text
"tcp::1234"
```

**定义位置（Location）**：[`boards/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)。

<a id="CONFIG_QEMU_ICOUNT"></a>

## 41.12 `CONFIG_QEMU_ICOUNT`

**提示（Prompt）**：QEMU 指令计数模式（icount Mode）

**说明（Help）**

启用 QEMU 虚拟指令计数器（Virtual Instruction Counter）。虚拟 CPU 每经过 `2^N` 纳秒虚拟时间执行一条指令，使客户机（Guest）观察到确定的执行时间（Deterministic Execution Times）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET
```

**默认值（Defaults）**

```text
y if !CONFIG_NETWORKING && !CONFIG_BT
```

**定义位置（Location）**：[`boards/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)。

<a id="CONFIG_QEMU_ICOUNT_SHIFT"></a>

## 41.13 `CONFIG_QEMU_ICOUNT_SHIFT`

**提示（Prompt）**：QEMU icount 移位值（Shift Value）

**说明（Help）**

虚拟 CPU 每经过 `2^N` 纳秒虚拟时间（Virtual Time）执行一条指令，其中 `N` 为此处设置的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_ICOUNT
```

**定义位置（Location）**：[`boards/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → QEMU 指令计数模式（icount Mode）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_ICOUNT`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_ICOUNT)。

<a id="CONFIG_QEMU_ICOUNT_SLEEP"></a>

## 41.14 `CONFIG_QEMU_ICOUNT_SLEEP`

**提示（Prompt）**：启用 QEMU icount 休眠模式（Sleep Mode）

**说明（Help）**

启用后，虚拟 CPU 休眠时，虚拟时间（Virtual Time）按默认速率前进。禁用后，只要虚拟 CPU 进入休眠模式，虚拟时间就立即跳到下一个定时器截止时刻（Timer Deadline）；如果未启用任何定时器，则时间不前进。这种行为使客户机（Guest）观察到确定的执行时间（Deterministic Execution Times）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_ICOUNT
```

**定义位置（Location）**：[`boards/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options） → QEMU 指令计数模式（icount Mode）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_ICOUNT`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_ICOUNT)。

<a id="CONFIG_QEMU_IVSHMEM_PLAIN_MEM_SIZE"></a>

## 41.15 `CONFIG_QEMU_IVSHMEM_PLAIN_MEM_SIZE`

**提示（Prompt）**：QEMU ivshmem-plain 共享内存大小，单位为兆字节（Shared Memory Size）

**说明（Help）**

设置 QEMU 使用 `ivshmem-plain` 设备时的共享内存（Shared Memory）大小。单位为兆字节，因此值 1 对应 QEMU 中的 `1M`，依此类推。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET && CONFIG_IVSHMEM && !CONFIG_IVSHMEM_DOORBELL
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`boards/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_IVSHMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM)、[`CONFIG_IVSHMEM_DOORBELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_DOORBELL)。

<a id="CONFIG_QEMU_TARGET"></a>

## 41.16 `CONFIG_QEMU_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用此变量标记所有 QEMU 目标，以检查当前是否运行在仿真环境（Emulated Environment）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_SOC_QEMU_CORTEX_A53
```

**定义位置（Location）**：[`boards/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_SOC_QEMU_CORTEX_A53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_QEMU_CORTEX_A53)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_QEMU_CORTEX_A53`。

<a id="CONFIG_QEMU_UEFI_BOOT"></a>

## 41.17 `CONFIG_QEMU_UEFI_BOOT`

**提示（Prompt）**：QEMU 使用 UEFI 启动（UEFI Boot）

**说明（Help）**

表示 QEMU 将使用统一可扩展固件接口（UEFI）可启动方式进行启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BUILD_OUTPUT_EFI && CONFIG_QEMU_TARGET && CONFIG_X86_64
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`boards/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_BUILD_OUTPUT_EFI`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_BUILD_OUTPUT_EFI)、[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_X86_64`](P039_arch_x86_配置项参考.md#CONFIG_X86_64)。

<a id="CONFIG_QEMU_VIRTIO_BLK_DISK_SIZE"></a>

## 41.18 `CONFIG_QEMU_VIRTIO_BLK_DISK_SIZE`

**提示（Prompt）**：QEMU virtio-blk 磁盘镜像大小（Disk Image Size）

**说明（Help）**

创建原始格式的 virtio-blk 后备镜像（Raw Backing Image）时传给 `qemu-img` 的大小。该值采用 `qemu-img` 的大小语法，例如 `1M` 或 `64M`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET && CONFIG_DISK_DRIVER_VIRTIO_BLK
```

**默认值（Defaults）**

```text
"1M"
```

**定义位置（Location）**：[`boards/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_VIRTIO_BLK)。

<a id="CONFIG_QEMU_VIRTIO_BLK_LOGICAL_BLOCK_SIZE"></a>

## 41.19 `CONFIG_QEMU_VIRTIO_BLK_LOGICAL_BLOCK_SIZE`

**提示（Prompt）**：QEMU virtio-blk 逻辑块大小（Logical Block Size）

**说明（Help）**

创建 QEMU 仿真的 virtio-blk 设备时使用 `logical_block_size=<value>`，因此客户机驱动（Guest Driver）会协商并看到该逻辑块大小（Logical Block Size）。主要用于测试非 512 字节的块大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_QEMU_TARGET && CONFIG_DISK_DRIVER_VIRTIO_BLK
```

**默认值（Defaults）**

```text
512
```

**取值范围（Ranges）**

```text
[512, 4096]
```

**定义位置（Location）**：[`boards/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 开发板选项（Board Options）

**配置项引用（Symbol References）**：[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_DISK_DRIVER_VIRTIO_BLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DISK_DRIVER_VIRTIO_BLK)。

<a id="CONFIG_WHISPER_TARGET"></a>

## 41.20 `CONFIG_WHISPER_TARGET`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

使用此变量标记目标，以检查当前是否运行在 Whisper 模拟器（Simulator）中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RISCV
```

**定义位置（Location）**：[`boards/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/boards/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<!-- kconfig-navigation -->

[上一章](P040_arch_xtensa_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P042_boards_Kconfig.v2_配置项参考.md)
