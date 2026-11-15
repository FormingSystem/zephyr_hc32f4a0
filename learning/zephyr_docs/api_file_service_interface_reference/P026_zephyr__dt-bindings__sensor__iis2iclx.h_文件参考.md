---
id: learning.zephyr-docs.api-file-service-interface-reference.page-26
title: zephyr__dt-bindings__sensor__iis2iclx.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iis2iclx_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_dt-bindings\_\_sensor\_\_iis2iclx.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/iis2iclx_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

the ST IIS2ICLX inclinometer的设备树绑定常量（Devicetree Binding Constants）。

查看此文件的源码。

<a id="details"></a>

the ST IIS2ICLX inclinometer的设备树绑定常量（Devicetree Binding Constants）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 加速度计满量程范围（Accelerometer full-scale range）

设备树 `range` 属性的取值。

<a id="r_ga95903c983d457bc48d2a49efb7f2846c"></a>

```c
#define IIS2ICLX_DT_FS_500mG 0
```

相关声明：[IIS2ICLX_DT_FS_500mG](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga95903c983d457bc48d2a49efb7f2846c)。

量程（range）：±0.5 g。

<a id="r_ga3d96639b08dc2d1dac0e4a07c3c27f55"></a>

```c
#define IIS2ICLX_DT_FS_3G 1
```

相关声明：[IIS2ICLX_DT_FS_3G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga3d96639b08dc2d1dac0e4a07c3c27f55)。

量程（range）：±3 g。

<a id="r_ga30d90393414465eb9ee5356cecc491a1"></a>

```c
#define IIS2ICLX_DT_FS_1G 2
```

相关声明：[IIS2ICLX_DT_FS_1G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga30d90393414465eb9ee5356cecc491a1)。

量程（range）：±1 g。

<a id="r_gae5be8696d32f8c3774e6a9cd8212c66c"></a>

```c
#define IIS2ICLX_DT_FS_2G 3
```

相关声明：[IIS2ICLX_DT_FS_2G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gae5be8696d32f8c3774e6a9cd8212c66c)。

量程（range）：±2 g。

<a id="define-members-1"></a>

### 加速度计输出数据率（Accelerometer output data rate）

设备树 `odr` 属性的取值。

<a id="r_gaa2856b0a48b1a1396b31d40226f8f257"></a>

```c
#define IIS2ICLX_DT_ODR_OFF 0x0
```

相关声明：[IIS2ICLX_DT_ODR_OFF](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gaa2856b0a48b1a1396b31d40226f8f257)。

掉电（Power-down）。

<a id="r_ga8a223914a9e619b7a229e81dfc6931a3"></a>

```c
#define IIS2ICLX_DT_ODR_12Hz5 0x1
```

相关声明：[IIS2ICLX_DT_ODR_12Hz5](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga8a223914a9e619b7a229e81dfc6931a3)。

频率：12.5 Hz。

<a id="r_ga80341116af73bd318edcfc1fbdc3ef3d"></a>

```c
#define IIS2ICLX_DT_ODR_26H 0x2
```

相关声明：[IIS2ICLX_DT_ODR_26H](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga80341116af73bd318edcfc1fbdc3ef3d)。

频率：26 Hz。

<a id="r_ga0dae0aaf2c7bc79f004aa3427750a3d2"></a>

```c
#define IIS2ICLX_DT_ODR_52Hz 0x3
```

相关声明：[IIS2ICLX_DT_ODR_52Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga0dae0aaf2c7bc79f004aa3427750a3d2)。

频率：52 Hz。

<a id="r_gacbde936ff668bf3e32f6b9f8a36d7f05"></a>

```c
#define IIS2ICLX_DT_ODR_104Hz 0x4
```

相关声明：[IIS2ICLX_DT_ODR_104Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gacbde936ff668bf3e32f6b9f8a36d7f05)。

频率：104 Hz。

<a id="r_ga49da4463f1cd8a26867b126543a05900"></a>

```c
#define IIS2ICLX_DT_ODR_208Hz 0x5
```

相关声明：[IIS2ICLX_DT_ODR_208Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga49da4463f1cd8a26867b126543a05900)。

频率：208 Hz。

<a id="r_ga81441c39564b83b2ad6262f616b4a108"></a>

```c
#define IIS2ICLX_DT_ODR_416Hz 0x6
```

相关声明：[IIS2ICLX_DT_ODR_416Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga81441c39564b83b2ad6262f616b4a108)。

频率：416 Hz。

<a id="r_gacc53fe7776bcbab828e619d0081bcdf6"></a>

```c
#define IIS2ICLX_DT_ODR_833Hz 0x7
```

相关声明：[IIS2ICLX_DT_ODR_833Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gacc53fe7776bcbab828e619d0081bcdf6)。

频率：833 Hz。


## 26.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P346_iis2iclx.h_源码浏览.md)
- [IIS2ICLX_DT_FS_500mG](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga95903c983d457bc48d2a49efb7f2846c)
- [IIS2ICLX_DT_FS_3G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga3d96639b08dc2d1dac0e4a07c3c27f55)
- [IIS2ICLX_DT_FS_1G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga30d90393414465eb9ee5356cecc491a1)
- [IIS2ICLX_DT_FS_2G](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gae5be8696d32f8c3774e6a9cd8212c66c)
- [IIS2ICLX_DT_ODR_OFF](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gaa2856b0a48b1a1396b31d40226f8f257)
- [IIS2ICLX_DT_ODR_12Hz5](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga8a223914a9e619b7a229e81dfc6931a3)
- [IIS2ICLX_DT_ODR_26H](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga80341116af73bd318edcfc1fbdc3ef3d)
- [IIS2ICLX_DT_ODR_52Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga0dae0aaf2c7bc79f004aa3427750a3d2)
- [IIS2ICLX_DT_ODR_104Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gacbde936ff668bf3e32f6b9f8a36d7f05)
- [IIS2ICLX_DT_ODR_208Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga49da4463f1cd8a26867b126543a05900)
- [IIS2ICLX_DT_ODR_416Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#ga81441c39564b83b2ad6262f616b4a108)
- [IIS2ICLX_DT_ODR_833Hz](../api_network_time_topic_reference/P015_IIS2ICLX API主题.md#gacc53fe7776bcbab828e619d0081bcdf6)

<a id="header-details"></a>

---

[上一章](P025_zephyr__bluetooth__classic__hid_device.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__dt-bindings__clock__imx_ccm_rev2.h_文件参考.md)
