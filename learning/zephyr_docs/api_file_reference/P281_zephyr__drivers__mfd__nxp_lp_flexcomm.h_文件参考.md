---
id: learning.zephyr-docs.api-file-reference.page-281
title: zephyr__drivers__mfd__nxp_lp_flexcomm.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp__lp__flexcomm_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第281章\_zephyr\_\_drivers\_\_mfd\_\_nxp\_lp\_flexcomm.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp__lp__flexcomm_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include "fsl_lpflexcomm.h"
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 281.1\_类型定义（Typedefs）

<a id="r_af38501b5aa1350ebc2c03be9b6623353"></a>

```c
typedef void(* child_isr_t) (const struct device *dev)
```

相关声明：[child_isr_t](#af38501b5aa1350ebc2c03be9b6623353)、[device](../device_reference/P002_设备对象结构.md)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 281.2\_函数（Functions）

<a id="r_a259055f21461b4dead75cdec3243719e"></a>

```c
void nxp_lp_flexcomm_setirqhandler (const struct device *dev, const struct device *child_dev, LP_FLEXCOMM_PERIPH_T periph, child_isr_t handler)
```

相关声明：[nxp_lp_flexcomm_setirqhandler](#a259055f21461b4dead75cdec3243719e)、[device](../device_reference/P002_设备对象结构.md)、[device](../device_reference/P002_设备对象结构.md)、[child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)、[child_isr_t](#af38501b5aa1350ebc2c03be9b6623353)。

## 281.3\_详细说明（Detailed Documentation）

<a id="af38501b5aa1350ebc2c03be9b6623353"></a>

### `child_isr_t`

```c
typedef void(* child_isr_t) (const struct device *dev)
```

<a id="a259055f21461b4dead75cdec3243719e"></a>

### `nxp_lp_flexcomm_setirqhandler()`

```c
void nxp_lp_flexcomm_setirqhandler ( const struct device * dev, const struct device * child_dev, LP_FLEXCOMM_PERIPH_T periph, child_isr_t handler )
```


## 281.4\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P621_nxp_lp_flexcomm.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [child_dev](https://docs.zephyrproject.org/latest/doxygen/html/group__mfd__interface__adp5360.html#gae4d56fd30130dc4f332ecf43465a1558)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P280_zephyr__dt-bindings__ethernet__nxp_enet.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P282_zephyr__dt-bindings__power__nxp_rw_pmu.h_文件参考.md)
