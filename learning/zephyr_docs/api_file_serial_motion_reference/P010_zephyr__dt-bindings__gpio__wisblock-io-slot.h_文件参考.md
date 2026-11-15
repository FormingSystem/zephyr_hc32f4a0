---
id: learning.zephyr-docs.api-file-serial-motion-reference.page-10
title: zephyr__dt-bindings__gpio__wisblock-io-slot.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wisblock-io-slot_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第10章\_zephyr\_\_dt-bindings\_\_gpio\_\_wisblock-io-slot.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wisblock-io-slot_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

WisBlock IO插槽连接器（Slot Connector）的引脚常量。

查看此文件的源码。

<a id="details"></a>

WisBlock IO插槽连接器（Slot Connector）的引脚常量。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 10.1\_宏定义（Macros）

<a id="r_ga81ae1a0d2970827b58bf90ef39e8ba1b"></a>

```c
#define WISBLOCK_IO_SW1 0
```

相关声明：[WISBLOCK_IO_SW1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga81ae1a0d2970827b58bf90ef39e8ba1b)。

用户按键（User Button）SW1。

<a id="r_gae4da8fe8a9b492a361ec5b4376bab7da"></a>

```c
#define WISBLOCK_IO_TXD0 1
```

相关声明：[WISBLOCK_IO_TXD0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae4da8fe8a9b492a361ec5b4376bab7da)。

UART0 发送（TX）。

<a id="r_ga61ff8daa9465e449398fa64b6518ea0a"></a>

```c
#define WISBLOCK_IO_RXD0 2
```

相关声明：[WISBLOCK_IO_RXD0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga61ff8daa9465e449398fa64b6518ea0a)。

UART0 接收（RX）。

<a id="r_gaeb47ed056f293c3af1af140d0e83e2f0"></a>

```c
#define WISBLOCK_IO_LED1 3
```

相关声明：[WISBLOCK_IO_LED1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaeb47ed056f293c3af1af140d0e83e2f0)。

发光二极管（LED）1。

<a id="r_ga2d91a7fedbb6aaf97557a3a762a5966c"></a>

```c
#define WISBLOCK_IO_LED2 4
```

相关声明：[WISBLOCK_IO_LED2](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga2d91a7fedbb6aaf97557a3a762a5966c)。

发光二极管（LED）2。

<a id="r_gac9466845a4e3e1ccc6f3ad382f608197"></a>

```c
#define WISBLOCK_IO_LED3 5
```

相关声明：[WISBLOCK_IO_LED3](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gac9466845a4e3e1ccc6f3ad382f608197)。

发光二极管（LED）3。

<a id="r_ga7f87854690b71d3b16e502957a54940c"></a>

```c
#define WISBLOCK_IO_I2C1_SDA 6
```

相关声明：[WISBLOCK_IO_I2C1_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7f87854690b71d3b16e502957a54940c)。

I2C1 串行数据线（SDA）。

<a id="r_ga25b47986a25855467112d00632d0ae00"></a>

```c
#define WISBLOCK_IO_I2C1_SCL 7
```

相关声明：[WISBLOCK_IO_I2C1_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga25b47986a25855467112d00632d0ae00)。

I2C1 串行时钟线（SCL）。

<a id="r_gae45f636f59ca63c5735a444c4d2ff40e"></a>

```c
#define WISBLOCK_IO_AIN0 8
```

相关声明：[WISBLOCK_IO_AIN0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae45f636f59ca63c5735a444c4d2ff40e)。

模拟输入（Analog Input）0。

<a id="r_gadc38a7c488480a5444f1b767679a80b9"></a>

```c
#define WISBLOCK_IO_AIN1 9
```

相关声明：[WISBLOCK_IO_AIN1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gadc38a7c488480a5444f1b767679a80b9)。

模拟输入（Analog Input）1。

<a id="r_gad369693a1b14c1f285f8c19cc7fce9e4"></a>

```c
#define WISBLOCK_IO_IO7 10
```

相关声明：[WISBLOCK_IO_IO7](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gad369693a1b14c1f285f8c19cc7fce9e4)。

通用输入输出（General-purpose I/O）7。

<a id="r_ga46237ab4d1b762bdd32272a1cf58b6ac"></a>

```c
#define WISBLOCK_IO_SPI_CS 11
```

相关声明：[WISBLOCK_IO_SPI_CS](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga46237ab4d1b762bdd32272a1cf58b6ac)。

SPI 片选（Chip Select）。

<a id="r_ga7991add3b5c7d08e8bc4053286af9d9d"></a>

```c
#define WISBLOCK_IO_SPI_CLK 12
```

相关声明：[WISBLOCK_IO_SPI_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7991add3b5c7d08e8bc4053286af9d9d)。

SPI 时钟（Clock）。

<a id="r_ga3163e1fa627535666c5426af649c46c1"></a>

```c
#define WISBLOCK_IO_SPI_MISO 13
```

相关声明：[WISBLOCK_IO_SPI_MISO](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga3163e1fa627535666c5426af649c46c1)。

SPI 主入从出（MISO）。

<a id="r_ga925b6f4572ed370556d58139be2f34b7"></a>

```c
#define WISBLOCK_IO_SPI_MOSI 14
```

相关声明：[WISBLOCK_IO_SPI_MOSI](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga925b6f4572ed370556d58139be2f34b7)。

SPI 主出从入（MOSI）。

<a id="r_gaed1997d34383d4b627866605c6533c69"></a>

```c
#define WISBLOCK_IO_IO1 15
```

相关声明：[WISBLOCK_IO_IO1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed1997d34383d4b627866605c6533c69)。

通用输入输出（General-purpose I/O）1。

<a id="r_ga32aee335ff96b08d3fd916d1925e52f7"></a>

```c
#define WISBLOCK_IO_IO2 16
```

相关声明：[WISBLOCK_IO_IO2](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga32aee335ff96b08d3fd916d1925e52f7)。

通用输入输出（General-purpose I/O）2。

<a id="r_ga94cc339044680fc1eab735848cc855af"></a>

```c
#define WISBLOCK_IO_IO3 17
```

相关声明：[WISBLOCK_IO_IO3](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94cc339044680fc1eab735848cc855af)。

通用输入输出（General-purpose I/O）3。

<a id="r_ga94d626e6b185484ba1d4fa22413e5e9c"></a>

```c
#define WISBLOCK_IO_IO4 18
```

相关声明：[WISBLOCK_IO_IO4](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94d626e6b185484ba1d4fa22413e5e9c)。

通用输入输出（General-purpose I/O）4。

<a id="r_ga77dda9dbc3172c7a0492b720d0763ada"></a>

```c
#define WISBLOCK_IO_TXD1 19
```

相关声明：[WISBLOCK_IO_TXD1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga77dda9dbc3172c7a0492b720d0763ada)。

UART1 发送（TX）。

<a id="r_ga85109755bea2ace4475f65b9a605fe39"></a>

```c
#define WISBLOCK_IO_RXD1 20
```

相关声明：[WISBLOCK_IO_RXD1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga85109755bea2ace4475f65b9a605fe39)。

UART1 接收（RX）。

<a id="r_ga37e14b285c36c7530fd36166d549e6ee"></a>

```c
#define WISBLOCK_IO_I2C2_SDA 21
```

相关声明：[WISBLOCK_IO_I2C2_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga37e14b285c36c7530fd36166d549e6ee)。

I2C2 串行数据线（SDA）。

<a id="r_gaed675138e04d827fd0d33d263e0fee44"></a>

```c
#define WISBLOCK_IO_I2C2_SCL 22
```

相关声明：[WISBLOCK_IO_I2C2_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed675138e04d827fd0d33d263e0fee44)。

I2C2 串行时钟线（SCL）。

<a id="r_gaa3ed2adedb3c39592b37e0fbb3d975b3"></a>

```c
#define WISBLOCK_IO_IO5 23
```

相关声明：[WISBLOCK_IO_IO5](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaa3ed2adedb3c39592b37e0fbb3d975b3)。

通用输入输出（General-purpose I/O）5。

<a id="r_ga08d262e36b8b4d33ed6b52c27c2b7c1f"></a>

```c
#define WISBLOCK_IO_IO6 24
```

相关声明：[WISBLOCK_IO_IO6](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga08d262e36b8b4d33ed6b52c27c2b7c1f)。

通用输入输出（General-purpose I/O）6。


## 10.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P922_wisblock-io-slot.h_源码浏览.md)
- [WISBLOCK_IO_SW1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga81ae1a0d2970827b58bf90ef39e8ba1b)
- [WISBLOCK_IO_TXD0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae4da8fe8a9b492a361ec5b4376bab7da)
- [WISBLOCK_IO_RXD0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga61ff8daa9465e449398fa64b6518ea0a)
- [WISBLOCK_IO_LED1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaeb47ed056f293c3af1af140d0e83e2f0)
- [WISBLOCK_IO_LED2](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga2d91a7fedbb6aaf97557a3a762a5966c)
- [WISBLOCK_IO_LED3](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gac9466845a4e3e1ccc6f3ad382f608197)
- [WISBLOCK_IO_I2C1_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7f87854690b71d3b16e502957a54940c)
- [WISBLOCK_IO_I2C1_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga25b47986a25855467112d00632d0ae00)
- [WISBLOCK_IO_AIN0](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gae45f636f59ca63c5735a444c4d2ff40e)
- [WISBLOCK_IO_AIN1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gadc38a7c488480a5444f1b767679a80b9)
- [WISBLOCK_IO_IO7](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gad369693a1b14c1f285f8c19cc7fce9e4)
- [WISBLOCK_IO_SPI_CS](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga46237ab4d1b762bdd32272a1cf58b6ac)
- [WISBLOCK_IO_SPI_CLK](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga7991add3b5c7d08e8bc4053286af9d9d)
- [WISBLOCK_IO_SPI_MISO](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga3163e1fa627535666c5426af649c46c1)
- [WISBLOCK_IO_SPI_MOSI](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga925b6f4572ed370556d58139be2f34b7)
- [WISBLOCK_IO_IO1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed1997d34383d4b627866605c6533c69)
- [WISBLOCK_IO_IO2](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga32aee335ff96b08d3fd916d1925e52f7)
- [WISBLOCK_IO_IO3](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94cc339044680fc1eab735848cc855af)
- [WISBLOCK_IO_IO4](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga94d626e6b185484ba1d4fa22413e5e9c)
- [WISBLOCK_IO_TXD1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga77dda9dbc3172c7a0492b720d0763ada)
- [WISBLOCK_IO_RXD1](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga85109755bea2ace4475f65b9a605fe39)
- [WISBLOCK_IO_I2C2_SDA](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga37e14b285c36c7530fd36166d549e6ee)
- [WISBLOCK_IO_I2C2_SCL](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaed675138e04d827fd0d33d263e0fee44)
- [WISBLOCK_IO_IO5](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#gaa3ed2adedb3c39592b37e0fbb3d975b3)
- [WISBLOCK_IO_IO6](https://docs.zephyrproject.org/latest/doxygen/html/group__wisblock-io-slot.html#ga08d262e36b8b4d33ed6b52c27c2b7c1f)

<a id="header-details"></a>

---

[上一章](P009_zephyr__drivers__mm__system_mm.h_文件参考.md) · [返回大纲](大纲.md)
