---
id: learning.zephyr-docs.api-file-service-interface-reference.page-11
title: zephyr__drivers__uart__cdc_acm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_uart\_\_cdc\_acm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cdc__acm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通信设备类抽象控制模型（CDC ACM）类驱动的公共API。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/device.h>
```

查看此文件的源码。

通信设备类抽象控制模型（CDC ACM）类驱动的公共API。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.1\_类型定义（Typedefs）

<a id="r_a0b2e4a171e5d56dba45c3d2e7cef72b4"></a>

```c
typedef void(* cdc_dte_rate_callback_t) (const struct device *dev, uint32_t rate)
```

相关声明：[cdc_dte_rate_callback_t](#a0b2e4a171e5d56dba45c3d2e7cef72b4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

USB 主机改变波特率（Baud Rate）时调用的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.2\_函数（Functions）

<a id="r_a5b71bd70532ed059fb31a1ee3e73eaa5"></a>

```c
int cdc_acm_dte_rate_callback_set (const struct device *dev, cdc_dte_rate_callback_t callback)
```

相关声明：[cdc_acm_dte_rate_callback_set](#a5b71bd70532ed059fb31a1ee3e73eaa5)、[device](../device_reference/P002_设备对象结构.md)、[cdc_dte_rate_callback_t](#a0b2e4a171e5d56dba45c3d2e7cef72b4)。

设置处理 `dwDTERate SetLineCoding` 请求的回调。

## 11.3\_详细说明（Detailed Documentation）

<a id="a0b2e4a171e5d56dba45c3d2e7cef72b4"></a>

### `cdc_dte_rate_callback_t`

```c
typedef void(* cdc_dte_rate_callback_t) (const struct device *dev, uint32_t rate)
```

USB 主机改变波特率（Baud Rate）时调用的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | CDC ACM 设备的设备结构体（Device Struct）。 |
| `rate` | 新的 USB 波特率（Baud Rate）。 |

<a id="a5b71bd70532ed059fb31a1ee3e73eaa5"></a>

### `cdc_acm_dte_rate_callback_set()`

```c
int cdc_acm_dte_rate_callback_set ( const struct device * dev, cdc_dte_rate_callback_t callback )
```

设置处理 `dwDTERate SetLineCoding` 请求的回调。

USB 主机改变波特率（Baud Rate）时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | CDC ACM 设备结构体（Device Structure）。 |
| `callback` | 事件处理函数（Event Handler）。 |

**已弃用（Deprecated）**：**已弃用（Deprecated）：**改用 USB 设备核心 API（USB Device Core API）及 `USBD_MSG_CDC_ACM_LINE_CODING`。

**说明（Note）**：**注意（Note）：**仅在启用 `CONFIG_CDC_ACM_DTE_RATE_CALLBACK_SUPPORT` 时提供本函数。

返回（Returns）：成功为0。


## 11.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P024_cdc_acm.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [Deprecated](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000065)
- [USB 设备核心 API（Device core API）](../usb/P015_USB设备核心API.md)
- [USBD_MSG_CDC_ACM_LINE_CODING](../usb/P016_USB设备消息API.md#ggaa9163408c0006825575a919322f25f56a820f9547e0db4baea563dca9c211f9b1)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__busy_sim.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__clock_control__clock_control_ti_cdce9xx.h_文件参考.md)
