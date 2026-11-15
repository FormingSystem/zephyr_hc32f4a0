---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-43
title: mspi_dt_spec_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dt__spec.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_mspi\_dt\_spec\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dt__spec.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI设备树（DT）信息。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI设备树（DT）信息。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 43.1\_数据成员（Data Fields）

<a id="r_ab21ff3d5959b78f5b5cdc7fcf70e8756"></a>

```c
const struct device * bus
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[bus](#ab21ff3d5959b78f5b5cdc7fcf70e8756)。

MSPI 总线。

<a id="r_aaedbcdc55394032e3af50ec7d2e8f439"></a>

```c
struct mspi_cfg config
```

相关声明：[mspi_cfg](P039_mspi_cfg_结构体.md)、[config](#aaedbcdc55394032e3af50ec7d2e8f439)。

MSPI 硬件特定配置。

## 43.2\_详细说明（Detailed Documentation）

<a id="ab21ff3d5959b78f5b5cdc7fcf70e8756"></a>

### `bus`

```c
const struct device* mspi_dt_spec::bus
```

MSPI 总线。

<a id="aaedbcdc55394032e3af50ec7d2e8f439"></a>

### `config`

```c
struct mspi_cfg mspi_dt_spec::config
```

MSPI 硬件特定配置。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 43.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_cfg](P039_mspi_cfg_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P042_mspi_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P044_mspi_dw_timing_cfg_结构体.md)
