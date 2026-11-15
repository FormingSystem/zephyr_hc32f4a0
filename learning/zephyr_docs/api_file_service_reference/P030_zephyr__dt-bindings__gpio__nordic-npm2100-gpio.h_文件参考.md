---
id: learning.zephyr-docs.api-file-service-reference.page-30
title: zephyr__dt-bindings__gpio__nordic-npm2100-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm2100-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_dt-bindings\_\_gpio\_\_nordic-npm2100-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm2100-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 30.1\_宏定义（Macros）

<a id="define-members-0"></a>

### nPM2100 GPIO 驱动强度标志（Drive Strength Flags）。

nPM2100 GPIO 驱动强度标志（Drive Strength Flags）。

<a id="r_gaaba391246c0041ce40cf9a9826cc2dbd"></a>

```c
#define NPM2100_GPIO_DRIVE_NORMAL (0U << 8U)
```

相关声明：[NPM2100_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#gaaba391246c0041ce40cf9a9826cc2dbd)。

普通驱动（Normal Drive）。

<a id="r_ga281cd37a16ba12b56850ea98d9b543d5"></a>

```c
#define NPM2100_GPIO_DRIVE_HIGH (1U << 8U)
```

相关声明：[NPM2100_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga281cd37a16ba12b56850ea98d9b543d5)。

高驱动（High Drive）。

<a id="define-members-1"></a>

### nPM2100 GPIO 去抖标志（Debounce Flags）。

nPM2100 GPIO 去抖标志（Debounce Flags）。

<a id="r_ga79471e04dd5ed29a8a819403ab6d83d0"></a>

```c
#define NPM2100_GPIO_DEBOUNCE_OFF (0U << 9U)
```

相关声明：[NPM2100_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga79471e04dd5ed29a8a819403ab6d83d0)。

普通驱动（Normal Drive）。

<a id="r_ga4b1336ed15dc7ed906d1aa69fddff33d"></a>

```c
#define NPM2100_GPIO_DEBOUNCE_ON (1U << 9U)
```

相关声明：[NPM2100_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga4b1336ed15dc7ed906d1aa69fddff33d)。

高驱动（High Drive）。


## 30.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P583_nordic-npm2100-gpio.h_源码浏览.md)
- [NPM2100_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#gaaba391246c0041ce40cf9a9826cc2dbd)
- [NPM2100_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga281cd37a16ba12b56850ea98d9b543d5)
- [NPM2100_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga79471e04dd5ed29a8a819403ab6d83d0)
- [NPM2100_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm2100.html#ga4b1336ed15dc7ed906d1aa69fddff33d)

---

[上一章](P029_zephyr__dt-bindings__gpio__nordic-npm10xx-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__dt-bindings__gpio__nxp-imx-igpio.h_文件参考.md)
