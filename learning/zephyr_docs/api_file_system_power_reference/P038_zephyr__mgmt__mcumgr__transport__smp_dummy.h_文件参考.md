---
id: learning.zephyr-docs.api-file-system-power-reference.page-38
title: zephyr__mgmt__mcumgr__transport__smp_dummy.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__dummy_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第38章\_zephyr\_\_mgmt\_\_mcumgr\_\_transport\_\_smp\_dummy.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/smp__dummy_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

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

## 38.1\_函数（Functions）

<a id="r_gad9b3c7f35e4fa24fe863145a687f53db"></a>

```c
void smp_dummy_clear_state (void)
```

相关声明：[smp_dummy_clear_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gad9b3c7f35e4fa24fe863145a687f53db)。

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="r_ga8bf3d0c12669c2cf5370eb7e148f10c2"></a>

```c
void dummy_mcumgr_add_data (uint8_t *data, uint16_t data_size)
```

相关声明：[dummy_mcumgr_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga8bf3d0c12669c2cf5370eb7e148f10c2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

<a id="r_gaa744df8e85bdb93cff2322b215164e9a"></a>

```c
struct net_buf * smp_dummy_get_outgoing (void)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_dummy_get_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gaa744df8e85bdb93cff2322b215164e9a)。

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

<a id="r_ga501596f79e8cf48fa1bb07484966fe53"></a>

```c
bool smp_dummy_wait_for_data (uint32_t wait_time_s)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_dummy_wait_for_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga501596f79e8cf48fa1bb07484966fe53)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

<a id="r_gab5a47cd08e9467c969cbee9c85dcfe8a"></a>

```c
void smp_dummy_add_data (void)
```

相关声明：[smp_dummy_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gab5a47cd08e9467c969cbee9c85dcfe8a)。

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="r_gab09b0ae8ed526252b4900e77afa57dc5"></a>

```c
uint16_t smp_dummy_get_send_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_dummy_get_send_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gab09b0ae8ed526252b4900e77afa57dc5)。

获取当前发送缓冲区位置（Send Buffer Position）。

<a id="r_ga71158b7a935497506a6cc9e2f40a2b1e"></a>

```c
uint16_t smp_dummy_get_receive_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_dummy_get_receive_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga71158b7a935497506a6cc9e2f40a2b1e)。

获取当前接收缓冲区位置（Receive Buffer Position）。

<a id="r_ga5440421e4994119fc98ec119706e4dd9"></a>

```c
int smp_dummy_tx_pkt (const uint8_t *data, int len)
```

相关声明：[smp_dummy_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga5440421e4994119fc98ec119706e4dd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

<a id="r_gadde2de8dc7895bda0e5d72a961dfba78"></a>

```c
void smp_dummy_enable (void)
```

相关声明：[smp_dummy_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gadde2de8dc7895bda0e5d72a961dfba78)。

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="r_ga57d38b86c8b826ef1d49bcae0565b772"></a>

```c
void smp_dummy_disable (void)
```

相关声明：[smp_dummy_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga57d38b86c8b826ef1d49bcae0565b772)。

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="r_ga364817f12c377c6538867c6118d071c6"></a>

```c
bool smp_dummy_get_status (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_dummy_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga364817f12c377c6538867c6118d071c6)。

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。


## 38.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](../api_source_reference/P521_mgmt.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/transport/serial.h](../api_source_reference/P770_serial.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P796_smp_dummy.h_源码浏览.md)
- [smp_dummy_clear_state](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gad9b3c7f35e4fa24fe863145a687f53db)
- [dummy_mcumgr_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga8bf3d0c12669c2cf5370eb7e148f10c2)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [smp_dummy_get_outgoing](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gaa744df8e85bdb93cff2322b215164e9a)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [smp_dummy_wait_for_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga501596f79e8cf48fa1bb07484966fe53)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [smp_dummy_add_data](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gab5a47cd08e9467c969cbee9c85dcfe8a)
- [smp_dummy_get_send_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gab09b0ae8ed526252b4900e77afa57dc5)
- [smp_dummy_get_receive_pos](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga71158b7a935497506a6cc9e2f40a2b1e)
- [smp_dummy_tx_pkt](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga5440421e4994119fc98ec119706e4dd9)
- [smp_dummy_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#gadde2de8dc7895bda0e5d72a961dfba78)
- [smp_dummy_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga57d38b86c8b826ef1d49bcae0565b772)
- [smp_dummy_get_status](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html#ga364817f12c377c6538867c6118d071c6)

<a id="header-details"></a>

---

[上一章](P037_zephyr__drivers__sensor__mcux_acmp.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P039_zephyr__mgmt__mcumgr__transport__smp_raw_dummy.h_文件参考.md)
