---
id: learning.zephyr-docs.modem-wireless-model-reference.page-67
title: sim7080_sms_buffer_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__sms__buffer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第67章\_sim7080\_sms\_buffer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsim7080__sms__buffer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

短消息（SMS）读取操作的缓冲区结构。

```c
#include <zephyr/drivers/modem/simcom-sim7080.h>
```

<a id="details"></a>

短消息（SMS）读取操作的缓冲区结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 67.1\_数据成员（Data Fields）

<a id="r_a7477db7ff124999b95f50f3ae32aca6a"></a>

```c
struct sim7080_sms * sms
```

相关声明：[sim7080_sms](P066_sim7080_sms_结构体.md)、[sms](#a7477db7ff124999b95f50f3ae32aca6a)。

用于接收读取结果的短消息结构体。

<a id="r_a54e1885be2e809fd360738d11547b79f"></a>

```c
uint8_t nsms
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[nsms](#a54e1885be2e809fd360738d11547b79f)。

短消息结构体的数量。

## 67.2\_详细说明（Detailed Documentation）

<a id="a54e1885be2e809fd360738d11547b79f"></a>

### `nsms`

```c
uint8_t sim7080_sms_buffer::nsms
```

短消息结构体的数量。

<a id="a7477db7ff124999b95f50f3ae32aca6a"></a>

### `sms`

```c
struct sim7080_sms* sim7080_sms_buffer::sms
```

用于接收读取结果的短消息结构体。

本数据类型文档由以下文件生成：

- `zephyr/drivers/modem/simcom-sim7080.h`

## 67.3\_原页交叉引用（Cross References）

- [zephyr/drivers/modem/simcom-sim7080.h](https://docs.zephyrproject.org/latest/doxygen/html/simcom-sim7080_8h_source.html)
- [sim7080_sms](P066_sim7080_sms_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P066_sim7080_sms_结构体.md) · [返回大纲](大纲.md) · [下一章](P068_sim7080_ue_sys_info_结构体.md)
