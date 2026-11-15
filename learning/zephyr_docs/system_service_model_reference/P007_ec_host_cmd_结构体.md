---
id: learning.zephyr-docs.system-service-model-reference.page-7
title: ec_host_cmd_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_ec\_host\_cmd\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

主机命令（Host Command）的上下文结构。

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

<a id="details"></a>

主机命令（Host Command）的上下文结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a1f5153ec8442ae8c70d4918ff21b908e"></a>

```c
struct ec_host_cmd_rx_ctx rx_ctx
```

相关声明：[ec_host_cmd_rx_ctx](P014_ec_host_cmd_rx_ctx_结构体.md)、[rx_ctx](#a1f5153ec8442ae8c70d4918ff21b908e)。

用于传递从主机收到的数据的上下文（context）。

<a id="r_af1a3f483c1a7ddb88db187e406caa08d"></a>

```c
struct ec_host_cmd_tx_buf tx
```

相关声明：[ec_host_cmd_tx_buf](P015_ec_host_cmd_tx_buf_结构体.md)、[tx](#af1a3f483c1a7ddb88db187e406caa08d)。

用于向主机发送响应的缓冲区。

<a id="r_ad269f3223fc0885ba5c847b4443c993c"></a>

```c
struct ec_host_cmd_backend * backend
```

相关声明：[ec_host_cmd_backend](P008_ec_host_cmd_backend_结构体.md)、[backend](#ad269f3223fc0885ba5c847b4443c993c)。

用于与主机通信的后端（backend）。

<a id="r_a465d588b50f0a881e7f1d8b761c4288f"></a>

```c
struct k_sem rx_ready
```

相关声明：[k_sem](../synchronization_reference/P009_内核信号量结构.md)、[rx_ready](#a465d588b50f0a881e7f1d8b761c4288f)。

当 `rx_ctx` 中的数据准备好时，后端通过调用 `ec_host_cmd_send_receive` 函数释放 `rx_ready`。

译注：官方原文此处使用 `ec_host_cmd_send_receive`；本页其他说明使用 `ec_host_cmd_send_received`，这里保留原文的函数名差异供对照。

<a id="r_a0e50770725cd93b0923769b3b650b04d"></a>

```c
enum ec_host_cmd_status rx_status
```

相关声明：[ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)、[rx_status](#a0e50770725cd93b0923769b3b650b04d)。

在 `ec_host_cmd_send_received` 函数中检查的接收数据状态。

<a id="r_ad2f10eda2e6c2743d9c3068bda4deb7c"></a>

```c
ec_host_cmd_user_cb_t user_cb
```

相关声明：[ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)、[user_cb](#ad2f10eda2e6c2743d9c3068bda4deb7c)。

接收到命令后的用户回调。

<a id="r_a7982f079e67180de58ebd0a6f0f5d7e0"></a>

```c
void * user_data
```

相关声明：[user_data](#a7982f079e67180de58ebd0a6f0f5d7e0)。

传给 `user_cb` 的用户数据。

<a id="r_a444f295157c5ada6162aea803ff219e1"></a>

```c
enum ec_host_cmd_state state
```

相关声明：[ec_host_cmd_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gabf0f1243bf55cb70078f2a9fd0a755ec)、[state](#a444f295157c5ada6162aea803ff219e1)。

主机命令处理器（host command handler）的当前状态。

<a id="r_a642d1b4e2325be11fcb628855c89cead"></a>

```c
k_tid_t thread
```

相关声明：[k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)、[thread](#a642d1b4e2325be11fcb628855c89cead)。

运行主机命令处理循环的线程。

## 7.2\_详细说明（Detailed Documentation）

<a id="ad269f3223fc0885ba5c847b4443c993c"></a>

### `backend`

```c
struct ec_host_cmd_backend* ec_host_cmd::backend
```

用于与主机通信的后端（backend）。

<a id="a1f5153ec8442ae8c70d4918ff21b908e"></a>

### `rx_ctx`

```c
struct ec_host_cmd_rx_ctx ec_host_cmd::rx_ctx
```

用于传递从主机收到的数据的上下文（context）。

<a id="a465d588b50f0a881e7f1d8b761c4288f"></a>

### `rx_ready`

```c
struct k_sem ec_host_cmd::rx_ready
```

当 `rx_ctx` 中的数据准备好时，后端通过调用 `ec_host_cmd_send_receive` 函数释放 `rx_ready`。

译注：官方原文此处使用 `ec_host_cmd_send_receive`；本页其他说明使用 `ec_host_cmd_send_received`，这里保留原文的函数名差异供对照。

处理器获取 `rx_ready` 后读取 `rx_ctx` 中的数据。

<a id="a0e50770725cd93b0923769b3b650b04d"></a>

### `rx_status`

```c
enum ec_host_cmd_status ec_host_cmd::rx_status
```

在 `ec_host_cmd_send_received` 函数中检查的接收数据状态。

<a id="a444f295157c5ada6162aea803ff219e1"></a>

### `state`

```c
enum ec_host_cmd_state ec_host_cmd::state
```

主机命令处理器（host command handler）的当前状态。

<a id="a642d1b4e2325be11fcb628855c89cead"></a>

### `thread`

```c
k_tid_t ec_host_cmd::thread
```

运行主机命令处理循环的线程。

<a id="af1a3f483c1a7ddb88db187e406caa08d"></a>

### `tx`

```c
struct ec_host_cmd_tx_buf ec_host_cmd::tx
```

用于向主机发送响应的缓冲区。

<a id="ad2f10eda2e6c2743d9c3068bda4deb7c"></a>

### `user_cb`

```c
ec_host_cmd_user_cb_t ec_host_cmd::user_cb
```

接收到命令后的用户回调。

由 `ec_host_cmd_send_received` 函数调用。

<a id="a7982f079e67180de58ebd0a6f0f5d7e0"></a>

### `user_data`

```c
void* ec_host_cmd::user_data
```

传给 `user_cb` 的用户数据。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/ec_host_cmd.h`

## 7.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/ec_host_cmd.h](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)
- [ec_host_cmd_rx_ctx](P014_ec_host_cmd_rx_ctx_结构体.md)
- [ec_host_cmd_tx_buf](P015_ec_host_cmd_tx_buf_结构体.md)
- [ec_host_cmd_backend](P008_ec_host_cmd_backend_结构体.md)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)
- [ec_host_cmd_user_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gaa6ea251ee113cc15fd085ef12b76a573)
- [ec_host_cmd_state](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#gabf0f1243bf55cb70078f2a9fd0a755ec)
- [k_tid_t](../thread_core_reference/P002_线程头文件参考.md#a6379f5a1f19ffbc262a6877c4f6e3647)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_dap_link_context_结构体.md) · [返回大纲](大纲.md) · [下一章](P008_ec_host_cmd_backend_结构体.md)
