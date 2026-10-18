---
id: learning.zephyr-docs.api-auxiliary-topic-reference.page-1
title: BBRAM 驱动后端 API（Driver Backend API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_BBRAM 驱动后端 API（Driver Backend API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface__backend.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

本组包含实现电池备份 RAM（BBRAM）驱动所需的 API 类型定义、回调签名及其他辅助定义。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_bbram_5Fdriver_5Fapi"></a>

```c
struct bbram_driver_api
```

相关声明：[bbram_driver_api](../driver_model_reference/P024_电池备份RAM驱动接口.md)。

驱动操作（Driver Operations）：电池备份 RAM（Battery-backed RAM，BBRAM）驱动操作。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_gac23658302662587043f3587080f798fe"></a>

```c
typedef int(* bbram_api_check_invalid_t) (const struct device *dev)
```

相关声明：[bbram_api_check_invalid_t](#gac23658302662587043f3587080f798fe)、[device](../device_reference/P002_设备对象结构.md)。

用于检查 BBRAM 是否无效的回调 API。参数说明参见 `bbram_check_invalid()`。

<a id="r_ga99adefcb89ab80d8b5e24b8ffad8f43e"></a>

```c
typedef int(* bbram_api_check_standby_power_t) (const struct device *dev)
```

相关声明：[bbram_api_check_standby_power_t](#ga99adefcb89ab80d8b5e24b8ffad8f43e)、[device](../device_reference/P002_设备对象结构.md)。

用于检查待机电源故障（standby power failure）的回调 API。参数说明参见 `bbram_check_standby_power()`。

<a id="r_gaa6edc8a61529edad90de2e6fff619fdf"></a>

```c
typedef int(* bbram_api_check_power_t) (const struct device *dev)
```

相关声明：[bbram_api_check_power_t](#gaa6edc8a61529edad90de2e6fff619fdf)、[device](../device_reference/P002_设备对象结构.md)。

用于检查 VCC1 电源故障的回调 API。参数说明参见 `bbram_check_power()`。

<a id="r_gacfa586f705c520a6a05638a2e289fe50"></a>

```c
typedef int(* bbram_api_get_size_t) (const struct device *dev, size_t *size)
```

相关声明：[bbram_api_get_size_t](#gacfa586f705c520a6a05638a2e289fe50)、[device](../device_reference/P002_设备对象结构.md)。

用于获取 BBRAM 大小的回调 API。参数说明参见 `bbram_get_size()`。

<a id="r_ga8b06a1b3bb9b524597804dd268904881"></a>

```c
typedef int(* bbram_api_read_t) (const struct device *dev, size_t offset, size_t size, uint8_t *data)
```

相关声明：[bbram_api_read_t](#ga8b06a1b3bb9b524597804dd268904881)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于从 BBRAM 读取数据的回调 API。参数说明参见 `bbram_read()`。

<a id="r_ga1b111ae421791b9544777c1bab5e2a02"></a>

```c
typedef int(* bbram_api_write_t) (const struct device *dev, size_t offset, size_t size, const uint8_t *data)
```

相关声明：[bbram_api_write_t](#ga1b111ae421791b9544777c1bab5e2a02)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

用于向 BBRAM 写入数据的回调 API。

## 1.3\_详细说明（Detailed Documentation）

<a id="gac23658302662587043f3587080f798fe"></a>

### `bbram_api_check_invalid_t`

```c
typedef int(* bbram_api_check_invalid_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于检查 BBRAM 是否无效的回调 API。参数说明参见 `bbram_check_invalid()`。

<a id="gaa6edc8a61529edad90de2e6fff619fdf"></a>

### `bbram_api_check_power_t`

```c
typedef int(* bbram_api_check_power_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于检查 VCC1 电源故障的回调 API。参数说明参见 `bbram_check_power()`。

<a id="ga99adefcb89ab80d8b5e24b8ffad8f43e"></a>

### `bbram_api_check_standby_power_t`

```c
typedef int(* bbram_api_check_standby_power_t) (const struct device *dev)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于检查待机电源故障（standby power failure）的回调 API。参数说明参见 `bbram_check_standby_power()`。

<a id="gacfa586f705c520a6a05638a2e289fe50"></a>

### `bbram_api_get_size_t`

```c
typedef int(* bbram_api_get_size_t) (const struct device *dev, size_t *size)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于获取 BBRAM 大小的回调 API。参数说明参见 `bbram_get_size()`。

<a id="ga8b06a1b3bb9b524597804dd268904881"></a>

### `bbram_api_read_t`

```c
typedef int(* bbram_api_read_t) (const struct device *dev, size_t offset, size_t size, uint8_t *data)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于从 BBRAM 读取数据的回调 API。参数说明参见 `bbram_read()`。

<a id="ga1b111ae421791b9544777c1bab5e2a02"></a>

### `bbram_api_write_t`

```c
typedef int(* bbram_api_write_t) (const struct device *dev, size_t offset, size_t size, const uint8_t *data)
```

```c
#include <zephyr/drivers/bbram.h>
```

用于向 BBRAM 写入数据的回调 API。

参数说明参见 `bbram_write()`。


## 1.4\_原页交叉引用（Cross References）

- [bbram_driver_api](../driver_model_reference/P024_电池备份RAM驱动接口.md)
- [device](../device_reference/P002_设备对象结构.md)
- [bbram_check_invalid()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga7164969f308616696a9ab71a4d19b70b)
- [bbram_check_standby_power()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga948ed0a7d3824f950ad46b99ba3d86f4)
- [bbram_check_power()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga8fc2a647bda90e96f866514300180a96)
- [bbram_get_size()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#gab6bdb4a1cba88ca645c256366a696bdd)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bbram_read()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga9ef786b0fbac3f8523be2bb87b7cff7b)
- [zephyr/drivers/bbram.h](https://docs.zephyrproject.org/latest/doxygen/html/bbram_8h.html)
- [bbram_write()](https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__interface.html#ga51007eed4820aed341d20e4562607564)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_代理（Proxy）.md)
