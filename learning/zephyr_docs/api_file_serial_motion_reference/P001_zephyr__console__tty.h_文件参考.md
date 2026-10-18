---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-1
title: zephyr__console__tty.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_console\_\_tty.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_tty_5Fserial"></a>

```c
struct tty_serial
```

相关声明：[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)。

串口对象（Serial Port Object），传统上称为tty。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.2\_函数（Functions）

<a id="r_a5a880bb61f0bdb0f37c501acc0408d32"></a>

```c
int tty_init (struct tty_serial *tty, const struct device *uart_dev)
```

相关声明：[tty_init](#a5a880bb61f0bdb0f37c501acc0408d32)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)、[device](../device_reference/P002_设备对象结构.md)。

初始化串口对象（Serial Port Object），传统上称为 tty。

<a id="r_a109fd8ee6b581a796d67025a0e33abde"></a>

```c
static void tty_set_rx_timeout (struct tty_serial *tty, int32_t timeout)
```

相关声明：[tty_set_rx_timeout](#a109fd8ee6b581a796d67025a0e33abde)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置 tty 设备的接收超时（Receive Timeout）。

<a id="r_a1c19c6ed8207ae711e047f9ae446e399"></a>

```c
static void tty_set_tx_timeout (struct tty_serial *tty, int32_t timeout)
```

相关声明：[tty_set_tx_timeout](#a1c19c6ed8207ae711e047f9ae446e399)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)、[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)。

设置 tty 设备的发送超时（Transmit Timeout）。

<a id="r_ad05b854f19b3bd97e2635bc8ebc07ce2"></a>

```c
int tty_set_rx_buf (struct tty_serial *tty, void *buf, size_t size)
```

相关声明：[tty_set_rx_buf](#ad05b854f19b3bd97e2635bc8ebc07ce2)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)。

设置 tty 设备的接收缓冲区（Receive Buffer）。

<a id="r_af6383a47f82797af9a45bc81d84de1be"></a>

```c
int tty_set_tx_buf (struct tty_serial *tty, void *buf, size_t size)
```

相关声明：[tty_set_tx_buf](#af6383a47f82797af9a45bc81d84de1be)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)。

设置 tty 设备的发送缓冲区（Transmit Buffer）。

<a id="r_a90ec3fbbe5f0fad19361d23e821c960c"></a>

```c
ssize_t tty_read (struct tty_serial *tty, void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[tty_read](#a90ec3fbbe5f0fad19361d23e821c960c)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)。

从 tty 设备读取数据（Read Data）。

<a id="r_af60d8a57ac3cb81a0a003a011a0f31e5"></a>

```c
ssize_t tty_write (struct tty_serial *tty, const void *buf, size_t size)
```

相关声明：[ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)、[tty_write](#af60d8a57ac3cb81a0a003a011a0f31e5)、[tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)。

向 tty 设备写入数据（Write Data）。

## 1.3\_详细说明（Detailed Documentation）

<a id="a5a880bb61f0bdb0f37c501acc0408d32"></a>

### `tty_init()`

```c
int tty_init ( struct tty_serial * tty, const struct device * uart_dev )
```

初始化串口对象（Serial Port Object），传统上称为 tty。

`tty` 设备支持以带缓冲（Buffered）、中断驱动（Interrupt-driven）和超时控制（Timeout-controlled）的方式访问底层 UART 设备。为保证完整性，也支持非中断驱动的忙轮询访问模式（Busy-polling）。初始化后，tty 处于“最保守”的无缓冲模式，且超时为无限长；此配置保证适用于任何硬件。用户应根据需要，通过 `tty_set_rx_buf()`、`tty_set_tx_buf()`、`tty_set_rx_timeout()` 和 `tty_set_tx_timeout()` 配置缓冲区及超时。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | 要初始化的 tty 设备结构体（Device Structure）。 |
| `uart_dev` | 要使用的底层 UART 设备，应支持中断驱动操作（Interrupt-driven Operation）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 `0`，否则返回负错误码。

<a id="a90ec3fbbe5f0fad19361d23e821c960c"></a>

### `tty_read()`

```c
ssize_t tty_read ( struct tty_serial * tty, void * buf, size_t size )
```

从 tty 设备读取数据（Read Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `buf` | 用于接收读取数据的缓冲区（Buffer）。 |
| `size` | 最多读取的字节数。 |

**返回（Returns）**：返回值：大于 0 时表示实际读取的字节数，可小于 `size` 参数；等于 0 时表示类似文件结束（EOF）的条件，例如收到 break 信号；小于 0 时表示错误，例如超时返回 `-EAGAIN`。同时设置 `errno` 变量。

<a id="ad05b854f19b3bd97e2635bc8ebc07ce2"></a>

### `tty_set_rx_buf()`

```c
int tty_set_rx_buf ( struct tty_serial * tty, void * buf, size_t size )
```

设置 tty 设备的接收缓冲区（Receive Buffer）。

设置接收缓冲区，或将接收切换为无缓冲操作（Unbuffered Operation）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `buf` | 缓冲区（Buffer）；无缓冲操作时为 `NULL`。 |
| `size` | 缓冲区大小（Buffer Size）；无缓冲操作时为 0。 |

**返回（Returns）**：返回值：成功返回 0，否则返回小于 0 的错误码；`EINVAL` 表示不支持的缓冲区或大小。

<a id="a109fd8ee6b581a796d67025a0e33abde"></a>

### `tty_set_rx_timeout()`

```c
void tty_set_rx_timeout ( struct tty_serial * tty, int32_t timeout )
```

声明属性：`inline`、`static`。

设置 tty 设备的接收超时（Receive Timeout）。

设置 `getchar()` 操作的超时（Timeout）。设备初始化后的默认超时为 `SYS_FOREVER_MS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `timeout` | 以毫秒表示的超时（Timeout），或 0，或 `SYS_FOREVER_MS`。 |

<a id="af6383a47f82797af9a45bc81d84de1be"></a>

### `tty_set_tx_buf()`

```c
int tty_set_tx_buf ( struct tty_serial * tty, void * buf, size_t size )
```

设置 tty 设备的发送缓冲区（Transmit Buffer）。

设置发送缓冲区，或将发送切换为无缓冲操作（Unbuffered Operation）。注意：无缓冲模式本身是阻塞的，等效于设置了 `tty_set_tx_timeout(SYS_FOREVER_MS)`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `buf` | 缓冲区（Buffer）；无缓冲操作时为 `NULL`。 |
| `size` | 缓冲区大小（Buffer Size）；无缓冲操作时为 0。 |

**返回（Returns）**：返回值：成功返回 0，否则返回小于 0 的错误码；`EINVAL` 表示不支持的缓冲区或大小。

<a id="a1c19c6ed8207ae711e047f9ae446e399"></a>

### `tty_set_tx_timeout()`

```c
void tty_set_tx_timeout ( struct tty_serial * tty, int32_t timeout )
```

声明属性：`inline`、`static`。

设置 tty 设备的发送超时（Transmit Timeout）。

设置输出缓冲区满时 `putchar()` 操作的超时（Timeout）。设备初始化后的默认超时为 `SYS_FOREVER_MS`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `timeout` | 以毫秒表示的超时（Timeout），或 0，或 `SYS_FOREVER_MS`。 |

<a id="af60d8a57ac3cb81a0a003a011a0f31e5"></a>

### `tty_write()`

```c
ssize_t tty_write ( struct tty_serial * tty, const void * buf, size_t size )
```

向 tty 设备写入数据（Write Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tty` | tty 设备结构体（Device Structure）。 |
| `buf` | 包含数据的缓冲区（Buffer）。 |
| `size` | 最多写入的字节数（Maximum Number of Bytes）。 |

**返回（Returns）**：**返回值（Returns）：**非负数为实际写入字节数，可能小于 `size`；出错返回负值，例如超时返回 `-EAGAIN`。同时设置 `errno` 变量。


## 1.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P116_tty.h_源码浏览.md)
- [tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [ssize_t](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a5c5d83d87790efd59ea916c2b99f9118)
- [putchar()](../api_file_reference/P409_____w__zephyr__zephyr__lib__libc__minimal__include__stdio.h_文件参考.md#a568f021a83b2c22e1e700d12559d660a)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__dai.h_文件参考.md)
