---
id: learning.zephyr-docs.rtio-work-reference.page-4
title: RTIO寄存器列表
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__regs_1_1rtio__regs__list.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_RTIO寄存器列表

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__regs_1_1rtio__regs__list.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入寄存器映射、工作队列的参考与源码浏览页及相关结构体，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

单个内存块的描述。

```c
#include <zephyr/rtio/regmap.h>
```

<a id="details"></a>

单个内存块的描述。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_afbcfb27d914d7c7c55c0efa214df1274"></a>

```c
uint8_t reg_addr
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reg_addr](#afbcfb27d914d7c7c55c0efa214df1274)。

寄存器地址（Register Address）。

<a id="r_a3a35dd42e3fdd4159b35da38f327bfbd"></a>

```c
uint8_t * bufp
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bufp](#a3a35dd42e3fdd4159b35da38f327bfbd)。

指向数据缓冲区的有效指针。

<a id="r_ac5fc22a14818e9beb4e9952122f0753a"></a>

```c
size_t len
```

相关声明：[len](#ac5fc22a14818e9beb4e9952122f0753a)。

缓冲区长度，单位为字节。

## 4.2\_详细说明（Detailed Documentation）

<a id="a3a35dd42e3fdd4159b35da38f327bfbd"></a>

### `bufp`

```c
uint8_t* rtio_regs::rtio_regs_list::bufp
```

指向数据缓冲区的有效指针。

<a id="ac5fc22a14818e9beb4e9952122f0753a"></a>

### `len`

```c
size_t rtio_regs::rtio_regs_list::len
```

缓冲区长度，单位为字节。

<a id="afbcfb27d914d7c7c55c0efa214df1274"></a>

### `reg_addr`

```c
uint8_t rtio_regs::rtio_regs_list::reg_addr
```

寄存器地址（Register Address）。

## 4.3\_源码定位与版本边界

相对源码定位：[寄存器辅助头文件](../../../include/zephyr/rtio/regmap.h)、[工作队列头文件](../../../include/zephyr/rtio/work.h)、[工作队列实现](../../../subsys/rtio/rtio_workq.c)、[工作队列配置](../../../subsys/rtio/Kconfig.workq)、[核心接口](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)及[P4队列类型](../../../include/zephyr/sys/p4wq.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：对列表中的每一项，辅助函数先准备一个1字节tiny_write发送寄存器地址，再准备一个read读取数据。前者设置TRANSACTION，使地址与读取成为一个事务；后者设置CHAINED，使下一项或末尾回调在之后执行。I2C／I3C读取条目还设置STOP和RESTART；SPI分支不自动设置读方向位，调用者必须按设备协议预先设置reg_addr。

> 译注——源码核对：寄存器地址在准备时复制到tiny_write的内部数组，读取目标bufp只保存引用，数据缓冲区必须在异步使用期间有效；不能因函数返回就释放。reg_addr是uint8_t，len是size_t，但read准备函数的长度参数为uint32_t；使用方应遵守实际地址和长度表示范围，不能把此辅助函数当作任意宽度寄存器地址传输器。

> 译注——源码核对：一个列表项表示从reg_addr起读取len字节到bufp，不要求不同项的目标内存连续。调用者提供有效的缓冲区及设备允许的寄存器访问范围。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界；仓库源码使用相对链接，未加入本机环境路径或实板操作前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.4\_原页交叉引用（Cross References）

- [zephyr/rtio/regmap.h](P002_RTIO寄存器映射头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_RTIO寄存器配置.md) · [返回大纲](大纲.md) · [下一章](P005_RTIO工作队列头文件参考.md)
