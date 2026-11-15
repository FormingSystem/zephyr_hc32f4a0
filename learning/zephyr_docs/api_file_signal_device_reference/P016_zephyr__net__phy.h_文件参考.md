---
id: learning.zephyr-docs.api-file-signal-device-reference.page-16
title: zephyr__net__phy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_zephyr\_\_net\_\_phy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/phy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网物理层（Ethernet PHY）驱动的公共API。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/device.h>
#include <zephyr/sys/util_macro.h>
#include <errno.h>
```

查看此文件的源码。

以太网物理层（Ethernet PHY）驱动的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_phy_5Flink_5Fstate"></a>

```c
struct phy_link_state
```

相关声明：[phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)。

链路状态（Link State）。

<a id="r_phy_5Fplca_5Fcfg"></a>

```c
struct phy_plca_cfg
```

相关声明：[phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)。

物理层冲突避免（PLCA）协调子层（Reconciliation Sublayer）的配置。

<a id="r_ethphy_5Fdriver_5Fapi"></a>

```c
struct ethphy_driver_api
```

相关声明：[ethphy_driver_api](../network_service_model_reference/P014_ethphy_driver_api_结构体.md)。

驱动操作（Driver Operations）：以太网物理层（Ethernet PHY）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 16.2\_宏定义（Macros）

<a id="r_ga7dcf0d74db291bf0922c8ceb34307558"></a>

```c
#define PHY_LINK_IS_FULL_DUPLEX(x)
```

相关声明：[PHY_LINK_IS_FULL_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga7dcf0d74db291bf0922c8ceb34307558)。

检查物理层（PHY）链路是否为全双工（Full Duplex）。

<a id="r_ga49f0673ace36bb3bac3e0c820a1f4de0"></a>

```c
#define PHY_LINK_IS_SPEED_1000M(x)
```

相关声明：[PHY_LINK_IS_SPEED_1000M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga49f0673ace36bb3bac3e0c820a1f4de0)。

检查物理层（PHY）链路速率是否为 1 Gbit/s。

<a id="r_ga35acfd5ebec25784cc1c5b6be7be6a05"></a>

```c
#define PHY_LINK_IS_SPEED_100M(x)
```

相关声明：[PHY_LINK_IS_SPEED_100M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga35acfd5ebec25784cc1c5b6be7be6a05)。

检查物理层（PHY）链路速率是否为 100 Mbit/s。

<a id="r_gabee5b68903eb89190289d88ecff74de7"></a>

```c
#define PHY_LINK_IS_SPEED_10M(x)
```

相关声明：[PHY_LINK_IS_SPEED_10M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gabee5b68903eb89190289d88ecff74de7)。

检查物理层（PHY）链路速率是否为 10 Mbit/s。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 16.3\_类型定义（Typedefs）

<a id="r_ga3ee3db4ac48395f07d0de536b313dfa4"></a>

```c
typedef void(* phy_callback_t) (const struct device *dev, struct phy_link_state *state, void *user_data)
```

相关声明：[phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

定义 `phy_link_callback_set()` 所用回调函数（Callback）的签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 16.4\_枚举（Enumerations）

<a id="r_ga9b97fff9fcd6823c9b564b3e86b8da68"></a>

```c
enum phy_link_speed { LINK_HALF_10BASE = BIT(0) , LINK_FULL_10BASE = BIT(1) , LINK_HALF_100BASE = BIT(2) , LINK_FULL_100BASE = BIT(3) , LINK_HALF_1000BASE = BIT(4) , LINK_FULL_1000BASE = BIT(5) , LINK_FULL_2500BASE = BIT(6) , LINK_FULL_5000BASE = BIT(7) }
```

相关声明：[phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)、[LINK_HALF_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)、[LINK_FULL_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)、[LINK_HALF_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)、[LINK_FULL_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)、[LINK_HALF_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)、[LINK_FULL_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)、[LINK_FULL_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)、[LINK_FULL_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)。

以太网链路速率（Ethernet Link Speeds）。

<a id="r_ga6221da76ffca235eafa291b90eab0d93"></a>

```c
enum phy_cfg_link_flag { PHY_FLAG_AUTO_NEGOTIATION_DISABLED = BIT(0) }
```

相关声明：[phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)、[PHY_FLAG_AUTO_NEGOTIATION_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)。

以太网链路配置标志（Ethernet Configure Link Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.5\_函数（Functions）

<a id="r_gafce454d5da52532e4588324752c5cec3"></a>

```c
static int phy_configure_link (const struct device *dev, enum phy_link_speed speeds, enum phy_cfg_link_flag flags)
```

相关声明：[phy_configure_link](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)、[phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置物理层（PHY）链路。

<a id="r_ga4d073c152ad4b6f5745db4f6d8477345"></a>

```c
static int phy_get_link_state (const struct device *dev, struct phy_link_state *state)
```

相关声明：[phy_get_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4d073c152ad4b6f5745db4f6d8477345)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取物理层（PHY）链路状态。

<a id="r_ga0ede85fdd6efd8c3520d7baf18d04a68"></a>

```c
static int phy_link_callback_set (const struct device *dev, phy_callback_t callback, void *user_data)
```

相关声明：[phy_link_callback_set](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga0ede85fdd6efd8c3520d7baf18d04a68)、[device](../device_reference/P002_设备对象结构.md)、[phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)。

设置链路状态变化回调（Link State Change Callback）。

<a id="r_ga3fcca53d29981e23426b43d5340d8651"></a>

```c
static int phy_read (const struct device *dev, uint16_t reg_addr, uint32_t *value)
```

相关声明：[phy_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3fcca53d29981e23426b43d5340d8651)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取物理层（PHY）寄存器。

<a id="r_ga520c049d830051ffa48708bb0dea429f"></a>

```c
static int phy_write (const struct device *dev, uint16_t reg_addr, uint32_t value)
```

相关声明：[phy_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga520c049d830051ffa48708bb0dea429f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入物理层（PHY）寄存器。

<a id="r_ga4fa30627b96c9a1d02b43c8e799f2796"></a>

```c
static int phy_read_c45 (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[phy_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4fa30627b96c9a1d02b43c8e799f2796)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取物理层（PHY）的 Clause 45（C45）寄存器。

<a id="r_ga492c16dd8b5f2708d9e702ce8906ffd3"></a>

```c
static int phy_write_c45 (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[phy_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga492c16dd8b5f2708d9e702ce8906ffd3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

写入物理层（PHY）的 Clause 45（C45）寄存器。

<a id="r_ga260e528dee1c967ccc9f4d9cb2aadad5"></a>

```c
static int phy_set_plca_cfg (__maybe_unused const struct device *dev, __maybe_unused struct phy_plca_cfg *plca_cfg)
```

相关声明：[phy_set_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga260e528dee1c967ccc9f4d9cb2aadad5)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)。

写入物理层冲突避免（PLCA）配置。

<a id="r_gaba1b0bda2a76a6d5db404d24ffec1aa5"></a>

```c
static int phy_get_plca_cfg (__maybe_unused const struct device *dev, __maybe_unused struct phy_plca_cfg *plca_cfg)
```

相关声明：[phy_get_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaba1b0bda2a76a6d5db404d24ffec1aa5)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)。

读取物理层冲突避免（PLCA）配置。

<a id="r_gaaf47828adbc414304d871441217e772c"></a>

```c
static int phy_get_plca_sts (__maybe_unused const struct device *dev, __maybe_unused bool *plca_status)
```

相关声明：[phy_get_plca_sts](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaaf47828adbc414304d871441217e772c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

读取物理层冲突避免（PLCA）状态。


## 16.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P142_phy.h_源码浏览.md)
- [phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)
- [phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)
- [ethphy_driver_api](../network_service_model_reference/P014_ethphy_driver_api_结构体.md)
- [PHY_LINK_IS_FULL_DUPLEX](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga7dcf0d74db291bf0922c8ceb34307558)
- [PHY_LINK_IS_SPEED_1000M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga49f0673ace36bb3bac3e0c820a1f4de0)
- [PHY_LINK_IS_SPEED_100M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga35acfd5ebec25784cc1c5b6be7be6a05)
- [PHY_LINK_IS_SPEED_10M](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gabee5b68903eb89190289d88ecff74de7)
- [phy_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3ee3db4ac48395f07d0de536b313dfa4)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [phy_link_callback_set()](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga0ede85fdd6efd8c3520d7baf18d04a68)
- [phy_link_speed](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga9b97fff9fcd6823c9b564b3e86b8da68)
- [LINK_HALF_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)
- [LINK_FULL_10BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)
- [LINK_HALF_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)
- [LINK_FULL_100BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)
- [LINK_HALF_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)
- [LINK_FULL_1000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)
- [LINK_FULL_2500BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)
- [LINK_FULL_5000BASE](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)
- [phy_cfg_link_flag](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga6221da76ffca235eafa291b90eab0d93)
- [PHY_FLAG_AUTO_NEGOTIATION_DISABLED](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)
- [phy_configure_link](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gafce454d5da52532e4588324752c5cec3)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [phy_get_link_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4d073c152ad4b6f5745db4f6d8477345)
- [phy_read](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga3fcca53d29981e23426b43d5340d8651)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [phy_write](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga520c049d830051ffa48708bb0dea429f)
- [phy_read_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga4fa30627b96c9a1d02b43c8e799f2796)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [phy_write_c45](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga492c16dd8b5f2708d9e702ce8906ffd3)
- [phy_set_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#ga260e528dee1c967ccc9f4d9cb2aadad5)
- [phy_get_plca_cfg](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaba1b0bda2a76a6d5db404d24ffec1aa5)
- [phy_get_plca_sts](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html#gaaf47828adbc414304d871441217e772c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>

---

[上一章](P015_zephyr__drivers__interrupt_controller__nxp_pint.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P017_zephyr__drivers__pulse_io.h_文件参考.md)
