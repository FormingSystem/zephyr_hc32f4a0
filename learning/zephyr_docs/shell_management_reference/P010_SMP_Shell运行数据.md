---
id: learning.zephyr-docs.shell-management-reference.page-10
title: SMP_Shell运行数据
kind: reference
status: maintained
domains: [zephyr, shell, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structsmp__shell__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_SMP\_Shell运行数据

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structsmp__shell__data.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入蓝牙Mesh Shell、mcumgr Shell管理与SMP传输接口。源码跟踪译注与官方原文分开标示。

SMP Shell使用的数据。

```c
#include <zephyr/mgmt/mcumgr/transport/smp_shell.h>
```

<a id="details"></a>

SMP Shell使用的数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 10.1\_数据成员（Data Fields）

<a id="r_a67997e0400ee096e98781b839df3d6c2"></a>

```c
struct net_buf_pool * buf_pool
```

相关声明：[net_buf_pool](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html)、[buf_pool](#a67997e0400ee096e98781b839df3d6c2)。

用于接收帧的网络缓冲区池（Network Buffer Pool）。

<a id="r_a3e15c83e64e1cab0f14141d2a6dd7bed"></a>

```c
struct k_fifo buf_ready
```

相关声明：[k_fifo](../queue_reference/P004_内核FIFO结构.md)、[buf_ready](#a3e15c83e64e1cab0f14141d2a6dd7bed)。

已准备好处理的帧的先进先出队列（FIFO）。

<a id="r_a281058a6cb23102af46cb0457c3a3232"></a>

```c
struct net_buf * buf
```

相关声明：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)、[buf](#a281058a6cb23102af46cb0457c3a3232)。

当前活动接收缓冲区（Active Receive Buffer）。

<a id="r_aea6798b62094c9d3bcc3dc6926800af4"></a>

```c
atomic_t esc_state
```

相关声明：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)、[esc_state](#aea6798b62094c9d3bcc3dc6926800af4)。

已经检测到通过控制台承载的SMP帧的哪些部分。

<a id="r_af2a9ec4af7279a114bee4c2cb11a31f3"></a>

```c
const struct shell_uart_common * uart
```

相关声明：[uart](#af2a9ec4af7279a114bee4c2cb11a31f3)。

负责接收的UART Shell对象。

## 10.2\_详细说明（Detailed Documentation）

<a id="a281058a6cb23102af46cb0457c3a3232"></a>

### `buf`

```c
struct net_buf* smp_shell_data::buf
```

当前活动接收缓冲区（Active Receive Buffer）。

<a id="a67997e0400ee096e98781b839df3d6c2"></a>

### `buf_pool`

```c
struct net_buf_pool* smp_shell_data::buf_pool
```

用于接收帧的网络缓冲区池（Network Buffer Pool）。

<a id="a3e15c83e64e1cab0f14141d2a6dd7bed"></a>

### `buf_ready`

```c
struct k_fifo smp_shell_data::buf_ready
```

已准备好处理的帧的先进先出队列（FIFO）。

<a id="aea6798b62094c9d3bcc3dc6926800af4"></a>

### `esc_state`

```c
atomic_t smp_shell_data::esc_state
```

已经检测到通过控制台承载的SMP帧的哪些部分。

<a id="af2a9ec4af7279a114bee4c2cb11a31f3"></a>

### `uart`

```c
const struct shell_uart_common* smp_shell_data::uart
```

负责接收的UART Shell对象。

## 10.3\_源码定位与版本边界

源码定位：[include/zephyr/mgmt/mcumgr/transport/smp_shell.h](../../../include/zephyr/mgmt/mcumgr/transport/smp_shell.h)、[subsys/mgmt/mcumgr/transport/src/smp_shell.c](../../../subsys/mgmt/mcumgr/transport/src/smp_shell.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：rx_bytes的返回值是本次消费的输入字节数，不是完成的帧数，也不是命令执行结果。它扫描到帧或缓冲区末尾为止；完整帧的后续处理由process完成。

> 译注——源码核对：process应在线程上下文调用，并从就绪FIFO取出帧进行处理。活动接收缓冲和已排队帧分别由buf与buf_ready表示，不能把当前缓冲指针非NULL当作整帧已接收的证据。

> 译注——源码核对：接收前先完成smp_shell_init。此初始化与普通Shell实例初始化、具体UART硬件配置属于不同阶段，接口返回0只描述本次初始化结果。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 10.4\_原页交叉引用（Cross References）

- [zephyr/mgmt/mcumgr/transport/smp_shell.h](P009_SMP_Shell头文件源码.md)
- [net_buf_pool](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P009_SMP_Shell头文件源码.md) · [返回大纲](大纲.md)
