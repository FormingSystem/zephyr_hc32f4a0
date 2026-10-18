---
id: learning.zephyr-docs.hardware.uartapi-0
title: UART公共接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第330章\_UART公共接口

原文：[group__uart__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html)。读取日期：2026-10-13，`latest`。

## 330.1\_接口范围

本页定义通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）控制器接口，自 Zephyr 1.0 提供，接口版本为 2.0.0。主头文件为 `zephyr/drivers/uart.h`，[`uart_config`](https://docs.zephyrproject.org/latest/doxygen/html/structuart__config.html) 描述控制器配置。

相关分组包括[异步 UART 接口](P334_UART异步接口.md)、[中断驱动 UART 接口](P333_UART中断驱动接口.md)、[轮询 UART 接口](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__polling.html)及 [UART 模拟接口](P341_UART模拟接口.md)。异步（Asynchronous）接口用事件通知进展，中断驱动（Interrupt-Driven）接口在中断处理路径服务收发，轮询（Polling）接口直接查询或等待硬件状态。

## 330.2\_数据位、校验与停止位

<a id="gab9f7de744a68a311330576d7da02c44a"></a>

<a id="ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27"></a>

<a id="ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4"></a>

<a id="ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913"></a>

<a id="ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97"></a>

<a id="ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f"></a>

[`uart_config_data_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gab9f7de744a68a311330576d7da02c44a) 枚举选择每帧的数据位数（Data Bits），原枚举不显式赋值；名称中的数字表示数据位数，不能把数字直接当成枚举编码。

```c
enum uart_config_data_bits {
    UART_CFG_DATA_BITS_5,
    UART_CFG_DATA_BITS_6,
    UART_CFG_DATA_BITS_7,
    UART_CFG_DATA_BITS_8,
    UART_CFG_DATA_BITS_9
};
```

<a id="gab2ab6aacb6e3c43bb26d4274157e5711"></a>

这五个值依次表示 5、6、7、8、9 个数据位。奇偶校验（Parity）由 [`uart_config_parity`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gab2ab6aacb6e3c43bb26d4274157e5711) 选择：

| 枚举项，按原声明顺序 | 含义 |
| --- | --- |
| <a id="ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d"></a>[`UART_CFG_PARITY_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d) | 无校验（No Parity） |
| <a id="ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed"></a>[`UART_CFG_PARITY_ODD`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed) | 奇校验（Odd Parity） |
| <a id="ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba"></a>[`UART_CFG_PARITY_EVEN`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba) | 偶校验（Even Parity） |
| <a id="ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca"></a>[`UART_CFG_PARITY_MARK`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca) | 传号校验（Mark Parity） |
| <a id="ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c"></a>[`UART_CFG_PARITY_SPACE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c) | 空号校验（Space Parity） |

> 译注：传号、空号校验分别使用恒为 1、恒为 0 的校验位；与根据数据统计奇偶性的校验方式区分。

<a id="gafc1aecb863e2456d73b78a49fcbad72e"></a>

[`uart_config_stop_bits`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gafc1aecb863e2456d73b78a49fcbad72e) 枚举选择帧结束的停止位（Stop Bits）：

| 枚举项，按原声明顺序 | 含义 |
| --- | --- |
| <a id="ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af"></a>[`UART_CFG_STOP_BITS_0_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af) | 0.5 个停止位 |
| <a id="ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58"></a>[`UART_CFG_STOP_BITS_1`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58) | 1 个停止位 |
| <a id="ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad"></a>[`UART_CFG_STOP_BITS_1_5`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad) | 1.5 个停止位 |
| <a id="ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6"></a>[`UART_CFG_STOP_BITS_2`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6) | 2 个停止位 |

校验与停止位枚举均未在原声明中显式赋值。

## 330.3\_硬件流控制与线路控制

<a id="ga8e2f1b4a8d60d7a6c24835d1b26f99e8"></a>

硬件流控制（Hardware Flow Control）决定如何借助握手信号协调发送与接收，使用 [`uart_config_flow_control`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)。请求发送（Request To Send，RTS）与清除发送阻止/允许发送（Clear To Send，CTS）是一组握手信号；数据终端就绪（Data Terminal Ready，DTR）和数据设备就绪（Data Set Ready，DSR）是另一组。RS-485 为串行电气接口标准名称，下表沿用原枚举拼写 `RS485`。

| 枚举项，按原声明顺序 | 原文含义 |
| --- | --- |
| <a id="gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973"></a>[`UART_CFG_FLOW_CTRL_NONE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973) | 无流控制 |
| <a id="gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86"></a>[`UART_CFG_FLOW_CTRL_RTS_CTS`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86) | RTS/CTS 流控制 |
| <a id="gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f"></a>[`UART_CFG_FLOW_CTRL_DTR_DSR`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f) | DTR/DSR 流控制 |
| <a id="gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c"></a>[`UART_CFG_FLOW_CTRL_RS485`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c) | RS485 流控制 |

这些枚举项没有显式赋值。流控制设为 NONE 时，用户可用 [`uart_line_ctrl`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga02552532e171e789efc1b000917a9be0) 系列函数管理相关信号操作；其他情况下由硬件或驱动管理。

<a id="ga02552532e171e789efc1b000917a9be0"></a>

[`uart_line_ctrl`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga02552532e171e789efc1b000917a9be0) 定义可查询或设置的线路控制项。`BIT(n)` 是第 n 位的位掩码，波特率（Baud Rate）与控制线都通过该枚举选择：

<a id="gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b"></a>

<a id="gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97"></a>

<a id="gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c"></a>

| 枚举项 | 原赋值 | 含义 |
| --- | --- | --- |
| [`UART_LINE_CTRL_BAUD_RATE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b) | `BIT(0)` | 波特率 |
| <a id="gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d"></a>[`UART_LINE_CTRL_RTS`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d) | `BIT(1)` | 请求发送 RTS |
| <a id="gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23"></a>[`UART_LINE_CTRL_DTR`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23) | `BIT(2)` | 数据终端就绪 DTR |
| [`UART_LINE_CTRL_DCD`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97) | `BIT(3)` | 数据载波检测（Data Carrier Detect，DCD） |
| [`UART_LINE_CTRL_DSR`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c) | `BIT(4)` | 数据设备就绪 DSR |

## 330.4\_接收停止原因

<a id="gadeba6c5485e01dfc1c8a6e1c21668a88"></a>

[`uart_rx_stop_reason`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gadeba6c5485e01dfc1c8a6e1c21668a88) 枚举描述导致接收停止的事件或错误，值保留如下：

| 枚举项 | 原赋值 | 含义 |
| --- | --- | --- |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54"></a>[`UART_ERROR_OVERRUN`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54) | `(1 << 0)` | 溢出错误（Overrun Error） |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5"></a>[`UART_ERROR_PARITY`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5) | `(1 << 1)` | 奇偶校验错误（Parity Error） |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b"></a>[`UART_ERROR_FRAMING`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b) | `(1 << 2)` | 帧格式错误（Framing Error） |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571"></a>[`UART_BREAK`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571) | `(1 << 3)` | 断线中断（Break Interrupt） |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786"></a>[`UART_ERROR_COLLISION`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786) | `(1 << 4)` | 冲突错误（Collision Error） |
| <a id="ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60"></a>[`UART_ERROR_NOISE`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60) | `(1 << 5)` | 噪声错误（Noise Error） |

接收到 Break 时，串行输入保持逻辑 0 的时间超过起始时间、数据位、校验位和停止位所需时间之和。

发送数据与接收数据不一致时，会产生冲突错误。这通常适用于发送（Transmit，TX）与接收（Receive，RX）线连接在一起的情形，例如 RS-485 半双工（Half Duplex）。只有支持冲突检测的 UART 才能使用此错误指示。

## 330.5\_读取与设置配置

配置函数均接收 UART 设备实例 `dev`。配置结构 `cfg` 描述波特率、数据格式及流控制。

```c
int uart_config_get(const struct device *dev, struct uart_config *cfg);
int uart_configure(const struct device *dev, const struct uart_config *cfg);
```

<a id="ga81dfc5f2134de8e4acb5f063512cf703"></a>

[`uart_config_get`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga81dfc5f2134de8e4acb5f063512cf703) 把当前配置存入 `*cfg`，可用于设备根据设备树源文件（Devicetree Source，DTS）数据初始化之后读取初始配置。成功返回 0，失败返回负错误码；`-ENOSYS` 表示驱动不支持获取当前配置，`-ENOTSUP` 表示该应用程序编程接口（Application Programming Interface，API）未启用。

<a id="gaa0b75777b879af10543f7e8f463ff9a2"></a>

[`uart_configure`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gaa0b75777b879af10543f7e8f463ff9a2) 使用 `*cfg` 设置 UART。成功返回 0，失败返回负错误码；`-ENOSYS` 表示设备不支持此配置，或者驱动不支持运行时配置；`-ENOTSUP` 表示 API 未启用。

## 330.6\_驱动命令与错误检查

<a id="gaa8683398e5d709b513509d08841ed51b"></a>

驱动专用命令通过 [`uart_drv_cmd`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gaa8683398e5d709b513509d08841ed51b) 发送，具体实现及支持的命令由驱动决定，应查阅相应驱动说明。

```c
int uart_drv_cmd(const struct device *dev, uint32_t cmd, uint32_t p);
int uart_err_check(const struct device *dev);
```

`uart_drv_cmd` 的 `dev` 为 UART 实例，[`cmd`](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615) 为命令，`p` 为该命令参数。成功返回 0，失败返回负错误码；`-ENOSYS` 表示函数未实现，`-ENOTSUP` 表示 API 未启用。

<a id="ga22ea20fd8e07153b3b71cc9416f5462f"></a>

[`uart_err_check`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga22ea20fd8e07153b3b71cc9416f5462f) 检查是否检测到错误。未检测到错误时返回 0；检测到错误时返回 [`uart_rx_stop_reason`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#gadeba6c5485e01dfc1c8a6e1c21668a88) 定义的错误标志；`-ENOSYS` 表示操作未实现。错误标志返回值与负的“不支持”错误码须分别处理。

## 330.7\_查询与设置线路控制

<a id="gab039414b41145dc8d31349836da91263"></a>

<a id="gafda8a550284a54c8e1d6b6638de978e5"></a>

线路控制函数通过 `ctrl` 选择 [`uart_line_ctrl`](https://docs.zephyrproject.org/latest/doxygen/html/group__uart__interface.html#ga02552532e171e789efc1b000917a9be0) 中的控制项：

```c
int uart_line_ctrl_get(const struct device *dev, uint32_t ctrl, uint32_t *val);
int uart_line_ctrl_set(const struct device *dev, uint32_t ctrl, uint32_t val);
```

两者的 `dev` 都是 UART 设备实例。读取函数的 `val` 指向保存控制值的变量；设置函数的 `val` 是准备写入的控制值。两者成功返回 0、失败返回负错误码；`-ENOSYS` 表示函数未实现，`-ENOTSUP` 表示 API 未启用。

---

[上一章：SPI设备树宏](P329_SPI设备树宏.md) · [下一章：UART配置结构](P331_UART配置结构.md) · [返回大纲](大纲.md)
