---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-4
title: bt_aics_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_bt\_aics\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__register__param.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

用于初始化音频输入控制服务（AICS）实例的结构体。

```c
#include <zephyr/bluetooth/audio/aics.h>
```

<a id="details"></a>

用于初始化音频输入控制服务（AICS）实例的结构体。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a966e9e99544392cdfac264ee6effcc7c"></a>

```c
int8_t gain
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[gain](#a966e9e99544392cdfac264ee6effcc7c)。

初始音频输入增益，范围为 -128 到 127。

<a id="r_ac95e17bc53539deeab5d161ca1b08194"></a>

```c
uint8_t mute
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mute](#ac95e17bc53539deeab5d161ca1b08194)。

初始音频输入静音状态。

<a id="r_a3658ed1900a44eef84b5602e567fe085"></a>

```c
uint8_t gain_mode
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[gain_mode](#a3658ed1900a44eef84b5602e567fe085)。

初始音频输入模式。

<a id="r_a4b2eae9a9716629e9c56ee3e6dc05e44"></a>

```c
uint8_t units
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[units](#a4b2eae9a9716629e9c56ee3e6dc05e44)。

初始音频输入增益单位，按 `N * 0.1 dB` 计算。

<a id="r_aac91095a831fe540ee356eb9b9d402d8"></a>

```c
int8_t min_gain
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[min_gain](#aac91095a831fe540ee356eb9b9d402d8)。

初始音频输入最小增益。

<a id="r_aa139122e2710d9ec28ec015692545dda"></a>

```c
int8_t max_gain
```

相关声明：[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[max_gain](#aa139122e2710d9ec28ec015692545dda)。

初始音频输入最大增益。

<a id="r_ad6afebea920fa4c168498ca11778ea7d"></a>

```c
uint8_t type
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[type](#ad6afebea920fa4c168498ca11778ea7d)。

初始音频输入类型。

<a id="r_a46437f4540d226ce3fbc470448f36e1f"></a>

```c
bool status
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[status](#a46437f4540d226ce3fbc470448f36e1f)。

初始音频输入活动状态：活动／非活动（Active/Inactive）。

<a id="r_acc408a0318b94cdc952ef7d6682e5705"></a>

```c
bool desc_writable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[desc_writable](#acc408a0318b94cdc952ef7d6682e5705)。

布尔值，用于设置客户端是否可以写入描述。

<a id="r_af99d31215008eb201c488a5b1107e009"></a>

```c
char * description
```

相关声明：[description](#af99d31215008eb201c488a5b1107e009)。

初始音频输入描述。

<a id="r_a6c961cde10dbfbaaa26bbc2b5c867001"></a>

```c
struct bt_aics_cb * cb
```

相关声明：[bt_aics_cb](P002_bt_aics_cb_结构体.md)、[cb](#a6c961cde10dbfbaaa26bbc2b5c867001)。

指向回调结构体（Callback Structure）的指针。

## 4.2\_详细说明（Detailed Documentation）

<a id="a6c961cde10dbfbaaa26bbc2b5c867001"></a>

### `cb`

```c
struct bt_aics_cb* bt_aics_register_param::cb
```

指向回调结构体（Callback Structure）的指针。

<a id="acc408a0318b94cdc952ef7d6682e5705"></a>

### `desc_writable`

```c
bool bt_aics_register_param::desc_writable
```

布尔值，用于设置客户端是否可以写入描述。

<a id="af99d31215008eb201c488a5b1107e009"></a>

### `description`

```c
char* bt_aics_register_param::description
```

初始音频输入描述。

<a id="a966e9e99544392cdfac264ee6effcc7c"></a>

### `gain`

```c
int8_t bt_aics_register_param::gain
```

初始音频输入增益，范围为 -128 到 127。

<a id="a3658ed1900a44eef84b5602e567fe085"></a>

### `gain_mode`

```c
uint8_t bt_aics_register_param::gain_mode
```

初始音频输入模式。

<a id="aa139122e2710d9ec28ec015692545dda"></a>

### `max_gain`

```c
int8_t bt_aics_register_param::max_gain
```

初始音频输入最大增益。

<a id="aac91095a831fe540ee356eb9b9d402d8"></a>

### `min_gain`

```c
int8_t bt_aics_register_param::min_gain
```

初始音频输入最小增益。

<a id="ac95e17bc53539deeab5d161ca1b08194"></a>

### `mute`

```c
uint8_t bt_aics_register_param::mute
```

初始音频输入静音状态。

<a id="a46437f4540d226ce3fbc470448f36e1f"></a>

### `status`

```c
bool bt_aics_register_param::status
```

初始音频输入活动状态：活动／非活动（Active/Inactive）。

<a id="ad6afebea920fa4c168498ca11778ea7d"></a>

### `type`

```c
uint8_t bt_aics_register_param::type
```

初始音频输入类型。

<a id="a4b2eae9a9716629e9c56ee3e6dc05e44"></a>

### `units`

```c
uint8_t bt_aics_register_param::units
```

初始音频输入增益单位，按 `N * 0.1 dB` 计算。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/aics.h`

## 4.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h_source.html)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [bt_aics_cb](P002_bt_aics_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_bt_aics_discover_param_结构体.md) · [返回大纲](大纲.md) · [下一章](P005_bt_ascs_cb_结构体.md)
