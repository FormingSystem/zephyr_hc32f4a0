---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-5
title: 控制台 API（Console API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_控制台 API（Console API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__console__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

控制台 API（Console API）

<a id="details"></a>

控制台 API（Console API）

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.1\_函数（Functions）

<a id="r_ga0bf949437e32d17992435003cf8b46b5"></a>

```c
int console_init (void)
```

相关声明：[console_init](#ga0bf949437e32d17992435003cf8b46b5)。

初始化控制台设备（Console Device）。

<a id="r_ga27785534c14d4098822db2b870b7d81d"></a>

```c
ssize_t console_read (void *dummy, void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[console_read](#ga27785534c14d4098822db2b870b7d81d)。

从控制台（Console）读取数据。

<a id="r_ga204fd795daf9ef6b1f2803547747545e"></a>

```c
ssize_t console_write (void *dummy, const void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[console_write](#ga204fd795daf9ef6b1f2803547747545e)。

向控制台（Console）写入数据。

<a id="r_ga2ba36eb1081cd0b98aa43216ccd6fbd5"></a>

```c
int console_getchar (void)
```

相关声明：[console_getchar](#ga2ba36eb1081cd0b98aa43216ccd6fbd5)。

从控制台输入缓冲区（Input Buffer）获取下一个字符。

<a id="r_ga7bd842f1cda6c8218cb1d41420e4de49"></a>

```c
int console_putchar (char c)
```

相关声明：[console_putchar](#ga7bd842f1cda6c8218cb1d41420e4de49)。

向控制台输出一个字符，使用缓冲（Buffered）。

<a id="r_gacd13267df8567c63f2285ce0e1cbbc20"></a>

```c
void console_getline_init (void)
```

相关声明：[console_getline_init](#gacd13267df8567c63f2285ce0e1cbbc20)。

初始化 `console_getline()` 调用所需的状态。

<a id="r_ga3454f5b84d38d46a6c2bbf7fd6baa815"></a>

```c
char * console_getline (void)
```

相关声明：[console_getline](#ga3454f5b84d38d46a6c2bbf7fd6baa815)。

从控制台输入缓冲区获取下一行（Next Line）。

<a id="r_ga83d86a81638a96ae84df792265dc0219"></a>

```c
void console_set_rx_timeout (k_timeout_t timeout)
```

相关声明：[console_set_rx_timeout](#ga83d86a81638a96ae84df792265dc0219)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置控制台操作的接收超时（Receive Timeout）。

<a id="r_ga401af68bb10c5b5e2a99997cee7de9c7"></a>

```c
void console_set_tx_timeout (k_timeout_t timeout)
```

相关声明：[console_set_tx_timeout](#ga401af68bb10c5b5e2a99997cee7de9c7)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

设置控制台操作的发送超时（Transmit Timeout）。

## 5.2\_详细说明（Detailed Documentation）

<a id="ga2ba36eb1081cd0b98aa43216ccd6fbd5"></a>

### `console_getchar()`

```c
int console_getchar ( void )
```

```c
#include <zephyr/console/console.h>
```

从控制台输入缓冲区（Input Buffer）获取下一个字符。

返回控制台的下一个输入字符（Input Character）。没有可用字符时阻塞。本函数类似 ANSI C 的 `getchar()`，用于方便移植已有软件。使用前必须先调用一次 `console_init()`。它与 Zephyr 原生基于回调的控制台输入处理、shell 子系统及 `console_getline()` 不兼容。

**返回（Returns）**：**返回值（Returns）：**`0–255` 为读到的字符，包括控制字符（Control Characters）；负值表示错误。

<a id="ga3454f5b84d38d46a6c2bbf7fd6baa815"></a>

### `console_getline()`

```c
char * console_getline ( void )
```

```c
#include <zephyr/console/console.h>
```

从控制台输入缓冲区获取下一行（Next Line）。

返回控制台的下一行输入（Input Line），完整行可用之前阻塞。本函数类似 ANSI C 的 `gets()`，但返回的行位于系统所有的缓冲区（System-owned Buffer），并由系统检查缓冲区溢出，用于方便移植已有软件。使用前必须先调用一次 `console_getline_init()`。它与 Zephyr 原生基于回调的控制台输入处理、shell 子系统及 `console_getchar()` 不兼容。

**返回（Returns）**：**返回值（Returns）：**指向读取行的指针，不包含行结束字符（EOL）。该行位于系统所有的缓冲区，因此应用应在 `console_getline()` 返回后立即完成处理，否则缓冲区可能被复用。

<a id="gacd13267df8567c63f2285ce0e1cbbc20"></a>

### `console_getline_init()`

```c
void console_getline_init ( void )
```

```c
#include <zephyr/console/console.h>
```

初始化 `console_getline()` 调用所需的状态。

应调用一次本函数，初始化通过 `console_getline()` 拉取式（Pull-style）访问控制台。它取代基于 `console_input_fn` 等回调的推送式（Push-style）控制台处理，并与后者不兼容。

<a id="ga0bf949437e32d17992435003cf8b46b5"></a>

### `console_init()`

```c
int console_init ( void )
```

```c
#include <zephyr/console/console.h>
```

初始化控制台设备（Console Device）。

应调用一次本函数，初始化通过 `console_getchar()` 拉取式（Pull-style）访问控制台，以及通过 `console_putchar()` 进行缓冲输出。它取代基于 `console_input_fn` 等回调的推送式（Push-style）控制台处理，并与后者不兼容。

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，否则返回负错误码。

<a id="ga7bd842f1cda6c8218cb1d41420e4de49"></a>

### `console_putchar()`

```c
int console_putchar ( char c)
```

```c
#include <zephyr/console/console.h>
```

向控制台输出一个字符，使用缓冲（Buffered）。

将一个字符放入控制台输出缓冲区（Output Buffer），随后异步发送到控制台，例如由 IRQ 处理程序发送。

**返回（Returns）**：**返回值（Returns）：**出错为负值，否则为 `0`。

<a id="ga27785534c14d4098822db2b870b7d81d"></a>

### `console_read()`

```c
ssize_t console_read ( void * dummy, void * buf, size_t size )
```

```c
#include <zephyr/console/console.h>
```

从控制台（Console）读取数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Dummy L2/driver Support Functions` | 忽略此参数，仅为遵循 `read()` 原型而保留。 |
| `buf` | 用于接收读取数据的缓冲区（Buffer）。 |
| `size` | 最多读取的字节数。 |

**返回（Returns）**：**返回值（Returns）：**正数为实际读取字节数，可能小于 `size`；文件结束（EOF）返回 `0`；出错返回负值，例如超时返回 `-EAGAIN`。同时设置 `errno` 变量。

<a id="ga83d86a81638a96ae84df792265dc0219"></a>

### `console_set_rx_timeout()`

```c
void console_set_rx_timeout ( k_timeout_t timeout)
```

```c
#include <zephyr/console/console.h>
```

设置控制台操作的接收超时（Receive Timeout）。

设置 `console_getchar()` 和 `console_read()` 操作的超时时间（Timeout）。初始化后的默认值为 `K_FOREVER`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 读取时的最长等待时间（Maximum Wait Time）。 |

<a id="ga401af68bb10c5b5e2a99997cee7de9c7"></a>

### `console_set_tx_timeout()`

```c
void console_set_tx_timeout ( k_timeout_t timeout)
```

```c
#include <zephyr/console/console.h>
```

设置控制台操作的发送超时（Transmit Timeout）。

设置输出缓冲区已满时，`console_putchar()` 和 `console_write()` 操作的超时时间（Timeout）。初始化后的默认值为 `K_FOREVER`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 写入时的最长等待时间（Maximum Wait Time）。 |

<a id="ga204fd795daf9ef6b1f2803547747545e"></a>

### `console_write()`

```c
ssize_t console_write ( void * dummy, const void * buf, size_t size )
```

```c
#include <zephyr/console/console.h>
```

向控制台（Console）写入数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `Dummy L2/driver Support Functions` | 忽略此参数，仅为遵循 `write()` 原型而保留。 |
| `buf` | 要写入数据的缓冲区（Buffer）。 |
| `size` | 最多写入的字节数（Maximum Number of Bytes）。 |

**返回（Returns）**：**返回值（Returns）：**非负数为实际写入字节数，可能小于 `size`；出错返回负值，例如超时返回 `-EAGAIN`。同时设置 `errno` 变量。


## 5.3\_原页交叉引用（Cross References）

- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [zephyr/console/console.h](../api_file_network_device_reference/P005_zephyr__console__console.h_文件参考.md)
- [console_input_fn](../api_file_interface_reference/P015_zephyr__drivers__console__console.h_文件参考.md#a0dab6d89950bb4c2bbb17571b9b1461f)
- [虚拟二层/驱动支持函数（Dummy L2/driver Support Functions）](../api_platform_topic_reference/P050_虚拟二层_驱动支持函数（Dummy L2_driver Support Functions）.md)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P004_连接管理器连接性实现 API（Connectivity Implementation API）.md) · [返回大纲](大纲.md) · [下一章](P006_磁盘访问接口（Disk Access Interface）.md)
