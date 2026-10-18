---
id: learning.zephyr-docs.bluetooth-connection-model-reference.page-111
title: bt_le_oob_sc_data_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__oob__sc__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第111章\_bt\_le\_oob\_sc\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__le__oob__sc__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

低功耗蓝牙安全连接（LE Secure Connections）配对使用的带外（Out of Band，OOB）数据。

```c
#include <zephyr/bluetooth/bluetooth.h>
```

<a id="details"></a>

低功耗蓝牙安全连接（LE Secure Connections）配对使用的带外（Out of Band，OOB）数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 111.1\_数据成员（Data Fields）

<a id="r_afa64bcc048d0e8709e262e2848a39d2c"></a>

```c
uint8_t r [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[r](#afa64bcc048d0e8709e262e2848a39d2c)。

随机数（Random Number）。

<a id="r_a9bd93f1e9e41e241d0f84ae16ae47ba1"></a>

```c
uint8_t c [16]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[c](#a9bd93f1e9e41e241d0f84ae16ae47ba1)。

确认值（Confirm Value）。

## 111.2\_详细说明（Detailed Documentation）

<a id="a9bd93f1e9e41e241d0f84ae16ae47ba1"></a>

### `c`

```c
uint8_t bt_le_oob_sc_data::c[16]
```

确认值（Confirm Value）。

<a id="afa64bcc048d0e8709e262e2848a39d2c"></a>

### `r`

```c
uint8_t bt_le_oob_sc_data::r[16]
```

随机数（Random Number）。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/bluetooth.h`

## 111.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/bluetooth.h](https://docs.zephyrproject.org/latest/doxygen/html/bluetooth_2bluetooth_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P110_bt_le_oob_结构体.md) · [返回大纲](大纲.md) · [下一章](P112_bt_le_per_adv_data_request_结构体.md)
