---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-54
title: mux_state_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmux__state.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_mux\_state\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmux__state.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多路复用器（MUX）控制线的寻址与默认状态对。

```c
#include <zephyr/drivers/mux.h>
```

<a id="details"></a>

MUX 控制线的寻址信息与默认状态组合。一个 `mux_state` 将 `mux_control` 与默认状态值配对，该状态值从设备树 `mux-states` 说明符的末尾单元提取。使用 `mux_state_apply()` 即可通过一次调用将 MUX 驱动到该状态。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 54.1\_数据成员（Data Fields）

<a id="r_a89ec6f427ae2b928694d953178cfc284"></a>

```c
const struct mux_control * control
```

相关声明：[mux_control](P052_mux_control_结构体.md)、[control](#a89ec6f427ae2b928694d953178cfc284)。

寻址部分，指向一个静态定义的 `mux_control`。

<a id="r_af1b91ac4571fd44b8138ca6b226d3812"></a>

```c
uint32_t state
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[state](#af1b91ac4571fd44b8138ca6b226d3812)。

取自说明符末尾单元的默认状态值。

## 54.2\_详细说明（Detailed Documentation）

<a id="a89ec6f427ae2b928694d953178cfc284"></a>

### `control`

```c
const struct mux_control* mux_state::control
```

寻址部分，指向一个静态定义的 `mux_control`。

<a id="af1b91ac4571fd44b8138ca6b226d3812"></a>

### `state`

```c
uint32_t mux_state::state
```

取自说明符末尾单元的默认状态值。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mux.h`

## 54.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mux.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html)
- [mux_control](P052_mux_control_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mux_state](P054_mux_state_结构体.md)
- [mux_state_apply()](https://docs.zephyrproject.org/latest/doxygen/html/group__mux__interface.html#gad1b56b4430fca99f03bdf2b0ad6725c5)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P053_mux_control_driver_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P055_osdp_cmd_结构体.md)
