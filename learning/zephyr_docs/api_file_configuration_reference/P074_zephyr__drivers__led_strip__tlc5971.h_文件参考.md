---
id: learning.zephyr-docs.api-file-configuration-reference.page-74
title: zephyr__drivers__led_strip__tlc5971.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/tlc5971_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第74章\_zephyr\_\_drivers\_\_led\_strip\_\_tlc5971.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/tlc5971_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TLC5971 LED灯带控制器（LED Strip Controller）扩展LED灯带API的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/led_strip.h>
```

查看此文件的源码。

TLC5971 LED灯带控制器（LED Strip Controller）扩展LED灯带API的头文件。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 74.1\_宏定义（Macros）

<a id="r_gaee75c4832a72869ca6e2960c726ed707"></a>

```c
#define TLC5971_GLOBAL_BRIGHTNESS_CONTROL_MAX 127
```

相关声明：[TLC5971_GLOBAL_BRIGHTNESS_CONTROL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__tlc5971__interface.html#gaee75c4832a72869ca6e2960c726ed707)。

全局亮度控制（Global Brightness Control）的最大值，即 100% 亮度。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 74.2\_函数（Functions）

<a id="r_gacc0ab1f6ae658de98d043e49291abea4"></a>

```c
int tlc5971_set_global_brightness (const struct device *dev, struct led_rgb pixel)
```

相关声明：[tlc5971_set_global_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__tlc5971__interface.html#gacc0ab1f6ae658de98d043e49291abea4)、[device](../device_reference/P002_设备对象结构.md)、[led_rgb](../hardware/P209_LED灯带颜色结构.md)。

设置 TLC5971 灯带（Strip）的全局亮度控制级别（Brightness Control，BC）。


## 74.3\_原页交叉引用（Cross References）

- [zephyr/drivers/led_strip.h](../api_source_runtime_reference/P037_led_strip.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P869_tlc5971.h_源码浏览.md)
- [TLC5971_GLOBAL_BRIGHTNESS_CONTROL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__tlc5971__interface.html#gaee75c4832a72869ca6e2960c726ed707)
- [tlc5971_set_global_brightness](https://docs.zephyrproject.org/latest/doxygen/html/group__tlc5971__interface.html#gacc0ab1f6ae658de98d043e49291abea4)
- [device](../device_reference/P002_设备对象结构.md)
- [led_rgb](../hardware/P209_LED灯带颜色结构.md)

<a id="header-details"></a>

---

[上一章](P073_zephyr__debug__symtab.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P075_zephyr__drivers__haptics__tm6605.h_文件参考.md)
