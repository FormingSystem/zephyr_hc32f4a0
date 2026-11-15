---
id: learning.zephyr-docs.api-source-reference.page-797
title: smp_raw_dummy.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第797章\_smp\_raw\_dummy.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h.html)。

## 797.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="agroup__mcumgr__transport__dummy_html_ga0ac2b264ccfbdd4861f162107f23fead"></a>
<a id="agroup__mcumgr__transport__dummy_html_ga2ddb5a7110046d6122dfce8d5ddab343"></a>
<a id="agroup__mcumgr__transport__dummy_html_ga58c6308491208020db01f09bff424465"></a>
<a id="agroup__mcumgr__transport__dummy_html_ga5e8c496f45a4ef5b67c033681900f167"></a>
<a id="agroup__mcumgr__transport__dummy_html_ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f"></a>
<a id="agroup__mcumgr__transport__dummy_html_gaa9c6ca2056062644fcb1db97755ff311"></a>
<a id="agroup__mcumgr__transport__dummy_html_gac2682f29403a437d2d7d50f1d069b742"></a>
<a id="agroup__mcumgr__transport__dummy_html_gac582aaa484eee63b36ab94739640b1dc"></a>
<a id="agroup__mcumgr__transport__dummy_html_gacb4b4948718df4c5ce13a27faca895b7"></a>
<a id="agroup__mcumgr__transport__dummy_html_gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d"></a>
<a id="agroup__mcumgr__transport__dummy_html_gafebbc255c07f6c08e15509118ab76f6a"></a>
<a id="akernel_8h_html"></a>
<a id="amgmt_8h_html"></a>
<a id="anet__buf_8h_html"></a>
<a id="aserial_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__buf_html_ac6eef59915e7ce167442fdacbbfb5e56"></a>
<a id="astructnet__buf_html_ae75b7ca728fb7440ea483be8bf88bc38"></a>

```c
/*
 * Copyright Runtime.io 2018. All rights reserved.
 * Copyright Laird Connectivity 2021-2022. All rights reserved.
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_RAW_DUMMY_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_RAW_DUMMY_H_


#include <zephyr/kernel.h>
#include <zephyr/net_buf.h>
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
#include <zephyr/mgmt/mcumgr/transport/serial.h>

#ifdef __cplusplus
extern "C" {
#endif

void smp_raw_dummy_clear_state(void);

void smp_raw_dummy_mcumgr_add_data(uint8_t *data, uint16_t data_size);

struct net_buf *smp_raw_dummy_get_outgoing(void);

bool smp_raw_dummy_wait_for_data(uint32_t wait_time_s);

void smp_raw_dummy_add_data(void);

uint16_t smp_raw_dummy_get_send_pos(void);

uint16_t smp_raw_dummy_get_receive_pos(void);

int smp_raw_dummy_tx_pkt(const uint8_t *data, int len);

void smp_raw_dummy_enable(void);

void smp_raw_dummy_disable(void);

bool smp_raw_dummy_get_status(void);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_RAW_DUMMY_H_ */
```

## 797.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：Runtime.io 2018. All rights reserved.。

版权（Copyright）：Laird Connectivity 2021-2022. All rights reserved.。

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 119 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_RAW_DUMMY_H_`。

## 797.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/smp__raw__dummy_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [zephyr/mgmt/mcumgr/transport/serial.h](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html)
- [smp_raw_dummy_clear_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga5e8c496f45a4ef5b67c033681900f167)
- [smp_raw_dummy_mcumgr_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac582aaa484eee63b36ab94739640b1dc)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_raw_dummy_get_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gafebbc255c07f6c08e15509118ab76f6a)
- [smp_raw_dummy_wait_for_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga0ac2b264ccfbdd4861f162107f23fead)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [smp_raw_dummy_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gaa9c6ca2056062644fcb1db97755ff311)
- [smp_raw_dummy_get_send_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gacb4b4948718df4c5ce13a27faca895b7)
- [smp_raw_dummy_get_receive_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga2ddb5a7110046d6122dfce8d5ddab343)
- [smp_raw_dummy_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gac2682f29403a437d2d7d50f1d069b742)
- [data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [smp_raw_dummy_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga58c6308491208020db01f09bff424465)
- [smp_raw_dummy_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d)
- [smp_raw_dummy_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [mgmt.h](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_8h.html)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [serial.h](https://docs.zephyrproject.org/latest/doxygen/html/serial_8h.html)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)

---

[上一章](P796_smp_dummy.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P798_smp_udp.h_源码浏览.md)
