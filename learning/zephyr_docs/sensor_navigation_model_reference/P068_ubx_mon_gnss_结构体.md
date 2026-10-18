---
id: learning.zephyr-docs.sensor-navigation-model-reference.page-68
title: ubx_mon_gnss_结构体
kind: reference
status: maintained
domains: [zephyr, sensors, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structubx__mon__gnss.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_ubx\_mon\_gnss\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structubx__mon__gnss.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/ubx/protocol.h>
```

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 68.1\_数据成员（Data Fields）

<a id="r_aebcccc44a80ef3b327d7d479ccb5ebe5"></a>

```c
uint8_t ver
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ver](#aebcccc44a80ef3b327d7d479ccb5ebe5)。

```c
struct {
```

<a id="r_a2fde292d9c657a65d92cbff1d11fbd4a"></a>

```c
uint8_t supported
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[supported](#a8f76d361c23ae4a94d29277be0aa36f8)。

<a id="r_a65deb253f5ba85ebae209dc1f06a2d52"></a>

```c
uint8_t default_enabled
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[default_enabled](#a2b94264d40d0aa740b20d9fa9565d155)。

<a id="r_a9fa81e5e2c76afc3ea1109d331d60211"></a>

```c
uint8_t enabled
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[enabled](#ad09bcd6e739e385c275f8a1cae8725b3)。

<a id="r_ae004377f656dede9b0ebe98caeea588f"></a>

```c
} selection
```

相关声明：[selection](#ae004377f656dede9b0ebe98caeea588f)。

<a id="r_a34b9073dda3d6ad734109cea8ba5a0d2"></a>

```c
uint8_t simultaneous
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[simultaneous](#a34b9073dda3d6ad734109cea8ba5a0d2)。

<a id="r_a045256bfbf8fe9b398ef77d10e00395a"></a>

```c
uint8_t reserved1 [3]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved1](#a045256bfbf8fe9b398ef77d10e00395a)。

## 68.2\_详细说明（Detailed Documentation）

<a id="a2b94264d40d0aa740b20d9fa9565d155"></a>

### `default_enabled`

```c
uint8_t ubx_mon_gnss::default_enabled
```

<a id="ad09bcd6e739e385c275f8a1cae8725b3"></a>

### `enabled`

```c
uint8_t ubx_mon_gnss::enabled
```

<a id="a045256bfbf8fe9b398ef77d10e00395a"></a>

### `reserved1`

```c
uint8_t ubx_mon_gnss::reserved1[3]
```

<a id="ae004377f656dede9b0ebe98caeea588f"></a>

### `[struct]`

```c
struct { ... } ubx_mon_gnss::selection
```

<a id="a34b9073dda3d6ad734109cea8ba5a0d2"></a>

### `simultaneous`

```c
uint8_t ubx_mon_gnss::simultaneous
```

<a id="a8f76d361c23ae4a94d29277be0aa36f8"></a>

### `supported`

```c
uint8_t ubx_mon_gnss::supported
```

<a id="aebcccc44a80ef3b327d7d479ccb5ebe5"></a>

### `ver`

```c
uint8_t ubx_mon_gnss::ver
```

本数据类型文档由以下文件生成：

- `zephyr/modem/ubx/protocol.h`

## 68.3\_原页交叉引用（Cross References）

- [zephyr/modem/ubx/protocol.h](https://docs.zephyrproject.org/latest/doxygen/html/modem_2ubx_2protocol_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P067_ubx_frame_match_结构体.md) · [返回大纲](大纲.md) · [下一章](P069_ubx_mon_ver_结构体.md)
