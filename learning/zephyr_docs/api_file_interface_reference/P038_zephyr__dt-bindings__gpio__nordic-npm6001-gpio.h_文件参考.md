---
id: learning.zephyr-docs.api-file-interface-reference.page-38
title: zephyr__dt-bindings__gpio__nordic-npm6001-gpio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_dt-bindings\_\_gpio\_\_nordic-npm6001-gpio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/nordic-npm6001-gpio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 38.1\_宏定义（Macros）

<a id="define-members-0"></a>

### nPM6001 GPIO 驱动强度标志（drive strength flags）。

nPM6001 GPIO 驱动强度标志（drive strength flags）。

<a id="r_gaa127d582ea7095b4d7a435ee5ea427c9"></a>

```c
#define NPM6001_GPIO_DRIVE_NORMAL (0U << 8U)
```

相关声明：[NPM6001_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#gaa127d582ea7095b4d7a435ee5ea427c9)。

普通驱动（Normal Drive）。

<a id="r_ga097b6c75d981ad5ecf38a2133d076178"></a>

```c
#define NPM6001_GPIO_DRIVE_HIGH (1U << 8U)
```

相关声明：[NPM6001_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga097b6c75d981ad5ecf38a2133d076178)。

高驱动（High Drive）。

<a id="r_ga3cde51b59da0f8bf4693ef18b9ee8a30"></a>

```c
#define NPM6001_GPIO_SENSE_SCHMITT (0U << 9U)
```

相关声明：[NPM6001_GPIO_SENSE_SCHMITT](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga3cde51b59da0f8bf4693ef18b9ee8a30)。

施密特触发器（Schmitt trigger）输入类型。

<a id="r_ga98c66bc1cf5a8c0f83b82c830a817fa2"></a>

```c
#define NPM6001_GPIO_SENSE_CMOS (1U << 9U)
```

相关声明：[NPM6001_GPIO_SENSE_CMOS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga98c66bc1cf5a8c0f83b82c830a817fa2)。

CMOS 输入类型。


## 38.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P584_nordic-npm6001-gpio.h_源码浏览.md)
- [NPM6001_GPIO_DRIVE_NORMAL](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#gaa127d582ea7095b4d7a435ee5ea427c9)
- [NPM6001_GPIO_DRIVE_HIGH](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga097b6c75d981ad5ecf38a2133d076178)
- [NPM6001_GPIO_SENSE_SCHMITT](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga3cde51b59da0f8bf4693ef18b9ee8a30)
- [NPM6001_GPIO_SENSE_CMOS](https://docs.zephyrproject.org/latest/doxygen/html/group__gpio__interface__npm6001.html#ga98c66bc1cf5a8c0f83b82c830a817fa2)

---

[上一章](P037_zephyr__net__net_core.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__dt-bindings__sensor__npcx_tach.h_文件参考.md)
