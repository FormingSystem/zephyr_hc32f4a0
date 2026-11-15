---
id: learning.zephyr-docs.api-connection-topic-reference.page-16
title: MSPI 传输 API（MSPI Transfer API）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_MSPI 传输 API（MSPI Transfer API）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mspi__transfer__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MSPI 传输 API（MSPI Transfer API）

<a id="details"></a>

MSPI 传输 API（MSPI Transfer API）

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 16.1\_数据结构（Data Structures）

<a id="r_mspi_5Fce_5Fcontrol"></a>

```c
struct mspi_ce_control
```

相关声明：[mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)。

MSPI片选（Chip Select）的控制结构。

<a id="r_mspi_5Fxfer_5Fpacket"></a>

```c
struct mspi_xfer_packet
```

相关声明：[mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)。

MSPI外设传输数据包格式（Xfer Packet Format）。

<a id="r_mspi_5Fxfer"></a>

```c
struct mspi_xfer
```

相关声明：[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

MSPI外设传输格式（Xfer Format），包括可能需要配置硬件的传输相关设置。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 16.2\_函数（Functions）

<a id="r_ga8c98c73e322c575b759ce911cc115129"></a>

```c
int mspi_transceive (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer *req)
```

相关声明：[mspi_transceive](#ga8c98c73e322c575b759ce911cc115129)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)。

通过 MSPI 执行传输请求。

<a id="r_gaa656820a834bcde0d06041cff8f0d5e1"></a>

```c
static int mspi_transceive_data_only (const struct device *controller, const struct mspi_dev_id *dev_id, const struct mspi_xfer_packet *packets, uint32_t num_packet, enum mspi_xfer_mode xfer_mode, bool async, uint32_t timeout)
```

相关声明：[mspi_transceive_data_only](#gaa656820a834bcde0d06041cff8f0d5e1)、[device](../device_reference/P002_设备对象结构.md)、[mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)、[mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[mspi_xfer_mode](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga116259bbb1d12a10c2ba9e6051f2f000)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

通过 MSPI 传输数据，不包含命令阶段和地址阶段。

## 16.3\_详细说明（Detailed Documentation）

<a id="ga8c98c73e322c575b759ce911cc115129"></a>

### `mspi_transceive()`

```c
int mspi_transceive ( const struct device * controller, const struct mspi_dev_id * dev_id, const struct mspi_xfer * req )
```

```c
#include <zephyr/drivers/mspi.h>
```

通过 MSPI 执行传输请求。

此例程提供以同步／异步方式传输请求的通用接口。

原文此处仅为不完整片段 `The`，没有给出进一步说明。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `req` | 请求内容及请求专用设置（request-specific settings）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` |  |
| `-EIO` | 一般输入／输出错误（I/O error），通过总线发送失败。 |

**参阅（See Also）**：另请参阅 `mspi_xfer`：确定并配置运行模式后，可通过它动态更改与传输有关的设置。该 API 使用 `mspi_xfer_packet` 支持起始地址和大小各不相同的批量传输（bulk transfers）。是否支持分散 I/O（scatter I/O）和回调管理，由控制器实现决定。如果已注册回调，控制器可在每次异步／同步传输完成时，根据 `mspi_bus_event_cb_mask` 决定触发哪个用户回调；也可通过 `MSPI_BUS_NO_CB` 不触发任何回调，即使回调已经注册。

<a id="gaa656820a834bcde0d06041cff8f0d5e1"></a>

### `mspi_transceive_data_only()`

```c
int mspi_transceive_data_only ( const struct device * controller, const struct mspi_dev_id * dev_id, const struct mspi_xfer_packet * packets, uint32_t num_packet, enum mspi_xfer_mode xfer_mode, bool async, uint32_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/mspi.h>
```

通过 MSPI 传输数据，不包含命令阶段和地址阶段。

基于 `mspi_transceive()` 的便捷封装，用于仅包含数据阶段（data phase）的传输。它从调用方拥有的数据包构造 `mspi_xfer`，并强制执行仅数据传输约定：`mspi_xfer::cmd_length` 和 `mspi_xfer::addr_length` 均为 0。驱动忽略 `mspi_xfer_packet::cmd` 和 `mspi_xfer_packet::address`。

当硬件无法区分命令字节和数据字节、仅 `mspi_xfer_packet::dir`、`mspi_xfer_packet::num_bytes` 和 `mspi_xfer_packet::data_buf` 有意义时，应使用此传输调用。控制器也可用它执行仅数据事务（data-only transactions）。

数据包仍归调用方所有；`async` 为 true 时，必须一直有效，直到传输完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `controller` | 指向驱动实例的设备结构（Device Structure）。 |
| `dev_id` | 指向设备的设备 ID 结构体的指针。 |
| `packets` | 传输数据包。 |
| `num_packet` | 传输数据包数量。 |
| `xfer_mode` | 传输模式（transfer mode）：程序控制 I/O（PIO）或直接存储器访问（DMA）。 |
| `async` | 异步或同步传输（Asynchronous/Synchronous transfer）。 |
| `timeout` | 传输超时值，单位为毫秒（ms）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-ENOTSUP` |  |
| `-EIO` | 一般输入／输出错误（I/O error），通过总线发送失败。 |


## 16.4\_原页交叉引用（Cross References）

- [mspi_ce_control](../peripheral_bus_storage_model_reference/P038_mspi_ce_control_结构体.md)
- [mspi_xfer_packet](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md)
- [mspi_xfer](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [mspi_dev_id](../peripheral_bus_storage_model_reference/P041_mspi_dev_id_结构体.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [mspi_xfer_mode](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ga116259bbb1d12a10c2ba9e6051f2f000)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [zephyr/drivers/mspi.h](../peripheral_bus_storage_header_reference/P017_zephyr__drivers__mspi.h_头文件参考.md)
- [设置（Settings）。](../storage/P063_设置子系统接口.md)
- [mspi_bus_event_cb_mask](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#gab33e9840b0937c944f4e1a2525534cb1)
- [MSPI_BUS_NO_CB](../api_auxiliary_topic_reference/P014_多位串行外设接口（MSPI）.md#ggab33e9840b0937c944f4e1a2525534cb1aac3e8481082214c0d995ce3c3b452277)
- [mspi_xfer::cmd_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#a387dd891ab994d75561b50a094427d22)
- [mspi_xfer::addr_length](../peripheral_bus_storage_model_reference/P050_mspi_xfer_结构体.md#ace851e368d69b76092f8429d83d963fd)
- [mspi_xfer_packet::cmd](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a2717e86b7fbb01be65a4955a8e26ebc0)
- [mspi_xfer_packet::address](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a08dae9b6fbda60f06430cb2b842280b9)
- [mspi_xfer_packet::dir](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#afb408ea48ff8863c9714d39c4f7c8a2c)
- [mspi_xfer_packet::num_bytes](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a050a827d0ee0349cd7a006de20b1db0c)
- [mspi_xfer_packet::data_buf](../peripheral_bus_storage_model_reference/P051_mspi_xfer_packet_结构体.md#a0b7b3d68ff46173378e4076b439e35ac)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P015_MSPI 驱动后端 API.md) · [返回大纲](大纲.md) · [下一章](P017_网络主机名库（Network Hostname Library）.md)
