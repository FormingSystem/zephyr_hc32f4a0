---
id: learning.zephyr-docs.stmesp-source-reference.page-3
title: STMESP底层头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stmesp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_STMESP底层头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stmesp_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入STMESP日志前端、解复用器与底层寄存器访问源码。源码跟踪译注与官方原文分开标示。

```c
#include <zephyr/devicetree.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.1\_函数（Functions）

<a id="r_ga2ffcc08b7d5c32c90b5d24982c0f6349"></a>

```c
static void stmesp_flag (STMESP_Type *reg, uint32_t data, bool ts, bool guaranteed)
```

相关声明：[stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向STMESP写入标志（Flag）。

<a id="r_ga4af9486d77c93a55f221c7647d69a9f2"></a>

```c
static void stmesp_data8 (STMESP_Type *reg, uint8_t data, bool ts, bool marked, bool guaranteed)
```

相关声明：[stmesp_data8](../trace_interface_reference/P002_STMESP底层接口.md#ga4af9486d77c93a55f221c7647d69a9f2)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向STMESP写入8位数据（8-bit Data）。

<a id="r_gaef1918a9d15d8da34fb5f2d7a11ff5fd"></a>

```c
static void stmesp_data16 (STMESP_Type *reg, uint16_t data, bool ts, bool marked, bool guaranteed)
```

相关声明：[stmesp_data16](../trace_interface_reference/P002_STMESP底层接口.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)、[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向STMESP写入16位数据（16-bit Data）。

<a id="r_gaa7885c5a7620e46a532dbf405bfc6034"></a>

```c
static void stmesp_data32 (STMESP_Type *reg, uint32_t data, bool ts, bool marked, bool guaranteed)
```

相关声明：[stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

向STMESP写入32位数据（32-bit Data）。

<a id="r_ga4350f5d201e3591221a932aa9fc3e94d"></a>

```c
static int stmesp_get_port (uint32_t idx, STMESP_Type **port)
```

相关声明：[stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

返回系统跟踪宏单元扩展激励端口（STM Extended Stimulus Port）的地址。

## 3.2\_源码定位与版本边界

源码定位：[include/zephyr/drivers/debug/stmesp.h](../../../include/zephyr/drivers/debug/stmesp.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。源码与译文采用相对链接。

> 译注——源码核对：系统跟踪宏单元（System Trace Macrocell，STM）的扩展激励端口（Extended Stimulus Port，ESP）采用内存映射寄存器访问（MMIO）。data8、data16、data32分别通过volatile指针执行对应位宽的写入，不是向普通RAM缓冲区复制日志。

> 译注——源码核对：时间戳（Timestamp）、标记（Marked）和保证型访问（Guaranteed Access）决定选用哪组寄存器。Guaranteed指STM访问类别，不能据此推断主机最终收到并解码了每条日志。

> 译注——源码核对：stmesp_get_port先检查输出指针是否为NULL，以及idx是否小于设备树寄存器区域大小除以单个STMESP_Type的大小。成功才写出端口地址；失败返回-EINVAL且不改写输出。idx是端口索引，不是字节地址。

> 译注——源码核对：取得端口地址依赖设备树（Devicetree）中stmesp节点的地址和大小，并不完成跟踪硬件、嵌入式跟踪路由器（Embedded Trace Router，ETR）或主机解码工具的初始化。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.3\_原页交叉引用（Cross References）

- [zephyr/devicetree.h](../dt_main_reference/P002_设备树主头文件源码.md)
- [查看此文件的源码](P004_STMESP底层头文件源码.md)
- [stmesp_flag](../trace_interface_reference/P002_STMESP底层接口.md#ga2ffcc08b7d5c32c90b5d24982c0f6349)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [stmesp_data8](../trace_interface_reference/P002_STMESP底层接口.md#ga4af9486d77c93a55f221c7647d69a9f2)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stmesp_data16](../trace_interface_reference/P002_STMESP底层接口.md#gaef1918a9d15d8da34fb5f2d7a11ff5fd)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [stmesp_data32](../trace_interface_reference/P002_STMESP底层接口.md#gaa7885c5a7620e46a532dbf405bfc6034)
- [stmesp_get_port](../trace_interface_reference/P002_STMESP底层接口.md#ga4350f5d201e3591221a932aa9fc3e94d)

---

[上一章](P002_STMESP日志解复用头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_STMESP底层头文件源码.md)
