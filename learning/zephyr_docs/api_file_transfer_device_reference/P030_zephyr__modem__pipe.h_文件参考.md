---
id: learning.zephyr-docs.api-file-transfer-device-reference.page-30
title: zephyr__modem__pipe.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第30章\_zephyr\_\_modem\_\_pipe.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/pipe_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 30.1\_数据结构（Data Structures）

<a id="r_modem_5Fpipe_5Fdata_5Ffragment"></a>

```c
struct modem_pipe_data_fragment
```

相关声明：[modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)。

多部分数据（Multi-Part Data）的片段。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 30.2\_类型定义（Typedefs）

<a id="r_gaf64941177c179cb9086a5736d1ea56f1"></a>

```c
typedef void(* modem_pipe_api_callback) (struct modem_pipe *pipe, enum modem_pipe_event event, void *user_data)
```

相关声明：[modem_pipe_api_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gaf64941177c179cb9086a5736d1ea56f1)、[modem_pipe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab9dd98d92d6446dd43852d280574f67a)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 30.3\_枚举（Enumerations）

<a id="r_gab9dd98d92d6446dd43852d280574f67a"></a>

```c
enum modem_pipe_event { MODEM_PIPE_EVENT_OPENED = 0 , MODEM_PIPE_EVENT_RECEIVE_READY , MODEM_PIPE_EVENT_TRANSMIT_IDLE , MODEM_PIPE_EVENT_CLOSED }
```

相关声明：[modem_pipe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab9dd98d92d6446dd43852d280574f67a)、[MODEM_PIPE_EVENT_OPENED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891)、[MODEM_PIPE_EVENT_RECEIVE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4)、[MODEM_PIPE_EVENT_TRANSMIT_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4)、[MODEM_PIPE_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f)。

调制解调器管道事件（Modem Pipe Event）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 30.4\_函数（Functions）

<a id="r_ga7521ac0aeda8027c47741237e8312bf0"></a>

```c
int modem_pipe_open (struct modem_pipe *pipe, k_timeout_t timeout)
```

相关声明：[modem_pipe_open](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga7521ac0aeda8027c47741237e8312bf0)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

打开管道（Pipe）。

<a id="r_ga0a7312eadaa76b433fe8a319d8c9ec74"></a>

```c
int modem_pipe_open_async (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_open_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga0a7312eadaa76b433fe8a319d8c9ec74)。

异步（Asynchronously）打开管道（Pipe）。

<a id="r_ga68674becf672b1009d629813c041b868"></a>

```c
void modem_pipe_attach (struct modem_pipe *pipe, modem_pipe_api_callback callback, void *user_data)
```

相关声明：[modem_pipe_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga68674becf672b1009d629813c041b868)、[modem_pipe_api_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gaf64941177c179cb9086a5736d1ea56f1)。

将管道（Pipe）与回调（Callback）关联。

<a id="r_gad181c9ee83b2294fb3fd16b690660926"></a>

```c
int modem_pipe_transmit_chain (struct modem_pipe *pipe, const struct modem_pipe_data_fragment *frags, size_t num_frags)
```

相关声明：[modem_pipe_transmit_chain](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad181c9ee83b2294fb3fd16b690660926)、[modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)。

通过管道（Pipe）发送数据缓冲区链（Chain of Data Buffers）。

<a id="r_gab1f1a3a37779900730c5ffad1aea3c7c"></a>

```c
static int modem_pipe_transmit (struct modem_pipe *pipe, const uint8_t *buf, size_t size)
```

相关声明：[modem_pipe_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab1f1a3a37779900730c5ffad1aea3c7c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过管道（Pipe）发送数据。

<a id="r_gab030b4040725ad4dab2399840ef73fde"></a>

```c
int modem_pipe_receive (struct modem_pipe *pipe, uint8_t *buf, size_t size)
```

相关声明：[modem_pipe_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab030b4040725ad4dab2399840ef73fde)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

通过管道（Pipe）接收数据。

<a id="r_gad1a9fa3dba49a86c187328b7ee022293"></a>

```c
void modem_pipe_release (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad1a9fa3dba49a86c187328b7ee022293)。

清除回调（Callback）。

<a id="r_ga4f5d30e87bb252c4e38ce2e3b10e78c5"></a>

```c
int modem_pipe_close (struct modem_pipe *pipe, k_timeout_t timeout)
```

相关声明：[modem_pipe_close](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga4f5d30e87bb252c4e38ce2e3b10e78c5)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

关闭管道（Pipe）。

<a id="r_ga9814c9a1a5da33b2787ac058a6a037f5"></a>

```c
int modem_pipe_close_async (struct modem_pipe *pipe)
```

相关声明：[modem_pipe_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga9814c9a1a5da33b2787ac058a6a037f5)。

异步（Asynchronously）关闭管道（Pipe）。


## 30.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P145_pipe.h_源码浏览.md)
- [modem_pipe_data_fragment](../modem_wireless_model_reference/P060_modem_pipe_data_fragment_结构体.md)
- [modem_pipe_api_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gaf64941177c179cb9086a5736d1ea56f1)
- [modem_pipe_event](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab9dd98d92d6446dd43852d280574f67a)
- [MODEM_PIPE_EVENT_OPENED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa68d9924c9fc58cf9ca8760573d32f891)
- [MODEM_PIPE_EVENT_RECEIVE_READY](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aa6687ded90e569690afc72020e78624c4)
- [MODEM_PIPE_EVENT_TRANSMIT_IDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aaa6e11b11afb91ec50c4d0dfb363e7ad4)
- [MODEM_PIPE_EVENT_CLOSED](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ggab9dd98d92d6446dd43852d280574f67aae3ed9618f4986a7c3bef59e16a61316f)
- [modem_pipe_open](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga7521ac0aeda8027c47741237e8312bf0)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [modem_pipe_open_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga0a7312eadaa76b433fe8a319d8c9ec74)
- [modem_pipe_attach](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga68674becf672b1009d629813c041b868)
- [modem_pipe_transmit_chain](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad181c9ee83b2294fb3fd16b690660926)
- [modem_pipe_transmit](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab1f1a3a37779900730c5ffad1aea3c7c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [modem_pipe_receive](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gab030b4040725ad4dab2399840ef73fde)
- [modem_pipe_release](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#gad1a9fa3dba49a86c187328b7ee022293)
- [modem_pipe_close](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga4f5d30e87bb252c4e38ce2e3b10e78c5)
- [modem_pipe_close_async](https://docs.zephyrproject.org/latest/doxygen/html/group__modem__pipe.html#ga9814c9a1a5da33b2787ac058a6a037f5)

---

[上一章](P029_zephyr__drivers__pinctrl__pinctrl_rcar_x5h_common.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P031_zephyr__modem__pipelink.h_文件参考.md)
