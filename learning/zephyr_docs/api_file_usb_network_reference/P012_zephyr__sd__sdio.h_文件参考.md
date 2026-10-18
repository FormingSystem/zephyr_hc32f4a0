---
id: learning.zephyr-docs.api-file-usb-network-reference.page-12
title: zephyr__sd__sdio.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_zephyr\_\_sd\_\_sdio.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sdio_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全数字输入输出（SDIO）子系统的公共API。

<a id="details"></a>

```c
#include <zephyr/device.h>
#include <zephyr/drivers/sdhc.h>
#include <zephyr/sd/sd.h>
```

查看此文件的源码。

安全数字输入输出（SDIO）子系统的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 12.1\_函数（Functions）

<a id="r_aae010680d9035116f503d7ddc1cf8590"></a>

```c
int sdio_init_func (struct sd_card *card, struct sdio_func *func, enum sdio_func_num num)
```

相关声明：[sdio_init_func](#aae010680d9035116f503d7ddc1cf8590)、[sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[sdio_func_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6)。

初始化 SDIO 功能（SDIO Function）。

<a id="r_aa3e60d2c643cd054af56cb44d193074b"></a>

```c
int sdio_enable_func (struct sdio_func *func)
```

相关声明：[sdio_enable_func](#aa3e60d2c643cd054af56cb44d193074b)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)。

启用 SDIO 功能（SDIO Function）。

<a id="r_a417829a0558b236465b70ff637a7ca38"></a>

```c
int sdio_set_block_size (struct sdio_func *func, uint16_t bsize)
```

相关声明：[sdio_set_block_size](#a417829a0558b236465b70ff637a7ca38)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 SDIO 功能的块大小（Block Size）。

<a id="r_a2ac93072041651597b9027156706f0d0"></a>

```c
int sdio_read_byte (struct sdio_func *func, uint32_t reg, uint8_t *val)
```

相关声明：[sdio_read_byte](#a2ac93072041651597b9027156706f0d0)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从 SDIO 寄存器（SDIO Register）读取一个字节。

<a id="r_a9bfb4970e28830151d2a293475b98435"></a>

```c
int sdio_write_byte (struct sdio_func *func, uint32_t reg, uint8_t write_val)
```

相关声明：[sdio_write_byte](#a9bfb4970e28830151d2a293475b98435)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SDIO 寄存器（SDIO Register）写入一个字节。

<a id="r_a8fbc927607a156abc4c47bc551f72b11"></a>

```c
int sdio_rw_byte (struct sdio_func *func, uint32_t reg, uint8_t write_val, uint8_t *read_val)
```

相关声明：[sdio_rw_byte](#a8fbc927607a156abc4c47bc551f72b11)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 SDIO 寄存器（SDIO Register）写入一个字节，并读取结果。

<a id="r_a8cf3af67ef909dd93cdfec29250d76c6"></a>

```c
int sdio_read_fifo (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t len)
```

相关声明：[sdio_read_fifo](#a8cf3af67ef909dd93cdfec29250d76c6)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SDIO 先进先出队列（FIFO）读取字节。

<a id="r_a5beb64599a265b117a42858e8087ae4a"></a>

```c
int sdio_write_fifo (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t len)
```

相关声明：[sdio_write_fifo](#a5beb64599a265b117a42858e8087ae4a)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 SDIO 先进先出队列（FIFO）写入字节。

<a id="r_ab7ec658d92672acfa36d073191d0369f"></a>

```c
int sdio_read_blocks_fifo (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t blocks)
```

相关声明：[sdio_read_blocks_fifo](#ab7ec658d92672acfa36d073191d0369f)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SDIO 先进先出队列（FIFO）读取数据块。

<a id="r_a68f75f10ea65cef4bc650b6e2ec4001d"></a>

```c
int sdio_write_blocks_fifo (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t blocks)
```

相关声明：[sdio_write_blocks_fifo](#a68f75f10ea65cef4bc650b6e2ec4001d)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 SDIO 先进先出队列（FIFO）写入数据块。

<a id="r_a341c846c55adf512a4c3397f38d4bbf9"></a>

```c
int sdio_read_addr (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t len)
```

相关声明：[sdio_read_addr](#a341c846c55adf512a4c3397f38d4bbf9)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 SDIO 卡复制字节。

<a id="r_a55bd42c4d41643444890227ee6cbbfc5"></a>

```c
int sdio_write_addr (struct sdio_func *func, uint32_t reg, uint8_t *data, uint32_t len)
```

相关声明：[sdio_write_addr](#a55bd42c4d41643444890227ee6cbbfc5)、[sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 SDIO 卡复制字节。

## 12.2\_详细说明（Detailed Documentation）

<a id="aa3e60d2c643cd054af56cb44d193074b"></a>

### `sdio_enable_func()`

```c
int sdio_enable_func ( struct sdio_func * func)
```

启用 SDIO 功能（SDIO Function）。

启用 SDIO 卡功能（Card Function）。在卡中启用该功能之前，必须先调用 `sdio_init_func` 初始化功能结构体（Function Structure）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要启用的功能（Function）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功启用该功能（Function）。 |
| `-ETIMEDOUT` | 卡的输入／输出（I/O）操作超时。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="aae010680d9035116f503d7ddc1cf8590"></a>

### `sdio_init_func()`

```c
int sdio_init_func ( struct sd_card * card, struct sdio_func * func, enum sdio_func_num num )
```

初始化 SDIO 功能（SDIO Function）。

初始化 SDIO 卡功能（Card Function）。此操作不会启用卡功能，但调用返回后即可使用 SDIO 功能结构体（Function Structure）读写卡中的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要初始化的功能结构体（Function Structure）。 |
| `card` | 要在其上启用该功能（Function）的 SD 卡。 |
| `num` | 要初始化的功能编号（Function Number）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 已成功初始化该功能（Function）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a341c846c55adf512a4c3397f38d4bbf9"></a>

### `sdio_read_addr()`

```c
int sdio_read_addr ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t len )
```

从 SDIO 卡复制字节。

从提供的地址开始，自 SDIO 卡复制字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要从中读取的功能（Function）。 |
| `reg` | 开始复制的寄存器地址（Register Address）。 |
| `data` | 用于接收复制数据的缓冲区（Buffer）。 |
| `len` | 要读取的数据长度（Data Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡读取超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="ab7ec658d92672acfa36d073191d0369f"></a>

### `sdio_read_blocks_fifo()`

```c
int sdio_read_blocks_fifo ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t blocks )
```

从 SDIO 先进先出队列（FIFO）读取数据块。

将 SDIO 寄存器视为先进先出队列（FIFO），从中读取数据块。所有读取操作均使用同一地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要从中读取的功能（Function）。 |
| `reg` | FIFO 的寄存器地址（Register Address）。 |
| `data` | 填入从 FIFO 读取的数据。 |
| `blocks` | 要从 FIFO 读取的数据块数量（Number of Blocks）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡读取超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a2ac93072041651597b9027156706f0d0"></a>

### `sdio_read_byte()`

```c
int sdio_read_byte ( struct sdio_func * func, uint32_t reg, uint8_t * val )
```

从 SDIO 寄存器（SDIO Register）读取一个字节。

从 SDIO 寄存器（SDIO Register）读取一个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要从中读取的功能（Function）。 |
| `reg` | 要读取的寄存器地址（register address）。 |
| `val` | 填入从寄存器读取的字节值（Byte Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡读取超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a8cf3af67ef909dd93cdfec29250d76c6"></a>

### `sdio_read_fifo()`

```c
int sdio_read_fifo ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t len )
```

从 SDIO 先进先出队列（FIFO）读取字节。

将 SDIO 寄存器视为先进先出队列（FIFO），从中读取字节。所有读取操作均使用同一地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要从中读取的功能（Function）。 |
| `reg` | FIFO 的寄存器地址（Register Address）。 |
| `data` | 填入从 FIFO 读取的数据。 |
| `len` | 要从卡中读取的数据长度（Data Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 读取成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡读取超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a8fbc927607a156abc4c47bc551f72b11"></a>

### `sdio_rw_byte()`

```c
int sdio_rw_byte ( struct sdio_func * func, uint32_t reg, uint8_t write_val, uint8_t * read_val )
```

向 SDIO 寄存器（SDIO Register）写入一个字节，并读取结果。

向 SDIO 寄存器（SDIO Register）写入一个字节，并在写入后读取该寄存器。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要写入的功能（Function）。 |
| `reg` | 要写入的寄存器地址。 |
| `write_val` | 要写入寄存器的值（Value）。 |
| `read_val` | 填入从寄存器读取的值（Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a417829a0558b236465b70ff637a7ca38"></a>

### `sdio_set_block_size()`

```c
int sdio_set_block_size ( struct sdio_func * func, uint16_t bsize )
```

设置 SDIO 功能的块大小（Block Size）。

为 SDIO 功能设置所需块大小（Block Size），用于对 SDIO 寄存器进行块传输（Block Transfer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要设置块大小（Block Size）的功能（Function）。 |
| `bsize` | 块大小（Block Size）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 块大小（Block Size）已设置。 |
| `-EINVAL` | 块大小（Block Size）不受支持或无效。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a55bd42c4d41643444890227ee6cbbfc5"></a>

### `sdio_write_addr()`

```c
int sdio_write_addr ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t len )
```

向 SDIO 卡复制字节。

从提供的地址开始，向 SDIO 卡复制字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要写入的功能（Function）。 |
| `reg` | 开始复制的寄存器地址（Register Address）。 |
| `data` | 作为复制数据来源的缓冲区（Buffer）。 |
| `len` | 要写入的数据长度（Data Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a68f75f10ea65cef4bc650b6e2ec4001d"></a>

### `sdio_write_blocks_fifo()`

```c
int sdio_write_blocks_fifo ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t blocks )
```

向 SDIO 先进先出队列（FIFO）写入数据块。

将 SDIO 寄存器视为先进先出队列（FIFO），向其写入数据块。所有写入操作均使用同一地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要写入的功能（Function）。 |
| `reg` | FIFO 的寄存器地址（Register Address）。 |
| `data` | 要写入 FIFO 的数据。 |
| `blocks` | 要写入 FIFO 的数据块数量（Number of Blocks）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a9bfb4970e28830151d2a293475b98435"></a>

### `sdio_write_byte()`

```c
int sdio_write_byte ( struct sdio_func * func, uint32_t reg, uint8_t write_val )
```

向 SDIO 寄存器（SDIO Register）写入一个字节。

向 SDIO 寄存器（SDIO Register）写入一个字节。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要写入的功能（Function）。 |
| `reg` | 要写入的寄存器地址。 |
| `write_val` | 要写入寄存器的值（Value）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |

<a id="a5beb64599a265b117a42858e8087ae4a"></a>

### `sdio_write_fifo()`

```c
int sdio_write_fifo ( struct sdio_func * func, uint32_t reg, uint8_t * data, uint32_t len )
```

向 SDIO 先进先出队列（FIFO）写入字节。

将 SDIO 寄存器视为先进先出队列（FIFO），向其写入字节。所有写入操作均使用同一地址。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `func` | 要写入的功能（Function）。 |
| `reg` | FIFO 的寄存器地址（Register Address）。 |
| `data` | 要写入 FIFO 的数据。 |
| `len` | 要写入卡的数据长度（Data Length）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 写入成功。 |
| `-EBUSY` | 卡正忙于另一请求。 |
| `-ETIMEDOUT` | 卡写入超时（Timed Out）。 |
| `-EIO` | 输入／输出错误（I/O Error）。 |


## 12.3\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/sdhc.h](../peripheral_bus_storage_source_reference/P025_zephyr__drivers__sdhc.h_头文件源码.md)
- [zephyr/sd/sd.h](../peripheral_bus_storage_source_reference/P024_zephyr__sd__sd.h_头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P750_sdio.h_源码浏览.md)
- [sd_card](../peripheral_bus_storage_model_reference/P074_sd_card_结构体.md)
- [sdio_func](../peripheral_bus_storage_model_reference/P086_sdio_func_结构体.md)
- [sdio_func_num](../peripheral_bus_storage_header_reference/P015_zephyr__sd__sd_spec.h_头文件参考.md#a3a542344967c5c1912bde216559e7cd6)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P011_zephyr__drivers__clock_control__renesas_ra_cgc.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P013_zephyr__sip_svc__sip_svc.h_文件参考.md)
