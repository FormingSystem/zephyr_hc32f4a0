---
id: learning.zephyr-docs.api-platform-topic-reference.page-130
title: Xen 控制台驱动（Console driver）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第130章\_Xen 控制台驱动（Console driver）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__console__driver.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

使 Xen UART 控制台实现与其设备数据布局保持同步。

<a id="details"></a>

使 Xen UART 控制台实现与其设备数据布局保持同步。

<a id="header-files"></a>
<a id="files"></a>

## 130.1\_文件（Files）

<a id="r_console_2Eh"></a>

```c
file console.h
```

相关声明：[console.h](../api_file_supplement_reference/P129_zephyr__xen__console.h_文件参考.md)。

Xen控制台驱动（Console Driver）的内部数据。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 130.2\_函数（Functions）

<a id="r_ga6e114bd3611c8d2e10541011f0c7c65e"></a>

```c
int xen_console_init (const struct device *dev)
```

相关声明：[xen_console_init](#ga6e114bd3611c8d2e10541011f0c7c65e)、[device](../device_reference/P002_设备对象结构.md)。

初始化 Xen 控制台 UART 实例（Console UART Instance）。

## 130.3\_详细说明（Detailed Documentation）

<a id="ga6e114bd3611c8d2e10541011f0c7c65e"></a>

### `xen_console_init()`

```c
int xen_console_init ( const struct device * dev)
```

```c
#include <zephyr/xen/console.h>
```

初始化 Xen 控制台 UART 实例（Console UART Instance）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 要初始化的 UART 设备实例（Device Instance）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 130.4\_原页交叉引用（Cross References）

- [console.h](../api_file_supplement_reference/P129_zephyr__xen__console.h_文件参考.md)
- [device](../device_reference/P002_设备对象结构.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P129_虚拟接口库（Virtual Interface Library）.md) · [返回大纲](大纲.md) · [下一章](P131_Xen 支持.md)
