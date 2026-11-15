---
id: learning.zephyr-docs.api-file-runtime-reference.page-70
title: zephyr__dt-bindings__interrupt-controller__ti-vim.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ti-vim_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第70章\_zephyr\_\_dt-bindings\_\_interrupt-controller\_\_ti-vim.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ti-vim_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

TI向量中断管理器（VIM）的设备树宏。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
```

查看此文件的源码。

TI向量中断管理器（VIM）的设备树宏。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 70.1\_宏定义（Macros）

<a id="r_ga296e915831223a614a6ea87dbe7735e7"></a>

```c
#define IRQ_TYPE_LEVEL BIT(1)
```

相关声明：[IRQ_TYPE_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#ga296e915831223a614a6ea87dbe7735e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电平触发中断（Level-Triggered Interrupt）。

<a id="r_gaff68b0efbc719bc28f0d56c9ba8607bc"></a>

```c
#define IRQ_TYPE_EDGE BIT(2)
```

相关声明：[IRQ_TYPE_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#gaff68b0efbc719bc28f0d56c9ba8607bc)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

边沿触发中断（Edge-Triggered Interrupt）。

<a id="r_ga2dbeaa0c017cdff0982b381cc96f0a6c"></a>

```c
#define IRQ_DEFAULT_PRIORITY 0xf
```

相关声明：[IRQ_DEFAULT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#ga2dbeaa0c017cdff0982b381cc96f0a6c)。

默认中断优先级（Default Interrupt Priority）。


## 70.2\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P865_ti-vim.h_源码浏览.md)
- [IRQ_TYPE_LEVEL](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#ga296e915831223a614a6ea87dbe7735e7)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [IRQ_TYPE_EDGE](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#gaff68b0efbc719bc28f0d56c9ba8607bc)
- [IRQ_DEFAULT_PRIORITY](https://docs.zephyrproject.org/latest/doxygen/html/group__dt__ti__vim.html#ga2dbeaa0c017cdff0982b381cc96f0a6c)

<a id="header-details"></a>

---

[上一章](P069_zephyr__dt-bindings__pinctrl__ti-cc32xx-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P071_zephyr__drivers__sensor__tmp451.h_文件参考.md)
