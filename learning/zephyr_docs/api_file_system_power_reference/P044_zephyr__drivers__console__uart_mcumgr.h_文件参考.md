---
id: learning.zephyr-docs.api-file-system-power-reference.page-44
title: zephyr__drivers__console__uart_mcumgr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_zephyr\_\_drivers\_\_console\_\_uart\_mcumgr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/uart__mcumgr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

通过UART发送和接收mcumgr数据包（Packets）的驱动。

<a id="details"></a>

```c
#include <stdlib.h>
#include <zephyr/types.h>
```

查看此文件的源码。

通过 UART 发送和接收 mcumgr 数据包（Packets）的驱动。**另见（See Also）：**`include/mgmt/serial.h`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 44.1\_数据结构（Data Structures）

<a id="r_uart_5Fmcumgr_5Frx_5Fbuf"></a>

```c
struct uart_mcumgr_rx_buf
```

相关声明：[uart_mcumgr_rx_buf](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md)。

包含通过UART接收的mcumgr片段（Fragment）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 44.2\_类型定义（Typedefs）

<a id="r_a0173a370be3e424b56cdfbb3d4174da1"></a>

```c
typedef void uart_mcumgr_recv_fn(struct uart_mcumgr_rx_buf *rx_buf)
```

相关声明：[uart_mcumgr_recv_fn](#a0173a370be3e424b56cdfbb3d4174da1)、[uart_mcumgr_rx_buf](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md)。

收到 mcumgr 数据包（Packet）时调用的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 44.3\_函数（Functions）

<a id="r_acf906a316bf77fc5cc8768130ce82e66"></a>

```c
int uart_mcumgr_send (const uint8_t *data, int len)
```

相关声明：[uart_mcumgr_send](#acf906a316bf77fc5cc8768130ce82e66)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过 UART 发送 mcumgr 数据包（Packet）。

<a id="r_ae173ad28a0301c8ddfdd9b8bc5583ba3"></a>

```c
void uart_mcumgr_free_rx_buf (struct uart_mcumgr_rx_buf *rx_buf)
```

相关声明：[uart_mcumgr_free_rx_buf](#ae173ad28a0301c8ddfdd9b8bc5583ba3)、[uart_mcumgr_rx_buf](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md)。

释放给定的接收缓冲区（Receive Buffer）。

<a id="r_a2b31278c4e600bcd10d1a069cc6f5655"></a>

```c
void uart_mcumgr_register (uart_mcumgr_recv_fn *cb)
```

相关声明：[uart_mcumgr_register](#a2b31278c4e600bcd10d1a069cc6f5655)、[uart_mcumgr_recv_fn](#a0173a370be3e424b56cdfbb3d4174da1)。

注册 mcumgr UART 接收处理程序（Receive Handler）。

## 44.4\_详细说明（Detailed Documentation）

<a id="a0173a370be3e424b56cdfbb3d4174da1"></a>

### `uart_mcumgr_recv_fn`

```c
typedef void uart_mcumgr_recv_fn(struct uart_mcumgr_rx_buf *rx_buf)
```

收到 mcumgr 数据包（Packet）时调用的函数。

收到 mcumgr 数据包（Packet）时调用的函数。本函数在中断上下文（Interrupt Context）中调用；调用发生时，指定缓冲区的所有权（Ownership）转移给回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx_buf` | 包含传入 mcumgr 数据包（Incoming Packet）的缓冲区。 |

<a id="ae173ad28a0301c8ddfdd9b8bc5583ba3"></a>

### `uart_mcumgr_free_rx_buf()`

```c
void uart_mcumgr_free_rx_buf ( struct uart_mcumgr_rx_buf * rx_buf)
```

释放给定的接收缓冲区（Receive Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx_buf` | 要释放的缓冲区（Buffer）。 |

<a id="a2b31278c4e600bcd10d1a069cc6f5655"></a>

### `uart_mcumgr_register()`

```c
void uart_mcumgr_register ( uart_mcumgr_recv_fn * cb)
```

注册 mcumgr UART 接收处理程序（Receive Handler）。

配置 mcumgr UART 驱动，使其在收到 mcumgr 请求包（Request Packet）时调用指定函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 收到 mcumgr 请求包（Request Packet）时执行的回调。 |

<a id="acf906a316bf77fc5cc8768130ce82e66"></a>

### `uart_mcumgr_send()`

```c
int uart_mcumgr_send ( const uint8_t * data, int len )
```

通过 UART 发送 mcumgr 数据包（Packet）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 包含待发送 mcumgr 数据包（Packet）的缓冲区。 |
| `len` | 缓冲区长度（Buffer Length），单位为字节。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负错误码。


## 44.5\_原页交叉引用（Cross References）

- [stdlib.h](../api_source_configuration_reference/P107_stdlib.h_源码浏览.md)
- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P232_uart_mcumgr.h_源码浏览.md)
- [uart_mcumgr_rx_buf](../system_service_model_reference/P088_uart_mcumgr_rx_buf_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P043_zephyr__mgmt__mcumgr__grp__transport_mgmt__transport_mgmt.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P045_zephyr__drivers__usb_c__usbc_ppc.h_文件参考.md)
