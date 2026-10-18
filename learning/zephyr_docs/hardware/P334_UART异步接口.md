---
id: learning.zephyr-docs.hardware.uartasync-0
title: UART异步接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第334章\_UART异步接口

原文：[group__uart__async](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html)。读取日期：2026-10-13，`latest`。

## 334.1\_接口范围与事件对象

通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）的异步（Asynchronous）接口通过事件通知传输进展。接口自 Zephyr 1.14 提供，版本为 1.0.0，声明来自 `zephyr/drivers/uart.h`。

发送（Transmit，TX）事件数据由 [`uart_event_tx`](P335_UART发送事件结构.md) 保存；接收（Receive，RX）数据由 [`uart_event_rx`](P336_UART接收事件结构.md) 保存；接收缓冲区释放信息由 [`uart_event_rx_buf`](P337_UART缓冲区释放事件结构.md) 保存，接收停止信息由 [`uart_event_rx_stop`](P338_UART接收停止事件结构.md) 保存。[`uart_event`](P339_UART事件联合结构.md) 汇集当前事件的信息。

## 334.2\_先安装事件回调

<a id="ga00b7c98a4da3ea3675d0a40c5dacb136"></a>

回调（Callback）类型 [`uart_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ga00b7c98a4da3ea3675d0a40c5dacb136) 定义事件处理函数的签名：

```c
typedef void (*uart_callback_t)(const struct device *dev,
                                struct uart_event *evt, void *user_data);
int uart_callback_set(const struct device *dev, uart_callback_t callback,
                      void *user_data);
```

<a id="gad33e627ed8729409b14e92453e53459c"></a>

回调的 `dev` 是 UART 设备实例，`evt` 指向 [`uart_event`](P339_UART事件联合结构.md)，`user_data` 指向用户指定的数据。[`uart_callback_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gad33e627ed8729409b14e92453e53459c) 为 `static inline`，把 `callback` 设为事件处理函数，并将 `user_data` 传给它。

使用其他异步函数之前，必须先设置回调；这个设置函数也可用于检测设备是否支持异步应用程序编程接口（Application Programming Interface，API），其余异步 API 没有该检测功能。成功返回 0，`-ENOSYS` 表示设备不支持，`-ENOTSUP` 表示 API 未启用。

## 334.3\_接收缓冲区的事件流程

[`uart_event_type`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gaf0c9513cbafa36d86b4c83f2b6a03dcd) 枚举定义传给异步回调的事件。开始接收前，先用第一个缓冲区调用 [`uart_rx_enable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ga902e18c2a727ed2988e1b6caa6a444b8)。开始往当前缓冲区接收时，驱动发出 [`UART_RX_BUF_REQUEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)，请求下一个缓冲区。

收到请求后，可以调用 [`uart_rx_buf_rsp`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ga3970fe2818e214b0814ea8b73a816a6a) 提供第二个缓冲区：第一块填满后，驱动自动切换到第二块。也可以忽略请求，但当前缓冲区填满时将产生 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)，随后接收停止。要实现连续可靠接收，必须在当前缓冲区填满前提供下一块。

已经收到一些数据之后，如果接收超时，会产生 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)。同一块缓冲区可以多次产生此事件。超时从最后收到的字节开始计时；如果根本没有收到数据，就不会因空闲而产生超时事件。

驱动不再使用当前缓冲区时，产生 [`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)，紧随 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)。具体实现可能在缓冲区完全填满或只填了一部分时释放它。已经提供第二块时，它成为当前缓冲区，流程重新从下一缓冲区请求开始；没有第二块时，接收停止并产生 [`UART_RX_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)，此后可重新开始整个流程。

接收期间随时可能发生 [`UART_RX_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)。若已经收到数据，接着产生 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)；然后对当前交给驱动的每块缓冲区产生 [`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)，最后产生 [`UART_RX_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)。

主动调用 [`uart_rx_disable`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gafd4753bee51b230091a3c6ddb26ea734) 也会关闭接收：若有已收数据，先产生相应 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)，再逐块释放驱动持有的缓冲区，最后产生 [`UART_RX_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)。

## 334.4\_发送流程与完整事件枚举

发送从 [`uart_tx`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gaf99f32ce2e2d9beb32a2f2e5a26320dc) 开始。整块缓冲区发送完毕后产生 [`UART_TX_DONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)；发生超时时产生 [`UART_TX_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)。主动调用 [`uart_tx_abort`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gaa8a26d3ea685fb98030ea03613be6280) 也会产生 [`UART_TX_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)。

<a id="gaf0c9513cbafa36d86b4c83f2b6a03dcd"></a>

原枚举没有显式赋值，顺序如下：

| 枚举项 | 含义 |
| --- | --- |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4"></a>[`UART_TX_DONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4) | 整个发送缓冲区已发完 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1"></a>[`UART_TX_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1) | 因超时或 [`uart_tx_abort`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gaa8a26d3ea685fb98030ea03613be6280) 调用而中止发送 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7"></a>[`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) | 接收的数据已可处理 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe"></a>[`UART_RX_BUF_REQUEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) | 驱动请求下一块缓冲区，以保持连续接收 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48"></a>[`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48) | UART 驱动不再使用该缓冲区 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203"></a>[`UART_RX_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203) | 接收已禁用，可再次启用 |
| <a id="ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd"></a>[`UART_RX_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) | 由于外部事件而停止接收 |

启用流控制（Flow Control）后，发送可能无法在给定时间内完成；即使收到 [`UART_TX_ABORTED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)，也可能已经发送了部分数据，其数量在事件数据中。

[`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) 的触发情形包括：收到数据后的空闲超时、缓冲区填满、调用 `uart_rx_disable` 之后，以及外部事件 [`UART_RX_STOPPED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd) 导致停止之后。对于同一缓冲区，超时触发可以重复发生。

[`UART_RX_BUF_REQUEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) 在开始使用新缓冲区接收时发出，以便提前安排下一块并平滑切换。接收器停止、禁用或完成工作且允许重新启用时，都会发出 [`UART_RX_DISABLED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)；随后可再次调用 `uart_rx_enable`。`UART_RX_STOPPED` 的原因是 [`uart_rx_stop_reason`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gadeba6c5485e01dfc1c8a6e1c21668a88) 中的某一项。

## 334.5\_启用接收

<a id="ga902e18c2a727ed2988e1b6caa6a444b8"></a>

<a id="ga12d91846133351a85fa471fa90f2a0fd"></a>

字节和 16 位宽数据接收使用以下接口：

```c
int uart_rx_enable(const struct device *dev, uint8_t *buf,
                    size_t len, int32_t timeout);
int uart_rx_enable_u16(const struct device *dev, uint16_t *buf,
                        size_t len, int32_t timeout);
```

`dev` 为 UART 实例，`buf` 指向第一块接收缓冲区，`len` 为缓冲区长度。函数将该缓冲区设为当前接收目标后立即返回；随后，通过 [`uart_callback_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gad33e627ed8729409b14e92453e53459c) 设置的事件处理函数收到 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) 或 [`UART_RX_BUF_REQUEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) 等事件。

`timeout` 是至少收到一个字节后的不活动时长，单位为微秒；达到该时长会触发 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)。[`SYS_FOREVER_US`](../timeutil_reference/P007_时间单位辅助接口.md#gad8743aaa97d3b2650908020ffb76ef0e) 禁用超时。原 `_u16` 说明同样使用“至少一个字节”的措辞，缓冲区类型则为 `uint16_t *`。

两者成功返回 0，失败返回负错误码；`-ENOTSUP` 表示 API 未启用，`-EBUSY` 表示接收已经在进行。

## 334.6\_响应下一缓冲区请求

<a id="ga3970fe2818e214b0814ea8b73a816a6a"></a>

<a id="ga778bcfc30be853c8d320f295b34c17c0"></a>

响应 [`UART_RX_BUF_REQUEST`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe) 时，使用以下 `static inline` 函数提供下一块缓冲区：

```c
int uart_rx_buf_rsp(const struct device *dev, uint8_t *buf, size_t len);
int uart_rx_buf_rsp_u16(const struct device *dev, uint16_t *buf, size_t len);
```

`dev` 为设备实例，`buf` 指向接收缓冲区，`len` 为长度；宽数据版本接收 [`uint16_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e) 缓冲区。驱动将在当前缓冲区填满后使用它。

**注意：**把仍由驱动使用的缓冲区再次提供给驱动会导致未定义行为。只有驱动已经释放后，才能复用该缓冲区；“收到可处理数据”与“缓冲区已释放”是不同的事件。

两者成功返回 0，失败返回负错误码。`-ENOTSUP` 表示 API 未启用，`-EBUSY` 表示下一块缓冲区已经设置，`-EACCES` 表示接收器已经禁用，可能是调用过晚。

## 334.7\_禁用接收

<a id="gafd4753bee51b230091a3c6ddb26ea734"></a>

`uart_rx_disable` 禁用指定设备的接收：

```c
int uart_rx_disable(const struct device *dev);
```

对每块已经安排的缓冲区，驱动会产生 [`UART_RX_BUF_RELEASED`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)，然后产生 `UART_RX_DISABLED`。如果还有待报告的接收数据，对这些数据的 [`UART_RX_RDY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7) 会先于各个缓冲区释放事件发出。

成功返回 0，失败返回负错误码；`-ENOTSUP` 表示 API 未启用，`-EFAULT` 表示当前没有活动的接收。

## 334.8\_发送与中止发送

普通版本发送缓冲区中的指定数量字节，宽数据版本发送指定数量的数据项：

```c
int uart_tx(const struct device *dev, const uint8_t *buf,
             size_t len, int32_t timeout);
int uart_tx_u16(const struct device *dev, const uint16_t *buf,
                 size_t len, int32_t timeout);
int uart_tx_abort(const struct device *dev);
```

<a id="gaf99f32ce2e2d9beb32a2f2e5a26320dc"></a>

<a id="gab0ea611cd072fa459a6f1780ce62c9e3"></a>

`uart_tx` 和 [`uart_tx_u16`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gab0ea611cd072fa459a6f1780ce62c9e3) 的 `dev` 为设备实例，`buf` 指向发送缓冲区，`len` 为相应缓冲区长度。函数立即返回，传输结束后调用通过 [`uart_callback_set`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__async.html#gad33e627ed8729409b14e92453e53459c) 设置的事件处理函数。`timeout` 单位为微秒，仅启用流控制时有效；[`SYS_FOREVER_US`](../timeutil_reference/P007_时间单位辅助接口.md#gad8743aaa97d3b2650908020ffb76ef0e) 禁用超时。

两者成功返回 0，失败返回负错误码；`-ENOTSUP` 表示 API 未启用，`-EBUSY` 表示已有传输进行中。

<a id="gaa8a26d3ea685fb98030ea03613be6280"></a>

`uart_tx_abort` 中止当前发送，随后产生包含已发送数据量的 `UART_TX_ABORTED` 事件。成功返回 0，失败返回负错误码；`-ENOTSUP` 表示 API 未启用，`-EFAULT` 表示没有活动的发送。

---

[上一章：UART中断驱动接口](P333_UART中断驱动接口.md) · [下一章：UART发送事件结构](P335_UART发送事件结构.md) · [返回大纲](大纲.md)
