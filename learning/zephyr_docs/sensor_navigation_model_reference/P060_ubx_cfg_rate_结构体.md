---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-60
title: ubx_cfg_rate_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__rate.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第60章\_ubx\_cfg\_rate\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__cfg__rate.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 60.1\_数据成员（Data Fields）

<a id="r_ae64d779c4a3fe255710be8f742f5b6c6"></a>

```c
uint16_t meas_rate_ms
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[meas_rate_ms](#ae64d779c4a3fe255710be8f742f5b6c6)。

<a id="r_aafcbb36f844534c77e698dceccb2f5dc"></a>

```c
uint16_t nav_rate
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[nav_rate](#aafcbb36f844534c77e698dceccb2f5dc)。

<a id="r_a444822a3a37dd51313bfc6968a3b4721"></a>

```c
uint16_t time_ref
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[time_ref](#a444822a3a37dd51313bfc6968a3b4721)。

## 60.2\_详细说明（Detailed Documentation）

<a id="ae64d779c4a3fe255710be8f742f5b6c6"></a>

### `meas_rate_ms`

```c
uint16_t ubx_cfg_rate::meas_rate_ms
```

<a id="aafcbb36f844534c77e698dceccb2f5dc"></a>

### `nav_rate`

```c
uint16_t ubx_cfg_rate::nav_rate
```

<a id="a444822a3a37dd51313bfc6968a3b4721"></a>

### `time_ref`

```c
uint16_t ubx_cfg_rate::time_ref
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 60.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P059_ubx_cfg_prt_结构体.md) · [返回大纲](大纲.md) · [下一章](P061_ubx_cfg_rst_结构体.md)
