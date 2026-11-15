---
id: learning.zephyr-docs.bluetooth-mesh-model-reference.page-73
title: bt_mesh_lpn_timing_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__lpn__timing.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第73章\_bt\_mesh\_lpn\_timing\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__mesh__lpn__timing.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

根据时间戳得到的低功耗节点（LPN）好友关系时序测量值。

```c
#include <zephyr/bluetooth/mesh/statistic.h>
```

<a id="details"></a>

由时间戳推导的低功耗节点友谊关系实测时序（Measured LPN friendship timing）。通过在低功耗节点（LPN）侧为协议事件记录时间戳，计算这些数值：T1 为轮询发送完成（Poll TX complete）；T2 为扫描器启用（Scanner enabled，即 ReceiveDelay 已过去）；T3 为收到友谊节点响应（Friend response received）。实测接收延迟（ReceiveDelay）＝T2 − T1，即 LPN 开始监听之前的实际等待时间；实测接收窗口（ReceiveWindow）＝T3 − T2，即直到收到响应为止的实际监听时间。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 73.1\_数据成员（Data Fields）

<a id="r_a7908bb6fa9f12aa437e397f8c1b4ecaf"></a>

```c
uint32_t recv_delay_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_delay_us](#a7908bb6fa9f12aa437e397f8c1b4ecaf)。

上一轮轮询周期的实测接收延迟（ReceiveDelay），单位为微秒。

<a id="r_a47584e8ba286e85a5a333946abf6b18c"></a>

```c
uint32_t recv_delay_min_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_delay_min_us](#a47584e8ba286e85a5a333946abf6b18c)。

最小实测接收延迟（ReceiveDelay），单位为微秒。

<a id="r_a2c9f8faef395768c1b6e69fcc45c01bf"></a>

```c
uint32_t recv_delay_max_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_delay_max_us](#a2c9f8faef395768c1b6e69fcc45c01bf)。

最大实测接收延迟（ReceiveDelay），单位为微秒。

<a id="r_ac115c2cf035c722f8b6f969f700c1f81"></a>

```c
uint32_t recv_win_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_win_us](#ac115c2cf035c722f8b6f969f700c1f81)。

上一轮轮询周期的实测接收窗口（ReceiveWindow），单位为微秒。

<a id="r_a3d2f6b4b247fadceef5412be13288d9b"></a>

```c
uint32_t recv_win_min_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_win_min_us](#a3d2f6b4b247fadceef5412be13288d9b)。

最小实测接收窗口（ReceiveWindow），单位为微秒。

<a id="r_aa2c0aac2b1be70b6bb0b9311213a2482"></a>

```c
uint32_t recv_win_max_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_win_max_us](#aa2c0aac2b1be70b6bb0b9311213a2482)。

最大实测接收窗口（ReceiveWindow），单位为微秒。

<a id="r_a94adbcabda24c6ee0f6fa71bedd23ce0"></a>

```c
uint32_t recv_win_expected_us
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[recv_win_expected_us](#a94adbcabda24c6ee0f6fa71bedd23ce0)。

预期接收窗口（ReceiveWindow），单位为微秒。

<a id="r_abb4bb74a205cb33573d0fbb078701b62"></a>

```c
uint32_t cnt
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cnt](#abb4bb74a205cb33573d0fbb078701b62)。

已完成的轮询—响应周期总数（Poll-response cycles）。

<a id="r_a414f154e693065c7c40df6bfeb533eab"></a>

```c
uint32_t cnt_failed
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cnt_failed](#a414f154e693065c7c40df6bfeb533eab)。

失败的轮询—响应周期总数（Poll-response cycles），即窗口内未收到响应的次数。

## 73.2\_详细说明（Detailed Documentation）

<a id="abb4bb74a205cb33573d0fbb078701b62"></a>

### `cnt`

```c
uint32_t bt_mesh_lpn_timing::cnt
```

已完成的轮询—响应周期总数（Poll-response cycles）。

<a id="a414f154e693065c7c40df6bfeb533eab"></a>

### `cnt_failed`

```c
uint32_t bt_mesh_lpn_timing::cnt_failed
```

失败的轮询—响应周期总数（Poll-response cycles），即窗口内未收到响应的次数。

<a id="a2c9f8faef395768c1b6e69fcc45c01bf"></a>

### `recv_delay_max_us`

```c
uint32_t bt_mesh_lpn_timing::recv_delay_max_us
```

最大实测接收延迟（ReceiveDelay），单位为微秒。

<a id="a47584e8ba286e85a5a333946abf6b18c"></a>

### `recv_delay_min_us`

```c
uint32_t bt_mesh_lpn_timing::recv_delay_min_us
```

最小实测接收延迟（ReceiveDelay），单位为微秒。

<a id="a7908bb6fa9f12aa437e397f8c1b4ecaf"></a>

### `recv_delay_us`

```c
uint32_t bt_mesh_lpn_timing::recv_delay_us
```

上一轮轮询周期的实测接收延迟（ReceiveDelay），单位为微秒。

从轮询发送结束（Poll TX end）到扫描器启用（Scanner enable）的时间。

<a id="a94adbcabda24c6ee0f6fa71bedd23ce0"></a>

### `recv_win_expected_us`

```c
uint32_t bt_mesh_lpn_timing::recv_win_expected_us
```

预期接收窗口（ReceiveWindow），单位为微秒。

未收到友谊节点响应（Friend response）时，从扫描器启用到关闭的时间，即完整窗口（Full window）。尚未发生超时时为零。

<a id="aa2c0aac2b1be70b6bb0b9311213a2482"></a>

### `recv_win_max_us`

```c
uint32_t bt_mesh_lpn_timing::recv_win_max_us
```

最大实测接收窗口（ReceiveWindow），单位为微秒。

<a id="a3d2f6b4b247fadceef5412be13288d9b"></a>

### `recv_win_min_us`

```c
uint32_t bt_mesh_lpn_timing::recv_win_min_us
```

最小实测接收窗口（ReceiveWindow），单位为微秒。

<a id="ac115c2cf035c722f8b6f969f700c1f81"></a>

### `recv_win_us`

```c
uint32_t bt_mesh_lpn_timing::recv_win_us
```

上一轮轮询周期的实测接收窗口（ReceiveWindow），单位为微秒。

收到友谊节点响应（Friend response RX）后，从扫描器启用到关闭的时间。保留最近一次成功测量值，超时时不更新。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/mesh/statistic.h`

## 73.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/mesh/statistic.h](https://docs.zephyrproject.org/latest/doxygen/html/statistic_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P072_bt_mesh_lpn_cb_结构体.md) · [返回大纲](大纲.md) · [下一章](P074_bt_mesh_mod_id_vnd_结构体.md)
