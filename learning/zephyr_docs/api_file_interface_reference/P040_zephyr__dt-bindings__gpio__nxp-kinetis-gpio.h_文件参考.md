---
id: learning.zephyr-docs.api-file-interface-reference.page-40
title: zephyr__dt-bindings__gpio__nxp-kinetis-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nxp-kinetis-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_zephyr\_\_dt-bindings\_\_gpio\_\_nxp-kinetis-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nxp-kinetis-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 40.1\_宏定义（Macros）

<a id="define-members-0"></a>

### GPIO 驱动强度标志（drive strength flags）

驱动强度标志（drive strength flags）是 Zephyr 对 Linux GPIO 绑定所规定标准 GPIO 标志的专用扩展。

仅适用于 NXP Kinetis 片上系统（SoC）。

该接口支持两种不同的驱动强度（drive strengths）：`DFLT` 为硬件支持的最低驱动强度；`ALT` 为硬件支持的最高驱动强度。

<a id="r_afc2673bf88bc72dda4effbf1d9d0015a"></a>

```c
#define KINETIS_GPIO_DS_DFLT (0x0U << KINETIS_GPIO_DS_POS)
```

相关声明：[KINETIS_GPIO_DS_DFLT](#afc2673bf88bc72dda4effbf1d9d0015a)。

默认驱动强度（default drive strength）。

<a id="r_a1c4baa298474c0cdc731c4a5cf9f0364"></a>

```c
#define KINETIS_GPIO_DS_ALT (0x3U << KINETIS_GPIO_DS_POS)
```

相关声明：[KINETIS_GPIO_DS_ALT](#a1c4baa298474c0cdc731c4a5cf9f0364)。

替代驱动强度（alternative drive strength）。

## 40.2\_详细说明（Detailed Documentation）

<a id="a1c4baa298474c0cdc731c4a5cf9f0364"></a>

### `KINETIS_GPIO_DS_ALT`

```c
#define KINETIS_GPIO_DS_ALT (0x3U << KINETIS_GPIO_DS_POS)
```

替代驱动强度（alternative drive strength）。

<a id="afc2673bf88bc72dda4effbf1d9d0015a"></a>

### `KINETIS_GPIO_DS_DFLT`

```c
#define KINETIS_GPIO_DS_DFLT (0x0U << KINETIS_GPIO_DS_POS)
```

默认驱动强度（default drive strength）。


## 40.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P612_nxp-kinetis-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P039_zephyr__dt-bindings__sensor__npcx_tach.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P041_zephyr__dt-bindings__clock__nxp_mc_cgm.h_文件参考.md)
