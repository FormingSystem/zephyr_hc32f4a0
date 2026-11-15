---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-41
title: mspi_dev_id_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__id.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第41章\_mspi\_dev\_id\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__id.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI设备标识（Device ID）。在多设备方案中，控制器可据此识别其设备，并判断是否允许访问。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI设备标识（Device ID）。在多设备方案中，控制器可据此识别其设备，并判断是否允许访问。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 41.1\_数据成员（Data Fields）

<a id="r_ac79d41731c8599f23b666f78cdb58bf0"></a>

```c
struct gpio_dt_spec ce
```

相关声明：[gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)、[ce](#ac79d41731c8599f23b666f78cdb58bf0)。

设备的 GPIO 片选使能（CE）。

<a id="r_aab54e4f449d4cfb87c5c6f0ccd1d7bfb"></a>

```c
uint16_t dev_idx
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[dev_idx](#aab54e4f449d4cfb87c5c6f0ccd1d7bfb)。

设备在设备树（DT）中的索引。

## 41.2\_详细说明（Detailed Documentation）

<a id="ac79d41731c8599f23b666f78cdb58bf0"></a>

### `ce`

```c
struct gpio_dt_spec mspi_dev_id::ce
```

设备的 GPIO 片选使能（CE）。

<a id="aab54e4f449d4cfb87c5c6f0ccd1d7bfb"></a>

### `dev_idx`

```c
uint16_t mspi_dev_id::dev_idx
```

设备在设备树（DT）中的索引。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 41.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P040_mspi_dev_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P042_mspi_driver_api_结构体.md)
