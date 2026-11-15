---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-46
title: mspi_event_data_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structmspi__event__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_mspi\_event\_data\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structmspi__event__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI事件数据（Event Data）。

```c
#include <zephyr/drivers/mspi.h>
```

<a id="details"></a>

MSPI事件数据（Event Data）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_af788dc5374778055d1ee9fddbe2a4d8d"></a>

```c
const struct device * controller
```

相关声明：[device](../device_reference/P002_设备对象结构.md)、[controller](#af788dc5374778055d1ee9fddbe2a4d8d)。

指向总线控制器的指针。

<a id="r_ab1138c26f9a6b11b75e1e50fb3e5d8e9"></a>

```c
const struct mspi_dev_id * dev_id
```

相关声明：[mspi_dev_id](P041_mspi_dev_id_结构体.md)、[dev_id](#ab1138c26f9a6b11b75e1e50fb3e5d8e9)。

指向外设设备 ID 的指针。

<a id="r_a1bb8c4591ced464181927b0c00003205"></a>

```c
const struct mspi_xfer_packet * packet
```

相关声明：[mspi_xfer_packet](P051_mspi_xfer_packet_结构体.md)、[packet](#a1bb8c4591ced464181927b0c00003205)。

指向传输数据包的指针。

<a id="r_a4b926cf5abb4f23bb7e1f85fecd323ef"></a>

```c
uint32_t status
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[status](#a4b926cf5abb4f23bb7e1f85fecd323ef)。

MSPI 事件状态。

<a id="r_a6e71714475e45a0d758aa49db33ff57e"></a>

```c
uint32_t packet_idx
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[packet_idx](#a6e71714475e45a0d758aa49db33ff57e)。

数据包索引（Packet index）。

## 46.2\_详细说明（Detailed Documentation）

<a id="af788dc5374778055d1ee9fddbe2a4d8d"></a>

### `controller`

```c
const struct device* mspi_event_data::controller
```

指向总线控制器的指针。

<a id="ab1138c26f9a6b11b75e1e50fb3e5d8e9"></a>

### `dev_id`

```c
const struct mspi_dev_id* mspi_event_data::dev_id
```

指向外设设备 ID 的指针。

<a id="a1bb8c4591ced464181927b0c00003205"></a>

### `packet`

```c
const struct mspi_xfer_packet* mspi_event_data::packet
```

指向传输数据包的指针。

<a id="a6e71714475e45a0d758aa49db33ff57e"></a>

### `packet_idx`

```c
uint32_t mspi_event_data::packet_idx
```

数据包索引（Packet index）。

<a id="a4b926cf5abb4f23bb7e1f85fecd323ef"></a>

### `status`

```c
uint32_t mspi_event_data::status
```

MSPI 事件状态。

本数据类型文档由以下文件生成：

- `zephyr/drivers/mspi.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/drivers/mspi.h](https://docs.zephyrproject.org/latest/doxygen/html/mspi_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_id](P041_mspi_dev_id_结构体.md)
- [mspi_xfer_packet](P051_mspi_xfer_packet_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_mspi_event_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_mspi_memmap_cfg_结构体.md)
