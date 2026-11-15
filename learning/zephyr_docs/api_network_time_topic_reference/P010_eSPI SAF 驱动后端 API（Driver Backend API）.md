---
id: learning.zephyr-docs.api-network-time-topic-reference.page-10
title: eSPI SAF 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_eSPI SAF 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现增强型串行外设接口（eSPI）的共享挂接闪存（Shared Attached Flash，SAF）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 10.1\_数据结构（Data Structures）

<a id="r_espi_5Fsaf_5Fdriver_5Fapi"></a>

```c
struct espi_saf_driver_api
```

相关声明：[espi_saf_driver_api](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md)。

驱动操作（Driver Operations）：eSPI SAF驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 10.2\_类型定义（Typedefs）

<a id="r_ga5f422a48cf008d7a737ec6a3fd0f0400"></a>

```c
typedef int(* espi_saf_api_config) (const struct device *dev, const struct espi_saf_cfg *cfg)
```

相关声明：[espi_saf_api_config](#ga5f422a48cf008d7a737ec6a3fd0f0400)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)。

配置 eSPI 从设备附接 Flash（SAF）控制器的回调 API。

<a id="r_gaeb3c1ee73f50fd05737f28a75013c2a8"></a>

```c
typedef int(* espi_saf_api_set_protection_regions) (const struct device *dev, const struct espi_saf_protection *pr)
```

相关声明：[espi_saf_api_set_protection_regions](#gaeb3c1ee73f50fd05737f28a75013c2a8)、[device](../device_reference/P002_设备对象结构.md)。

设置一个或多个 SAF 保护区域的回调 API。

<a id="r_ga03a72ef8a19738d90681114f478ff068"></a>

```c
typedef int(* espi_saf_api_activate) (const struct device *dev)
```

相关声明：[espi_saf_api_activate](#ga03a72ef8a19738d90681114f478ff068)、[device](../device_reference/P002_设备对象结构.md)。

激活 SAF 模块的回调 API。

<a id="r_ga6ac9186c5b022f79dd8671594450efff"></a>

```c
typedef bool(* espi_saf_api_get_channel_status) (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[espi_saf_api_get_channel_status](#ga6ac9186c5b022f79dd8671594450efff)、[device](../device_reference/P002_设备对象结构.md)。

查询 SAF 是否就绪的回调 API。

<a id="r_ga6154711885b4edc54db016ba9826c176"></a>

```c
typedef int(* espi_saf_api_flash_read) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_read](#ga6154711885b4edc54db016ba9826c176)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 读取请求的回调 API。

<a id="r_ga24498afe1639bd7c5192215dc8bbbed9"></a>

```c
typedef int(* espi_saf_api_flash_write) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_write](#ga24498afe1639bd7c5192215dc8bbbed9)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 写入请求的回调 API。

<a id="r_ga4e8a12a1311d6604a61d1a9e57573e17"></a>

```c
typedef int(* espi_saf_api_flash_erase) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_erase](#ga4e8a12a1311d6604a61d1a9e57573e17)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

发送从设备附接 Flash 擦除请求的回调 API。

<a id="r_ga7c1aef03f238ced4e64c6e3be7ad643c"></a>

```c
typedef int(* espi_saf_api_flash_unsuccess) (const struct device *dev, struct espi_saf_packet *pckt)
```

相关声明：[espi_saf_api_flash_unsuccess](#ga7c1aef03f238ced4e64c6e3be7ad643c)、[device](../device_reference/P002_设备对象结构.md)、[espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)。

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应的回调 API。

<a id="r_ga20ae708179a104c9334fe8fd554e5e05"></a>

```c
typedef int(* espi_saf_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

相关声明：[espi_saf_api_manage_callback](#ga20ae708179a104c9334fe8fd554e5e05)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

管理应用程序回调的回调 API，包括添加和移除。

## 10.3\_详细说明（Detailed Documentation）

<a id="ga03a72ef8a19738d90681114f478ff068"></a>

### `espi_saf_api_activate`

```c
typedef int(* espi_saf_api_activate) (const struct device *dev)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

激活 SAF 模块的回调 API。

参数说明参见 `espi_saf_activate()`。

<a id="ga5f422a48cf008d7a737ec6a3fd0f0400"></a>

### `espi_saf_api_config`

```c
typedef int(* espi_saf_api_config) (const struct device *dev, const struct espi_saf_cfg *cfg)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

配置 eSPI 从设备附接 Flash（SAF）控制器的回调 API。

参数说明参见 `espi_saf_config()`。

<a id="ga4e8a12a1311d6604a61d1a9e57573e17"></a>

### `espi_saf_api_flash_erase`

```c
typedef int(* espi_saf_api_flash_erase) (const struct device *dev, struct espi_saf_packet *pckt)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 擦除请求的回调 API。

参数说明参见 `espi_saf_flash_erase()`。

<a id="ga6154711885b4edc54db016ba9826c176"></a>

### `espi_saf_api_flash_read`

```c
typedef int(* espi_saf_api_flash_read) (const struct device *dev, struct espi_saf_packet *pckt)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 读取请求的回调 API。

参数说明参见 `espi_saf_flash_read()`。

<a id="ga7c1aef03f238ced4e64c6e3be7ad643c"></a>

### `espi_saf_api_flash_unsuccess`

```c
typedef int(* espi_saf_api_flash_unsuccess) (const struct device *dev, struct espi_saf_packet *pckt)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

针对从设备附接 Flash 返回未成功完成（Unsuccessful completion）响应的回调 API。

参数说明参见 `espi_saf_flash_unsuccess()`。

<a id="ga24498afe1639bd7c5192215dc8bbbed9"></a>

### `espi_saf_api_flash_write`

```c
typedef int(* espi_saf_api_flash_write) (const struct device *dev, struct espi_saf_packet *pckt)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

发送从设备附接 Flash 写入请求的回调 API。

参数说明参见 `espi_saf_flash_write()`。

<a id="ga6ac9186c5b022f79dd8671594450efff"></a>

### `espi_saf_api_get_channel_status`

```c
typedef bool(* espi_saf_api_get_channel_status) (const struct device *dev)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

查询 SAF 是否就绪的回调 API。

参数说明参见 `espi_saf_get_channel_status()`。

<a id="ga20ae708179a104c9334fe8fd554e5e05"></a>

### `espi_saf_api_manage_callback`

```c
typedef int(* espi_saf_api_manage_callback) (const struct device *dev, struct espi_callback *callback, bool set)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

管理应用程序回调的回调 API，包括添加和移除。

参数说明参见 `espi_saf_add_callback()` 和 `espi_saf_remove_callback()`。

<a id="gaeb3c1ee73f50fd05737f28a75013c2a8"></a>

### `espi_saf_api_set_protection_regions`

```c
typedef int(* espi_saf_api_set_protection_regions) (const struct device *dev, const struct espi_saf_protection *pr)
```

```c
#include <zephyr/drivers/espi_saf.h>
```

设置一个或多个 SAF 保护区域的回调 API。

参数说明参见 `espi_saf_set_protection_regions()`。


## 10.4\_原页交叉引用（Cross References）

- [espi_saf_driver_api](../peripheral_bus_storage_model_reference/P016_espi_saf_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [espi_saf_cfg](../peripheral_bus_storage_model_reference/P015_espi_saf_cfg_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [espi_saf_packet](../peripheral_bus_storage_model_reference/P017_espi_saf_packet_结构体.md)
- [zephyr/drivers/espi_saf.h](../peripheral_bus_storage_header_reference/P005_zephyr__drivers__espi_saf.h_头文件参考.md)
- [espi_saf_activate()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaafe30738c18a16b056ed8dcf8638eb84)
- [espi_saf_config()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga34b0f6336aec45016d97528767b09434)
- [espi_saf_flash_erase()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga15855a2ac593b97dc1a3e83ac9eda300)
- [espi_saf_flash_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga0f5017eac05f928e635fec8e5f877c7d)
- [espi_saf_flash_unsuccess()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga6c54d9274b1a8e883484bd892f606fd5)
- [espi_saf_flash_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga104175f74019e58b8b7901f3dae245db)
- [espi_saf_get_channel_status()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga8b53a93559f0c67953e283f59107aa22)
- [espi_saf_add_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gadb881f847082f713bb0159d1e474980a)
- [espi_saf_remove_callback()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#gaf987842bc7dad310c7270aed50086af9)
- [espi_saf_set_protection_regions()](https://docs.zephyrproject.org/latest/doxygen/html/group__espi__saf__interface.html#ga273a9707f3ca501ed2dd3019cdeaa363)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P009_DHCPv6 服务器.md) · [返回大纲](大纲.md) · [下一章](P011_以太网桥转发数据库（Ethernet bridge FDB）.md)
