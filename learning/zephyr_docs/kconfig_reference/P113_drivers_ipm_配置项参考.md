---
id: learning.zephyr-docs.kconfig-reference.page-113
title: "`drivers/ipm`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第113章\_`drivers/ipm`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/ipm` 的 70 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ESP32_SOFT_IPM"></a>

## 113.1 `CONFIG_ESP32_SOFT_IPM`

**提示（Prompt）**：ESP32 软件 IPM 驱动

**说明（Help）**

使用非对称多处理（AMP）时 ESP32 的处理器间通信驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_IPM_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM"></a>

## 113.2 `CONFIG_IPM`

**提示（Prompt）**：处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**说明（Help）**

在系统配置中纳入基于中断的处理器间邮箱（IPM）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_RPMSG_SERVICE
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_RPMSG_SERVICE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RPMSG_SERVICE)。

<a id="CONFIG_IPM_CALLBACK_ASYNC"></a>

## 113.3 `CONFIG_IPM_CALLBACK_ASYNC`

**提示（Prompt）**：异步投递回调（Asynchronous Callback Delivery）

**说明（Help）**

选中后，驱动支持“异步”（Asynchronous）命令投递。中断服务例程（ISR）返回后，命令仍保持活动状态，直到应用稍后显式“完成”该命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM
```

**被选择（Selected by）**

```text
CONFIG_IPM_SEDI
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.sedi:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.sedi#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_SEDI`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_SEDI)。

<a id="CONFIG_IPM_IMX"></a>

## 113.4 `CONFIG_IPM_IMX`

**提示（Prompt）**：IMX IPM 驱动

**说明（Help）**

NXP i.MX 消息单元（Messaging Unit）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_IMX_MU_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.imx:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.imx#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_IMX_MAX_DATA_SIZE_16"></a>

## 113.5 `CONFIG_IPM_IMX_MAX_DATA_SIZE_16`

**提示（Prompt）**：16 字节（Bytes）

**说明（Help）**

只有一种消息类型，ID 为 0，最大大小为 16 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.imx:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.imx#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IMX IPM 驱动 → IMX IPM 最大数据大小（Max Data Size）

<a id="CONFIG_IPM_IMX_MAX_DATA_SIZE_4"></a>

## 113.6 `CONFIG_IPM_IMX_MAX_DATA_SIZE_4`

**提示（Prompt）**：4 字节（Bytes）

**说明（Help）**

共有四种消息类型，ID 为 0、1、2 或 3，每种最大大小为 4 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.imx:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.imx#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IMX IPM 驱动 → IMX IPM 最大数据大小（Max Data Size）

<a id="CONFIG_IPM_IMX_MAX_DATA_SIZE_8"></a>

## 113.7 `CONFIG_IPM_IMX_MAX_DATA_SIZE_8`

**提示（Prompt）**：8 字节（Bytes）

**说明（Help）**

共有两种消息类型，ID 为 0 或 1，每种最大大小为 8 字节。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.imx:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.imx#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IMX IPM 驱动 → IMX IPM 最大数据大小（Max Data Size）

<a id="CONFIG_IPM_IVSHMEM"></a>

## 113.8 `CONFIG_IPM_IVSHMEM`

**提示（Prompt）**：基于 IVSHMEM-Doorbell 的 IPM 驱动

**说明（Help）**

使用 IVSHMEM 门铃（Doorbell）机制的处理器间通信驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LINARO_IVSHMEM_IPM_ENABLED && CONFIG_IVSHMEM && CONFIG_IVSHMEM_DOORBELL && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM)、[`CONFIG_IVSHMEM_DOORBELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_DOORBELL)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_IVSHMEM_EVENT_LOOP_PRIO"></a>

## 113.9 `CONFIG_IPM_IVSHMEM_EVENT_LOOP_PRIO`

**提示（Prompt）**：IVSHMEM IPM 事件循环任务优先级（Event Loop Task Priority）

**说明（Help）**

调整 IVSHMEM 事件循环任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_IVSHMEM && CONFIG_IPM
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.ivshmem:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.ivshmem#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM_IVSHMEM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_IVSHMEM)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_IVSHMEM_EVENT_LOOP_STACK_SIZE"></a>

## 113.10 `CONFIG_IPM_IVSHMEM_EVENT_LOOP_STACK_SIZE`

**提示（Prompt）**：IVSHMEM IPM 事件循环任务栈大小，单位为字节

**说明（Help）**

调整 IVSHMEM 事件循环任务的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_IVSHMEM && CONFIG_IPM
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.ivshmem:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.ivshmem#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM_IVSHMEM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_IVSHMEM)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MAX_DATA_SIZE"></a>

## 113.11 `CONFIG_IPM_MAX_DATA_SIZE`

**提示（Prompt）**：支持的最大数据大小（Max Data Size）

**说明（Help）**

定义 IPM 设备可发送或接收数据的最大大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM
```

**默认值（Defaults）**

```text
0 if CONFIG_IPM_STM32_IPCC || CONFIG_IPM_STM32_HSEM
1024
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_STM32_IPCC`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_STM32_IPCC)、[`CONFIG_IPM_STM32_HSEM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_STM32_HSEM)。

<a id="CONFIG_IPM_MBOX"></a>

## 113.12 `CONFIG_IPM_MBOX`

**提示（Prompt）**：基于 MBOX 的 IPM 驱动

**说明（Help）**

使用邮箱（MBOX）驱动作为后端机制（Backend Mechanism）的 IPM 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_MBOX_IPM_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_MBOX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MBOX)。

<a id="CONFIG_IPM_MCUX"></a>

## 113.13 `CONFIG_IPM_MCUX`

**提示（Prompt）**：MCUX IPM 驱动

**说明（Help）**

MCUX 邮箱（Mailbox）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_LPC_MAILBOX_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_RESET
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.imx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.imx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_RESET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RESET)。

<a id="CONFIG_IPM_MHU"></a>

## 113.14 `CONFIG_IPM_MHU`

**提示（Prompt）**：IPM MHU 驱动

**说明（Help）**

SSE 200 消息处理单元（Message Handling Unit，MHU）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_MHU_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_0_ENABLE"></a>

## 113.15 `CONFIG_IPM_MSG_CH_0_ENABLE`

**提示（Prompt）**：IPM 消息通道（Message Channel）0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [0] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_0_RX"></a>

## 113.16 `CONFIG_IPM_MSG_CH_0_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_0_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [0] 配置。 → IPM 消息通道（Message Channel）0

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_0_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_0_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_0_TX"></a>

## 113.17 `CONFIG_IPM_MSG_CH_0_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_0_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_0_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [0] 配置。 → IPM 消息通道（Message Channel）0

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_0_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_0_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_0_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_0_RX)。

<a id="CONFIG_IPM_MSG_CH_10_ENABLE"></a>

## 113.18 `CONFIG_IPM_MSG_CH_10_ENABLE`

**提示（Prompt）**：IPM 消息通道 10

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [10] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_10_RX"></a>

## 113.19 `CONFIG_IPM_MSG_CH_10_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_10_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [10] 配置。 → IPM 消息通道 10

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_10_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_10_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_10_TX"></a>

## 113.20 `CONFIG_IPM_MSG_CH_10_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_10_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_10_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [10] 配置。 → IPM 消息通道 10

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_10_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_10_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_10_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_10_RX)。

<a id="CONFIG_IPM_MSG_CH_11_ENABLE"></a>

## 113.21 `CONFIG_IPM_MSG_CH_11_ENABLE`

**提示（Prompt）**：IPM 消息通道 11

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [11] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_11_RX"></a>

## 113.22 `CONFIG_IPM_MSG_CH_11_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_11_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [11] 配置。 → IPM 消息通道 11

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_11_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_11_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_11_TX"></a>

## 113.23 `CONFIG_IPM_MSG_CH_11_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_11_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_11_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [11] 配置。 → IPM 消息通道 11

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_11_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_11_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_11_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_11_RX)。

<a id="CONFIG_IPM_MSG_CH_12_ENABLE"></a>

## 113.24 `CONFIG_IPM_MSG_CH_12_ENABLE`

**提示（Prompt）**：IPM 消息通道 12

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [12] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_12_RX"></a>

## 113.25 `CONFIG_IPM_MSG_CH_12_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_12_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [12] 配置。 → IPM 消息通道 12

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_12_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_12_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_12_TX"></a>

## 113.26 `CONFIG_IPM_MSG_CH_12_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_12_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_12_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [12] 配置。 → IPM 消息通道 12

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_12_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_12_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_12_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_12_RX)。

<a id="CONFIG_IPM_MSG_CH_13_ENABLE"></a>

## 113.27 `CONFIG_IPM_MSG_CH_13_ENABLE`

**提示（Prompt）**：IPM 消息通道 13

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [13] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_13_RX"></a>

## 113.28 `CONFIG_IPM_MSG_CH_13_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_13_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [13] 配置。 → IPM 消息通道 13

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_13_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_13_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_13_TX"></a>

## 113.29 `CONFIG_IPM_MSG_CH_13_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_13_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_13_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [13] 配置。 → IPM 消息通道 13

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_13_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_13_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_13_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_13_RX)。

<a id="CONFIG_IPM_MSG_CH_14_ENABLE"></a>

## 113.30 `CONFIG_IPM_MSG_CH_14_ENABLE`

**提示（Prompt）**：IPM 消息通道 14

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [14] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_14_RX"></a>

## 113.31 `CONFIG_IPM_MSG_CH_14_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_14_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [14] 配置。 → IPM 消息通道 14

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_14_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_14_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_14_TX"></a>

## 113.32 `CONFIG_IPM_MSG_CH_14_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_14_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_14_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [14] 配置。 → IPM 消息通道 14

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_14_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_14_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_14_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_14_RX)。

<a id="CONFIG_IPM_MSG_CH_15_ENABLE"></a>

## 113.33 `CONFIG_IPM_MSG_CH_15_ENABLE`

**提示（Prompt）**：IPM 消息通道 15

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [15] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_15_RX"></a>

## 113.34 `CONFIG_IPM_MSG_CH_15_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_15_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [15] 配置。 → IPM 消息通道 15

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_15_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_15_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_15_TX"></a>

## 113.35 `CONFIG_IPM_MSG_CH_15_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_15_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_15_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [15] 配置。 → IPM 消息通道 15

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_15_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_15_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_15_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_15_RX)。

<a id="CONFIG_IPM_MSG_CH_1_ENABLE"></a>

## 113.36 `CONFIG_IPM_MSG_CH_1_ENABLE`

**提示（Prompt）**：IPM 消息通道 1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [1] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_1_RX"></a>

## 113.37 `CONFIG_IPM_MSG_CH_1_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_1_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [1] 配置。 → IPM 消息通道 1

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_1_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_1_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_1_TX"></a>

## 113.38 `CONFIG_IPM_MSG_CH_1_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_1_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_1_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [1] 配置。 → IPM 消息通道 1

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_1_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_1_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_1_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_1_RX)。

<a id="CONFIG_IPM_MSG_CH_2_ENABLE"></a>

## 113.39 `CONFIG_IPM_MSG_CH_2_ENABLE`

**提示（Prompt）**：IPM 消息通道 2

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [2] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_2_RX"></a>

## 113.40 `CONFIG_IPM_MSG_CH_2_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_2_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [2] 配置。 → IPM 消息通道 2

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_2_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_2_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_2_TX"></a>

## 113.41 `CONFIG_IPM_MSG_CH_2_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_2_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_2_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [2] 配置。 → IPM 消息通道 2

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_2_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_2_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_2_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_2_RX)。

<a id="CONFIG_IPM_MSG_CH_3_ENABLE"></a>

## 113.42 `CONFIG_IPM_MSG_CH_3_ENABLE`

**提示（Prompt）**：IPM 消息通道 3

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [3] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_3_RX"></a>

## 113.43 `CONFIG_IPM_MSG_CH_3_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_3_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [3] 配置。 → IPM 消息通道 3

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_3_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_3_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_3_TX"></a>

## 113.44 `CONFIG_IPM_MSG_CH_3_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_3_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_3_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [3] 配置。 → IPM 消息通道 3

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_3_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_3_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_3_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_3_RX)。

<a id="CONFIG_IPM_MSG_CH_4_ENABLE"></a>

## 113.45 `CONFIG_IPM_MSG_CH_4_ENABLE`

**提示（Prompt）**：IPM 消息通道 4

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [4] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_4_RX"></a>

## 113.46 `CONFIG_IPM_MSG_CH_4_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_4_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [4] 配置。 → IPM 消息通道 4

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_4_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_4_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_4_TX"></a>

## 113.47 `CONFIG_IPM_MSG_CH_4_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_4_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_4_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [4] 配置。 → IPM 消息通道 4

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_4_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_4_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_4_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_4_RX)。

<a id="CONFIG_IPM_MSG_CH_5_ENABLE"></a>

## 113.48 `CONFIG_IPM_MSG_CH_5_ENABLE`

**提示（Prompt）**：IPM 消息通道 5

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [5] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_5_RX"></a>

## 113.49 `CONFIG_IPM_MSG_CH_5_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_5_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [5] 配置。 → IPM 消息通道 5

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_5_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_5_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_5_TX"></a>

## 113.50 `CONFIG_IPM_MSG_CH_5_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_5_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_5_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [5] 配置。 → IPM 消息通道 5

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_5_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_5_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_5_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_5_RX)。

<a id="CONFIG_IPM_MSG_CH_6_ENABLE"></a>

## 113.51 `CONFIG_IPM_MSG_CH_6_ENABLE`

**提示（Prompt）**：IPM 消息通道 6

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [6] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_6_RX"></a>

## 113.52 `CONFIG_IPM_MSG_CH_6_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_6_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [6] 配置。 → IPM 消息通道 6

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_6_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_6_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_6_TX"></a>

## 113.53 `CONFIG_IPM_MSG_CH_6_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_6_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_6_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [6] 配置。 → IPM 消息通道 6

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_6_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_6_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_6_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_6_RX)。

<a id="CONFIG_IPM_MSG_CH_7_ENABLE"></a>

## 113.54 `CONFIG_IPM_MSG_CH_7_ENABLE`

**提示（Prompt）**：IPM 消息通道 7

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [7] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_7_RX"></a>

## 113.55 `CONFIG_IPM_MSG_CH_7_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_7_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [7] 配置。 → IPM 消息通道 7

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_7_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_7_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_7_TX"></a>

## 113.56 `CONFIG_IPM_MSG_CH_7_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_7_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_7_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [7] 配置。 → IPM 消息通道 7

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_7_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_7_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_7_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_7_RX)。

<a id="CONFIG_IPM_MSG_CH_8_ENABLE"></a>

## 113.57 `CONFIG_IPM_MSG_CH_8_ENABLE`

**提示（Prompt）**：IPM 消息通道 8

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [8] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_8_RX"></a>

## 113.58 `CONFIG_IPM_MSG_CH_8_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_8_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [8] 配置。 → IPM 消息通道 8

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_8_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_8_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_8_TX"></a>

## 113.59 `CONFIG_IPM_MSG_CH_8_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_8_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_8_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [8] 配置。 → IPM 消息通道 8

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_8_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_8_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_8_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_8_RX)。

<a id="CONFIG_IPM_MSG_CH_9_ENABLE"></a>

## 113.60 `CONFIG_IPM_MSG_CH_9_ENABLE`

**提示（Prompt）**：IPM 消息通道 9

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [9] 配置。

**配置项引用（Symbol References）**：[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_9_RX"></a>

## 113.61 `CONFIG_IPM_MSG_CH_9_RX`

**提示（Prompt）**：IPM 消息接收通道（RX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_9_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [9] 配置。 → IPM 消息通道 9

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_9_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_9_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_MSG_CH_9_TX"></a>

## 113.62 `CONFIG_IPM_MSG_CH_9_TX`

**提示（Prompt）**：IPM 消息发送通道（TX Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_MSG_CH_9_ENABLE && CONFIG_IPM_NRFX && CONFIG_IPM
```

**默认值（Defaults）**

```text
!CONFIG_IPM_MSG_CH_9_RX
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.nrfx_ipc_channel:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.nrfx_ipc_channel#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → IPM 消息通道 [9] 配置。 → IPM 消息通道 9

**配置项引用（Symbol References）**：[`CONFIG_IPM_MSG_CH_9_ENABLE`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_9_ENABLE)、[`CONFIG_IPM_NRFX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_NRFX)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_MSG_CH_9_RX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MSG_CH_9_RX)。

<a id="CONFIG_IPM_NRFX"></a>

## 113.63 `CONFIG_IPM_NRFX`

**提示（Prompt）**：IPM NRF 驱动

**说明（Help）**

Nordic nRF 消息单元（Messaging Unit）的驱动，基于 nRF IPC 外设硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_IPC_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_IPC
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_NRFX_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_IPC)。

<a id="CONFIG_IPM_NRF_SINGLE_INSTANCE"></a>

## 113.64 `CONFIG_IPM_NRF_SINGLE_INSTANCE`

**提示（Prompt）**：IPM 设备单实例（Single Instance）

**说明（Help）**

如果 IPM 设备应只有一个实例，而非每个 IPC 消息通道各有一个实例，请启用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_SEDI"></a>

## 113.65 `CONFIG_IPM_SEDI`

**提示（Prompt）**：Intel SEDI IPM 驱动

**说明（Help）**

此选项启用 Intel SEDI IPM（IPC）驱动。该驱动只是构建在 `hal-intel` 模块中 SEDI 裸机（Bare Metal）IPC 驱动之上的适配层驱动（Shim Driver）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM
```

**默认值（Defaults）**

```text
y if DT_HAS_INTEL_SEDI_IPM_ENABLED
```

**主动选择（Selects）**

```text
CONFIG_IPM_CALLBACK_ASYNC
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.sedi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.sedi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)、[`CONFIG_IPM_CALLBACK_ASYNC`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_CALLBACK_ASYNC)。

<a id="CONFIG_IPM_STM32_HSEM"></a>

## 113.66 `CONFIG_IPM_STM32_HSEM`

**提示（Prompt）**：STM32 HSEM 控制器

**说明（Help）**

STM32 硬件信号量（HSEM）邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_HSEM_MAILBOX_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.stm32:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.stm32#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_STM32_HSEM_CPU"></a>

## 113.67 `CONFIG_IPM_STM32_HSEM_CPU`

**提示（Prompt）**：HSEM CPU ID

**说明（Help）**

用于定义 HSEM 所用的 CPU ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_STM32_HSEM && CONFIG_IPM
```

**默认值（Defaults）**

```text
1 if n
2 if n
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.stm32:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.stm32#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → STM32 HSEM 控制器

**配置项引用（Symbol References）**：[`CONFIG_IPM_STM32_HSEM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_STM32_HSEM)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_STM32_IPCC"></a>

## 113.68 `CONFIG_IPM_STM32_IPCC`

**提示（Prompt）**：STM32 IPCC 控制器

**说明（Help）**

STM32 处理器间通信控制器（IPCC）邮箱的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32_IPCC_MAILBOX_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.stm32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.stm32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_IPM_STM32_IPCC_PROCID"></a>

## 113.69 `CONFIG_IPM_STM32_IPCC_PROCID`

**提示（Prompt）**：STM32 IPCC 处理器 ID（Processor ID）

**说明（Help）**

用于定义访问 IPCC 所用的处理器 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IPM_STM32_IPCC && CONFIG_IPM
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 2]
```

**定义位置（Location）**：[`drivers/ipm/Kconfig.stm32:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig.stm32#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动 → STM32 IPCC 控制器

**配置项引用（Symbol References）**：[`CONFIG_IPM_STM32_IPCC`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_STM32_IPCC)、[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<a id="CONFIG_XLNX_IPI"></a>

## 113.70 `CONFIG_XLNX_IPI`

**提示（Prompt）**：AMD-Xilinx IPM 驱动

**说明（Help）**

用于 ZynqMP Ultrascale+ 等 AMD-Xilinx 平台的处理器间中断（Inter Processor Interrupt）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_ZYNQMP_IPI_MAILBOX_ENABLED && CONFIG_IPM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ipm/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ipm/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 处理器间邮箱（Inter-Processor Mailbox，IPM）驱动

**配置项引用（Symbol References）**：[`CONFIG_IPM`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM)。

<!-- kconfig-navigation -->

[上一章](P112_drivers_input_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P114_drivers_led_配置项参考.md)
