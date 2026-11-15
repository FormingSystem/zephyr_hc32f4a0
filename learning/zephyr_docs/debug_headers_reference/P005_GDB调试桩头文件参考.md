---
id: learning.zephyr-docs.debug-headers-reference.page-5
title: GDB调试桩头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gdbstub_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_GDB调试桩头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gdbstub_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入核心转储公共接口、伪设备驱动和GDB调试桩头文件参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_gdb_5Fmem_5Fregion"></a>

```c
struct gdb_mem_region
```

相关声明：[gdb_mem_region](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)。

描述一个内存区域。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_a34e3537cdca807d30b24ce76ab1e503c"></a>

```c
#define GDB_EXCEPTION_INVALID_INSTRUCTION 4UL
```

相关声明：[GDB_EXCEPTION_INVALID_INSTRUCTION](#a34e3537cdca807d30b24ce76ab1e503c)。

<a id="r_af97b5ae81a45e635e69c613b4e2fa9f4"></a>

```c
#define GDB_EXCEPTION_BREAKPOINT 5UL
```

相关声明：[GDB_EXCEPTION_BREAKPOINT](#af97b5ae81a45e635e69c613b4e2fa9f4)。

<a id="r_a37ea8e51fd123a434d6d221280cedca2"></a>

```c
#define GDB_EXCEPTION_MEMORY_FAULT 7UL
```

相关声明：[GDB_EXCEPTION_MEMORY_FAULT](#a37ea8e51fd123a434d6d221280cedca2)。

<a id="r_ad65b407f7c8d6d44ab5886866ee2d9da"></a>

```c
#define GDB_EXCEPTION_DIVIDE_ERROR 8UL
```

相关声明：[GDB_EXCEPTION_DIVIDE_ERROR](#ad65b407f7c8d6d44ab5886866ee2d9da)。

<a id="r_a94da0c93f951fc608c76a525251a9d3a"></a>

```c
#define GDB_EXCEPTION_INVALID_MEMORY 11UL
```

相关声明：[GDB_EXCEPTION_INVALID_MEMORY](#a94da0c93f951fc608c76a525251a9d3a)。

<a id="r_acc588c5509a9cf55df485b90dff54ba4"></a>

```c
#define GDB_EXCEPTION_OVERFLOW 16UL
```

相关声明：[GDB_EXCEPTION_OVERFLOW](#acc588c5509a9cf55df485b90dff54ba4)。

<a id="r_a02b9a9d5f33f9ee43bfdd0e68a9a6462"></a>

```c
#define GDB_MEM_REGION_NO_ACCESS 0UL
```

相关声明：[GDB_MEM_REGION_NO_ACCESS](#a02b9a9d5f33f9ee43bfdd0e68a9a6462)。

<a id="r_a8a7f81403bcc747817792171bf502d1a"></a>

```c
#define GDB_MEM_REGION_READ BIT(0)
```

相关声明：[GDB_MEM_REGION_READ](#a8a7f81403bcc747817792171bf502d1a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_adb7926e4055fc3ffd94da16c9f0a97b6"></a>

```c
#define GDB_MEM_REGION_WRITE BIT(1)
```

相关声明：[GDB_MEM_REGION_WRITE](#adb7926e4055fc3ffd94da16c9f0a97b6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

<a id="r_a083549c8b9db7f28536481e33d362479"></a>

```c
#define GDB_MEM_REGION_RO (GDB_MEM_REGION_READ)
```

相关声明：[GDB_MEM_REGION_RO](#a083549c8b9db7f28536481e33d362479)、[GDB_MEM_REGION_READ](#a8a7f81403bcc747817792171bf502d1a)。

<a id="r_a386751baaedc3e607a37a473a88bb05a"></a>

```c
#define GDB_MEM_REGION_RW (GDB_MEM_REGION_READ | GDB_MEM_REGION_WRITE)
```

相关声明：[GDB_MEM_REGION_RW](#a386751baaedc3e607a37a473a88bb05a)、[GDB_MEM_REGION_READ](#a8a7f81403bcc747817792171bf502d1a)、[GDB_MEM_REGION_WRITE](#adb7926e4055fc3ffd94da16c9f0a97b6)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.3\_枚举（Enumerations）

<a id="r_aa266df02c8e0a69322bb2a6d40670c57"></a>

```c
enum gdb_loop_state { GDB_LOOP_RECEIVING , GDB_LOOP_CONTINUE , GDB_LOOP_ERROR }
```

相关声明：[gdb_loop_state](#aa266df02c8e0a69322bb2a6d40670c57)、[GDB_LOOP_RECEIVING](#aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73)、[GDB_LOOP_CONTINUE](#aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a)、[GDB_LOOP_ERROR](#aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077)。

数据包处理循环的状态（Packet Processing Loop State）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 5.4\_函数（Functions）

<a id="r_ab392b604a2edf4bea077eb7fa02079e1"></a>

```c
size_t gdb_bin2hex (const uint8_t *buf, size_t buflen, char *hex, size_t hexlen)
```

相关声明：[gdb_bin2hex](#ab392b604a2edf4bea077eb7fa02079e1)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将二进制数组转换为字符串表示。

<a id="r_add890d2dc6e197a2b94c45c4de94c8b1"></a>

```c
bool gdb_mem_can_read (const uintptr_t addr, const size_t len, uint8_t *align)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gdb_mem_can_read](#add890d2dc6e197a2b94c45c4de94c8b1)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查能否读取一个内存块。

<a id="r_aac6c53353a4751d835028c6fd9906d19"></a>

```c
bool gdb_mem_can_write (const uintptr_t addr, const size_t len, uint8_t *align)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[gdb_mem_can_write](#aac6c53353a4751d835028c6fd9906d19)、[uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

检查能否写入一个内存块。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 5.5\_变量（Variables）

<a id="r_a9d01831c656bae3ee4592ccb45456295"></a>

```c
const struct gdb_mem_region gdb_mem_region_array []
```

相关声明：[gdb_mem_region](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)、[gdb_mem_region_array](#a9d01831c656bae3ee4592ccb45456295)。

供 GDB 内存访问使用的内存区域描述。

<a id="r_a439e80da6ae6e5388f9a78744d0978d1"></a>

```c
const size_t gdb_mem_num_regions
```

相关声明：[gdb_mem_num_regions](#a439e80da6ae6e5388f9a78744d0978d1)。

内存区域数量。

## 5.6\_详细说明（Detailed Documentation）

<a id="af97b5ae81a45e635e69c613b4e2fa9f4"></a>

### `GDB_EXCEPTION_BREAKPOINT`

```c
#define GDB_EXCEPTION_BREAKPOINT 5UL
```

<a id="ad65b407f7c8d6d44ab5886866ee2d9da"></a>

### `GDB_EXCEPTION_DIVIDE_ERROR`

```c
#define GDB_EXCEPTION_DIVIDE_ERROR 8UL
```

<a id="a34e3537cdca807d30b24ce76ab1e503c"></a>

### `GDB_EXCEPTION_INVALID_INSTRUCTION`

```c
#define GDB_EXCEPTION_INVALID_INSTRUCTION 4UL
```

<a id="a94da0c93f951fc608c76a525251a9d3a"></a>

### `GDB_EXCEPTION_INVALID_MEMORY`

```c
#define GDB_EXCEPTION_INVALID_MEMORY 11UL
```

<a id="a37ea8e51fd123a434d6d221280cedca2"></a>

### `GDB_EXCEPTION_MEMORY_FAULT`

```c
#define GDB_EXCEPTION_MEMORY_FAULT 7UL
```

<a id="acc588c5509a9cf55df485b90dff54ba4"></a>

### `GDB_EXCEPTION_OVERFLOW`

```c
#define GDB_EXCEPTION_OVERFLOW 16UL
```

<a id="a02b9a9d5f33f9ee43bfdd0e68a9a6462"></a>

### `GDB_MEM_REGION_NO_ACCESS`

```c
#define GDB_MEM_REGION_NO_ACCESS 0UL
```

<a id="a8a7f81403bcc747817792171bf502d1a"></a>

### `GDB_MEM_REGION_READ`

```c
#define GDB_MEM_REGION_READ BIT(0)
```

<a id="a083549c8b9db7f28536481e33d362479"></a>

### `GDB_MEM_REGION_RO`

```c
#define GDB_MEM_REGION_RO (GDB_MEM_REGION_READ)
```

<a id="a386751baaedc3e607a37a473a88bb05a"></a>

### `GDB_MEM_REGION_RW`

```c
#define GDB_MEM_REGION_RW (GDB_MEM_REGION_READ | GDB_MEM_REGION_WRITE)
```

<a id="adb7926e4055fc3ffd94da16c9f0a97b6"></a>

### `GDB_MEM_REGION_WRITE`

```c
#define GDB_MEM_REGION_WRITE BIT(1)
```

<a id="aa266df02c8e0a69322bb2a6d40670c57"></a>

### `gdb_loop_state`

```c
enum gdb_loop_state
```

数据包处理循环的状态（Packet Processing Loop State）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `GDB_LOOP_RECEIVING` |  |
| `GDB_LOOP_CONTINUE` |  |
| `GDB_LOOP_ERROR` |  |

<a id="ab392b604a2edf4bea077eb7fa02079e1"></a>

### `gdb_bin2hex()`

```c
size_t gdb_bin2hex ( const uint8_t * buf, size_t buflen, char * hex, size_t hexlen )
```

将二进制数组转换为字符串表示。

注意，此函数与 `bin2hex()` 类似，但不会强制在十六进制输出缓冲区末尾追加空字符（Null Character）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 待转换的二进制数组。 |
| `buflen` | 待转换的二进制数组长度。 |
| `hex` | 用于存储字符串表示的地址。 |
| `hexlen` | 用于存储字符串表示的存储区大小。 |

返回（Returns）：转换后的字符串长度；发生错误时为 0。

> 译注——源码核对：gdb_bin2hex每个输入字节输出两个十六进制字符，当前实现要求hexlen至少为2*buflen，且不追加字符串结束空字符。需要C字符串时，调用者必须另预留并设置结束字符，不能直接把协议载荷当作已终止字符串。

<a id="add890d2dc6e197a2b94c45c4de94c8b1"></a>

### `gdb_mem_can_read()`

```c
bool gdb_mem_can_read ( const uintptr_t addr, const size_t len, uint8_t * align )
```

检查能否读取一个内存块。

检查能否读取指定的内存块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] addr` | 内存块的起始地址。 |
| `[in] len` | 内存块大小。 |
| `[out] align` | 区域的读取对齐要求（Read Alignment）。 |

返回（Returns）：能够读取内存块时为 true，否则为 false。

> 译注——源码核对：gdb_mem_can_read与gdb_mem_can_write按GDB区域描述检查属性，并通过align输出所需对齐。它们不是操作系统的用户权限检查，也不是对地址实际可访问性的无故障探测；表项和硬件状态仍需正确。 当前gdb_mem_num_regions为0时，两项函数把访问视为不受区域表限制，返回true并设置align为1。空表不是拒绝所有地址，也不能据返回true断言任意物理地址都可安全访问。

<a id="aac6c53353a4751d835028c6fd9906d19"></a>

### `gdb_mem_can_write()`

```c
bool gdb_mem_can_write ( const uintptr_t addr, const size_t len, uint8_t * align )
```

检查能否写入一个内存块。

检查能否写入指定的内存块。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] addr` | 内存块的起始地址。 |
| `[in] len` | 内存块大小。 |
| `[out] align` | 区域的写入对齐要求（Write Alignment）。 |

返回（Returns）：GDB 调试桩（GDB Stub）能够写入该内存块时为 true，否则为 false。

> 译注——源码核对：gdb_mem_can_read与gdb_mem_can_write按GDB区域描述检查属性，并通过align输出所需对齐。它们不是操作系统的用户权限检查，也不是对地址实际可访问性的无故障探测；表项和硬件状态仍需正确。 当前gdb_mem_num_regions为0时，两项函数把访问视为不受区域表限制，返回true并设置align为1。空表不是拒绝所有地址，也不能据返回true断言任意物理地址都可安全访问。

<a id="a439e80da6ae6e5388f9a78744d0978d1"></a>

### `gdb_mem_num_regions`

```c
const size_t gdb_mem_num_regions
```

声明属性：`extern`。

内存区域数量。

`gdb_mem_region_array[]` 中的元素数量。

<a id="a9d01831c656bae3ee4592ccb45456295"></a>

### `gdb_mem_region_array`

```c
const struct gdb_mem_region gdb_mem_region_array[]
```

声明属性：`extern`。

供 GDB 内存访问使用的内存区域描述。

此数组指定 GDB 可以访问哪些内存区域及其读写属性，用于将 GDB 调试桩的内存读写限制在能够合法访问、不会引发内存故障的内存中。

## 5.7\_源码定位与版本边界

源码定位：[include/zephyr/debug/gdbstub.h](../../../include/zephyr/debug/gdbstub.h)、[subsys/debug/gdbstub/gdbstub.c](../../../subsys/debug/gdbstub/gdbstub.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。仓库源码使用相对链接；源码和文档核对不表示已在目标板触发故障、生成转储或连接GDB调试会话。

> 译注——源码核对：gdb_bin2hex每个输入字节输出两个十六进制字符，当前实现要求hexlen至少为2*buflen，且不追加字符串结束空字符。需要C字符串时，调用者必须另预留并设置结束字符，不能直接把协议载荷当作已终止字符串。

> 译注——源码核对：gdb_mem_can_read与gdb_mem_can_write按GDB区域描述检查属性，并通过align输出所需对齐。它们不是操作系统的用户权限检查，也不是对地址实际可访问性的无故障探测；表项和硬件状态仍需正确。

> 译注——源码核对：当前gdb_mem_num_regions为0时，两项函数把访问视为不受区域表限制，返回true并设置align为1。空表不是拒绝所有地址，也不能据返回true断言任意物理地址都可安全访问。

> 译注——源码核对：存在区域表时，当前查找实现要求addr及addr+len均落入同一个条目的比较范围，并使用严格小于end的条件。因此不能自行推断恰好到达end的请求一定获准，或把相邻条目自动合并成一个范围。

> 译注——源码核对：align是输出参数，当前代码在成功路径写入区域对齐值或默认1；失败路径可能不修改它，调用者应先检查布尔结果。配置中的对齐值为0表示使用默认对齐，不表示可以把0当作有效访问宽度。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.8\_原页交叉引用（Cross References）

- [查看此文件的源码](P006_GDB调试桩头文件源码.md)
- [gdb_mem_region](https://docs.zephyrproject.org/latest/doxygen/html/structgdb__mem__region.html)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [bin2hex()](../util_reference/P001_通用工具公共接口.md#gaf8f2ab98cc3f045ba834dbbb13a5dfd7)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aa266df02c8e0a69322bb2a6d40670c57ae6d3b76f57693d31a91014cb1d595f73"></a>
<a id="aa266df02c8e0a69322bb2a6d40670c57a7bb32aeeb3ec6d88e37bf05306cb5e4a"></a>
<a id="aa266df02c8e0a69322bb2a6d40670c57a00f30ed14785675b4c9f8392cf5e8077"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="doc-var-members"></a>
<a id="header-doc-var-members"></a>

---

[上一章](P004_核心转储驱动头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_GDB调试桩头文件源码.md)
