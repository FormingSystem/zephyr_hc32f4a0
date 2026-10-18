---
id: learning.zephyr-docs.api-protocol-topic-reference.page-44
title: PECI 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_PECI 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现平台环境控制接口（PECI）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 44.1\_数据结构（Data Structures）

<a id="r_peci_5Fdriver_5Fapi"></a>

```c
struct peci_driver_api
```

相关声明：[peci_driver_api](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md)。

驱动操作（Driver Operations）：平台环境控制接口（PECI）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 44.2\_类型定义（Typedefs）

<a id="r_gabdb55d1aeea952970562c58f7c901361"></a>

```c
typedef int(* peci_config_t) (const struct device *dev, uint32_t bitrate)
```

相关声明：[peci_config_t](#gabdb55d1aeea952970562c58f7c901361)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置 PECI 接口的回调 API。

<a id="r_ga3addf7ae61d89626f7d8889910c6f5b9"></a>

```c
typedef int(* peci_transfer_t) (const struct device *dev, struct peci_msg *msg)
```

相关声明：[peci_transfer_t](#ga3addf7ae61d89626f7d8889910c6f5b9)、[device](../device_reference/P002_设备对象结构.md)、[peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)。

执行 PECI 事务的回调 API。

<a id="r_ga97cd68ca4d0b79a6ff8fc19828e0cb76"></a>

```c
typedef int(* peci_disable_t) (const struct device *dev)
```

相关声明：[peci_disable_t](#ga97cd68ca4d0b79a6ff8fc19828e0cb76)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PECI 接口的回调 API。

<a id="r_ga60a85f356ed8f18050f1a4cd02389c77"></a>

```c
typedef int(* peci_enable_t) (const struct device *dev)
```

相关声明：[peci_enable_t](#ga60a85f356ed8f18050f1a4cd02389c77)、[device](../device_reference/P002_设备对象结构.md)。

启用 PECI 接口的回调 API。

## 44.3\_详细说明（Detailed Documentation）

<a id="gabdb55d1aeea952970562c58f7c901361"></a>

### `peci_config_t`

```c
typedef int(* peci_config_t) (const struct device *dev, uint32_t bitrate)
```

```c
#include <zephyr/drivers/peci.h>
```

配置 PECI 接口的回调 API。

参数说明参见 `peci_config()`。

<a id="ga97cd68ca4d0b79a6ff8fc19828e0cb76"></a>

### `peci_disable_t`

```c
typedef int(* peci_disable_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/peci.h>
```

禁用 PECI 接口的回调 API。

参数说明参见 `peci_disable()`。

<a id="ga60a85f356ed8f18050f1a4cd02389c77"></a>

### `peci_enable_t`

```c
typedef int(* peci_enable_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/peci.h>
```

启用 PECI 接口的回调 API。

参数说明参见 `peci_enable()`。

<a id="ga3addf7ae61d89626f7d8889910c6f5b9"></a>

### `peci_transfer_t`

```c
typedef int(* peci_transfer_t) (const struct device *dev, struct peci_msg *msg)
```

```c
#include <zephyr/drivers/peci.h>
```

执行 PECI 事务的回调 API。

参数说明参见 `peci_transfer()`。


## 44.4\_原页交叉引用（Cross References）

- [peci_driver_api](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)
- [zephyr/drivers/peci.h](../peripheral_bus_storage_header_reference/P021_zephyr__drivers__peci.h_头文件参考.md)
- [peci_config()](../api_extension_topic_reference/P026_平台环境控制接口（PECI）.md#gaa1fee6839b68eed73f0a8d93b3a3ec82)
- [peci_disable()](../api_extension_topic_reference/P026_平台环境控制接口（PECI）.md#gaf197262cd58db5eb7691d1ce816057de)
- [peci_enable()](../api_extension_topic_reference/P026_平台环境控制接口（PECI）.md#gaa42e2e015a2c778a9eaf2dc1b697630f)
- [peci_transfer()](../api_extension_topic_reference/P026_平台环境控制接口（PECI）.md#gacf15bdae6483ad3e9498ed984a959687)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P043_PAT9136 API主题.md) · [返回大纲](大纲.md) · [下一章](P045_FocalTech FT9001 引脚控制辅助工具（Pin control helpers）.md)
