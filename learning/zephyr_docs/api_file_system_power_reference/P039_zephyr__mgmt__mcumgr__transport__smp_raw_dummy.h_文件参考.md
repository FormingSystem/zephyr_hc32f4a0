---
id: learning.zephyr-docs.api-file-system-power-reference.page-39
title: zephyr__mgmt__mcumgr__transport__smp_raw_dummy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第39章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_smp\_raw\_dummy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

供单元测试使用的mcumgr简单管理协议（SMP）虚拟传输。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/transport/serial.h>
```

查看此文件的源码。

供单元测试使用的mcumgr简单管理协议（SMP）虚拟传输。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 39.1\_函数（Functions）

<a id="r_ga5e8c496f45a4ef5b67c033681900f167"></a>

```c
void smp_raw_dummy_clear_state (void)
```

相关声明：[smp_raw_dummy_clear_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga5e8c496f45a4ef5b67c033681900f167)。

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="r_gac582aaa484eee63b36ab94739640b1dc"></a>

```c
void smp_raw_dummy_mcumgr_add_data (uint8_t *data, uint16_t data_size)
```

相关声明：[smp_raw_dummy_mcumgr_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac582aaa484eee63b36ab94739640b1dc)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

<a id="r_gafebbc255c07f6c08e15509118ab76f6a"></a>

```c
struct net_buf * smp_raw_dummy_get_outgoing (void)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_raw_dummy_get_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gafebbc255c07f6c08e15509118ab76f6a)。

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

<a id="r_ga0ac2b264ccfbdd4861f162107f23fead"></a>

```c
bool smp_raw_dummy_wait_for_data (uint32_t wait_time_s)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_raw_dummy_wait_for_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga0ac2b264ccfbdd4861f162107f23fead)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

<a id="r_gaa9c6ca2056062644fcb1db97755ff311"></a>

```c
void smp_raw_dummy_add_data (void)
```

相关声明：[smp_raw_dummy_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gaa9c6ca2056062644fcb1db97755ff311)。

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="r_gacb4b4948718df4c5ce13a27faca895b7"></a>

```c
uint16_t smp_raw_dummy_get_send_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_raw_dummy_get_send_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gacb4b4948718df4c5ce13a27faca895b7)。

获取当前发送缓冲区位置（Send Buffer Position）。

<a id="r_ga2ddb5a7110046d6122dfce8d5ddab343"></a>

```c
uint16_t smp_raw_dummy_get_receive_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_raw_dummy_get_receive_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga2ddb5a7110046d6122dfce8d5ddab343)。

获取当前接收缓冲区位置（Receive Buffer Position）。

<a id="r_gac2682f29403a437d2d7d50f1d069b742"></a>

```c
int smp_raw_dummy_tx_pkt (const uint8_t *data, int len)
```

相关声明：[smp_raw_dummy_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac2682f29403a437d2d7d50f1d069b742)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

<a id="r_ga58c6308491208020db01f09bff424465"></a>

```c
void smp_raw_dummy_enable (void)
```

相关声明：[smp_raw_dummy_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga58c6308491208020db01f09bff424465)。

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="r_gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d"></a>

```c
void smp_raw_dummy_disable (void)
```

相关声明：[smp_raw_dummy_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d)。

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="r_ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f"></a>

```c
bool smp_raw_dummy_get_status (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_raw_dummy_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f)。

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。


## 39.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](../api_source_reference/P521_mgmt.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/transport/serial.h](../api_source_reference/P770_serial.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P797_smp_raw_dummy.h_源码浏览.md)
- [smp_raw_dummy_clear_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga5e8c496f45a4ef5b67c033681900f167)
- [smp_raw_dummy_mcumgr_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac582aaa484eee63b36ab94739640b1dc)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_raw_dummy_get_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gafebbc255c07f6c08e15509118ab76f6a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_raw_dummy_wait_for_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga0ac2b264ccfbdd4861f162107f23fead)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [smp_raw_dummy_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gaa9c6ca2056062644fcb1db97755ff311)
- [smp_raw_dummy_get_send_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gacb4b4948718df4c5ce13a27faca895b7)
- [smp_raw_dummy_get_receive_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga2ddb5a7110046d6122dfce8d5ddab343)
- [smp_raw_dummy_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac2682f29403a437d2d7d50f1d069b742)
- [smp_raw_dummy_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga58c6308491208020db01f09bff424465)
- [smp_raw_dummy_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d)
- [smp_raw_dummy_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f)

<a id="header-details"></a>

---

[上一章](P038_zephyr__mgmt__mcumgr__transport__smp_dummy.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P040_zephyr__drivers__modem__st87mxx_app_services.h_文件参考.md)
