---
id: learning.zephyr-docs.debug-headers-reference.page-6
title: GDB调试桩头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gdbstub_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_GDB调试桩头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/gdbstub_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P005_GDB调试桩头文件参考.md)和[公共API](P005_GDB调试桩头文件参考.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00023"></a>
<a id="foldopen00026"></a>
<a id="foldopen00030"></a>
<a id="foldopen00047"></a>
<a id="agdbstub_8h_html_a439e80da6ae6e5388f9a78744d0978d1"></a>
<a id="agdbstub_8h_html_a9d01831c656bae3ee4592ccb45456295"></a>
<a id="agdbstub_8h_html_aa266df02c8e0a69322bb2a6d40670c57"></a>
<a id="agdbstub_8h_html_aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077"></a>
<a id="agdbstub_8h_html_aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a"></a>
<a id="agdbstub_8h_html_aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73"></a>
<a id="agdbstub_8h_html_aac6c53353a4751d835028c6fd9906d19"></a>
<a id="agdbstub_8h_html_ab392b604a2edf4bea077eb7fa02079e1"></a>
<a id="agdbstub_8h_html_add890d2dc6e197a2b94c45c4de94c8b1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructgdb__mem__region_html"></a>
<a id="astructgdb__mem__region_html_a16001ef766b3c5775c1d1b2c59575b74"></a>
<a id="astructgdb__mem__region_html_a463465123fd373996a857b38c71474b3"></a>
<a id="astructgdb__mem__region_html_aa714bde657eb3572367a924298dd927f"></a>
<a id="astructgdb__mem__region_html_ad8ae6acf6950428a9846a25fb0219eeb"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2020 Intel Corporation
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DEBUG_GDBSTUB_H_
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DEBUG_GDBSTUB_H_
<a id="l00009"></a>
<a id="l00010"></a>/* Map from CPU exceptions to GDB  */
<a id="l00011"></a>#define GDB_EXCEPTION_INVALID_INSTRUCTION   4UL
<a id="l00012"></a>#define GDB_EXCEPTION_BREAKPOINT            5UL
<a id="l00013"></a>#define GDB_EXCEPTION_MEMORY_FAULT          7UL
<a id="l00014"></a>#define GDB_EXCEPTION_DIVIDE_ERROR          8UL
<a id="l00015"></a>#define GDB_EXCEPTION_INVALID_MEMORY        11UL
<a id="l00016"></a>#define GDB_EXCEPTION_OVERFLOW              16UL
<a id="l00017"></a>
<a id="l00018"></a>/* Access permissions for memory regions */
<a id="l00019"></a>#define GDB_MEM_REGION_NO_ACCESS            0UL
<a id="l00020"></a>#define GDB_MEM_REGION_READ                 BIT(0)
<a id="l00021"></a>#define GDB_MEM_REGION_WRITE                BIT(1)
<a id="l00022"></a>
<a id="l00023"></a>#define GDB_MEM_REGION_RO \
<a id="l00024"></a>        (GDB_MEM_REGION_READ)
<a id="l00025"></a>
<a id="l00026"></a>#define GDB_MEM_REGION_RW \
<a id="l00027"></a>        (GDB_MEM_REGION_READ | GDB_MEM_REGION_WRITE)
<a id="l00028"></a>
<a id="l00030"></a>struct gdb_mem_region {
<a id="l00032"></a>        uintptr_t start;
<a id="l00033"></a>
<a id="l00035"></a>        uintptr_t end;
<a id="l00036"></a>
<a id="l00038"></a>        uint16_t  attributes;
<a id="l00039"></a>
<a id="l00041"></a>        uint8_t   alignment;
<a id="l00042"></a>};
<a id="l00043"></a>
<a id="l00047"></a>enum gdb_loop_state {
<a id="l00048"></a>        GDB_LOOP_RECEIVING,
<a id="l00049"></a>        GDB_LOOP_CONTINUE,
<a id="l00050"></a>        GDB_LOOP_ERROR,
<a id="l00051"></a>};
<a id="l00052"></a>
<a id="l00061"></a>extern const struct gdb_mem_region gdb_mem_region_array[];
<a id="l00062"></a>
<a id="l00068"></a>extern const size_t gdb_mem_num_regions;
<a id="l00069"></a>
<a id="l00083"></a>size_t gdb_bin2hex(const uint8_t *buf, size_t buflen,
<a id="l00084"></a>                   char *hex, size_t hexlen);
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00098"></a>bool gdb_mem_can_read(const uintptr_t addr, const size_t len, uint8_t *align);
<a id="l00099"></a>
<a id="l00111"></a>bool gdb_mem_can_write(const uintptr_t addr, const size_t len, uint8_t *align);
<a id="l00112"></a>
<a id="l00113"></a>#endif
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2020 Intel Corporation；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. 从CPU异常映射到GDB异常编号。

3. 内存区域的访问权限（Access Permissions）。

## 6.3\_原页符号提示（Symbol Descriptions）

### `gdb_mem_num_regions`

```c
const size_t gdb_mem_num_regions
```

内存区域数量。

符号定位：[gdb_mem_num_regions](P005_GDB调试桩头文件参考.md#a439e80da6ae6e5388f9a78744d0978d1)。

### `gdb_mem_region_array`

```c
const struct gdb_mem_region gdb_mem_region_array[]
```

供 GDB 内存访问使用的内存区域描述。

符号定位：[gdb_mem_region_array](P005_GDB调试桩头文件参考.md#a9d01831c656bae3ee4592ccb45456295)。

### `gdb_loop_state`

```c
gdb_loop_state
```

数据包处理循环的状态（Packet Processing Loop State）。

定义位置（Definition）：gdbstub.h:47。

符号定位：[gdb_loop_state](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57)。

### `GDB_LOOP_ERROR`

```c
@ GDB_LOOP_ERROR
```

定义位置（Definition）：gdbstub.h:50。

符号定位：[GDB_LOOP_ERROR](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077)。

### `GDB_LOOP_CONTINUE`

```c
@ GDB_LOOP_CONTINUE
```

定义位置（Definition）：gdbstub.h:49。

符号定位：[GDB_LOOP_CONTINUE](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a)。

### `GDB_LOOP_RECEIVING`

```c
@ GDB_LOOP_RECEIVING
```

定义位置（Definition）：gdbstub.h:48。

符号定位：[GDB_LOOP_RECEIVING](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73)。

### `gdb_mem_can_write`

```c
bool gdb_mem_can_write(const uintptr_t addr, const size_t len, uint8_t *align)
```

检查能否写入一个内存块。

符号定位：[gdb_mem_can_write](P005_GDB调试桩头文件参考.md#aac6c53353a4751d835028c6fd9906d19)。

### `gdb_bin2hex`

```c
size_t gdb_bin2hex(const uint8_t *buf, size_t buflen, char *hex, size_t hexlen)
```

将二进制数组转换为字符串表示。

符号定位：[gdb_bin2hex](P005_GDB调试桩头文件参考.md#ab392b604a2edf4bea077eb7fa02079e1)。

### `gdb_mem_can_read`

```c
bool gdb_mem_can_read(const uintptr_t addr, const size_t len, uint8_t *align)
```

检查能否读取一个内存块。

符号定位：[gdb_mem_can_read](P005_GDB调试桩头文件参考.md#add890d2dc6e197a2b94c45c4de94c8b1)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `uintptr_t`

```c
__UINTPTR_TYPE__ uintptr_t
```

定义位置（Definition）：stdint.h:105。

符号定位：[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `gdb_mem_region`

描述一个内存区域。

定义位置（Definition）：gdbstub.h:30。

符号定位：[gdb_mem_region](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)。

### `gdb_mem_region::end`

```c
uintptr_t end
```

内存区域的结束地址。

定义位置（Definition）：gdbstub.h:35。

符号定位：[gdb_mem_region::end](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#a16001ef766b3c5775c1d1b2c59575b74)。

### `gdb_mem_region::start`

```c
uintptr_t start
```

内存区域的起始地址。

定义位置（Definition）：gdbstub.h:32。

符号定位：[gdb_mem_region::start](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#a463465123fd373996a857b38c71474b3)。

### `gdb_mem_region::alignment`

```c
uint8_t alignment
```

读写对齐要求，0表示使用默认对齐。

定义位置（Definition）：gdbstub.h:41。

符号定位：[gdb_mem_region::alignment](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#aa714bde657eb3572367a924298dd927f)。

### `gdb_mem_region::attributes`

```c
uint16_t attributes
```

内存区域属性（Memory Region Attributes）。

定义位置（Definition）：gdbstub.h:38。

符号定位：[gdb_mem_region::attributes](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#ad8ae6acf6950428a9846a25fb0219eeb)。

## 6.4\_源码跟踪译注

> 译注——gdb_bin2hex每个输入字节输出两个十六进制字符，当前实现要求hexlen至少为2*buflen，且不追加字符串结束空字符。需要C字符串时，调用者必须另预留并设置结束字符，不能直接把协议载荷当作已终止字符串。

> 译注——gdb_mem_can_read与gdb_mem_can_write按GDB区域描述检查属性，并通过align输出所需对齐。它们不是操作系统的用户权限检查，也不是对地址实际可访问性的无故障探测；表项和硬件状态仍需正确。

> 译注——当前gdb_mem_num_regions为0时，两项函数把访问视为不受区域表限制，返回true并设置align为1。空表不是拒绝所有地址，也不能据返回true断言任意物理地址都可安全访问。

> 译注——存在区域表时，当前查找实现要求addr及addr+len均落入同一个条目的比较范围，并使用严格小于end的条件。因此不能自行推断恰好到达end的请求一定获准，或把相邻条目自动合并成一个范围。

> 译注——align是输出参数，当前代码在成功路径写入区域对齐值或默认1；失败路径可能不修改它，调用者应先检查布尔结果。配置中的对齐值为0表示使用默认对齐，不表示可以把0当作有效访问宽度。

头文件定位：[include/zephyr/debug/gdbstub.h](../../../include/zephyr/debug/gdbstub.h)，关联实现／接口：[subsys/debug/gdbstub/gdbstub.c](../../../subsys/debug/gdbstub/gdbstub.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/debug/gdbstub.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/gdbstub/gdbstub.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P005_GDB调试桩头文件参考.md)
- [gdb_mem_region](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [start](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#a463465123fd373996a857b38c71474b3)
- [end](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#a16001ef766b3c5775c1d1b2c59575b74)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [attributes](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#ad8ae6acf6950428a9846a25fb0219eeb)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [alignment](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html#aa714bde657eb3572367a924298dd927f)
- [gdb_loop_state](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57)
- [GDB_LOOP_RECEIVING](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73)
- [GDB_LOOP_CONTINUE](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a)
- [GDB_LOOP_ERROR](P005_GDB调试桩头文件参考.md#aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077)
- [gdb_mem_region_array](P005_GDB调试桩头文件参考.md#a9d01831c656bae3ee4592ccb45456295)
- [gdb_mem_num_regions](P005_GDB调试桩头文件参考.md#a439e80da6ae6e5388f9a78744d0978d1)
- [gdb_bin2hex](P005_GDB调试桩头文件参考.md#ab392b604a2edf4bea077eb7fa02079e1)
- [gdb_mem_can_read](P005_GDB调试桩头文件参考.md#add890d2dc6e197a2b94c45c4de94c8b1)
- [gdb_mem_can_write](P005_GDB调试桩头文件参考.md#aac6c53353a4751d835028c6fd9906d19)

---

[上一章](P005_GDB调试桩头文件参考.md) · [返回大纲](大纲.md)
