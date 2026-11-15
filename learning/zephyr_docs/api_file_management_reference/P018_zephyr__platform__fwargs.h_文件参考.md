---
id: learning.zephyr-docs.api-file-management-reference.page-18
title: zephyr__platform__fwargs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第18章\_zephyr\_\_platform\_\_fwargs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fwargs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固件参数处理钩子（Firmware Argument Handling Hooks）。

<a id="details"></a>

```c
#include <stddef.h>
#include <stdint.h>
```

查看此文件的源码。

固件参数处理钩子（Firmware Argument Handling Hooks）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 18.1\_函数（Functions）

<a id="r_adb1a5f394ddae4582b7a522e9b0a80bc"></a>

```c
void fwargs_handler_hook (const uintptr_t *args, size_t argc)
```

相关声明：[fwargs_handler_hook](#adb1a5f394ddae4582b7a522e9b0a80bc)、[uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)。

处理架构保留的固件参数（firmware arguments）。

## 18.2\_详细说明（Detailed Documentation）

<a id="adb1a5f394ddae4582b7a522e9b0a80bc"></a>

### `fwargs_handler_hook()`

```c
void fwargs_handler_hook ( const uintptr_t * args, size_t argc )
```

处理架构保留的固件参数（firmware arguments）。

此钩子（hook）由了解该架构固件参数约定的平台专用代码实现。它接收架构在初始化期间保留的固件参数。

此钩子在主 CPU 上运行，时机为 BSS 和数据初始化之后、常规内核初始化之前。实现不得假定内存地址转换（memory translation）、设备、内存分配或调度服务已经可用。

参数数组在调用期间有效。稍后还需要使用的值必须复制。由这些值引用的内存，其生命周期取决于平台的启动协议（boot protocol）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `args` | 架构提供的固件参数数组。 |
| `argc` | `args` 中的条目数。 |


## 18.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P282_fwargs.h_源码浏览.md)
- [uintptr_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a4788399d1d0b37ccf098a7da82254808)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P017_zephyr__drivers__misc__ft8xx__ft8xx_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P019_zephyr__dt-bindings__clock__gd32-clocks-common.h_文件参考.md)
