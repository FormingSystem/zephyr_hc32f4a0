---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-50
title: mspi_xfer_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_mspi\_xfer\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__xfer.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI外设传输格式（Xfer Format），包括可能需要配置硬件的传输相关设置。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI外设传输格式（Xfer Format），包括可能需要配置硬件的传输相关设置。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 50.1\_数据成员（Data Fields）

<a id="r_abf10b3fed96161447ffb7a8a6dce7649"></a>

```c
bool async
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[async](#abf10b3fed96161447ffb7a8a6dce7649)。

异步或同步传输（Asynchronous/Synchronous transfer）。

<a id="r_afa30e0fac32c6c3e7a3c9d7e29ccc8cb"></a>

```c
enum mspi_xfer_mode xfer_mode
```

相关声明：[mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)、[xfer_mode](#afa30e0fac32c6c3e7a3c9d7e29ccc8cb)。

传输模式（Transfer mode）。

<a id="r_adfe7adf63f83f40d1ab92ed511f4e917"></a>

```c
uint16_t tx_dummy
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_dummy](#adfe7adf63f83f40d1ab92ed511f4e917)。

配置发送空周期（TX dummy cycles）。

<a id="r_a98f23415592095749a853f3d850d399f"></a>

```c
uint16_t rx_dummy
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_dummy](#a98f23415592095749a853f3d850d399f)。

配置接收空周期（RX dummy cycles）。

<a id="r_a387dd891ab994d75561b50a094427d22"></a>

```c
uint8_t cmd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd_length](#a387dd891ab994d75561b50a094427d22)。

配置命令长度。

<a id="r_ace851e368d69b76092f8429d83d963fd"></a>

```c
uint8_t addr_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr_length](#ace851e368d69b76092f8429d83d963fd)。

配置地址长度。

<a id="r_a335fd5fb02bc75053902c4d1b294af57"></a>

```c
bool hold_ce
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[hold_ce](#a335fd5fb02bc75053902c4d1b294af57)。

传输完成后保持 CE 有效。

<a id="r_ae2e7a475ac4bcec88f12742642087505"></a>

```c
struct mspi_ce_control ce_sw_ctrl
```

相关声明：[mspi_ce_control](P038_mspi_ce_control_结构体.md)、[ce_sw_ctrl](#ae2e7a475ac4bcec88f12742642087505)。

软件 CE 控制。

<a id="r_aa763b87b9219d6c325a9f45d8d108d02"></a>

```c
enum mspi_xfer_priority priority
```

相关声明：[mspi_xfer_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga632af162124ca2959a21ca3759e1cc9e)、[priority](#aa763b87b9219d6c325a9f45d8d108d02)。

MSPI 传输优先级（Priority）。

<a id="r_a49e4102b694ffb5f9afe72c81fb7ca94"></a>

```c
const struct mspi_xfer_packet * packets
```

相关声明：[mspi_xfer_packet](P051_mspi_xfer_packet_结构体.md)、[packets](#a49e4102b694ffb5f9afe72c81fb7ca94)。

传输数据包。

<a id="r_a4061b26045ef860b8c9a6509ff054bc3"></a>

```c
uint32_t num_packet
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[num_packet](#a4061b26045ef860b8c9a6509ff054bc3)。

传输数据包数量。

<a id="r_afd83aa864cf300e9848ef46b7331ca5a"></a>

```c
uint32_t timeout
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[timeout](#afd83aa864cf300e9848ef46b7331ca5a)。

传输超时值，单位为毫秒（ms）。

## 50.2\_详细说明（Detailed Documentation）

<a id="ace851e368d69b76092f8429d83d963fd"></a>

### `addr_length`

```c
uint8_t mspi_xfer::addr_length
```

配置地址长度。

<a id="abf10b3fed96161447ffb7a8a6dce7649"></a>

### `async`

```c
bool mspi_xfer::async
```

异步或同步传输（Asynchronous/Synchronous transfer）。

<a id="ae2e7a475ac4bcec88f12742642087505"></a>

### `ce_sw_ctrl`

```c
struct mspi_ce_control mspi_xfer::ce_sw_ctrl
```

软件 CE 控制。

<a id="a387dd891ab994d75561b50a094427d22"></a>

### `cmd_length`

```c
uint8_t mspi_xfer::cmd_length
```

配置命令长度。

<a id="a335fd5fb02bc75053902c4d1b294af57"></a>

### `hold_ce`

```c
bool mspi_xfer::hold_ce
```

传输完成后保持 CE 有效。

<a id="a4061b26045ef860b8c9a6509ff054bc3"></a>

### `num_packet`

```c
uint32_t mspi_xfer::num_packet
```

传输数据包数量。

<a id="a49e4102b694ffb5f9afe72c81fb7ca94"></a>

### `packets`

```c
const struct mspi_xfer_packet* mspi_xfer::packets
```

传输数据包。

<a id="aa763b87b9219d6c325a9f45d8d108d02"></a>

### `priority`

```c
enum mspi_xfer_priority mspi_xfer::priority
```

MSPI 传输优先级（Priority）。

<a id="a98f23415592095749a853f3d850d399f"></a>

### `rx_dummy`

```c
uint16_t mspi_xfer::rx_dummy
```

配置接收空周期（RX dummy cycles）。

<a id="afd83aa864cf300e9848ef46b7331ca5a"></a>

### `timeout`

```c
uint32_t mspi_xfer::timeout
```

传输超时值，单位为毫秒（ms）。

<a id="adfe7adf63f83f40d1ab92ed511f4e917"></a>

### `tx_dummy`

```c
uint16_t mspi_xfer::tx_dummy
```

配置发送空周期（TX dummy cycles）。

<a id="afa30e0fac32c6c3e7a3c9d7e29ccc8cb"></a>

### `xfer_mode`

```c
enum mspi_xfer_mode mspi_xfer::xfer_mode
```

传输模式（Transfer mode）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 50.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [mspi_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga116259bbb1d12a10c2ba9e6051f2f000)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mspi_ce_control](P038_mspi_ce_control_结构体.md)
- [mspi_xfer_priority](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga632af162124ca2959a21ca3759e1cc9e)
- [mspi_xfer_packet](P051_mspi_xfer_packet_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P049_mspi_timing_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P051_mspi_xfer_packet_结构体.md)
