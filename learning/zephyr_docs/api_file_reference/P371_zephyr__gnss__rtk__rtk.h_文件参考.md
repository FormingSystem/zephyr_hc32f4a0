---
id: learning.zephyr-docs.api-file-reference.page-371
title: zephyr__gnss__rtk__rtk.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第371章\_zephyr\_\_gnss\_\_rtk\_\_rtk.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/rtk_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <stddef.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 371.1\_数据结构（Data Structures）

<a id="r_gnss_5Frtk_5Fdata"></a>

```c
struct gnss_rtk_data
```

相关声明：[gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)。

<a id="r_gnss_5Frtk_5Fdata_5Fcallback"></a>

```c
struct gnss_rtk_data_callback
```

相关声明：[gnss_rtk_data_callback](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 371.2\_宏定义（Macros）

<a id="r_a823c6d6f0975df9c6513998ed7ab6016"></a>

```c
#define GNSS_RTK_DATA_CALLBACK_DEFINE(_dev, _callback)
```

相关声明：[GNSS_RTK_DATA_CALLBACK_DEFINE](#a823c6d6f0975df9c6513998ed7ab6016)。

<a id="r_a4e9e710a110ac2340f3314cdf4d3a872"></a>

```c
#define GNSS_DT_RTK_DATA_CALLBACK_DEFINE(_node_id, _callback)
```

相关声明：[GNSS_DT_RTK_DATA_CALLBACK_DEFINE](#a4e9e710a110ac2340f3314cdf4d3a872)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 371.3\_类型定义（Typedefs）

<a id="r_a3fdf2f1d4f0414cc99c926a6fa06acf2"></a>

```c
typedef void(* gnss_rtk_data_callback_t) (const struct device *dev, const struct gnss_rtk_data *data)
```

相关声明：[gnss_rtk_data_callback_t](#a3fdf2f1d4f0414cc99c926a6fa06acf2)、[device](../device_reference/P002_设备对象结构.md)、[gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)。

## 371.4\_详细说明（Detailed Documentation）

<a id="a4e9e710a110ac2340f3314cdf4d3a872"></a>

### `GNSS_DT_RTK_DATA_CALLBACK_DEFINE`

```c
#define GNSS_DT_RTK_DATA_CALLBACK_DEFINE ( _node_id, _callback )
```

<a id="a823c6d6f0975df9c6513998ed7ab6016"></a>

### `GNSS_RTK_DATA_CALLBACK_DEFINE`

```c
#define GNSS_RTK_DATA_CALLBACK_DEFINE ( _dev, _callback )
```

<a id="a3fdf2f1d4f0414cc99c926a6fa06acf2"></a>

### `gnss_rtk_data_callback_t`

```c
typedef void(* gnss_rtk_data_callback_t) (const struct device *dev, const struct gnss_rtk_data *data)
```


## 371.5\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P733_rtk.h_源码浏览.md)
- [gnss_rtk_data](../sensor_navigation_model_reference/P013_gnss_rtk_data_结构体.md)
- [gnss_rtk_data_callback](../sensor_navigation_model_reference/P014_gnss_rtk_data_callback_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>

---

[上一章](P370_zephyr__dt-bindings__clock__rpi_pico_rp2350_clock.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P372_zephyr__gnss__rtk__rtk_publish.h_文件参考.md)
