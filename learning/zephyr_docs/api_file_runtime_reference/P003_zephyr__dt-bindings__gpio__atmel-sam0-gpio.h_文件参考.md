---
id: learning.zephyr-docs.api-file-runtime-reference.page-3
title: zephyr__dt-bindings__gpio__atmel-sam0-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/atmel-sam0-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_dt-bindings\_\_gpio\_\_atmel-sam0-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/atmel-sam0-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.1\_宏定义（Macros）

<a id="r_a3aef3839686a04a080b1f2243c5feba3"></a>

```c
#define SAM0_GPIO_DEBOUNCE (1U << 8)
```

相关声明：[SAM0_GPIO_DEBOUNCE](#a3aef3839686a04a080b1f2243c5feba3)。

启用 GPIO 引脚去抖（Debounce）。

<a id="r_ac778f1fbb4497f3faaf3780b7a5d74ad"></a>

```c
#define SAM0_GPIO_DRIVE_STRONG (1U << 9)
```

相关声明：[SAM0_GPIO_DRIVE_STRONG](#ac778f1fbb4497f3faaf3780b7a5d74ad)。

启用更强的输出驱动能力（Stronger Output Drive，`PORT PINCFG.DRVSTR`）。

## 3.2\_详细说明（Detailed Documentation）

<a id="a3aef3839686a04a080b1f2243c5feba3"></a>

### `SAM0_GPIO_DEBOUNCE`

```c
#define SAM0_GPIO_DEBOUNCE (1U << 8)
```

启用 GPIO 引脚去抖（Debounce）。

去抖标志（Debounce Flag）是 Zephyr 对 Linux GPIO 绑定所规定的标准 GPIO 标志的扩展。它仅适用于 Atmel SAM0 片上系统（SoCs）。

<a id="ac778f1fbb4497f3faaf3780b7a5d74ad"></a>

### `SAM0_GPIO_DRIVE_STRONG`

```c
#define SAM0_GPIO_DRIVE_STRONG (1U << 9)
```

启用更强的输出驱动能力（Stronger Output Drive，`PORT PINCFG.DRVSTR`）。

提高引脚的额定输出电流（Rated Output Current）；例如，在 SAM D5x/E5x 上，当 `VDD >= 3.0 V` 时从 2 mA 提高到 8 mA。仅对配置为输出（Outputs）的引脚有意义。仅适用于 Atmel SAM0 片上系统（SoCs）。


## 3.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P044_atmel-sam0-gpio.h_源码浏览.md)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P002_zephyr__drivers__video__arducam_mega.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__mesh__blob.h_文件参考.md)
