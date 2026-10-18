---
id: learning.zephyr-docs.checksum-reference.page-2
title: UBX校验和头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/checksum_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_UBX校验和头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/checksum_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入校验和目录、UBX校验和宏与位反转接口参考，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_a6d1496f64e46cba548340c9c98697758"></a>

```c
#define UBX_CSUM_A(...)
```

相关声明：[UBX_CSUM_A](#a6d1496f64e46cba548340c9c98697758)。

用于在编译期计算 UBX 校验和（Checksum）的一组宏技巧。

<a id="r_a326f038f1130800d50ff861f5a7e0d9d"></a>

```c
#define UBX_CSUM_A_(...)
```

相关声明：[UBX_CSUM_A_](#a326f038f1130800d50ff861f5a7e0d9d)。

<a id="r_a72257fa1af8c2e6addda019b8da4b19c"></a>

```c
#define UBX_CSUM_A_I(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...)
```

相关声明：[UBX_CSUM_A_I](#a72257fa1af8c2e6addda019b8da4b19c)。

<a id="r_a01922620d77048df31c70368a68062c0"></a>

```c
#define UBX_CSUM_B(...)
```

相关声明：[UBX_CSUM_B](#a01922620d77048df31c70368a68062c0)。

<a id="r_a6d53729decd2998ddd2894d711397e0d"></a>

```c
#define UBX_CSUM_B_(...)
```

相关声明：[UBX_CSUM_B_](#a6d53729decd2998ddd2894d711397e0d)。

<a id="r_a98cbec44089842c71101b16342be39ac"></a>

```c
#define UBX_CSUM_B_I(len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ...)
```

相关声明：[UBX_CSUM_B_I](#a98cbec44089842c71101b16342be39ac)。

<a id="r_af30e21304d2621a9ef9d2a6edfe7332c"></a>

```c
#define UBX_CSUM(...)
```

相关声明：[UBX_CSUM](#af30e21304d2621a9ef9d2a6edfe7332c)。

## 2.2\_详细说明（Detailed Documentation）

<a id="af30e21304d2621a9ef9d2a6edfe7332c"></a>

### `UBX_CSUM`

```c
#define UBX_CSUM ( ...)
```

展开值（Value）：

```c
UBX_CSUM_A(__VA_ARGS__), UBX_CSUM_B(__VA_ARGS__)
```

<a id="a6d1496f64e46cba548340c9c98697758"></a>

### `UBX_CSUM_A`

```c
#define UBX_CSUM_A ( ...)
```

展开值（Value）：

```c
UBX_CSUM_A_(__VA_ARGS__)
```

用于在编译期计算 UBX 校验和（Checksum）的一组宏技巧。

<a id="a326f038f1130800d50ff861f5a7e0d9d"></a>

### `UBX_CSUM_A_`

```c
#define UBX_CSUM_A_ ( ...)
```

展开值（Value）：

```c
UBX_CSUM_A_I(__VA_ARGS__,                                            \
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

<a id="a72257fa1af8c2e6addda019b8da4b19c"></a>

### `UBX_CSUM_A_I`

```c
#define UBX_CSUM_A_I ( a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ... )
```

展开值（Value）：

```c
((a1) + (a2) + (a3) + (a4) + (a5) + (a6) + (a7) + (a8) + (a9) + (a10) +                    \
 (a11) + (a12) + (a13) + (a14) + (a15) + (a16) + (a17) + (a18) + (a19) + (a20)) & 0xFF
```

<a id="a01922620d77048df31c70368a68062c0"></a>

### `UBX_CSUM_B`

```c
#define UBX_CSUM_B ( ...)
```

展开值（Value）：

```c
UBX_CSUM_B_(__VA_ARGS__)
```

<a id="a6d53729decd2998ddd2894d711397e0d"></a>

### `UBX_CSUM_B_`

```c
#define UBX_CSUM_B_ ( ...)
```

展开值（Value）：

```c
UBX_CSUM_B_I(NUM_VA_ARGS(__VA_ARGS__), __VA_ARGS__,                           \
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
```

<a id="a98cbec44089842c71101b16342be39ac"></a>

### `UBX_CSUM_B_I`

```c
#define UBX_CSUM_B_I ( len, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, ... )
```

展开值（Value）：

```c
(((len) * a1) + ((len - 1) * a2) + ((len - 2) * a3) + ((len - 3) * a4) +                   \
 ((len - 4) * a5) + ((len - 5) * a6) + ((len - 6) * a7) + ((len - 7) * a8) +               \
 ((len - 8) * a9) + ((len - 9) * a10) + ((len - 10) * a11) + ((len - 11) * a12) +          \
 ((len - 12) * a13) + ((len - 13) * a14) + ((len - 14) * a15) + ((len - 15) * a16) +       \
 ((len - 16) * a17) + ((len - 17) * a18) + ((len - 18) * a19) + ((len - 19) * a20)) & 0xFF
```

## 2.3\_源码定位与版本边界

源码定位：[include/zephyr/modem/ubx/checksum.h](../../../include/zephyr/modem/ubx/checksum.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。仓库源码使用相对链接；未将头文件对照视为已进行协议通信或目标处理器指令验证。

> 译注——源码核对：此checksum.h位于include/zephyr/modem/ubx，专用于UBX校验和的编译期宏，不是CRC公共头文件，也不是接受指针和长度的运行时流式计算函数。本文只翻译官方头文件所展示的宏及原始说明。

> 译注——源码核对：UBX_CSUM_A按输入元素求和后取低8位；UBX_CSUM_B按元素位置进行加权求和后取低8位。UBX_CSUM展开为以逗号分隔的两个表达式，供两个校验字节使用，不是单一16位返回值。

> 译注——源码核对：当前内部宏显式接收a1至a20并用零补足参数；传入超过20项不能当作支持任意长度，尾部可变参数不会被求和表达式完整消费。调用者应遵守实际宏范围，不把它推广为通用数组处理。

> 译注——源码核对：原宏表达式、掩码、参数括号和求值方式保持原样。部分展开未对整个表达式额外加括号，且组合宏会复用参数；不要传入带副作用的表达式或假定任意嵌套运算都不受C运算符优先级影响。NUM_VA_ARGS来自宏工具，调用环境必须提供相应定义。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.4\_原页交叉引用（Cross References）

- [查看此文件的源码](P003_UBX校验和头文件源码.md)
- [NUM_VA_ARGS](../util_reference/P001_通用工具公共接口.md#ga1e5b59140ab2bf4471a512b689eda2cb)

<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="achecksum_8h_html_a01922620d77048df31c70368a68062c0"></a>
<a id="achecksum_8h_html_a6d1496f64e46cba548340c9c98697758"></a>
<a id="achecksum_8h_html_a326f038f1130800d50ff861f5a7e0d9d"></a>
<a id="achecksum_8h_html_a72257fa1af8c2e6addda019b8da4b19c"></a>
<a id="achecksum_8h_html_a6d53729decd2998ddd2894d711397e0d"></a>
<a id="achecksum_8h_html_a98cbec44089842c71101b16342be39ac"></a>
<a id="agroup__sys-util_html_ga1e5b59140ab2bf4471a512b689eda2cb"></a>

---

[上一章](P001_校验和主题目录.md) · [返回大纲](大纲.md) · [下一章](P003_UBX校验和头文件源码.md)
