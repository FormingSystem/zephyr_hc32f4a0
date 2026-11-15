---
id: learning.zephyr-docs.uart-driver-reference.page-1
title: UART驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2uart_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_UART驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2uart_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入UART公共与内部头文件参考和源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

UART（通用异步收发器，Universal Asynchronous Receiver/Transmitter）驱动API的主头文件。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart/uart_internal.h>
#include <zephyr/syscalls/uart.h>
```

查看此文件的源码。

UART（通用异步收发器，Universal Asynchronous Receiver/Transmitter）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_uart_5Fconfig"></a>

```c
struct uart_config
```

相关声明：[uart_config](../hardware/P331_UART配置结构.md)。

UART控制器（Controller）配置结构。

<a id="r_uart_5Fevent_5Ftx"></a>

```c
struct uart_event_tx
```

相关声明：[uart_event_tx](../hardware/P335_UART发送事件结构.md)。

UART发送（Transmit，TX）事件数据。

<a id="r_uart_5Fevent_5Frx"></a>

```c
struct uart_event_rx
```

相关声明：[uart_event_rx](../hardware/P336_UART接收事件结构.md)。

UART接收（Receive，RX）事件数据。

<a id="r_uart_5Fevent_5Frx_5Fbuf"></a>

```c
struct uart_event_rx_buf
```

相关声明：[uart_event_rx_buf](../hardware/P337_UART缓冲区释放事件结构.md)。

UART接收缓冲区释放（RX Buffer Released）事件数据。

<a id="r_uart_5Fevent_5Frx_5Fstop"></a>

```c
struct uart_event_rx_stop
```

相关声明：[uart_event_rx_stop](../hardware/P338_UART接收停止事件结构.md)。

UART接收停止（RX Stopped）数据。

<a id="r_uart_5Fevent"></a>

```c
struct uart_event
```

相关声明：[uart_event](../hardware/P339_UART事件联合结构.md)。

包含当前事件（Event）信息的结构。

<a id="r_uart_5Fevent_3A_3Auart_5Fevent_5Fdata"></a>

```c
union uart_event::uart_event_data
```

相关声明：[uart_event::uart_event_data](../hardware/P340_UART事件数据联合体.md)。

事件数据（Event Data）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_gad7a26b1a1d6212d7d39c05c8ad4ec926"></a>

```c
typedef void(* uart_irq_callback_user_data_t) (const struct device *dev, void *user_data)
```

相关声明：[uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)、[device](../device_reference/P002_设备对象结构.md)。

定义供uart_irq_callback_user_data_set()使用的应用程序回调函数签名（Callback Function Signature）。

<a id="r_ga00b7c98a4da3ea3675d0a40c5dacb136"></a>

```c
typedef void(* uart_callback_t) (const struct device *dev, struct uart_event *evt, void *user_data)
```

相关声明：[uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)、[device](../device_reference/P002_设备对象结构.md)、[uart_event](../hardware/P339_UART事件联合结构.md)。

定义供uart_callback_set()使用的应用程序回调函数签名。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.3\_枚举（Enumerations）

<a id="r_ga02552532e171e789efc1b000917a9be0"></a>

```c
enum uart_line_ctrl { UART_LINE_CTRL_BAUD_RATE = BIT(0) , UART_LINE_CTRL_RTS = BIT(1) , UART_LINE_CTRL_DTR = BIT(2) , UART_LINE_CTRL_DCD = BIT(3) , UART_LINE_CTRL_DSR = BIT(4) }
```

相关声明：[uart_line_ctrl](../hardware/P330_UART公共接口.md#ga02552532e171e789efc1b000917a9be0)、[UART_LINE_CTRL_BAUD_RATE](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)、[UART_LINE_CTRL_RTS](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)、[UART_LINE_CTRL_DTR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)、[UART_LINE_CTRL_DCD](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)、[UART_LINE_CTRL_DSR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)。

线路控制信号（Line Control Signals）。

<a id="r_gadeba6c5485e01dfc1c8a6e1c21668a88"></a>

```c
enum uart_rx_stop_reason { UART_ERROR_OVERRUN = (1 << 0) , UART_ERROR_PARITY = (1 << 1) , UART_ERROR_FRAMING = (1 << 2) , UART_BREAK = (1 << 3) , UART_ERROR_COLLISION = (1 << 4) , UART_ERROR_NOISE = (1 << 5) }
```

相关声明：[uart_rx_stop_reason](../hardware/P330_UART公共接口.md#gadeba6c5485e01dfc1c8a6e1c21668a88)、[UART_ERROR_OVERRUN](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)、[UART_ERROR_PARITY](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)、[UART_ERROR_FRAMING](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)、[UART_BREAK](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)、[UART_ERROR_COLLISION](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)、[UART_ERROR_NOISE](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)。

接收停止原因（Reception Stop Reasons）。

<a id="r_gab2ab6aacb6e3c43bb26d4274157e5711"></a>

```c
enum uart_config_parity { UART_CFG_PARITY_NONE , UART_CFG_PARITY_ODD , UART_CFG_PARITY_EVEN , UART_CFG_PARITY_MARK , UART_CFG_PARITY_SPACE }
```

相关声明：[uart_config_parity](../hardware/P330_UART公共接口.md#gab2ab6aacb6e3c43bb26d4274157e5711)、[UART_CFG_PARITY_NONE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)、[UART_CFG_PARITY_ODD](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)、[UART_CFG_PARITY_EVEN](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)、[UART_CFG_PARITY_MARK](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)、[UART_CFG_PARITY_SPACE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)。

奇偶校验模式（Parity Modes）。

<a id="r_gafc1aecb863e2456d73b78a49fcbad72e"></a>

```c
enum uart_config_stop_bits { UART_CFG_STOP_BITS_0_5 , UART_CFG_STOP_BITS_1 , UART_CFG_STOP_BITS_1_5 , UART_CFG_STOP_BITS_2 }
```

相关声明：[uart_config_stop_bits](../hardware/P330_UART公共接口.md#gafc1aecb863e2456d73b78a49fcbad72e)、[UART_CFG_STOP_BITS_0_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)、[UART_CFG_STOP_BITS_1](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)、[UART_CFG_STOP_BITS_1_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)、[UART_CFG_STOP_BITS_2](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)。

停止位数量（Number of Stop Bits）。

<a id="r_gab9f7de744a68a311330576d7da02c44a"></a>

```c
enum uart_config_data_bits { UART_CFG_DATA_BITS_5 , UART_CFG_DATA_BITS_6 , UART_CFG_DATA_BITS_7 , UART_CFG_DATA_BITS_8 , UART_CFG_DATA_BITS_9 }
```

相关声明：[uart_config_data_bits](../hardware/P330_UART公共接口.md#gab9f7de744a68a311330576d7da02c44a)、[UART_CFG_DATA_BITS_5](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)、[UART_CFG_DATA_BITS_6](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)、[UART_CFG_DATA_BITS_7](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)、[UART_CFG_DATA_BITS_8](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)、[UART_CFG_DATA_BITS_9](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)。

数据位数量（Number of Data Bits）。

<a id="r_ga8e2f1b4a8d60d7a6c24835d1b26f99e8"></a>

```c
enum uart_config_flow_control { UART_CFG_FLOW_CTRL_NONE , UART_CFG_FLOW_CTRL_RTS_CTS , UART_CFG_FLOW_CTRL_DTR_DSR , UART_CFG_FLOW_CTRL_RS485 }
```

相关声明：[uart_config_flow_control](../hardware/P330_UART公共接口.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)、[UART_CFG_FLOW_CTRL_NONE](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)、[UART_CFG_FLOW_CTRL_RTS_CTS](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)、[UART_CFG_FLOW_CTRL_DTR_DSR](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)、[UART_CFG_FLOW_CTRL_RS485](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)。

硬件流控制（Hardware Flow Control）选项。

<a id="r_gaf0c9513cbafa36d86b4c83f2b6a03dcd"></a>

```c
enum uart_event_type { UART_TX_DONE , UART_TX_ABORTED , UART_RX_RDY , UART_RX_BUF_REQUEST , UART_RX_BUF_RELEASED , UART_RX_DISABLED , UART_RX_STOPPED }
```

相关声明：[uart_event_type](../hardware/P334_UART异步接口.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)、[UART_TX_DONE](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)、[UART_TX_ABORTED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)、[UART_RX_RDY](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)、[UART_RX_BUF_REQUEST](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)、[UART_RX_BUF_RELEASED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)、[UART_RX_DISABLED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)、[UART_RX_STOPPED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)。

UART_ASYNC_API中传给回调函数的事件类型（Event Types）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga22ea20fd8e07153b3b71cc9416f5462f"></a>

```c
int uart_err_check (const struct device *dev)
```

相关声明：[uart_err_check](../hardware/P330_UART公共接口.md#ga22ea20fd8e07153b3b71cc9416f5462f)、[device](../device_reference/P002_设备对象结构.md)。

检查是否检测到错误。

<a id="r_gae81ac8cc976a20d774cfbda09e9c983d"></a>

```c
int uart_poll_in (const struct device *dev, unsigned char *p_char)
```

相关声明：[uart_poll_in](../hardware/P332_UART轮询接口.md#gae81ac8cc976a20d774cfbda09e9c983d)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

从设备读取一个字符作为输入。

<a id="r_gaad39c1358019bfdcb919da7982743553"></a>

```c
int uart_poll_in_u16 (const struct device *dev, uint16_t *p_u16)
```

相关声明：[uart_poll_in_u16](../hardware/P332_UART轮询接口.md#gaad39c1358019bfdcb919da7982743553)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

从设备读取一个16位数据项作为输入。

<a id="r_ga06ba27ba772a7a18462b8cdbc7f9353c"></a>

```c
void uart_poll_out (const struct device *dev, unsigned char out_char)
```

相关声明：[uart_poll_out](../hardware/P332_UART轮询接口.md#ga06ba27ba772a7a18462b8cdbc7f9353c)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

向设备写入一个字符作为输出。

<a id="r_ga8faa3f58b9098c97e288e9c5f3367fd9"></a>

```c
void uart_poll_out_u16 (const struct device *dev, uint16_t out_u16)
```

相关声明：[uart_poll_out_u16](../hardware/P332_UART轮询接口.md#ga8faa3f58b9098c97e288e9c5f3367fd9)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

向设备写入一个16位数据项作为输出。

<a id="r_gaa0b75777b879af10543f7e8f463ff9a2"></a>

```c
int uart_configure (const struct device *dev, const struct uart_config *cfg)
```

相关声明：[uart_configure](../hardware/P330_UART公共接口.md#gaa0b75777b879af10543f7e8f463ff9a2)、[device](../device_reference/P002_设备对象结构.md)、[uart_config](../hardware/P331_UART配置结构.md)。

设置UART配置。

<a id="r_ga81dfc5f2134de8e4acb5f063512cf703"></a>

```c
int uart_config_get (const struct device *dev, struct uart_config *cfg)
```

相关声明：[uart_config_get](../hardware/P330_UART公共接口.md#ga81dfc5f2134de8e4acb5f063512cf703)、[device](../device_reference/P002_设备对象结构.md)、[uart_config](../hardware/P331_UART配置结构.md)。

取得UART配置。

<a id="r_gafe42e4719eada7e25904bc9ebfe87791"></a>

```c
static int uart_fifo_fill (const struct device *dev, const uint8_t *tx_data, int size)
```

相关声明：[uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向先进先出队列（First In, First Out，FIFO）填充数据。

<a id="r_gaa89f58818d8428ad6a11abf692c54c0d"></a>

```c
static int uart_fifo_fill_u16 (const struct device *dev, const uint16_t *tx_data, int size)
```

相关声明：[uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

向FIFO填充宽数据（Wide Data）。

<a id="r_gab10942076ac47ecff29e924098049398"></a>

```c
static int uart_fifo_read (const struct device *dev, uint8_t *rx_data, const int size)
```

相关声明：[uart_fifo_read](../hardware/P333_UART中断驱动接口.md#gab10942076ac47ecff29e924098049398)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从FIFO读取数据。

<a id="r_ga4a3c25dad2290f1f40e4b847e3b83f64"></a>

```c
static int uart_fifo_read_u16 (const struct device *dev, uint16_t *rx_data, const int size)
```

相关声明：[uart_fifo_read_u16](../hardware/P333_UART中断驱动接口.md#ga4a3c25dad2290f1f40e4b847e3b83f64)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

从FIFO读取宽数据。

<a id="r_ga9cbd6e33dce6a5b06233cf10077e19cc"></a>

```c
void uart_irq_tx_enable (const struct device *dev)
```

相关声明：[uart_irq_tx_enable](../hardware/P333_UART中断驱动接口.md#ga9cbd6e33dce6a5b06233cf10077e19cc)、[device](../device_reference/P002_设备对象结构.md)。

在中断使能寄存器（Interrupt Enable Register，IER）中使能TX中断。

<a id="r_gaf8a5bc26cd7c32e7bc6516c6f873c45a"></a>

```c
void uart_irq_tx_disable (const struct device *dev)
```

相关声明：[uart_irq_tx_disable](../hardware/P333_UART中断驱动接口.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)、[device](../device_reference/P002_设备对象结构.md)。

在IER中禁用TX中断。

<a id="r_ga5e126b5f19549eb7f5b785b98ebe7638"></a>

```c
static int uart_irq_tx_ready (const struct device *dev)
```

相关声明：[uart_irq_tx_ready](../hardware/P333_UART中断驱动接口.md#ga5e126b5f19549eb7f5b785b98ebe7638)、[device](../device_reference/P002_设备对象结构.md)。

检查UART发送缓冲区是否能够接受字节。

<a id="r_ga4ec3ae3974da2b3ab94ae7b835d17bad"></a>

```c
void uart_irq_rx_enable (const struct device *dev)
```

相关声明：[uart_irq_rx_enable](../hardware/P333_UART中断驱动接口.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)、[device](../device_reference/P002_设备对象结构.md)。

使能RX中断。

<a id="r_gaa759d7935fdd9ab6ca0761f161389a29"></a>

```c
void uart_irq_rx_disable (const struct device *dev)
```

相关声明：[uart_irq_rx_disable](../hardware/P333_UART中断驱动接口.md#gaa759d7935fdd9ab6ca0761f161389a29)、[device](../device_reference/P002_设备对象结构.md)。

禁用RX中断。

<a id="r_ga917935a13bf6a5d1e32ef34339e96455"></a>

```c
static int uart_irq_tx_complete (const struct device *dev)
```

相关声明：[uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)、[device](../device_reference/P002_设备对象结构.md)。

检查UART发送模块是否已完成传输。

<a id="r_gad04073b1b8e3de13b43ae1194561377b"></a>

```c
static int uart_irq_rx_ready (const struct device *dev)
```

相关声明：[uart_irq_rx_ready](../hardware/P333_UART中断驱动接口.md#gad04073b1b8e3de13b43ae1194561377b)、[device](../device_reference/P002_设备对象结构.md)。

检查UART接收缓冲区是否已有接收到的字符。

<a id="r_ga7c24daae3326bc2959ea13a2be79969f"></a>

```c
void uart_irq_err_enable (const struct device *dev)
```

相关声明：[uart_irq_err_enable](../hardware/P333_UART中断驱动接口.md#ga7c24daae3326bc2959ea13a2be79969f)、[device](../device_reference/P002_设备对象结构.md)。

使能错误中断（Error Interrupt）。

<a id="r_gaaf8a88361807e204f7227fbd1d0e75b2"></a>

```c
void uart_irq_err_disable (const struct device *dev)
```

相关声明：[uart_irq_err_disable](../hardware/P333_UART中断驱动接口.md#gaaf8a88361807e204f7227fbd1d0e75b2)、[device](../device_reference/P002_设备对象结构.md)。

禁用错误中断。

<a id="r_gacd8c2978e0f1316dd79bb42baad1c5a7"></a>

```c
static int uart_irq_is_pending (const struct device *dev)
```

相关声明：[uart_irq_is_pending](../hardware/P333_UART中断驱动接口.md#gacd8c2978e0f1316dd79bb42baad1c5a7)、[device](../device_reference/P002_设备对象结构.md)。

检查是否存在待处理的中断请求（Interrupt Request，IRQ）。

<a id="r_ga20cf50f53fb9e09e760c6499fd156ff2"></a>

```c
static void uart_irq_update (const struct device *dev)
```

相关声明：[uart_irq_update](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)、[device](../device_reference/P002_设备对象结构.md)。

在中断服务程序（Interrupt Service Routine，ISR）中开始处理中断。

<a id="r_gaf469966a56d1fc9f50108201597ee0a0"></a>

```c
static int uart_irq_callback_user_data_set (const struct device *dev, uart_irq_callback_user_data_t cb, void *user_data)
```

相关声明：[uart_irq_callback_user_data_set](../hardware/P333_UART中断驱动接口.md#gaf469966a56d1fc9f50108201597ee0a0)、[device](../device_reference/P002_设备对象结构.md)、[uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)。

设置IRQ回调函数指针。

<a id="r_ga5f7af3f7f0d9155349ea3b4fad78956c"></a>

```c
static int uart_irq_callback_set (const struct device *dev, uart_irq_callback_user_data_t cb)
```

相关声明：[uart_irq_callback_set](../hardware/P333_UART中断驱动接口.md#ga5f7af3f7f0d9155349ea3b4fad78956c)、[device](../device_reference/P002_设备对象结构.md)、[uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)。

设置IRQ回调函数指针的旧式接口（Legacy）。

<a id="r_gad33e627ed8729409b14e92453e53459c"></a>

```c
static int uart_callback_set (const struct device *dev, uart_callback_t callback, void *user_data)
```

相关声明：[uart_callback_set](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)、[device](../device_reference/P002_设备对象结构.md)、[uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)。

设置事件处理函数（Event Handler）。

<a id="r_gaf99f32ce2e2d9beb32a2f2e5a26320dc"></a>

```c
int uart_tx (const struct device *dev, const uint8_t *buf, size_t len, int32_t timeout)
```

相关声明：[uart_tx](../hardware/P334_UART异步接口.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

通过UART发送缓冲区中指定数量的字节。

<a id="r_gab0ea611cd072fa459a6f1780ce62c9e3"></a>

```c
int uart_tx_u16 (const struct device *dev, const uint16_t *buf, size_t len, int32_t timeout)
```

相关声明：[uart_tx_u16](../hardware/P334_UART异步接口.md#gab0ea611cd072fa459a6f1780ce62c9e3)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

通过UART发送缓冲区中指定数量的数据项。

<a id="r_gaa8a26d3ea685fb98030ea03613be6280"></a>

```c
int uart_tx_abort (const struct device *dev)
```

相关声明：[uart_tx_abort](../hardware/P334_UART异步接口.md#gaa8a26d3ea685fb98030ea03613be6280)、[device](../device_reference/P002_设备对象结构.md)。

中止当前TX传输（Abort）。

<a id="r_ga902e18c2a727ed2988e1b6caa6a444b8"></a>

```c
int uart_rx_enable (const struct device *dev, uint8_t *buf, size_t len, int32_t timeout)
```

相关声明：[uart_rx_enable](../hardware/P334_UART异步接口.md#ga902e18c2a727ed2988e1b6caa6a444b8)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

开始通过UART接收数据。

<a id="r_ga12d91846133351a85fa471fa90f2a0fd"></a>

```c
int uart_rx_enable_u16 (const struct device *dev, uint16_t *buf, size_t len, int32_t timeout)
```

相关声明：[uart_rx_enable_u16](../hardware/P334_UART异步接口.md#ga12d91846133351a85fa471fa90f2a0fd)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

开始通过UART接收宽数据。

<a id="r_ga3970fe2818e214b0814ea8b73a816a6a"></a>

```c
static int uart_rx_buf_rsp (const struct device *dev, uint8_t *buf, size_t len)
```

相关声明：[uart_rx_buf_rsp](../hardware/P334_UART异步接口.md#ga3970fe2818e214b0814ea8b73a816a6a)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

响应UART_RX_BUF_REQUEST事件，提供接收缓冲区。

<a id="r_ga778bcfc30be853c8d320f295b34c17c0"></a>

```c
static int uart_rx_buf_rsp_u16 (const struct device *dev, uint16_t *buf, size_t len)
```

相关声明：[uart_rx_buf_rsp_u16](../hardware/P334_UART异步接口.md#ga778bcfc30be853c8d320f295b34c17c0)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

响应UART_RX_BUF_REQUEST事件，提供宽数据接收缓冲区。

<a id="r_gafd4753bee51b230091a3c6ddb26ea734"></a>

```c
int uart_rx_disable (const struct device *dev)
```

相关声明：[uart_rx_disable](../hardware/P334_UART异步接口.md#gafd4753bee51b230091a3c6ddb26ea734)、[device](../device_reference/P002_设备对象结构.md)。

禁用RX。

<a id="r_gab039414b41145dc8d31349836da91263"></a>

```c
int uart_line_ctrl_set (const struct device *dev, uint32_t ctrl, uint32_t val)
```

相关声明：[uart_line_ctrl_set](../hardware/P330_UART公共接口.md#gab039414b41145dc8d31349836da91263)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

设置UART线路控制。

<a id="r_gafda8a550284a54c8e1d6b6638de978e5"></a>

```c
int uart_line_ctrl_get (const struct device *dev, uint32_t ctrl, uint32_t *val)
```

相关声明：[uart_line_ctrl_get](../hardware/P330_UART公共接口.md#gafda8a550284a54c8e1d6b6638de978e5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

读取UART线路控制。

<a id="r_gaa8683398e5d709b513509d08841ed51b"></a>

```c
int uart_drv_cmd (const struct device *dev, uint32_t cmd, uint32_t p)
```

相关声明：[uart_drv_cmd](../hardware/P330_UART公共接口.md#gaa8683398e5d709b513509d08841ed51b)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

向驱动发送额外命令（Driver Command）。

## 1.5\_源码定位与版本边界

相对源码定位：[UART公共头文件](../../../include/zephyr/drivers/uart.h)、[UART内部头文件](../../../include/zephyr/drivers/uart/uart_internal.h)、[系统调用处理](../../../drivers/serial/uart_handlers.c)、[串口配置选项](../../../drivers/serial/Kconfig)和[控制器绑定](../../../dts/bindings/serial/uart-controller.yaml)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：公共声明与内部实现：uart.h定义配置、事件与公共接口，在末尾包含uart/uart_internal.h和生成的syscalls/uart.h。内部头文件中的uart_driver_api及z_impl_*／内联包装负责把调用转交给驱动函数表；普通应用仍以公共头文件为入口。官方内部参考页将这些内容列为INTERNAL_HIDDEN，只有文件说明与源码入口，不能把它当成缺失了公开成员说明；完整可见代码在本册内部源码页保留。

> 译注——源码核对：枚举编码与配置值：UART_LINE_CTRL_*和UART_ERROR_*是位标志（Bit Flags），而数据位、停止位、奇偶校验与流控制枚举采用各自的顺序编码。UART_CFG_DATA_BITS_8不是整数8，不能直接把设备树data-bits数值赋给uart_config.data_bits；应使用对应枚举。uart_config.baudrate按原文字段说明使用bps，实际速率、格式和流控制是否可用取决于驱动及硬件。绑定中的current-speed、hw-flow-control等是初始化配置来源，不等于运行时已成功调用uart_configure。

> 译注——源码核对：三种传输方式：轮询输入（Polling Input）为非阻塞接口，轮询输出（Polling Output）可能等待发送条件。中断驱动（Interrupt-driven）由IRQ回调处理FIFO，异步API（Asynchronous API）由uart_event回调报告传输进度和完成。三类入口、回调签名与配置条件不同。UART_EXCLUSIVE_API_CALLBACKS在异步与中断接口同时启用时默认使两类回调互斥，具体清除动作由相应驱动落实；不能仅因两组选项都启用就假定同一设备可以同时保留两套回调。

> 译注——源码核对：中断处理顺序：官方公共约定要求先在ISR调用uart_irq_update，再查询RX／TX就绪、发送完成或挂起状态。当前uart_irq_update返回void，内部包装在驱动有irq_update操作时才调用它，不能写成依赖其整数返回值的判断。TX就绪时应填充FIFO并检查实际写入数量；RX就绪时持续读取，直至返回数量小于请求数量，避免假定中断一定按电平触发。错误返回应单独处理，不能把负errno当作成功计数或简单布尔真值。

> 译注——源码核对：异步事件与缓冲区：uart_tx／uart_rx_enable返回的是启动结果，完成与数据可用通过事件通知。UART_RX_RDY给出当前缓冲区内从offset开始、长度为len的新数据，不表示缓冲区已释放，同一缓冲区可以出现多次RDY。收到UART_RX_BUF_REQUEST时可提供下一缓冲区；驱动仍在使用的缓冲区不能再次提交，要等UART_RX_BUF_RELEASED后复用。停收或错误可先通知剩余数据，再释放缓冲区，最后报告UART_RX_DISABLED。

> 译注——源码核对：超时与宽数据单位：异步timeout单位为微秒（Microsecond），TX超时按原约定仅在流控制启用时有效；RX超时是至少收到一个字节后的不活动间隔，没有收到数据时不会单凭该间隔产生RDY。SYS_FOREVER_US禁用超时。带_u16接口以uint16_t容纳宽数据，FIFO与异步传输长度按数据项计；用户态校验也采用len乘sizeof(uint16_t)检查数组范围，不能把len直接当作字节数。公开事件字段的字节措辞按原文保留，宽数据场景仍须核对具体驱动的事件填充。

> 译注——源码核对：错误与空操作边界：运行时配置、线路控制、驱动命令、FIFO及多数中断状态查询，在对应功能未启用时返回-ENOTSUP；已启用但所检查的操作指针为空时返回-ENOSYS。部分void中断使能／禁用包装在缺少操作时不做任何事，宽数据轮询输出在功能未启用时同样为空操作。poll_out以及异步TX、RX和缓冲区提交包装在已编译分支中直接调用相应操作，不统一执行空指针检查。应按所用入口及设备能力判断，不能把一处检查推广给所有UART API。

> 译注——源码核对：用户态与回调边界：uart_handlers.c为系统调用核对设备对象／操作权限及输入输出缓冲区可访问范围；这些校验不代表内核内联包装也自动拥有相同检查。回调安装与rx_buf_rsp未提供同类系统调用入口，原注释明确回调安装不允许来自用户态，缓冲区响应用于ISR回调。自定义驱动命令的cmd是UART命令参数；原Doxygen页面将同名符号链接到显示协处理器函数，相关符号提示按原文保留，该交叉引用不意味着UART具有显示命令功能。

> 译注——源码核对：版本边界：本批核对公共与内部两个头文件、UART系统调用处理、串口Kconfig和公共控制器绑定，共五份官方源码并记录摘要。两份源码浏览页的非注释代码分别与读取的官方原始头文件一致；latest、滚动main与仓库参照版本不自动相同。仓库定位使用相对路径，本次未构建固件、打开串口、发送数据或操作硬件。

本次验证范围为文档与源码对照，未构建固件、打开串口或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/uart/uart_internal.h](P004_UART内部头文件源码.md)
- [查看此文件的源码](P002_UART驱动头文件源码.md)
- [uart_config](../hardware/P331_UART配置结构.md)
- [uart_event_tx](../hardware/P335_UART发送事件结构.md)
- [uart_event_rx](../hardware/P336_UART接收事件结构.md)
- [uart_event_rx_buf](../hardware/P337_UART缓冲区释放事件结构.md)
- [uart_event_rx_stop](../hardware/P338_UART接收停止事件结构.md)
- [uart_event](../hardware/P339_UART事件联合结构.md)
- [uart_event::uart_event_data](../hardware/P340_UART事件数据联合体.md)
- [uart_irq_callback_user_data_t](../hardware/P333_UART中断驱动接口.md#gad7a26b1a1d6212d7d39c05c8ad4ec926)
- [device](../device_reference/P002_设备对象结构.md)
- [uart_irq_callback_user_data_set()](../hardware/P333_UART中断驱动接口.md#gaf469966a56d1fc9f50108201597ee0a0)
- [uart_callback_t](../hardware/P334_UART异步接口.md#ga00b7c98a4da3ea3675d0a40c5dacb136)
- [uart_callback_set()](../hardware/P334_UART异步接口.md#gad33e627ed8729409b14e92453e53459c)
- [uart_line_ctrl](../hardware/P330_UART公共接口.md#ga02552532e171e789efc1b000917a9be0)
- [UART_LINE_CTRL_BAUD_RATE](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a3fdd02679f4f103190f3c12ab3cda00b)
- [UART_LINE_CTRL_RTS](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a205d22bd797ab1c55323dc1ffda75f0d)
- [UART_LINE_CTRL_DTR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a19e76af9901fc0274a9e27ff40e29e23)
- [UART_LINE_CTRL_DCD](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a6d2c438044dd64f5cef07bbe4c6b3e97)
- [UART_LINE_CTRL_DSR](../hardware/P330_UART公共接口.md#gga02552532e171e789efc1b000917a9be0a87d8bedb5c918c182b271884ee42d75c)
- [uart_rx_stop_reason](../hardware/P330_UART公共接口.md#gadeba6c5485e01dfc1c8a6e1c21668a88)
- [UART_ERROR_OVERRUN](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a442beffc51cdf265bbcb40810a9a6e54)
- [UART_ERROR_PARITY](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a86d38eac5a46e6659aa765164b833eb5)
- [UART_ERROR_FRAMING](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88af13f72a8c615b4bc570b5a4df573407b)
- [UART_BREAK](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a4986147e23cc46ab8c2aa7e151d09571)
- [UART_ERROR_COLLISION](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88aad8ca4dca9a846560293df71e6b39786)
- [UART_ERROR_NOISE](../hardware/P330_UART公共接口.md#ggadeba6c5485e01dfc1c8a6e1c21668a88a412058adbf7668b7051efb8419984d60)
- [uart_config_parity](../hardware/P330_UART公共接口.md#gab2ab6aacb6e3c43bb26d4274157e5711)
- [UART_CFG_PARITY_NONE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a6a23a2ef22fb3b144648b244fff82b8d)
- [UART_CFG_PARITY_ODD](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8a618b0a531c8d62809e39eb56eaf5ed)
- [UART_CFG_PARITY_EVEN](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711ac3a4310efe198a1fa7d977a5531486ba)
- [UART_CFG_PARITY_MARK](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a5ee61c29a32447644ff70385158a11ca)
- [UART_CFG_PARITY_SPACE](../hardware/P330_UART公共接口.md#ggab2ab6aacb6e3c43bb26d4274157e5711a8dc5306c8ca26321431bcf22ce9b036c)
- [uart_config_stop_bits](../hardware/P330_UART公共接口.md#gafc1aecb863e2456d73b78a49fcbad72e)
- [UART_CFG_STOP_BITS_0_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea308c660590a9fd16143806e8bef002af)
- [UART_CFG_STOP_BITS_1](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea73024f1618eb04385bf488214c635e58)
- [UART_CFG_STOP_BITS_1_5](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72ea1da47ec95b6a6eee65abef3d6d84f9ad)
- [UART_CFG_STOP_BITS_2](../hardware/P330_UART公共接口.md#ggafc1aecb863e2456d73b78a49fcbad72eae180ecebc76516e89669e1d16bfb31c6)
- [uart_config_data_bits](../hardware/P330_UART公共接口.md#gab9f7de744a68a311330576d7da02c44a)
- [UART_CFG_DATA_BITS_5](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa1b0545c2d1970e67d697b62510bfbe27)
- [UART_CFG_DATA_BITS_6](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aac6e0f3c0479164c34144d0e6e28298e4)
- [UART_CFG_DATA_BITS_7](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa6120eb8f668b257c8c2dd0dc9cf0c913)
- [UART_CFG_DATA_BITS_8](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aa23f55bdb24b4016c8c23c518e981df97)
- [UART_CFG_DATA_BITS_9](../hardware/P330_UART公共接口.md#ggab9f7de744a68a311330576d7da02c44aaf3b601af696d8841fe79871ca3e41e5f)
- [uart_config_flow_control](../hardware/P330_UART公共接口.md#ga8e2f1b4a8d60d7a6c24835d1b26f99e8)
- [UART_CFG_FLOW_CTRL_NONE](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a546b28db6f8bfc26266e8f7d6b8ff973)
- [UART_CFG_FLOW_CTRL_RTS_CTS](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8ad682bfe14a9f0860d1fdc3e8e9d56f86)
- [UART_CFG_FLOW_CTRL_DTR_DSR](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a0efc5de86bf80119f750cf372814309f)
- [UART_CFG_FLOW_CTRL_RS485](../hardware/P330_UART公共接口.md#gga8e2f1b4a8d60d7a6c24835d1b26f99e8a9675cc80d44e980b66e99bc8548f085c)
- [uart_event_type](../hardware/P334_UART异步接口.md#gaf0c9513cbafa36d86b4c83f2b6a03dcd)
- [UART_TX_DONE](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda4b5cdf863d8b6e5cd7b58f611808a6e4)
- [UART_TX_ABORTED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0abcf565ba1011815285bb3845f8d5a1)
- [UART_RX_RDY](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda7c70c3a56f64602f3d808b46e7b047f7)
- [UART_RX_BUF_REQUEST](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda0d250f372702526f1bce6d4dfe166abe)
- [UART_RX_BUF_RELEASED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdab2d152bd84f659d4fc4060df29811b48)
- [UART_RX_DISABLED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcdaa8ff5629c002a61bc3bdf5baa2ebc203)
- [UART_RX_STOPPED](../hardware/P334_UART异步接口.md#ggaf0c9513cbafa36d86b4c83f2b6a03dcda05b81ddf74d208aeabace6ac90ae52dd)
- [uart_err_check](../hardware/P330_UART公共接口.md#ga22ea20fd8e07153b3b71cc9416f5462f)
- [uart_poll_in](../hardware/P332_UART轮询接口.md#gae81ac8cc976a20d774cfbda09e9c983d)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [uart_poll_in_u16](../hardware/P332_UART轮询接口.md#gaad39c1358019bfdcb919da7982743553)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uart_poll_out](../hardware/P332_UART轮询接口.md#ga06ba27ba772a7a18462b8cdbc7f9353c)
- [uart_poll_out_u16](../hardware/P332_UART轮询接口.md#ga8faa3f58b9098c97e288e9c5f3367fd9)
- [uart_configure](../hardware/P330_UART公共接口.md#gaa0b75777b879af10543f7e8f463ff9a2)
- [uart_config_get](../hardware/P330_UART公共接口.md#ga81dfc5f2134de8e4acb5f063512cf703)
- [uart_fifo_fill](../hardware/P333_UART中断驱动接口.md#gafe42e4719eada7e25904bc9ebfe87791)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uart_fifo_fill_u16](../hardware/P333_UART中断驱动接口.md#gaa89f58818d8428ad6a11abf692c54c0d)
- [uart_fifo_read](../hardware/P333_UART中断驱动接口.md#gab10942076ac47ecff29e924098049398)
- [uart_fifo_read_u16](../hardware/P333_UART中断驱动接口.md#ga4a3c25dad2290f1f40e4b847e3b83f64)
- [uart_irq_tx_enable](../hardware/P333_UART中断驱动接口.md#ga9cbd6e33dce6a5b06233cf10077e19cc)
- [uart_irq_tx_disable](../hardware/P333_UART中断驱动接口.md#gaf8a5bc26cd7c32e7bc6516c6f873c45a)
- [uart_irq_tx_ready](../hardware/P333_UART中断驱动接口.md#ga5e126b5f19549eb7f5b785b98ebe7638)
- [uart_irq_rx_enable](../hardware/P333_UART中断驱动接口.md#ga4ec3ae3974da2b3ab94ae7b835d17bad)
- [uart_irq_rx_disable](../hardware/P333_UART中断驱动接口.md#gaa759d7935fdd9ab6ca0761f161389a29)
- [uart_irq_tx_complete](../hardware/P333_UART中断驱动接口.md#ga917935a13bf6a5d1e32ef34339e96455)
- [uart_irq_rx_ready](../hardware/P333_UART中断驱动接口.md#gad04073b1b8e3de13b43ae1194561377b)
- [uart_irq_err_enable](../hardware/P333_UART中断驱动接口.md#ga7c24daae3326bc2959ea13a2be79969f)
- [uart_irq_err_disable](../hardware/P333_UART中断驱动接口.md#gaaf8a88361807e204f7227fbd1d0e75b2)
- [uart_irq_is_pending](../hardware/P333_UART中断驱动接口.md#gacd8c2978e0f1316dd79bb42baad1c5a7)
- [uart_irq_update](../hardware/P333_UART中断驱动接口.md#ga20cf50f53fb9e09e760c6499fd156ff2)
- [uart_irq_callback_set](../hardware/P333_UART中断驱动接口.md#ga5f7af3f7f0d9155349ea3b4fad78956c)
- [uart_tx](../hardware/P334_UART异步接口.md#gaf99f32ce2e2d9beb32a2f2e5a26320dc)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [uart_tx_u16](../hardware/P334_UART异步接口.md#gab0ea611cd072fa459a6f1780ce62c9e3)
- [uart_tx_abort](../hardware/P334_UART异步接口.md#gaa8a26d3ea685fb98030ea03613be6280)
- [uart_rx_enable](../hardware/P334_UART异步接口.md#ga902e18c2a727ed2988e1b6caa6a444b8)
- [uart_rx_enable_u16](../hardware/P334_UART异步接口.md#ga12d91846133351a85fa471fa90f2a0fd)
- [uart_rx_buf_rsp](../hardware/P334_UART异步接口.md#ga3970fe2818e214b0814ea8b73a816a6a)
- [uart_rx_buf_rsp_u16](../hardware/P334_UART异步接口.md#ga778bcfc30be853c8d320f295b34c17c0)
- [uart_rx_disable](../hardware/P334_UART异步接口.md#gafd4753bee51b230091a3c6ddb26ea734)
- [uart_line_ctrl_set](../hardware/P330_UART公共接口.md#gab039414b41145dc8d31349836da91263)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uart_line_ctrl_get](../hardware/P330_UART公共接口.md#gafda8a550284a54c8e1d6b6638de978e5)
- [uart_drv_cmd](../hardware/P330_UART公共接口.md#gaa8683398e5d709b513509d08841ed51b)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_UART驱动头文件源码.md)
