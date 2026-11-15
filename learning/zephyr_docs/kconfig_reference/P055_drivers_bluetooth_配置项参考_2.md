---
id: learning.zephyr-docs.kconfig-reference.page-55
title: "`drivers/bluetooth`配置项参考（2/4）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第55章\_`drivers/bluetooth`配置项参考（2/4）

本章翻译官方 Kconfig 数据库中 `drivers/bluetooth` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_SILABS_EFR32"></a>

## 55.1 `CONFIG_BT_SILABS_EFR32`

**提示（Prompt）**：Silicon Labs EFR32 主机控制器接口驱动（HCI Driver）

**说明（Help）**

使用 Silicon Labs 二进制蓝牙库（Binary Bluetooth Library）连接控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_BT_HCI_EFR32_ENABLED && (CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_SOC_VENDOR_SILABS_HAS_RADIO && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SOC_GECKO_USE_RAIL
CONFIG_PSA_CRYPTO
CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO
CONFIG_HAS_BT_CTLR
CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT
CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT
CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT
CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT
CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT
CONFIG_BT_CTLR_CONN_RSSI_SUPPORT
CONFIG_BT_CTLR_ADV_EXT_SUPPORT
CONFIG_BT_CTLR_PRIVACY_SUPPORT
CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT
CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT
CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT
CONFIG_BT_CTLR_PHY_2M_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_2M
CONFIG_BT_CTLR_PHY_CODED_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_CODED
CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CS
CONFIG_BT_CTLR_DF_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX
CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX
CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_RX
CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_RX
CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX
CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX
CONFIG_BT_SILABS_EFR32_HIGH_POWER if CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_TX_HIGH_POWER
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SOC_GECKO_USE_RAIL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_GECKO_USE_RAIL)、[`CONFIG_PSA_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PSA_CRYPTO)、[`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO)、[`CONFIG_HAS_BT_CTLR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_BT_CTLR)、[`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT)、[`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT)、[`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT)、[`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT)、[`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CONN_RSSI_SUPPORT)、[`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_EXT_SUPPORT)、[`CONFIG_BT_CTLR_PRIVACY_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PRIVACY_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT)、[`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT)、[`CONFIG_BT_CTLR_PHY_2M_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_2M_SUPPORT)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_2M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_2M)、[`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_PHY_CODED_SUPPORT)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_CODED`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_CODED)、[`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CS)、[`CONFIG_BT_CTLR_DF_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_SUPPORT)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX)、[`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT)、[`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_RX)、[`CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT)、[`CONFIG_BT_SILABS_EFR32_HIGH_POWER`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32_HIGH_POWER)、[`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_TX_HIGH_POWER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_TX_HIGH_POWER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_SILABS_MODULE_BLOBS`、`CONFIG_SILABS_SISDK_PROTOCOL_CRYPTO`、`CONFIG_HAS_BT_CTLR`、`CONFIG_BT_CTLR_PHY_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_PER_INIT_FEAT_XCHG_SUPPORT`、`CONFIG_BT_CTLR_DATA_LEN_UPDATE_SUPPORT`、`CONFIG_BT_CTLR_EXT_REJ_IND_SUPPORT`、`CONFIG_BT_CTLR_CHAN_SEL_2_SUPPORT`、`CONFIG_BT_CTLR_CONN_RSSI_SUPPORT`、`CONFIG_BT_CTLR_ADV_EXT_SUPPORT`、`CONFIG_BT_CTLR_PRIVACY_SUPPORT`、`CONFIG_BT_CTLR_SYNC_PERIODIC_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_RECEIVER_SUPPORT`、`CONFIG_BT_CTLR_SYNC_TRANSFER_SENDER_SUPPORT`、`CONFIG_BT_CTLR_PHY_2M_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_2M`、`CONFIG_BT_CTLR_PHY_CODED_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_BLE_CODED`、`CONFIG_BT_CTLR_CHANNEL_SOUNDING_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CS`、`CONFIG_BT_CTLR_DF_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_TX`、`CONFIG_BT_CTLR_DF_CTE_TX_SUPPORT`、`CONFIG_BT_CTLR_DF_CTE_RX_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_CTE_RX`、`CONFIG_BT_CTLR_DF_CTE_RX_SAMPLE_1US_SUPPORT`、`CONFIG_BT_CTLR_DF_ANT_SWITCH_1US_SUPPORT`、`CONFIG_BT_CTLR_DF_ANT_SWITCH_2US_SUPPORT`、`CONFIG_SOC_VENDOR_SILABS_HAS_RADIO_TX_HIGH_POWER`。

<a id="CONFIG_BT_SILABS_EFR32_ACCEPT_LIST_SIZE"></a>

## 55.2 `CONFIG_BT_SILABS_EFR32_ACCEPT_LIST_SIZE`

**提示（Prompt）**：接受列表大小（Accept List Size）

**说明（Help）**

接受列表（Accept List）的大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_ACTIVATE_POWER_CONTROL"></a>

## 55.3 `CONFIG_BT_SILABS_EFR32_ACTIVATE_POWER_CONTROL`

**提示（Prompt）**：EFR32 低功耗蓝牙功率控制（LE Power Control）

**说明（Help）**

启用功率控制（Power Control），根据接收信号强度调整发射功率。控制器会要求发射方调整功率，使接收数据包的接收信号强度指示（RSSI）保持在理想范围（Golden Range）内；每种物理层（PHY）分别指定其范围。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_BUFFER_MEMORY"></a>

## 55.4 `CONFIG_BT_SILABS_EFR32_BUFFER_MEMORY`

**提示（Prompt）**：内存缓冲区大小（Memory Buffer Size）

**说明（Help）**

选择为 Silicon Labs 蓝牙库（Bluetooth Library）分配的内存缓冲区大小。设置过小可能影响链路层（Link Layer）的处理能力。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
6144
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_COMPLETED_PACKETS_THRESHOLD"></a>

## 55.5 `CONFIG_BT_SILABS_EFR32_COMPLETED_PACKETS_THRESHOLD`

**提示（Prompt）**：已完成数据包报告阈值（Completed Packet Reporting Threshold）

**说明（Help）**

触发 HCI 已完成数据包数量事件（Number Of Completed Packets）的已通过空中接口发送的异步连接逻辑传输（ACL）包数量。大多数情况下应设为 1，因为主机协议栈（Host Stack）使用它判断数据包是否已通过无线接口发送。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_COMPLETED_PACKETS_TIMEOUT"></a>

## 55.6 `CONFIG_BT_SILABS_EFR32_COMPLETED_PACKETS_TIMEOUT`

**提示（Prompt）**：已完成数据包报告事件超时（Completed Packet Report Event Timeout）

**说明（Help）**

自上一次 HCI 已完成数据包数量事件（Number Of Completed Packets）起，允许经过的最大连接事件（Connection Event）数量；达到此数量后，触发对所有已完成但尚未报告的 ACL 数据包的报告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_1M"></a>

## 55.7 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_1M`

**提示（Prompt）**：1M PHY 理想 RSSI 范围上限（Golden RSSI Upper Bound）

**说明（Help）**

1M 物理层（PHY）的接收信号强度指示（RSSI）理想范围上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-40
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_2M"></a>

## 55.8 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_2M`

**提示（Prompt）**：2M PHY 理想 RSSI 范围上限（Golden RSSI Upper Bound）

**说明（Help）**

2M 物理层（PHY）的接收信号强度指示（RSSI）理想范围上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-40
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_CODED_S2"></a>

## 55.9 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_CODED_S2`

**提示（Prompt）**：编码 S=2 PHY 理想 RSSI 范围上限（Coded PHY Golden RSSI Upper Bound）

**说明（Help）**

编码参数为 `S=2` 的物理层（Coded PHY）的接收信号强度指示（RSSI）理想范围上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-40
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_CODED_S8"></a>

## 55.10 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MAX_CODED_S8`

**提示（Prompt）**：编码 S=8 PHY 理想 RSSI 范围上限（Coded PHY Golden RSSI Upper Bound）

**说明（Help）**

编码参数为 `S=8` 的物理层（Coded PHY）的接收信号强度指示（RSSI）理想范围上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-40
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_1M"></a>

## 55.11 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_1M`

**提示（Prompt）**：1M PHY 理想 RSSI 范围下限（Golden RSSI Lower Bound）

**说明（Help）**

1M 物理层（PHY）的接收信号强度指示（RSSI）理想范围下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-60
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_2M"></a>

## 55.12 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_2M`

**提示（Prompt）**：2M PHY 理想 RSSI 范围下限（Golden RSSI Lower Bound）

**说明（Help）**

2M 物理层（PHY）的接收信号强度指示（RSSI）理想范围下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-60
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_CODED_S2"></a>

## 55.13 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_CODED_S2`

**提示（Prompt）**：编码 S=2 PHY 理想 RSSI 范围下限（Coded PHY Golden RSSI Lower Bound）

**说明（Help）**

编码参数为 `S=2` 的物理层（Coded PHY）的接收信号强度指示（RSSI）理想范围下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-60
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_CODED_S8"></a>

## 55.14 `CONFIG_BT_SILABS_EFR32_GOLDEN_RSSI_MIN_CODED_S8`

**提示（Prompt）**：编码 S=8 PHY 理想 RSSI 范围下限（Coded PHY Golden RSSI Lower Bound）

**说明（Help）**

编码参数为 `S=8` 的物理层（Coded PHY）的接收信号强度指示（RSSI）理想范围下限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_TRANSMIT_POWER_CONTROL && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
-60
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_HCI_VS"></a>

## 55.15 `CONFIG_BT_SILABS_EFR32_HCI_VS`

**提示（Prompt）**：Silicon Labs 厂商专用 HCI 扩展（Vendor-Specific HCI Extensions）

**说明（Help）**

启用 Silicon Labs 厂商专用主机控制器接口（HCI）扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_HIGH_POWER"></a>

## 55.16 `CONFIG_BT_SILABS_EFR32_HIGH_POWER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通常发射功率（Transmit Power）限制为 10 dBm。对于支持高功率放大器（High-Power PA）的设备，会自动启用此选项，允许控制器以更高功率发射。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**被选择（Selected by）**

```text
CONFIG_BT_SILABS_EFR32
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_HIGH_POWER_AFH"></a>

## 55.17 `CONFIG_BT_SILABS_EFR32_HIGH_POWER_AFH`

**提示（Prompt）**：高功率发射器的自适应跳频（Adaptive Frequency Hopping）

**说明（Help）**

使用高发射功率时，为符合监管要求（Regulatory Requirements），控制器可能需要执行自适应跳频（Adaptive Frequency Hopping）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32_HIGH_POWER && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32_HIGH_POWER`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32_HIGH_POWER)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_LINK_LAYER_STACK_SIZE"></a>

## 55.18 `CONFIG_BT_SILABS_EFR32_LINK_LAYER_STACK_SIZE`

**提示（Prompt）**：链路层线程栈大小（Link Layer Thread Stack Size）

**说明（Help）**

链路层（Link Layer）线程的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2048 if CONFIG_SOC_FAMILY_SILABS_S3
1024
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SOC_FAMILY_SILABS_S3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_SILABS_S3)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_SILABS_S3`。

<a id="CONFIG_BT_SILABS_EFR32_MAX_CS_CONFIGS_PER_CONNECTION"></a>

## 55.19 `CONFIG_BT_SILABS_EFR32_MAX_CS_CONFIGS_PER_CONNECTION`

**提示（Prompt）**：每个连接的最大信道探测配置数量（CS Configurations）

**说明（Help）**

定义应用在每个蓝牙连接中需要的信道探测（Channel Sounding，CS）配置数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_CS_PROCEDURES"></a>

## 55.20 `CONFIG_BT_SILABS_EFR32_MAX_CS_PROCEDURES`

**提示（Prompt）**：每个 CS 配置的最大信道探测过程数量（CS Procedures）

**说明（Help）**

定义应用在每个信道探测（Channel Sounding）配置中需要的信道探测过程数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_PAWR_ADVERTISED_DATA_LENGTH_HINT"></a>

## 55.21 `CONFIG_BT_SILABS_EFR32_MAX_PAWR_ADVERTISED_DATA_LENGTH_HINT`

**提示（Prompt）**：向控制器提示 PAwR 最大数据长度（Maximum PAwR Data Length Hint）

**说明（Help）**

应用预期在带响应周期性广播（Periodic Advertising with Response，PAwR）数据包中发送的最大数据长度。控制器使用此提示优化并发连接调度（Concurrent Connection Scheduling）。该值不妨碍使用更长的数据长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_RSP && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
61
```

**取值范围（Ranges）**

```text
[0, 251]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_PAWR_ADVERTISERS"></a>

## 55.22 `CONFIG_BT_SILABS_EFR32_MAX_PAWR_ADVERTISERS`

**提示（Prompt）**：带响应周期性广播的最大发布者数量（PAwR Advertisers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_RSP && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, CONFIG_BT_SILABS_EFR32_MAX_PERIODIC_ADVERTISERS]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SILABS_EFR32_MAX_PERIODIC_ADVERTISERS`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32_MAX_PERIODIC_ADVERTISERS)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_PAWR_SYNCHRONIZERS"></a>

## 55.23 `CONFIG_BT_SILABS_EFR32_MAX_PAWR_SYNCHRONIZERS`

**提示（Prompt）**：最大 PAwR 同步器数量（PAwR Synchronizers）

**说明（Help）**

定义应用使用带响应周期性广播（Periodic Advertising with Responses）时需要同时运行的周期性同步实例（Periodic Synchronizing Instances）数量。该值不得超过周期性广播同步实例的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_SYNC && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_PER_ADV_SYNC_MAX]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_PER_ADV_SYNC_MAX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_MAX)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_PERIODIC_ADVERTISERS"></a>

## 55.24 `CONFIG_BT_SILABS_EFR32_MAX_PERIODIC_ADVERTISERS`

**提示（Prompt）**：周期性广播发布者的最大数量（Periodic Advertisers）

**说明（Help）**

定义应用需要同时使用的周期性广播实例（Periodic Advertising Instances）数量。该值不得超过广播集（Advertisement Set）的总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, CONFIG_BT_EXT_ADV_MAX_ADV_SET]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:149`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L149)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_EXT_ADV_MAX_ADV_SET`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV_MAX_ADV_SET)。

<a id="CONFIG_BT_SILABS_EFR32_MAX_QUEUED_ADV_REPORTS"></a>

## 55.25 `CONFIG_BT_SILABS_EFR32_MAX_QUEUED_ADV_REPORTS`

**提示（Prompt）**：最大排队广播报告数量（Queued Advertising Reports）

**说明（Help）**

允许排队的广播报告（Advertising Report）最大数量。超出的广播报告会被丢弃。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_PAWR_PACKET_REQUEST_ADVANCE"></a>

## 55.26 `CONFIG_BT_SILABS_EFR32_PAWR_PACKET_REQUEST_ADVANCE`

**提示（Prompt）**：提前请求 PAwR 数据的子事件数量（Subevent Request Advance）

**说明（Help）**

在子事件（Subevent）通过无线接口发送之前，控制器会请求主机提供即将发生的子事件所需的数据。此参数配置请求提前多少个子事件发送给主机。提前量越大，主机处理请求的时间越多，但控制器必须预留更多内存缓冲子事件数据。

注意，最大提前量受 PAwR 广播序列（PAwR Train）所配置的子事件数量限制，因此实际提前量可能小于此参数设定的数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_RSP && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 6]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_PAWR_PACKET_REQUEST_COUNT"></a>

## 55.27 `CONFIG_BT_SILABS_EFR32_PAWR_PACKET_REQUEST_COUNT`

**提示（Prompt）**：每次请求从主机获取的 PAwR 数据包数量（Packets per Request）

**说明（Help）**

控制器在一次低功耗周期性广播子事件数据请求事件（LE Periodic Advertising Subevent Data Request）中向主机请求的数据包数量。这是在控制器内存用量与需要发送的独立 HCI 事件数量之间进行权衡。

此值分别应用于每个 PAwR 广播发布者（Advertiser）。注意，请求数量受 PAwR 广播序列（PAwR Train）的子事件数量和请求提前量配置限制。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_PER_ADV_RSP && CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 12]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_EFR32_USER_ADVERTISERS"></a>

## 55.28 `CONFIG_BT_SILABS_EFR32_USER_ADVERTISERS`

**提示（Prompt）**：用户广播集（User Advertisement Sets）

**说明（Help）**

为应用预留的广播集（Advertisement Set）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SILABS_EFR32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → Silicon Labs EFR32 主机控制器接口驱动（HCI Driver） → EFR32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_SILABS_EFR32`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SILABS_EFR32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SILABS_SIWX91X"></a>

## 55.29 `CONFIG_BT_SILABS_SIWX91X`

**提示（Prompt）**：Silicon Labs SiWx91x 蓝牙接口（Bluetooth Interface）

**说明（Help）**

使用 Silicon Labs Wiseconnect 3.x 蓝牙库（Bluetooth Library）连接控制器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_SILABS_SIWX91X_BT_HCI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SILABS_SIWX91X_NWP
CONFIG_ENTROPY_GENERATOR
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.silabs:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.silabs#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SILABS_SIWX91X_NWP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SILABS_SIWX91X_NWP)、[`CONFIG_ENTROPY_GENERATOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_GENERATOR)。

<a id="CONFIG_BT_SPI"></a>

## 55.30 `CONFIG_BT_SPI`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

支持使用 SPI 作为通信协议的蓝牙集成电路（Bluetooth IC）。主机控制器接口（HCI）数据包按单字节传输方式发送和接收，并在数据包前添加已知的头部（Header）。不同器件的头部可能不同，因此增加器件支持时，可能还需要补充平台专用信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_SPI
```

**被选择（Selected by）**

```text
CONFIG_BT_SPI_ZEPHYR
CONFIG_BT_SPI_BLUENRG
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SPI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SPI)、[`CONFIG_BT_SPI_ZEPHYR`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI_ZEPHYR)、[`CONFIG_BT_SPI_BLUENRG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI_BLUENRG)。

<a id="CONFIG_BT_SPI_BLUENRG"></a>

## 55.31 `CONFIG_BT_SPI_BLUENRG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 SPI 传输蓝牙主机控制器接口（Bluetooth HCI）数据的驱动，用于与意法半导体（STMicroelectronics）BlueNRG 器件通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(DT_HAS_ST_HCI_SPI_V1_ENABLED || DT_HAS_ST_HCI_SPI_V2_ENABLED) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_SPI
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SPI`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI)。

<a id="CONFIG_BT_SPI_BOOT_TIMEOUT_SEC"></a>

## 55.32 `CONFIG_BT_SPI_BOOT_TIMEOUT_SEC`

**提示（Prompt）**：等待 SPI 器件报告就绪的秒数（Ready Timeout）

**说明（Help）**

等待 HCI SPI 控制器通过 Zephyr 项目定义的 `EVT_BLUE_INITIALIZED` 厂商专用 HCI 事件报告就绪（Ready）的最长时间。默认为 30 秒，以支持控制器上的引导加载程序镜像交换（Bootloader Image Swap）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_BT_SPI_ZEPHYR || CONFIG_BT_SPI_BLUENRG) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_SPI_ZEPHYR`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI_ZEPHYR)、[`CONFIG_BT_SPI_BLUENRG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI_BLUENRG)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SPI_INIT_PRIORITY"></a>

## 55.33 `CONFIG_BT_SPI_INIT_PRIORITY`

**提示（Prompt）**：蓝牙 SPI 初始化优先级（BT SPI Init Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_SPI && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
75
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_SPI`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_SPI_ZEPHYR"></a>

## 55.34 `CONFIG_BT_SPI_ZEPHYR`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过 SPI 传输蓝牙主机控制器接口（Bluetooth HCI）数据的驱动，用于与运行 Zephyr 的蓝牙控制器通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ZEPHYR_BT_HCI_SPI_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_BT_SPI
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_SPI`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_SPI)。

<a id="CONFIG_BT_STM32WB0"></a>

## 55.35 `CONFIG_BT_STM32WB0`

**提示（Prompt）**：STM32WB0 主机控制器接口驱动（HCI Driver）

**说明（Help）**

ST STM32WB0 HCI 蓝牙接口（HCI Bluetooth Interface）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_HCI_STM32WB0_ENABLED && CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_STM32LIB
CONFIG_USE_STM32_HAL_PKA
CONFIG_USE_STM32_HAL_CORTEX
CONFIG_USE_STM32_HAL_GPIO
CONFIG_USE_STM32_HAL_RADIO
CONFIG_USE_STM32_HAL_RADIO_TIMER
CONFIG_BT_SYSTEM_WORKQUEUE_COOP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:139`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L139)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)、[`CONFIG_USE_STM32_HAL_PKA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_PKA)、[`CONFIG_USE_STM32_HAL_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_CORTEX)、[`CONFIG_USE_STM32_HAL_GPIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_GPIO)、[`CONFIG_USE_STM32_HAL_RADIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_RADIO)、[`CONFIG_USE_STM32_HAL_RADIO_TIMER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_RADIO_TIMER)、[`CONFIG_BT_SYSTEM_WORKQUEUE_COOP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SYSTEM_WORKQUEUE_COOP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`、`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_BT_STM32WBA"></a>

## 55.36 `CONFIG_BT_STM32WBA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

ST STM32WBA HCI 蓝牙接口（HCI Bluetooth Interface）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_HCI_STM32WBA_ENABLED && (CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS || CONFIG_BUILD_ONLY_NO_BLOBS) && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_HAS_STM32LIB
CONFIG_BT_HCI_SET_PUBLIC_ADDR if !CONFIG_BT_HCI_RAW
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS)、[`CONFIG_BUILD_ONLY_NO_BLOBS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BUILD_ONLY_NO_BLOBS)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)、[`CONFIG_BT_HCI_SET_PUBLIC_ADDR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_HCI_SET_PUBLIC_ADDR)、[`CONFIG_BT_HCI_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_RAW)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ZEPHYR_HAL_STM32_MODULE_BLOBS`、`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_BT_STM32WBA_BASIC_LIB"></a>

## 55.37 `CONFIG_BT_STM32WBA_BASIC_LIB`

**提示（Prompt）**：STM32WBA 蓝牙库基本配置（Basic Configuration）

**说明（Help）**

在 STM32WBA 中加入以下基本蓝牙功能支持：广播（Advertising）、扫描（Scanning）、外设和中心设备连接（Peripheral and Central Connections）、隐私（Privacy）、信道选择算法 2（Channel Selection Algorithm #2）、数据长度扩展（Data Length Extension）、低功耗加密（LE Encryption）、传统配对（Legacy Pairing）、低功耗安全连接（LE Secure Connections）、LE 2Mbit 物理层（PHY）及 LE 编码物理层（Coded PHY）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_STM32WBA_LIB_CONFIG>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WBA 蓝牙配置（Bluetooth Configuration） → STM32WBA 蓝牙库配置（Bluetooth Library Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA_LIB_CONFIG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_LIB_CONFIG)。

<a id="CONFIG_BT_STM32WBA_BASIC_PLUS_LIB"></a>

## 55.38 `CONFIG_BT_STM32WBA_BASIC_PLUS_LIB`

**提示（Prompt）**：STM32WBA 蓝牙库增强基本配置（Basic Plus Configuration）

**说明（Help）**

在 STM32WBA 中加入以下增强基本蓝牙功能支持：广播（Advertising）、扫描（Scanning）、外设和中心设备连接（Peripheral and Central Connections）、隐私（Privacy）、信道选择算法 2（Channel Selection Algorithm #2）、数据长度扩展（Data Length Extension）、低功耗加密（LE Encryption）、传统配对（Legacy Pairing）、低功耗安全连接（LE Secure Connections）、LE 2Mbit 物理层（PHY）、LE 编码物理层（Coded PHY）、扩展广播（Extended Advertising）、低功耗功率控制（LE Power Control）和连接子速率（Connection Subrating）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_STM32WBA_LIB_CONFIG>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WBA 蓝牙配置（Bluetooth Configuration） → STM32WBA 蓝牙库配置（Bluetooth Library Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA_LIB_CONFIG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_LIB_CONFIG)。

<a id="CONFIG_BT_STM32WBA_FULL_LIB"></a>

## 55.39 `CONFIG_BT_STM32WBA_FULL_LIB`

**提示（Prompt）**：STM32WBA 蓝牙库完整配置（Full Configuration）

**说明（Help）**

在 STM32WBA 中加入完整的蓝牙功能（Bluetooth Features）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_STM32WBA_LIB_CONFIG>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WBA 蓝牙配置（Bluetooth Configuration） → STM32WBA 蓝牙库配置（Bluetooth Library Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA_LIB_CONFIG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_LIB_CONFIG)。

<a id="CONFIG_BT_STM32WBA_LIB_CONFIG"></a>

## 55.40 `CONFIG_BT_STM32WBA_LIB_CONFIG`

**提示（Prompt）**：STM32WBA 蓝牙库配置（Bluetooth Library Configuration）

**说明（Help）**

根据所需蓝牙功能（Bluetooth Features）设置库配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32WBA && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_BT_STM32WBA_FULL_LIB if CONFIG_BT_PER_ADV || CONFIG_BT_PER_ADV_SYNC || CONFIG_BT_SCA_UPDATE || CONFIG_BT_DF_CTE_RX_AOA || CONFIG_BT_CTLR_DF_ANT_SWITCH_RX || CONFIG_BT_CTLR_DF_ANT_SWITCH_TX || CONFIG_BT_DF_CTE_TX_AOD || CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER || CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER || CONFIG_BT_CTLR_SYNC_PERIODIC || CONFIG_BT_ISO_UNICAST || CONFIG_BT_ISO_BROADCASTER || CONFIG_BT_ISO_SYNC_RECEIVER || CONFIG_BT_CTLR_ADV_PERIODIC_ADI_SUPPORT || CONFIG_BT_EXT_ADV_CODING_SELECTION
CONFIG_BT_STM32WBA_BASIC_PLUS_LIB if CONFIG_BT_EXT_ADV || CONFIG_BT_TRANSMIT_POWER_CONTROL || CONFIG_BT_SUBRATING
CONFIG_BT_STM32WBA_BASIC_LIB
```

**可选项（Choices）**

```text
CONFIG_BT_STM32WBA_BASIC_LIB
CONFIG_BT_STM32WBA_BASIC_PLUS_LIB
CONFIG_BT_STM32WBA_FULL_LIB
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WBA 蓝牙配置（Bluetooth Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_BT_STM32WBA_FULL_LIB`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_FULL_LIB)、[`CONFIG_BT_PER_ADV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV)、[`CONFIG_BT_PER_ADV_SYNC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC)、[`CONFIG_BT_SCA_UPDATE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SCA_UPDATE)、[`CONFIG_BT_DF_CTE_RX_AOA`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CTE_RX_AOA)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_RX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_RX)、[`CONFIG_BT_CTLR_DF_ANT_SWITCH_TX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_DF_ANT_SWITCH_TX)、[`CONFIG_BT_DF_CTE_TX_AOD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_DF_CTE_TX_AOD)、[`CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_RECEIVER)、[`CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_TRANSFER_SENDER)、[`CONFIG_BT_CTLR_SYNC_PERIODIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_SYNC_PERIODIC)、[`CONFIG_BT_ISO_UNICAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_UNICAST)、[`CONFIG_BT_ISO_BROADCASTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_BROADCASTER)、[`CONFIG_BT_ISO_SYNC_RECEIVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO_SYNC_RECEIVER)、[`CONFIG_BT_CTLR_ADV_PERIODIC_ADI_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CTLR_ADV_PERIODIC_ADI_SUPPORT)、[`CONFIG_BT_EXT_ADV_CODING_SELECTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EXT_ADV_CODING_SELECTION)、[`CONFIG_BT_STM32WBA_BASIC_PLUS_LIB`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_BASIC_PLUS_LIB)、[`CONFIG_BT_EXT_ADV`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT_EXT_ADV)、[`CONFIG_BT_TRANSMIT_POWER_CONTROL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TRANSMIT_POWER_CONTROL)、[`CONFIG_BT_SUBRATING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_SUBRATING)、[`CONFIG_BT_STM32WBA_BASIC_LIB`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA_BASIC_LIB)。

<a id="CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB"></a>

## 55.41 `CONFIG_BT_STM32WBA_USE_TEMP_BASED_CALIB`

**提示（Prompt）**：基于温度传感器的 STM32WBA 无线电校准（Radio Calibration）

**说明（Help）**

允许链路层（Link Layer）根据从 ADC4 读取的当前温度进行自身校准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32WBA && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_SENSOR
CONFIG_STM32_TEMP
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WBA 蓝牙配置（Bluetooth Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32WBA`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32WBA)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_SENSOR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SENSOR)、[`CONFIG_STM32_TEMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STM32_TEMP)。

<a id="CONFIG_BT_STM32_IPM"></a>

## 55.42 `CONFIG_BT_STM32_IPM`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

STM32WB 主机控制器接口（HCI）驱动，使用 CPU1 与 CPU2 上无线协处理器（Wireless Coprocessor）之间的共享内存传输（Shared Memory Transport）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
DT_HAS_ST_STM32WB_RF_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_USE_STM32_HAL_CORTEX
CONFIG_HAS_STM32LIB
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_USE_STM32_HAL_CORTEX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_STM32_HAL_CORTEX)、[`CONFIG_HAS_STM32LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAS_STM32LIB)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_HAS_STM32LIB`。

<a id="CONFIG_BT_STM32_IPM_FW_CHECK_STRICT"></a>

## 55.43 `CONFIG_BT_STM32_IPM_FW_CHECK_STRICT`

**提示（Prompt）**：STM32WB 无线固件不匹配时使初始化失败（Firmware Mismatch）

**说明（Help）**

启用后，如果检测到 CPU2 无线固件协议栈类型（Stack Type）或版本与预期不一致，则蓝牙初始化失败。禁用后，不匹配只记录为警告，初始化继续。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM_FW_INFO_CHECK && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → STM32WB 无线固件运行时检查（Runtime Check）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM_FW_INFO_CHECK`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM_FW_INFO_CHECK)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_STM32_IPM_FW_INFO_CHECK"></a>

## 55.44 `CONFIG_BT_STM32_IPM_FW_INFO_CHECK`

**提示（Prompt）**：STM32WB 无线固件运行时检查（Runtime Check）

**说明（Help）**

在运行时验证 CPU2 上运行的 STM32WB 无线协议栈（Wireless Stack）的类型和版本，是否与驱动预期一致。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.stm32:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.stm32#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LOG)。

<a id="CONFIG_BT_STM32_IPM_RX_STACK_SIZE"></a>

## 55.45 `CONFIG_BT_STM32_IPM_RX_STACK_SIZE`

**提示（Prompt）**：STM32 IPM 接收线程栈大小（RX Thread Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_STM32_IPM && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_BT_STM32_IPM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_BT_STM32_IPM)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_BT_USERCHAN"></a>

## 55.46 `CONFIG_BT_USERCHAN`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

通过连接 Linux 内核的用户通道 HCI 套接字（User Channel HCI Socket），访问本地 Linux 主机的蓝牙适配器（Bluetooth Adapter）。也可以连接 UNIX 套接字或 TCP HCI 端点（Endpoint）。

此驱动用于基于原生模拟器（Native Simulator）、以实时方式运行的目标，包括树外开发板（Out-of-Tree Boards）。使用本地蓝牙适配器时，必须先关闭其电源状态（Powered Off），Zephyr 才能使用它。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NATIVE_LIBRARY && DT_HAS_ZEPHYR_BT_HCI_USERCHAN_ENABLED && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NATIVE_LIBRARY`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_NATIVE_LIBRARY)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)。

<a id="CONFIG_CYW20829"></a>

## 55.47 `CONFIG_CYW20829`

**提示（Prompt）**：CYW20829

**说明（Help）**

启用英飞凌（Infineon）CYW20829 低功耗蓝牙（BLE）连接功能。更多信息见[CYW20829 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-bluetooth-le-bluetooth-multiprotocol/airoc-bluetooth-le/cyw20829/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CYW208XX && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_CYW208XX`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_CYW208XX)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW20829B0_BT_FW_ISOC_TX0"></a>

## 55.48 `CONFIG_CYW20829B0_BT_FW_ISOC_TX0`

**提示（Prompt）**：CYW20829B0_BT_FW_ISOC_TX0

**说明（Help）**

启用发射功率（TX Power）为 0 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与等时（ISOC）应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B0_BT_FW_ISOC_TX10"></a>

## 55.49 `CONFIG_CYW20829B0_BT_FW_ISOC_TX10`

**提示（Prompt）**：CYW20829B0_BT_FW_ISOC_TX10

**说明（Help）**

启用发射功率（TX Power）为 10 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与等时（ISOC）应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B0_BT_FW_PAWR_TX0"></a>

## 55.50 `CONFIG_CYW20829B0_BT_FW_PAWR_TX0`

**提示（Prompt）**：CYW20829B0_BT_FW_PAWR_TX0

**说明（Help）**

启用支持带响应周期性广播（PAwR）、发射功率（TX Power）为 0 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与 PAwR 应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B0_BT_FW_PAWR_TX10"></a>

## 55.51 `CONFIG_CYW20829B0_BT_FW_PAWR_TX10`

**提示（Prompt）**：CYW20829B0_BT_FW_PAWR_TX10

**说明（Help）**

启用发射功率（TX Power）为 10 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与带响应周期性广播（PAwR）应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B0_BT_FW_TX0"></a>

## 55.52 `CONFIG_CYW20829B0_BT_FW_TX0`

**提示（Prompt）**：CYW20829B0_BT_FW_TX0

**说明（Help）**

启用发射功率（TX Power）为 0 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与既不使用带响应周期性广播（PAwR）、也不使用等时（ISOC）功能的应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B0_BT_FW_TX10"></a>

## 55.53 `CONFIG_CYW20829B0_BT_FW_TX10`

**提示（Prompt）**：CYW20829B0_BT_FW_TX10

**说明（Help）**

启用发射功率（TX Power）为 10 dBm 的 CYW20829B0 固件补丁（FW Patch）。此配置应与既不使用带响应周期性广播（PAwR）、也不使用等时（ISOC）功能的应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B1_BT_FW_TX0"></a>

## 55.54 `CONFIG_CYW20829B1_BT_FW_TX0`

**提示（Prompt）**：CYW20829B1_BT_FW_TX0

**说明（Help）**

启用发射功率（TX Power）为 0 dBm 的 CYW20829B1 固件补丁（FW Patch）。此配置应与既不使用带响应周期性广播（PAwR）、也不使用等时（ISOC）功能的应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829B1_BT_FW_TX10"></a>

## 55.55 `CONFIG_CYW20829B1_BT_FW_TX10`

**提示（Prompt）**：CYW20829B1_BT_FW_TX10

**说明（Help）**

启用发射功率（TX Power）为 10 dBm 的 CYW20829B1 固件补丁（FW Patch）。此配置应与既不使用带响应周期性广播（PAwR）、也不使用等时（ISOC）功能的应用配合使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:222`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L222)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

<a id="CONFIG_CYW20829_BT_FW"></a>

## 55.56 `CONFIG_CYW20829_BT_FW`

**提示（Prompt）**：选择默认 CYW20829 蓝牙固件变体（BT FW Variant）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW20829 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_CYW20829B0_BT_FW_ISOC_TX10 if CONFIG_BT_ISO && CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B0_BT_FW_ISOC_TX0 if CONFIG_BT_ISO && !CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B0_BT_FW_PAWR_TX10 if (CONFIG_BT_PER_ADV_RSP || CONFIG_BT_PER_ADV_SYNC_RSP) && CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B0_BT_FW_PAWR_TX0 if (CONFIG_BT_PER_ADV_RSP || CONFIG_BT_PER_ADV_SYNC_RSP) && !CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B0_BT_FW_TX10 if CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B0_BT_FW_TX0 if n
CONFIG_CYW20829B1_BT_FW_TX10 if CONFIG_CYW20829_BT_FW_TX10DBM_POWER && n
CONFIG_CYW20829B1_BT_FW_TX0 if n
```

**可选项（Choices）**

```text
CONFIG_CYW20829B0_BT_FW_TX0
CONFIG_CYW20829B0_BT_FW_TX10
CONFIG_CYW20829B0_BT_FW_PAWR_TX0
CONFIG_CYW20829B0_BT_FW_PAWR_TX10
CONFIG_CYW20829B0_BT_FW_ISOC_TX0
CONFIG_CYW20829B0_BT_FW_ISOC_TX10
CONFIG_CYW20829B1_BT_FW_TX0
CONFIG_CYW20829B1_BT_FW_TX10
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW20829`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW20829B0_BT_FW_ISOC_TX10`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_ISOC_TX10)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_CYW20829_BT_FW_TX10DBM_POWER`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829_BT_FW_TX10DBM_POWER)、[`CONFIG_CYW20829B0_BT_FW_ISOC_TX0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_ISOC_TX0)、[`CONFIG_CYW20829B0_BT_FW_PAWR_TX10`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_PAWR_TX10)、[`CONFIG_BT_PER_ADV_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_RSP)、[`CONFIG_BT_PER_ADV_SYNC_RSP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_PER_ADV_SYNC_RSP)、[`CONFIG_CYW20829B0_BT_FW_PAWR_TX0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_PAWR_TX0)、[`CONFIG_CYW20829B0_BT_FW_TX10`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_TX10)、[`CONFIG_CYW20829B0_BT_FW_TX0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B0_BT_FW_TX0)、[`CONFIG_CYW20829B1_BT_FW_TX10`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B1_BT_FW_TX10)、[`CONFIG_CYW20829B1_BT_FW_TX0`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829B1_BT_FW_TX0)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`。

<a id="CONFIG_CYW20829_BT_FW_TX10DBM_POWER"></a>

## 55.57 `CONFIG_CYW20829_BT_FW_TX10DBM_POWER`

**提示（Prompt）**：CYW20829_BT_FW_TX10DBM_POWER

**说明（Help）**

启用 CYW20829 固件补丁（FW Patch）的 10 dBm 发射功率（TX Power）变体。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW20829 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW20829`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW20829)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_CYW43012"></a>

## 55.58 `CONFIG_CYW43012`

原库同名定义共 2 条；本项为数据库第 4587 条记录，各定义分别保留。

**提示（Prompt）**：CYW43012

**说明（Help）**

启用英飞凌（Infineon）CYW43012 低功耗蓝牙（BLE）连接功能。更多信息见[CYW43012 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43012/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43012_MODULE"></a>

## 55.59 `CONFIG_CYW43012_MODULE`

原库同名定义共 2 条；本项为数据库第 4589 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW43012 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW43012 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW43012_MURATA_1LV
CONFIG_CYW43012_MURATA_1LV
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW43012`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW43012_MURATA_1LV`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012_MURATA_1LV)。

<a id="CONFIG_CYW43012_MURATA_1LV"></a>

## 55.60 `CONFIG_CYW43012_MURATA_1LV`

原库同名定义共 2 条；本项为数据库第 4591 条记录，各定义分别保留。

**提示（Prompt）**：MURATA-1LV

**说明（Help）**

村田（Murata）Type 1LV 模块基于英飞凌（Infineon）CYW43012 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11a/b/g/n 与 Bluetooth® 5.0 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 72.2 Mbps，蓝牙 PHY 数据速率最高 3 Mbps，也支持 2 Mbps LE PHY。更多信息见[村田 Type 1LV 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1lv)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43012_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 CYW43012 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW43012_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43012_MODULE)。

<a id="CONFIG_CYW43438"></a>

## 55.61 `CONFIG_CYW43438`

原库同名定义共 2 条；本项为数据库第 4596 条记录，各定义分别保留。

**提示（Prompt）**：CYW43438

**说明（Help）**

启用英飞凌（Infineon）CYW43438 低功耗蓝牙（BLE）连接功能。更多信息见[CYW43438 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43438/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43439"></a>

## 55.62 `CONFIG_CYW43439`

原库同名定义共 2 条；本项为数据库第 4598 条记录，各定义分别保留。

**提示（Prompt）**：CYW43439

**说明（Help）**

启用英飞凌（Infineon）CYW43439 低功耗蓝牙（BLE）连接功能。更多信息见[CYW43439 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw43439/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW43439_MODULE"></a>

## 55.63 `CONFIG_CYW43439_MODULE`

原库同名定义共 2 条；本项为数据库第 4600 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW43439 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW43439 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW43439_MURATA_1YN
CONFIG_CYW43439_MURATA_1YN
CONFIG_CYW43439_STERLING_LWBPLUS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW43439`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW43439_MURATA_1YN`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439_MURATA_1YN)、[`CONFIG_CYW43439_STERLING_LWBPLUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW43439_STERLING_LWBPLUS)。

<a id="CONFIG_CYW43439_MURATA_1YN"></a>

## 55.64 `CONFIG_CYW43439_MURATA_1YN`

原库同名定义共 2 条；本项为数据库第 4602 条记录，各定义分别保留。

**提示（Prompt）**：MURATA_1YN

**说明（Help）**

村田（Murata）Type 1YN 模块基于英飞凌（Infineon）CYW43439 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11b/g/n 与 Bluetooth® 5.2 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 65 Mbps，蓝牙 PHY 数据速率最高 3 Mbps。更多信息见[村田 Type 1YN 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1yn)。

译注：此处 Bluetooth 5.2 保留自 Zephyr 官方配置数据库。2026-10-17 核验所引村田 Type 1YN 官方页面时，其 Description 和 Specs 写为 Bluetooth 5.1；两份来源存在版本差异，不能把本条译文当作独立确认的硬件版本规格。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW43439_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 CYW43439 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW43439_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW43439_MODULE)。

<a id="CONFIG_CYW4343W"></a>

## 55.65 `CONFIG_CYW4343W`

原库同名定义共 2 条；本项为数据库第 4605 条记录，各定义分别保留。

**提示（Prompt）**：CYW4343W

**说明（Help）**

启用英飞凌（Infineon）CYW4343W 低功耗蓝牙（BLE）连接功能。更多信息见[CYW4343W 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw4343w/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW4343W_MODULE"></a>

## 55.66 `CONFIG_CYW4343W_MODULE`

原库同名定义共 2 条；本项为数据库第 4607 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW4343W 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW4343W && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW4343W_MURATA_1DX
CONFIG_CYW4343W_MURATA_1DX
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW4343W`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW4343W_MURATA_1DX`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W_MURATA_1DX)。

<a id="CONFIG_CYW4343W_MURATA_1DX"></a>

## 55.67 `CONFIG_CYW4343W_MURATA_1DX`

原库同名定义共 2 条；本项为数据库第 4609 条记录，各定义分别保留。

**提示（Prompt）**：MURATA-1DX

**说明（Help）**

村田（Murata）Type 1DX 模块基于英飞凌（Infineon）CYW4343W 组合芯片组（Combo Chipset），支持 Wi-Fi® 802.11b/g/n 与 Bluetooth® 5.1 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 65 Mbps，蓝牙 PHY 数据速率最高 3 Mbps。更多信息见[村田 Type 1DX 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type1dx)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4343W_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:95`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L95)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 CYW4343W 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4343W_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4343W_MODULE)。

<a id="CONFIG_CYW4373"></a>

## 55.68 `CONFIG_CYW4373`

原库同名定义共 2 条；本项为数据库第 4611 条记录，各定义分别保留。

**提示（Prompt）**：CYW4373

**说明（Help）**

启用英飞凌（Infineon）CYW4373 低功耗蓝牙（BLE）连接功能。更多信息见[CYW4373 官方产品页面](https://www.infineon.com/cms/en/product/wireless-connectivity/airoc-wi-fi-plus-bluetooth-combos/cyw4373/)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_H4 && <choice CONFIG_AIROC_PART>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 AIROC 器件（AIROC Part）

**配置项引用（Symbol References）**：[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_AIROC_PART`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_AIROC_PART)。

<a id="CONFIG_CYW4373_MODULE"></a>

## 55.69 `CONFIG_CYW4373_MODULE`

原库同名定义共 2 条；本项为数据库第 4613 条记录，各定义分别保留。

**提示（Prompt）**：选择 CYW4373 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW4373 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW4373_STERLING_LWB5PLUS
CONFIG_CYW4373_MURATA_2AE
CONFIG_CYW4373_MURATA_2BC
CONFIG_CYW4373_STERLING_LWB5PLUS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW4373`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW4373_STERLING_LWB5PLUS`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_STERLING_LWB5PLUS)、[`CONFIG_CYW4373_MURATA_2AE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW4373_MURATA_2AE)、[`CONFIG_CYW4373_MURATA_2BC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW4373_MURATA_2BC)。

<a id="CONFIG_CYW4373_STERLING_LWB5PLUS"></a>

## 55.70 `CONFIG_CYW4373_STERLING_LWB5PLUS`

原库同名定义共 2 条；本项为数据库第 4617 条记录，各定义分别保留。

**提示（Prompt）**：STERLING-LWB5plus

**说明（Help）**

Ezurio Sterling LWB5+ 802.11ac / Bluetooth 5.0 M.2 载板（Carrier Board），采用 E 型键位（E-Type Key），提供 SDIO / UART。更多信息见[Sterling LWB5+ 官方模块页面](https://www.ezurio.com/wireless-modules/wifi-modules-bluetooth/sterling-lwb5-plus-wifi-5-bluetooth-5-module)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW4373_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 选择 CYW4373 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW4373_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW4373_MODULE)。

<a id="CONFIG_CYW55500_MODULE"></a>

## 55.71 `CONFIG_CYW55500_MODULE`

原库同名定义共 2 条；本项为数据库第 4620 条记录，各定义分别保留。

**提示（Prompt）**：CYW55500 模块（Module）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CYW55500 && CONFIG_BT_H4 && CONFIG_BT_AIROC && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_CYW55513IUBG_SM
CONFIG_CYW55513_MURATA_2FY
CONFIG_CYW955513SDM2WLIPA_SM
CONFIG_CYW55513IUBG_SM
CONFIG_CYW55513_MURATA_2FY_SM
CONFIG_CYW55513_MOD_PSE84_SOM
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CYW55500`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55500)、[`CONFIG_BT_H4`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4)、[`CONFIG_BT_AIROC`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_AIROC)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_CYW55513IUBG_SM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55513IUBG_SM)、[`CONFIG_CYW55513_MURATA_2FY`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55513_MURATA_2FY)、[`CONFIG_CYW955513SDM2WLIPA_SM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW955513SDM2WLIPA_SM)、[`CONFIG_CYW55513_MURATA_2FY_SM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55513_MURATA_2FY_SM)、[`CONFIG_CYW55513_MOD_PSE84_SOM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CYW55513_MOD_PSE84_SOM)。

<a id="CONFIG_CYW55513IUBG_SM"></a>

## 55.72 `CONFIG_CYW55513IUBG_SM`

原库同名定义共 2 条；本项为数据库第 4622 条记录，各定义分别保留。

**提示（Prompt）**：CYW55513 模块（Module）

**说明（Help）**

AIROC™ CYW55513 Wi-Fi 与 Bluetooth® 是低功耗单芯片器件，支持单流（Single-Stream）、三频段（Tri-Band）Wi-Fi 6/6E，具有符合 IEEE 802.11ax 的 Wi-Fi 媒体访问控制层／基带／无线电（MAC / Baseband / Radio），并支持 Bluetooth® 与 Bluetooth® Low Energy 5.4。

译注：上游原文在 Wi-Fi 6/6E 前多写了一个 `m`，此处按其余上下文中的 Wi-Fi 名称翻译。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → CYW55500 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_CYW55513_MURATA_2FY"></a>

## 55.73 `CONFIG_CYW55513_MURATA_2FY`

**提示（Prompt）**：CYW55513 村田 2FY 模块（Murata Module）

**说明（Help）**

Type 2FY 是基于英飞凌（Infineon）CYW55513 组合芯片组（Combo Chipset）的小型高性能模块，支持 Wi-Fi® 802.11a/b/g/n/ac/ax 与 Bluetooth® 5.4 基本速率／增强数据速率／低功耗（BR/EDR/LE）。Wi-Fi 物理层（PHY）数据速率最高 143 Mbps，蓝牙 PHY 最高 3 Mbps，低功耗蓝牙（Bluetooth LE）PHY 最高 2 Mbps。更多信息见[村田 Type 2FY 官方模块页面](https://www.murata.com/en-us/products/connectivitymodule/wi-fi-bluetooth/overview/lineup/type2fy)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_CYW55500_MODULE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.infineon:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.infineon#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → CYW55500 模块（Module）

**配置项引用（Symbol References）**：[`CONFIG_CYW55500_MODULE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_CYW55500_MODULE)。

<a id="CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK"></a>

## 55.74 `CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK`

**提示（Prompt）**：蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**说明（Help）**

蓝牙调制解调器休眠（Modem Sleep）使用的低功耗时钟源（Low-Power Clock Source）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP_MODE_ORIG && CONFIG_SOC_SERIES_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL
```

**可选项（Choices）**

```text
CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL
CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:848`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L848)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙原始调制解调器休眠模式（Modem Sleep Mode ORIG）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP_MODE_ORIG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP_MODE_ORIG)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL)、[`CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL)。

<a id="CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL"></a>

## 55.75 `CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL`

**提示（Prompt）**：外部 32kHz 晶体／振荡器（External Crystal / Oscillator）

**说明（Help）**

使用外部 32.768 kHz 参考源作为蓝牙低功耗时钟（BT LP Clock）。选择此项且运行时检测到晶体（Crystal）后，允许系统在蓝牙活动期间进入轻度休眠（Light Sleep），与 IDF 的 `BTDM_CTRL_LPCLK_SEL_EXT_32K_XTAL` 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:861`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L861)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙原始调制解调器休眠模式（Modem Sleep Mode ORIG） → 蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK)。

<a id="CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL"></a>

## 55.76 `CONFIG_ESP32_BTDM_CTRL_LPCLK_SEL_MAIN_XTAL`

**提示（Prompt）**：主晶体（Main Crystal）

**说明（Help）**

使用主晶体（Main Crystal）作为蓝牙低功耗时钟（BT LP Clock）。蓝牙活动期间禁止轻度休眠（Light Sleep），因为主晶体必须保持开启；与 IDF 的 `BTDM_CTRL_LPCLK_SEL_MAIN_XTAL` 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:855`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L855)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep） → 蓝牙原始调制解调器休眠模式（Modem Sleep Mode ORIG） → 蓝牙低功耗时钟（Bluetooth Low-Power Clock）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_LOW_POWER_CLOCK)。

<a id="CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP"></a>

## 55.77 `CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP`

**提示（Prompt）**：蓝牙调制解调器休眠（Bluetooth Modem Sleep）

**说明（Help）**

启用蓝牙控制器低功耗模式，即调制解调器休眠（Modem Sleep）。控制器在 BLE／BT 事件之间关闭物理层（PHY），使系统能够降低高级外设总线（APB）频率或进入轻度休眠（Light Sleep）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SOC_SERIES_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:832`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L832)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32（Modem Sleep）

**配置项引用（Symbol References）**：[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP_MODE_ORIG"></a>

## 55.78 `CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP_MODE_ORIG`

**提示（Prompt）**：蓝牙原始调制解调器休眠模式（Modem Sleep Mode ORIG）

**说明（Help）**

原始调制解调器休眠模式（Original Modem Sleep Mode）：控制器使用专用低功耗时钟，在 BLE／BR-EDR 事件之间休眠，与 IDF 的 `BTDM_CTRL_MODEM_SLEEP_MODE_ORIG` 相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP && CONFIG_SOC_SERIES_ESP32 && CONFIG_PM && CONFIG_TICKLESS_KERNEL && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:840`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L840)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → 调制解调器休眠，ESP32（Modem Sleep） → 蓝牙调制解调器休眠（Bluetooth Modem Sleep）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BTDM_CTRL_MODEM_SLEEP)、[`CONFIG_SOC_SERIES_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32)、[`CONFIG_PM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PM)、[`CONFIG_TICKLESS_KERNEL`](P002_kernel_配置项参考_2.md#CONFIG_TICKLESS_KERNEL)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_BLE_FEAT_CONN_SUBRATING"></a>

## 55.79 `CONFIG_ESP32_BT_BLE_FEAT_CONN_SUBRATING`

**提示（Prompt）**：连接子速率功能支持（Connection Subrating Support）

**说明（Help）**

在控制器功能集合（Feature Set）中声明原文所标注的 BLE 5.2 连接子速率（Connection Subrating）支持，使主机协议栈（Host Stack）能够与对端协商子速率。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_BT_LE_SUBRATE_ENABLED && (CONFIG_SOC_SERIES_ESP32C2 || CONFIG_SOC_SERIES_ESP32C5 || CONFIG_SOC_SERIES_ESP32C61 || CONFIG_SOC_SERIES_ESP32C6 || CONFIG_SOC_SERIES_ESP32H2) && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:395`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L395)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → BLE 5 功能支持（Feature Support） → 连接子速率，原文标为 BLE 5.2（Connection Subrating）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_LE_SUBRATE_ENABLED`](P056_drivers_bluetooth_配置项参考_3.md#CONFIG_ESP32_BT_LE_SUBRATE_ENABLED)、[`CONFIG_SOC_SERIES_ESP32C2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C2)、[`CONFIG_SOC_SERIES_ESP32C5`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C5)、[`CONFIG_SOC_SERIES_ESP32C61`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C61)、[`CONFIG_SOC_SERIES_ESP32C6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32C6)、[`CONFIG_SOC_SERIES_ESP32H2`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_SERIES_ESP32H2)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_SERIES_ESP32C2`、`CONFIG_SOC_SERIES_ESP32C5`、`CONFIG_SOC_SERIES_ESP32C61`、`CONFIG_SOC_SERIES_ESP32C6`、`CONFIG_SOC_SERIES_ESP32H2`。

<a id="CONFIG_ESP32_BT_CONTROLLER_STACK_SIZE"></a>

## 55.80 `CONFIG_ESP32_BT_CONTROLLER_STACK_SIZE`

**提示（Prompt）**：蓝牙控制器栈大小（Bluetooth Controller Stack Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CONTROLLER_TASK_PRIO"></a>

## 55.81 `CONFIG_ESP32_BT_CONTROLLER_TASK_PRIO`

**提示（Prompt）**：蓝牙控制器任务优先级（Bluetooth Controller Task Priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_ADV_DUP_FILT_MAX"></a>

## 55.82 `CONFIG_ESP32_BT_CTLR_ADV_DUP_FILT_MAX`

**提示（Prompt）**：BLE 重复过滤条目上限（Duplicate Filter Entry Limit）

**说明（Help）**

扩展广播重复扫描过滤器（Extended Advertising Duplicate Scan Filter）的最大条目数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 500]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_BR_EDR_MAX_ACL_CONN"></a>

## 55.83 `CONFIG_ESP32_BT_CTLR_BR_EDR_MAX_ACL_CONN`

**提示（Prompt）**：BR/EDR ACL 连接上限（Connection Limit）

**说明（Help）**

基本速率／增强数据速率（BR/EDR）异步连接逻辑传输（ACL）的最大连接数量。每个连接约使用 1.2 KB 动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_BR_EDR_MAX_SYNC_CONN"></a>

## 55.84 `CONFIG_ESP32_BT_CTLR_BR_EDR_MAX_SYNC_CONN`

**提示（Prompt）**：BR/EDR 同步连接上限，SCO／eSCO（Synchronous Connection Limit）

**说明（Help）**

同步连接（SCO / eSCO）的最大数量。每个连接约使用 2 KB 动态 RAM（DRAM）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 3]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_BR_EDR_MIN_ENC_KEY_SZ_DFT"></a>

## 55.85 `CONFIG_ESP32_BT_CTLR_BR_EDR_MIN_ENC_KEY_SZ_DFT`

**提示（Prompt）**：BR/EDR 最小加密密钥长度（Minimum Encryption Key Size）

**说明（Help）**

发起基本速率／增强数据速率（BR/EDR）加密时默认的最小加密密钥长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_CLASSIC && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
7
```

**取值范围（Ranges）**

```text
[7, 16]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_CLASSIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_CLASSIC)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE"></a>

## 55.86 `CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE`

**提示（Prompt）**：连接事件长度类型（Connection Event Length Type）

**说明（Help）**

决定控制器如何设置连接事件长度（Connection Event Length）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_ORIG
CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_CE
CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_SD
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:135`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L135)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_ORIG`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_ORIG)、[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_CE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_CE)、[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_SD`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_SD)。

<a id="CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_CE"></a>

## 55.87 `CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_CE`

**提示（Prompt）**：使用 HCI 连接事件参数（CE Parameter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 连接事件长度类型（Connection Event Length Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE)。

<a id="CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_ORIG"></a>

## 55.88 `CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_ORIG`

**提示（Prompt）**：原始方法（Original Method）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 连接事件长度类型（Connection Event Length Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE)。

<a id="CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_SD"></a>

## 55.89 `CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE_SD`

**提示（Prompt）**：乐鑫自定义方法（Espressif Custom Method）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 连接事件长度类型（Connection Event Length Type）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_CE_LENGTH_TYPE)。

<a id="CONFIG_ESP32_BT_CTLR_CHAN_ASS_EN"></a>

## 55.90 `CONFIG_ESP32_BT_CTLR_CHAN_ASS_EN`

**提示（Prompt）**：信道评估定时器（Channel Assessment Timer）

**说明（Help）**

定期评估信道质量（Channel Quality），每 4 秒更新一次信道映射（Channel Map）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_CHECK_CONNECT_IND_ACCESS_ADDRESS"></a>

## 55.91 `CONFIG_ESP32_BT_CTLR_CHECK_CONNECT_IND_ACCESS_ADDRESS`

**提示（Prompt）**：CONNECT_IND 接入地址验证（Access Address Verification）

**说明（Help）**

严格验证 `CONNECT_IND` 协议数据单元（PDU）中的接入地址（Access Address），以提高安全性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:245`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L245)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM"></a>

## 55.92 `CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM`

**提示（Prompt）**：共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**说明（Help）**

限制编码物理层（Coded PHY）的发送／接收（TX/RX）时间，以减少 Wi-Fi 干扰。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ESP32_SW_COEXIST_ENABLE && CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS
```

**可选项（Choices）**

```text
CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_EN
CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_SW_COEXIST_ENABLE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ESP32_SW_COEXIST_ENABLE)、[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)、[`CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS)、[`CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_EN`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_EN)。

<a id="CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS"></a>

## 55.93 `CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_DIS`

**提示（Prompt）**：无时间限制（No Time Limit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:260`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L260)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM)。

<a id="CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_EN"></a>

## 55.94 `CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM_EN`

**提示（Prompt）**：应用时间限制（Apply Time Limit）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM>
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 共存场景下编码 PHY 收发时间限制（Coded PHY TX/RX Time Limit）

**配置项引用（Symbol References）**：[`CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM`](P055_drivers_bluetooth_配置项参考_2.md#CONFIG_ESP32_BT_CTLR_COEX_PHY_CODED_TX_RX_TLIM)。

<a id="CONFIG_ESP32_BT_CTLR_DTM_ENABLE"></a>

## 55.95 `CONFIG_ESP32_BT_CTLR_DTM_ENABLE`

**提示（Prompt）**：直接测试模式支持（Direct Test Mode Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:223`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L223)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_HW_CCA"></a>

## 55.96 `CONFIG_ESP32_BT_CTLR_HW_CCA`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

硬件空闲信道评估（CCA）的内部有效值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_HW_CCA_VAL"></a>

## 55.97 `CONFIG_ESP32_BT_CTLR_HW_CCA_VAL`

**提示（Prompt）**：硬件 CCA 阈值，单位为 dBm（Hardware CCA Threshold）

**说明（Help）**

硬件空闲信道评估（CCA）的接收信号强度指示（RSSI）阈值。数值 30 对应 −30 dBm。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
20
```

**取值范围（Ranges）**

```text
[20, 100]
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:122`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L122)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_ADV"></a>

## 55.98 `CONFIG_ESP32_BT_CTLR_LE_ADV`

**提示（Prompt）**：低功耗蓝牙广播支持（BLE Advertising Support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_LLCP_CHAN_MAP_UPDATE"></a>

## 55.99 `CONFIG_ESP32_BT_CTLR_LE_LLCP_CHAN_MAP_UPDATE`

**提示（Prompt）**：信道映射更新超时时终止（Channel Map Update Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙链路层控制过程（BLE Link-Layer Control Procedures）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<a id="CONFIG_ESP32_BT_CTLR_LE_LLCP_CONN_UPDATE"></a>

## 55.100 `CONFIG_ESP32_BT_CTLR_LE_LLCP_CONN_UPDATE`

**提示（Prompt）**：连接更新超时时终止（Connection Update Timeout）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BT_ESP32 && CONFIG_BT_HCI && CONFIG_BT_DRIVERS
```

**定义位置（Location）**：[`drivers/bluetooth/hci/Kconfig.esp32:212`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/bluetooth/hci/Kconfig.esp32#L212)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 蓝牙驱动（Bluetooth Drivers） → ESP32 蓝牙控制器配置（Bluetooth Controller Configuration） → 低功耗蓝牙链路层控制过程（BLE Link-Layer Control Procedures）

**配置项引用（Symbol References）**：[`CONFIG_BT_ESP32`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_ESP32)、[`CONFIG_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI)、[`CONFIG_BT_DRIVERS`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_DRIVERS)。

<!-- kconfig-navigation -->

[上一章](P054_drivers_bluetooth_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P056_drivers_bluetooth_配置项参考_3.md)
