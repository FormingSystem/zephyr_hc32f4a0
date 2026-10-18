---
id: learning.zephyr-docs.api-file-management-reference.page-46
title: zephyr__dt-bindings__gpio__ti-cc13xx-cc26xx-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-cc13xx-cc26xx-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_zephyr\_\_dt-bindings\_\_gpio\_\_ti-cc13xx-cc26xx-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti-cc13xx-cc26xx-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 46.1\_宏定义（Macros）

<a id="r_a7fd876bbceee04263d760146333d3b56"></a>

```c
#define CC13XX_CC26XX_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[CC13XX_CC26XX_GPIO_DEBOUNCE](#a7fd876bbceee04263d760146333d3b56)。

启用 GPIO 引脚去抖（Debounce）。

<a id="define-members-0"></a>

### GPIO 驱动强度标志（drive strength flags）

驱动强度标志（drive strength flags）是 Zephyr 对 Linux GPIO 绑定所规定标准 GPIO 标志的专用扩展。

仅适用于 Texas Instruments CC13xx/CC26xx 片上系统（SoC）。

该接口支持两种不同的驱动强度（drive strengths）：`DFLT` 为硬件支持的最低驱动强度；`ALT` 为硬件支持的最高驱动强度。

<a id="r_a038b78d724a2344c100e99ef66fa4613"></a>

```c
#define CC13XX_CC26XX_GPIO_DS_DFLT (0x0U << CC13XX_CC26XX_GPIO_DS_POS)
```

相关声明：[CC13XX_CC26XX_GPIO_DS_DFLT](#a038b78d724a2344c100e99ef66fa4613)。

默认驱动强度（default drive strength）。

<a id="r_a287f8063ecbc0672818d7b813b37e855"></a>

```c
#define CC13XX_CC26XX_GPIO_DS_ALT (0x3U << CC13XX_CC26XX_GPIO_DS_POS)
```

相关声明：[CC13XX_CC26XX_GPIO_DS_ALT](#a287f8063ecbc0672818d7b813b37e855)。

替代驱动强度（alternative drive strength）。

## 46.2\_详细说明（Detailed Documentation）

<a id="a7fd876bbceee04263d760146333d3b56"></a>

### `CC13XX_CC26XX_GPIO_DEBOUNCE`

```c
#define CC13XX_CC26XX_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（debounce flag）是 Zephyr 对 Linux GPIO 绑定所规定标准 GPIO 标志的专用扩展。仅适用于 Texas Instruments CC1xx/CC26xx SoC。

<a id="a287f8063ecbc0672818d7b813b37e855"></a>

### `CC13XX_CC26XX_GPIO_DS_ALT`

```c
#define CC13XX_CC26XX_GPIO_DS_ALT (0x3U << CC13XX_CC26XX_GPIO_DS_POS)
```

替代驱动强度（alternative drive strength）。

<a id="a038b78d724a2344c100e99ef66fa4613"></a>

### `CC13XX_CC26XX_GPIO_DS_DFLT`

```c
#define CC13XX_CC26XX_GPIO_DS_DFLT (0x0U << CC13XX_CC26XX_GPIO_DS_POS)
```

默认驱动强度（default drive strength）。


## 46.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P863_ti-cc13xx-cc26xx-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P045_zephyr__drivers__i3c__target_device.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P047_zephyr__dt-bindings__video__video-interfaces.h_文件参考.md)
