---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-183
title: bt_vcp_vol_rend_register_param_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__rend__register__param.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第183章\_bt\_vcp\_vol\_rend\_register\_param\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__vcp__vol__rend__register__param.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

音量控制服务（Volume Control Service）的注册结构。

```c
#include <zephyr/bluetooth/audio/vcp.h>
```

<a id="details"></a>

音量控制服务（Volume Control Service）的注册结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 183.1\_数据成员（Data Fields）

<a id="r_a098e6c6921813b3f0dc7512cd483c829"></a>

```c
uint8_t step
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[step](#a098e6c6921813b3f0dc7512cd483c829)。

初始步长（step size），范围为 1 至 255。

<a id="r_a93f2b246ac4241db468a46a64909866e"></a>

```c
uint8_t mute
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[mute](#a93f2b246ac4241db468a46a64909866e)。

初始静音状态（mute state），范围为 0 至 1。

<a id="r_a6cf1343a2b3033c3f4676d66017cfda7"></a>

```c
uint8_t volume
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[volume](#a6cf1343a2b3033c3f4676d66017cfda7)。

初始音量级别（volume level），范围为 0 至 255。

<a id="r_a6b5096f174425659c7fbc71df0da8e67"></a>

```c
struct bt_vocs_register_param vocs_param [0U]
```

相关声明：[bt_vocs_register_param](P187_bt_vocs_register_param_结构体.md)、[vocs_param](#a6b5096f174425659c7fbc71df0da8e67)。

音量偏移控制服务（Volume Offset Control Services）的注册参数。

<a id="r_a69257b668dc52429c64daa7af5161805"></a>

```c
struct bt_aics_register_param aics_param [0U]
```

相关声明：[bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)、[aics_param](#a69257b668dc52429c64daa7af5161805)。

音频输入控制服务（Audio Input Control Services）的注册参数。

<a id="r_af9a09c453394fd4a28d6415e2775c3f5"></a>

```c
struct bt_vcp_vol_rend_cb * cb
```

相关声明：[bt_vcp_vol_rend_cb](P182_bt_vcp_vol_rend_cb_结构体.md)、[cb](#af9a09c453394fd4a28d6415e2775c3f5)。

音量控制服务（Volume Control Service）回调结构体。

## 183.2\_详细说明（Detailed Documentation）

<a id="a69257b668dc52429c64daa7af5161805"></a>

### `aics_param`

```c
struct bt_aics_register_param bt_vcp_vol_rend_register_param::aics_param[0U]
```

音频输入控制服务（Audio Input Control Services）的注册参数。

<a id="af9a09c453394fd4a28d6415e2775c3f5"></a>

### `cb`

```c
struct bt_vcp_vol_rend_cb* bt_vcp_vol_rend_register_param::cb
```

音量控制服务（Volume Control Service）回调结构体。

<a id="a93f2b246ac4241db468a46a64909866e"></a>

### `mute`

```c
uint8_t bt_vcp_vol_rend_register_param::mute
```

初始静音状态（mute state），范围为 0 至 1。

<a id="a098e6c6921813b3f0dc7512cd483c829"></a>

### `step`

```c
uint8_t bt_vcp_vol_rend_register_param::step
```

初始步长（step size），范围为 1 至 255。

<a id="a6b5096f174425659c7fbc71df0da8e67"></a>

### `vocs_param`

```c
struct bt_vocs_register_param bt_vcp_vol_rend_register_param::vocs_param[0U]
```

音量偏移控制服务（Volume Offset Control Services）的注册参数。

<a id="a6cf1343a2b3033c3f4676d66017cfda7"></a>

### `volume`

```c
uint8_t bt_vcp_vol_rend_register_param::volume
```

初始音量级别（volume level），范围为 0 至 255。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/vcp.h`

## 183.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/vcp.h](https://docs.zephyrproject.org/latest/doxygen/html/vcp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_vocs_register_param](P187_bt_vocs_register_param_结构体.md)
- [bt_aics_register_param](../bluetooth_le_audio_model_reference/P004_bt_aics_register_param_结构体.md)
- [bt_vcp_vol_rend_cb](P182_bt_vcp_vol_rend_cb_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P182_bt_vcp_vol_rend_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P184_bt_vocs_结构体.md)
