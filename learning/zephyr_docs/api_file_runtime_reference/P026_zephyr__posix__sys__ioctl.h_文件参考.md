---
id: learning.zephyr-docs.api-file-runtime-reference.page-26
title: zephyr__posix__sys__ioctl.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ioctl_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_zephyr\_\_posix\_\_sys\_\_ioctl.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ioctl_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/sys/fdtable.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 26.1\_宏定义（Macros）

<a id="r_af48a6e38eb0ae226621514b44b9844eb"></a>

```c
#define FIONBIO ZFD_IOCTL_FIONBIO
```

相关声明：[FIONBIO](#af48a6e38eb0ae226621514b44b9844eb)、[ZFD_IOCTL_FIONBIO](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)。

设置非阻塞模式（Non-Blocking Mode）。

<a id="r_ac68826c621a12d91544dab200c86c75a"></a>

```c
#define FIONREAD ZFD_IOCTL_FIONREAD
```

相关声明：[FIONREAD](#ac68826c621a12d91544dab200c86c75a)、[ZFD_IOCTL_FIONREAD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)。

获取可供读取的字节数（Number of Bytes Available to Read）。

<a id="r_a6826e2f7fe26c70ff7b4929843ce399a"></a>

```c
#define FIONWRITE ZFD_IOCTL_FIONWRITE
```

相关声明：[FIONWRITE](#a6826e2f7fe26c70ff7b4929843ce399a)、[ZFD_IOCTL_FIONWRITE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb)。

获取已排队等待 TCP 发送、但尚未收到确认的字节数（Unacknowledged TCP TX Bytes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.2\_函数（Functions）

<a id="r_a1487536105f7a596481bf6bfa8de99f6"></a>

```c
int ioctl (int fd, unsigned long request,...)
```

相关声明：[ioctl](#a1487536105f7a596481bf6bfa8de99f6)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

## 26.3\_详细说明（Detailed Documentation）

<a id="af48a6e38eb0ae226621514b44b9844eb"></a>

### `FIONBIO`

```c
#define FIONBIO ZFD_IOCTL_FIONBIO
```

设置非阻塞模式（Non-Blocking Mode）。

<a id="ac68826c621a12d91544dab200c86c75a"></a>

### `FIONREAD`

```c
#define FIONREAD ZFD_IOCTL_FIONREAD
```

获取可供读取的字节数（Number of Bytes Available to Read）。

<a id="a6826e2f7fe26c70ff7b4929843ce399a"></a>

### `FIONWRITE`

```c
#define FIONWRITE ZFD_IOCTL_FIONWRITE
```

获取已排队等待 TCP 发送、但尚未收到确认的字节数（Unacknowledged TCP TX Bytes）。

<a id="a1487536105f7a596481bf6bfa8de99f6"></a>

### `ioctl()`

```c
int ioctl ( int fd, unsigned long request, ... )
```


## 26.4\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P408_ioctl.h_源码浏览.md)
- [ZFD_IOCTL_FIONBIO](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a7c70aef3ad6110cbdfa3bd4f843ec530)
- [ZFD_IOCTL_FIONREAD](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a34b26658321074989ee1db15aab5f683)
- [ZFD_IOCTL_FIONWRITE](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h.html#aac8cb8bde69d227a7a8e9edf2980bd20a1e88b6e9ca6cf0db43029f485af43ccb)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P025_zephyr__drivers__interrupt_controller__intc_max32_rv32.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P027_zephyr__net__ipv4_nat.h_文件参考.md)
