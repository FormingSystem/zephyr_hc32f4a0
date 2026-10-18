---
id: learning.zephyr-docs.api-file-runtime-reference.page-12
title: zephyr__drivers__sensor__icm4268x.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2icm4268x_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_drivers\_\_sensor\_\_icm4268x.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2sensor_2icm4268x_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

ICM4268X的扩展公共API（Extended Public API）。

<a id="details"></a>

```c
#include <zephyr/drivers/sensor.h>
```

查看此文件的源码。

ICM4268X 的扩展公共 API（Extended Public API）。在当前传感器驱动抽象（Sensor Driver Abstraction）下，通过属性（Attributes）配置引脚功能（Pin Function）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.1\_宏定义（Macros）

<a id="r_aeb3eac3210893146929958aaf7ec98ad"></a>

```c
#define ICM4268X_PIN9_FUNCTION_INT2 0
```

相关声明：[ICM4268X_PIN9_FUNCTION_INT2](#aeb3eac3210893146929958aaf7ec98ad)。

<a id="r_ade0ef01a6f215021da73e1e73509cde6"></a>

```c
#define ICM4268X_PIN9_FUNCTION_FSYNC 1
```

相关声明：[ICM4268X_PIN9_FUNCTION_FSYNC](#ade0ef01a6f215021da73e1e73509cde6)。

<a id="r_acf8bc21bf1f377ec0f57d465717fc341"></a>

```c
#define ICM4268X_PIN9_FUNCTION_CLKIN 2
```

相关声明：[ICM4268X_PIN9_FUNCTION_CLKIN](#acf8bc21bf1f377ec0f57d465717fc341)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.2\_枚举（Enumerations）

<a id="r_a31c9177c953fcc83378318205c7f7cba"></a>

```c
enum sensor_attribute_icm4268x { SENSOR_ATTR_ICM4268X_PIN9_FUNCTION = SENSOR_ATTR_PRIV_START }
```

相关声明：[sensor_attribute_icm4268x](#a31c9177c953fcc83378318205c7f7cba)、[SENSOR_ATTR_ICM4268X_PIN9_FUNCTION](#a31c9177c953fcc83378318205c7f7cbaa8272a53654e378ad009a571d10763148)。

ICM4268X 的扩展传感器属性（Extended Sensor Attributes）。

## 12.3\_详细说明（Detailed Documentation）

<a id="acf8bc21bf1f377ec0f57d465717fc341"></a>

### `ICM4268X_PIN9_FUNCTION_CLKIN`

```c
#define ICM4268X_PIN9_FUNCTION_CLKIN 2
```

<a id="ade0ef01a6f215021da73e1e73509cde6"></a>

### `ICM4268X_PIN9_FUNCTION_FSYNC`

```c
#define ICM4268X_PIN9_FUNCTION_FSYNC 1
```

<a id="aeb3eac3210893146929958aaf7ec98ad"></a>

### `ICM4268X_PIN9_FUNCTION_INT2`

```c
#define ICM4268X_PIN9_FUNCTION_INT2 0
```

<a id="a31c9177c953fcc83378318205c7f7cba"></a>

### `sensor_attribute_icm4268x`

```c
enum sensor_attribute_icm4268x
```

ICM4268X 的扩展传感器属性（Extended Sensor Attributes）。

用于设置引脚功能（Pin Function）的属性（Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SENSOR_ATTR_ICM4268X_PIN9_FUNCTION` |  |


## 12.4\_原页交叉引用（Cross References）

- [zephyr/drivers/sensor.h](https://docs.zephyrproject.org/latest/doxygen/html/sensor_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P174_icm4268x.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a31c9177c953fcc83378318205c7f7cbaa8272a53654e378ad009a571d10763148"></a>

---

[上一章](P011_zephyr__drivers__sensor__battery.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__net__dsa_core.h_文件参考.md)
