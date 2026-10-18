---
id: learning.zephyr-docs.api-network-time-topic-reference.page-13
title: 现场可编程门阵列（FPGA）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_现场可编程门阵列（FPGA）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__fpga__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

现场可编程门阵列（Field-Programmable Gate Arrays，FPGA）接口。

<a id="details"></a>

现场可编程门阵列（Field-Programmable Gate Arrays，FPGA）接口。自 Zephyr 2.7 起提供；API 版本为 0.8.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 13.1\_主题（Topics）

<a id="r_fpga_5Finterface_5Fbackend"></a>

相关声明：[FPGA 驱动后端 API（Driver Backend API）](../api_device_topic_reference/P009_FPGA 驱动后端 API（Driver Backend API）.md)。

<a id="header-files"></a>
<a id="files"></a>

## 13.2\_文件（Files）

<a id="r_fpga_2Eh"></a>

```c
file fpga.h
```

相关声明：[fpga.h](../peripheral_bus_storage_header_reference/P006_zephyr__drivers__fpga.h_头文件参考.md)。

现场可编程门阵列（FPGA）驱动API的主头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 13.3\_宏定义（Macros）

<a id="r_gab41c04907be508f62e8df813d633b34b"></a>

```c
#define FPGA_GET_INFO_DEFAULT "n/a"
```

相关声明：[FPGA_GET_INFO_DEFAULT](#gab41c04907be508f62e8df813d633b34b)。

无可用信息时，`fpga_get_info()` 返回的默认字符串。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 13.4\_枚举（Enumerations）

<a id="r_ga0bbacdfdac79bace1786bb2a1627bb1e"></a>

```c
enum FPGA_status { FPGA_STATUS_INACTIVE , FPGA_STATUS_ACTIVE }
```

相关声明：[FPGA_status](#ga0bbacdfdac79bace1786bb2a1627bb1e)、[FPGA_STATUS_INACTIVE](#gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441)、[FPGA_STATUS_ACTIVE](#gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131)。

FPGA 配置状态（Programming status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 13.5\_函数（Functions）

<a id="r_ga1a1e78a46df9f4bd374cf5ecc2449360"></a>

```c
static enum FPGA_status fpga_get_status (const struct device *dev)
```

相关声明：[FPGA_status](#ga0bbacdfdac79bace1786bb2a1627bb1e)、[fpga_get_status](#ga1a1e78a46df9f4bd374cf5ecc2449360)、[device](../device_reference/P002_设备对象结构.md)。

读取现场可编程门阵列（FPGA）的状态。

<a id="r_gadfc8d6c24cb1b1640393017a462011c9"></a>

```c
static int fpga_reset (const struct device *dev)
```

相关声明：[fpga_reset](#gadfc8d6c24cb1b1640393017a462011c9)、[device](../device_reference/P002_设备对象结构.md)。

复位 FPGA。

<a id="r_ga1cace6c7cc44705bf861d7aa5e863e16"></a>

```c
static int fpga_load (const struct device *dev, uint32_t *image_ptr, uint32_t img_size)
```

相关声明：[fpga_load](#ga1cace6c7cc44705bf861d7aa5e863e16)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

加载位流（Bitstream）并配置 FPGA。

<a id="r_gad9093bd96c6a62cd958718d1e01e3f37"></a>

```c
static int fpga_on (const struct device *dev)
```

相关声明：[fpga_on](#gad9093bd96c6a62cd958718d1e01e3f37)、[device](../device_reference/P002_设备对象结构.md)。

开启 FPGA。

<a id="r_gab887999e8728bcc335a784afbdbbee8f"></a>

```c
static const char * fpga_get_info (const struct device *dev)
```

相关声明：[fpga_get_info](#gab887999e8728bcc335a784afbdbbee8f)、[device](../device_reference/P002_设备对象结构.md)。

返回 FPGA 的相关信息。

<a id="r_gaa161c7a7006db24793c1a1ecdea25b5c"></a>

```c
static int fpga_off (const struct device *dev)
```

相关声明：[fpga_off](#gaa161c7a7006db24793c1a1ecdea25b5c)、[device](../device_reference/P002_设备对象结构.md)。

关闭 FPGA。

## 13.6\_详细说明（Detailed Documentation）

<a id="gab41c04907be508f62e8df813d633b34b"></a>

### `FPGA_GET_INFO_DEFAULT`

```c
#define FPGA_GET_INFO_DEFAULT "n/a"
```

```c
#include <zephyr/drivers/fpga.h>
```

无可用信息时，`fpga_get_info()` 返回的默认字符串。

<a id="ga0bbacdfdac79bace1786bb2a1627bb1e"></a>

### `FPGA_status`

```c
enum FPGA_status
```

```c
#include <zephyr/drivers/fpga.h>
```

FPGA 配置状态（Programming status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `FPGA_STATUS_INACTIVE` | FPGA 无法接收比特流（bitstream），不能正确编程。 |
| `FPGA_STATUS_ACTIVE` | FPGA 能够接收比特流，可以正确编程。 |

<a id="gab887999e8728bcc335a784afbdbbee8f"></a>

### `fpga_get_info()`

```c
const char * fpga_get_info ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

返回 FPGA 的相关信息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |

**返回（Returns）**：返回值：包含相关信息的字符串。

<a id="ga1a1e78a46df9f4bd374cf5ecc2449360"></a>

### `fpga_get_status()`

```c
enum FPGA_status fpga_get_status ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

读取现场可编程门阵列（FPGA）的状态。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | FPGA 处于 `INACTIVE` 状态时。 |
| `1` | FPGA 处于 `ACTIVE` 状态时。 |

<a id="ga1cace6c7cc44705bf861d7aa5e863e16"></a>

### `fpga_load()`

```c
int fpga_load ( const struct device * dev, uint32_t * image_ptr, uint32_t img_size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

加载位流（Bitstream）并配置 FPGA。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |
| `image_ptr` | 指向比特流（bitstream）的指针。 |
| `img_size` | 比特流大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

**返回（Returns）**：返回值：其他情况下表示失败。

<a id="gaa161c7a7006db24793c1a1ecdea25b5c"></a>

### `fpga_off()`

```c
int fpga_off ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

关闭 FPGA。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `<0` | 失败时返回负 `errno` 错误码。 |

<a id="gad9093bd96c6a62cd958718d1e01e3f37"></a>

### `fpga_on()`

```c
int fpga_on ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

开启 FPGA。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `<0` | 失败时返回负 `errno` 错误码。 |

<a id="gadfc8d6c24cb1b1640393017a462011c9"></a>

### `fpga_reset()`

```c
int fpga_reset ( const struct device * dev)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/fpga.h>
```

复位 FPGA。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | FPGA 设备结构体。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |

**返回（Returns）**：返回值：其他情况下表示失败。


## 13.7\_原页交叉引用（Cross References）

- [FPGA 驱动后端 API（Driver Backend API）](../api_device_topic_reference/P009_FPGA 驱动后端 API（Driver Backend API）.md)
- [fpga.h](../peripheral_bus_storage_header_reference/P006_zephyr__drivers__fpga.h_头文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga0bbacdfdac79bace1786bb2a1627bb1ea46571663477ca2df50b24cf93a5e2441"></a>
<a id="gga0bbacdfdac79bace1786bb2a1627bb1eac1b036277b07dfdef1dd1c3e1a299131"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P012_EPORTRSTR 复位控制（Reset Control）.md) · [返回大纲](大纲.md) · [下一章](P014_互联网组管理协议（IGMP）的API。.md)
