---
id: learning.zephyr-docs.api-file-system-device-reference.page-55
title: zephyr__drivers__usb__usb_buf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_drivers\_\_usb\_\_usb\_buf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/usb__buf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

USB设备支持使用的缓冲区（Buffers）。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
```

查看此文件的源码。

USB设备支持使用的缓冲区（Buffers）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 55.1\_宏定义（Macros）

<a id="r_ga7c04001e0a2fba2d343d7d2eee6aff37"></a>

```c
#define USB_BUF_ALIGN USB_PRIV_BUFALIGN
```

相关声明：[USB_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)。

USB 设备控制器（UDC）驱动要求的缓冲区对齐（alignment）。

<a id="r_ga52954c29bc5f64f5e7b8fc3b881a11bf"></a>

```c
#define USB_BUF_GRANULARITY USB_PRIV_BUFGRANULARITY
```

相关声明：[USB_BUF_GRANULARITY](../usb/P039_USB缓冲区宏与定义.md#ga52954c29bc5f64f5e7b8fc3b881a11bf)。

UDC 驱动要求的缓冲区粒度（granularity）。

<a id="r_ga5cfb8cab648a98fbc21ec1edbce057b7"></a>

```c
#define USB_BUF_ROUND_UP(size)
```

相关声明：[USB_BUF_ROUND_UP](../usb/P039_USB缓冲区宏与定义.md#ga5cfb8cab648a98fbc21ec1edbce057b7)。

向上取整到 UDC 驱动要求的粒度。

<a id="r_gac3e4ef96b046b995e0365bd3528cd32e"></a>

```c
#define USB_STATIC_BUF_DEFINE(name, size)
```

相关声明：[USB_STATIC_BUF_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gac3e4ef96b046b995e0365bd3528cd32e)。

定义符合 UDC 驱动要求的静态缓冲区。

<a id="r_ga07b92466efcdf72a561f50f141f7b0b3"></a>

```c
#define IS_USB_BUF_ALIGNED(buf)
```

相关声明：[IS_USB_BUF_ALIGNED](../usb/P039_USB缓冲区宏与定义.md#ga07b92466efcdf72a561f50f141f7b0b3)。

验证缓冲区是否按 UDC 驱动要求对齐。

<a id="r_gadad8a14719e700eee228eff922ec6fbd"></a>

```c
#define USB_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)
```

相关声明：[USB_BUF_POOL_VAR_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gadad8a14719e700eee228eff922ec6fbd)。

为可变大小有效载荷（variable-size payloads）的 UDC 缓冲区定义新池。

<a id="r_ga9dd362f9f98bda540c8bafa958345053"></a>

```c
#define USB_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)
```

相关声明：[USB_BUF_POOL_DEFINE](../usb/P039_USB缓冲区宏与定义.md#ga9dd362f9f98bda540c8bafa958345053)。

基于固定大小数据，为 UDC 缓冲区定义新池。

<a id="r_gaf53404357b1184c1eda430e92cd696dc"></a>

```c
#define UDC_BUF_ALIGN USB_BUF_ALIGN
```

相关声明：[UDC_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#gaf53404357b1184c1eda430e92cd696dc)、[USB_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)。

USB 设备控制器（UDC）驱动要求的缓冲区对齐（alignment）。

<a id="r_ga87ea6bf98e8be1ca3378928fbf03bf8e"></a>

```c
#define UDC_BUF_GRANULARITY USB_BUF_GRANULARITY
```

相关声明：[UDC_BUF_GRANULARITY](../usb/P039_USB缓冲区宏与定义.md#ga87ea6bf98e8be1ca3378928fbf03bf8e)、[USB_BUF_GRANULARITY](../usb/P039_USB缓冲区宏与定义.md#ga52954c29bc5f64f5e7b8fc3b881a11bf)。

UDC 驱动要求的缓冲区粒度（granularity）。

<a id="r_ga683a98bd402195fd5b57e6b3b9fe6e4a"></a>

```c
#define UDC_ROUND_UP(size)
```

相关声明：[UDC_ROUND_UP](../usb/P039_USB缓冲区宏与定义.md#ga683a98bd402195fd5b57e6b3b9fe6e4a)。

向上取整到 UDC 驱动要求的粒度。

<a id="r_gae5cb6affd574da5f4cd0c25e9178a0eb"></a>

```c
#define UDC_STATIC_BUF_DEFINE(name, size)
```

相关声明：[UDC_STATIC_BUF_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gae5cb6affd574da5f4cd0c25e9178a0eb)。

定义符合 UDC 驱动要求的静态缓冲区。

<a id="r_ga4e77ceb9142c9d414966f0c4e0eb7710"></a>

```c
#define IS_UDC_ALIGNED(buf)
```

相关声明：[IS_UDC_ALIGNED](../usb/P039_USB缓冲区宏与定义.md#ga4e77ceb9142c9d414966f0c4e0eb7710)。

验证缓冲区是否按 UDC 驱动要求对齐。

<a id="r_ga064d3f73dbde0f98479ffdad5141e8c0"></a>

```c
#define UDC_BUF_POOL_VAR_DEFINE(pname, count, size, ud_size, fdestroy)
```

相关声明：[UDC_BUF_POOL_VAR_DEFINE](../usb/P039_USB缓冲区宏与定义.md#ga064d3f73dbde0f98479ffdad5141e8c0)。

基于固定大小数据，为 UDC 缓冲区定义新池。

<a id="r_gac96f1518df5748927c3377cb3abc222d"></a>

```c
#define UDC_BUF_POOL_DEFINE(pname, count, size, ud_size, fdestroy)
```

相关声明：[UDC_BUF_POOL_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gac96f1518df5748927c3377cb3abc222d)。

基于固定大小数据，为 UDC 缓冲区定义新池。


## 55.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_runtime_reference/P066_usb_buf.h_源码浏览.md)
- [USB_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#ga7c04001e0a2fba2d343d7d2eee6aff37)
- [USB_BUF_GRANULARITY](../usb/P039_USB缓冲区宏与定义.md#ga52954c29bc5f64f5e7b8fc3b881a11bf)
- [USB_BUF_ROUND_UP](../usb/P039_USB缓冲区宏与定义.md#ga5cfb8cab648a98fbc21ec1edbce057b7)
- [USB_STATIC_BUF_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gac3e4ef96b046b995e0365bd3528cd32e)
- [IS_USB_BUF_ALIGNED](../usb/P039_USB缓冲区宏与定义.md#ga07b92466efcdf72a561f50f141f7b0b3)
- [USB_BUF_POOL_VAR_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gadad8a14719e700eee228eff922ec6fbd)
- [USB_BUF_POOL_DEFINE](../usb/P039_USB缓冲区宏与定义.md#ga9dd362f9f98bda540c8bafa958345053)
- [UDC_BUF_ALIGN](../usb/P039_USB缓冲区宏与定义.md#gaf53404357b1184c1eda430e92cd696dc)
- [UDC_BUF_GRANULARITY](../usb/P039_USB缓冲区宏与定义.md#ga87ea6bf98e8be1ca3378928fbf03bf8e)
- [UDC_ROUND_UP](../usb/P039_USB缓冲区宏与定义.md#ga683a98bd402195fd5b57e6b3b9fe6e4a)
- [UDC_STATIC_BUF_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gae5cb6affd574da5f4cd0c25e9178a0eb)
- [IS_UDC_ALIGNED](../usb/P039_USB缓冲区宏与定义.md#ga4e77ceb9142c9d414966f0c4e0eb7710)
- [UDC_BUF_POOL_VAR_DEFINE](../usb/P039_USB缓冲区宏与定义.md#ga064d3f73dbde0f98479ffdad5141e8c0)
- [UDC_BUF_POOL_DEFINE](../usb/P039_USB缓冲区宏与定义.md#gac96f1518df5748927c3377cb3abc222d)

<a id="header-details"></a>

---

[上一章](P054_zephyr__mgmt__updatehub.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__dt-bindings__pwm__wisblock-pwm.h_文件参考.md)
