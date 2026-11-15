---
id: learning.zephyr-docs.api-video-event-topic-reference.page-6
title: 调制解调器管道（Modem Pipe）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_调制解调器管道（Modem Pipe）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

调制解调器管道（Modem Pipe）

<a id="details"></a>

调制解调器管道（Modem Pipe）。自 3.5 起提供，版本 1.0.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_modem_5Fpipe_5Fdata_5Ffragment"></a>

```c
struct modem_pipe_data_fragment
```

相关声明：[modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)。

多部分数据（Multi-Part Data）的片段。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.2\_类型定义（Typedefs）

<a id="r_gaf64941177c179cb9086a5736d1ea56f1"></a>

```c
typedef void(* modem_pipe_api_callback) (struct modem_pipe *pipe, enum modem_pipe_event event, void *user_data)
```

相关声明：[modem_pipe_api_callback](#gaf64941177c179cb9086a5736d1ea56f1)、[modem_pipe_event](#gab9dd98d92d6446dd43852d280574f67a)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.3\_枚举（Enumerations）

<a id="r_gab9dd98d92d6446dd43852d280574f67a"></a>

```c
enum modem_pipe_event { MODEM_PIPE_EVENT_OPENED = 0 , MODEM_PIPE_EVENT_RECEIVE_READY , MODEM_PIPE_EVENT_TRANSMIT_IDLE , MODEM_PIPE_EVENT_CLOSED }
```

相关声明：[modem_pipe_event](#gab9dd98d92d6446dd43852d280574f67a)、[MODEM_PIPE_EVENT_OPENED](#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891)、[MODEM_PIPE_EVENT_RECEIVE_READY](#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4)、[MODEM_PIPE_EVENT_TRANSMIT_IDLE](#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4)、[MODEM_PIPE_EVENT_CLOSED](#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f)。

调制解调器管道事件（Modem Pipe Event）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_ga7521ac0aeda8027c47741237e8312bf0"></a>

```c
int modem_pipe_open (struct modem_pipe *pipe, k_timeout_t timeout)
```

相关声明：[modem_pipe_open](#ga7521ac0aeda8027c47741237e8312bf0)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

打开管道（Pipe）。

<a id="r_ga0a7312eadaa76b433fe8a319d8c9ec74"></a>

```c
int modem_pipe_open_async (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_open_async](#ga0a7312eadaa76b433fe8a319d8c9ec74)。

异步（Asynchronously）打开管道（Pipe）。

<a id="r_ga68674becf672b1009d629813c041b868"></a>

```c
void modem_pipe_attach (struct modem_pipe *pipe, modem_pipe_api_callback callback, void *user_data)
```

相关声明：[modem_pipe_attach](#ga68674becf672b1009d629813c041b868)、[modem_pipe_api_callback](#gaf64941177c179cb9086a5736d1ea56f1)。

将管道（Pipe）与回调（Callback）关联。

<a id="r_gad181c9ee83b2294fb3fd16b690660926"></a>

```c
int modem_pipe_transmit_chain (struct modem_pipe *pipe, const struct modem_pipe_data_fragment *frags, size_t num_frags)
```

相关声明：[modem_pipe_transmit_chain](#gad181c9ee83b2294fb3fd16b690660926)、[modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)。

通过管道（Pipe）发送数据缓冲区链（Chain of Data Buffers）。

<a id="r_gab1f1a3a37779900730c5ffad1aea3c7c"></a>

```c
static int modem_pipe_transmit (struct modem_pipe *pipe, const uint8_t *buf, size_t size)
```

相关声明：[modem_pipe_transmit](#gab1f1a3a37779900730c5ffad1aea3c7c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过管道（Pipe）发送数据。

<a id="r_gab030b4040725ad4dab2399840ef73fde"></a>

```c
int modem_pipe_receive (struct modem_pipe *pipe, uint8_t *buf, size_t size)
```

相关声明：[modem_pipe_receive](#gab030b4040725ad4dab2399840ef73fde)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过管道（Pipe）接收数据。

<a id="r_gad1a9fa3dba49a86c187328b7ee022293"></a>

```c
void modem_pipe_release (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_release](#gad1a9fa3dba49a86c187328b7ee022293)。

清除回调（Callback）。

<a id="r_ga4f5d30e87bb252c4e38ce2e3b10e78c5"></a>

```c
int modem_pipe_close (struct modem_pipe *pipe, k_timeout_t timeout)
```

相关声明：[modem_pipe_close](#ga4f5d30e87bb252c4e38ce2e3b10e78c5)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

关闭管道（Pipe）。

<a id="r_ga9814c9a1a5da33b2787ac058a6a037f5"></a>

```c
int modem_pipe_close_async (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_close_async](#ga9814c9a1a5da33b2787ac058a6a037f5)。

异步（Asynchronously）关闭管道（Pipe）。

## 6.5\_详细说明（Detailed Documentation）

<a id="gaf64941177c179cb9086a5736d1ea56f1"></a>

### `modem_pipe_api_callback`

```c
typedef void(* modem_pipe_api_callback) (struct modem_pipe *pipe, enum modem_pipe_event event, void *user_data)
```

```c
#include <zephyr/modem/pipe.h>
```

<a id="gab9dd98d92d6446dd43852d280574f67a"></a>

### `modem_pipe_event`

```c
enum modem_pipe_event
```

```c
#include <zephyr/modem/pipe.h>
```

调制解调器管道事件（Modem Pipe Event）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MODEM_PIPE_EVENT_OPENED` |  |
| `MODEM_PIPE_EVENT_RECEIVE_READY` |  |
| `MODEM_PIPE_EVENT_TRANSMIT_IDLE` |  |
| `MODEM_PIPE_EVENT_CLOSED` |  |

<a id="ga68674becf672b1009d629813c041b868"></a>

### `modem_pipe_attach()`

```c
void modem_pipe_attach ( struct modem_pipe * pipe, modem_pipe_api_callback callback, void * user_data )
```

```c
#include <zephyr/modem/pipe.h>
```

将管道（Pipe）与回调（Callback）关联。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |
| `callback` | 管道事件（Pipe Event）发生时调用的回调。 |
| `user_data` | 随回调传递、可由用户自由使用的数据（User Data）。 |

**说明（Note）**：注意：若管道已有待接收数据，将立即触发 `MODEM_PIPE_EVENT_RECEIVE_READY` 事件。

<a id="ga4f5d30e87bb252c4e38ce2e3b10e78c5"></a>

### `modem_pipe_close()`

```c
int modem_pipe_close ( struct modem_pipe * pipe, k_timeout_t timeout )
```

```c
#include <zephyr/modem/pipe.h>
```

关闭管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |
| `timeout` | 等待管道关闭的超时（Timeout）。 |

**返回（Returns）**：返回值：管道已成功关闭或原本已关闭时返回 0，否则返回负 errno 值。译注：官方原句的 `pipe open was called closed` 存在措辞错误，此处按关闭接口语境翻译。

**警告（Warning）**：警告：谨慎使用此同步调用（Synchronous Call）。它可能阻塞调用线程；若在线程所属的系统工作队列（System Workqueue）中调用，可能产生死锁，直到等待管道关闭的调用超时。

<a id="ga9814c9a1a5da33b2787ac058a6a037f5"></a>

### `modem_pipe_close_async()`

```c
int modem_pipe_close_async ( struct modem_pipe * pipe)
```

```c
#include <zephyr/modem/pipe.h>
```

异步（Asynchronously）关闭管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |

**说明（Note）**：注意：若管道已经关闭，将立即触发 `MODEM_PIPE_EVENT_CLOSED` 事件。

**返回（Returns）**：返回值：管道关闭调用成功或管道原本已关闭时返回 0，否则返回负 errno 值。

<a id="ga7521ac0aeda8027c47741237e8312bf0"></a>

### `modem_pipe_open()`

```c
int modem_pipe_open ( struct modem_pipe * pipe, k_timeout_t timeout )
```

```c
#include <zephyr/modem/pipe.h>
```

打开管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |
| `timeout` | 等待管道打开的超时（Timeout）。 |

**返回（Returns）**：返回值：管道成功打开或原本已打开时返回 0，否则返回负 errno 值。

**警告（Warning）**：警告：谨慎使用此同步调用（Synchronous Call）。它可能阻塞调用线程；若在系统工作队列（System Workqueue）中调用，可能产生死锁，直到等待管道打开的调用超时。

<a id="ga0a7312eadaa76b433fe8a319d8c9ec74"></a>

### `modem_pipe_open_async()`

```c
int modem_pipe_open_async ( struct modem_pipe * pipe)
```

```c
#include <zephyr/modem/pipe.h>
```

异步（Asynchronously）打开管道（Pipe）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |

**说明（Note）**：注意：若管道已经打开，将立即触发 `MODEM_PIPE_EVENT_OPENED` 事件。

**返回（Returns）**：返回值：管道打开调用成功或管道原本已打开时返回 0，否则返回负 errno 值。

<a id="gab030b4040725ad4dab2399840ef73fde"></a>

### `modem_pipe_receive()`

```c
int modem_pipe_receive ( struct modem_pipe * pipe, uint8_t * buf, size_t size )
```

```c
#include <zephyr/modem/pipe.h>
```

通过管道（Pipe）接收数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 要从中接收数据的管道（Pipe）。 |
| `buf` | 接收数据的目标区域（Destination），不得已被某个调制解调器模块使用。 |
| `size` | 接收数据目标区域的容量（Capacity）。 |

**返回（Returns）**：返回值：从管道接收的字节数，管道关闭时为 0；出错时返回负 errno 值。

**警告（Warning）**：警告：此调用必须是非阻塞的（Non-blocking）。

<a id="gad1a9fa3dba49a86c187328b7ee022293"></a>

### `modem_pipe_release()`

```c
void modem_pipe_release ( struct modem_pipe * pipe)
```

```c
#include <zephyr/modem/pipe.h>
```

清除回调（Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 管道实例（Pipe Instance）。 |

<a id="gab1f1a3a37779900730c5ffad1aea3c7c"></a>

### `modem_pipe_transmit()`

```c
int modem_pipe_transmit ( struct modem_pipe * pipe, const uint8_t * buf, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/modem/pipe.h>
```

通过管道（Pipe）发送数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 用于发送的管道（Pipe）。 |
| `buf` | 要发送的数据（Data）。 |
| `size` | 要发送的字节数。 |

**返回（Returns）**：返回值：放入管道的字节数，管道关闭时为 0；出错时返回负 errno 值。

**警告（Warning）**：警告：此调用必须是非阻塞的（Non-blocking）。

<a id="gad181c9ee83b2294fb3fd16b690660926"></a>

### `modem_pipe_transmit_chain()`

```c
int modem_pipe_transmit_chain ( struct modem_pipe * pipe, const struct modem_pipe_data_fragment * frags, size_t num_frags )
```

```c
#include <zephyr/modem/pipe.h>
```

通过管道（Pipe）发送数据缓冲区链（Chain of Data Buffers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pipe` | 用于发送的管道（Pipe）。 |
| `frags` | 要发送的数据片段数组（Data Fragment Array）。 |
| `num_frags` | `frags` 中的片段数量（Number of Fragments）。 |

**返回（Returns）**：返回值：放入管道的字节数，管道关闭时为 0；出错时返回负 errno 值。

**警告（Warning）**：警告：此调用必须是非阻塞的（Non-blocking）。


## 6.6\_原页交叉引用（Cross References）

- [modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [zephyr/modem/pipe.h](../api_file_transfer_device_reference/P030_zephyr__modem__pipe.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891"></a>
<a id="ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4"></a>
<a id="ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4"></a>
<a id="ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_数字可寻址照明接口（DALI）.md) · [返回大纲](大纲.md) · [下一章](P007_消息（Messages）.md)
