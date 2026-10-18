---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-9
title: zephyr__data__cobs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_zephyr\_\_data\_\_cobs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/cobs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

固定开销字节填充（Consistent Overhead Byte Stuffing，COBS）编码API的头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <sys/types.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

固定开销字节填充（Consistent Overhead Byte Stuffing，COBS）编码API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

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

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="define-members-0"></a>

### COBS 编码器／解码器标志（Encoder/Decoder Flags）



<a id="r_ga67d201df9cea6c681ed537516dd1d35e"></a>

```c
#define COBS_DEFAULT_DELIMITER 0x00
```

相关声明：[COBS_DEFAULT_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga67d201df9cea6c681ed537516dd1d35e)。

一致开销字节填充（COBS）的默认分隔符值（Delimiter Value）。

<a id="r_ga016e001ca84dae52391b5bc22b5c92ad"></a>

```c
#define COBS_FLAG_TRAILING_DELIMITER BIT(8)
```

相关声明：[COBS_FLAG_TRAILING_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga016e001ca84dae52391b5bc22b5c92ad)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

表示编码或解码应包含尾部分隔符（Trailing Delimiter）的标志。

<a id="r_ga5e05dfb0ac63e51372805f2241c90491"></a>

```c
#define COBS_FLAG_CUSTOM_DELIMITER(x)
```

相关声明：[COBS_FLAG_CUSTOM_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga5e05dfb0ac63e51372805f2241c90491)。

在标志（Flags）中设置自定义分隔符（Custom Delimiter）的宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_gaf07cf3c33fd82490a8db4fa0f64bf906"></a>

```c
typedef int(* cobs_stream_cb) (const uint8_t *buf, size_t len, void *user_data)
```

相关声明：[cobs_stream_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

流式 COBS 编码器／解码器（Streaming Encoder/Decoder）的回调函数类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.4\_函数（Functions）

<a id="r_ga71047f135e408e95d83828e898e823b0"></a>

```c
static size_t cobs_max_encoded_len (size_t decoded_size, uint32_t flags)
```

相关声明：[cobs_max_encoded_len](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga71047f135e408e95d83828e898e823b0)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

计算编码缓冲区大小上限（Maximum Encoded Buffer Size）。

<a id="r_gadf39d47a13fe1e3b10bcc9208f5b4786"></a>

```c
int cobs_encode (struct net_buf *src, struct net_buf *dst, uint32_t flags)
```

相关声明：[cobs_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gadf39d47a13fe1e3b10bcc9208f5b4786)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

COBS 编码（Encoding）。

<a id="r_gabb6193b8d15b33e5c739c9609376950f"></a>

```c
int cobs_decode (struct net_buf *src, struct net_buf *dst, uint32_t flags)
```

相关声明：[cobs_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gabb6193b8d15b33e5c739c9609376950f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

COBS 解码（Decoding）。

<a id="r_gafebbd3ea1b058cf7834dd534048602fb"></a>

```c
int cobs_encoder_init (struct cobs_encoder *enc, cobs_stream_cb cb, void *user_data, uint32_t flags)
```

相关声明：[cobs_encoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gafebbd3ea1b058cf7834dd534048602fb)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)、[cobs_stream_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

初始化 COBS 流式编码器（Streaming Encoder）。

<a id="r_ga0b6ad6f90e70629f143c65f8dbe76a33"></a>

```c
int cobs_encoder_close (struct cobs_encoder *enc)
```

相关声明：[cobs_encoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga0b6ad6f90e70629f143c65f8dbe76a33)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)。

完成 COBS 流式编码器的收尾（Finalize Streaming Encoder）。

<a id="r_ga88a7600ca21e3a160ed8354a5af0987b"></a>

```c
int cobs_encoder_write (struct cobs_encoder *enc, const uint8_t *buf, size_t len)
```

相关声明：[cobs_encoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga88a7600ca21e3a160ed8354a5af0987b)、[cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 COBS 流式编码器（Streaming Encoder）写入数据。

<a id="r_ga49fa5a2c541ac72c2a0fe89971bec38d"></a>

```c
int cobs_decoder_init (struct cobs_decoder *dec, cobs_stream_cb cb, void *user_data, uint32_t flags)
```

相关声明：[cobs_decoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga49fa5a2c541ac72c2a0fe89971bec38d)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)、[cobs_stream_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gaf07cf3c33fd82490a8db4fa0f64bf906)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

初始化 COBS 流式解码器（Streaming Decoder）。

<a id="r_gac50b6fd7bf9943429a4c0706350fcd76"></a>

```c
int cobs_decoder_close (struct cobs_decoder *dec)
```

相关声明：[cobs_decoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gac50b6fd7bf9943429a4c0706350fcd76)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)。

完成 COBS 流式解码器的收尾（Finalize Streaming Decoder）。

<a id="r_ga16669d639b1bdf7bc4a90190530ec2d9"></a>

```c
int cobs_decoder_write (struct cobs_decoder *dec, const uint8_t *buf, size_t len)
```

相关声明：[cobs_decoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga16669d639b1bdf7bc4a90190530ec2d9)、[cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向 COBS 流式解码器（Streaming Decoder）写入数据。


## 9.5\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P031_cobs.h_源码浏览.md)
- [cobs_encoder](../system_service_model_reference/P004_cobs_encoder_结构体.md)
- [cobs_decoder](../system_service_model_reference/P003_cobs_decoder_结构体.md)
- [COBS_DEFAULT_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga67d201df9cea6c681ed537516dd1d35e)
- [COBS_FLAG_TRAILING_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga016e001ca84dae52391b5bc22b5c92ad)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [COBS_FLAG_CUSTOM_DELIMITER](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga5e05dfb0ac63e51372805f2241c90491)
- [cobs_stream_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gaf07cf3c33fd82490a8db4fa0f64bf906)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cobs_max_encoded_len](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga71047f135e408e95d83828e898e823b0)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [标志（Flags）。](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [cobs_encode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gadf39d47a13fe1e3b10bcc9208f5b4786)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [cobs_decode](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gabb6193b8d15b33e5c739c9609376950f)
- [cobs_encoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gafebbd3ea1b058cf7834dd534048602fb)
- [cobs_encoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga0b6ad6f90e70629f143c65f8dbe76a33)
- [cobs_encoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga88a7600ca21e3a160ed8354a5af0987b)
- [cobs_decoder_init](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga49fa5a2c541ac72c2a0fe89971bec38d)
- [cobs_decoder_close](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#gac50b6fd7bf9943429a4c0706350fcd76)
- [cobs_decoder_write](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html#ga16669d639b1bdf7bc4a90190530ec2d9)

<a id="COBS_FLAGS"></a>
<a id="header-details"></a>

---

[上一章](P008_zephyr__net__coap_client.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_zephyr__audio__dmic.h_文件参考.md)
