---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-64
title: ubx_cfg_val_u32_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u32.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第64章\_ubx\_cfg\_val\_u32\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__val__u32.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 64.1\_数据成员（Data Fields）

<a id="r_adc51df7bc8a50e1ca8843067bb309ac9"></a>

```c
struct ubx_cfg_val_hdr hdr
```

相关声明：[ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)、[hdr](#adc51df7bc8a50e1ca8843067bb309ac9)。

<a id="r_ab02aa8d3b7039c06692a805aed30f246"></a>

```c
uint32_t key
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[key](#ab02aa8d3b7039c06692a805aed30f246)。

<a id="r_a2c1d446c7c8bef80052d2438fb998d58"></a>

```c
uint32_t value
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[value](#a2c1d446c7c8bef80052d2438fb998d58)。

## 64.2\_详细说明（Detailed Documentation）

<a id="adc51df7bc8a50e1ca8843067bb309ac9"></a>

### `hdr`

```c
struct ubx_cfg_val_hdr ubx_cfg_val_u32::hdr
```

<a id="ab02aa8d3b7039c06692a805aed30f246"></a>

### `key`

```c
uint32_t ubx_cfg_val_u32::key
```

<a id="a2c1d446c7c8bef80052d2438fb998d58"></a>

### `value`

```c
uint32_t ubx_cfg_val_u32::value
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 64.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [ubx_cfg_val_hdr](P062_ubx_cfg_val_hdr_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P063_ubx_cfg_val_u16_结构体.md) · [返回大纲](大纲.md) · [下一章](P065_ubx_cfg_val_u8_结构体.md)
