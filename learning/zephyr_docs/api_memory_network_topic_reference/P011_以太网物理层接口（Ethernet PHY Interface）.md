---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-11
title: 以太网物理层接口（Ethernet PHY Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_以太网物理层接口（Ethernet PHY Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet__phy.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

以太网物理层接口（Ethernet PHY Interface）

<a id="details"></a>

以太网物理层接口（Ethernet PHY Interface）。引入版本（Since）：2.7；API 版本（Version）：0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 11.1\_主题（Topics）

<a id="r_ethernet_5Fphy_5Fbackend"></a>

相关声明：[以太网 PHY 驱动后端 API](../api_platform_topic_reference/P051_以太网 PHY 驱动后端 API.md)。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.3\_宏定义（Macros）

<a id="r_ga7dcf0d74db291bf0922c8ceb34307558"></a>

```c
#define PHY_LINK_IS_FULL_DUPLEX(x)
```

相关声明：[PHY_LINK_IS_FULL_DUPLEX](#ga7dcf0d74db291bf0922c8ceb34307558)。

检查物理层（PHY）链路是否为全双工（Full Duplex）。

<a id="r_ga49f0673ace36bb3bac3e0c820a1f4de0"></a>

```c
#define PHY_LINK_IS_SPEED_1000M(x)
```

相关声明：[PHY_LINK_IS_SPEED_1000M](#ga49f0673ace36bb3bac3e0c820a1f4de0)。

检查物理层（PHY）链路速率是否为 1 Gbit/s。

<a id="r_ga35acfd5ebec25784cc1c5b6be7be6a05"></a>

```c
#define PHY_LINK_IS_SPEED_100M(x)
```

相关声明：[PHY_LINK_IS_SPEED_100M](#ga35acfd5ebec25784cc1c5b6be7be6a05)。

检查物理层（PHY）链路速率是否为 100 Mbit/s。

<a id="r_gabee5b68903eb89190289d88ecff74de7"></a>

```c
#define PHY_LINK_IS_SPEED_10M(x)
```

相关声明：[PHY_LINK_IS_SPEED_10M](#gabee5b68903eb89190289d88ecff74de7)。

检查物理层（PHY）链路速率是否为 10 Mbit/s。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.4\_类型定义（Typedefs）

<a id="r_ga3ee3db4ac48395f07d0de536b313dfa4"></a>

```c
typedef void(* phy_callback_t) (const struct device *dev, struct phy_link_state *state, void *user_data)
```

相关声明：[phy_callback_t](#ga3ee3db4ac48395f07d0de536b313dfa4)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

定义 `phy_link_callback_set()` 所用回调函数（Callback）的签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.5\_枚举（Enumerations）

<a id="r_ga9b97fff9fcd6823c9b564b3e86b8da68"></a>

```c
enum phy_link_speed { LINK_HALF_10BASE = BIT(0) , LINK_FULL_10BASE = BIT(1) , LINK_HALF_100BASE = BIT(2) , LINK_FULL_100BASE = BIT(3) , LINK_HALF_1000BASE = BIT(4) , LINK_FULL_1000BASE = BIT(5) , LINK_FULL_2500BASE = BIT(6) , LINK_FULL_5000BASE = BIT(7) }
```

相关声明：[phy_link_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68)、[LINK_HALF_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c)、[LINK_FULL_10BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c)、[LINK_HALF_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d)、[LINK_FULL_100BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956)、[LINK_HALF_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec)、[LINK_FULL_1000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04)、[LINK_FULL_2500BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e)、[LINK_FULL_5000BASE](#gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6)。

以太网链路速率（Ethernet Link Speeds）。

<a id="r_ga6221da76ffca235eafa291b90eab0d93"></a>

```c
enum phy_cfg_link_flag { PHY_FLAG_AUTO_NEGOTIATION_DISABLED = BIT(0) }
```

相关声明：[phy_cfg_link_flag](#ga6221da76ffca235eafa291b90eab0d93)、[PHY_FLAG_AUTO_NEGOTIATION_DISABLED](#gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009)。

以太网链路配置标志（Ethernet Configure Link Flags）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.6\_函数（Functions）

<a id="r_gafce454d5da52532e4588324752c5cec3"></a>

```c
static int phy_configure_link (const struct device *dev, enum phy_link_speed speeds, enum phy_cfg_link_flag flags)
```

相关声明：[phy_configure_link](#gafce454d5da52532e4588324752c5cec3)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_speed](#ga9b97fff9fcd6823c9b564b3e86b8da68)、[phy_cfg_link_flag](#ga6221da76ffca235eafa291b90eab0d93)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

配置物理层（PHY）链路。

<a id="r_ga4d073c152ad4b6f5745db4f6d8477345"></a>

```c
static int phy_get_link_state (const struct device *dev, struct phy_link_state *state)
```

相关声明：[phy_get_link_state](#ga4d073c152ad4b6f5745db4f6d8477345)、[device](../device_reference/P002_设备对象结构.md)、[phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

获取物理层（PHY）链路状态。

<a id="r_ga0ede85fdd6efd8c3520d7baf18d04a68"></a>

```c
static int phy_link_callback_set (const struct device *dev, phy_callback_t callback, void *user_data)
```

相关声明：[phy_link_callback_set](#ga0ede85fdd6efd8c3520d7baf18d04a68)、[device](../device_reference/P002_设备对象结构.md)、[phy_callback_t](#ga3ee3db4ac48395f07d0de536b313dfa4)。

设置链路状态变化回调（Link State Change Callback）。

<a id="r_ga3fcca53d29981e23426b43d5340d8651"></a>

```c
static int phy_read (const struct device *dev, uint16_t reg_addr, uint32_t *value)
```

相关声明：[phy_read](#ga3fcca53d29981e23426b43d5340d8651)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取物理层（PHY）寄存器。

<a id="r_ga520c049d830051ffa48708bb0dea429f"></a>

```c
static int phy_write (const struct device *dev, uint16_t reg_addr, uint32_t value)
```

相关声明：[phy_write](#ga520c049d830051ffa48708bb0dea429f)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

写入物理层（PHY）寄存器。

<a id="r_ga4fa30627b96c9a1d02b43c8e799f2796"></a>

```c
static int phy_read_c45 (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t *data)
```

相关声明：[phy_read_c45](#ga4fa30627b96c9a1d02b43c8e799f2796)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

读取物理层（PHY）的 Clause 45（C45）寄存器。

<a id="r_ga492c16dd8b5f2708d9e702ce8906ffd3"></a>

```c
static int phy_write_c45 (const struct device *dev, uint8_t devad, uint16_t regad, uint16_t data)
```

相关声明：[phy_write_c45](#ga492c16dd8b5f2708d9e702ce8906ffd3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

写入物理层（PHY）的 Clause 45（C45）寄存器。

<a id="r_ga260e528dee1c967ccc9f4d9cb2aadad5"></a>

```c
static int phy_set_plca_cfg (__maybe_unused const struct device *dev, __maybe_unused struct phy_plca_cfg *plca_cfg)
```

相关声明：[phy_set_plca_cfg](#ga260e528dee1c967ccc9f4d9cb2aadad5)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)。

写入物理层冲突避免（PLCA）配置。

<a id="r_gaba1b0bda2a76a6d5db404d24ffec1aa5"></a>

```c
static int phy_get_plca_cfg (__maybe_unused const struct device *dev, __maybe_unused struct phy_plca_cfg *plca_cfg)
```

相关声明：[phy_get_plca_cfg](#gaba1b0bda2a76a6d5db404d24ffec1aa5)、[device](../device_reference/P002_设备对象结构.md)、[phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)。

读取物理层冲突避免（PLCA）配置。

<a id="r_gaaf47828adbc414304d871441217e772c"></a>

```c
static int phy_get_plca_sts (__maybe_unused const struct device *dev, __maybe_unused bool *plca_status)
```

相关声明：[phy_get_plca_sts](#gaaf47828adbc414304d871441217e772c)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

读取物理层冲突避免（PLCA）状态。

## 11.7\_详细说明（Detailed Documentation）

<a id="ga7dcf0d74db291bf0922c8ceb34307558"></a>

### `PHY_LINK_IS_FULL_DUPLEX`

```c
#define PHY_LINK_IS_FULL_DUPLEX ( x)
```

```c
#include <zephyr/net/phy.h>
```

展开值（Value）：

```c
(x & (LINK_FULL_10BASE | LINK_FULL_100BASE | LINK_FULL_1000BASE | LINK_FULL_2500BASE |     \
      LINK_FULL_5000BASE))
```

检查物理层（PHY）链路是否为全双工（Full Duplex）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 链路能力（Link Capabilities） |

**返回（Returns）**：返回值（Returns）：链路为全双工（Full Duplex）时返回 True，否则返回 false。

<a id="ga49f0673ace36bb3bac3e0c820a1f4de0"></a>

### `PHY_LINK_IS_SPEED_1000M`

```c
#define PHY_LINK_IS_SPEED_1000M ( x)
```

```c
#include <zephyr/net/phy.h>
```

展开值（Value）：

```c
(x & (LINK_HALF_1000BASE | LINK_FULL_1000BASE))
```

检查物理层（PHY）链路速率是否为 1 Gbit/s。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 链路能力（Link Capabilities） |

**返回（Returns）**：返回值（Returns）：链路为 1 Gbit/s 时返回 True，否则返回 false。

<a id="ga35acfd5ebec25784cc1c5b6be7be6a05"></a>

### `PHY_LINK_IS_SPEED_100M`

```c
#define PHY_LINK_IS_SPEED_100M ( x)
```

```c
#include <zephyr/net/phy.h>
```

展开值（Value）：

```c
(x & (LINK_HALF_100BASE | LINK_FULL_100BASE))
```

检查物理层（PHY）链路速率是否为 100 Mbit/s。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 链路能力（Link Capabilities） |

**返回（Returns）**：返回值（Returns）：链路为 100 Mbit/s 时返回 True，否则返回 false。

<a id="gabee5b68903eb89190289d88ecff74de7"></a>

### `PHY_LINK_IS_SPEED_10M`

```c
#define PHY_LINK_IS_SPEED_10M ( x)
```

```c
#include <zephyr/net/phy.h>
```

展开值（Value）：

```c
(x & (LINK_HALF_10BASE | LINK_FULL_10BASE))
```

检查物理层（PHY）链路速率是否为 10 Mbit/s。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 链路能力（Link Capabilities） |

**返回（Returns）**：返回值（Returns）：链路为 10 Mbit/s 时返回 True，否则返回 false。

<a id="ga3ee3db4ac48395f07d0de536b313dfa4"></a>

### `phy_callback_t`

```c
typedef void(* phy_callback_t) (const struct device *dev, struct phy_link_state *state, void *user_data)
```

```c
#include <zephyr/net/phy.h>
```

定义 `phy_link_callback_set()` 所用回调函数（Callback）的签名。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | PHY 设备结构体（Device Structure） |
| `state` | 指向 link_state 结构体的指针。 |
| `user_data` | 指向用户指定数据的指针 |

<a id="ga6221da76ffca235eafa291b90eab0d93"></a>

### `phy_cfg_link_flag`

```c
enum phy_cfg_link_flag
```

```c
#include <zephyr/net/phy.h>
```

以太网链路配置标志（Ethernet Configure Link Flags）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PHY_FLAG_AUTO_NEGOTIATION_DISABLED` | 禁用自动协商（Auto-negotiation）。 |

<a id="ga9b97fff9fcd6823c9b564b3e86b8da68"></a>

### `phy_link_speed`

```c
enum phy_link_speed
```

```c
#include <zephyr/net/phy.h>
```

以太网链路速率（Ethernet Link Speeds）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `LINK_HALF_10BASE` | 10Base 半双工（Half-Duplex）。 |
| `LINK_FULL_10BASE` | 10Base 全双工（Full-Duplex）。 |
| `LINK_HALF_100BASE` | 100Base 半双工（Half-Duplex）。 |
| `LINK_FULL_100BASE` | 100Base 全双工（Full-Duplex）。 |
| `LINK_HALF_1000BASE` | 1000Base 半双工（Half-Duplex）。 |
| `LINK_FULL_1000BASE` | 1000Base 全双工（Full-Duplex）。 |
| `LINK_FULL_2500BASE` | 2.5GBase 全双工（Full-Duplex）。 |
| `LINK_FULL_5000BASE` | 5GBase 全双工（Full-Duplex）。 |

<a id="gafce454d5da52532e4588324752c5cec3"></a>

### `phy_configure_link()`

```c
int phy_configure_link ( const struct device * dev, enum phy_link_speed speeds, enum phy_cfg_link_flag flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

配置物理层（PHY）链路。

此例程配置通告的链路速率（Advertised Link Speeds）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| ` speeds` | PHY 要通告的链路速率，以按位或（OR）组合。 |
| ` flags` | 控制链路配置的标志，以按位或（OR）组合；或传 0。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |
| `-ENOTSUP` | 不支持此操作。 |
| `-EALREADY` | 已配置相同速率和标志时。 |

<a id="ga4d073c152ad4b6f5745db4f6d8477345"></a>

### `phy_get_link_state()`

```c
int phy_get_link_state ( const struct device * dev, struct phy_link_state * state )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

获取物理层（PHY）链路状态。

返回 PHY 链路当前状态，可用于确定链路何时建立，以及协商出的链路速率（Negotiated Link Speed）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| ` state` | 用于接收 PHY 状态的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

<a id="gaba1b0bda2a76a6d5db404d24ffec1aa5"></a>

### `phy_get_plca_cfg()`

```c
int phy_get_plca_cfg ( __maybe_unused const struct device * dev, __maybe_unused struct phy_plca_cfg * plca_cfg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

读取物理层冲突避免（PLCA）配置。

此例程提供获取 PHY 物理层冲突避免（PLCA）设置的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| ` plca_cfg` | 指向 PLCA 配置结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="gaaf47828adbc414304d871441217e772c"></a>

### `phy_get_plca_sts()`

```c
int phy_get_plca_sts ( __maybe_unused const struct device * dev, __maybe_unused bool * plca_status )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

读取物理层冲突避免（PLCA）状态。

此例程提供获取 PHY 物理层冲突避免（PLCA）状态的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| ` plca_status` | 指向 PLCA 状态的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="ga0ede85fdd6efd8c3520d7baf18d04a68"></a>

### `phy_link_callback_set()`

```c
int phy_link_callback_set ( const struct device * dev, phy_callback_t callback, void * user_data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

设置链路状态变化回调（Link State Change Callback）。

设置链路状态变化时调用的回调，这是以太网驱动接收 PHY 链路状态变化通知的首选方式。设置后即使状态未变，也会调用一次回调。任何时刻只能设置并激活一个回调函数。此函数主要用于以太网驱动注册链路状态变化回调，因此应用不应使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| ` callback` | 回调处理函数（Callback Handler） |
| ` user_data` | 指向用户指定数据的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` | 不支持此操作。 |

<a id="ga3fcca53d29981e23426b43d5340d8651"></a>

### `phy_read()`

```c
int phy_read ( const struct device * dev, uint16_t reg_addr, uint32_t * value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

读取物理层（PHY）寄存器。

此例程提供读取 PHY 寄存器（Register）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| `[in] reg_addr` | 寄存器地址（Register Address）。 |
| ` value` | 用于接收所读值的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

<a id="ga4fa30627b96c9a1d02b43c8e799f2796"></a>

### `phy_read_c45()`

```c
int phy_read_c45 ( const struct device * dev, uint8_t devad, uint16_t regad, uint16_t * data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

读取物理层（PHY）的 Clause 45（C45）寄存器。

此例程提供读取 PHY C45 寄存器（Register）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| `[in] devad` | 设备地址。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| ` data` | 用于接收读取数据的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

<a id="ga260e528dee1c967ccc9f4d9cb2aadad5"></a>

### `phy_set_plca_cfg()`

```c
int phy_set_plca_cfg ( __maybe_unused const struct device * dev, __maybe_unused struct phy_plca_cfg * plca_cfg )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

写入物理层冲突避免（PLCA）配置。

此例程提供配置 PHY 物理层冲突避免（PLCA）设置的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| `[in] plca_cfg` | 指向 PLCA 配置结构体的指针 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

**注意（Attention）**：注意：仅在启用以下 Kconfig 选项时可用：`CONFIG_ETH_PHY_API_PLCA`。

<a id="ga520c049d830051ffa48708bb0dea429f"></a>

### `phy_write()`

```c
int phy_write ( const struct device * dev, uint16_t reg_addr, uint32_t value )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

写入物理层（PHY）寄存器。

此例程提供写入 PHY 寄存器（Register）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| `[in] reg_addr` | 寄存器地址（Register Address）。 |
| `[in] value` | 要写入的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |

<a id="ga492c16dd8b5f2708d9e702ce8906ffd3"></a>

### `phy_write_c45()`

```c
int phy_write_c45 ( const struct device * dev, uint8_t devad, uint16_t regad, uint16_t data )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net/phy.h>
```

写入物理层（PHY）的 Clause 45（C45）寄存器。

此例程提供写入 PHY C45 寄存器（Register）的通用接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] dev` | PHY 设备结构体（Device Structure） |
| `[in] devad` | 设备地址。 |
| `[in] regad` | 寄存器地址（Register Address）。 |
| `[in] data` | 要写入的数据。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EIO` | 与 PHY 通信失败时。 |


## 11.8\_原页交叉引用（Cross References）

- [以太网 PHY 驱动后端 API](../api_platform_topic_reference/P051_以太网 PHY 驱动后端 API.md)
- [phy_link_state](../network_service_model_reference/P040_phy_link_state_结构体.md)
- [phy_plca_cfg](../network_service_model_reference/P041_phy_plca_cfg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/net/phy.h](../api_file_signal_device_reference/P016_zephyr__net__phy.h_文件参考.md)
- [CONFIG_ETH_PHY_API_PLCA](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ETH_PHY_API_PLCA)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d"></a>
<a id="agroup__ethernet__phy_html_gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6221da76ffca235eafa291b90eab0d93a29ae079e026a6171aee11aad0a26a009"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68a31f84ef851304d6f09029e413414212c"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68a73121ca47757e8a5dacd2f24c972624c"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68a882f179b6de90a7bd0233da7ecc1024d"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68af0adee55a0a82b9362e342579710a956"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68ae5b04b07c08a31c182416a95560160ec"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68aa3c6b736fb44fa247999b7327c901b04"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68a4371662a242b197c3520948bc8673e4e"></a>
<a id="gga9b97fff9fcd6823c9b564b3e86b8da68aef11379cb040a86aa1608cc7086aa5c6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_Realtek Bee DMA 宏（Macros）.md) · [返回大纲](大纲.md) · [下一章](P012_HTTP服务（Service）API。.md)
