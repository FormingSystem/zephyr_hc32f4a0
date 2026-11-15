---
id: learning.zephyr-docs.api-file-interface-reference.page-42
title: zephyr__dt-bindings__gpio__pca-series-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pca-series-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第42章\_zephyr\_\_dt-bindings\_\_gpio\_\_pca-series-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pca-series-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 42.1\_宏定义（Macros）

<a id="define-members-0"></a>

### PCA 系列 GPIO 驱动强度标志（drive strength flags）

PCA 系列 GPIO 扩展器（GPIO expander）专用标志。

驱动标志（Driver Flags）编码在 `gpio_dt_flags_t` 的高 8 位，具体如下：

用于配置输出驱动强度（output drive strength）的宏，与 `gpio_pca_series.c` 中的 `enum gpio_pca_series_drive_strength` 对应。`PCA_SERIES_GPIO_DRIVE_STRENGTH_X1` 为最低强度，`PCA_SERIES_GPIO_DRIVE_STRENGTH_X4` 为最高强度。复位后的默认驱动强度为 `PCA_SERIES_GPIO_DRIVE_STRENGTH_X4`。

注意：仅适用于具备 `PCA_HAS_LATCH` 能力的器件型号。

<a id="r_ad6313ca79dab706277f8d4dc519a47ea"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X1
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_X1](#ad6313ca79dab706277f8d4dc519a47ea)。

中断（Interrupt）路由到唤醒单元控制器（WKPU Controller）。

<a id="r_ad3b7b671db0264ff3f24e33954ee1387"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X2
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_X2](#ad3b7b671db0264ff3f24e33954ee1387)。

<a id="r_ada33ae2517be5b5153ee634e9190092a"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X3
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_X3](#ada33ae2517be5b5153ee634e9190092a)。

<a id="r_acad6d3f1edd215a42007dffd40da1920"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X4
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_X4](#acad6d3f1edd215a42007dffd40da1920)。

<a id="r_ac9cf8e664d47a19f82ab0ddb27c81e63"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_DEFAULT PCA_SERIES_GPIO_DRIVE_STRENGTH_X4
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_DEFAULT](#ac9cf8e664d47a19f82ab0ddb27c81e63)、[PCA_SERIES_GPIO_DRIVE_STRENGTH_X4](#acad6d3f1edd215a42007dffd40da1920)。

设备复位时的默认驱动强度（default drive strength）。

<a id="r_aa043b39fc8e1ec1c8ff5f79771a52a76"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG(x)
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG](#aa043b39fc8e1ec1c8ff5f79771a52a76)。

<a id="r_af66bb54ba2badcfafe1cefab6c75c828"></a>

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE(x)
```

相关声明：[PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE](#af66bb54ba2badcfafe1cefab6c75c828)。

## 42.2\_详细说明（Detailed Documentation）

<a id="aa043b39fc8e1ec1c8ff5f79771a52a76"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG ( x)
```

展开值（Value）：

```c
((x & PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG_MASK) >> \
PCA_SERIES_GPIO_DRIVE_STRENGTH_CONFIG_POS)
```

<a id="ac9cf8e664d47a19f82ab0ddb27c81e63"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_DEFAULT`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_DEFAULT PCA_SERIES_GPIO_DRIVE_STRENGTH_X4
```

设备复位时的默认驱动强度（default drive strength）。

<a id="af66bb54ba2badcfafe1cefab6c75c828"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE ( x)
```

展开值（Value）：

```c
((x & PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_MASK) >> \
PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_POS)
```

<a id="ad6313ca79dab706277f8d4dc519a47ea"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_X1`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X1
```

展开值（Value）：

```c
((0x0U << PCA_SERIES_GPIO_DRIVE_STRENGTH_POS) | \
 (0x1U << PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_POS))
```

中断（Interrupt）路由到唤醒单元控制器（WKPU Controller）。

<a id="ad3b7b671db0264ff3f24e33954ee1387"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_X2`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X2
```

展开值（Value）：

```c
((0x1U << PCA_SERIES_GPIO_DRIVE_STRENGTH_POS) | \
 (0x1U << PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_POS))
```

<a id="ada33ae2517be5b5153ee634e9190092a"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_X3`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X3
```

展开值（Value）：

```c
((0x2U << PCA_SERIES_GPIO_DRIVE_STRENGTH_POS) | \
 (0x1U << PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_POS))
```

<a id="acad6d3f1edd215a42007dffd40da1920"></a>

### `PCA_SERIES_GPIO_DRIVE_STRENGTH_X4`

```c
#define PCA_SERIES_GPIO_DRIVE_STRENGTH_X4
```

展开值（Value）：

```c
((0x3U << PCA_SERIES_GPIO_DRIVE_STRENGTH_POS) | \
 (0x1U << PCA_SERIES_GPIO_DRIVE_STRENGTH_ENABLE_POS))
```


## 42.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P646_pca-series-gpio.h_源码浏览.md)
- [gpio_dt_flags_t](../hardware/P266_GPIO公共接口.md#gad435719dccdc37c05852960a7218fbd2)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P041_zephyr__dt-bindings__clock__nxp_mc_cgm.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P043_zephyr__drivers__pinctrl__pinctrl_rp1_common.h_文件参考.md)
