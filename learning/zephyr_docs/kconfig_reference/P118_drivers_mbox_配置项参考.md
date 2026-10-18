---
id: learning.zephyr-docs.kconfig-reference.page-118
title: "`drivers/mbox`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第118章\_`drivers/mbox`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/mbox` 的 35 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MBOX"></a>

## 118.1 `CONFIG_MBOX`

**提示（Prompt）**：多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**说明（Help）**

在系统配置中纳入基于中断的多通道处理器间邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SERIALIZATION
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_NRF_802154_SERIALIZATION
CONFIG_IRONSIDE_SE_CALL_ZEPHYR
CONFIG_NRF53_SYNC_RTC
CONFIG_BT_HCI_IPC
CONFIG_ETH_NXP_S32_NETC
CONFIG_RASPBERRYPI_FIRMWARE
CONFIG_TISCI
CONFIG_IPM_MBOX
CONFIG_WDT_NRF_GSWDT
CONFIG_ZBUS_PROXY_AGENT_IPC
```

**定义位置（Location）**：[`drivers/mbox/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NRF_802154_SERIALIZATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SERIALIZATION)、[`CONFIG_IRONSIDE_SE_CALL_ZEPHYR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IRONSIDE_SE_CALL_ZEPHYR)、[`CONFIG_NRF53_SYNC_RTC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_BT_HCI_IPC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_IPC)、[`CONFIG_ETH_NXP_S32_NETC`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_S32_NETC)、[`CONFIG_RASPBERRYPI_FIRMWARE`](P091_drivers_firmware_配置项参考.md#CONFIG_RASPBERRYPI_FIRMWARE)、[`CONFIG_TISCI`](P091_drivers_firmware_配置项参考.md#CONFIG_TISCI)、[`CONFIG_IPM_MBOX`](P113_drivers_ipm_配置项参考.md#CONFIG_IPM_MBOX)、[`CONFIG_WDT_NRF_GSWDT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WDT_NRF_GSWDT)、[`CONFIG_ZBUS_PROXY_AGENT_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZBUS_PROXY_AGENT_IPC)。

<a id="CONFIG_MBOX_ADI_MAX32_SEMA"></a>

## 118.2 `CONFIG_MBOX_ADI_MAX32_SEMA`

**提示（Prompt）**：ADI MAX32 SEMA 邮箱驱动

**说明（Help）**

ADI MAX32 SEMA 外设邮箱功能的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ADI_MBOX_MAX32_SEMA_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.adi_max32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.adi_max32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_ANDES_PLIC_SW"></a>

## 118.3 `CONFIG_MBOX_ANDES_PLIC_SW`

**提示（Prompt）**：MBOX Andes PLIC-SW 驱动

**说明（Help）**

启用基于 Andes PLIC-SW 的 MBOX 控制器驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ANDESTECH_MBOX_PLIC_SW_ENABLED && CONFIG_PLIC_SUPPORTS_SOFT_INTERRUPT && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.andes:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.andes#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_PLIC_SUPPORTS_SOFT_INTERRUPT`](P006_drivers_interrupt_controller_配置项参考_2.md#CONFIG_PLIC_SUPPORTS_SOFT_INTERRUPT)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)。

<a id="CONFIG_MBOX_BCM2711"></a>

## 118.4 `CONFIG_MBOX_BCM2711`

**提示（Prompt）**：Broadcom BCM2711 邮箱驱动

**说明（Help）**

Broadcom BCM2711 邮箱的驱动，用于与 VideoCore 通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BRCM_BCM2711_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.brcm_bcm2711:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.brcm_bcm2711#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_ESP32"></a>

## 118.5 `CONFIG_MBOX_ESP32`

**提示（Prompt）**：ESP32 软件邮箱（Soft Mailbox）驱动

**说明（Help）**

基于 ESP32 门铃（Doorbell）机制的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_MBOX_ESP32_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.esp32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.esp32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_INFINEON"></a>

## 118.6 `CONFIG_MBOX_INFINEON`

**提示（Prompt）**：Infineon IPC 邮箱驱动

**说明（Help）**

启用 Infineon 处理器间通信（IPC）模块的邮箱（MBOX）驱动，使用直接寄存器访问（Direct Register Access）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_INFINEON_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.infineon:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.infineon#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_INIT_PRIORITY"></a>

## 118.7 `CONFIG_MBOX_INIT_PRIORITY`

**提示（Prompt）**：MBOX 初始化优先级（Initialization Priority）

**说明（Help）**

MBOX 驱动设备的初始化优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`drivers/mbox/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_IVSHMEM"></a>

## 118.8 `CONFIG_MBOX_IVSHMEM`

**提示（Prompt）**：基于 IVSHMEM-Doorbell 的 MBOX 驱动

**说明（Help）**

使用 IVSHMEM 门铃（Doorbell）机制的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_LINARO_IVSHMEM_MBOX_ENABLED && CONFIG_IVSHMEM && CONFIG_IVSHMEM_DOORBELL && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.ivshmem:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.ivshmem#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_IVSHMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM)、[`CONFIG_IVSHMEM_DOORBELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IVSHMEM_DOORBELL)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_IVSHMEM_EVENT_LOOP_PRIO"></a>

## 118.9 `CONFIG_MBOX_IVSHMEM_EVENT_LOOP_PRIO`

**提示（Prompt）**：IVSHMEM MBOX 事件循环任务优先级（Event Loop Task Priority）

**说明（Help）**

调整 IVSHMEM 事件循环任务的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX_IVSHMEM && CONFIG_MBOX
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.ivshmem:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.ivshmem#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 基于 IVSHMEM-Doorbell 的 MBOX 驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX_IVSHMEM`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_IVSHMEM)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_IVSHMEM_EVENT_LOOP_STACK_SIZE"></a>

## 118.10 `CONFIG_MBOX_IVSHMEM_EVENT_LOOP_STACK_SIZE`

**提示（Prompt）**：IVSHMEM MBOX 事件循环任务栈大小，单位为字节

**说明（Help）**

调整 IVSHMEM 事件循环任务的栈大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX_IVSHMEM && CONFIG_MBOX
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.ivshmem:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.ivshmem#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 基于 IVSHMEM-Doorbell 的 MBOX 驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX_IVSHMEM`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_IVSHMEM)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_MHUV2"></a>

## 118.11 `CONFIG_MBOX_MHUV2`

**提示（Prompt）**：ARM MHUv2 邮箱驱动

**说明（Help）**

Arm 消息处理单元第 2 版（Message Handling Unit v2，MHUv2）驱动，通过 Zephyr `mbox` API 提供门铃信号（Doorbell Signalling）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_MHUV2_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.mhuv2:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.mhuv2#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_MHUV2_NUM_CHANS"></a>

## 118.12 `CONFIG_MBOX_MHUV2_NUM_CHANS`

**提示（Prompt）**：ARM MHUv2 邮箱通道数量

**说明（Help）**

支持的最大硬件通道窗口（Channel Window）数量。必须小于或等于硬件报告的 `MSG_NO_CAP`。MHUv2 最多允许 124 个通道窗口，每个窗口有 32 个门铃槽位。需要此配置参数，是为了避免动态分配每个门铃的数据结构。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX_MHUV2 && CONFIG_MBOX
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 124]
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.mhuv2:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.mhuv2#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → ARM MHUv2 邮箱驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX_MHUV2`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_MHUV2)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_MHUV3"></a>

## 118.13 `CONFIG_MBOX_MHUV3`

**提示（Prompt）**：ARM MHUv3 邮箱驱动

**说明（Help）**

Arm 消息处理单元第 3 版（Message Handling Unit v3，MHUv3）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ARM_MHUV3_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.mhuv3:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.mhuv3#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_MHUV3_NUM_DBCH"></a>

## 118.14 `CONFIG_MBOX_MHUV3_NUM_DBCH`

**提示（Prompt）**：ARM MHUv3 邮箱门铃通道数量（Doorbell Channels）

**说明（Help）**

Postbox/Mailbox 中允许的最大门铃通道数量。必须小于或等于 `PBX_DBCH_CFG0`/`MBX_DBCH_CFG0` 寄存器中的 `NUM_DBCH + 1`。如果支持门铃扩展（Doorbell Extension），此数量必须大于 0。MHUv3 最多允许 128 个门铃通道。需要此配置参数，是为了避免动态分配门铃通道数据结构。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX_MHUV3 && CONFIG_MBOX
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.mhuv3:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.mhuv3#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → ARM MHUv3 邮箱驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX_MHUV3`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_MHUV3)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRFX_IPC"></a>

## 118.15 `CONFIG_MBOX_NRFX_IPC`

**提示（Prompt）**：MBOX NRF IPC 驱动

**说明（Help）**

Nordic nRF 消息单元（Messaging Unit）的驱动，基于 nRF IPC 外设硬件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_MBOX_NRF_IPC_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRFX_IPC
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrfx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrfx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_NRFX_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRFX_IPC)。

<a id="CONFIG_MBOX_NRF_BELLBOARD_RX"></a>

## 118.16 `CONFIG_MBOX_NRF_BELLBOARD_RX`

**提示（Prompt）**：nRF BELLBOARD 接收（RX）驱动

**说明（Help）**

用于接收的 Nordic nRF BELLBOARD 邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_BELLBOARD_RX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_bellboard:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_bellboard#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRF_BELLBOARD_TX"></a>

## 118.17 `CONFIG_MBOX_NRF_BELLBOARD_TX`

**提示（Prompt）**：nRF BELLBOARD 发送（TX）驱动

**说明（Help）**

用于发送的 Nordic nRF BELLBOARD 邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_BELLBOARD_TX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_bellboard:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_bellboard#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRF_VEVIF_EVENT_EARLY_INT_HANDLE"></a>

## 118.18 `CONFIG_MBOX_NRF_VEVIF_EVENT_EARLY_INT_HANDLE`

**提示（Prompt）**：早期中断处理（Early Interrupt Handling）

**说明（Help）**

启用处理在 VPR 事件启用之前到达的早期中断。挂起的中断会在对应事件启用后处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX
```

**被选择（Selected by）**

```text
CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_event:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_event#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16)。

<a id="CONFIG_MBOX_NRF_VEVIF_EVENT_RX"></a>

## 118.19 `CONFIG_MBOX_NRF_VEVIF_EVENT_RX`

**提示（Prompt）**：nRF VEVIF 事件接收（RX）驱动

**说明（Help）**

接收 VPR 触发事件的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VEVIF_EVENT_RX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_event:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_event#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRF_VEVIF_EVENT_TX"></a>

## 118.20 `CONFIG_MBOX_NRF_VEVIF_EVENT_TX`

**提示（Prompt）**：nRF VEVIF 事件发送（TX）驱动

**说明（Help）**

将事件从 VPR 发送到远端核心（Remote Core）的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VEVIF_EVENT_TX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_event:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_event#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16"></a>

## 118.21 `CONFIG_MBOX_NRF_VEVIF_EVENT_USE_54L_ERRATA_16`

**提示（Prompt）**：应用 nRF54L 系列勘误（Errata）16 的规避措施

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_SOC_NRF54L05 || CONFIG_SOC_NRF54L10 || CONFIG_SOC_NRF54L15) && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBOX_NRF_VEVIF_EVENT_EARLY_INT_HANDLE
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_event:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_event#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_SOC_NRF54L05`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L05)、[`CONFIG_SOC_NRF54L10`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L10)、[`CONFIG_SOC_NRF54L15`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_NRF54L15)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_MBOX_NRF_VEVIF_EVENT_EARLY_INT_HANDLE`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_NRF_VEVIF_EVENT_EARLY_INT_HANDLE)。

<a id="CONFIG_MBOX_NRF_VEVIF_TASK_RX"></a>

## 118.22 `CONFIG_MBOX_NRF_VEVIF_TASK_RX`

**提示（Prompt）**：nRF VEVIF 任务接收（RX）驱动

**说明（Help）**

在 VPR 上以 CLIC 中断形式接收 VEVIF 任务的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VEVIF_TASK_RX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_task:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_task#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NRF_VEVIF_TASK_TX"></a>

## 118.23 `CONFIG_MBOX_NRF_VEVIF_TASK_TX`

**提示（Prompt）**：nRF VEVIF 任务发送（TX）驱动

**说明（Help）**

以 CLIC 中断形式向 VPR 发送 VEVIF 任务的邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_VEVIF_TASK_TX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nrf_vevif_task:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nrf_vevif_task#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NXP_IMX_MU"></a>

## 118.24 `CONFIG_MBOX_NXP_IMX_MU`

**提示（Prompt）**：NXP i.MX 消息单元（Message Unit，MU）驱动

**说明（Help）**

NXP i.MX 消息单元驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MBOX_IMX_MU_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nxp_imx:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nxp_imx#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NXP_MAILBOX"></a>

## 118.25 `CONFIG_MBOX_NXP_MAILBOX`

**提示（Prompt）**：用于 MBOX 的 NXP 邮箱驱动

**说明（Help）**

通过 MBOX 接口提供 NXP 邮箱单元（Mailbox Unit）的驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MBOX_MAILBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nxp_mailbox:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nxp_mailbox#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_NXP_S32_MRU"></a>

## 118.26 `CONFIG_MBOX_NXP_S32_MRU`

**提示（Prompt）**：NXP S32 消息接收单元（Message Receive Unit，MRU）驱动

**说明（Help）**

NXP S32 消息接收单元（MRU）驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_S32_MRU_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NOCACHE_MEMORY if CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.nxp_s32:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.nxp_s32#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_NOCACHE_MEMORY`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_NOCACHE_MEMORY)、[`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_NOCACHE_MEMORY_SUPPORT`。

<a id="CONFIG_MBOX_RENESAS_RA_IPC"></a>

## 118.27 `CONFIG_MBOX_RENESAS_RA_IPC`

**提示（Prompt）**：Renesas RA IPC 邮箱驱动

**说明（Help）**

启用 RA IPC 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RA_IPC_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RA_FSP_IPC
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.renesas_ra:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.renesas_ra#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_USE_RA_FSP_IPC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RA_FSP_IPC)。

<a id="CONFIG_MBOX_RENESAS_RCAR_MFIS"></a>

## 118.28 `CONFIG_MBOX_RENESAS_RCAR_MFIS`

**提示（Prompt）**：Renesas R-Car MFIS 驱动

**说明（Help）**

R-Car MFIS 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RCAR_MFIS_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.renesas_rcar:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.renesas_rcar#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_RENESAS_RZ_MHU"></a>

## 118.29 `CONFIG_MBOX_RENESAS_RZ_MHU`

**提示（Prompt）**：Renesas RZ MHU 驱动

**说明（Help）**

启用 RZ MHU 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_RENESAS_RZ_MHU_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_RZ_FSP_MHU
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.renesas_rz:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.renesas_rz#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_USE_RZ_FSP_MHU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_RZ_FSP_MHU)。

<a id="CONFIG_MBOX_RENESAS_RZ_MHU_BUSY_WAIT_TIMEOUT_US"></a>

## 118.30 `CONFIG_MBOX_RENESAS_RZ_MHU_BUSY_WAIT_TIMEOUT_US`

**提示（Prompt）**：MBOX 发送 API 超时（Send API Timeout），单位为微秒

**说明（Help）**

此选项指定 `mbox_send` API 在发送新消息前，忙等待（Busy-wait）远端处理器消费上一条消息的超时时间。如果该消息未在此时间内被消费，`mbox_send` 返回错误。设为 0 或负数时，`mbox_send` 会无限期等待上一条消息被消费，再发送新消息。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MBOX_RENESAS_RZ_MHU && CONFIG_MBOX
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.renesas_rz:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.renesas_rz#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → Renesas RZ MHU 驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX_RENESAS_RZ_MHU`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX_RENESAS_RZ_MHU)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_RPI_PICO"></a>

## 118.31 `CONFIG_MBOX_RPI_PICO`

**提示（Prompt）**：RP2350/RP2040 SoC 的处理器间邮箱（Inter-processor Mailbox）驱动

**说明（Help）**

Raspberry Pi Pico 邮箱驱动，基于 RP2350/RP2040 处理器间先入先出队列（FIFO）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM && DT_HAS_RASPBERRYPI_PICO_MBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.rpi_pico:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.rpi_pico#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_STM32_HSEM"></a>

## 118.32 `CONFIG_MBOX_STM32_HSEM`

**提示（Prompt）**：MBOX STM32 HSEM 驱动

**说明（Help）**

STM32 硬件信号量（Hardware Semaphore）的 MBOX 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_MBOX_STM32_HSEM_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.stm32_hsem:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.stm32_hsem#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_TI_OMAP_MAILBOX"></a>

## 118.33 `CONFIG_MBOX_TI_OMAP_MAILBOX`

**提示（Prompt）**：TI OMAP 邮箱驱动

**说明（Help）**

TI OMAP 邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_OMAP_MAILBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.ti_omap:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.ti_omap#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_TI_SECURE_PROXY"></a>

## 118.34 `CONFIG_MBOX_TI_SECURE_PROXY`

**提示（Prompt）**：TI Secureproxy 邮箱驱动

**说明（Help）**

TI 安全代理（Secure Proxy）邮箱驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_SECURE_PROXY_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.ti_secproxy:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.ti_secproxy#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<a id="CONFIG_MBOX_XLNX_IPI_MAILBOX"></a>

## 118.35 `CONFIG_MBOX_XLNX_IPI_MAILBOX`

**提示（Prompt）**：MBOX XLNX IPI MAILBOX 驱动

**说明（Help）**

启用 AMD-Xilinx IPI 邮箱外设的 MBOX 驱动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_XLNX_MBOX_VERSAL_IPI_MAILBOX_ENABLED && CONFIG_MBOX
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/mbox/Kconfig.xlnx:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/mbox/Kconfig.xlnx#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)。

<!-- kconfig-navigation -->

[上一章](P117_drivers_lora_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P119_drivers_memc_配置项参考.md)
