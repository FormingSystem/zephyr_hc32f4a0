---
id: learning.zephyr-docs.modem-wireless-model-reference.page-44
title: modem_backend_uart_async_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__async.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第44章\_modem\_backend\_uart\_async\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__backend__uart__async.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/backend/uart.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 44.1\_数据成员（Data Fields）

<a id="r_a8c186bed442db94aa84bf76ad3253fc2"></a>

```c
struct modem_backend_uart_async_common common
```

相关声明：[modem_backend_uart_async_common](P045_modem_backend_uart_async_common_结构体.md)、[common](#a8c186bed442db94aa84bf76ad3253fc2)。

<a id="r_a8e6ff3cae3a79e8b26e67282bb50f5ad"></a>

```c
uint8_t * receive_bufs [2]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_bufs](#a8e6ff3cae3a79e8b26e67282bb50f5ad)。

<a id="r_a85e0e51366bbb2e1d7a72e0b9a0650ee"></a>

```c
uint32_t receive_buf_size
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[receive_buf_size](#a85e0e51366bbb2e1d7a72e0b9a0650ee)。

<a id="r_ac3909d735bfecac46001f1b289e222a2"></a>

```c
struct ring_buf receive_rb
```

相关声明：[ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)、[receive_rb](#ac3909d735bfecac46001f1b289e222a2)。

<a id="r_ab61b263cdbe9bfb796f3dd6ed69b3dea"></a>

```c
struct k_spinlock receive_rb_lock
```

相关声明：[k_spinlock](../kernel/P066_自旋锁结构参考.md)、[receive_rb_lock](#ab61b263cdbe9bfb796f3dd6ed69b3dea)。

## 44.2\_详细说明（Detailed Documentation）

<a id="a8c186bed442db94aa84bf76ad3253fc2"></a>

### `common`

```c
struct modem_backend_uart_async_common modem_backend_uart_async::common
```

<a id="a85e0e51366bbb2e1d7a72e0b9a0650ee"></a>

### `receive_buf_size`

```c
uint32_t modem_backend_uart_async::receive_buf_size
```

<a id="a8e6ff3cae3a79e8b26e67282bb50f5ad"></a>

### `receive_bufs`

```c
uint8_t* modem_backend_uart_async::receive_bufs[2]
```

<a id="ac3909d735bfecac46001f1b289e222a2"></a>

### `receive_rb`

```c
struct ring_buf modem_backend_uart_async::receive_rb
```

<a id="ab61b263cdbe9bfb796f3dd6ed69b3dea"></a>

### `receive_rb_lock`

```c
struct k_spinlock modem_backend_uart_async::receive_rb_lock
```

本数据类型文档由以下文件生成：

- `zephyr/modem/backend/uart.h`

## 44.3\_原页交叉引用（Cross References）

- [zephyr/modem/backend/uart.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2backend_2uart_8h_source.html)
- [modem_backend_uart_async_common](P045_modem_backend_uart_async_common_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P043_modem_backend_uart_结构体.md) · [返回大纲](大纲.md) · [下一章](P045_modem_backend_uart_async_common_结构体.md)
