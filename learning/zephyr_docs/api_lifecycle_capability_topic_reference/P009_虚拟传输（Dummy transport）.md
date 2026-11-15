---
id: learning.zephyr-docs.api-lifecycle-capability-topic-reference.page-9
title: 虚拟传输（Dummy transport）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_虚拟传输（Dummy transport）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__transport__dummy.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

允许通过虚拟传输使用 MCUmgr SMP 协议，通常用于测试。

<a id="details"></a>

允许通过虚拟传输使用 MCUmgr SMP 协议，通常用于测试。

<a id="header-files"></a>
<a id="files"></a>

## 9.1\_文件（Files）

<a id="r_smp_5Fdummy_2Eh"></a>

```c
file smp_dummy.h
```

相关声明：[smp_dummy.h](../api_file_system_power_reference/P038_zephyr__mgmt__mcumgr__transport__smp_dummy.h_文件参考.md)。

供单元测试使用的mcumgr简单管理协议（SMP）虚拟传输。

<a id="r_smp_5Fraw_5Fdummy_2Eh"></a>

```c
file smp_raw_dummy.h
```

相关声明：[smp_raw_dummy.h](../api_file_system_power_reference/P039_zephyr__mgmt__mcumgr__transport__smp_raw_dummy.h_文件参考.md)。

供单元测试使用的mcumgr简单管理协议（SMP）虚拟传输。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.2\_函数（Functions）

<a id="r_gad9b3c7f35e4fa24fe863145a687f53db"></a>

```c
void smp_dummy_clear_state (void)
```

相关声明：[smp_dummy_clear_state](#gad9b3c7f35e4fa24fe863145a687f53db)。

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="r_ga8bf3d0c12669c2cf5370eb7e148f10c2"></a>

```c
void dummy_mcumgr_add_data (uint8_t *data, uint16_t data_size)
```

相关声明：[dummy_mcumgr_add_data](#ga8bf3d0c12669c2cf5370eb7e148f10c2)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

<a id="r_gaa744df8e85bdb93cff2322b215164e9a"></a>

```c
struct net_buf * smp_dummy_get_outgoing (void)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_dummy_get_outgoing](#gaa744df8e85bdb93cff2322b215164e9a)。

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

<a id="r_ga501596f79e8cf48fa1bb07484966fe53"></a>

```c
bool smp_dummy_wait_for_data (uint32_t wait_time_s)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_dummy_wait_for_data](#ga501596f79e8cf48fa1bb07484966fe53)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

<a id="r_gab5a47cd08e9467c969cbee9c85dcfe8a"></a>

```c
void smp_dummy_add_data (void)
```

相关声明：[smp_dummy_add_data](#gab5a47cd08e9467c969cbee9c85dcfe8a)。

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="r_gab09b0ae8ed526252b4900e77afa57dc5"></a>

```c
uint16_t smp_dummy_get_send_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_dummy_get_send_pos](#gab09b0ae8ed526252b4900e77afa57dc5)。

获取当前发送缓冲区位置（Send Buffer Position）。

<a id="r_ga71158b7a935497506a6cc9e2f40a2b1e"></a>

```c
uint16_t smp_dummy_get_receive_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_dummy_get_receive_pos](#ga71158b7a935497506a6cc9e2f40a2b1e)。

获取当前接收缓冲区位置（Receive Buffer Position）。

<a id="r_ga5440421e4994119fc98ec119706e4dd9"></a>

```c
int smp_dummy_tx_pkt (const uint8_t *data, int len)
```

相关声明：[smp_dummy_tx_pkt](#ga5440421e4994119fc98ec119706e4dd9)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

<a id="r_gadde2de8dc7895bda0e5d72a961dfba78"></a>

```c
void smp_dummy_enable (void)
```

相关声明：[smp_dummy_enable](#gadde2de8dc7895bda0e5d72a961dfba78)。

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="r_ga57d38b86c8b826ef1d49bcae0565b772"></a>

```c
void smp_dummy_disable (void)
```

相关声明：[smp_dummy_disable](#ga57d38b86c8b826ef1d49bcae0565b772)。

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="r_ga364817f12c377c6538867c6118d071c6"></a>

```c
bool smp_dummy_get_status (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_dummy_get_status](#ga364817f12c377c6538867c6118d071c6)。

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。

<a id="r_ga5e8c496f45a4ef5b67c033681900f167"></a>

```c
void smp_raw_dummy_clear_state (void)
```

相关声明：[smp_raw_dummy_clear_state](#ga5e8c496f45a4ef5b67c033681900f167)。

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="r_gac582aaa484eee63b36ab94739640b1dc"></a>

```c
void smp_raw_dummy_mcumgr_add_data (uint8_t *data, uint16_t data_size)
```

相关声明：[smp_raw_dummy_mcumgr_add_data](#gac582aaa484eee63b36ab94739640b1dc)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

<a id="r_gafebbc255c07f6c08e15509118ab76f6a"></a>

```c
struct net_buf * smp_raw_dummy_get_outgoing (void)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_raw_dummy_get_outgoing](#gafebbc255c07f6c08e15509118ab76f6a)。

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

<a id="r_ga0ac2b264ccfbdd4861f162107f23fead"></a>

```c
bool smp_raw_dummy_wait_for_data (uint32_t wait_time_s)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_raw_dummy_wait_for_data](#ga0ac2b264ccfbdd4861f162107f23fead)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

<a id="r_gaa9c6ca2056062644fcb1db97755ff311"></a>

```c
void smp_raw_dummy_add_data (void)
```

相关声明：[smp_raw_dummy_add_data](#gaa9c6ca2056062644fcb1db97755ff311)。

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="r_gacb4b4948718df4c5ce13a27faca895b7"></a>

```c
uint16_t smp_raw_dummy_get_send_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_raw_dummy_get_send_pos](#gacb4b4948718df4c5ce13a27faca895b7)。

获取当前发送缓冲区位置（Send Buffer Position）。

<a id="r_ga2ddb5a7110046d6122dfce8d5ddab343"></a>

```c
uint16_t smp_raw_dummy_get_receive_pos (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[smp_raw_dummy_get_receive_pos](#ga2ddb5a7110046d6122dfce8d5ddab343)。

获取当前接收缓冲区位置（Receive Buffer Position）。

<a id="r_gac2682f29403a437d2d7d50f1d069b742"></a>

```c
int smp_raw_dummy_tx_pkt (const uint8_t *data, int len)
```

相关声明：[smp_raw_dummy_tx_pkt](#gac2682f29403a437d2d7d50f1d069b742)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

<a id="r_ga58c6308491208020db01f09bff424465"></a>

```c
void smp_raw_dummy_enable (void)
```

相关声明：[smp_raw_dummy_enable](#ga58c6308491208020db01f09bff424465)。

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="r_gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d"></a>

```c
void smp_raw_dummy_disable (void)
```

相关声明：[smp_raw_dummy_disable](#gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d)。

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="r_ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f"></a>

```c
bool smp_raw_dummy_get_status (void)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_raw_dummy_get_status](#ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f)。

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。

## 9.3\_详细说明（Detailed Documentation）

<a id="ga8bf3d0c12669c2cf5370eb7e148f10c2"></a>

### `dummy_mcumgr_add_data()`

```c
void dummy_mcumgr_add_data ( uint8_t * data, uint16_t data_size )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 输入数据缓冲区（Input Data Buffer）。 |
| `data_size` | 数据大小，以字节为单位。 |

<a id="gab5a47cd08e9467c969cbee9c85dcfe8a"></a>

### `smp_dummy_add_data()`

```c
void smp_dummy_add_data ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="gad9b3c7f35e4fa24fe863145a687f53db"></a>

### `smp_dummy_clear_state()`

```c
void smp_dummy_clear_state ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="ga57d38b86c8b826ef1d49bcae0565b772"></a>

### `smp_dummy_disable()`

```c
void smp_dummy_disable ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="gadde2de8dc7895bda0e5d72a961dfba78"></a>

### `smp_dummy_enable()`

```c
void smp_dummy_enable ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="gaa744df8e85bdb93cff2322b215164e9a"></a>

### `smp_dummy_get_outgoing()`

```c
struct net_buf * smp_dummy_get_outgoing ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `net` | 处理后数据的缓冲区（Buffer of Processed Data）。 |

<a id="ga71158b7a935497506a6cc9e2f40a2b1e"></a>

### `smp_dummy_get_receive_pos()`

```c
uint16_t smp_dummy_get_receive_pos ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

获取当前接收缓冲区位置（Receive Buffer Position）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Current` | 接收缓冲区位置（Receive Buffer Position），单位为字节。 |

<a id="gab09b0ae8ed526252b4900e77afa57dc5"></a>

### `smp_dummy_get_send_pos()`

```c
uint16_t smp_dummy_get_send_pos ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

获取当前发送缓冲区位置（Send Buffer Position）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Current` | 发送缓冲区位置（Send Buffer Position），单位为字节。 |

<a id="ga364817f12c377c6538867c6118d071c6"></a>

### `smp_dummy_get_status()`

```c
bool smp_dummy_get_status ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 模拟 SMP（Dummy SMP）已启用时；否则为 `false`。 |

<a id="ga5440421e4994119fc98ec119706e4dd9"></a>

### `smp_dummy_tx_pkt()`

```c
int smp_dummy_tx_pkt ( const uint8_t * data, int len )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 输入数据缓冲区（Input Data Buffer）。 |
| `len` | 数据大小，以字节为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga501596f79e8cf48fa1bb07484966fe53"></a>

### `smp_dummy_wait_for_data()`

```c
bool smp_dummy_wait_for_data ( uint32_t wait_time_s)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_dummy.h>
```

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wait_time_s` | 等待数据的时间（Time to Wait），单位为秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 成功收到消息时；超时返回 `false`。 |

<a id="gaa9c6ca2056062644fcb1db97755ff311"></a>

### `smp_raw_dummy_add_data()`

```c
void smp_raw_dummy_add_data ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

使用内部 SMPC 接收缓冲区（Receive Buffer）调用 `dummy_mcumgr_add_data`。

<a id="ga5e8c496f45a4ef5b67c033681900f167"></a>

### `smp_raw_dummy_clear_state()`

```c
void smp_raw_dummy_clear_state ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

清除内部模拟 SMP 状态（Dummy SMP State），并复位信号量（Semaphore）。

<a id="gadf6a0a6ccb5a5ecdd5b4f323b4f7ee7d"></a>

### `smp_raw_dummy_disable()`

```c
void smp_raw_dummy_disable ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

禁用模拟 SMP 模块（Dummy SMP Module），使其不处理发送／接收的数据。

<a id="ga58c6308491208020db01f09bff424465"></a>

### `smp_raw_dummy_enable()`

```c
void smp_raw_dummy_enable ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

启用模拟 SMP 模块（Dummy SMP Module），使其处理发送／接收的数据。

<a id="gafebbc255c07f6c08e15509118ab76f6a"></a>

### `smp_raw_dummy_get_outgoing()`

```c
struct net_buf * smp_raw_dummy_get_outgoing ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

处理来自 mcumgr 响应的一行（分片，Fragment），供测试使用。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `net` | 处理后数据的缓冲区（Buffer of Processed Data）。 |

<a id="ga2ddb5a7110046d6122dfce8d5ddab343"></a>

### `smp_raw_dummy_get_receive_pos()`

```c
uint16_t smp_raw_dummy_get_receive_pos ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

获取当前接收缓冲区位置（Receive Buffer Position）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Current` | 接收缓冲区位置（Receive Buffer Position），单位为字节。 |

<a id="gacb4b4948718df4c5ce13a27faca895b7"></a>

### `smp_raw_dummy_get_send_pos()`

```c
uint16_t smp_raw_dummy_get_send_pos ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

获取当前发送缓冲区位置（Send Buffer Position）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Current` | 发送缓冲区位置（Send Buffer Position），单位为字节。 |

<a id="ga9ff3bb7e8e4e0fdc5c4e8826ab660b4f"></a>

### `smp_raw_dummy_get_status()`

```c
bool smp_raw_dummy_get_status ( void )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

返回模拟 SMP 系统（Dummy SMP System）是否处于活动状态（Active）。

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 模拟 SMP（Dummy SMP）已启用时；否则为 `false`。 |

<a id="gac582aaa484eee63b36ab94739640b1dc"></a>

### `smp_raw_dummy_mcumgr_add_data()`

```c
void smp_raw_dummy_mcumgr_add_data ( uint8_t * data, uint16_t data_size )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

将 SMPC 数据加入内部缓冲区（Internal Buffer），以供处理。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 输入数据缓冲区（Input Data Buffer）。 |
| `data_size` | 数据大小，以字节为单位。 |

<a id="gac2682f29403a437d2d7d50f1d069b742"></a>

### `smp_raw_dummy_tx_pkt()`

```c
int smp_raw_dummy_tx_pkt ( const uint8_t * data, int len )
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

转换输入数据，使其通过内部 SMPC 缓冲区（Buffer）发送。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | 输入数据缓冲区（Input Data Buffer）。 |
| `len` | 数据大小，以字节为单位。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时；出错时为负值（Negative）。 |

<a id="ga0ac2b264ccfbdd4861f162107f23fead"></a>

### `smp_raw_dummy_wait_for_data()`

```c
bool smp_raw_dummy_wait_for_data ( uint32_t wait_time_s)
```

```c
#include <zephyr/mgmt/mcumgr/transport/smp_raw_dummy.h>
```

等待一段时间，直到待发送 SMPC 数据就绪；完整消息就绪或超时时返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `wait_time_s` | 等待数据的时间（Time to Wait），单位为秒。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `true` | 成功收到消息时；超时返回 `false`。 |


## 9.4\_原页交叉引用（Cross References）

- [smp_dummy.h](../api_file_system_power_reference/P038_zephyr__mgmt__mcumgr__transport__smp_dummy.h_文件参考.md)
- [smp_raw_dummy.h](../api_file_system_power_reference/P039_zephyr__mgmt__mcumgr__transport__smp_raw_dummy.h_文件参考.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [true](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#a41f9c5fb8b08eb5dc3edce4dcb37fee7)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P008_操作系统管理（OS Management）.md) · [返回大纲](大纲.md) · [下一章](P010_页面淘汰算法 API（Eviction Algorithm APIs）.md)
