---
id: learning.zephyr-docs.api-protocol-topic-reference.page-52
title: PS_2 驱动后端 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_PS\_2 驱动后端 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ps2__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现 PS/2 驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 52.1\_数据结构（Data Structures）

<a id="r_ps2_5Fdriver_5Fapi"></a>

```c
struct ps2_driver_api
```

相关声明：[ps2_driver_api](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md)。

驱动操作（Driver Operations）：PS/2驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 52.2\_类型定义（Typedefs）

<a id="r_ga7fb2edbebe2523efde6c7f73bffb850a"></a>

```c
typedef int(* ps2_config_t) (const struct device *dev, ps2_callback_t callback_isr)
```

相关声明：[ps2_config_t](#ga7fb2edbebe2523efde6c7f73bffb850a)、[device](../device_reference/P002_设备对象结构.md)、[ps2_callback_t](P051_PS_2 API主题.md#gad7cf29301681fac0d2a359d425a13b5f)。

配置 PS/2 设备的回调 API。

<a id="r_ga3d5a1b7e613e0e2b1a28689b9ab52ca5"></a>

```c
typedef int(* ps2_read_t) (const struct device *dev, uint8_t *value)
```

相关声明：[ps2_read_t](#ga3d5a1b7e613e0e2b1a28689b9ab52ca5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 PS/2 设备读取的回调 API。

<a id="r_gaf7a935b2e1debd819792dbb02bd84ee2"></a>

```c
typedef int(* ps2_write_t) (const struct device *dev, uint8_t value)
```

相关声明：[ps2_write_t](#gaf7a935b2e1debd819792dbb02bd84ee2)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 PS/2 设备写入的回调 API。

<a id="r_gaaa51cb5cf5f5d7560c35374561746f6d"></a>

```c
typedef int(* ps2_disable_callback_t) (const struct device *dev)
```

相关声明：[ps2_disable_callback_t](#gaaa51cb5cf5f5d7560c35374561746f6d)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PS/2 设备回调的回调 API。

<a id="r_gaad5d2a31e2f4768953b6d611364e748c"></a>

```c
typedef int(* ps2_enable_callback_t) (const struct device *dev)
```

相关声明：[ps2_enable_callback_t](#gaad5d2a31e2f4768953b6d611364e748c)、[device](../device_reference/P002_设备对象结构.md)。

启用 PS/2 设备回调的回调 API。

## 52.3\_详细说明（Detailed Documentation）

<a id="ga7fb2edbebe2523efde6c7f73bffb850a"></a>

### `ps2_config_t`

```c
typedef int(* ps2_config_t) (const struct device *dev, ps2_callback_t callback_isr)
```

```c
#include <zephyr/drivers/ps2.h>
```

配置 PS/2 设备的回调 API。

**参阅（See Also）**：另请参阅 `ps2_config()` 中的参数说明。

<a id="gaaa51cb5cf5f5d7560c35374561746f6d"></a>

### `ps2_disable_callback_t`

```c
typedef int(* ps2_disable_callback_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/ps2.h>
```

禁用 PS/2 设备回调的回调 API。

<a id="gaad5d2a31e2f4768953b6d611364e748c"></a>

### `ps2_enable_callback_t`

```c
typedef int(* ps2_enable_callback_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/ps2.h>
```

启用 PS/2 设备回调的回调 API。

**参阅（See Also）**：另请参阅 `ps2_enable_callback()` 中的参数说明。

<a id="ga3d5a1b7e613e0e2b1a28689b9ab52ca5"></a>

### `ps2_read_t`

```c
typedef int(* ps2_read_t) (const struct device *dev, uint8_t *value)
```

```c
#include <zephyr/drivers/ps2.h>
```

从 PS/2 设备读取的回调 API。

**参阅（See Also）**：另请参阅 `ps2_read()` 中的参数说明。

<a id="gaf7a935b2e1debd819792dbb02bd84ee2"></a>

### `ps2_write_t`

```c
typedef int(* ps2_write_t) (const struct device *dev, uint8_t value)
```

```c
#include <zephyr/drivers/ps2.h>
```

向 PS/2 设备写入的回调 API。

**参阅（See Also）**：另请参阅 `ps2_write()` 中的参数说明。


## 52.4\_原页交叉引用（Cross References）

- [ps2_driver_api](../peripheral_bus_storage_model_reference/P069_ps2_driver_api_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [ps2_callback_t](P051_PS_2 API主题.md#gad7cf29301681fac0d2a359d425a13b5f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/drivers/ps2.h](../peripheral_bus_storage_header_reference/P022_zephyr__drivers__ps2.h_头文件参考.md)
- [ps2_config()](P051_PS_2 API主题.md#ga8d6da9b966432defb0cd482003c11f15)
- [ps2_enable_callback()](P051_PS_2 API主题.md#ga9568487018f4ef972eb463ea2098e254)
- [ps2_read()](P051_PS_2 API主题.md#gab91b1efe1f07d409607922f4eb87b221)
- [ps2_write()](P051_PS_2 API主题.md#gae291cb991ae9525552fdb52c2fa4ac5e)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P051_PS_2 API主题.md) · [返回大纲](大纲.md) · [下一章](P053_精确时间协议时钟（PTP Clock）.md)
