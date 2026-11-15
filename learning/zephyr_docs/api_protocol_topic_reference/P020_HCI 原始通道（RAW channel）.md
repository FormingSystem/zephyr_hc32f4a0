---
id: learning.zephyr-docs.api-protocol-topic-reference.page-20
title: HCI 原始通道（RAW channel）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_HCI 原始通道（RAW channel）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__hci__raw.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HCI 原始通道（RAW channel）

<a id="details"></a>

主机控制器接口原始通道（HCI RAW channel）。自 Zephyr 2.3 起提供；API 版本为 1.0.0。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 20.1\_函数（Functions）

<a id="r_ga8de934e01eb9a16a3c9d096151e58313"></a>

```c
int bt_send (struct net_buf *buf)
```

相关声明：[bt_send](#ga8de934e01eb9a16a3c9d096151e58313)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向蓝牙控制器（Bluetooth Controller）发送数据包（Packet）。

<a id="r_gaae30308fe69b1b2fd2972dbcd5a34d9f"></a>

```c
int bt_enable_raw (struct k_fifo *rx_queue)
```

相关声明：[bt_enable_raw](#gaae30308fe69b1b2fd2972dbcd5a34d9f)、[k_fifo](../queue_reference/P004_内核FIFO结构.md)。

启用蓝牙原始通道（Bluetooth RAW Channel）：

## 20.2\_详细说明（Detailed Documentation）

<a id="gaae30308fe69b1b2fd2972dbcd5a34d9f"></a>

### `bt_enable_raw()`

```c
int bt_enable_raw ( struct k_fifo * rx_queue)
```

```c
#include <zephyr/bluetooth/hci_raw.h>
```

启用蓝牙原始通道（Bluetooth RAW Channel）：

启用蓝牙原始 HCI 通道（Bluetooth RAW HCI channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `rx_queue` | 用于排队存放从蓝牙控制器收到的 HCI 数据包的网络缓冲区（netbuf）队列。队列由调用方定义，可用缓冲池由协议栈管理。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。

<a id="ga8de934e01eb9a16a3c9d096151e58313"></a>

### `bt_send()`

```c
int bt_send ( struct net_buf * buf)
```

```c
#include <zephyr/bluetooth/hci_raw.h>
```

向蓝牙控制器（Bluetooth Controller）发送数据包（Packet）。

向蓝牙控制器发送数据包。缓冲区应使用 `bt_buf_get_tx()` 分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 待发送的 HCI 数据包。 |

**返回（Returns）**：返回值：成功时为零，否则为负错误码。


## 20.3\_原页交叉引用（Cross References）

- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [zephyr/bluetooth/hci_raw.h](../api_file_configuration_reference/P036_zephyr__bluetooth__hci_raw.h_文件参考.md)
- [bt_buf_get_tx()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__buf.html#ga761a31b7fb19f2325b3a9ac6b1fb1700)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P019_FocalTech 复位控制模块寄存器（Reset Control Module Registers）.md) · [返回大纲](大纲.md) · [下一章](P021_HX711 API主题.md)
