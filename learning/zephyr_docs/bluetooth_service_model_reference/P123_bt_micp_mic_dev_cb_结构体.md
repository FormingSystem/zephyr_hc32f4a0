---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-123
title: bt_micp_mic_dev_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__dev__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第123章\_bt\_micp\_mic\_dev\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__micp__mic__dev__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

保存麦克风设备（Microphone Device）回调的结构。

```c
#include <zephyr/bluetooth/audio/micp.h>
```

<a id="details"></a>

保存麦克风设备回调的结构体。可通过 `bt_micp_mic_dev_register()` 注册这些回调供使用。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 123.1\_数据成员（Data Fields）

<a id="r_ad674b130546ceabbb90e6004121ccd98"></a>

```c
void(* mute )(uint8_t mute)
```

相关声明：[mute](#ad674b130546ceabbb90e6004121ccd98)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

麦克风设备（Microphone Device）静音状态的回调函数。

## 123.2\_详细说明（Detailed Documentation）

<a id="ad674b130546ceabbb90e6004121ccd98"></a>

### `mute`

```c
void(* bt_micp_mic_dev_cb::mute) (uint8_t mute)
```

麦克风设备（Microphone Device）静音状态的回调函数。

通过 `bt_micp_mic_dev_mute_get()` 读取此值时调用；当麦克风设备或麦克风控制器更改此值时，也会调用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `mute` | 麦克风控制服务（Microphone Control Service）的静音设置。 |

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/audio/micp.h`

## 123.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/micp.h](https://docs.zephyrproject.org/latest/doxygen/html/micp_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_micp_mic_dev_register()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga5dee6c7a1115bffbea39ba0575f369fc)
- [bt_micp_mic_dev_mute_get()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__micp.html#ga263bf5cf51e4ef8d7e6986f0d8358da3)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P122_bt_micp_mic_ctlr_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P124_bt_micp_mic_dev_register_param_结构体.md)
