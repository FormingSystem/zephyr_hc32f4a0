---
id: learning.zephyr-docs.api-file-service-reference.page-38
title: zephyr__drivers__pinctrl__pinctrl_soc_sam_common.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_drivers\_\_pinctrl\_\_pinctrl\_soc\_sam\_common.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__soc__sam__common_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

引脚控制（Pinctrl）驱动使用的Atmel SAM片上系统（SoC）专用辅助接口。

<a id="details"></a>

```c
#include <zephyr/devicetree.h>
#include <zephyr/types.h>
#include <dt-bindings/pinctrl/atmel_sam_pinctrl.h>
```

查看此文件的源码。

引脚控制（Pinctrl）驱动使用的Atmel SAM片上系统（SoC）专用辅助接口。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.1\_宏定义（Macros）

<a id="r_ac0d76820e58e8d0ef6a65663ccd488d4"></a>

```c
#define SAM_PINCTRL_FLAG_GET(pincfg, pos)
```

相关声明：[SAM_PINCTRL_FLAG_GET](#ac0d76820e58e8d0ef6a65663ccd488d4)。

从 `pinctrl_soc_pin_t` 配置（Configuration）获取标志值（Flag Value）。

<a id="r_a65850f6768e47ce900ab6ae615764570"></a>

```c
#define SAM_PINCTRL_FLAGS_GET(pincfg)
```

相关声明：[SAM_PINCTRL_FLAGS_GET](#a65850f6768e47ce900ab6ae615764570)。

<a id="define-members-0"></a>

<a id="r_a966bab3a458ab5d74319cd296f25f756"></a>

```c
#define SAM_PINCTRL_FLAGS_DEFAULT (0U)
```

相关声明：[SAM_PINCTRL_FLAGS_DEFAULT](#a966bab3a458ab5d74319cd296f25f756)。

引脚标志／属性（Pin Flags / Attributes）。

<a id="r_ae42a8c43d997c40238c0cb3af2855ea8"></a>

```c
#define SAM_PINCTRL_FLAGS_POS (0U)
```

相关声明：[SAM_PINCTRL_FLAGS_POS](#ae42a8c43d997c40238c0cb3af2855ea8)。

<a id="r_a47928c213072d5e26923570e8ef14bd9"></a>

```c
#define SAM_PINCTRL_FLAGS_MASK (0x3F << SAM_PINCTRL_FLAGS_POS)
```

相关声明：[SAM_PINCTRL_FLAGS_MASK](#a47928c213072d5e26923570e8ef14bd9)、[SAM_PINCTRL_FLAGS_POS](#ae42a8c43d997c40238c0cb3af2855ea8)。

<a id="r_aea986207fa829b606d47d4919a1fb515"></a>

```c
#define SAM_PINCTRL_FLAG_MASK (1U)
```

相关声明：[SAM_PINCTRL_FLAG_MASK](#aea986207fa829b606d47d4919a1fb515)。

<a id="r_a60ca2e906d19a30ac9168163301491c0"></a>

```c
#define SAM_PINCTRL_PULLUP_POS (SAM_PINCTRL_FLAGS_POS)
```

相关声明：[SAM_PINCTRL_PULLUP_POS](#a60ca2e906d19a30ac9168163301491c0)、[SAM_PINCTRL_FLAGS_POS](#ae42a8c43d997c40238c0cb3af2855ea8)。

<a id="r_a72052ca63d8cac12fdb6314dc9db7f12"></a>

```c
#define SAM_PINCTRL_PULLUP (1U << SAM_PINCTRL_PULLUP_POS)
```

相关声明：[SAM_PINCTRL_PULLUP](#a72052ca63d8cac12fdb6314dc9db7f12)、[SAM_PINCTRL_PULLUP_POS](#a60ca2e906d19a30ac9168163301491c0)。

<a id="r_a3d1ff6f736aed51318196736067db4c9"></a>

```c
#define SAM_PINCTRL_PULLDOWN_POS (SAM_PINCTRL_PULLUP_POS + 1U)
```

相关声明：[SAM_PINCTRL_PULLDOWN_POS](#a3d1ff6f736aed51318196736067db4c9)、[SAM_PINCTRL_PULLUP_POS](#a60ca2e906d19a30ac9168163301491c0)。

<a id="r_ac39a6835941c340ee1bb0fb71bb34c9c"></a>

```c
#define SAM_PINCTRL_PULLDOWN (1U << SAM_PINCTRL_PULLDOWN_POS)
```

相关声明：[SAM_PINCTRL_PULLDOWN](#ac39a6835941c340ee1bb0fb71bb34c9c)、[SAM_PINCTRL_PULLDOWN_POS](#a3d1ff6f736aed51318196736067db4c9)。

<a id="r_af23ac8ff95ef934f2d8dd6f3727ef5fc"></a>

```c
#define SAM_PINCTRL_OPENDRAIN_POS (SAM_PINCTRL_PULLDOWN_POS + 1U)
```

相关声明：[SAM_PINCTRL_OPENDRAIN_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)、[SAM_PINCTRL_PULLDOWN_POS](#a3d1ff6f736aed51318196736067db4c9)。

<a id="r_a41a3c21a35fbe8baaea766ffeb56d6ea"></a>

```c
#define SAM_PINCTRL_OPENDRAIN (1U << SAM_PINCTRL_OPENDRAIN_POS)
```

相关声明：[SAM_PINCTRL_OPENDRAIN](#a41a3c21a35fbe8baaea766ffeb56d6ea)、[SAM_PINCTRL_OPENDRAIN_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)。

<a id="r_a32af1969f02a3f5ac5c92f19258c6b71"></a>

```c
#define SAM_PINCTRL_INPUTENABLE_POS (SAM_PINCTRL_OPENDRAIN_POS + 1U)
```

相关声明：[SAM_PINCTRL_INPUTENABLE_POS](#a32af1969f02a3f5ac5c92f19258c6b71)、[SAM_PINCTRL_OPENDRAIN_POS](#af23ac8ff95ef934f2d8dd6f3727ef5fc)。

<a id="r_a354e8d543c70ab5affdffeda7c0e84d9"></a>

```c
#define SAM_PINCTRL_INPUTENABLE (1U << SAM_PINCTRL_INPUTENABLE_POS)
```

相关声明：[SAM_PINCTRL_INPUTENABLE](#a354e8d543c70ab5affdffeda7c0e84d9)、[SAM_PINCTRL_INPUTENABLE_POS](#a32af1969f02a3f5ac5c92f19258c6b71)。

<a id="r_a078ce2bd47b20adc4d31756373a343a1"></a>

```c
#define SAM_PINCTRL_OUTPUTENABLE_POS (SAM_PINCTRL_INPUTENABLE_POS + 1U)
```

相关声明：[SAM_PINCTRL_OUTPUTENABLE_POS](#a078ce2bd47b20adc4d31756373a343a1)、[SAM_PINCTRL_INPUTENABLE_POS](#a32af1969f02a3f5ac5c92f19258c6b71)。

<a id="r_a3d0d020327f4ce53c3e8a705551e01bf"></a>

```c
#define SAM_PINCTRL_OUTPUTENABLE (1U << SAM_PINCTRL_OUTPUTENABLE_POS)
```

相关声明：[SAM_PINCTRL_OUTPUTENABLE](#a3d0d020327f4ce53c3e8a705551e01bf)、[SAM_PINCTRL_OUTPUTENABLE_POS](#a078ce2bd47b20adc4d31756373a343a1)。

<a id="r_a984860553e4a824427b86ab627e9e48a"></a>

```c
#define SAM_PINCTRL_DRIVESTRENGTH_POS (SAM_PINCTRL_OUTPUTENABLE_POS + 1U)
```

相关声明：[SAM_PINCTRL_DRIVESTRENGTH_POS](#a984860553e4a824427b86ab627e9e48a)、[SAM_PINCTRL_OUTPUTENABLE_POS](#a078ce2bd47b20adc4d31756373a343a1)。

<a id="r_a510309503bbe70010329b11748f94b23"></a>

```c
#define SAM_PINCTRL_DRIVESTRENGTH (1U << SAM_PINCTRL_DRIVESTRENGTH_POS)
```

相关声明：[SAM_PINCTRL_DRIVESTRENGTH](#a510309503bbe70010329b11748f94b23)、[SAM_PINCTRL_DRIVESTRENGTH_POS](#a984860553e4a824427b86ab627e9e48a)。

## 38.2\_详细说明（Detailed Documentation）

<a id="a510309503bbe70010329b11748f94b23"></a>

### `SAM_PINCTRL_DRIVESTRENGTH`

```c
#define SAM_PINCTRL_DRIVESTRENGTH (1U << SAM_PINCTRL_DRIVESTRENGTH_POS)
```

<a id="a984860553e4a824427b86ab627e9e48a"></a>

### `SAM_PINCTRL_DRIVESTRENGTH_POS`

```c
#define SAM_PINCTRL_DRIVESTRENGTH_POS (SAM_PINCTRL_OUTPUTENABLE_POS + 1U)
```

<a id="ac0d76820e58e8d0ef6a65663ccd488d4"></a>

### `SAM_PINCTRL_FLAG_GET`

```c
#define SAM_PINCTRL_FLAG_GET ( pincfg, pos )
```

展开值（Value）：

```c
(((pincfg) >> pos) & SAM_PINCTRL_FLAG_MASK)
```

从 `pinctrl_soc_pin_t` 配置（Configuration）获取标志值（Flag Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pincfg` | `pinctrl_soc_pin_t` 位域值（Bit Field Value）。 |
| `pos` | 属性／标志的位位置（Attribute / Flags Bit Position），即 `SAM_PINFLAGS`。 |

<a id="aea986207fa829b606d47d4919a1fb515"></a>

### `SAM_PINCTRL_FLAG_MASK`

```c
#define SAM_PINCTRL_FLAG_MASK (1U)
```

<a id="a966bab3a458ab5d74319cd296f25f756"></a>

### `SAM_PINCTRL_FLAGS_DEFAULT`

```c
#define SAM_PINCTRL_FLAGS_DEFAULT (0U)
```

引脚标志／属性（Pin Flags / Attributes）。

<a id="a65850f6768e47ce900ab6ae615764570"></a>

### `SAM_PINCTRL_FLAGS_GET`

```c
#define SAM_PINCTRL_FLAGS_GET ( pincfg)
```

展开值（Value）：

```c
(((pincfg) >> SAM_PINCTRL_FLAGS_POS) & SAM_PINCTRL_FLAGS_MASK)
```

<a id="a47928c213072d5e26923570e8ef14bd9"></a>

### `SAM_PINCTRL_FLAGS_MASK`

```c
#define SAM_PINCTRL_FLAGS_MASK (0x3F << SAM_PINCTRL_FLAGS_POS)
```

<a id="ae42a8c43d997c40238c0cb3af2855ea8"></a>

### `SAM_PINCTRL_FLAGS_POS`

```c
#define SAM_PINCTRL_FLAGS_POS (0U)
```

<a id="a354e8d543c70ab5affdffeda7c0e84d9"></a>

### `SAM_PINCTRL_INPUTENABLE`

```c
#define SAM_PINCTRL_INPUTENABLE (1U << SAM_PINCTRL_INPUTENABLE_POS)
```

<a id="a32af1969f02a3f5ac5c92f19258c6b71"></a>

### `SAM_PINCTRL_INPUTENABLE_POS`

```c
#define SAM_PINCTRL_INPUTENABLE_POS (SAM_PINCTRL_OPENDRAIN_POS + 1U)
```

<a id="a41a3c21a35fbe8baaea766ffeb56d6ea"></a>

### `SAM_PINCTRL_OPENDRAIN`

```c
#define SAM_PINCTRL_OPENDRAIN (1U << SAM_PINCTRL_OPENDRAIN_POS)
```

<a id="af23ac8ff95ef934f2d8dd6f3727ef5fc"></a>

### `SAM_PINCTRL_OPENDRAIN_POS`

```c
#define SAM_PINCTRL_OPENDRAIN_POS (SAM_PINCTRL_PULLDOWN_POS + 1U)
```

<a id="a3d0d020327f4ce53c3e8a705551e01bf"></a>

### `SAM_PINCTRL_OUTPUTENABLE`

```c
#define SAM_PINCTRL_OUTPUTENABLE (1U << SAM_PINCTRL_OUTPUTENABLE_POS)
```

<a id="a078ce2bd47b20adc4d31756373a343a1"></a>

### `SAM_PINCTRL_OUTPUTENABLE_POS`

```c
#define SAM_PINCTRL_OUTPUTENABLE_POS (SAM_PINCTRL_INPUTENABLE_POS + 1U)
```

<a id="ac39a6835941c340ee1bb0fb71bb34c9c"></a>

### `SAM_PINCTRL_PULLDOWN`

```c
#define SAM_PINCTRL_PULLDOWN (1U << SAM_PINCTRL_PULLDOWN_POS)
```

<a id="a3d1ff6f736aed51318196736067db4c9"></a>

### `SAM_PINCTRL_PULLDOWN_POS`

```c
#define SAM_PINCTRL_PULLDOWN_POS (SAM_PINCTRL_PULLUP_POS + 1U)
```

<a id="a72052ca63d8cac12fdb6314dc9db7f12"></a>

### `SAM_PINCTRL_PULLUP`

```c
#define SAM_PINCTRL_PULLUP (1U << SAM_PINCTRL_PULLUP_POS)
```

<a id="a60ca2e906d19a30ac9168163301491c0"></a>

### `SAM_PINCTRL_PULLUP_POS`

```c
#define SAM_PINCTRL_PULLUP_POS (SAM_PINCTRL_FLAGS_POS)
```


## 38.3\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P659_pinctrl_soc_sam_common.h_源码浏览.md)
- [pinctrl_soc_pin_t](https://docs.zephyrproject.org/latest/doxygen/html/pinctrl__rcar__common_8h.html#a022eeb1c811e7ef94d3a7a99cbda0e2d)

<a id="SAM_PINFLAGS"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="apinctrl__soc__sam__common_8h_html_aea986207fa829b606d47d4919a1fb515"></a>
<a id="apinctrl__soc__sam__common_8h_html_a47928c213072d5e26923570e8ef14bd9"></a>
<a id="apinctrl__soc__sam__common_8h_html_ae42a8c43d997c40238c0cb3af2855ea8"></a>

---

[上一章](P037_zephyr__dt-bindings__pinctrl__pinctrl-zynq.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__net__promiscuous.h_文件参考.md)
