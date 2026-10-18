---
id: learning.zephyr-docs.hardware.spiback-0
title: SPI驱动后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第324章\_SPI驱动后端接口

原文：[group__spi__interface__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html)。读取日期：2026-10-13，`latest`。

## 324.1\_驱动实现侧的类型

本组提供实现串行外设接口（Serial Peripheral Interface，SPI）驱动所需的应用程序编程接口（Application Programming Interface，API）类型、回调（Callback）签名及辅助定义，声明来自 `zephyr/drivers/spi.h`。[`spi_driver_api`](https://docs.zephyrproject.org/latest/doxygen/html/structspi__driver__api.html) 将这些操作组织为驱动函数表。

## 324.2\_输入输出与异步完成

<a id="ga3fc669f866b03cfdad98754de69cda13"></a>

[`spi_api_io`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#ga3fc669f866b03cfdad98754de69cda13) 是输入输出（Input/Output，I/O）操作回调类型；参数与 `spi_transceive` 相同：

```c
typedef int (*spi_api_io)(const struct device *dev,
                          const struct spi_config *config,
                          const struct spi_buf_set *tx_bufs,
                          const struct spi_buf_set *rx_bufs);
```

`dev` 为驱动设备，`config` 为有效通信配置，`tx_bufs`、`rx_bufs` 分别为发送及接收缓冲区集合，无对应方向数据时可为 `NULL`。配置可能通过指针比较与前次操作区分。

<a id="ga03be7f33032ac479153616bbe26848e7"></a>

[`spi_api_io_async`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#ga03be7f33032ac479153616bbe26848e7) 为异步 I/O 回调类型，增加完成回调及用户数据：

```c
typedef int (*spi_api_io_async)(const struct device *dev,
                                const struct spi_config *config,
                                const struct spi_buf_set *tx_bufs,
                                const struct spi_buf_set *rx_bufs,
                                spi_callback_t cb, void *userdata);
```

原文把参数说明指向 `spi_transceive_signal`。译注：该引用提供信号版本的说明，而此处签名实际使用 `cb`、`userdata`；回调版本还可参照 `spi_transceive_cb`。保留原引用和实际签名，不能把 `cb` 当作轮询信号对象。

<a id="ga1db2a410f482d0f26c49f96352aa606d"></a>

完成回调 [`spi_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#ga1db2a410f482d0f26c49f96352aa606d) 用于异步传输请求：

```c
typedef void (*spi_callback_t)(const struct device *dev,
                               int result, void *data);
```

`dev` 是发出传输完成或错误通知的 SPI 设备；`result` 是结果码，0 表示成功，失败为 `-errno`；`data` 是请求者提供并传给回调的数据。

## 324.3\_RTIO提交与解锁

<a id="gae274c0d704e8fd8993631fc1b91bfcb1"></a>

实时输入输出（Real-Time Input/Output，RTIO）通过提交队列条目（Submission Queue Entry，SQE）安排工作。[`spi_api_iodev_submit`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#gae274c0d704e8fd8993631fc1b91bfcb1) 是向 SPI 设备提交 RTIO 工作的回调类型：

```c
typedef void (*spi_api_iodev_submit)(const struct device *dev,
                                     struct rtio_iodev_sqe *iodev_sqe);
```

原页对此类型未进一步列出参数和返回值说明。

<a id="gac651ff7cd3dde7abe2525e20ef2e9e7d"></a>

[`spi_api_release`](https://docs.zephyrproject.org/latest/doxygen/html/group__spi__interface__backend.html#gac651ff7cd3dde7abe2525e20ef2e9e7d) 是解锁 SPI 设备的回调类型；参数说明见 `spi_release`：

```c
typedef int (*spi_api_release)(const struct device *dev,
                               const struct spi_config *config);
```

它接收设备与有效配置指针，用于释放该配置保留的设备锁和/或片选（Chip Select，CS）。

---

[上一章：SPI缓冲区集合结构](P323_SPI缓冲区集合结构.md) · [下一章：SPI驱动函数表](P325_SPI驱动函数表.md) · [返回大纲](大纲.md)
