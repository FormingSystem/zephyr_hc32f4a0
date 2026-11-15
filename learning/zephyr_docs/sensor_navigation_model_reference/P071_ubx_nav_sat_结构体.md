---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-71
title: ubx_nav_sat_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__sat.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第71章\_ubx\_nav\_sat\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__nav__sat.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 71.1\_数据结构（Data Structures）

<a id="r_ubx_5Fnav_5Fsat_5Finfo"></a>

```c
struct ubx_nav_sat_info
```

相关声明：[ubx_nav_sat_info](P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 71.2\_数据成员（Data Fields）

<a id="r_aac587fd77fa832021ebca87e7897eb2e"></a>

```c
uint32_t itow
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[itow](#aac587fd77fa832021ebca87e7897eb2e)。

<a id="r_a7204f8b1b28f3dc0970fa62567885cdc"></a>

```c
uint8_t version
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[version](#a7204f8b1b28f3dc0970fa62567885cdc)。

<a id="r_ae0bea798d815cc25e837e3fa394fb429"></a>

```c
uint8_t num_sv
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[num_sv](#ae0bea798d815cc25e837e3fa394fb429)。

<a id="r_a6f5bf3da0f5633aa95ff4d736656cb21"></a>

```c
uint16_t reserved1
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved1](#a6f5bf3da0f5633aa95ff4d736656cb21)。

<a id="r_ade983d7b35cf81a6d769979f7cb5919d"></a>

```c
struct ubx_nav_sat::ubx_nav_sat_info sat []
```

相关声明：[ubx_nav_sat::ubx_nav_sat_info](P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)、[sat](#ade983d7b35cf81a6d769979f7cb5919d)。

## 71.3\_详细说明（Detailed Documentation）

<a id="aac587fd77fa832021ebca87e7897eb2e"></a>

### `itow`

```c
uint32_t ubx_nav_sat::itow
```

<a id="ae0bea798d815cc25e837e3fa394fb429"></a>

### `num_sv`

```c
uint8_t ubx_nav_sat::num_sv
```

<a id="a6f5bf3da0f5633aa95ff4d736656cb21"></a>

### `reserved1`

```c
uint16_t ubx_nav_sat::reserved1
```

<a id="ade983d7b35cf81a6d769979f7cb5919d"></a>

### `sat`

```c
struct ubx_nav_sat::ubx_nav_sat_info ubx_nav_sat::sat[]
```

<a id="a7204f8b1b28f3dc0970fa62567885cdc"></a>

### `version`

```c
uint8_t ubx_nav_sat::version
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 71.4\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [ubx_nav_sat_info](P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P070_ubx_nav_pvt_结构体.md) · [返回大纲](大纲.md) · [下一章](P072_ubx_nav_sat__ubx_nav_sat_info_结构体.md)
