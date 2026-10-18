---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-53
title: mux_control_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmux__control__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_mux\_control\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmux__control__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

多路复用器（MUX）控制器驱动API。

```c
#include <zephyr/drivers/mux.h>
```

<a id="details"></a>

多路复用器（MUX）控制器驱动API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 53.1\_数据成员（Data Fields）

<a id="r_a7f6eabe1190c03f4c3f88e75ffb5def1"></a>

```c
mux_control_set_fn set
```

相关声明：[set](#a7f6eabe1190c03f4c3f88e75ffb5def1)。

`REQ`：将 MUX 控制线驱动到给定状态。

<a id="r_a0594f85b8a90eb1f2aa77c3b09ef9a33"></a>

```c
mux_state_get_fn get_state
```

相关声明：[get_state](#a0594f85b8a90eb1f2aa77c3b09ef9a33)。

`OPT`：读回 MUX 控制线的当前状态。

<a id="r_a869779d5815628bb6ca7b7b9dd0258cd"></a>

```c
mux_control_disconnect_fn disconnect
```

相关声明：[disconnect](#a869779d5815628bb6ca7b7b9dd0258cd)。

`OPT`：物理断开 MUX 控制线。

## 53.2\_详细说明（Detailed Documentation）

<a id="a869779d5815628bb6ca7b7b9dd0258cd"></a>

### `disconnect`

```c
mux_control_disconnect_fn mux_control_driver_api::disconnect
```

`OPT`：物理断开 MUX 控制线。

<a id="a0594f85b8a90eb1f2aa77c3b09ef9a33"></a>

### `get_state`

```c
mux_state_get_fn mux_control_driver_api::get_state
```

`OPT`：读回 MUX 控制线的当前状态。

<a id="a7f6eabe1190c03f4c3f88e75ffb5def1"></a>

### `set`

```c
mux_control_set_fn mux_control_driver_api::set
```

`REQ`：将 MUX 控制线驱动到给定状态。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mux.h`

## 53.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mux.h](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2mux_8h_source.html)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P052_mux_control_结构体.md) · [返回大纲](大纲.md) · [下一章](P054_mux_state_结构体.md)
