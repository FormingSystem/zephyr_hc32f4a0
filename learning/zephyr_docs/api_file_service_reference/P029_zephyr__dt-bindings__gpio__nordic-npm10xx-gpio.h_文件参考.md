---
id: learning.zephyr-docs.api-file-service-reference.page-29
title: zephyr__dt-bindings__gpio__nordic-npm10xx-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm10xx-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第29章\_zephyr\_\_dt-bindings\_\_gpio\_\_nordic-npm10xx-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm10xx-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

nPM10xx专用GPIO标志（Flags）。

查看此文件的源码。

<a id="details"></a>

nPM10xx专用GPIO标志（Flags）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 29.1\_宏定义（Macros）

<a id="define-members-0"></a>

### nPM10xx GPIO 驱动强度标志（Drive Strength Flags）

<a id="r_gaa453cd596eca9e14d222457506d805d5"></a>

```c
#define NPM10XX_GPIO_DRIVE_NORMAL (0U << 8U)
```

相关声明：[NPM10XX_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gaa453cd596eca9e14d222457506d805d5)。

普通驱动（Normal Drive），电流为 2 mA。

<a id="r_ga83f0e8761270947b758546c259206f0d"></a>

```c
#define NPM10XX_GPIO_DRIVE_HIGH (1U << 8U)
```

相关声明：[NPM10XX_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga83f0e8761270947b758546c259206f0d)。

高驱动（High Drive），电流为 4 mA。

<a id="define-members-1"></a>

### nPM10xx GPIO 去抖标志（Debounce Flags）

<a id="r_ga52154f1315bad8d24afbacb0d3924bc9"></a>

```c
#define NPM10XX_GPIO_DEBOUNCE_OFF (0U << 9U)
```

相关声明：[NPM10XX_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga52154f1315bad8d24afbacb0d3924bc9)。

关闭去抖（Debounce Off）。

<a id="r_gae76b53ec23c6515a7761c517fb35fe3a"></a>

```c
#define NPM10XX_GPIO_DEBOUNCE_ON (1U << 9U)
```

相关声明：[NPM10XX_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gae76b53ec23c6515a7761c517fb35fe3a)。

开启去抖（Debounce On）。


## 29.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P581_nordic-npm10xx-gpio.h_源码浏览.md)
- [NPM10XX_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gaa453cd596eca9e14d222457506d805d5)
- [NPM10XX_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga83f0e8761270947b758546c259206f0d)
- [NPM10XX_GPIO_DEBOUNCE_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#ga52154f1315bad8d24afbacb0d3924bc9)
- [NPM10XX_GPIO_DEBOUNCE_ON](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm10xx.html#gae76b53ec23c6515a7761c517fb35fe3a)

<a id="header-details"></a>

---

[上一章](P028_zephyr__net__prometheus__counter.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P030_zephyr__dt-bindings__gpio__nordic-npm2100-gpio.h_文件参考.md)
