---
id: learning.zephyr-docs.api-file-system-power-reference.page-34
title: zephyr__posix__sys__eventfd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第34章\_zephyr\_\_posix\_\_sys\_\_eventfd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2eventfd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/zvfs/eventfd.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 34.1\_宏定义（Macros）

<a id="r_aa1cf1f9ea4d84916ad5fdf7105d4ee1f"></a>

```c
#define EFD_SEMAPHORE ZVFS_EFD_SEMAPHORE
```

相关声明：[EFD_SEMAPHORE](#aa1cf1f9ea4d84916ad5fdf7105d4ee1f)、[ZVFS_EFD_SEMAPHORE](P047_zephyr__zvfs__eventfd.h_文件参考.md#acab48945c7bdd3530651feeb169b75f6)。

<a id="r_a04677f5ad8d61c569b9c32ec35b05e7a"></a>

```c
#define EFD_NONBLOCK ZVFS_EFD_NONBLOCK
```

相关声明：[EFD_NONBLOCK](#a04677f5ad8d61c569b9c32ec35b05e7a)、[ZVFS_EFD_NONBLOCK](P047_zephyr__zvfs__eventfd.h_文件参考.md#a6374eeebdd4ebe2d5580f5be79839c26)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 34.2\_类型定义（Typedefs）

<a id="r_ac8eb3d8ee0d064d293a5433c2c1f6165"></a>

```c
typedef zvfs_eventfd_t eventfd_t
```

相关声明：[zvfs_eventfd_t](P047_zephyr__zvfs__eventfd.h_文件参考.md#a2f8a313f0a8175844c91c78d5b9340ad)、[eventfd_t](#ac8eb3d8ee0d064d293a5433c2c1f6165)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 34.3\_函数（Functions）

<a id="r_ab06039421a08cedb36946381608fa7f7"></a>

```c
int eventfd (unsigned int initval, int flags)
```

相关声明：[eventfd](#ab06039421a08cedb36946381608fa7f7)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

创建用于事件通知（Event Notification）的文件描述符（File Descriptor）。

<a id="r_a32e55549cb7aea88db8a14be9ed5d092"></a>

```c
int eventfd_read (int fd, eventfd_t *value)
```

相关声明：[eventfd_read](#a32e55549cb7aea88db8a14be9ed5d092)、[eventfd_t](#ac8eb3d8ee0d064d293a5433c2c1f6165)。

从 `eventfd` 读取（Read）。

<a id="r_a9c7aafe8ee787e3ba362fb6aab3e5542"></a>

```c
int eventfd_write (int fd, eventfd_t value)
```

相关声明：[eventfd_write](#a9c7aafe8ee787e3ba362fb6aab3e5542)、[eventfd_t](#ac8eb3d8ee0d064d293a5433c2c1f6165)。

向 `eventfd` 写入（Write）。

## 34.4\_详细说明（Detailed Documentation）

<a id="a04677f5ad8d61c569b9c32ec35b05e7a"></a>

### `EFD_NONBLOCK`

```c
#define EFD_NONBLOCK ZVFS_EFD_NONBLOCK
```

<a id="aa1cf1f9ea4d84916ad5fdf7105d4ee1f"></a>

### `EFD_SEMAPHORE`

```c
#define EFD_SEMAPHORE ZVFS_EFD_SEMAPHORE
```

<a id="ac8eb3d8ee0d064d293a5433c2c1f6165"></a>

### `eventfd_t`

```c
typedef zvfs_eventfd_t eventfd_t
```

<a id="ab06039421a08cedb36946381608fa7f7"></a>

### `eventfd()`

```c
int eventfd ( unsigned int initval, int flags )
```

创建用于事件通知（Event Notification）的文件描述符（File Descriptor）。

返回的文件描述符（File Descriptor）可与 POSIX `read`／`write` 调用一起使用，也可与 `eventfd_read`／`eventfd_write` 函数一起使用。

它也支持轮询（Polling）。在 `poll` 调用中加入 `eventfd` 后，只需向该 `eventfd` 写入，即可发出信号并唤醒轮询线程（Polling Thread）。

对 `eventfd` 使用 `read()` 和 `write()` 时，大小必须始终至少为 8 字节，否则操作将失败并报 `EINVAL`。

**返回（Returns）**：**返回值（Returns）：**成功返回新的 `eventfd` 文件描述符（File Descriptor），出错返回 `-1`。

<a id="a32e55549cb7aea88db8a14be9ed5d092"></a>

### `eventfd_read()`

```c
int eventfd_read ( int fd, eventfd_t * value )
```

从 `eventfd` 读取（Read）。

调用成功时，`value` 参数的值为 `1`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符（File Descriptor）。 |
| `value` | 用于存储读取值的指针（Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回 `-1`。

<a id="a9c7aafe8ee787e3ba362fb6aab3e5542"></a>

### `eventfd_write()`

```c
int eventfd_write ( int fd, eventfd_t value )
```

向 `eventfd` 写入（Write）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符（File Descriptor）。 |
| `value` | 要写入的值。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回 `-1`。


## 34.5\_原页交叉引用（Cross References）

- [zephyr/zvfs/eventfd.h](../api_source_reference/P942_eventfd.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P666_eventfd.h_源码浏览.md)
- [ZVFS_EFD_SEMAPHORE](P047_zephyr__zvfs__eventfd.h_文件参考.md#acab48945c7bdd3530651feeb169b75f6)
- [ZVFS_EFD_NONBLOCK](P047_zephyr__zvfs__eventfd.h_文件参考.md#a6374eeebdd4ebe2d5580f5be79839c26)
- [zvfs_eventfd_t](P047_zephyr__zvfs__eventfd.h_文件参考.md#a2f8a313f0a8175844c91c78d5b9340ad)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P033_zephyr__dt-bindings__usb-c__pd.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P035_zephyr__drivers__interrupt_controller__riscv_plic.h_文件参考.md)
