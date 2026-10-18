---
id: learning.zephyr-docs.api-scoped-clock-topic-reference.page-9
title: 一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

支持自定义分隔符的 COBS 编码与解码函数。

<a id="details"></a>

支持自定义分隔符（Custom Delimiter）的固定开销字节填充（COBS）编码与解码函数。提供可配置分隔符的 COBS 编码／解码，既处理标准的零分隔 COBS，也处理自定义分隔符变体。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_cobs_2Eh"></a>

```c
file cobs.h
```

相关声明：[cobs.h](../api_file_protocol_service_reference/P009_zephyr__data__cobs.h_文件参考.md)。

固定开销字节填充（Consistent Overhead Byte Stuffing，COBS）编码API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.2\_数据结构（Data Structures）

<a id="r_cobs_5Fencoder"></a>

```c
struct cobs_encoder
```

相关声明：[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)。

固定开销字节填充（COBS）的流式编码器状态。

<a id="r_cobs_5Fdecoder"></a>

```c
struct cobs_decoder
```

相关声明：[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)。

固定开销字节填充（COBS）的流式解码器状态。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_gaf07cf3c33fd82490a8db4fa0f64bf906"></a>

```c
typedef int(* cobs_stream_cb) (const uint8_t *buf, size_t len, void *user_data)
```

相关声明：[cobs_stream_cb](#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流式 COBS 编码器／解码器（Streaming Encoder/Decoder）的回调函数类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_ga71047f135e408e95d83828e898e823b0"></a>

```c
static size_t cobs_max_encoded_len (size_t decoded_size, uint32_t flags)
```

相关声明：[cobs_max_encoded_len](#ga71047f135e408e95d83828e898e823b0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

计算编码缓冲区大小上限（Maximum Encoded Buffer Size）。

<a id="r_gadf39d47a13fe1e3b10bcc9208f5b4786"></a>

```c
int cobs_encode (struct net_buf *src, struct net_buf *dst, uint32_t flags)
```

相关声明：[cobs_encode](#gadf39d47a13fe1e3b10bcc9208f5b4786)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

COBS 编码（Encoding）。

<a id="r_gabb6193b8d15b33e5c739c9609376950f"></a>

```c
int cobs_decode (struct net_buf *src, struct net_buf *dst, uint32_t flags)
```

相关声明：[cobs_decode](#gabb6193b8d15b33e5c739c9609376950f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

COBS 解码（Decoding）。

<a id="r_gafebbd3ea1b058cf7834dd534048602fb"></a>

```c
int cobs_encoder_init (struct cobs_encoder *enc, cobs_stream_cb cb, void *user_data, uint32_t flags)
```

相关声明：[cobs_encoder_init](#gafebbd3ea1b058cf7834dd534048602fb)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)、[cobs_stream_cb](#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

初始化 COBS 流式编码器（Streaming Encoder）。

<a id="r_ga0b6ad6f90e70629f143c65f8dbe76a33"></a>

```c
int cobs_encoder_close (struct cobs_encoder *enc)
```

相关声明：[cobs_encoder_close](#ga0b6ad6f90e70629f143c65f8dbe76a33)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)。

完成 COBS 流式编码器的收尾（Finalize Streaming Encoder）。

<a id="r_ga88a7600ca21e3a160ed8354a5af0987b"></a>

```c
int cobs_encoder_write (struct cobs_encoder *enc, const uint8_t *buf, size_t len)
```

相关声明：[cobs_encoder_write](#ga88a7600ca21e3a160ed8354a5af0987b)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 COBS 流式编码器（Streaming Encoder）写入数据。

<a id="r_ga49fa5a2c541ac72c2a0fe89971bec38d"></a>

```c
int cobs_decoder_init (struct cobs_decoder *dec, cobs_stream_cb cb, void *user_data, uint32_t flags)
```

相关声明：[cobs_decoder_init](#ga49fa5a2c541ac72c2a0fe89971bec38d)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)、[cobs_stream_cb](#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

初始化 COBS 流式解码器（Streaming Decoder）。

<a id="r_gac50b6fd7bf9943429a4c0706350fcd76"></a>

```c
int cobs_decoder_close (struct cobs_decoder *dec)
```

相关声明：[cobs_decoder_close](#gac50b6fd7bf9943429a4c0706350fcd76)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)。

完成 COBS 流式解码器的收尾（Finalize Streaming Decoder）。

<a id="r_ga16669d639b1bdf7bc4a90190530ec2d9"></a>

```c
int cobs_decoder_write (struct cobs_decoder *dec, const uint8_t *buf, size_t len)
```

相关声明：[cobs_decoder_write](#ga16669d639b1bdf7bc4a90190530ec2d9)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 COBS 流式解码器（Streaming Decoder）写入数据。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 9.5\_COBS 编码器／解码器标志（Encoder/Decoder Flags）



<a id="r_ga67d201df9cea6c681ed537516dd1d35e"></a>

```c
#define COBS_DEFAULT_DELIMITER 0x00
```

相关声明：[COBS_DEFAULT_DELIMITER](#ga67d201df9cea6c681ed537516dd1d35e)。

一致开销字节填充（COBS）的默认分隔符值（Delimiter Value）。

<a id="r_ga016e001ca84dae52391b5bc22b5c92ad"></a>

```c
#define COBS_FLAG_TRAILING_DELIMITER BIT(8)
```

相关声明：[COBS_FLAG_TRAILING_DELIMITER](#ga016e001ca84dae52391b5bc22b5c92ad)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示编码或解码应包含尾部分隔符（Trailing Delimiter）的标志。

<a id="r_ga5e05dfb0ac63e51372805f2241c90491"></a>

```c
#define COBS_FLAG_CUSTOM_DELIMITER(x)
```

相关声明：[COBS_FLAG_CUSTOM_DELIMITER](#ga5e05dfb0ac63e51372805f2241c90491)。

在标志（Flags）中设置自定义分隔符（Custom Delimiter）的宏。

## 9.6\_详细说明（Detailed Documentation）

<a id="ga67d201df9cea6c681ed537516dd1d35e"></a>

### `COBS_DEFAULT_DELIMITER`

```c
#define COBS_DEFAULT_DELIMITER 0x00
```

```c
#include <zephyr/data/cobs.h>
```

一致开销字节填充（COBS）的默认分隔符值（Delimiter Value）。

标准 COBS 分隔符（Delimiter）为零（0x00）；未指定 COBS_FLAG_CUSTOM_DELIMITER 时，使用此值。

<a id="ga5e05dfb0ac63e51372805f2241c90491"></a>

### `COBS_FLAG_CUSTOM_DELIMITER`

```c
#define COBS_FLAG_CUSTOM_DELIMITER ( x)
```

```c
#include <zephyr/data/cobs.h>
```

展开值（Value）：

```c
((x) & 0xff)
```

在标志（Flags）中设置自定义分隔符（Custom Delimiter）的宏。

flags 的最低 8 位（8 LSB）用于存放分隔符值（Delimiter Value）。配置自定义分隔符后，实现会在编码完成后和解码开始前，将编码数据与分隔符值进行异或（XOR）运算，使 COBS 能够使用零以外的分隔符。

使用示例：

原始示例（Example）：

```c
cobs_encode(src_buf, dst_buf, COBS_FLAG_TRAILING_DELIMITER | COBS_FLAG_CUSTOM_DELIMITER(0x7F));
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 自定义分隔符值（Custom Delimiter Value），范围为 0–255。 |

返回（Returns）：经掩码保留为 8 位的分隔符值（Delimiter Value）。

<a id="ga016e001ca84dae52391b5bc22b5c92ad"></a>

### `COBS_FLAG_TRAILING_DELIMITER`

```c
#define COBS_FLAG_TRAILING_DELIMITER BIT(8)
```

```c
#include <zephyr/data/cobs.h>
```

表示编码或解码应包含尾部分隔符（Trailing Delimiter）的标志。

设置后，编码器（Encoder）在编码数据后追加一个分隔字节，解码器（Decoder）则接受编码数据末尾的分隔字节。

<a id="gaf07cf3c33fd82490a8db4fa0f64bf906"></a>

### `cobs_stream_cb`

```c
typedef int(* cobs_stream_cb) (const uint8_t *buf, size_t len, void *user_data)
```

```c
#include <zephyr/data/cobs.h>
```

流式 COBS 编码器／解码器（Streaming Encoder/Decoder）的回调函数类型。

流式编码器／解码器（Streaming Encoder/Decoder）调用此回调以输出已处理的数据块。允许尾部分隔符（Trailing Delimiter）的解码器遇到该分隔符时，会以 NULL 指针和零长度调用回调，表示一帧已完成。

此回调函数返回负错误值时，编码或解码流（Stream）被中止，错误向上传递。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 包含已处理数据（Processed Data）的缓冲区。 |
| `len` | 缓冲区中的数据长度（Data Length）。 |
| `user_data` | 用户提供的上下文指针（Context Pointer）。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gabb6193b8d15b33e5c739c9609376950f"></a>

### `cobs_decode()`

```c
int cobs_decode ( struct net_buf * src, struct net_buf * dst, uint32_t flags )
```

```c
#include <zephyr/data/cobs.h>
```

COBS 解码（Decoding）。

将源缓冲区中的 COBS 编码数据解码到目标缓冲区（Destination Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 待解码的源缓冲区（Source Buffer）。 |
| `dst` | 用于存放解码数据的目标缓冲区（Destination Buffer）。 |
| `flags` | 解码标志（Decoding Flags），参见 COBS_FLAGS。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 目标空间不足（Insufficient Destination Space）。 |
| `-EINVAL` | COBS 结构或参数无效（Invalid Structure or Parameters）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_NET_BUF 时可用。

<a id="gac50b6fd7bf9943429a4c0706350fcd76"></a>

### `cobs_decoder_close()`

```c
int cobs_decoder_close ( struct cobs_decoder * dec)
```

```c
#include <zephyr/data/cobs.h>
```

完成 COBS 流式解码器的收尾（Finalize Streaming Decoder）。

完成解码过程（Decoding Process），并验证流是否正确结束。应在全部数据写入解码器之后调用。

解码器状态（Decoder State）将被重置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dec` | 指向解码器结构体（Decoder Structure）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-EINVAL` | 关闭之前还预期有更多数据。 |

<a id="ga49fa5a2c541ac72c2a0fe89971bec38d"></a>

### `cobs_decoder_init()`

```c
int cobs_decoder_init ( struct cobs_decoder * dec, cobs_stream_cb cb, void * user_data, uint32_t flags )
```

```c
#include <zephyr/data/cobs.h>
```

初始化 COBS 流式解码器（Streaming Decoder）。

初始化用于流式操作（Streaming Operation）的 COBS 解码器。解码后的数据块一旦可用，解码器便调用所提供的回调函数输出它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dec` | 指向待初始化解码器结构体（Decoder Structure）的指针。 |
| `cb` | 输出数据的回调函数（Callback Function）。 |
| `user_data` | 传给回调的用户数据指针（User Data Pointer）。 |
| `flags` | 解码标志（Decoding Flags），参见 COBS_FLAGS。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga16669d639b1bdf7bc4a90190530ec2d9"></a>

### `cobs_decoder_write()`

```c
int cobs_decoder_write ( struct cobs_decoder * dec, const uint8_t * buf, size_t len )
```

```c
#include <zephyr/data/cobs.h>
```

向 COBS 流式解码器（Streaming Decoder）写入数据。

解码所提供的编码数据，并通过已注册回调函数输出解码后的数据块。可多次调用此函数，增量解码（Incremental Decoding）数据。

返回错误时，解码器状态（Decoder State）将被重置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dec` | 指向解码器结构体（Decoder Structure）的指针。 |
| `buf` | 包含编码数据（Encoded Data）的缓冲区。 |
| `len` | 缓冲区中的数据长度（Data Length）。 |

**说明（Note）**：注意（Note）：遇到分隔符（Delimiter）且设置了 COBS_FLAG_TRAILING_DELIMITER 标志时，将以 NULL 指针调用已注册的回调函数，表示帧结束（Frame End）。

返回（Returns）：成功时为从 buf 使用的字节数，失败时为负 errno 错误码。

<a id="gadf39d47a13fe1e3b10bcc9208f5b4786"></a>

### `cobs_encode()`

```c
int cobs_encode ( struct net_buf * src, struct net_buf * dst, uint32_t flags )
```

```c
#include <zephyr/data/cobs.h>
```

COBS 编码（Encoding）。

使用 COBS 编码（Encoding），将源缓冲区中的数据编码到目标缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src` | 待编码的源缓冲区（Source Buffer）。 |
| `dst` | 用于存放编码数据的目标缓冲区（Destination Buffer）。 |
| `flags` | 编码标志（Encoding Flags），参见 COBS_FLAGS。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOMEM` | 目标空间不足（Insufficient Destination Space）。 |
| `-EINVAL` | COBS 结构或参数无效（Invalid Structure or Parameters）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 CONFIG_NET_BUF 时可用。

<a id="ga0b6ad6f90e70629f143c65f8dbe76a33"></a>

### `cobs_encoder_close()`

```c
int cobs_encoder_close ( struct cobs_encoder * enc)
```

```c
#include <zephyr/data/cobs.h>
```

完成 COBS 流式编码器的收尾（Finalize Streaming Encoder）。

输出所有剩余数据；如果初始化时设置了 COBS_FLAG_TRAILING_DELIMITER，还会写入尾部分隔符（Trailing Delimiter）。

编码器状态（Encoder State）将被重置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enc` | 指向编码器结构体（Encoder Structure）的指针。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="gafebbd3ea1b058cf7834dd534048602fb"></a>

### `cobs_encoder_init()`

```c
int cobs_encoder_init ( struct cobs_encoder * enc, cobs_stream_cb cb, void * user_data, uint32_t flags )
```

```c
#include <zephyr/data/cobs.h>
```

初始化 COBS 流式编码器（Streaming Encoder）。

初始化用于流式操作（Streaming Operation）的 COBS 编码器。编码后的数据块一旦可用，编码器便调用所提供的回调函数输出它们。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enc` | 指向待初始化编码器结构体（Encoder Structure）的指针。 |
| `cb` | 输出数据的回调函数（Callback Function）。 |
| `user_data` | 传给回调的用户数据指针（User Data Pointer）。 |
| `flags` | 编码标志（Encoding Flags），参见 COBS_FLAGS。 |

**返回（Returns）**：返回值：成功时返回 0，失败时返回负 `errno` 错误码。

<a id="ga88a7600ca21e3a160ed8354a5af0987b"></a>

### `cobs_encoder_write()`

```c
int cobs_encoder_write ( struct cobs_encoder * enc, const uint8_t * buf, size_t len )
```

```c
#include <zephyr/data/cobs.h>
```

向 COBS 流式编码器（Streaming Encoder）写入数据。

编码所提供的数据，并通过已注册回调函数输出编码后的数据块。可多次调用此函数，增量编码（Incremental Encoding）数据。

返回错误时，编码器状态（Encoder State）将被重置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `enc` | 指向编码器结构体（Encoder Structure）的指针。 |
| `buf` | 包含待编码数据的缓冲区（Buffer）。 |
| `len` | 缓冲区中的数据长度（Data Length）。 |

返回（Returns）：成功时为从 buf 使用的字节数，失败时为负 errno 错误码。

<a id="ga71047f135e408e95d83828e898e823b0"></a>

### `cobs_max_encoded_len()`

```c
size_t cobs_max_encoded_len ( size_t decoded_size, uint32_t flags )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/data/cobs.h>
```

计算编码缓冲区大小上限（Maximum Encoded Buffer Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `decoded_size` | 要编码的输入数据大小（Input Data Size）。 |
| `flags` | 编码标志（Encoding Flags），参见 COBS_FLAGS。 |

返回（Returns）：最坏编码情形（Worst-case Encoding Scenario）所需的缓冲区大小。


## 9.7\_原页交叉引用（Cross References）

- [cobs.h](../api_file_protocol_service_reference/P009_zephyr__data__cobs.h_文件参考.md)
- [cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)
- [cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [CONFIG_NET_BUF](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF)

<a id="COBS_FLAGS"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__cobs_html_ga016e001ca84dae52391b5bc22b5c92ad"></a>
<a id="agroup__cobs_html_ga5e05dfb0ac63e51372805f2241c90491"></a>
<a id="agroup__cobs_html_gadf39d47a13fe1e3b10bcc9208f5b4786"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_Nordic nRF API主题.md) · [返回大纲](大纲.md) · [下一章](P010_FT8xx 协处理器（Co-processor）.md)
