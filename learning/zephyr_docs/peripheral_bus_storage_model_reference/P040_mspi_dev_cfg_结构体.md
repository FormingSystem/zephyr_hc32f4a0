---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-40
title: mspi_dev_cfg_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__cfg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第40章\_mspi\_dev\_cfg\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__dev__cfg.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI控制器设备专用配置（Device Specific Configuration）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI控制器设备专用配置（Device Specific Configuration）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 40.1\_数据成员（Data Fields）

<a id="r_abf8d45f88d0c8e1c4ee52ea238ff4466"></a>

```c
uint8_t ce_num
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ce_num](#abf8d45f88d0c8e1c4ee52ea238ff4466)。

配置 CE0、CE1 或更多片选。

<a id="r_a9490d822b67d7fab123f32f38b0ccef8"></a>

```c
uint32_t freq
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[freq](#a9490d822b67d7fab123f32f38b0ccef8)。

配置频率。

<a id="r_ad0f5c1a4cd3002313087a9b1fe6cf7a1"></a>

```c
enum mspi_io_mode io_mode
```

相关声明：[mspi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga904dfc1c800fb9832f7c6200f767f9a5)、[io_mode](#ad0f5c1a4cd3002313087a9b1fe6cf7a1)。

配置 I/O 模式。

<a id="r_a0da8c2ccf80fdf610fcdd7fae7d159f8"></a>

```c
enum mspi_data_rate data_rate
```

相关声明：[mspi_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gaa2131d9846bbfd74488a6ae1c2003e68)、[data_rate](#a0da8c2ccf80fdf610fcdd7fae7d159f8)。

配置数据速率（Data rate）。

<a id="r_a2bb78caec28fadcecd787fc8a573a336"></a>

```c
enum mspi_cpp_mode cpp
```

相关声明：[mspi_cpp_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga704e4d3759d3261b4468e9d9900e578c)、[cpp](#a2bb78caec28fadcecd787fc8a573a336)。

配置时钟极性与相位（Clock polarity and phase）。

<a id="r_a28cf9d7887e9f840344e2804c4040bc4"></a>

```c
enum mspi_endian endian
```

相关声明：[mspi_endian](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3625cde1379e66cb66a8cb3803ab2e44)、[endian](#a28cf9d7887e9f840344e2804c4040bc4)。

配置传输字节序（Endianness）。

<a id="r_ab6ed7eeb6d4b31530e06f69706b98278"></a>

```c
enum mspi_ce_polarity ce_polarity
```

相关声明：[mspi_ce_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga283275f86fe186f4b5e30110ae0d506b)、[ce_polarity](#ab6ed7eeb6d4b31530e06f69706b98278)。

配置片选使能信号的极性。

<a id="r_affdcd07ac3d3d25b8a8e0882277af39a"></a>

```c
bool dqs_enable
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[dqs_enable](#affdcd07ac3d3d25b8a8e0882277af39a)。

配置 DQS 模式。

<a id="r_aae492d2e5bad4b266779be9f5bb12ee9"></a>

```c
uint16_t rx_dummy
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[rx_dummy](#aae492d2e5bad4b266779be9f5bb12ee9)。

配置接收方向地址阶段与数据阶段之间的时钟周期数。

<a id="r_a9feb1c35f7e1f5c43489771e13f2af8d"></a>

```c
uint16_t tx_dummy
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[tx_dummy](#a9feb1c35f7e1f5c43489771e13f2af8d)。

配置发送方向地址阶段与数据阶段之间的时钟周期数。

<a id="r_ac9f47b226289005271a800739707456b"></a>

```c
uint32_t read_cmd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[read_cmd](#ac9f47b226289005271a800739707456b)。

配置读取命令。

<a id="r_acac2a0913bfbfe1f3b5e34ff1b71ff42"></a>

```c
uint32_t write_cmd
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[write_cmd](#acac2a0913bfbfe1f3b5e34ff1b71ff42)。

配置写入命令。

<a id="r_a0b0c9f101656e67d71d191b656738d2d"></a>

```c
uint8_t cmd_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd_length](#a0b0c9f101656e67d71d191b656738d2d)。

配置命令长度。

<a id="r_a6dbe113d5075b1b22896c7d0c281bd3d"></a>

```c
uint8_t addr_length
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[addr_length](#a6dbe113d5075b1b22896c7d0c281bd3d)。

配置地址长度。

<a id="r_a3ec3e22e25440ac5eecf0f9b2d79b9e0"></a>

```c
uint32_t mem_boundary
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[mem_boundary](#a3ec3e22e25440ac5eecf0f9b2d79b9e0)。

配置存储器边界（Memory boundary）。

<a id="r_a60eeb1503018fa47cc5618d150f09aa8"></a>

```c
uint32_t time_to_break
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[time_to_break](#a60eeb1503018fa47cc5618d150f09aa8)。

配置将一次传输拆分为两次传输的时间。

## 40.2\_详细说明（Detailed Documentation）

<a id="a6dbe113d5075b1b22896c7d0c281bd3d"></a>

### `addr_length`

```c
uint8_t mspi_dev_cfg::addr_length
```

配置地址长度。

<a id="abf8d45f88d0c8e1c4ee52ea238ff4466"></a>

### `ce_num`

```c
uint8_t mspi_dev_cfg::ce_num
```

配置 CE0、CE1 或更多片选。

<a id="ab6ed7eeb6d4b31530e06f69706b98278"></a>

### `ce_polarity`

```c
enum mspi_ce_polarity mspi_dev_cfg::ce_polarity
```

配置片选使能信号的极性。

<a id="a0b0c9f101656e67d71d191b656738d2d"></a>

### `cmd_length`

```c
uint8_t mspi_dev_cfg::cmd_length
```

配置命令长度。

<a id="a2bb78caec28fadcecd787fc8a573a336"></a>

### `cpp`

```c
enum mspi_cpp_mode mspi_dev_cfg::cpp
```

配置时钟极性与相位（Clock polarity and phase）。

<a id="a0da8c2ccf80fdf610fcdd7fae7d159f8"></a>

### `data_rate`

```c
enum mspi_data_rate mspi_dev_cfg::data_rate
```

配置数据速率（Data rate）。

<a id="affdcd07ac3d3d25b8a8e0882277af39a"></a>

### `dqs_enable`

```c
bool mspi_dev_cfg::dqs_enable
```

配置 DQS 模式。

<a id="a28cf9d7887e9f840344e2804c4040bc4"></a>

### `endian`

```c
enum mspi_endian mspi_dev_cfg::endian
```

配置传输字节序（Endianness）。

<a id="a9490d822b67d7fab123f32f38b0ccef8"></a>

### `freq`

```c
uint32_t mspi_dev_cfg::freq
```

配置频率。

<a id="ad0f5c1a4cd3002313087a9b1fe6cf7a1"></a>

### `io_mode`

```c
enum mspi_io_mode mspi_dev_cfg::io_mode
```

配置 I/O 模式。

<a id="a3ec3e22e25440ac5eecf0f9b2d79b9e0"></a>

### `mem_boundary`

```c
uint32_t mspi_dev_cfg::mem_boundary
```

配置存储器边界（Memory boundary）。

<a id="ac9f47b226289005271a800739707456b"></a>

### `read_cmd`

```c
uint32_t mspi_dev_cfg::read_cmd
```

配置读取命令。

<a id="aae492d2e5bad4b266779be9f5bb12ee9"></a>

### `rx_dummy`

```c
uint16_t mspi_dev_cfg::rx_dummy
```

配置接收方向地址阶段与数据阶段之间的时钟周期数。

<a id="a60eeb1503018fa47cc5618d150f09aa8"></a>

### `time_to_break`

```c
uint32_t mspi_dev_cfg::time_to_break
```

配置将一次传输拆分为两次传输的时间。

<a id="a9feb1c35f7e1f5c43489771e13f2af8d"></a>

### `tx_dummy`

```c
uint16_t mspi_dev_cfg::tx_dummy
```

配置发送方向地址阶段与数据阶段之间的时钟周期数。

<a id="acac2a0913bfbfe1f3b5e34ff1b71ff42"></a>

### `write_cmd`

```c
uint32_t mspi_dev_cfg::write_cmd
```

配置写入命令。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 40.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [mspi_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga904dfc1c800fb9832f7c6200f767f9a5)
- [mspi_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#gaa2131d9846bbfd74488a6ae1c2003e68)
- [mspi_cpp_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga704e4d3759d3261b4468e9d9900e578c)
- [mspi_endian](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga3625cde1379e66cb66a8cb3803ab2e44)
- [mspi_ce_polarity](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__interface.html#ga283275f86fe186f4b5e30110ae0d506b)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P039_mspi_cfg_结构体.md) · [返回大纲](大纲.md) · [下一章](P041_mspi_dev_id_结构体.md)
