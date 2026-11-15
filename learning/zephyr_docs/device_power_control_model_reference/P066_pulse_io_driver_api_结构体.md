---
id: learning.zephyr-docs.device-power-control-model-reference.page-66
title: pulse_io_driver_api_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第66章\_pulse\_io\_driver\_api\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structpulse__io__driver__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

驱动虚表（Driver Vtable）。

```c
#include <zephyr/drivers/pulse_io.h>
```

<a id="details"></a>

驱动虚函数表（Driver vtable）。由各后端实现，不供应用程序直接使用。核心操作为必需项，不能为 `NULL`；实时 I/O（RTIO）操作为可选项，为 `NULL` 时封装函数返回 `-ENOSYS`。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 66.1\_数据成员（Data Fields）

<a id="r_a9aa7510ea5c1aab6b490dd3b6b1a4bbc"></a>

```c
int(* get_capabilities )(const struct device *dev, struct pulse_io_caps *caps)
```

相关声明：[get_capabilities](#a9aa7510ea5c1aab6b490dd3b6b1a4bbc)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_caps](P063_pulse_io_caps_结构体.md)。

`OPT`：为 `NULL` 时，封装函数返回 `-ENOSYS`。

<a id="r_aee848f0d513e8fe1573cf1e8f5c480a4"></a>

```c
int(* channel_get )(const struct device *dev, uint8_t channel_idx, struct pulse_io_channel **chan)
```

相关声明：[channel_get](#aee848f0d513e8fe1573cf1e8f5c480a4)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

`REQ`：必需项（Required）。

<a id="r_a27dab2f1794e29d51ff613af6d85b0ee"></a>

```c
int(* channel_release )(const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[channel_release](#a27dab2f1794e29d51ff613af6d85b0ee)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：必需项（Required）。

<a id="r_a6a3d4ba7f6da3ffdc79f9bc30cbc4429"></a>

```c
int(* channel_configure )(const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_config *cfg)
```

相关声明：[channel_configure](#a6a3d4ba7f6da3ffdc79f9bc30cbc4429)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_config](P064_pulse_io_config_结构体.md)。

`REQ`：必需项（Required）。

<a id="r_a5c621cc969cddc1af5698616a3809994"></a>

```c
int(* transmit_sync )(const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_tx_req *req, k_timeout_t timeout)
```

相关声明：[transmit_sync](#a5c621cc969cddc1af5698616a3809994)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_tx_req](P069_pulse_io_tx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

`REQ`：必需项（Required）。

<a id="r_a42d3e7109cab1333e12ba4da57eac80c"></a>

```c
int(* receive_sync )(const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_rx_req *req, size_t *count, k_timeout_t timeout)
```

相关声明：[receive_sync](#a42d3e7109cab1333e12ba4da57eac80c)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_rx_req](P068_pulse_io_rx_req_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

`REQ`：必需项（Required）。

<a id="r_a1e5d2a7e7aa0a44d4b8cc106c22242e9"></a>

```c
int(* stop )(const struct device *dev, struct pulse_io_channel *chan)
```

相关声明：[stop](#a1e5d2a7e7aa0a44d4b8cc106c22242e9)、[device](../device_reference/P002_设备对象结构.md)。

`REQ`：必需项（Required）。

<a id="r_afba3d4238934be36aa5a27c20160df5f"></a>

```c
void(* submit )(const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[submit](#afba3d4238934be36aa5a27c20160df5f)、[device](../device_reference/P002_设备对象结构.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

`OPT`：RTIO 提交操作；后端不支持 RTIO 时为 `NULL`。

<a id="r_a9aeb9a2a707d8a3c2fe81d064e59c320"></a>

```c
int(* get_encoder )(const struct device *dev, const struct pulse_io_encoder_api **api)
```

相关声明：[get_encoder](#a9aeb9a2a707d8a3c2fe81d064e59c320)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_encoder_api](P067_pulse_io_encoder_api_结构体.md)。

`OPT`：可选项（Optional）。

<a id="r_adbfd779fcbcecce8af577256c38cf941"></a>

```c
int(* get_decoder )(const struct device *dev, const struct pulse_io_decoder_api **api)
```

相关声明：[get_decoder](#adbfd779fcbcecce8af577256c38cf941)、[device](../device_reference/P002_设备对象结构.md)、[pulse_io_decoder_api](P065_pulse_io_decoder_api_结构体.md)。

`OPT`：可选项（Optional）。

## 66.2\_详细说明（Detailed Documentation）

<a id="a6a3d4ba7f6da3ffdc79f9bc30cbc4429"></a>

### `channel_configure`

```c
int(* pulse_io_driver_api::channel_configure) (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_config *cfg)
```

`REQ`：必需项（Required）。

<a id="aee848f0d513e8fe1573cf1e8f5c480a4"></a>

### `channel_get`

```c
int(* pulse_io_driver_api::channel_get) (const struct device *dev, uint8_t channel_idx, struct pulse_io_channel **chan)
```

`REQ`：必需项（Required）。

<a id="a27dab2f1794e29d51ff613af6d85b0ee"></a>

### `channel_release`

```c
int(* pulse_io_driver_api::channel_release) (const struct device *dev, struct pulse_io_channel *chan)
```

`REQ`：必需项（Required）。

<a id="a9aa7510ea5c1aab6b490dd3b6b1a4bbc"></a>

### `get_capabilities`

```c
int(* pulse_io_driver_api::get_capabilities) (const struct device *dev, struct pulse_io_caps *caps)
```

`OPT`：为 `NULL` 时，封装函数返回 `-ENOSYS`。

<a id="adbfd779fcbcecce8af577256c38cf941"></a>

### `get_decoder`

```c
int(* pulse_io_driver_api::get_decoder) (const struct device *dev, const struct pulse_io_decoder_api **api)
```

`OPT`：可选项（Optional）。

<a id="a9aeb9a2a707d8a3c2fe81d064e59c320"></a>

### `get_encoder`

```c
int(* pulse_io_driver_api::get_encoder) (const struct device *dev, const struct pulse_io_encoder_api **api)
```

`OPT`：可选项（Optional）。

<a id="a42d3e7109cab1333e12ba4da57eac80c"></a>

### `receive_sync`

```c
int(* pulse_io_driver_api::receive_sync) (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_rx_req *req, size_t *count, k_timeout_t timeout)
```

`REQ`：必需项（Required）。

<a id="a1e5d2a7e7aa0a44d4b8cc106c22242e9"></a>

### `stop`

```c
int(* pulse_io_driver_api::stop) (const struct device *dev, struct pulse_io_channel *chan)
```

`REQ`：必需项（Required）。

<a id="afba3d4238934be36aa5a27c20160df5f"></a>

### `submit`

```c
void(* pulse_io_driver_api::submit) (const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
```

`OPT`：RTIO 提交操作；后端不支持 RTIO 时为 `NULL`。

<a id="a5c621cc969cddc1af5698616a3809994"></a>

### `transmit_sync`

```c
int(* pulse_io_driver_api::transmit_sync) (const struct device *dev, struct pulse_io_channel *chan, const struct pulse_io_tx_req *req, k_timeout_t timeout)
```

`REQ`：必需项（Required）。

本数据类型文档由以下文件生成：

- `zephyr/drivers/pulse_io.h`

## 66.3\_原页交叉引用（Cross References）

- [zephyr/drivers/pulse_io.h](https://docs.zephyrproject.org/latest/doxygen/html/pulse__io_8h_source.html)
- [device](../device_reference/P002_设备对象结构.md)
- [pulse_io_caps](P063_pulse_io_caps_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [pulse_io_config](P064_pulse_io_config_结构体.md)
- [pulse_io_tx_req](P069_pulse_io_tx_req_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [pulse_io_rx_req](P068_pulse_io_rx_req_结构体.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [pulse_io_encoder_api](P067_pulse_io_encoder_api_结构体.md)
- [pulse_io_decoder_api](P065_pulse_io_decoder_api_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P065_pulse_io_decoder_api_结构体.md) · [返回大纲](大纲.md) · [下一章](P067_pulse_io_encoder_api_结构体.md)
