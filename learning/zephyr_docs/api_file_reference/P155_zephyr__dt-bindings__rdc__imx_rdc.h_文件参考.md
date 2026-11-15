---
id: learning.zephyr-docs.api-file-reference.page-155
title: zephyr__dt-bindings__rdc__imx_rdc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/imx__rdc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第155章\_zephyr\_\_dt-bindings\_\_rdc\_\_imx\_rdc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/imx__rdc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 155.1\_宏定义（Macros）

<a id="r_aac94244543640603434faa2862eb1eef"></a>

```c
#define A7_DOMAIN_ID 0
```

相关声明：[A7_DOMAIN_ID](#aac94244543640603434faa2862eb1eef)。

<a id="r_a2f961de9f7c100cf1ef6aa65cf40cd4f"></a>

```c
#define A9_DOMAIN_ID 0
```

相关声明：[A9_DOMAIN_ID](#a2f961de9f7c100cf1ef6aa65cf40cd4f)。

<a id="r_ad150e5ccb613174d8aadea285fd99a03"></a>

```c
#define A53_DOMAIN_ID 0
```

相关声明：[A53_DOMAIN_ID](#ad150e5ccb613174d8aadea285fd99a03)。

<a id="r_adf4bff1dbb4418d4c9aa2ecb5d8e129a"></a>

```c
#define M4_DOMAIN_ID 1
```

相关声明：[M4_DOMAIN_ID](#adf4bff1dbb4418d4c9aa2ecb5d8e129a)。

<a id="r_a926358589743b689f3b9fc11a06c9f52"></a>

```c
#define M7_DOMAIN_ID 1
```

相关声明：[M7_DOMAIN_ID](#a926358589743b689f3b9fc11a06c9f52)。

<a id="r_aacbb82ed8695c00e9bfcb0458495c17d"></a>

```c
#define RDC_DOMAIN_PERM_NONE (0x0)
```

相关声明：[RDC_DOMAIN_PERM_NONE](#aacbb82ed8695c00e9bfcb0458495c17d)。

<a id="r_a29b98390e0431ebd6c92e227c5fda530"></a>

```c
#define RDC_DOMAIN_PERM_W (0x1)
```

相关声明：[RDC_DOMAIN_PERM_W](#a29b98390e0431ebd6c92e227c5fda530)。

<a id="r_a95d915525ff5b3873462f00f2f64dedc"></a>

```c
#define RDC_DOMAIN_PERM_R (0x2)
```

相关声明：[RDC_DOMAIN_PERM_R](#a95d915525ff5b3873462f00f2f64dedc)。

<a id="r_ad50d355ba8404bbd872a0d6a8ea23f9d"></a>

```c
#define RDC_DOMAIN_PERM_RW (RDC_DOMAIN_PERM_W|RDC_DOMAIN_PERM_R)
```

相关声明：[RDC_DOMAIN_PERM_RW](#ad50d355ba8404bbd872a0d6a8ea23f9d)、[RDC_DOMAIN_PERM_W](#a29b98390e0431ebd6c92e227c5fda530)、[RDC_DOMAIN_PERM_R](#a95d915525ff5b3873462f00f2f64dedc)。

<a id="r_a6e2ca7030bfeb01a10d3b66e37f06a03"></a>

```c
#define RDC_DOMAIN_PERM(domain, perm)
```

相关声明：[RDC_DOMAIN_PERM](#a6e2ca7030bfeb01a10d3b66e37f06a03)。

<a id="r_acdbb0f6700bd61336079152f3e704896"></a>

```c
#define RDC_DT_VAL(nodelabel)
```

相关声明：[RDC_DT_VAL](#acdbb0f6700bd61336079152f3e704896)。

## 155.2\_详细说明（Detailed Documentation）

<a id="ad150e5ccb613174d8aadea285fd99a03"></a>

### `A53_DOMAIN_ID`

```c
#define A53_DOMAIN_ID 0
```

<a id="aac94244543640603434faa2862eb1eef"></a>

### `A7_DOMAIN_ID`

```c
#define A7_DOMAIN_ID 0
```

<a id="a2f961de9f7c100cf1ef6aa65cf40cd4f"></a>

### `A9_DOMAIN_ID`

```c
#define A9_DOMAIN_ID 0
```

<a id="adf4bff1dbb4418d4c9aa2ecb5d8e129a"></a>

### `M4_DOMAIN_ID`

```c
#define M4_DOMAIN_ID 1
```

<a id="a926358589743b689f3b9fc11a06c9f52"></a>

### `M7_DOMAIN_ID`

```c
#define M7_DOMAIN_ID 1
```

<a id="a6e2ca7030bfeb01a10d3b66e37f06a03"></a>

### `RDC_DOMAIN_PERM`

```c
#define RDC_DOMAIN_PERM ( domain, perm )
```

展开值（Value）：

```c
(perm << (domain * 2))
```

<a id="aacbb82ed8695c00e9bfcb0458495c17d"></a>

### `RDC_DOMAIN_PERM_NONE`

```c
#define RDC_DOMAIN_PERM_NONE (0x0)
```

<a id="a95d915525ff5b3873462f00f2f64dedc"></a>

### `RDC_DOMAIN_PERM_R`

```c
#define RDC_DOMAIN_PERM_R (0x2)
```

<a id="ad50d355ba8404bbd872a0d6a8ea23f9d"></a>

### `RDC_DOMAIN_PERM_RW`

```c
#define RDC_DOMAIN_PERM_RW (RDC_DOMAIN_PERM_W|RDC_DOMAIN_PERM_R)
```

<a id="a29b98390e0431ebd6c92e227c5fda530"></a>

### `RDC_DOMAIN_PERM_W`

```c
#define RDC_DOMAIN_PERM_W (0x1)
```

<a id="acdbb0f6700bd61336079152f3e704896"></a>

### `RDC_DT_VAL`

```c
#define RDC_DT_VAL ( nodelabel)
```

展开值（Value）：

```c
DT_PROP(DT_NODELABEL(nodelabel), rdc)
```


## 155.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P356_imx_rdc.h_源码浏览.md)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_NODELABEL](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-id_html_gab7d23294a6bf7fd44a98b48ec47d8a79"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>

---

[上一章](P154_zephyr__dt-bindings__power__imx95_power.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P156_zephyr__dt-bindings__power__imx_scu_rsrc.h_文件参考.md)
