---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-51
title: mspi_xfer_packet_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer__packet.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_mspi\_xfer\_packet\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer__packet.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI外设传输数据包格式（Xfer Packet Format）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI外设传输数据包格式（Xfer Packet Format）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 51.1\_数据成员（Data Fields）

<a id="r_afb408ea48ff8863c9714d39c4f7c8a2c"></a>

```c
enum mspi_xfer_direction dir
```

相关声明：[mspi_xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga498f10591acf5dc7ec88e0aa98e537d6)、[dir](#afb408ea48ff8863c9714d39c4f7c8a2c)。

方向：发送/接收（Transmit/Receive）。

<a id="r_aedc8eadfb3a0737c3984b130ec21d96c"></a>

```c
enum mspi_bus_event_cb_mask cb_mask
```

相关声明：[mspi_bus_event_cb_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1)、[cb_mask](#aedc8eadfb3a0737c3984b130ec21d96c)。

总线事件回调掩码。

<a id="r_a2717e86b7fbb01be65a4955a8e26ebc0"></a>

```c
uint32_t cmd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cmd](#a2717e86b7fbb01be65a4955a8e26ebc0)。

传输命令。

<a id="r_a08dae9b6fbda60f06430cb2b842280b9"></a>

```c
uint32_t address
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[address](#a08dae9b6fbda60f06430cb2b842280b9)。

传输地址。

<a id="r_a050a827d0ee0349cd7a006de20b1db0c"></a>

```c
uint32_t num_bytes
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_bytes](#a050a827d0ee0349cd7a006de20b1db0c)。

要传输的字节数。

<a id="r_a0b7b3d68ff46173378e4076b439e35ac"></a>

```c
uint8_t * data_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data_buf](#a0b7b3d68ff46173378e4076b439e35ac)。

数据缓冲区（Data buffer）。

## 51.2\_详细说明（Detailed Documentation）

<a id="a08dae9b6fbda60f06430cb2b842280b9"></a>

### `address`

```c
uint32_t mspi_xfer_packet::address
```

传输地址。

<a id="aedc8eadfb3a0737c3984b130ec21d96c"></a>

### `cb_mask`

```c
enum mspi_bus_event_cb_mask mspi_xfer_packet::cb_mask
```

总线事件回调掩码。

<a id="a2717e86b7fbb01be65a4955a8e26ebc0"></a>

### `cmd`

```c
uint32_t mspi_xfer_packet::cmd
```

传输命令。

<a id="a0b7b3d68ff46173378e4076b439e35ac"></a>

### `data_buf`

```c
uint8_t* mspi_xfer_packet::data_buf
```

数据缓冲区（Data buffer）。

<a id="afb408ea48ff8863c9714d39c4f7c8a2c"></a>

### `dir`

```c
enum mspi_xfer_direction mspi_xfer_packet::dir
```

方向：发送/接收（Transmit/Receive）。

<a id="a050a827d0ee0349cd7a006de20b1db0c"></a>

### `num_bytes`

```c
uint32_t mspi_xfer_packet::num_bytes
```

要传输的字节数。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 51.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [mspi_xfer_direction](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga498f10591acf5dc7ec88e0aa98e537d6)
- [mspi_bus_event_cb_mask](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gab33e9840b0937c944f4e1a2525534cb1)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P050_mspi_xfer_结构体.md) · [返回大纲](大纲.md) · [下一章](P052_mux_control_结构体.md)
