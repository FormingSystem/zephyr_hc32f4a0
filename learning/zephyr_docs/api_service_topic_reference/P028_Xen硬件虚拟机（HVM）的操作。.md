---
id: learning.zephyr-docs.api-service-topic-reference.page-28
title: Xen硬件虚拟机（HVM）的操作。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第28章\_Xen硬件虚拟机（HVM）的操作。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__xen__hvm.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过 HVM 超级调用（Hypercall）配置 Xen 硬件虚拟机（HVM）客户机参数。

<a id="details"></a>

通过 HVM 超级调用（Hypercall）配置 Xen 硬件虚拟机（HVM）客户机参数。

<a id="header-files"></a>
<a id="files"></a>

## 28.1\_文件（Files）

<a id="r_hvm_2Eh"></a>

```c
file hvm.h
```

相关声明：[hvm.h](../api_file_configuration_reference/P038_zephyr__xen__hvm.h_文件参考.md)。

Xen硬件虚拟机（HVM）的操作。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 28.2\_函数（Functions）

<a id="r_gae375499424094b2f6f8059160456b53e"></a>

```c
int hvm_set_parameter (int idx, int domid, uint64_t value)
```

相关声明：[hvm_set_parameter](#gae375499424094b2f6f8059160456b53e)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

为 Xen 域（Domain）设置硬件虚拟机参数（HVM Parameter）。

<a id="r_gaa4c66d130a846c3effc5ec3052d95f82"></a>

```c
int hvm_get_parameter (int idx, int domid, uint64_t *value)
```

相关声明：[hvm_get_parameter](#gaa4c66d130a846c3effc5ec3052d95f82)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

从 Xen 域（Domain）获取硬件虚拟机参数（HVM Parameter）。

## 28.3\_详细说明（Detailed Documentation）

<a id="gaa4c66d130a846c3effc5ec3052d95f82"></a>

### `hvm_get_parameter()`

```c
int hvm_get_parameter ( int idx, int domid, uint64_t * value )
```

```c
#include <zephyr/xen/hvm.h>
```

从 Xen 域（Domain）获取硬件虚拟机参数（HVM Parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` idx` | 硬件虚拟机参数选择器（HVM Parameter Selector），通常为某个 `HVM_PARAM_*` 常量。 |
| ` domid` | 目标 Xen 域标识（Domain Identifier）。 |
| `[out] value` | 指向接收参数值的缓冲区（Buffer）的指针（Pointer）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gae375499424094b2f6f8059160456b53e"></a>

### `hvm_set_parameter()`

```c
int hvm_set_parameter ( int idx, int domid, uint64_t value )
```

```c
#include <zephyr/xen/hvm.h>
```

为 Xen 域（Domain）设置硬件虚拟机参数（HVM Parameter）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `idx` | 硬件虚拟机参数选择器（HVM Parameter Selector），通常为某个 `HVM_PARAM_*` 常量。 |
| `domid` | 目标 Xen 域标识（Domain Identifier）。 |
| `value` | 要存储的参数值（Parameter Value）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 28.4\_原页交叉引用（Cross References）

- [hvm.h](../api_file_configuration_reference/P038_zephyr__xen__hvm.h_文件参考.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P027_XBR818 API主题.md) · [返回大纲](大纲.md)
