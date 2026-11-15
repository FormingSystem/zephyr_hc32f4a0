---
id: learning.zephyr-docs.shell-management-reference.page-9
title: SMP_Shell头文件源码
kind: reference
status: maintained
domains: [zephyr, shell, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/smp__shell_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_SMP\_Shell头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/smp__shell_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P008_SMP_Shell头文件参考.md)和[公共接口](P007_mcumgr_Shell传输接口.md)；访问语义和生命周期见本页译注。

## 9.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00033"></a>
<a id="adevice_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__mcumgr__transport__shell_html_ga1b71c4da07049b47269002ef6ec2b256"></a>
<a id="agroup__mcumgr__transport__shell_html_ga44b90f6ba276d8d7a89d6b90c8bb0341"></a>
<a id="agroup__mcumgr__transport__shell_html_ga785293b670fcc10190e6c3d480a7d6d6"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructk__fifo_html"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructsmp__shell__data_html"></a>
<a id="astructsmp__shell__data_html_a281058a6cb23102af46cb0457c3a3232"></a>
<a id="astructsmp__shell__data_html_a3e15c83e64e1cab0f14141d2a6dd7bed"></a>
<a id="astructsmp__shell__data_html_a67997e0400ee096e98781b839df3d6c2"></a>
<a id="astructsmp__shell__data_html_aea6798b62094c9d3bcc3dc6926800af4"></a>
<a id="astructsmp__shell__data_html_af2a9ec4af7279a114bee4c2cb11a31f3"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2019 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_SHELL_H_
<a id="l00013"></a>#define ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_SHELL_H_
<a id="l00014"></a>
<a id="l00021"></a>
<a id="l00022"></a>#include &lt;zephyr/device.h&gt;
<a id="l00023"></a>#include &lt;zephyr/kernel.h&gt;
<a id="l00024"></a>#include &lt;zephyr/types.h&gt;
<a id="l00025"></a>
<a id="l00026"></a>#ifdef __cplusplus
<a id="l00027"></a>extern "C" {
<a id="l00028"></a>#endif
<a id="l00029"></a>
<a id="l00030"></a>#define SMP_SHELL_RX_BUF_SIZE   127
<a id="l00031"></a>
<a id="l00033"></a>struct smp_shell_data {
<a id="l00035"></a>        struct net_buf_pool *buf_pool;
<a id="l00037"></a>        struct k_fifo buf_ready;
<a id="l00039"></a>        struct net_buf *buf;
<a id="l00041"></a>        atomic_t esc_state;
<a id="l00043"></a>        const struct shell_uart_common *uart;
<a id="l00044"></a>};
<a id="l00045"></a>
<a id="l00058"></a>size_t smp_shell_rx_bytes(struct smp_shell_data *data, const uint8_t *bytes,
<a id="l00059"></a>                          size_t size);
<a id="l00060"></a>
<a id="l00068"></a>void smp_shell_process(struct smp_shell_data *data);
<a id="l00069"></a>
<a id="l00078"></a>int smp_shell_init(void);
<a id="l00079"></a>
<a id="l00080"></a>#ifdef __cplusplus
<a id="l00081"></a>}
<a id="l00082"></a>#endif
<a id="l00083"></a>
<a id="l00087"></a>
<a id="l00088"></a>#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_SHELL_H_ */
</code></pre>

## 9.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2019 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. ZEPHYR_INCLUDE_MGMT_MCUMGR_TRANSPORT_SMP_SHELL_H_头文件包含保护结束。

## 9.3\_原页符号提示（Symbol Descriptions）

### `device.h`

Zephyr设备模型（Device Model）的API和宏。

符号定位：[device.h](../device_reference/P007_设备模型头文件参考.md)。

### `atomic_t`

```c
long atomic_t
```

原子整型变量（Atomic Integer Variable）。

定义位置（Definition）：atomic_types.h:34。

符号定位：[atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)。

### `smp_shell_init`

```c
int smp_shell_init(void)
```

初始化通过Shell承载的SMP传输（SMP Transport）。

符号定位：[smp_shell_init](P007_mcumgr_Shell传输接口.md#ga1b71c4da07049b47269002ef6ec2b256)。

### `smp_shell_process`

```c
void smp_shell_process(struct smp_shell_data *data)
```

处理SMP数据；收到完整帧时执行命令。

符号定位：[smp_shell_process](P007_mcumgr_Shell传输接口.md#ga44b90f6ba276d8d7a89d6b90c8bb0341)。

### `smp_shell_rx_bytes`

```c
size_t smp_shell_rx_bytes(struct smp_shell_data *data, const uint8_t *bytes, size_t size)
```

尝试将收到的字节作为SMP帧（Frame）的一部分处理。

符号定位：[smp_shell_rx_bytes](P007_mcumgr_Shell传输接口.md#ga785293b670fcc10190e6c3d480a7d6d6)。

### `types.h`

符号定位：[types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)。

### `kernel.h`

公共内核 API（Public Kernel APIs）。

符号定位：[kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `k_fifo`

内核先进先出队列结构（Kernel FIFO Structure）。

定义位置（Definition）：kernel.h:2951。

符号定位：[k_fifo](../queue_reference/P004_内核FIFO结构.md)。

### `net_buf_pool`

网络缓冲区池表示（Network Buffer Pool Representation）。

定义位置（Definition）：net_buf.h:1198。

符号定位：[net_buf_pool](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html)。

### `net_buf`

网络缓冲区表示（Network Buffer Representation）。

定义位置（Definition）：net_buf.h:1062。

符号定位：[net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。

### `smp_shell_data`

SMP Shell使用的数据。

定义位置（Definition）：smp_shell.h:33。

符号定位：[smp_shell_data](P010_SMP_Shell运行数据.md)。

### `smp_shell_data::buf`

```c
struct net_buf * buf
```

当前活动接收缓冲区（Active Receive Buffer）。

定义位置（Definition）：smp_shell.h:39。

符号定位：[smp_shell_data::buf](P010_SMP_Shell运行数据.md#a281058a6cb23102af46cb0457c3a3232)。

### `smp_shell_data::buf_ready`

```c
struct k_fifo buf_ready
```

已准备好处理的帧的先进先出队列（FIFO）。

定义位置（Definition）：smp_shell.h:37。

符号定位：[smp_shell_data::buf_ready](P010_SMP_Shell运行数据.md#a3e15c83e64e1cab0f14141d2a6dd7bed)。

### `smp_shell_data::buf_pool`

```c
struct net_buf_pool * buf_pool
```

用于接收帧的网络缓冲区池（Network Buffer Pool）。

定义位置（Definition）：smp_shell.h:35。

符号定位：[smp_shell_data::buf_pool](P010_SMP_Shell运行数据.md#a67997e0400ee096e98781b839df3d6c2)。

### `smp_shell_data::esc_state`

```c
atomic_t esc_state
```

已经检测到通过控制台承载的SMP帧的哪些部分。

定义位置（Definition）：smp_shell.h:41。

符号定位：[smp_shell_data::esc_state](P010_SMP_Shell运行数据.md#aea6798b62094c9d3bcc3dc6926800af4)。

### `smp_shell_data::uart`

```c
const struct shell_uart_common * uart
```

负责接收的UART Shell对象。

定义位置（Definition）：smp_shell.h:43。

符号定位：[smp_shell_data::uart](P010_SMP_Shell运行数据.md#af2a9ec4af7279a114bee4c2cb11a31f3)。

## 9.4\_源码跟踪译注

> 译注——rx_bytes的返回值是本次消费的输入字节数，不是完成的帧数，也不是命令执行结果。它扫描到帧或缓冲区末尾为止；完整帧的后续处理由process完成。

> 译注——process应在线程上下文调用，并从就绪FIFO取出帧进行处理。活动接收缓冲和已排队帧分别由buf与buf_ready表示，不能把当前缓冲指针非NULL当作整帧已接收的证据。

> 译注——接收前先完成smp_shell_init。此初始化与普通Shell实例初始化、具体UART硬件配置属于不同阶段，接口返回0只描述本次初始化结果。

头文件定位：[include/zephyr/mgmt/mcumgr/transport/smp_shell.h](../../../include/zephyr/mgmt/mcumgr/transport/smp_shell.h)，关联实现／接口：[subsys/mgmt/mcumgr/transport/src/smp_shell.c](../../../subsys/mgmt/mcumgr/transport/src/smp_shell.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/mgmt/mcumgr/transport/smp_shell.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/mgmt/mcumgr/transport/src/smp_shell.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P008_SMP_Shell头文件参考.md)
- [zephyr/device.h](../device_reference/P007_设备模型头文件参考.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [smp_shell_data](P010_SMP_Shell运行数据.md)
- [net_buf_pool](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf__pool.html)
- [buf_pool](P010_SMP_Shell运行数据.md#a67997e0400ee096e98781b839df3d6c2)
- [k_fifo](../queue_reference/P004_内核FIFO结构.md)
- [buf_ready](P010_SMP_Shell运行数据.md#a3e15c83e64e1cab0f14141d2a6dd7bed)
- [net_buf](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)
- [buf](P010_SMP_Shell运行数据.md#a281058a6cb23102af46cb0457c3a3232)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [esc_state](P010_SMP_Shell运行数据.md#aea6798b62094c9d3bcc3dc6926800af4)
- [uart](P010_SMP_Shell运行数据.md#af2a9ec4af7279a114bee4c2cb11a31f3)
- [smp_shell_rx_bytes](P007_mcumgr_Shell传输接口.md#ga785293b670fcc10190e6c3d480a7d6d6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [smp_shell_process](P007_mcumgr_Shell传输接口.md#ga44b90f6ba276d8d7a89d6b90c8bb0341)
- [smp_shell_init](P007_mcumgr_Shell传输接口.md#ga1b71c4da07049b47269002ef6ec2b256)

---

[上一章](P008_SMP_Shell头文件参考.md) · [返回大纲](大纲.md) · [下一章](P010_SMP_Shell运行数据.md)
