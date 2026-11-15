---
id: learning.zephyr-docs.kconfig-reference.page-336
title: "`subsys/crc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第336章\_`subsys/crc`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/crc` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_CRC"></a>

## 336.1 `CONFIG_CRC`

**提示（Prompt）**：循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**说明（Help）**

允许使用循环冗余校验（CRC）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_ADC_AD7124
CONFIG_ADC_LMP90XXX
CONFIG_BT_NXP
CONFIG_BT_H4_NXP_CTLR
CONFIG_CAN_MCP251XFD
CONFIG_ENTROPY_MAXQ10XX_RNG
CONFIG_ETH_WCH_MULTICAST_FILTER
CONFIG_ETH_NXP_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_QOS
CONFIG_ETH_STM32_DWC_ETHER_1000
CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH
CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS
CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS
CONFIG_FLASH_MCUX_FLEXSPI_NAND
CONFIG_SPI_NAND
CONFIG_LC709203F
CONFIG_GPIO_MAX14917
CONFIG_IEEE802154_CC13XX_CC26XX
CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ
CONFIG_INPUT_CRSF
CONFIG_MFD_MAX22017
CONFIG_NET_PPP
CONFIG_SPI_SDHC
CONFIG_DHT20_CRC
CONFIG_HTU31D
CONFIG_HS400X_CRC
CONFIG_SCD4X
CONFIG_SGP40
CONFIG_SHT3XD
CONFIG_SHT4X
CONFIG_SHTCX
CONFIG_STCC4
CONFIG_STS4X
CONFIG_SI7055
CONFIG_TAD2144
CONFIG_TI_HDC302X
CONFIG_TMAG5170_CRC
CONFIG_SMBUS_SOFT_PEC
CONFIG_SMBUS_ITE_IT51XXX
CONFIG_W1
CONFIG_WIFI_BFLB_WIFI4
CONFIG_BT_CLASSIC
CONFIG_FCB
CONFIG_GNSS_RTK_PROTOCOL_RTCM3
CONFIG_NVS
CONFIG_ZMS
CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32
CONFIG_OSDP
CONFIG_MODBUS
CONFIG_MODEM_CMUX
CONFIG_MODEM_PPP
CONFIG_DNS_RESOLVER
CONFIG_LWM2M_SHELL
CONFIG_MCTP_I3C_CONTROLLER
CONFIG_MCTP_I3C_TARGET
```

**被弱选择（Implied by）**

```text
CONFIG_ETH_ADIN2111
CONFIG_ETH_STM32_HAL
CONFIG_ICE40_FPGA
CONFIG_TMAG5273
CONFIG_BT_OTS_OACP_CHECKSUM_SUPPORT
CONFIG_RETENTION
```

**定义位置（Location）**：[`subsys/crc/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ADC_AD7124`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_AD7124)、[`CONFIG_ADC_LMP90XXX`](P047_drivers_adc_配置项参考_1.md#CONFIG_ADC_LMP90XXX)、[`CONFIG_BT_NXP`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_NXP)、[`CONFIG_BT_H4_NXP_CTLR`](P054_drivers_bluetooth_配置项参考_1.md#CONFIG_BT_H4_NXP_CTLR)、[`CONFIG_CAN_MCP251XFD`](P060_drivers_can_配置项参考.md#CONFIG_CAN_MCP251XFD)、[`CONFIG_ENTROPY_MAXQ10XX_RNG`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_MAXQ10XX_RNG)、[`CONFIG_ETH_WCH_MULTICAST_FILTER`](P089_drivers_ethernet_配置项参考_3.md#CONFIG_ETH_WCH_MULTICAST_FILTER)、[`CONFIG_ETH_NXP_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_QOS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_QOS)、[`CONFIG_ETH_STM32_DWC_ETHER_1000`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_DWC_ETHER_1000)、[`CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DWC_ETHER_MULTICAST_FILTER_HASH)、[`CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_NXP_ENET_QOS_UNIQUE_MAC_ADDRESS)、[`CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS`](P091_drivers_firmware_配置项参考.md#CONFIG_ARM_SCMI_NXP_VENDOR_EXTENSIONS)、[`CONFIG_FLASH_MCUX_FLEXSPI_NAND`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH_MCUX_FLEXSPI_NAND)、[`CONFIG_SPI_NAND`](P094_drivers_flash_配置项参考_3.md#CONFIG_SPI_NAND)、[`CONFIG_LC709203F`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_LC709203F)、[`CONFIG_GPIO_MAX14917`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_MAX14917)、[`CONFIG_IEEE802154_CC13XX_CC26XX`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX)、[`CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CC13XX_CC26XX_SUB_GHZ)、[`CONFIG_INPUT_CRSF`](P111_drivers_input_配置项参考_1.md#CONFIG_INPUT_CRSF)、[`CONFIG_MFD_MAX22017`](P120_drivers_mfd_配置项参考.md#CONFIG_MFD_MAX22017)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_SPI_SDHC`](P148_drivers_sdhc_配置项参考.md#CONFIG_SPI_SDHC)、[`CONFIG_DHT20_CRC`](P153_drivers_sensor_配置项参考_5.md#CONFIG_DHT20_CRC)、[`CONFIG_HTU31D`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HTU31D)、[`CONFIG_HS400X_CRC`](P154_drivers_sensor_配置项参考_6.md#CONFIG_HS400X_CRC)、[`CONFIG_SCD4X`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SCD4X)、[`CONFIG_SGP40`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SGP40)、[`CONFIG_SHT3XD`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT3XD)、[`CONFIG_SHT4X`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHT4X)、[`CONFIG_SHTCX`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SHTCX)、[`CONFIG_STCC4`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STCC4)、[`CONFIG_STS4X`](P161_drivers_sensor_配置项参考_13.md#CONFIG_STS4X)、[`CONFIG_SI7055`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SI7055)、[`CONFIG_TAD2144`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TAD2144)、[`CONFIG_TI_HDC302X`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TI_HDC302X)、[`CONFIG_TMAG5170_CRC`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5170_CRC)、[`CONFIG_SMBUS_SOFT_PEC`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_SOFT_PEC)、[`CONFIG_SMBUS_ITE_IT51XXX`](P171_drivers_smbus_配置项参考.md#CONFIG_SMBUS_ITE_IT51XXX)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_WIFI_BFLB_WIFI4`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB_WIFI4)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_FCB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FCB)、[`CONFIG_GNSS_RTK_PROTOCOL_RTCM3`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_GNSS_RTK_PROTOCOL_RTCM3)、[`CONFIG_NVS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NVS)、[`CONFIG_ZMS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ZMS)、[`CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_FS_CHECKSUM_IEEE_CRC32)、[`CONFIG_OSDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OSDP)、[`CONFIG_MODBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS)、[`CONFIG_MODEM_CMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_PPP)、[`CONFIG_DNS_RESOLVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DNS_RESOLVER)、[`CONFIG_LWM2M_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_SHELL)、[`CONFIG_MCTP_I3C_CONTROLLER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCTP_I3C_CONTROLLER)、[`CONFIG_MCTP_I3C_TARGET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCTP_I3C_TARGET)、[`CONFIG_ETH_ADIN2111`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_ADIN2111)、[`CONFIG_ETH_STM32_HAL`](P088_drivers_ethernet_配置项参考_2.md#CONFIG_ETH_STM32_HAL)、[`CONFIG_ICE40_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_ICE40_FPGA)、[`CONFIG_TMAG5273`](P161_drivers_sensor_配置项参考_13.md#CONFIG_TMAG5273)、[`CONFIG_BT_OTS_OACP_CHECKSUM_SUPPORT`](P330_subsys_bluetooth_配置项参考_11.md#CONFIG_BT_OTS_OACP_CHECKSUM_SUPPORT)、[`CONFIG_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION)。

<a id="CONFIG_CRC16"></a>

## 336.2 `CONFIG_CRC16`

**提示（Prompt）**：通用 CRC-16（CRC-16 Generic）

**说明（Help）**

实现通用 CRC-16 算法（generic CRC-16 algorithm），常用于存储、文件传输和基本串行通信协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16 && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:75`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L75)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC16_ANSI"></a>

## 336.3 `CONFIG_CRC16_ANSI`

**提示（Prompt）**：ANSI CRC-16（CRC-16 ANSI）

**说明（Help）**

实现 CRC-16 的 ANSI 变体，也称 CRC-16-IBM，常用于传统串行系统和文件系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16_ANSI && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16_ANSI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ANSI)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC16_CCITT"></a>

## 336.4 `CONFIG_CRC16_CCITT`

**提示（Prompt）**：CCITT CRC-16（CRC-16 CCITT）

**说明（Help）**

实现 CRC-16 的 CCITT 变体，广泛用于通信系统，例如 XMODEM 和 HDLC 协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16_CCITT && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_CCITT)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC16_ITU_T"></a>

## 336.5 `CONFIG_CRC16_ITU_T`

**提示（Prompt）**：ITU-T CRC-16（CRC-16 ITU-T）

**说明（Help）**

实现 ITU-T（原 CCITT）的 CRC-16 变体，常见于调制解调器协议和无线通信标准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_ITU_T)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC16_REFLECT"></a>

## 336.6 `CONFIG_CRC16_REFLECT`

**提示（Prompt）**：反射形式 CRC-16（CRC-16 Reflected）

**说明（Help）**

实现 CRC-16-CCITT 的反射形式（reflected），即位反转（bit-reversed）变体，适用于按最低有效位优先（LSB-first）顺序处理数据的系统。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC16_REFLECT)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC24_PGP"></a>

## 336.7 `CONFIG_CRC24_PGP`

**提示（Prompt）**：PGP CRC-24（CRC-24 PGP）

**说明（Help）**

实现 CRC24 算法，原文列举蓝牙和某些密码协议等应用。

译注：本选项提示指定 PGP，帮助文本则泛指 CRC24 的应用；不应仅因同为 24 位 CRC 就认为不同协议的算法参数相同。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC24_PGP && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC24_PGP`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC24_PGP)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC32_C"></a>

## 336.8 `CONFIG_CRC32_C`

**提示（Prompt）**：CRC-32C 循环冗余校验（CRC-32C）

**说明（Help）**

实现 CRC32-C（Castagnoli）算法，针对存储、网络以及现代处理器错误检测等高性能应用进行优化。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC32_C && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC32_C`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_C)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC32_IEEE"></a>

## 336.9 `CONFIG_CRC32_IEEE`

**提示（Prompt）**：IEEE CRC-32（CRC-32 IEEE）

**说明（Help）**

实现 CRC32-IEEE（CRC-32）算法，常用于以太网、ZIP 文件完整性检查及其他标准网络与存储应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC32_IEEE && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC32_IEEE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_IEEE)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC32_K_4_2"></a>

## 336.10 `CONFIG_CRC32_K_4_2`

**提示（Prompt）**：CRC-32K/4.2 循环冗余校验（CRC-32K/4.2）

**说明（Help）**

实现 CRC-32K/4.2 算法。原文将其描述为用于以太网、ZIP 文件及其他数据完整性应用的标准 CRC32-IEEE 的变体。

译注：这里保留原帮助文本的分类表述，不表示 CRC-32K/4.2 可直接替换协议所规定的 CRC32-IEEE；应核对具体 CRC 参数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2 && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:142`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L142)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_K_4_2)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC32_K_4_2_TABLE_256"></a>

## 336.11 `CONFIG_CRC32_K_4_2_TABLE_256`

**提示（Prompt）**：CRC-32K/4.2 的 256 项表（Table 256）

**说明（Help）**

启用使用 `256` 项查找表（lookup table）的 CRC-32K/4.2 软件实现，以加快计算。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/crc/Kconfig:161`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L161)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC32_MPEG2"></a>

## 336.12 `CONFIG_CRC32_MPEG2`

**提示（Prompt）**：MPEG-2 CRC-32（CRC-32 MPEG-2）

**说明（Help）**

实现 CRC-32/MPEG-2 算法：多项式（polynomial）为 `0x04C11DB7`，初始值为 `0xFFFFFFFF`，输入／输出均不反射（no reflection），最终不异或（no final XOR）。用于 MPEG-2 传输流（ISO/IEC 13818-1），且微控制器（MCU）CRC 外设通常支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2 && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC32_MPEG2)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC4"></a>

## 336.13 `CONFIG_CRC4`

**提示（Prompt）**：通用 CRC-4（CRC-4 Generic）

**说明（Help）**

实现通用 CRC-4 算法，适用于没有硬件 CRC 支持的平台。该实现灵活，但性能低于基于硬件的实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC4 && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC4`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC4)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC4_TI"></a>

## 336.14 `CONFIG_CRC4_TI`

**提示（Prompt）**：TI 多项式 CRC-4（CRC-4 TI Polynomial）

**说明（Help）**

实现 TI 专用 CRC-4 算法，常用于要求 CRC 开销最小的底层嵌入式通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC4_TI && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC4_TI`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC4_TI)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC7_BE"></a>

## 336.15 `CONFIG_CRC7_BE`

**提示（Prompt）**：大端位序 CRC-7（CRC-7 Big Endian）

**说明（Help）**

实现采用大端位序（Big Endian bit order）的 CRC-7 算法，常用于 SD 卡协议及其他串行通信标准。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC7_BE && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC7_BE`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC7_BE)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC8"></a>

## 336.16 `CONFIG_CRC8`

**提示（Prompt）**：通用 CRC-8（CRC-8 Generic）

**说明（Help）**

实现通用 CRC-8 算法，适用于小规模数据完整性检查，例如校验和及简单通信协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC8 && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC8`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC8_CCITT"></a>

## 336.17 `CONFIG_CRC8_CCITT`

**提示（Prompt）**：CCITT CRC-8（CRC-8 CCITT）

**说明（Help）**

实现 CRC-8 CCITT 多项式（polynomial），常用于通信和低功耗传感器协议。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC8_CCITT && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC8_CCITT`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_CCITT)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC8_ROHC"></a>

## 336.18 `CONFIG_CRC8_ROHC`

**提示（Prompt）**：ROHC CRC-8（CRC-8 ROHC）

**说明（Help）**

实现 CRC-8 鲁棒头压缩（Robust Header Compression，ROHC）算法，通常用于压缩 IP 头协议和网络通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CRC_DRIVER_HAS_CRC8_ROHC && CONFIG_CRC
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/crc/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER_HAS_CRC8_ROHC`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER_HAS_CRC8_ROHC)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_CRC_HW_HANDLER"></a>

## 336.19 `CONFIG_CRC_HW_HANDLER`

**提示（Prompt）**：CRC 硬件加速器（CRC Hardware Accelerator）

**说明（Help）**

允许使用 CRC 硬件（CRC hardware）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_CRC_DRIVER
```

**定义位置（Location）**：[`subsys/crc/Kconfig:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_CRC_DRIVER`](P070_drivers_crc_配置项参考.md#CONFIG_CRC_DRIVER)。

<a id="CONFIG_CRC_SHELL"></a>

## 336.20 `CONFIG_CRC_SHELL`

**提示（Prompt）**：CRC Shell（CRC 命令行）

**说明（Help）**

允许从 Shell 对内存区域（memory regions）执行 CRC 检查。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_CRC
```

**主动选择（Selects）**

```text
CONFIG_GETOPT
```

**定义位置（Location）**：[`subsys/crc/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/crc/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 循环冗余校验支持（Cyclic Redundancy Check，CRC Support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)、[`CONFIG_GETOPT`](P197_lib_配置项参考_1.md#CONFIG_GETOPT)。

<!-- kconfig-navigation -->

[上一章](P335_subsys_cpu_freq_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P337_subsys_dap_配置项参考.md)
