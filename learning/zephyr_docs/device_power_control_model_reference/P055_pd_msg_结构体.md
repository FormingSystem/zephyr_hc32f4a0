---
id: learning.zephyr-docs.device-power-control-model-reference.page-55
title: pd_msg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpd__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_pd\_msg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpd__msg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

电力传输消息（Power Delivery Message）。

```c
#include <zephyr/drivers/usb_c/usbc_pd.h>
```

<a id="details"></a>

电力传输消息（Power Delivery Message）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 55.1\_数据成员（Data Fields）

<a id="r_af9f676afd2c2824fb9f01a08d8339231"></a>

```c
enum pd_packet_type type
```

相关声明：[pd_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad2df13a24f0365198d37b10af608376b)、[type](#af9f676afd2c2824fb9f01a08d8339231)。

此数据包的类型。

<a id="r_ae6f1fa8a1fb006e3d90e75cd834e6d05"></a>

```c
union pd_header header
```

相关声明：[pd_header](P114_pd_header_联合体.md)、[header](#ae6f1fa8a1fb006e3d90e75cd834e6d05)。

此消息的头部（Header）。

<a id="r_aa03ec4ce6d2f0d16a829394ff0ed2688"></a>

```c
uint32_t len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[len](#aa03ec4ce6d2f0d16a829394ff0ed2688)。

`data` 中数据的字节数。

<a id="r_ad6fd282617b5f6dfeeef6cf4598883ee"></a>

```c
uint8_t data [260]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ad6fd282617b5f6dfeeef6cf4598883ee)。

消息数据。

## 55.2\_详细说明（Detailed Documentation）

<a id="ad6fd282617b5f6dfeeef6cf4598883ee"></a>

### `data`

```c
uint8_t pd_msg::data[260]
```

消息数据。

<a id="ae6f1fa8a1fb006e3d90e75cd834e6d05"></a>

### `header`

```c
union pd_header pd_msg::header
```

此消息的头部（Header）。

<a id="aa03ec4ce6d2f0d16a829394ff0ed2688"></a>

### `len`

```c
uint32_t pd_msg::len
```

`data` 中数据的字节数。

<a id="af9f676afd2c2824fb9f01a08d8339231"></a>

### `type`

```c
enum pd_packet_type pd_msg::type
```

此数据包的类型。

本数据类型文档由以下文件生成：

- `zephyr/drivers/usb_c/usbc_pd.h`

## 55.3\_原页交叉引用（Cross References）

- [zephyr/drivers/usb_c/usbc_pd.h](https://docs.zephyrproject.org/latest/doxygen/html/usbc__pd_8h_source.html)
- [pd_packet_type](https://docs.zephyrproject.org/latest/doxygen/html/group__usb__power__delivery.html#gad2df13a24f0365198d37b10af608376b)
- [pd_header](P114_pd_header_联合体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P054_numicro_scc_subsys_pcc_结构体.md) · [返回大纲](大纲.md) · [下一章](P056_pfc_bias_reg_结构体.md)
