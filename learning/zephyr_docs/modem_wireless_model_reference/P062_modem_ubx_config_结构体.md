---
id: learning.zephyr-docs.modem-wireless-model-reference.page-62
title: modem_ubx_config_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__config.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第62章\_modem\_ubx\_config\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmodem__ubx__config.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 62.1\_数据成员（Data Fields）

<a id="r_acac2ab2800443c4f60cbf5df9ca8cd5e"></a>

```c
void * user_data
```

相关声明：[user_data](#acac2ab2800443c4f60cbf5df9ca8cd5e)。

<a id="r_a7ac0f254167c3197366b210bef2ac75d"></a>

```c
uint8_t * receive_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[receive_buf](#a7ac0f254167c3197366b210bef2ac75d)。

<a id="r_a75634cde7a69ef78ea0370f423307a0e"></a>

```c
uint16_t receive_buf_size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[receive_buf_size](#a75634cde7a69ef78ea0370f423307a0e)。

```c
struct {
```

<a id="r_a6491d37ade10afcaff7ef1aebe3cc02f"></a>

```c
const struct modem_ubx_match * array
```

相关声明：[modem_ubx_match](P063_modem_ubx_match_结构体.md)、[array](#a75237681e1c9bf094b347e71e1ad823e)。

<a id="r_a653b9ea47ecd95da5747e49c4f55e3d7"></a>

```c
size_t size
```

相关声明：[size](#a19f107638346a44bddc73045f595ec98)。

<a id="r_a08ba4ac10872f451a302fcbc04a04253"></a>

```c
} unsol_matches
```

相关声明：[unsol_matches](#a08ba4ac10872f451a302fcbc04a04253)。

## 62.2\_详细说明（Detailed Documentation）

<a id="a75237681e1c9bf094b347e71e1ad823e"></a>

### `array`

```c
const struct modem_ubx_match* modem_ubx_config::array
```

<a id="a7ac0f254167c3197366b210bef2ac75d"></a>

### `receive_buf`

```c
uint8_t* modem_ubx_config::receive_buf
```

<a id="a75634cde7a69ef78ea0370f423307a0e"></a>

### `receive_buf_size`

```c
uint16_t modem_ubx_config::receive_buf_size
```

<a id="a19f107638346a44bddc73045f595ec98"></a>

### `size`

```c
size_t modem_ubx_config::size
```

<a id="a08ba4ac10872f451a302fcbc04a04253"></a>

### `[struct]`

```c
struct { ... } modem_ubx_config::unsol_matches
```

<a id="acac2ab2800443c4f60cbf5df9ca8cd5e"></a>

### `user_data`

```c
void* modem_ubx_config::user_data
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx.h`

## 62.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx.h](https://docs.zephyrproject.org/latest/doxygen/html/ubx_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [modem_ubx_match](P063_modem_ubx_match_结构体.md)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P061_modem_ubx_结构体.md) · [返回大纲](大纲.md) · [下一章](P063_modem_ubx_match_结构体.md)
