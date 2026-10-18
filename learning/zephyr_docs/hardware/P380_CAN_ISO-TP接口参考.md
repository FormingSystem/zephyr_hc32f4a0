---
id: learning.zephyr-docs.hardware.isotpsvc-2
title: CAN_ISO-TP接口参考
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第380章\_CAN_ISO-TP接口参考

原文：[group__can__isotp](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html)。读取日期：2026-10-13，`latest`。

## 380.1\_接口与数据类型

本页说明控制器局域网（Controller Area Network，CAN）的 ISO-TP 传输协议（Transport Protocol）应用程序编程接口（Application Programming Interface，API）。接口自 Zephyr 2.2 提供，版本为 1.0.0。包含头文件 `zephyr/canbus/isotp.h`。

- `struct isotp_msg_id`：ISO-TP 消息标识结构。
- `struct isotp_fc_opts`：ISO-TP 帧流控选项结构。

以下使用单帧（Single Frame，SF）、首帧（First Frame，FF）、连续帧（Consecutive Frame，CF）和流控帧（Flow Control Frame，FC）术语。块大小（Block Size，BS）控制连续发送多少帧后等待下一流控帧，详见[协议概述](P379_CAN_ISO-TP协议.md)。发送与接收分别记作 TX（Transmit）和 RX（Receive）。

## 380.2\_结果与错误码

协议数据单元（Protocol Data Unit，PDU）携带的流状态（Flow Status）可能为等待 `WAIT` 或溢出 `OVFLW`。下表保留官方所有返回码；`Ar`、`As`、`Cr` 为协议计时参数名称。

| 宏 | 值 | 含义 |
| --- | --- | --- |
| [`ISOTP_N_OK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab7daaebbc303665beb2946ce077d5312) | `0` | 成功完成。 |
| [`ISOTP_N_TIMEOUT_A`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga8298423e96932f94308f3064755d18fb) | `-1` | Ar/As 超时。 |
| [`ISOTP_N_TIMEOUT_BS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9e525bb24928a2656e7cd2842b306553) | `-2` | 等待接收下一流控帧超时。 |
| [`ISOTP_N_TIMEOUT_CR`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga77b802df46c66ed6002f143b57f73b7a) | `-3` | Cr 超时。 |
| [`ISOTP_N_WRONG_SN`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9caa5677a171e1bd0be06ebb6b006046) | `-4` | 序列号（Sequence Number，SN）不符合预期。 |
| [`ISOTP_N_INVALID_FS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga99312831df8e1822f02b41e3fccc0661) | `-5` | 收到无效流状态。 |
| [`ISOTP_N_UNEXP_PDU`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga45e3bfdd3948be6ccb3daec5db412b78) | `-6` | 收到非预期协议数据单元。 |
| [`ISOTP_N_WFT_OVRN`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gad6bcb7b6fb8ab30da1a4ddeabe3e3178) | `-7` | `WAIT` 流状态协议数据单元的数量超过允许的最大值。 |
| [`ISOTP_N_BUFFER_OVERFLW`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga1b8e6b35a637b5f98e7a2ab4270efd41) | `-8` | 收到 `OVFLW` 流状态协议数据单元。 |
| [`ISOTP_N_ERROR`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga0805646e65d39a9e2f15e110720887ca) | `-9` | 通用错误。 |
| [`ISOTP_NO_FREE_FILTER`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaf0624cd5e7d12e94f4a739bc47ee0361) | `-10` | 实现特有错误：CAN 设备没有可用过滤器，无法绑定或发送。 |
| [`ISOTP_NO_NET_BUF_LEFT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga901f61175e228a70c2f882bc999caea6) | `-11` | 没有可分配的网络缓冲区。 |
| [`ISOTP_NO_BUF_DATA_LEFT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaed5270f0ee489128adb8c2ea481c6c77) | `-12` | 缓冲区剩余空间不足以容纳数据。 |
| [`ISOTP_NO_CTX_LEFT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac5cb1fafeb8aa5cf9fe1695612671c7d) | `-13` | 没有可分配的上下文缓冲区。 |
| [`ISOTP_RECV_TIMEOUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaa3e873d4a80ee128f1858520874f93b6) | `-14` | 接收等待超时。 |

## 380.3\_固定寻址宏

固定寻址（Fixed Addressing）使用源地址（Source Address，SA）、目标地址（Target Address，TA）及优先级（Priority）。下表宏直接使用同名 Kconfig 配置项的值；`POS` 表示位位置，`MASK` 表示掩码（Mask）。

| 宏 | 展开值 | 含义 |
| --- | --- | --- |
| [`ISOTP_FIXED_ADDR_SA_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaedb0e7330d19b1cdc380c0b36cabf2f5) | `(CONFIG_ISOTP_FIXED_ADDR_SA_POS)` | 固定源地址的位置。 |
| [`ISOTP_FIXED_ADDR_SA_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2a9cbfd95bae05a9f7433f3b1c58689e) | `(CONFIG_ISOTP_FIXED_ADDR_SA_MASK)` | 提取固定源地址的掩码。 |
| [`ISOTP_FIXED_ADDR_TA_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga2b64d4dffde99159ae5120586364e1c6) | `(CONFIG_ISOTP_FIXED_ADDR_TA_POS)` | 固定目标地址的位置。 |
| [`ISOTP_FIXED_ADDR_TA_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga5d5415982e04e506c9b045bfbe2be337) | `(CONFIG_ISOTP_FIXED_ADDR_TA_MASK)` | 提取固定目标地址的掩码。 |
| [`ISOTP_FIXED_ADDR_PRIO_POS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga29f8806889f4e41c1529c35a56ee98a9) | `(CONFIG_ISOTP_FIXED_ADDR_PRIO_POS)` | 固定寻址模式中优先级的位置。 |
| [`ISOTP_FIXED_ADDR_PRIO_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab5dc33148923e7cd58b438a8906d1ace) | `(CONFIG_ISOTP_FIXED_ADDR_PRIO_MASK)` | 固定寻址模式中优先级的掩码。 |
| [`ISOTP_FIXED_ADDR_RX_MASK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gac27b3210cb754b4621c54923696bfe2d) | `(CONFIG_ISOTP_FIXED_ADDR_RX_MASK)` | CAN 接收过滤掩码，用于匹配任意优先级和源地址。 |

## 380.4\_消息标识标志

CAN FD 表示灵活数据速率 CAN（CAN with Flexible Data-rate），位速率切换（Bit Rate Switch，BRS）仅适用于 CAN FD 格式。`BIT(n)` 表示设置第 n 位的位掩码。

| 宏 | 值 | 含义与限制 |
| --- | --- | --- |
| [`ISOTP_MSG_EXT_ADDR`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga903d326b3bfb05151b9d5d0a0ace59b9) | `BIT(0)` | 使用 ISO-TP 扩展寻址（Extended Addressing），地址位于 CAN 帧有效载荷的第一个字节。 |
| [`ISOTP_MSG_FIXED_ADDR`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga998ae9b1645485f567e692bfbaa50cbe) | `BIT(1)` | 按 SAE J1939 使用 ISO-TP 固定寻址；只能与 [`ISOTP_MSG_IDE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga16935466c1a543c03d11b71b8944d0b8) 一起使用。 |
| [`ISOTP_MSG_IDE`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga16935466c1a543c03d11b71b8944d0b8) | `BIT(2)` | 使用扩展的 29 位 CAN 标识符（Identifier，ID）。 |
| [`ISOTP_MSG_FDF`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga70b485a2e576b1b0fec2cc8037215bd9) | `BIT(3)` | 使用 CAN FD 帧格式（FD Format，FDF）。 |
| [`ISOTP_MSG_BRS`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga9275708b5afba61c8b5c98c718ec4635) | `BIT(4)` | 使用 CAN FD 位速率切换；只能与 [`ISOTP_MSG_FDF`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga70b485a2e576b1b0fec2cc8037215bd9) 一起使用。 |

> 译注：原页面将 BRS 写为 Baud Rate Switch，本译文同时沿用 CAN 文档中的 Bit Rate Switch 术语。ISO-TP 扩展寻址与 29 位 CAN 扩展标识符对应不同的标志。

## 380.5\_发送完成回调

```c
typedef void (*isotp_tx_callback_t)(int error_nr, void *arg);
```

发送完成时调用此回调（Callback）。`error_nr` 成功时为 [`ISOTP_N_OK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab7daaebbc303665beb2946ce077d5312)，出错时为 `ISOTP_N_*`；`arg` 是调用发送函数时传入的回调参数。

## 380.6\_绑定与解除绑定

```c
int isotp_bind(struct isotp_recv_ctx *rctx,
               const struct device *can_dev,
               const struct isotp_msg_id *rx_addr,
               const struct isotp_msg_id *tx_addr,
               const struct isotp_fc_opts *opts,
               k_timeout_t timeout);
void isotp_unbind(struct isotp_recv_ctx *rctx);
```

[`isotp_bind()`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga725696a26c3bdc0c99e3c4e611a897f9) 将一组接收/发送地址绑定到接收上下文（Context）。来自指定地址的数据会被缓冲，之后可调用 [`isotp_recv()`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga79c9cad7f39802c5c80af743717e22c6) 读取。绑定时，在 CAN 设备上安装过滤器并初始化上下文。上下文必须一直有效，直到调用解除绑定操作。

| 参数 | 含义 |
| --- | --- |
| `rctx` | 保存内部状态的接收上下文。 |
| `can_dev` | 用于发送和接收的 CAN 设备。 |
| `rx_addr` | 输入数据的标识。 |
| `tx_addr` | 发送流控帧所用的标识。 |
| `opts` | 流量控制选项。 |
| `timeout` | 分配首帧/单帧缓冲区的超时。 |

绑定成功返回 [`ISOTP_N_OK`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gab7daaebbc303665beb2946ce077d5312)；CAN 设备没有剩余过滤器时返回 [`ISOTP_NO_FREE_FILTER`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaf0624cd5e7d12e94f4a739bc47ee0361)。

[`isotp_unbind()`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#ga622293da5564203bf6dcb993410d21ba) 删除 `isotp_bind()` 建立的绑定，从 CAN 设备移除过滤器；如果传输正在进行，还会释放缓冲区。`rctx` 指向要解除绑定的上下文，调用后即可安全丢弃该上下文。

## 380.7\_复制接收数据

```c
int isotp_recv(struct isotp_recv_ctx *rctx, uint8_t *data,
               size_t len, k_timeout_t timeout);
```

从已绑定上下文 `rctx` 的先进先出接收队列（First In, First Out，FIFO）读取数据。队列为空时阻塞。发生错误时返回负数，并保持 `data` 缓冲区不变。

`data` 指向接收复制数据的目标缓冲区，`len` 是该缓冲区大小，`timeout` 是等待输入数据的超时。成功返回复制的字节数；等待超时返回 [`ISOTP_RECV_TIMEOUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaa3e873d4a80ee128f1858520874f93b6)；其他错误返回 `ISOTP_N_*`。

## 380.8\_取得网络缓冲区

```c
int isotp_recv_net(struct isotp_recv_ctx *rctx,
                   struct net_buf **buffer, k_timeout_t timeout);
```

把输入数据读入网络缓冲区（Network Buffer）。调用会阻塞，直到完整数据包已接收、达到块大小 BS，或发生错误。

BS 为 0 时，数据位于单个 [`net_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html) 中；否则，数据按 BS 大小分块。返回的网络缓冲区持有引用，处理完数据后必须调用 `net_buf_unref()` 释放引用。

> 译注：BS 的单位是连续帧数量，不是字节数；“按 BS 大小分块”沿用原接口说明，不能把 BS 当成字节缓冲区长度。

`rctx` 是已绑定的上下文，`buffer` 指向写出 [`net_buf`](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html) 指针的位置，`timeout` 为等待输入数据的超时。

BS 大于 0 时，返回本次传输的剩余数据长度；BS 为 0 时返回 0。等待超时返回 [`ISOTP_RECV_TIMEOUT`](https://docs.zephyrproject.org/latest/doxygen/html/group__can__isotp.html#gaa3e873d4a80ee128f1858520874f93b6)；出错返回 `ISOTP_N_*`。

## 380.9\_发送数据

```c
int isotp_send(struct isotp_send_ctx *sctx,
               const struct device *can_dev,
               const uint8_t *data, size_t len,
               const struct isotp_msg_id *tx_addr,
               const struct isotp_msg_id *rx_addr,
               isotp_tx_callback_t complete_cb, void *cb_arg);
```

向监听 `tx_addr` 的对端发送数据。内部使用工作队列（Workqueue）传输分段数据。数据和上下文必须保持有效，直到发送完成。

提供 `complete_cb` 时，此函数为非阻塞（Non-blocking）调用；发送完成后调用回调，并通过回调参数报告返回值。

| 参数 | 含义 |
| --- | --- |
| `sctx` | 保存内部状态的发送上下文。 |
| `can_dev` | 用于发送和接收的 CAN 设备。 |
| `data` | 待发送数据。 |
| `len` | 待发送数据长度。 |
| `tx_addr` | 输出帧的标识，接收端监听此标识。 |
| `rx_addr` | 接收流控帧所用的标识。 |
| `complete_cb` | 完成时调用的函数，或 `NULL`。 |
| `cb_arg` | 传给完成回调的参数。 |

成功返回 `ISOTP_N_OK`；错误返回 `ISOTP_N_*`。

---

[上一章：CAN_ISO-TP协议](P379_CAN_ISO-TP协议.md) · [下一章：ISO-TP消息标识](P381_ISO-TP消息标识.md) · [返回大纲](大纲.md)
