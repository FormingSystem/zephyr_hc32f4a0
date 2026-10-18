---
id: learning.zephyr-docs.api-file-system-power-reference.page-47
title: zephyr__zvfs__eventfd.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zvfs_2eventfd_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_zephyr\_\_zvfs\_\_eventfd.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/zvfs_2eventfd_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 47.1\_宏定义（Macros）

<a id="r_acab48945c7bdd3530651feeb169b75f6"></a>

```c
#define ZVFS_EFD_SEMAPHORE 2
```

相关声明：[ZVFS_EFD_SEMAPHORE](#acab48945c7bdd3530651feeb169b75f6)。

<a id="r_a6374eeebdd4ebe2d5580f5be79839c26"></a>

```c
#define ZVFS_EFD_NONBLOCK 0x4000
```

相关声明：[ZVFS_EFD_NONBLOCK](#a6374eeebdd4ebe2d5580f5be79839c26)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 47.2\_类型定义（Typedefs）

<a id="r_a2f8a313f0a8175844c91c78d5b9340ad"></a>

```c
typedef uint64_t zvfs_eventfd_t
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[zvfs_eventfd_t](#a2f8a313f0a8175844c91c78d5b9340ad)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 47.3\_函数（Functions）

<a id="r_af970bc2d7c58286477ae098ce03843ca"></a>

```c
int zvfs_eventfd (unsigned int initval, int flags)
```

相关声明：[zvfs_eventfd](#af970bc2d7c58286477ae098ce03843ca)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

创建用于 ZVFS 事件通知（Event Notification）的文件描述符（File Descriptor）。

<a id="r_a350f18c251bf9e925d3632a6ae8fa1f3"></a>

```c
int zvfs_eventfd_read (int fd, zvfs_eventfd_t *value)
```

相关声明：[zvfs_eventfd_read](#a350f18c251bf9e925d3632a6ae8fa1f3)、[zvfs_eventfd_t](#a2f8a313f0a8175844c91c78d5b9340ad)。

从 ZVFS `eventfd` 读取（Read）。

<a id="r_a75c589c08e741558dc4086d84713e031"></a>

```c
int zvfs_eventfd_write (int fd, zvfs_eventfd_t value)
```

相关声明：[zvfs_eventfd_write](#a75c589c08e741558dc4086d84713e031)、[zvfs_eventfd_t](#a2f8a313f0a8175844c91c78d5b9340ad)。

向 ZVFS `eventfd` 写入（Write）。

## 47.4\_详细说明（Detailed Documentation）

<a id="a6374eeebdd4ebe2d5580f5be79839c26"></a>

### `ZVFS_EFD_NONBLOCK`

```c
#define ZVFS_EFD_NONBLOCK 0x4000
```

<a id="acab48945c7bdd3530651feeb169b75f6"></a>

### `ZVFS_EFD_SEMAPHORE`

```c
#define ZVFS_EFD_SEMAPHORE 2
```

<a id="a2f8a313f0a8175844c91c78d5b9340ad"></a>

### `zvfs_eventfd_t`

```c
typedef uint64_t zvfs_eventfd_t
```

<a id="af970bc2d7c58286477ae098ce03843ca"></a>

### `zvfs_eventfd()`

```c
int zvfs_eventfd ( unsigned int initval, int flags )
```

创建用于 ZVFS 事件通知（Event Notification）的文件描述符（File Descriptor）。

返回的文件描述符（File Descriptor）可与 POSIX `read`／`write` 调用一起使用，也可与 `zvfs_eventfd_read` 或 `zvfs_eventfd_write` 函数一起使用。

它也支持轮询（Polling）。在 `poll` 调用中加入 `eventfd` 后，只需向该 `eventfd` 写入，即可发出信号并唤醒轮询线程（Polling Thread）。

对 ZVFS `eventfd` 使用 `read()` 和 `write()` 时，大小必须始终至少为 8 字节，否则操作将失败并报 `EINVAL`。

**返回（Returns）**：**返回值（Returns）：**成功返回新的 ZVFS `eventfd` 文件描述符（File Descriptor），出错返回 `-1`。

<a id="a350f18c251bf9e925d3632a6ae8fa1f3"></a>

### `zvfs_eventfd_read()`

```c
int zvfs_eventfd_read ( int fd, zvfs_eventfd_t * value )
```

从 ZVFS `eventfd` 读取（Read）。

调用成功时，`value` 参数的值为 `1`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符（File Descriptor）。 |
| `value` | 用于存储读取值的指针（Pointer）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回 `-1`。

<a id="a75c589c08e741558dc4086d84713e031"></a>

### `zvfs_eventfd_write()`

```c
int zvfs_eventfd_write ( int fd, zvfs_eventfd_t value )
```

向 ZVFS `eventfd` 写入（Write）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `fd` | 文件描述符（File Descriptor）。 |
| `value` | 要写入的值。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，出错返回 `-1`。


## 47.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P942_eventfd.h_源码浏览.md)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P046_____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztress.h_文件参考.md) · [返回大纲](大纲.md)
