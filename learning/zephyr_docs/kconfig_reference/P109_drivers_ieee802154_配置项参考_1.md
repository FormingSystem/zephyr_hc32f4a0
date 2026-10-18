---
id: learning.zephyr-docs.kconfig-reference.page-109
title: "`drivers/ieee802154`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第109章\_`drivers/ieee802154`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `drivers/ieee802154` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_IEEE802154"></a>

## 109.1 `CONFIG_IEEE802154`

**提示（Prompt）**：IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_L2_PHY_IEEE802154
```

**主动选择（Selects）**

```text
CONFIG_NET_PKT_CONTROL_BLOCK
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:9`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L9)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_L2_PHY_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PHY_IEEE802154)、[`CONFIG_NET_PKT_CONTROL_BLOCK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_CONTROL_BLOCK)。

<a id="CONFIG_IEEE802154_B91_CCA_RSSI_THRESHOLD"></a>

## 109.2 `CONFIG_IEEE802154_B91_CCA_RSSI_THRESHOLD`

**提示（Prompt）**：空闲信道评估（CCA）过程的 RSSI 阈值

**说明（Help）**

当前接收信号强度指示（RSSI）值小于此参数时，空闲信道评估（CCA）过程返回 true。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
-50
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_INIT_PRIO"></a>

## 109.3 `CONFIG_IEEE802154_B91_INIT_PRIO`

**提示（Prompt）**：Telink B91 IEEE 802.15.4 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_MAC4"></a>

## 109.4 `CONFIG_IEEE802154_B91_MAC4`

**提示（Prompt）**：MAC 地址第 4 字节（Byte 4）

**说明（Help）**

这是介质访问控制（MAC）地址的第 4 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_B91_RANDOM_MAC && CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_B91_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_B91_RANDOM_MAC)、[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_MAC5"></a>

## 109.5 `CONFIG_IEEE802154_B91_MAC5`

**提示（Prompt）**：MAC 地址第 5 字节（Byte 5）

**说明（Help）**

这是介质访问控制（MAC）地址的第 5 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_B91_RANDOM_MAC && CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_B91_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_B91_RANDOM_MAC)、[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_MAC6"></a>

## 109.6 `CONFIG_IEEE802154_B91_MAC6`

**提示（Prompt）**：MAC 地址第 6 字节（Byte 6）

**说明（Help）**

这是介质访问控制（MAC）地址的第 6 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_B91_RANDOM_MAC && CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_B91_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_B91_RANDOM_MAC)、[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_MAC7"></a>

## 109.7 `CONFIG_IEEE802154_B91_MAC7`

**提示（Prompt）**：MAC 地址第 7 字节（Byte 7）

**说明（Help）**

这是介质访问控制（MAC）地址的第 7 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_B91_RANDOM_MAC && CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_B91_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_B91_RANDOM_MAC)、[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_RANDOM_MAC"></a>

## 109.8 `CONFIG_IEEE802154_B91_RANDOM_MAC`

**提示（Prompt）**：随机 MAC 地址（Random MAC Address）

**说明（Help）**

动态生成随机 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_B91_SET_TXRX_DELAY_US"></a>

## 109.9 `CONFIG_IEEE802154_B91_SET_TXRX_DELAY_US`

**提示（Prompt）**：收发模式切换延迟（Tx/Rx Switching Delay，微秒）

**说明（Help）**

发送／接收（Tx/Rx）模式切换期间，锁相环（PLL）稳定所需的延迟时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_TELINK_B91 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
120
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.b91:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.b91#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Telink B91 射频（RF）驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_TELINK_B91`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_TELINK_B91)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_BFLB"></a>

## 109.10 `CONFIG_IEEE802154_BFLB`

**提示（Prompt）**：Bouffalo Lab IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_BFLB_IEEE802154_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_DYNAMIC_INTERRUPTS if CONFIG_SOC_SERIES_BL70X || CONFIG_SOC_SERIES_BL70XL
CONFIG_BFLB_PHYRF
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.bflb:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.bflb#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_DYNAMIC_INTERRUPTS`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DYNAMIC_INTERRUPTS)、[`CONFIG_SOC_SERIES_BL70X`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70X)、[`CONFIG_SOC_SERIES_BL70XL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_BL70XL)、[`CONFIG_BFLB_PHYRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BFLB_PHYRF)。

<a id="CONFIG_IEEE802154_BFLB_INIT_PRIO"></a>

## 109.11 `CONFIG_IEEE802154_BFLB_INIT_PRIO`

**提示（Prompt）**：Bouffalo Lab IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_BFLB && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.bflb:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.bflb#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Bouffalo Lab IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_BFLB`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_BFLB)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CARRIER_FUNCTIONS"></a>

## 109.12 `CONFIG_IEEE802154_CARRIER_FUNCTIONS`

**提示（Prompt）**：载波功能（Carrier Functions）支持

**说明（Help）**

启用调制载波（Modulated Carrier）和连续载波（Continuous Carrier）等功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_DIAG
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_OPENTHREAD_DIAG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_DIAG)。

<a id="CONFIG_IEEE802154_CC1200"></a>

## 109.13 `CONFIG_IEEE802154_CC1200`

**提示（Prompt）**：TI CC1200 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC1200_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_CCA_THRESHOLD"></a>

## 109.14 `CONFIG_IEEE802154_CC1200_CCA_THRESHOLD`

**提示（Prompt）**：CCA 阈值，单位为 dBm

**说明（Help）**

设置空闲信道评估（CCA）阈值。详情参见数据手册中的 `AGC_CS_THR` 寄存器。除非清楚其影响，否则不要修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
-91
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_INIT_PRIO"></a>

## 109.15 `CONFIG_IEEE802154_CC1200_INIT_PRIO`

**提示（Prompt）**：CC1200 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。注意，CC1200 要求 GPIO 和 SPI 先准备就绪，有时 GPIO 应最先初始化，因为 SPI 也可能需要它。当然，CC1200 必须在网络协议栈（Network Stack）之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_MAC4"></a>

## 109.16 `CONFIG_IEEE802154_CC1200_MAC4`

**提示（Prompt）**：MAC 地址第 4 字节（Byte 4）

**说明（Help）**

这是介质访问控制（MAC）地址的第 4 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC1200_RANDOM_MAC && CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200_RANDOM_MAC)、[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_MAC5"></a>

## 109.17 `CONFIG_IEEE802154_CC1200_MAC5`

**提示（Prompt）**：MAC 地址第 5 字节（Byte 5）

**说明（Help）**

这是介质访问控制（MAC）地址的第 5 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC1200_RANDOM_MAC && CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:44`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L44)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200_RANDOM_MAC)、[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_MAC6"></a>

## 109.18 `CONFIG_IEEE802154_CC1200_MAC6`

**提示（Prompt）**：MAC 地址第 6 字节（Byte 6）

**说明（Help）**

这是介质访问控制（MAC）地址的第 6 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC1200_RANDOM_MAC && CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200_RANDOM_MAC)、[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_MAC7"></a>

## 109.19 `CONFIG_IEEE802154_CC1200_MAC7`

**提示（Prompt）**：MAC 地址第 7 字节（Byte 7）

**说明（Help）**

这是介质访问控制（MAC）地址的第 7 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC1200_RANDOM_MAC && CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200_RANDOM_MAC)、[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_RANDOM_MAC"></a>

## 109.20 `CONFIG_IEEE802154_CC1200_RANDOM_MAC`

**提示（Prompt）**：随机 MAC 地址（Random MAC Address）

**说明（Help）**

动态生成随机 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_RF_PRESET"></a>

## 109.21 `CONFIG_IEEE802154_CC1200_RF_PRESET`

**提示（Prompt）**：使用 TI CC1200 射频预设（RF Presets）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_RF_SET_0"></a>

## 109.22 `CONFIG_IEEE802154_CC1200_RF_SET_0`

**提示（Prompt）**：IEEE 802.15.4g SUN MR-FSK，863 MHz 频段，模式 #1——信道页（Channel Page）9，34 个信道，50 Kbps（ETSI）

**说明（Help）**

这是旧版 IEEE 802.15.4g-2012 智能公用事业网络（SUN）多速率频移键控（MR-FSK）物理层（PHY），在较新的标准（IEEE 802.15.4-2015 及之后版本）中已不存在。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持 → 使用 TI CC1200 射频预设（RF Presets） → TI CC1200 射频预设（RF Preset）

<a id="CONFIG_IEEE802154_CC1200_RF_SET_1"></a>

## 109.23 `CONFIG_IEEE802154_CC1200_RF_SET_1`

**提示（Prompt）**：IEEE 802.15.4g SUN MR-FSK，920 MHz 频段，模式 #1——信道页（Channel Page）9，39 个信道，50 Kbps（ARIB）

**说明（Help）**

这是旧版 IEEE 802.15.4g-2012 智能公用事业网络（SUN）多速率频移键控（MR-FSK）物理层（PHY），在较新的标准（IEEE 802.15.4-2015 及之后版本）中已不存在。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持 → 使用 TI CC1200 射频预设（RF Presets） → TI CC1200 射频预设（RF Preset）

<a id="CONFIG_IEEE802154_CC1200_RF_SET_2"></a>

## 109.24 `CONFIG_IEEE802154_CC1200_RF_SET_2`

**提示（Prompt）**：IEEE 802.15.4 非标准（Non-Standard）2-GFSK，433 MHz 频段——信道页 9，15 个信道，50 Kbps（ETSI）

**说明（Help）**

这是非标准物理层（PHY），类似 IEEE 802.15.4g-2012 SUN MR-FSK PHY，但不使用任何标准规定的频段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持 → 使用 TI CC1200 射频预设（RF Presets） → TI CC1200 射频预设（RF Preset）

<a id="CONFIG_IEEE802154_CC1200_RSSI_OFFSET"></a>

## 109.25 `CONFIG_IEEE802154_CC1200_RSSI_OFFSET`

**提示（Prompt）**：RSSI 偏移量（Offset），单位为 dBm

**说明（Help）**

设置增益调整（Gain Adjustment）。详情参见数据手册中的 `AGC_GAIN_ADJUST` 寄存器。除非清楚其影响，否则不要修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
-81
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_RX_STACK_SIZE"></a>

## 109.26 `CONFIG_IEEE802154_CC1200_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，可通过此选项方便地调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC1200_XOSC"></a>

## 109.27 `CONFIG_IEEE802154_CC1200_XOSC`

**提示（Prompt）**：晶体振荡器（Crystal Oscillator）频率，单位为 kHz

**说明（Help）**

设置 XOSC 频率，必须介于 38400 和 40000 之间。此值应与通过 SmartRF 工具设置的射频配置一致。除非清楚其影响，否则不要修改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC1200 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
40000
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc1200:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc1200#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC1200 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC1200`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC1200)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX"></a>

## 109.28 `CONFIG_IEEE802154_CC13XX_CC26XX`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_IEEE802154_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_INIT_PRIO"></a>

## 109.29 `CONFIG_IEEE802154_CC13XX_CC26XX_INIT_PRIO`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级（Initialization Priority）数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MAX_BE"></a>

## 109.30 `CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MAX_BE`

**提示（Prompt）**：CSMA MAC 最大退避指数（Maximum Backoff Exponent）

**说明（Help）**

载波侦听多路访问／冲突避免（CSMA-CA）算法中退避指数（BE）的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE if CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA
5
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BE)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MAX_BO"></a>

## 109.31 `CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MAX_BO`

**提示（Prompt）**：CSMA 最大退避次数（Maximum Backoffs）

**说明（Help）**

带冲突避免的载波侦听多址（CSMA-CA）算法在判定信道访问失败前尝试退避（Backoff）的最大次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BO if CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA
4
```

**取值范围（Ranges）**

```text
[1, 5]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MAX_BO)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MIN_BE"></a>

## 109.32 `CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_CSMA_CA_MIN_BE`

**提示（Prompt）**：CSMA MAC 最小退避指数（Minimum Backoff Exponent）

**说明（Help）**

载波侦听多路访问／冲突避免（CSMA-CA）算法中退避指数（BE）的最小值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MIN_BE if CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA
3
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MIN_BE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA_MIN_BE)、[`CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_CSMA_CA)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_TX_RETRIES"></a>

## 109.33 `CONFIG_IEEE802154_CC13XX_CC26XX_RADIO_TX_RETRIES`

**提示（Prompt）**：无线电发送尝试次数（Transmission Attempts）

**说明（Help）**

无线电驱动在报告无法发送数据包之前，应执行的发送尝试次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_NET_L2_IEEE802154_RADIO_TX_RETRIES if CONFIG_NET_L2_IEEE802154
3
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NET_L2_IEEE802154_RADIO_TX_RETRIES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_RADIO_TX_RETRIES)、[`CONFIG_NET_L2_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ"></a>

## 109.34 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC13XX_CC26XX_IEEE802154_SUBGHZ_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CS_THRESHOLD"></a>

## 109.35 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CS_THRESHOLD`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4g 载波侦听能量检测阈值（Carrier Sense ED Threshold），单位为 dBm

**说明（Help）**

此选项设置 CSMA/CA 算法中空闲信道评估（CCA）模式 1 或 3 的能量检测（ED）阈值。除 SUN O-QPSK PHY 外，ED 阈值对应的接收信号功率应最多比该物理层规定的接收灵敏度高 10 dB，或符合当地规定（见 IEEE 802.15.4-2020 第 10.2.8 节）。对于 SUN O-QPSK PHY，ED 阈值应符合 IEEE 802.15.4-2020 第 21.5.13 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
-80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CUSTOM_POWER_TABLE"></a>

## 109.36 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CUSTOM_POWER_TABLE`

**提示（Prompt）**：使用自定义功率表结构（Custom Power Table Structure，高级）

**说明（Help）**

从外部模块导入无线电功率表，允许覆盖射频调制（RF Modulation）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CUSTOM_RADIO_SETUP"></a>

## 109.37 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_CUSTOM_RADIO_SETUP`

**提示（Prompt）**：使用自定义无线电配置结构（Custom Radio Setup Structures，高级）

**说明（Help）**

从外部模块导入无线电配置结构，取代默认结构。允许覆盖射频调制／协议（RF Modulation / Protocol）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_INIT_PRIO"></a>

## 109.38 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_INIT_PRIO`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4g 初始化优先级

**说明（Help）**

设置初始化优先级（Initialization Priority）数值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_NUM_RX_BUF"></a>

## 109.39 `CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ_NUM_RX_BUF`

**提示（Prompt）**：TI CC13xx / CC26xx IEEE 802.15.4g 接收缓冲区数量（Receive Buffer Count）

**说明（Help）**

此选项允许用户配置接收缓冲区的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc13xx_cc26xx:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc13xx_cc26xx#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC13xx / CC26xx IEEE 802.15.4g 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520"></a>

## 109.40 `CONFIG_IEEE802154_CC2520`

**提示（Prompt）**：TI CC2520 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_TI_CC2520_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_CRYPTO"></a>

## 109.41 `CONFIG_IEEE802154_CC2520_CRYPTO`

**提示（Prompt）**：CC2520 硬件加密辅助功能（Hardware Crypto Helper）

**说明（Help）**

此选项公开 CC2520 的硬件 AES 加密功能。该功能只应用于 802.15.4 安全机制，不应用于其他用途。公开的加密设备仅支持同步 CCM 操作（Synchronous CCM Operation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_IEEE802154_SECURITY && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_IEEE802154_SECURITY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_SECURITY)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_CRYPTO_INIT_PRIO"></a>

## 109.42 `CONFIG_IEEE802154_CC2520_CRYPTO_INIT_PRIO`

**提示（Prompt）**：TI CC2520 加密设备初始化优先级

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。由于共享同一个运行时上下文（Runtime Context），它应在 CC2520 之后初始化。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC2520_CRYPTO && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:77`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L77)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持 → CC2520 硬件加密辅助功能（Hardware Crypto Helper）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520_CRYPTO`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520_CRYPTO)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_INIT_PRIO"></a>

## 109.43 `CONFIG_IEEE802154_CC2520_INIT_PRIO`

**提示（Prompt）**：CC2520 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。注意，CC2520 要求 GPIO 和 SPI 先准备就绪，有时 GPIO 应最先初始化，因为 SPI 也可能需要它。当然，CC2520 必须在网络协议栈之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_MAC4"></a>

## 109.44 `CONFIG_IEEE802154_CC2520_MAC4`

**提示（Prompt）**：MAC 地址第 4 字节（Byte 4）

**说明（Help）**

这是介质访问控制（MAC）地址的第 4 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC2520_RANDOM_MAC && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:38`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L38)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520_RANDOM_MAC)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_MAC5"></a>

## 109.45 `CONFIG_IEEE802154_CC2520_MAC5`

**提示（Prompt）**：MAC 地址第 5 字节（Byte 5）

**说明（Help）**

这是介质访问控制（MAC）地址的第 5 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC2520_RANDOM_MAC && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520_RANDOM_MAC)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_MAC6"></a>

## 109.46 `CONFIG_IEEE802154_CC2520_MAC6`

**提示（Prompt）**：MAC 地址第 6 字节（Byte 6）

**说明（Help）**

这是介质访问控制（MAC）地址的第 6 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC2520_RANDOM_MAC && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520_RANDOM_MAC)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_MAC7"></a>

## 109.47 `CONFIG_IEEE802154_CC2520_MAC7`

**提示（Prompt）**：MAC 地址第 7 字节（Byte 7）

**说明（Help）**

这是介质访问控制（MAC）地址的第 7 字节。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_CC2520_RANDOM_MAC && CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520_RANDOM_MAC`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520_RANDOM_MAC)、[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_RANDOM_MAC"></a>

## 109.48 `CONFIG_IEEE802154_CC2520_RANDOM_MAC`

**提示（Prompt）**：随机 MAC 地址（Random MAC Address）

**说明（Help）**

动态生成随机 MAC 地址。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CC2520_RX_STACK_SIZE"></a>

## 109.49 `CONFIG_IEEE802154_CC2520_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，可通过此选项方便地调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_CC2520 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.cc2520:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.cc2520#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → TI CC2520 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_CC2520`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC2520)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_CSL_ENDPOINT"></a>

## 109.50 `CONFIG_IEEE802154_CSL_ENDPOINT`

**提示（Prompt）**：协调采样侦听端点（CSL Endpoint）支持

**说明（Help）**

使此设备成为协调采样侦听（Coordinated Sampled Listening，CSL）端点，具备延迟接收处理和 CSL 信息元素（IE）注入功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_DW1000"></a>

## 109.51 `CONFIG_IEEE802154_DW1000`

**提示（Prompt）**：Decawave DW1000 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_DECAWAVE_DW1000_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.dw1000:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.dw1000#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

<a id="CONFIG_IEEE802154_DW1000_INIT_PRIO"></a>

## 109.52 `CONFIG_IEEE802154_DW1000_INIT_PRIO`

**提示（Prompt）**：DW1000 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。注意，DW1000 要求 GPIO 和 SPI 先准备就绪，有时 GPIO 应最先初始化，因为 SPI 也可能需要它。当然，DW1000 必须在网络协议栈之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_DW1000 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.dw1000:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.dw1000#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Decawave DW1000 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DW1000`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_DW1000)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_DW1000_SNIFF_OFFT"></a>

## 109.53 `CONFIG_IEEE802154_DW1000_SNIFF_OFFT`

**提示（Prompt）**：SNIFF 关闭时间（Off Time）

**说明（Help）**

SNIFF 关闭时间，单位约为 1 微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_DW1000 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
16
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.dw1000:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.dw1000#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Decawave DW1000 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DW1000`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_DW1000)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_DW1000_SNIFF_ONT"></a>

## 109.54 `CONFIG_IEEE802154_DW1000_SNIFF_ONT`

**提示（Prompt）**：SNIFF 开启时间（On Time）

**说明（Help）**

SNIFF 开启时间，以 PAC 为单位。最短开启时间为两个 PAC 的持续时间。SNIFF 计数器总会在开启时间计数上加 1 个 PAC 单位。`SNIFF_ONT` 值应为 1～15。值为 0 时禁用 SNIFF 模式。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_DW1000 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 15]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.dw1000:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.dw1000#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → Decawave DW1000 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_DW1000`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_DW1000)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32"></a>

## 109.55 `CONFIG_IEEE802154_ESP32`

**提示（Prompt）**：ESP32 系列 IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ESPRESSIF_ESP32_IEEE802154_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_ASSERT"></a>

## 109.56 `CONFIG_IEEE802154_ESP32_ASSERT`

**提示（Prompt）**：在断言信息中补充 IEEE802154 状态和事件

**说明（Help）**

启用此选项会在驱动中加入一些探测代码，并在触发断言（Assert）时打印相关信息。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_CCA_CARRIER"></a>

## 109.57 `CONFIG_IEEE802154_ESP32_CCA_CARRIER`

**提示（Prompt）**：仅载波侦听（Carrier Sense Only）

**说明（Help）**

将 CCA 模式配置为仅载波侦听（Carrier Sense Only）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_ESP32_CCA_MODE>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → 空闲信道评估（Clear Channel Assessment，CCA）模式

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_CCA_MODE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_MODE)。

<a id="CONFIG_IEEE802154_ESP32_CCA_CARRIER_AND_ED"></a>

## 109.58 `CONFIG_IEEE802154_ESP32_CCA_CARRIER_AND_ED`

**提示（Prompt）**：载波侦听且能量超过阈值（Carrier Sense AND Energy Above Threshold）

**说明（Help）**

将 CCA 模式配置为载波侦听与能量超过阈值同时成立（AND）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_ESP32_CCA_MODE>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → 空闲信道评估（Clear Channel Assessment，CCA）模式

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_CCA_MODE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_MODE)。

<a id="CONFIG_IEEE802154_ESP32_CCA_CARRIER_OR_ED"></a>

## 109.59 `CONFIG_IEEE802154_ESP32_CCA_CARRIER_OR_ED`

**提示（Prompt）**：载波侦听或能量超过阈值（Carrier Sense OR Energy Above Threshold）

**说明（Help）**

将 CCA 模式配置为载波侦听或能量超过阈值任一成立（OR）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_ESP32_CCA_MODE>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → 空闲信道评估（Clear Channel Assessment，CCA）模式

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_CCA_MODE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_MODE)。

<a id="CONFIG_IEEE802154_ESP32_CCA_ED"></a>

## 109.60 `CONFIG_IEEE802154_ESP32_CCA_ED`

**提示（Prompt）**：能量超过阈值（Energy Above Threshold）

**说明（Help）**

将 CCA 模式配置为能量超过阈值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_IEEE802154_ESP32_CCA_MODE>
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → 空闲信道评估（Clear Channel Assessment，CCA）模式

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_CCA_MODE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_MODE)。

<a id="CONFIG_IEEE802154_ESP32_CCA_MODE"></a>

## 109.61 `CONFIG_IEEE802154_ESP32_CCA_MODE`

**提示（Prompt）**：空闲信道评估（Clear Channel Assessment，CCA）模式

**说明（Help）**

配置空闲信道评估（CCA）模式。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_IEEE802154_ESP32_CCA_ED
```

**可选项（Choices）**

```text
CONFIG_IEEE802154_ESP32_CCA_CARRIER
CONFIG_IEEE802154_ESP32_CCA_ED
CONFIG_IEEE802154_ESP32_CCA_CARRIER_OR_ED
CONFIG_IEEE802154_ESP32_CCA_CARRIER_AND_ED
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_IEEE802154_ESP32_CCA_ED`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_ED)、[`CONFIG_IEEE802154_ESP32_CCA_CARRIER`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_CARRIER)、[`CONFIG_IEEE802154_ESP32_CCA_CARRIER_OR_ED`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_CARRIER_OR_ED)、[`CONFIG_IEEE802154_ESP32_CCA_CARRIER_AND_ED`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_CCA_CARRIER_AND_ED)。

<a id="CONFIG_IEEE802154_ESP32_CCA_THRESHOLD"></a>

## 109.62 `CONFIG_IEEE802154_ESP32_CCA_THRESHOLD`

**提示（Prompt）**：CCA 检测阈值（Detection Threshold）

**说明（Help）**

设置 CCA 阈值，单位为 dB。Espressif HAL 模块使用此配置。译注：此条原文单位为 dB，按原文保留。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
-60
```

**取值范围（Ranges）**

```text
[-120, 0]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_DEBUG"></a>

## 109.63 `CONFIG_IEEE802154_ESP32_DEBUG`

**提示（Prompt）**：IEEE802154 调试（Debug）

**说明（Help）**

启用此选项可输出不同类型的 IEEE802154 调试信息。所有 IEEE802154 调试功能都会增大最终二进制文件的大小。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_INIT_PRIO"></a>

## 109.64 `CONFIG_IEEE802154_ESP32_INIT_PRIO`

**提示（Prompt）**：ESP32 IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_MULTI_PAN_ENABLE"></a>

## 109.65 `CONFIG_IEEE802154_ESP32_MULTI_PAN_ENABLE`

**提示（Prompt）**：用于帧过滤器（Frame Filter）的多 PAN 功能

**说明（Help）**

启用 IEEE802154 多个个域网（Multi-PAN）功能。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_PENDING_TABLE_SIZE"></a>

## 109.66 `CONFIG_IEEE802154_ESP32_PENDING_TABLE_SIZE`

**提示（Prompt）**：待处理表大小（Pending Table Size）

**说明（Help）**

设置待处理表（Pending Table）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_ABORT"></a>

## 109.67 `CONFIG_IEEE802154_ESP32_RECORD_ABORT`

**提示（Prompt）**：记录中止信息（Abort Information）以供调试

**说明（Help）**

启用此选项以记录中止信息。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_ABORT_SIZE"></a>

## 109.68 `CONFIG_IEEE802154_ESP32_RECORD_ABORT_SIZE`

**提示（Prompt）**：中止记录表大小（Record Abort Table Size）

**说明（Help）**

设置中止记录表的大小。Espressif HAL 模块使用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_RECORD_ABORT && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 50]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug） → 记录中止信息（Abort Information）以供调试

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_RECORD_ABORT`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_RECORD_ABORT)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_CMD"></a>

## 109.69 `CONFIG_IEEE802154_ESP32_RECORD_CMD`

**提示（Prompt）**：记录命令信息（Command Information）以供调试

**说明（Help）**

启用此选项以记录命令信息。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_CMD_SIZE"></a>

## 109.70 `CONFIG_IEEE802154_ESP32_RECORD_CMD_SIZE`

**提示（Prompt）**：命令记录表大小（Record Command Table Size）

**说明（Help）**

设置命令记录表的大小。Espressif HAL 模块使用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_RECORD_CMD && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 50]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug） → 记录命令信息（Command Information）以供调试

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_RECORD_CMD`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_RECORD_CMD)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_EVENT"></a>

## 109.71 `CONFIG_IEEE802154_ESP32_RECORD_EVENT`

**提示（Prompt）**：记录事件信息（Event Information）以供调试

**说明（Help）**

启用此选项以记录事件；触发断言（Assert）时，将打印已记录的事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_EVENT_SIZE"></a>

## 109.72 `CONFIG_IEEE802154_ESP32_RECORD_EVENT_SIZE`

**提示（Prompt）**：事件记录表大小（Record Event Table Size）

**说明（Help）**

设置事件记录表的大小。Espressif HAL 模块使用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_RECORD_EVENT && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 50]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug） → 记录事件信息（Event Information）以供调试

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_RECORD_EVENT`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_RECORD_EVENT)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_STATE"></a>

## 109.73 `CONFIG_IEEE802154_ESP32_RECORD_STATE`

**提示（Prompt）**：记录状态信息（State Information）以供调试

**说明（Help）**

启用此选项以记录状态；触发断言（Assert）时，将打印已记录的状态。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RECORD_STATE_SIZE"></a>

## 109.74 `CONFIG_IEEE802154_ESP32_RECORD_STATE_SIZE`

**提示（Prompt）**：状态记录表大小（Record State Table Size）

**说明（Help）**

设置状态记录表的大小。Espressif HAL 模块使用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_RECORD_STATE && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 50]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:145`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L145)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug） → 记录状态信息（State Information）以供调试

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_RECORD_STATE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_RECORD_STATE)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RX_BUFFER_SIZE"></a>

## 109.75 `CONFIG_IEEE802154_ESP32_RX_BUFFER_SIZE`

**提示（Prompt）**：802.15.4 接收缓冲区数量（Receive Buffer Count）

**说明（Help）**

802.15.4 接收缓冲区的数量。Espressif HAL 模块使用此配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[2, 100]
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RX_STACK_SIZE"></a>

## 109.76 `CONFIG_IEEE802154_ESP32_RX_STACK_SIZE`

**提示（Prompt）**：ESP32 802.15.4 接收工作线程栈大小（RX Worker Thread Stack Size）

**说明（Help）**

专用线程所用的栈；该线程通过 `net_pkt` 分配和 `net_recv_data` 将接收到的帧转交给网络协议栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_RX_THREAD_PRIORITY"></a>

## 109.77 `CONFIG_IEEE802154_ESP32_RX_THREAD_PRIORITY`

**提示（Prompt）**：ESP32 802.15.4 接收工作线程的抢占优先级（Preempt Priority，值越小越紧急）

**说明（Help）**

必须是本次构建有效的抢占式线程优先级，参见 `CONFIG_NUM_PREEMPT_PRIORITIES`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_ESP32_SLEEP_ENABLE"></a>

## 109.78 `CONFIG_IEEE802154_ESP32_SLEEP_ENABLE`

**提示（Prompt）**：IEEE 802.15.4 轻度睡眠（Light Sleep）

**说明（Help）**

在轻度睡眠（Light Sleep）期间关闭 802.15.4 物理层（PHY）的电源，以降低电流消耗。无线电处于睡眠状态时，驱动会释放 SoC 电源管理（PM）策略锁。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_IEEE802154_ESP32 && CONFIG_NET_L2_OPENTHREAD && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**主动选择（Selects）**

```text
CONFIG_MAC_BB_PD if CONFIG_SOC_SERIES_ESP32C6
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:199`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L199)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_MAC_BB_PD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MAC_BB_PD)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C6`。

<a id="CONFIG_IEEE802154_ESP32_TXRX_STATISTIC"></a>

## 109.79 `CONFIG_IEEE802154_ESP32_TXRX_STATISTIC`

**提示（Prompt）**：记录收发数据包信息（TX/RX Packet Information）以供调试

**说明（Help）**

启用此选项以记录发送和接收数据包的信息。Espressif HAL 模块使用此配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_ESP32_DEBUG && CONFIG_IEEE802154_ESP32 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.esp32:191`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.esp32#L191)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → ESP32 系列 IEEE 802.15.4 驱动 → IEEE802154 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_ESP32_DEBUG`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32_DEBUG)、[`CONFIG_IEEE802154_ESP32`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_ESP32)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_KW41Z"></a>

## 109.80 `CONFIG_IEEE802154_KW41Z`

**提示（Prompt）**：NXP KW41Z 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_KW41Z_IEEE802154_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_REQUIRES_FULL_LIBC
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.kw41z:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.kw41z#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_REQUIRES_FULL_LIBC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REQUIRES_FULL_LIBC)。

<a id="CONFIG_IEEE802154_KW41Z_INIT_PRIO"></a>

## 109.81 `CONFIG_IEEE802154_KW41Z_INIT_PRIO`

**提示（Prompt）**：KW41Z 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要修改。它必须在网络协议栈之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_KW41Z && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.kw41z:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.kw41z#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP KW41Z 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_KW41Z`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_KW41Z)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_L2_PKT_INCL_FCS"></a>

## 109.82 `CONFIG_IEEE802154_L2_PKT_INCL_FCS`

**提示（Prompt）**：在二层（L2）数据包中包含帧校验序列（FCS）字段

**说明（Help）**

某些 802.15.4 二层（L2）实现要求数据包包含帧校验序列（FCS），另一些则不要求。此选项允许根据选用的上层配置该行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y if CONFIG_IEEE802154_RAW_MODE || CONFIG_NET_L2_OPENTHREAD
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_IEEE802154_RAW_MODE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_RAW_MODE)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)。

<a id="CONFIG_IEEE802154_MCR20A"></a>

## 109.83 `CONFIG_IEEE802154_MCR20A`

**提示（Prompt）**：NXP MCR20A 驱动支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCR20A_ENABLED && CONFIG_HAS_MCUX && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_HAS_MCUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_MCUX)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_MCUX`。

<a id="CONFIG_IEEE802154_MCR20A_INIT_PRIO"></a>

## 109.84 `CONFIG_IEEE802154_MCR20A_INIT_PRIO`

**提示（Prompt）**：MCR20A 初始化优先级（Initialization Priority）

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。注意，MCR20A 要求 GPIO 和 SPI 先准备就绪，有时 GPIO 应最先初始化，因为 SPI 也可能需要它。当然，MCR20A 必须在网络协议栈之前启动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCR20A && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCR20A`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCR20A)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_MCR20A_RX_STACK_SIZE"></a>

## 109.85 `CONFIG_IEEE802154_MCR20A_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，可通过此选项方便地调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCR20A && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcr20a:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcr20a#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCR20A 驱动支持

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCR20A`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCR20A)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_MCXW"></a>

## 109.86 `CONFIG_IEEE802154_MCXW`

**提示（Prompt）**：NXP MCXW 系列 IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NXP_MCXW_IEEE802154_ENABLED && !CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER
CONFIG_NVMEM
CONFIG_NET_PKT_TXTIME
CONFIG_NET_PKT_TIMESTAMP
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcxw:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcxw#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)、[`CONFIG_NVMEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVMEM)、[`CONFIG_NET_PKT_TXTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TXTIME)、[`CONFIG_NET_PKT_TIMESTAMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TIMESTAMP)。

<a id="CONFIG_IEEE802154_MCXW_CSL_ACCURACY"></a>

## 109.87 `CONFIG_IEEE802154_MCXW_CSL_ACCURACY`

**提示（Prompt）**：延迟操作的 CSL 精度（Accuracy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCXW && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcxw:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcxw#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCXW 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_MCXW_INIT_PRIO"></a>

## 109.88 `CONFIG_IEEE802154_MCXW_INIT_PRIO`

**提示（Prompt）**：IEEE802154 驱动的初始化优先级（Initialization Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCXW && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcxw:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcxw#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCXW 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_MCXW_RX_STACK_SIZE"></a>

## 109.89 `CONFIG_IEEE802154_MCXW_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_MCXW && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.mcxw:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.mcxw#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → NXP MCXW 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_MCXW`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_MCXW)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NET_IF_NO_AUTO_START"></a>

## 109.90 `CONFIG_IEEE802154_NET_IF_NO_AUTO_START`

**提示（Prompt）**：不自动启动（Auto-start）的 IEEE 802.15.4 接口

**说明（Help）**

此选项允许用户在无线电开始工作之前设置任意配置和／或过滤器。例如，可使用 `net_if_set_link_addr(iface, mac, 8, NET_LINK_IEEE802154)` 配置 EUI-64 值。全部配置完成后，必须调用 `net_if_up()` 启用接口。使用 OpenThread 或 Zigbee 时，此选项可能有用。若对此选项有疑问，请保持默认值。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5"></a>

## 109.91 `CONFIG_IEEE802154_NRF5`

**提示（Prompt）**：nRF52 系列 IEEE 802.15.4 驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_NORDIC_NRF_IEEE802154_ENABLED && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NRF_802154_RADIO_DRIVER if CONFIG_HAS_HW_NRF_RADIO_IEEE802154
CONFIG_NRF_802154_SER_HOST if !CONFIG_HAS_HW_NRF_RADIO_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NRF_802154_RADIO_DRIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_RADIO_DRIVER)、[`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_HW_NRF_RADIO_IEEE802154)、[`CONFIG_NRF_802154_SER_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SER_HOST)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_HW_NRF_RADIO_IEEE802154`。

<a id="CONFIG_IEEE802154_NRF5_CST_ENDPOINT"></a>

## 109.92 `CONFIG_IEEE802154_NRF5_CST_ENDPOINT`

**提示（Prompt）**：在 ieee802154_nrf5 中支持 OpenThread CST 端点扩展（Endpoint Extension）。

**说明（Help）**

启用 OpenThread 协调采样发送器（Coordinated Sampled Transmitter，CST）端点支持，提供 CST 信息元素（IE）注入，作为 `ieee802154_nrf5` 驱动的扩展。启用后，该驱动支持 `IEEE802154_OPENTHREAD_HW_CST` 能力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_WAKEUP_COORDINATOR
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_OPENTHREAD_WAKEUP_COORDINATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_WAKEUP_COORDINATOR)。

<a id="CONFIG_IEEE802154_NRF5_DELAY_TRX_ACC"></a>

## 109.93 `CONFIG_IEEE802154_NRF5_DELAY_TRX_ACC`

**提示（Prompt）**：延迟操作的时钟精度（Clock Accuracy）

**说明（Help）**

用于调度无线电延迟操作（延迟发送或延迟接收）的时钟精度，单位为百万分之一（ppm）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
CONFIG_CLOCK_CONTROL_NRF_ACCURACY if CONFIG_CLOCK_CONTROL_NRF && CONFIG_CLOCK_CONTROL_NRF_ACCURACY < 255
0 if CONFIG_CLOCK_CONTROL_NRF_LFCLK && 0 < 255
255
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_CLOCK_CONTROL_NRF_ACCURACY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_ACCURACY)、[`CONFIG_CLOCK_CONTROL_NRF`](P062_drivers_clock_control_配置项参考_1.md#CONFIG_CLOCK_CONTROL_NRF)、[`CONFIG_CLOCK_CONTROL_NRF_LFCLK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CLOCK_CONTROL_NRF_LFCLK)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_CLOCK_CONTROL_NRF_ACCURACY`、`CONFIG_CLOCK_CONTROL_NRF_LFCLK`。

<a id="CONFIG_IEEE802154_NRF5_EXT_IRQ_MGMT"></a>

## 109.94 `CONFIG_IEEE802154_NRF5_EXT_IRQ_MGMT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

驱动可以自行管理无线电中断请求（IRQ），也可以使用外部无线电 IRQ 提供者。由外部提供者管理时，驱动不得配置无线电 IRQ。系统启用外部无线电 IRQ 提供者时，应启用此选项。动态多协议应用使用的无线电仲裁器（Radio Arbiter）就是外部提供者的一个例子。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**被选择（Selected by）**

```text
CONFIG_NRF_802154_SER_HOST
CONFIG_NRF_802154_SER_HOST
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_NRF_802154_SER_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NRF_802154_SER_HOST)。

<a id="CONFIG_IEEE802154_NRF5_INIT_PRIO"></a>

## 109.95 `CONFIG_IEEE802154_NRF5_INIT_PRIO`

**提示（Prompt）**：nRF52 IEEE 802.15.4 初始化优先级

**说明（Help）**

设置初始化优先级数值。除非清楚其影响，否则不要随意更改。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
80
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5_LOG_RX_FAILURES"></a>

## 109.96 `CONFIG_IEEE802154_NRF5_LOG_RX_FAILURES`

**提示（Prompt）**：帧接收失败日志（Frame Reception Failure Logging）

**说明（Help）**

某些情况下，内部原因可能导致帧接收失败。这些情况以通用错误码向上传递。此选项启用帧接收失败原因的日志记录，有助于分析网络流量，但在高压力环境中也会产生大量日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5_MULTIPLE_CCA"></a>

## 109.97 `CONFIG_IEEE802154_NRF5_MULTIPLE_CCA`

**提示（Prompt）**：支持发送前多次 CCA 尝试（Multiple CCA Attempts）

**说明（Help）**

启用此选项后，`ieee802154_nrf5` 支持 OpenThread 能力 `IEEE802154_OPENTHREAD_HW_MULTIPLE_CCA`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5_RX_STACK_SIZE"></a>

## 109.98 `CONFIG_IEEE802154_NRF5_RX_STACK_SIZE`

**提示（Prompt）**：驱动内部接收线程栈大小（RX Thread Stack Size）

**说明（Help）**

此选项设置驱动内部接收线程的栈大小。默认值应足够使用；如果实际过小，可通过此选项方便地调整。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
800
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5_UICR_EUI64_ENABLE"></a>

## 109.99 `CONFIG_IEEE802154_NRF5_UICR_EUI64_ENABLE`

**提示（Prompt）**：支持使用 UICR 寄存器中保存的 EUI64 值

**说明（Help）**

此选项启用设置保存在用户信息配置寄存器（User Information Configuration Registers，UICR）中的自定义厂商 EUI64 值。注意，这会禁用从工厂信息配置寄存器（Factory Information Configuration Registers，FICR）设置 EUI64 的默认行为。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_IEEE802154_VENDOR_OUI_ENABLE && (CONFIG_SOC_SERIES_NRF52 || CONFIG_SOC_SERIES_NRF53 || CONFIG_SOC_SERIES_NRF54L) && CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_VENDOR_OUI_ENABLE`](P110_drivers_ieee802154_配置项参考_2.md#CONFIG_IEEE802154_VENDOR_OUI_ENABLE)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)、[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_IEEE802154_NRF5_UICR_EUI64_REG"></a>

## 109.100 `CONFIG_IEEE802154_NRF5_UICR_EUI64_REG`

**提示（Prompt）**：保存 EUI64 值的 UICR 起始寄存器（Base Register）

**说明（Help）**

UICR 用户区域中用于保存自定义 EUI64 的两个连续寄存器的起始位置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_IEEE802154_NRF5_UICR_EUI64_ENABLE && CONFIG_IEEE802154_NRF5 && CONFIG_IEEE802154
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 30] if CONFIG_SOC_SERIES_NRF52
[0, 190] if CONFIG_SOC_SERIES_NRF53
[0, 318] if CONFIG_SOC_SERIES_NRF54L
```

**定义位置（Location）**：[`drivers/ieee802154/Kconfig.nrf5:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/ieee802154/Kconfig.nrf5#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → IEEE 802.15.4 驱动 → nRF52 系列 IEEE 802.15.4 驱动 → 支持使用 UICR 寄存器中保存的 EUI64 值

**配置项引用（Symbol References）**：[`CONFIG_IEEE802154_NRF5_UICR_EUI64_ENABLE`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5_UICR_EUI64_ENABLE)、[`CONFIG_IEEE802154_NRF5`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_NRF5)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)、[`CONFIG_SOC_SERIES_NRF52`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF52)、[`CONFIG_SOC_SERIES_NRF53`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_SERIES_NRF54L`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_NRF54L)。

<!-- kconfig-navigation -->

[上一章](P108_drivers_i3c_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P110_drivers_ieee802154_配置项参考_2.md)
