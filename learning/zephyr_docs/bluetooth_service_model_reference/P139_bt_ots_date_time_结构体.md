---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-139
title: bt_ots_date_time_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__date__time.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第139章\_bt\_ots\_date\_time\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__date__time.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

日期与时间（Date and Time）结构。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

日期与时间（Date and Time）结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 139.1\_数据成员（Data Fields）

<a id="r_af348ad2613ba309de6a93d357bcce3bc"></a>

```c
uint16_t year
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[year](#af348ad2613ba309de6a93d357bcce3bc)。

<a id="r_ac3959eac8188df6114d70aed1ccbf3f4"></a>

```c
uint8_t month
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[month](#ac3959eac8188df6114d70aed1ccbf3f4)。

<a id="r_a09ca928752dc844e89de3957d1baae3c"></a>

```c
uint8_t day
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[day](#a09ca928752dc844e89de3957d1baae3c)。

<a id="r_ae139a310b4d17078f52bfbe7707e185a"></a>

```c
uint8_t hours
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[hours](#ae139a310b4d17078f52bfbe7707e185a)。

<a id="r_acc118b311bfdcb3c2f7801121831fcd6"></a>

```c
uint8_t minutes
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[minutes](#acc118b311bfdcb3c2f7801121831fcd6)。

<a id="r_a4eb6899dbce61478b97025958c62f586"></a>

```c
uint8_t seconds
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[seconds](#a4eb6899dbce61478b97025958c62f586)。

## 139.2\_详细说明（Detailed Documentation）

<a id="a09ca928752dc844e89de3957d1baae3c"></a>

### `day`

```c
uint8_t bt_ots_date_time::day
```

<a id="ae139a310b4d17078f52bfbe7707e185a"></a>

### `hours`

```c
uint8_t bt_ots_date_time::hours
```

<a id="acc118b311bfdcb3c2f7801121831fcd6"></a>

### `minutes`

```c
uint8_t bt_ots_date_time::minutes
```

<a id="ac3959eac8188df6114d70aed1ccbf3f4"></a>

### `month`

```c
uint8_t bt_ots_date_time::month
```

<a id="a4eb6899dbce61478b97025958c62f586"></a>

### `seconds`

```c
uint8_t bt_ots_date_time::seconds
```

<a id="af348ad2613ba309de6a93d357bcce3bc"></a>

### `year`

```c
uint16_t bt_ots_date_time::year
```

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 139.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P138_bt_ots_client_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P140_bt_ots_feat_结构体.md)
