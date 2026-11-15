---
id: learning.zephyr-docs.api-network-time-topic-reference.page-26
title: USB-C 总线电源（VBUS）API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_USB-C 总线电源（VBUS）API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__usbc__vbus__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB-C 总线电源（VBUS）API

<a id="details"></a>

USB-C VBUS API。自 Zephyr 3.3 起提供；API 版本为 0.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 26.1\_主题（Topics）

<a id="r_usbc_5Fvbus_5Fapi_5Fbackend"></a>

相关声明：[USB-C VBUS 驱动后端 API](../api_platform_topic_reference/P125_USB-C VBUS 驱动后端 API.md)。

<a id="header-files"></a>
<a id="files"></a>

## 26.2\_文件（Files）

<a id="r_usbc_5Fvbus_2Eh"></a>

```c
file usbc_vbus.h
```

相关声明：[usbc_vbus.h](../api_file_interface_reference/P062_zephyr__drivers__usb_c__usbc_vbus.h_文件参考.md)。

USB-C VBUS的设备API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.3\_函数（Functions）

<a id="r_ga421653274fe9b8e2e6237a4bbe47e3ad"></a>

```c
static bool usbc_vbus_check_level (const struct device *dev, enum tc_vbus_level level)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[usbc_vbus_check_level](#ga421653274fe9b8e2e6237a4bbe47e3ad)、[device](../device_reference/P002_设备对象结构.md)、[tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)。

检查 VBUS 是否处于特定电平（level）。

<a id="r_ga0b6c561c5f74a30d54397294cb21660d"></a>

```c
static int usbc_vbus_measure (const struct device *dev, int *meas)
```

相关声明：[usbc_vbus_measure](#ga0b6c561c5f74a30d54397294cb21660d)、[device](../device_reference/P002_设备对象结构.md)。

读取并返回 VBUS 电压，单位为 mV。

<a id="r_ga8414cfcfeee7799ea57854c59c0c1677"></a>

```c
static int usbc_vbus_discharge (const struct device *dev, bool enable)
```

相关声明：[usbc_vbus_discharge](#ga8414cfcfeee7799ea57854c59c0c1677)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制用于对 VBUS 放电（discharge）的引脚。

<a id="r_ga7c94eac0f28be6cd12717d2f1a50ec54"></a>

```c
static int usbc_vbus_enable (const struct device *dev, bool enable)
```

相关声明：[usbc_vbus_enable](#ga7c94eac0f28be6cd12717d2f1a50ec54)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

控制用于启用 VBUS 测量（measurement）的引脚。

## 26.4\_详细说明（Detailed Documentation）

<a id="ga421653274fe9b8e2e6237a4bbe47e3ad"></a>

### `usbc_vbus_check_level()`

```c
bool usbc_vbus_check_level ( const struct device * dev, enum tc_vbus_level level )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

检查 VBUS 是否处于特定电平（level）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `level` | 用于比较检查的电平电压（level voltage）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | VBUS 处于该电平电压时。 |
| `false` | VBUS 不处于该电平电压时。 |

<a id="ga8414cfcfeee7799ea57854c59c0c1677"></a>

### `usbc_vbus_discharge()`

```c
int usbc_vbus_discharge ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

控制用于对 VBUS 放电（discharge）的引脚。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 true 时对 VBUS 放电（discharge）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOENT` | 未定义放电引脚时。 |

<a id="ga7c94eac0f28be6cd12717d2f1a50ec54"></a>

### `usbc_vbus_enable()`

```c
int usbc_vbus_enable ( const struct device * dev, bool enable )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

控制用于启用 VBUS 测量（measurement）的引脚。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `enable` | 为 true 时启用 VBUS 测量。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |
| `-ENOENT` | 未定义使能引脚时。 |

<a id="ga0b6c561c5f74a30d54397294cb21660d"></a>

### `usbc_vbus_measure()`

```c
int usbc_vbus_measure ( const struct device * dev, int * meas )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/usb_c/usbc_vbus.h>
```

读取并返回 VBUS 电压，单位为 mV。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 运行时设备结构体（runtime device structure）。 |
| `meas` | 用于保存 VBUS 电压测量值的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EIO` | 失败。 |


## 26.5\_原页交叉引用（Cross References）

- [USB-C VBUS 驱动后端 API](../api_platform_topic_reference/P125_USB-C VBUS 驱动后端 API.md)
- [usbc_vbus.h](../api_file_interface_reference/P062_zephyr__drivers__usb_c__usbc_vbus.h_文件参考.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [device](../device_reference/P002_设备对象结构.md)
- [tc_vbus_level](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__type__c.html#ga015455a6c5620dfc96cfb713bbb72161)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)
- [false](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a65e9886d74aaee76545e83dd09011727)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P025_触摸屏事件（Touchscreen Events）.md) · [返回大纲](大纲.md)
