---
id: learning.zephyr-docs.kconfig-reference.page-384
title: "`subsys/mgmt`配置项参考（1/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第384章\_`subsys/mgmt`配置项参考（1/4）

本章翻译官方 Kconfig 数据库中 `subsys/mgmt` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_EC_HOST_CMD"></a>

## 384.1 `CONFIG_EC_HOST_CMD`

**提示（Prompt）**：支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**说明（Help）**

为笔记本电脑上的嵌入式控制器（embedded controllers）启用主机命令处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem）

<a id="CONFIG_EC_HOST_CMD_BACKEND_ESPI"></a>

## 384.2 `CONFIG_EC_HOST_CMD_BACKEND_ESPI`

**提示（Prompt）**：通过 eSPI 总线支持主机命令（host commands）

**说明（Help）**

启用通过增强型串行外设接口（eSPI）总线传输嵌入式控制器（EC）主机命令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD && CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_EC_HOST_CMD)、[`CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI_PERIPHERAL_CUSTOM_OPCODE)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI"></a>

## 384.3 `CONFIG_EC_HOST_CMD_BACKEND_SHI`

**提示（Prompt）**：通过串行主机接口（SHI）支持主机命令

**说明（Help）**

启用通过串行主机接口（Serial Host Interface）传输嵌入式控制器主机命令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER"></a>

## 384.4 `CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER`

**提示（Prompt）**：串行主机接口驱动（SHI driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX if CONFIG_SOC_FAMILY_NPCX
CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE if CONFIG_SOC_IT8XXX2
```

**可选项（Choices）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX
CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX)、[`CONFIG_SOC_FAMILY_NPCX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NPCX)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE)、[`CONFIG_SOC_IT8XXX2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_IT8XXX2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NPCX`、`CONFIG_SOC_IT8XXX2`。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE"></a>

## 384.5 `CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE`

**提示（Prompt）**：ITE 串行主机接口（SHI）

**说明（Help）**

启用 ITE IT8xxx2 芯片系列中串行主机接口（SHI）后端的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ITE_IT8XXX2_SHI_ENABLED && <choice CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER>
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 串行主机接口驱动（SHI driver）

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_MAX_REQUEST"></a>

## 384.6 `CONFIG_EC_HOST_CMD_BACKEND_SHI_MAX_REQUEST`

**提示（Prompt）**：第 3 版请求数据包的最大数据大小

**说明（Help）**

指定第 3 版请求数据包（version 3 request packet）的最大数据大小，必须足以处理可能出现的最大请求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
544 if CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX
256 if CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_MAX_RESPONSE"></a>

## 384.7 `CONFIG_EC_HOST_CMD_BACKEND_SHI_MAX_RESPONSE`

**提示（Prompt）**：第 3 版响应数据包的最大数据大小

**说明（Help）**

指定第 3 版响应数据包（version 3 response packet）的最大数据大小，必须足以处理可能出现的最大响应。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
544 if CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX
248 if CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_ITE)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX"></a>

## 384.8 `CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX`

**提示（Prompt）**：Nuvoton 串行主机接口（SHI）

**说明（Help）**

启用 Nuvoton NPCX 芯片中串行主机接口（SHI）后端的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_NUVOTON_NPCX_SHI_ENABLED || DT_HAS_NUVOTON_NPCX_SHI_ENHANCED_ENABLED) && <choice CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER>
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 串行主机接口驱动（SHI driver）

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX_CS_DETECT_WORKAROUND"></a>

## 384.9 `CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX_CS_DETECT_WORKAROUND`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

绕过 npcx9m7fb 片上系统勘误（SoC errata）中“EVSTATS2 寄存器（SHI）的 CSnFE 与 CSnRE 位”问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_NPCX9M7FB
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:80`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L80)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_SOC_NPCX9M7FB`](P292_soc_nuvoton_配置项参考.md#CONFIG_SOC_NPCX9M7FB)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX_ENHANCED_BUF_MODE"></a>

## 384.10 `CONFIG_EC_HOST_CMD_BACKEND_SHI_NPCX_ENHANCED_BUF_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

此模式下，除原有 128 字节先进先出缓冲区（FIFO）外，还可选择／切换到一个额外的单字节输出缓冲区，为同时进行的读写事务（simultaneous Read/Write transactions）生成响应。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SHI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
DT_HAS_NUVOTON_NPCX_SHI_ENHANCED_ENABLED
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SIMULATOR"></a>

## 384.11 `CONFIG_EC_HOST_CMD_BACKEND_SIMULATOR`

**提示（Prompt）**：嵌入式控制器主机命令后端模拟器（Backend Simulator）

**说明（Help）**

启用嵌入式控制器（EC）主机命令模拟器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_POSIX && CONFIG_EC_HOST_CMD
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_SOC_POSIX`](P287_soc_native_配置项参考.md#CONFIG_SOC_POSIX)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SPI"></a>

## 384.12 `CONFIG_EC_HOST_CMD_BACKEND_SPI`

**提示（Prompt）**：通过 SPI 支持主机命令（host commands）

**说明（Help）**

启用通过串行外设接口（SPI）传输嵌入式控制器主机命令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SPI_DRIVER"></a>

## 384.13 `CONFIG_EC_HOST_CMD_BACKEND_SPI_DRIVER`

**提示（Prompt）**：串行主机接口驱动（SHI driver）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SPI && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32 if DT_HAS_ST_STM32_SPI_HOST_CMD_ENABLED
```

**可选项（Choices）**

```text
CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SPI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SPI)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32"></a>

## 384.14 `CONFIG_EC_HOST_CMD_BACKEND_SPI_STM32`

**提示（Prompt）**：STM32 串行外设接口（SPI）

**说明（Help）**

启用 STM32 芯片系列中 SPI 后端的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HOST_CMD_BACKEND_SPI_DRIVER>
```

**主动选择（Selects）**

```text
CONFIG_PINCTRL
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 串行主机接口驱动（SHI driver）

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_SPI_DRIVER`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SPI_DRIVER)、[`CONFIG_PINCTRL`](P136_drivers_pinctrl_配置项参考.md#CONFIG_PINCTRL)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_UART"></a>

## 384.15 `CONFIG_EC_HOST_CMD_BACKEND_UART`

**提示（Prompt）**：通过 UART 支持主机命令（host commands）

**说明（Help）**

启用通过通用异步收发器（UART）传输嵌入式控制器主机命令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_UART_TIMEOUT"></a>

## 384.16 `CONFIG_EC_HOST_CMD_BACKEND_UART_TIMEOUT`

**提示（Prompt）**：等待消息剩余部分的超时时间（毫秒）

**说明（Help）**

主机可以分块发送消息。此配置指定 UART 后端收到首个数据块后，等待消息剩余部分的时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD_BACKEND_UART && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
150
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:126`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L126)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_BACKEND_UART`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_UART)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_BACKEND_USB"></a>

## 384.17 `CONFIG_EC_HOST_CMD_BACKEND_USB`

**提示（Prompt）**：通过 USB 支持主机命令（host commands）

**说明（Help）**

启用通过 USB 传输嵌入式控制器主机命令的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_USB_DEVICE_STACK_NEXT && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/backends/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/backends/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_DEDICATED_THREAD"></a>

## 384.18 `CONFIG_EC_HOST_CMD_DEDICATED_THREAD`

**提示（Prompt）**：为主机命令创建新任务（task）

**说明（Help）**

由 `ec_host_cmd_init` 创建专门处理主机命令（Host Command）的新线程；否则，必须在另一个线程内调用 `ec_host_cmd_task`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_BUFFER_ALIGN"></a>

## 384.19 `CONFIG_EC_HOST_CMD_HANDLER_BUFFER_ALIGN`

**提示（Prompt）**：发送／接收缓冲区的内存对齐（tx/rx alignment）

**说明（Help）**

某些接口需要特殊的内存对齐（memory alignment）才能正常工作，此配置用于指定对齐要求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
CONFIG_DCACHE_LINE_SIZE if CONFIG_DCACHE_LINE_SIZE > 0 && CONFIG_EC_HOST_CMD_BACKEND_USB
4
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_DCACHE_LINE_SIZE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE_LINE_SIZE)、[`CONFIG_EC_HOST_CMD_BACKEND_USB`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_USB)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_PRIO"></a>

## 384.20 `CONFIG_EC_HOST_CMD_HANDLER_PRIO`

**提示（Prompt）**：主机命令任务优先级（task priority）

**说明（Help）**

处理主机命令的内核任务优先级。若优先级过低，即数值过大，主机命令处理程序可能无法及时处理命令，应用处理器（AP）会中止等待响应，导致系统无法正常启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
13
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_DEF"></a>

## 384.21 `CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_DEF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理程序定义公共接收缓冲区（common rx buffer）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y if CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE > 0
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE"></a>

## 384.22 `CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_SIZE`

**提示（Prompt）**：所有 EC 主机命令共享的接收缓冲区（RX buffer）大小，单位为字节。

**说明（Help）**

主机命令处理程序定义的发送缓冲区（TX buffer）大小，单位为字节。某些后端层可以定义自己的缓冲区，此时可将大小设为零，避免重复分配。使用多个后端时，用户必须设为各后端要求中的最大值。

译注：原文将此 TX 帮助文案同时用于 RX 和 TX 缓冲区大小选项；在 RX 选项下，标题与帮助存在差异。这里保留原文描述，配置时请同时核对选项标识与实现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
256 if CONFIG_EC_HOST_CMD_BACKEND_ESPI
0 if CONFIG_EC_HOST_CMD_BACKEND_SHI
544 if CONFIG_EC_HOST_CMD_BACKEND_UART
544 if CONFIG_EC_HOST_CMD_BACKEND_SPI
256
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_ESPI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_ESPI)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD_BACKEND_UART`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_UART)、[`CONFIG_EC_HOST_CMD_BACKEND_SPI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SPI)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_STACK_SIZE"></a>

## 384.23 `CONFIG_EC_HOST_CMD_HANDLER_STACK_SIZE`

**提示（Prompt）**：EC 主机命令处理线程的栈大小（stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_DEF"></a>

## 384.24 `CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_DEF`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理程序定义公共发送缓冲区（common tx buffer）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y if CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE > 0
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE)。

<a id="CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE"></a>

## 384.25 `CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_SIZE`

**提示（Prompt）**：所有 EC 主机命令共享的发送缓冲区（TX buffer）大小，单位为字节。

**说明（Help）**

主机命令处理程序定义的发送缓冲区（TX buffer）大小，单位为字节。某些后端层可以定义自己的缓冲区，此时可将大小设为零，避免重复分配。使用多个后端时，用户必须设为各后端要求中的最大值。

译注：原文将此 TX 帮助文案同时用于 RX 和 TX 缓冲区大小选项；在 RX 选项下，标题与帮助存在差异。这里保留原文描述，配置时请同时核对选项标识与实现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
0 if CONFIG_EC_HOST_CMD_BACKEND_ESPI
0 if CONFIG_EC_HOST_CMD_BACKEND_SHI
256 if CONFIG_EC_HOST_CMD_BACKEND_UART
552 if CONFIG_EC_HOST_CMD_BACKEND_SPI
256
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_ESPI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_ESPI)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)、[`CONFIG_EC_HOST_CMD_BACKEND_UART`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_UART)、[`CONFIG_EC_HOST_CMD_BACKEND_SPI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SPI)。

<a id="CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT"></a>

## 384.26 `CONFIG_EC_HOST_CMD_INITIALIZE_AT_BOOT`

**提示（Prompt）**：自动初始化主机命令子系统（automatically initialize）

**说明（Help）**

使用选定后端自动初始化主机命令子系统。由选定后端调用 `ec_host_cmd_init`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_INIT_PRIORITY"></a>

## 384.27 `CONFIG_EC_HOST_CMD_INIT_PRIORITY`

**提示（Prompt）**：初始化优先级（Initialization Priority）

**说明（Help）**

主机命令（Host Command）的初始化优先级，必须高于所用后端设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
80
```

**取值范围（Ranges）**

```text
[0, 99]
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS"></a>

## 384.28 `CONFIG_EC_HOST_CMD_IN_PROGRESS_STATUS`

**提示（Prompt）**：保存上一条 IN_PROGRESS 命令的状态

**说明（Help）**

允许保存最近一条曾返回 `EC_HOST_CMD_IN_PROGRESS` 状态的命令的最终状态。可通过 `ec_host_cmd_send_in_progress_status` 获取所保存的状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y if CONFIG_EC_HOST_CMD_BACKEND_SHI
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:109`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L109)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HOST_CMD_BACKEND_SHI`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_BACKEND_SHI)。

<a id="CONFIG_EC_HOST_CMD_LOG_DBG_BUFFERS"></a>

## 384.29 `CONFIG_EC_HOST_CMD_LOG_DBG_BUFFERS`

**提示（Prompt）**：在调试日志级别记录完整参数与响应缓冲区

**说明（Help）**

每条命令均以调试日志级别（debug logging level）记录。此配置决定是否在其他命令参数之外，同时记录完整请求和响应缓冲区。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HC_LOG_LEVEL_DBG && CONFIG_EC_HOST_CMD
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig.logging:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig.logging#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_DBG)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_LOG_SUPPRESSED_INTERVAL_SECS"></a>

## 384.30 `CONFIG_EC_HOST_CMD_LOG_SUPPRESSED_INTERVAL_SECS`

**提示（Prompt）**：受抑制命令的日志记录间隔（suppressed commands）

**说明（Help）**

每隔一个时间区间，记录一次受抑制命令及其被抑制的次数（suppression number）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
3600
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig.logging:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig.logging#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_LOG_SUPPRESSED_NUMBER"></a>

## 384.31 `CONFIG_EC_HOST_CMD_LOG_SUPPRESSED_NUMBER`

**提示（Prompt）**：受抑制命令的最大数量

**说明（Help）**

收到主机命令时，不记录列表中的受抑制命令（suppressed commands）。此项设置可抑制命令的最大数量，设为 `0` 可禁用命令抑制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig.logging:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig.logging#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)。

<a id="CONFIG_EC_HOST_CMD_NOCACHE_BUFFERS"></a>

## 384.32 `CONFIG_EC_HOST_CMD_NOCACHE_BUFFERS`

**提示（Prompt）**：将 RX 和 TX 缓冲区放入 __nocache 段

**说明（Help）**

通信经常使用直接存储器访问（DMA），而 DMA 通常需要不可缓存内存（uncached memory）。此项允许将接收（RX）和发送（TX）缓冲区放入 `__nocache` 段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_DEF || CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_DEF) && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
y if CONFIG_DCACHE && CONFIG_DMA
```

**定义位置（Location）**：[`subsys/mgmt/ec_host_cmd/Kconfig:87`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/ec_host_cmd/Kconfig#L87)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_DEF`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_HANDLER_TX_BUFFER_DEF)、[`CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_DEF`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD_HANDLER_RX_BUFFER_DEF)、[`CONFIG_EC_HOST_CMD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_EC_HOST_CMD)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)。

<a id="CONFIG_FOTA_HTTP"></a>

## 384.33 `CONFIG_FOTA_HTTP`

**提示（Prompt）**：基于HTTP的固件空中升级（Firmware Over-the-Air）。

**说明（Help）**

从 HTTP 服务器下载固件映像，直接写入当前未运行的 MCUboot 槽位（slot），再请求引导加载程序（bootloader）于下次复位时启动该映像。无需特定服务器端协议，任何能够提供文件的 HTTP 服务器均可使用。映像边接收边流式写入闪存，因此其大小不受 RAM 限制。下载后仅检查 MCUboot 头部（header）；MCUboot 会在实际启动映像之前验证其签名（signature）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING && CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_HTTP_CLIENT && CONFIG_FLASH && CONFIG_FLASH_MAP && CONFIG_IMG_MANAGER && CONFIG_MCUBOOT_IMG_MANAGER
```

**主动选择（Selects）**

```text
CONFIG_IMG_ERASE_PROGRESSIVELY
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_HTTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_CLIENT)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_MCUBOOT_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_MCUBOOT_IMG_MANAGER)、[`CONFIG_IMG_ERASE_PROGRESSIVELY`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ERASE_PROGRESSIVELY)。

<a id="CONFIG_FOTA_HTTP_ASYNC"></a>

## 384.34 `CONFIG_FOTA_HTTP_ASYNC`

**提示（Prompt）**：异步下载 API（Asynchronous download API）

**说明（Help）**

提供 `fota_http_download_async()`，在库拥有的工作队列线程（work queue thread）中执行下载。未启用时，不分配该线程及其栈，`fota_http_download_async()` 返回 `-ENOTSUP`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**被选择（Selected by）**

```text
CONFIG_FOTA_HTTP_SHELL
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)、[`CONFIG_FOTA_HTTP_SHELL`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_SHELL)。

<a id="CONFIG_FOTA_HTTP_MAX_REDIRECTS"></a>

## 384.35 `CONFIG_FOTA_HTTP_MAX_REDIRECTS`

**提示（Prompt）**：可跟随的 HTTP 重定向次数上限

**说明（Help）**

最多跟随指定次数的 `301`、`302`、`303`、`307` 和 `308` 响应。设为 `0` 时，将所有重定向（redirects）视为错误。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[0, 10]
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_RECV_BUF_SIZE"></a>

## 384.36 `CONFIG_FOTA_HTTP_RECV_BUF_SIZE`

**提示（Prompt）**：HTTP 接收缓冲区大小（receive buffer size）

**说明（Help）**

保存单次接收的响应头（response headers）和正文数据（body data）的缓冲区大小。较大的缓冲区可减少下载每个映像所需的接收调用次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
2048
```

**取值范围（Ranges）**

```text
[512, 16384]
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_REJECT_DOWNGRADE"></a>

## 384.37 `CONFIG_FOTA_HTTP_REJECT_DOWNGRADE`

**提示（Prompt）**：拒绝比当前运行映像更旧的映像

**说明（Help）**

将下载映像头部中的版本与当前运行映像比较；若版本较旧，则下载失败并擦除该映像。这只是便利性检查；若需要强制执行降级限制，应使用 MCUboot 的防降级选项（downgrade prevention options）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_RESUME"></a>

## 384.38 `CONFIG_FOTA_HTTP_RESUME`

**提示（Prompt）**：恢复中断的下载（Resume interrupted downloads）

**说明（Help）**

在设置子系统（settings）中持久化下载偏移量（offset），使断电或网络错误中断的下载可通过 HTTP Range 请求从停止处继续。服务器若忽略 Range 头部，则从零重新传输。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STREAM_FLASH_PROGRESS && CONFIG_FOTA_HTTP
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_PROGRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH_PROGRESS)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_RESUME_SAVE_INTERVAL"></a>

## 384.39 `CONFIG_FOTA_HTTP_RESUME_SAVE_INTERVAL`

**提示（Prompt）**：两次进度保存之间写入的字节数

**说明（Help）**

下载失败时也会保存进度，因此本项仅限制断电时丢失的进度数据量。较小的值会更快消耗 settings 存储的写入寿命。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_RESUME && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
65536
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 恢复中断的下载（Resume interrupted downloads）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_RESUME`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_RESUME)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_SHA256_CHECK"></a>

## 384.40 `CONFIG_FOTA_HTTP_SHA256_CHECK`

**提示（Prompt）**：下载后验证调用者提供的 SHA-256

**说明（Help）**

将闪存内容与 `fota_http_download_params` 中传入的摘要（digest）比较；若不匹配，则擦除映像。这可在重启前检测传输损坏，但不能代替 MCUboot 签名验证（signature check）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**主动选择（Selects）**

```text
CONFIG_IMG_ENABLE_IMAGE_CHECK
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)、[`CONFIG_IMG_ENABLE_IMAGE_CHECK`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ENABLE_IMAGE_CHECK)。

<a id="CONFIG_FOTA_HTTP_SHELL"></a>

## 384.41 `CONFIG_FOTA_HTTP_SHELL`

**提示（Prompt）**：FOTA HTTP 命令行命令（shell commands）

**说明（Help）**

注册 `fota` 命令行命令，包含 `download`、`cancel`、`apply`、`confirm`、`status` 和 `erase` 子命令。下载在库的线程中执行，因此不依赖命令行线程的栈大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_FOTA_HTTP_ASYNC
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)、[`CONFIG_FOTA_HTTP_ASYNC`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_ASYNC)。

<a id="CONFIG_FOTA_HTTP_THREAD_PRIORITY"></a>

## 384.42 `CONFIG_FOTA_HTTP_THREAD_PRIORITY`

**提示（Prompt）**：下载线程优先级（thread priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_ASYNC && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 异步下载 API（Asynchronous download API）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_ASYNC`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_ASYNC)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_THREAD_STACK_SIZE"></a>

## 384.43 `CONFIG_FOTA_HTTP_THREAD_STACK_SIZE`

**提示（Prompt）**：下载线程栈大小（thread stack size）

**说明（Help）**

执行 `fota_http_download_async()` 的线程栈大小。传输层安全协议（TLS）握手需要较大的值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_ASYNC && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
8192 if CONFIG_FOTA_HTTP_TLS
4096
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 异步下载 API（Asynchronous download API）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_ASYNC`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_ASYNC)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)、[`CONFIG_FOTA_HTTP_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS)。

<a id="CONFIG_FOTA_HTTP_TIMEOUT_MS"></a>

## 384.44 `CONFIG_FOTA_HTTP_TIMEOUT_MS`

**提示（Prompt）**：HTTP 请求超时（毫秒，request timeout）

**说明（Help）**

整个传输过程的超时时间，不是单个分片的超时。应按实际使用的最慢链路传输预期最大映像所需时间设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
60000
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_TLS"></a>

## 384.45 `CONFIG_FOTA_HTTP_TLS`

**提示（Prompt）**：允许 HTTPS URL

**说明（Help）**

接受 HTTPS URL。首次下载前，使用 `fota_http_tls_add_ca()` 注册证书颁发机构（CA）证书，或通过 `tls_credential_add()` 将其注册到 `FOTA_HTTP_TLS_SEC_TAG` 下。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_FOTA_HTTP
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_TLS_PEER_VERIFY"></a>

## 384.46 `CONFIG_FOTA_HTTP_TLS_PEER_VERIFY`

**提示（Prompt）**：TLS 对端验证级别（peer verification level）

**说明（Help）**

`0` 禁用验证，`1` 表示可选验证，`2` 要求验证。较低值允许接受无法认证的服务器，使任何能够重定向连接的人都有机会安装自己的固件。生产环境应保持为 `2`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_TLS && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 2]
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 允许 HTTPS URL

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_TLS_SEC_TAG"></a>

## 384.47 `CONFIG_FOTA_HTTP_TLS_SEC_TAG`

**提示（Prompt）**：TLS 安全标签（security tag）

**说明（Help）**

用于注册 CA 证书以及可选客户端证书和密钥的安全标签（security tag）。每次下载也可改用自行传入的标签列表。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_TLS && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 允许 HTTPS URL

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_FOTA_HTTP_TLS_VERSION"></a>

## 384.48 `CONFIG_FOTA_HTTP_TLS_VERSION`

**提示（Prompt）**：TLS 协议版本（protocol version）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP_TLS && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
CONFIG_FOTA_HTTP_TLS_VERSION_1_2
```

**可选项（Choices）**

```text
CONFIG_FOTA_HTTP_TLS_VERSION_1_2
CONFIG_FOTA_HTTP_TLS_VERSION_1_3
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 允许 HTTPS URL

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS)、[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)、[`CONFIG_FOTA_HTTP_TLS_VERSION_1_2`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS_VERSION_1_2)、[`CONFIG_FOTA_HTTP_TLS_VERSION_1_3`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS_VERSION_1_3)。

<a id="CONFIG_FOTA_HTTP_TLS_VERSION_1_2"></a>

## 384.49 `CONFIG_FOTA_HTTP_TLS_VERSION_1_2`

**提示（Prompt）**：TLS 1.2 版本

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_TLS_VERSION>
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 允许 HTTPS URL → TLS 协议版本（protocol version）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_TLS_VERSION`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS_VERSION)。

<a id="CONFIG_FOTA_HTTP_TLS_VERSION_1_3"></a>

## 384.50 `CONFIG_FOTA_HTTP_TLS_VERSION_1_3`

**提示（Prompt）**：TLS 1.3 版本

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_3 && <choice CONFIG_FOTA_HTTP_TLS_VERSION>
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 允许 HTTPS URL → TLS 协议版本（protocol version）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_3`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_3)、[`CONFIG_FOTA_HTTP_TLS_VERSION`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP_TLS_VERSION)。

<a id="CONFIG_FOTA_HTTP_URL_MAX_LEN"></a>

## 384.51 `CONFIG_FOTA_HTTP_URL_MAX_LEN`

**提示（Prompt）**：URL 最大长度（Maximum URL length）

**说明（Help）**

可接受的最长 URL，包括所有重定向目标（redirect targets）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[64, 1024]
```

**定义位置（Location）**：[`subsys/mgmt/fota_http/Kconfig:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/fota_http/Kconfig#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_FOTA_HTTP)。

<a id="CONFIG_HAWKBIT"></a>

## 384.52 `CONFIG_HAWKBIT`

**提示（Prompt）**：Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**说明（Help）**

hawkBit 是不限定业务领域的后端框架（back-end framework），通过轮询向资源受限的边缘设备，以及连接到基于 IP 的网络基础设施的较强控制器和网关分发软件更新。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_FLASH && CONFIG_REBOOT && CONFIG_NET_TCP && CONFIG_NET_SOCKETS && CONFIG_IMG_MANAGER && CONFIG_NETWORKING && CONFIG_HTTP_CLIENT && CONFIG_JSON_LIBRARY && (CONFIG_BOOTLOADER_MCUBOOT || CONFIG_TFM_BL2) && CONFIG_SMF && CONFIG_SMF_ANCESTOR_SUPPORT && !CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP && !CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT
```

**主动选择（Selects）**

```text
CONFIG_MPU_ALLOW_FLASH_WRITE if CONFIG_ARM_MPU
CONFIG_IMG_ENABLE_IMAGE_CHECK
CONFIG_IMG_ERASE_PROGRESSIVELY
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS)、[`CONFIG_IMG_MANAGER`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_MANAGER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_HTTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_CLIENT)、[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_BOOTLOADER_MCUBOOT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_BOOTLOADER_MCUBOOT)、[`CONFIG_TFM_BL2`](P252_modules_trusted-firmware-m_配置项参考.md#CONFIG_TFM_BL2)、[`CONFIG_SMF`](P198_lib_配置项参考_2.md#CONFIG_SMF)、[`CONFIG_SMF_ANCESTOR_SUPPORT`](P198_lib_配置项参考_2.md#CONFIG_SMF_ANCESTOR_SUPPORT)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP)、[`CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTLOADER_MODE_DIRECT_XIP_WITH_REVERT)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)、[`CONFIG_ARM_MPU`](P032_arch_common_配置项参考.md#CONFIG_ARM_MPU)、[`CONFIG_IMG_ENABLE_IMAGE_CHECK`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ENABLE_IMAGE_CHECK)、[`CONFIG_IMG_ERASE_PROGRESSIVELY`](P339_subsys_dfu_配置项参考.md#CONFIG_IMG_ERASE_PROGRESSIVELY)。

<a id="CONFIG_HAWKBIT_AUTOHANDLER"></a>

## 384.53 `CONFIG_HAWKBIT_AUTOHANDLER`

**提示（Prompt）**：hawkBit 自动处理程序（autohandler）

**说明（Help）**

启用自动处理程序（autohandler），自动处理更新过程。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_EVENTS
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_EVENTS`](P001_kernel_配置项参考_1.md#CONFIG_EVENTS)。

<a id="CONFIG_HAWKBIT_CERT_TAG"></a>

## 384.54 `CONFIG_HAWKBIT_CERT_TAG`

**提示（Prompt）**：hawkBit 证书标签（certificate tag）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_USE_TLS && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
CONFIG_HAWKBIT_USE_STATIC_CERT_TAG
```

**可选项（Choices）**

```text
CONFIG_HAWKBIT_USE_STATIC_CERT_TAG
CONFIG_HAWKBIT_USE_DYNAMIC_CERT_TAG
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 使用 TLS 连接 hawkBit 服务器

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_USE_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_TLS)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_HAWKBIT_USE_STATIC_CERT_TAG`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_STATIC_CERT_TAG)、[`CONFIG_HAWKBIT_USE_DYNAMIC_CERT_TAG`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_DYNAMIC_CERT_TAG)。

<a id="CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT"></a>

## 384.55 `CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT`

**提示（Prompt）**：在 hawkBit 初始化时确认启动映像（boot image）

**说明（Help）**

在 hawkBit 初始化时自动确认当前启动映像。设为 false 时，由应用负责确认映像（image confirmation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES"></a>

## 384.56 `CONFIG_HAWKBIT_CUSTOM_ATTRIBUTES`

**提示（Prompt）**：自定义设备属性（Custom device attributes）

**说明（Help）**

使用自定义设备属性（device attributes）定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_CUSTOM_DEVICE_ID"></a>

## 384.57 `CONFIG_HAWKBIT_CUSTOM_DEVICE_ID`

**提示（Prompt）**：通过回调函数自定义设备 ID

**说明（Help）**

通过配置回调函数（callback function），在运行时将设备 ID 自定义为所需值。参见 `hawkbit_set_device_identity_cb`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_DEVICE_ID_SOURCE>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 设备 ID 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_DEVICE_ID_SOURCE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DEVICE_ID_SOURCE)。

<a id="CONFIG_HAWKBIT_DDI_GATEWAY_SECURITY"></a>

## 384.58 `CONFIG_HAWKBIT_DDI_GATEWAY_SECURITY`

**提示（Prompt）**：使用网关安全令牌认证（gateway security token authentication）

**说明（Help）**

为 hawkBit 直接设备集成（DDI）API 使用网关安全令牌认证。相同租户（tenant）下的所有设备共享此安全令牌。设备可在首次连接 hawkBit 服务器时自行注册，使用此认证模式前不必预先在服务器注册设备。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_DDI_SECURITY>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:114`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L114)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit DDI API 认证模式（authentication modes）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_DDI_SECURITY`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DDI_SECURITY)。

<a id="CONFIG_HAWKBIT_DDI_SECURITY"></a>

## 384.59 `CONFIG_HAWKBIT_DDI_SECURITY`

**提示（Prompt）**：hawkBit DDI API 认证模式（authentication modes）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
CONFIG_HAWKBIT_DDI_TARGET_SECURITY
```

**可选项（Choices）**

```text
CONFIG_HAWKBIT_DDI_TARGET_SECURITY
CONFIG_HAWKBIT_DDI_GATEWAY_SECURITY
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_HAWKBIT_DDI_TARGET_SECURITY`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DDI_TARGET_SECURITY)、[`CONFIG_HAWKBIT_DDI_GATEWAY_SECURITY`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DDI_GATEWAY_SECURITY)。

<a id="CONFIG_HAWKBIT_DDI_SECURITY_TOKEN"></a>

## 384.60 `CONFIG_HAWKBIT_DDI_SECURITY_TOKEN`

**提示（Prompt）**：认证安全令牌（Authentication security token）

**说明（Help）**

供所配置的 hawkBit DDI 认证模式使用的安全令牌（security token）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_DDI_TARGET_SECURITY"></a>

## 384.61 `CONFIG_HAWKBIT_DDI_TARGET_SECURITY`

**提示（Prompt）**：使用目标安全令牌认证（target security token authentication）

**说明（Help）**

为 hawkBit DDI API 使用目标安全令牌认证。每个设备的安全令牌唯一，在设备注册过程中生成。因此，使用此认证模式前，设备必须已经在 hawkBit 服务器注册。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_DDI_SECURITY>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit DDI API 认证模式（authentication modes）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_DDI_SECURITY`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DDI_SECURITY)。

<a id="CONFIG_HAWKBIT_DEVICE_ID_MAX_LENGTH"></a>

## 384.62 `CONFIG_HAWKBIT_DEVICE_ID_MAX_LENGTH`

**提示（Prompt）**：设备 ID 最大长度（Maximum length）

**说明（Help）**

设备 ID 的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_CUSTOM_DEVICE_ID && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 128]
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_CUSTOM_DEVICE_ID`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_DEVICE_ID_SOURCE"></a>

## 384.63 `CONFIG_HAWKBIT_DEVICE_ID_SOURCE`

**提示（Prompt）**：hawkBit 设备 ID 来源（Source）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**可选项（Choices）**

```text
CONFIG_HAWKBIT_HWINFO_DEVICE_ID
CONFIG_HAWKBIT_CUSTOM_DEVICE_ID
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_HAWKBIT_HWINFO_DEVICE_ID`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_HWINFO_DEVICE_ID)、[`CONFIG_HAWKBIT_CUSTOM_DEVICE_ID`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_CUSTOM_DEVICE_ID)。

<a id="CONFIG_HAWKBIT_DOMAIN_NAME_MAX_LEN"></a>

## 384.64 `CONFIG_HAWKBIT_DOMAIN_NAME_MAX_LEN`

**提示（Prompt）**：存储域名字符串的缓冲区大小

**说明（Help）**

用于保存域名字符串（domain name string）的内部缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_USE_DOMAIN_NAME && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
CONFIG_DNS_RESOLVER_MAX_QUERY_LEN if CONFIG_DNS_RESOLVER
255
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 在运行时设置 hawkBit 配置（settings） → 使用 server_domain 而非 server_addr 提供域名

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_USE_DOMAIN_NAME`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_DOMAIN_NAME)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_DNS_RESOLVER_MAX_QUERY_LEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER_MAX_QUERY_LEN)、[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)。

<a id="CONFIG_HAWKBIT_ERASE_SECOND_SLOT_ON_CONFIRM"></a>

## 384.65 `CONFIG_HAWKBIT_ERASE_SECOND_SLOT_ON_CONFIRM`

**提示（Prompt）**：确认启动映像后擦除第二槽位（second slot）

**说明（Help）**

在 hawkBit 初始化阶段确认当前启动映像后，擦除第二映像槽位分区（image slot partition）的内容。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:261`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L261)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 在 hawkBit 初始化时确认启动映像（boot image）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_CONFIRM_IMG_ON_INIT)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_EVENT_CALLBACKS"></a>

## 384.66 `CONFIG_HAWKBIT_EVENT_CALLBACKS`

**提示（Prompt）**：设置 hawkBit 事件回调（event callbacks）

**说明（Help）**

允许为 hawkBit 设置事件回调（event callbacks）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_HWINFO_DEVICE_ID"></a>

## 384.67 `CONFIG_HAWKBIT_HWINFO_DEVICE_ID`

**提示（Prompt）**：通过硬件信息（HWINFO）模块获取设备 ID

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HWINFO && <choice CONFIG_HAWKBIT_DEVICE_ID_SOURCE>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 设备 ID 来源（Source）

**配置项引用（Symbol References）**：[`CONFIG_HWINFO`](P103_drivers_hwinfo_配置项参考.md#CONFIG_HWINFO)、[`CONFIG_HAWKBIT_DEVICE_ID_SOURCE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_DEVICE_ID_SOURCE)。

<a id="CONFIG_HAWKBIT_POLL_INTERVAL"></a>

## 384.68 `CONFIG_HAWKBIT_POLL_INTERVAL`

**提示（Prompt）**：轮询间隔（分钟，poll interval）

**说明（Help）**

设置轮询 hawkBit 更新服务器的间隔。原文给出的时间范围为 0 至 43200 分钟，即 30 天；hawkBit 服务器设置中配置的值会覆盖此值。译注：原文写作 “zero and 43200”，此处按区间上下限表达。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 43200]
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_PORT"></a>

## 384.69 `CONFIG_HAWKBIT_PORT`

**提示（Prompt）**：hawkBit 服务器端口号（port number）

**说明（Help）**

配置 hawkBit 端口号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
8080
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_REBOOT_COLD"></a>

## 384.70 `CONFIG_HAWKBIT_REBOOT_COLD`

**提示（Prompt）**：更新后冷重启（Cold reboot）

**说明（Help）**

更新后执行冷重启（cold reboot）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_REBOOT_MODE>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 更新后重启模式（Reboot mode）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_REBOOT_MODE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_MODE)。

<a id="CONFIG_HAWKBIT_REBOOT_MODE"></a>

## 384.71 `CONFIG_HAWKBIT_REBOOT_MODE`

**提示（Prompt）**：更新后重启模式（Reboot mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
CONFIG_HAWKBIT_REBOOT_WARM
```

**可选项（Choices）**

```text
CONFIG_HAWKBIT_REBOOT_WARM
CONFIG_HAWKBIT_REBOOT_COLD
CONFIG_HAWKBIT_REBOOT_NONE
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)、[`CONFIG_HAWKBIT_REBOOT_WARM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_WARM)、[`CONFIG_HAWKBIT_REBOOT_COLD`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_COLD)、[`CONFIG_HAWKBIT_REBOOT_NONE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_NONE)。

<a id="CONFIG_HAWKBIT_REBOOT_NONE"></a>

## 384.72 `CONFIG_HAWKBIT_REBOOT_NONE`

**提示（Prompt）**：更新后不重启

**说明（Help）**

更新后不执行重启。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_REBOOT_MODE>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 更新后重启模式（Reboot mode）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_REBOOT_MODE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_MODE)。

<a id="CONFIG_HAWKBIT_REBOOT_WARM"></a>

## 384.73 `CONFIG_HAWKBIT_REBOOT_WARM`

**提示（Prompt）**：更新后热重启（Warm reboot）

**说明（Help）**

更新后执行热重启（warm reboot）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_REBOOT_MODE>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:206`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L206)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 更新后重启模式（Reboot mode）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_REBOOT_MODE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_REBOOT_MODE)。

<a id="CONFIG_HAWKBIT_SAVE_PROGRESS"></a>

## 384.74 `CONFIG_HAWKBIT_SAVE_PROGRESS`

**提示（Prompt）**：保存 hawkBit 更新下载进度（download progress）

**说明（Help）**

定期保存 hawkBit 更新下载操作的进度。启用后，将进度定期写入非易失性存储（non-volatile storage）；下载中断后，可从最后保存的位置继续，避免从头开始，节省带宽和时间。适用于通过不可靠网络进行大型更新，或资源受限的环境。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_STREAM_FLASH_PROGRESS && CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:234`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L234)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_PROGRESS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH_PROGRESS)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_SAVE_PROGRESS_INTERVAL"></a>

## 384.75 `CONFIG_HAWKBIT_SAVE_PROGRESS_INTERVAL`

**提示（Prompt）**：hawkBit 更新下载进度保存间隔

**说明（Help）**

以百分比设置 hawkBit 下载进度的保存间隔。`0` 表示每下载一个新数据块（chunk）就保存进度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_SAVE_PROGRESS && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 100]
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 保存 hawkBit 更新下载进度（download progress）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_SAVE_PROGRESS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_SAVE_PROGRESS)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_SERVER"></a>

## 384.76 `CONFIG_HAWKBIT_SERVER`

**提示（Prompt）**：用户指定的 hawkBit 服务器地址（server address）

**说明（Help）**

配置 hawkBit 服务器地址。若地址不是 IP 地址，则必须启用 `CONFIG_DNS_RESOLVER`，以解析主机名（hostname）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME"></a>

## 384.77 `CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`

**提示（Prompt）**：在运行时设置 hawkBit 配置（settings）

**说明（Help）**

允许运行时设置 hawkBit 配置（settings）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:81`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L81)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_SHELL"></a>

## 384.78 `CONFIG_HAWKBIT_SHELL`

**提示（Prompt）**：hawkBit 命令行工具（shell utilities）

**说明（Help）**

启用提供 hawkBit 命令的命令行模块（shell module）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_HAWKBIT_AUTOHANDLER && CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 自动处理程序（autohandler）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_HAWKBIT_AUTOHANDLER`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_AUTOHANDLER)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_SHELL_AUTOHANDLER_TIMEOUT"></a>

## 384.79 `CONFIG_HAWKBIT_SHELL_AUTOHANDLER_TIMEOUT`

**提示（Prompt）**：hawkBit 命令行自动处理超时（autohandler timeout）

**说明（Help）**

设置 hawkBit 命令行自动处理程序的超时时间，单位为毫秒。等待期间，它阻塞命令行（shell），等待 hawkBit 自动处理程序完成；此时不会打印命令行日志器的日志消息，因此超时不宜过长，以免丢失日志。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_SHELL && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 自动处理程序（autohandler） → hawkBit 命令行工具（shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_SHELL`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_SHELL)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_STATIC_CERT_TAG"></a>

## 384.80 `CONFIG_HAWKBIT_STATIC_CERT_TAG`

**提示（Prompt）**：静态证书标签（Static certificate tag）

**说明（Help）**

与 hawkBit 服务器建立 TLS 连接时使用的静态证书标签（certificate tag）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_USE_STATIC_CERT_TAG && CONFIG_HAWKBIT_USE_TLS && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 使用 TLS 连接 hawkBit 服务器

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_USE_STATIC_CERT_TAG`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_STATIC_CERT_TAG)、[`CONFIG_HAWKBIT_USE_TLS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_USE_TLS)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_STATUS_BUFFER_SIZE"></a>

## 384.81 `CONFIG_HAWKBIT_STATUS_BUFFER_SIZE`

**提示（Prompt）**：hawkBit 状态缓冲区大小（status buffer size）

**说明（Help）**

设置用于存储待发送至 hawkBit 服务器的 JSON 字符串的缓冲区大小。大量使用自定义属性（custom attributes）时，可能需要增大此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_TENANT"></a>

## 384.82 `CONFIG_HAWKBIT_TENANT`

**提示（Prompt）**：hawkBit 服务器租户名称（Tenant name）

**说明（Help）**

配置 hawkBit 服务器的租户名称（tenant name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
"default"
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_USE_DOMAIN_NAME"></a>

## 384.83 `CONFIG_HAWKBIT_USE_DOMAIN_NAME`

**提示（Prompt）**：使用 server_domain 而非 server_addr 提供域名

**说明（Help）**

允许 TLS 和 HTTP 使用 `server_domain` 字段。启用后，`server_addr` 可接收已经解析的 IP 地址，域名则通过 `server_domain` 提供。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME && CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 在运行时设置 hawkBit 配置（settings）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HAWKBIT_USE_DYNAMIC_CERT_TAG"></a>

## 384.84 `CONFIG_HAWKBIT_USE_DYNAMIC_CERT_TAG`

**提示（Prompt）**：使用动态证书标签（dynamic certificate tag）

**说明（Help）**

与 hawkBit 服务器建立 TLS 连接时，使用动态证书标签（certificate tag）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME && <choice CONFIG_HAWKBIT_CERT_TAG>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:185`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L185)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 使用 TLS 连接 hawkBit 服务器 → hawkBit 证书标签（certificate tag）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_SET_SETTINGS_RUNTIME)、[`CONFIG_HAWKBIT_CERT_TAG`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_CERT_TAG)。

<a id="CONFIG_HAWKBIT_USE_STATIC_CERT_TAG"></a>

## 384.85 `CONFIG_HAWKBIT_USE_STATIC_CERT_TAG`

**提示（Prompt）**：使用静态证书标签（static certificate tag）

**说明（Help）**

与 hawkBit 服务器建立 TLS 连接时，使用静态证书标签（certificate tag）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_CERT_TAG>
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → 使用 TLS 连接 hawkBit 服务器 → hawkBit 证书标签（certificate tag）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_CERT_TAG`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT_CERT_TAG)。

<a id="CONFIG_HAWKBIT_USE_TLS"></a>

## 384.86 `CONFIG_HAWKBIT_USE_TLS`

**提示（Prompt）**：使用 TLS 连接 hawkBit 服务器

**说明（Help）**

使用 TLS 建立 hawkBit 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_HAWKBIT
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_HEAP_MEM_POOL_ADD_SIZE_HAWKBIT"></a>

## 384.87 `CONFIG_HEAP_MEM_POOL_ADD_SIZE_HAWKBIT`

**提示（Prompt）**：hawkBit 堆内存池大小（heap memory pool size）

**说明（Help）**

设置 hawkBit 堆内存池（heap memory pool）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/mgmt/hawkbit/Kconfig:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/hawkbit/Kconfig#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_HAWKBIT)。

<a id="CONFIG_MCUMGR"></a>

## 384.88 `CONFIG_MCUMGR`

**提示（Prompt）**：微控制器管理支持（MCUmgr Support）

**说明（Help）**

启用微控制器管理（MCUmgr）库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF && CONFIG_ZCBOR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)。

<a id="CONFIG_MCUMGR_GRP_ENUM"></a>

## 384.89 `CONFIG_MCUMGR_GRP_ENUM`

**提示（Prompt）**：MCUmgr 枚举管理处理程序（enumeration management handlers）

**说明（Help）**

启用 MCUmgr 枚举管理处理程序（enumeration management handlers），以列出支持的命令组（command groups）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS"></a>

## 384.90 `CONFIG_MCUMGR_GRP_ENUM_DETAILS`

**提示（Prompt）**：组详情命令（Group details command）

**说明（Help）**

实现列出组详情（group details）的功能。注意：此命令的响应可能非常大。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4 if CONFIG_ZCBOR_CANONICAL
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_3`、`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_4`。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE"></a>

## 384.91 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE`

**提示（Prompt）**：缓冲区类型（Buffer type）

**说明（Help）**

选择处理请求时所需的变量使用栈（stack）还是堆（heap）存储。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK
CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_HEAP
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS)、[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK)、[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_HEAP`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_HEAP)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_HEAP"></a>

## 384.92 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_HEAP`

**提示（Prompt）**：堆，动态大小（Heap, dynamic size）

**说明（Help）**

通过 `malloc` 动态分配堆内存。若可用堆内存不足以完成分配，则拒绝请求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE > 0 && <choice CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command） → 缓冲区类型（Buffer type）

**配置项引用（Symbol References）**：[`CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE`](P197_lib_配置项参考_1.md#CONFIG_COMMON_LIBC_MALLOC_ARENA_SIZE)、[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK"></a>

## 384.93 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK`

**提示（Prompt）**：栈，固定大小（Stack, fixed size）

**说明（Help）**

使用固定大小的栈缓冲区，拒绝超过此大小的用户输入值。注意，仅参数存储的栈占用就为 `MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK * 2`，因此应合理设置 MCUmgr 栈大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE>
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command） → 缓冲区类型（Buffer type）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK_ENTRIES"></a>

## 384.94 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK_ENTRIES`

**提示（Prompt）**：列表条目数量上限（Maximum list item entries）

**说明（Help）**

详情命令（details command）支持的列表值数量上限，每个值在栈上占用 2 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK && <choice CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE>
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 65535]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command） → 缓冲区类型（Buffer type） → 栈，固定大小（Stack, fixed size）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE_STACK)、[`CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS_BUFFER_TYPE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_HANDLERS"></a>

## 384.95 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_HANDLERS`

**提示（Prompt）**：在详情响应中包含组名称（group names）

**说明（Help）**

在详情命令（detail command）的响应中包含各组处理程序（handlers）的数量。译注：此选项的原文标题写“包含组名称”，正文及 `HANDLERS` 标识则指处理程序数量；此处保留差异供对照。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS)、[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_HOOK"></a>

## 384.96 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_HOOK`

**提示（Prompt）**：回调钩子（Callback hook）

**说明（Help）**

允许应用向支持的命令组详情响应中添加额外字段（fields）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS && CONFIG_MCUMGR_GRP_ENUM_DETAILS && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS`](P385_subsys_mgmt_配置项参考_2.md#CONFIG_MCUMGR_MGMT_NOTIFICATION_HOOKS)、[`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS)、[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME"></a>

## 384.97 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_NAME`

**提示（Prompt）**：在详情响应中包含组名称（group names）

**说明（Help）**

在详情命令（detail command）的响应中包含组名称。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS)、[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_ENUM_DETAILS_STATES"></a>

## 384.98 `CONFIG_MCUMGR_GRP_ENUM_DETAILS_STATES`

**提示（Prompt）**：每组条目数量的预计上限（Predicted maximum number）

**说明（Help）**

用于定义保存组数据的简洁二进制对象表示（CBOR）映射。此值不影响内存分配，而是供 zcbor 根据预估大小决定映射的编码方式。应在默认值上增加由钩子（hooks）返回的额外字段数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_ENUM_DETAILS && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[3, 32]
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/enum_mgmt/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → 组详情命令（Group details command） → 回调钩子（Callback hook）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_DETAILS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM_DETAILS)、[`CONFIG_MCUMGR_GRP_ENUM`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<a id="CONFIG_MCUMGR_GRP_FS"></a>

## 384.99 `CONFIG_MCUMGR_GRP_FS`

**提示（Prompt）**：MCUmgr 文件管理处理程序（file management handlers）

**说明（Help）**

启用 MCUmgr 文件管理处理程序（file management handlers）。

注意：此功能允许 MCUmgr 客户端访问文件系统中的任何内容，包括应用保存的私钥等秘密信息。强烈不建议在缺少适当保护机制的生产环境中使用。应用可启用 `MCUMGR_GRP_FS_FILE_ACCESS_HOOK` 并注册回调，在尝试访问文件时进行过滤、允许、拒绝或重写路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FILE_SYSTEM && CONFIG_MCUMGR
```

**主动选择（Selects）**

```text
CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers）

**配置项引用（Symbol References）**：[`CONFIG_FILE_SYSTEM`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUMGR_SMP_CBOR_MIN_DECODING_LEVEL_2`。

<a id="CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH"></a>

## 384.100 `CONFIG_MCUMGR_GRP_FS_CHECKSUM_HASH`

**提示（Prompt）**：MCUmgr 校验和／散列功能（Checksum/hash）

**说明（Help）**

支持 MCUmgr 散列／校验和（hash/checksum）功能，具体算法类型还需在下方分别启用。注意：需要足够栈空间来缓冲文件读取数据，并生成输出散列或校验和。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**定义位置（Location）**：[`subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/grp/fs_mgmt/Kconfig#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](P384_subsys_mgmt_配置项参考_1.md#CONFIG_MCUMGR)。

<!-- kconfig-navigation -->

[上一章](P383_subsys_mem_mgmt_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P385_subsys_mgmt_配置项参考_2.md)
