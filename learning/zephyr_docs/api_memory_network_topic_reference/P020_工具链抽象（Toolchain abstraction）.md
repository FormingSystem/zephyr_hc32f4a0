---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-20
title: 工具链抽象（Toolchain abstraction）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第20章\_工具链抽象（Toolchain abstraction）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

利用工具链专用属性（Attribute）和/或编译指示（Pragma）来抽象编译器能力的宏。

<a id="details"></a>

利用工具链专用属性（Attribute）和/或编译指示（Pragma）来抽象编译器能力的宏。

<a id="header-files"></a>
<a id="files"></a>

## 20.1\_文件（Files）

<a id="r_toolchain_2Eh"></a>

```c
file toolchain.h
```

相关声明：[toolchain.h](../api_file_clock_network_reference/P025_zephyr__toolchain.h_文件参考.md)。

抽象工具链专有能力（Toolchain Specific Capabilities）的宏。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 20.2\_编译器内建功能、版本与特性探测（Compiler Builtins, Versions, and Feature Probes）

<a id="r_ga474a719388efd0578c7c98a0961e23dd"></a>

```c
#define HAS_BUILTIN(x)
```

相关声明：[HAS_BUILTIN](#ga474a719388efd0578c7c98a0961e23dd)。

检查编译器是否支持内建函数（Built-in Function）x。

<a id="r_gacbf8a21b471b2086cbe276789c5061d5"></a>

```c
#define TOOLCHAIN_GCC_VERSION 0
```

相关声明：[TOOLCHAIN_GCC_VERSION](#gacbf8a21b471b2086cbe276789c5061d5)。

将 GCC 版本 xx.yy.zz 表示为 xxyyzz。

<a id="r_gacdbda8f5e81a320dfdbc32bda1b33fad"></a>

```c
#define TOOLCHAIN_CLANG_VERSION 0
```

相关声明：[TOOLCHAIN_CLANG_VERSION](#gacdbda8f5e81a320dfdbc32bda1b33fad)。

将 Clang 版本 xx.yy.zz 表示为 xxyyzz。

<a id="r_ga763b60a74b3b8917b8a91614f1d443e4"></a>

```c
#define TOOLCHAIN_HAS_PRAGMA_DIAG 0
```

相关声明：[TOOLCHAIN_HAS_PRAGMA_DIAG](#ga763b60a74b3b8917b8a91614f1d443e4)。

指示工具链是否支持 #pragma diagnostics（诊断指令）。

<a id="r_ga49263980cf39cd330a9e9976dccb4c90"></a>

```c
#define TOOLCHAIN_HAS_C_GENERIC 0
```

相关声明：[TOOLCHAIN_HAS_C_GENERIC](#ga49263980cf39cd330a9e9976dccb4c90)。

指示工具链是否支持 C 泛型（C Generic）。

<a id="r_ga9502cad506e0dfb7c3a7b51b5eeb5eeb"></a>

```c
#define TOOLCHAIN_HAS_C_AUTO_TYPE 0
```

相关声明：[TOOLCHAIN_HAS_C_AUTO_TYPE](#ga9502cad506e0dfb7c3a7b51b5eeb5eeb)。

指示工具链是否支持 C __auto_type。

<a id="r_ga90e5fd6ed234d1494c7f156635c2e6e1"></a>

```c
#define TOOLCHAIN_HAS_ZLA 0
```

相关声明：[TOOLCHAIN_HAS_ZLA](#ga90e5fd6ed234d1494c7f156635c2e6e1)。

指示工具链是否支持零长度数组（Zero Length Arrays）。

<a id="r_ga4bd2473c4ecff861c6bc3e187b0fee12"></a>

```c
#define TOOLCHAIN_PRAGMA(x)
```

相关声明：[TOOLCHAIN_PRAGMA](#ga4bd2473c4ecff861c6bc3e187b0fee12)。

在宏中使用 pragma 指令的辅助接口。

## 20.3\_编译器警告标识符（Compiler Warning Identifiers）

<a id="r_gaef9c3722dc2b189226eb2e6223c080bf"></a>

```c
#define TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER
```

相关声明：[TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER](#gaef9c3722dc2b189226eb2e6223c080bf)。

工具链专用警告：获取紧凑布局成员地址（Address of a Packed Member）。

<a id="r_ga8b81dbfdc3dde900a58540709a4f1dff"></a>

```c
#define TOOLCHAIN_WARNING_ARRAY_BOUNDS
```

相关声明：[TOOLCHAIN_WARNING_ARRAY_BOUNDS](#ga8b81dbfdc3dde900a58540709a4f1dff)。

工具链专用警告：数组越界（Array Bounds Violations）。

<a id="r_ga5f5fef9bda4762c368f26c9028cdd34a"></a>

```c
#define TOOLCHAIN_WARNING_ATTRIBUTES
```

相关声明：[TOOLCHAIN_WARNING_ATTRIBUTES](#ga5f5fef9bda4762c368f26c9028cdd34a)。

工具链专用警告：未知属性（Unknown Attributes）。

<a id="r_ga003b55bfd0a8b95a4e57e419eb980a39"></a>

```c
#define TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR
```

相关声明：[TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR](#ga003b55bfd0a8b95a4e57e419eb980a39)。

工具链专用警告：通过指针删除析构函数非虚的对象（Non-virtual Destructor）。

<a id="r_ga64d8f26c21ee3639e82d93783e09387e"></a>

```c
#define TOOLCHAIN_WARNING_EXTRA
```

相关声明：[TOOLCHAIN_WARNING_EXTRA](#ga64d8f26c21ee3639e82d93783e09387e)。

工具链专用警告：额外警告（Extra Warnings）。

<a id="r_ga3e95e267a042393b4a1cada284e3244c"></a>

```c
#define TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER
```

相关声明：[TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER](#ga3e95e267a042393b4a1cada284e3244c)。

工具链专用警告：启用 VFP 时，Arm 中断服务例程（Interrupt Service Routines）可能破坏 VFP 状态。

<a id="r_gaf990df9b277505b97d4c9c2549fffa9f"></a>

```c
#define TOOLCHAIN_WARNING_NONNULL
```

相关声明：[TOOLCHAIN_WARNING_NONNULL](#gaf990df9b277505b97d4c9c2549fffa9f)。

工具链专用警告：向标有 nonnull 的函数传递空指针参数（Null Pointer Arguments）。

<a id="r_ga9c83552055a1817801dedc6655fc0cbf"></a>

```c
#define TOOLCHAIN_WARNING_POINTER_ARITH
```

相关声明：[TOOLCHAIN_WARNING_POINTER_ARITH](#ga9c83552055a1817801dedc6655fc0cbf)。

工具链专用警告：指针运算（Pointer Arithmetic）。

<a id="r_gae917ae1adad468956fa5d28a50d10670"></a>

```c
#define TOOLCHAIN_WARNING_SHADOW
```

相关声明：[TOOLCHAIN_WARNING_SHADOW](#gae917ae1adad468956fa5d28a50d10670)。

工具链专用警告：遮蔽变量（Shadow Variables）。

<a id="r_ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9"></a>

```c
#define TOOLCHAIN_WARNING_UNUSED_LABEL
```

相关声明：[TOOLCHAIN_WARNING_UNUSED_LABEL](#ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9)。

工具链专用警告：未使用标签（Unused Labels）。

<a id="r_gac567335f987f8f89640e22bd8e3e9385"></a>

```c
#define TOOLCHAIN_WARNING_UNUSED_VARIABLE
```

相关声明：[TOOLCHAIN_WARNING_UNUSED_VARIABLE](#gac567335f987f8f89640e22bd8e3e9385)。

工具链专用警告：未使用变量（Unused Variables）。

<a id="r_ga17e576d00c76be3c3eeaddba5907d0ef"></a>

```c
#define TOOLCHAIN_WARNING_ALWAYS_INLINE
```

相关声明：[TOOLCHAIN_WARNING_ALWAYS_INLINE](#ga17e576d00c76be3c3eeaddba5907d0ef)。

工具链专用警告：内联函数（Inline Functions）。

<a id="r_ga2db0c0472e8635d69ada180695da4c1c"></a>

```c
#define TOOLCHAIN_WARNING_CAST_QUAL
```

相关声明：[TOOLCHAIN_WARNING_CAST_QUAL](#ga2db0c0472e8635d69ada180695da4c1c)。

工具链专用警告：移除类型限定符（Type Qualifier）的指针转换。

## 20.4\_编译器警告控制（Compiler Warning Control）

<a id="r_ga1f08471f8dba6ce2a3e0f38bea73d7b5"></a>

```c
#define TOOLCHAIN_DISABLE_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_WARNING](#ga1f08471f8dba6ce2a3e0f38bea73d7b5)。

对所有编译器禁用指定编译器警告（Compiler Warning）。

<a id="r_ga5365fdbb6323f48ddca9ab4149e9a561"></a>

```c
#define TOOLCHAIN_ENABLE_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_WARNING](#ga5365fdbb6323f48ddca9ab4149e9a561)。

对所有编译器重新启用指定编译器警告（Compiler Warning）。

<a id="r_gac4bfe24556e3dd2bfb093434a4e98517"></a>

```c
#define TOOLCHAIN_DISABLE_CLANG_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_CLANG_WARNING](#gac4bfe24556e3dd2bfb093434a4e98517)。

对 Clang 禁用指定编译器警告（Compiler Warning）。

<a id="r_ga35eaaf7a69eae890687c196e81304667"></a>

```c
#define TOOLCHAIN_ENABLE_CLANG_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_CLANG_WARNING](#ga35eaaf7a69eae890687c196e81304667)。

对 Clang 重新启用指定编译器警告（Compiler Warning）。

<a id="r_ga245aa1544cf704ac88da3904e0982f05"></a>

```c
#define TOOLCHAIN_DISABLE_GCC_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_GCC_WARNING](#ga245aa1544cf704ac88da3904e0982f05)。

对 GCC 禁用指定编译器警告（Compiler Warning）。

<a id="r_ga57a000da2786521299f7bc9460977c60"></a>

```c
#define TOOLCHAIN_ENABLE_GCC_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_GCC_WARNING](#ga57a000da2786521299f7bc9460977c60)。

对 GCC 重新启用指定编译器警告（Compiler Warning）。

<a id="r_gaace39dc11f4da885c3a75210519cff13"></a>

```c
#define TOOLCHAIN_DISABLE_IAR_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_IAR_WARNING](#gaace39dc11f4da885c3a75210519cff13)。

对 IAR 编译器禁用指定编译器警告（Compiler Warning）。

<a id="r_ga8a1fc59f2665be53c4e183d295d91e15"></a>

```c
#define TOOLCHAIN_ENABLE_IAR_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_IAR_WARNING](#ga8a1fc59f2665be53c4e183d295d91e15)。

对 IAR 编译器重新启用指定编译器警告（Compiler Warning）。

## 20.5\_详细说明（Detailed Documentation）

<a id="ga474a719388efd0578c7c98a0961e23dd"></a>

### `HAS_BUILTIN`

```c
#define HAS_BUILTIN ( x)
```

```c
#include <zephyr/toolchain.h>
```

展开值（Value）：

```c
HAS_BUILTIN_##x
```

检查编译器是否支持内建函数（Built-in Function）x。

此宏用于条件编译（Conditional Compilation），以启用使用内建函数的代码，因为并非所有编译器都提供该内建函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | 内建函数标识符（Built-in Function Identifier），包括开头的下划线。 |

**返回（Returns）**：返回值（Returns）：支持此内建函数时返回非零值，否则返回 0。

<a id="gacdbda8f5e81a320dfdbc32bda1b33fad"></a>

### `TOOLCHAIN_CLANG_VERSION`

```c
#define TOOLCHAIN_CLANG_VERSION 0
```

```c
#include <zephyr/toolchain.h>
```

将 Clang 版本 xx.yy.zz 表示为 xxyyzz。

不兼容 Clang 时为 0。

<a id="gac4bfe24556e3dd2bfb093434a4e98517"></a>

### `TOOLCHAIN_DISABLE_CLANG_WARNING`

```c
#define TOOLCHAIN_DISABLE_CLANG_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 Clang 禁用指定编译器警告（Compiler Warning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | Clang 警告标识符（Warning Identifier）。 |

<a id="ga245aa1544cf704ac88da3904e0982f05"></a>

### `TOOLCHAIN_DISABLE_GCC_WARNING`

```c
#define TOOLCHAIN_DISABLE_GCC_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 GCC 禁用指定编译器警告（Compiler Warning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | GCC 警告标识符（Warning Identifier）。 |

<a id="gaace39dc11f4da885c3a75210519cff13"></a>

### `TOOLCHAIN_DISABLE_IAR_WARNING`

```c
#define TOOLCHAIN_DISABLE_IAR_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 IAR 编译器禁用指定编译器警告（Compiler Warning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | IAR 警告标识符（Warning Identifier）。 |

<a id="ga1f08471f8dba6ce2a3e0f38bea73d7b5"></a>

### `TOOLCHAIN_DISABLE_WARNING`

```c
#define TOOLCHAIN_DISABLE_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对所有编译器禁用指定编译器警告（Compiler Warning）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | 工具链专用警告标识符（Toolchain-specific Warning Identifier）。 |

<a id="ga35eaaf7a69eae890687c196e81304667"></a>

### `TOOLCHAIN_ENABLE_CLANG_WARNING`

```c
#define TOOLCHAIN_ENABLE_CLANG_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 Clang 重新启用指定编译器警告（Compiler Warning）。

只能在调用 TOOLCHAIN_DISABLE_CLANG_WARNING 之后使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | Clang 警告标识符（Warning Identifier）。 |

<a id="ga57a000da2786521299f7bc9460977c60"></a>

### `TOOLCHAIN_ENABLE_GCC_WARNING`

```c
#define TOOLCHAIN_ENABLE_GCC_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 GCC 重新启用指定编译器警告（Compiler Warning）。

只能在调用 TOOLCHAIN_DISABLE_GCC_WARNING 之后使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | GCC 警告标识符（Warning Identifier）。 |

<a id="ga8a1fc59f2665be53c4e183d295d91e15"></a>

### `TOOLCHAIN_ENABLE_IAR_WARNING`

```c
#define TOOLCHAIN_ENABLE_IAR_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对 IAR 编译器重新启用指定编译器警告（Compiler Warning）。

只能在调用 TOOLCHAIN_DISABLE_IAR_WARNING 之后使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | IAR 警告标识符（Warning Identifier）。 |

<a id="ga5365fdbb6323f48ddca9ab4149e9a561"></a>

### `TOOLCHAIN_ENABLE_WARNING`

```c
#define TOOLCHAIN_ENABLE_WARNING ( warning)
```

```c
#include <zephyr/toolchain.h>
```

对所有编译器重新启用指定编译器警告（Compiler Warning）。

只能在调用 TOOLCHAIN_DISABLE_WARNING 之后使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `warning` | 工具链专用警告标识符（Toolchain-specific Warning Identifier）。 |

<a id="gacbf8a21b471b2086cbe276789c5061d5"></a>

### `TOOLCHAIN_GCC_VERSION`

```c
#define TOOLCHAIN_GCC_VERSION 0
```

```c
#include <zephyr/toolchain.h>
```

将 GCC 版本 xx.yy.zz 表示为 xxyyzz。

不兼容 GCC 时为 0。

<a id="ga9502cad506e0dfb7c3a7b51b5eeb5eeb"></a>

### `TOOLCHAIN_HAS_C_AUTO_TYPE`

```c
#define TOOLCHAIN_HAS_C_AUTO_TYPE 0
```

```c
#include <zephyr/toolchain.h>
```

指示工具链是否支持 C __auto_type。

<a id="ga49263980cf39cd330a9e9976dccb4c90"></a>

### `TOOLCHAIN_HAS_C_GENERIC`

```c
#define TOOLCHAIN_HAS_C_GENERIC 0
```

```c
#include <zephyr/toolchain.h>
```

指示工具链是否支持 C 泛型（C Generic）。

<a id="ga763b60a74b3b8917b8a91614f1d443e4"></a>

### `TOOLCHAIN_HAS_PRAGMA_DIAG`

```c
#define TOOLCHAIN_HAS_PRAGMA_DIAG 0
```

```c
#include <zephyr/toolchain.h>
```

指示工具链是否支持 #pragma diagnostics（诊断指令）。

<a id="ga90e5fd6ed234d1494c7f156635c2e6e1"></a>

### `TOOLCHAIN_HAS_ZLA`

```c
#define TOOLCHAIN_HAS_ZLA 0
```

```c
#include <zephyr/toolchain.h>
```

指示工具链是否支持零长度数组（Zero Length Arrays）。

<a id="ga4bd2473c4ecff861c6bc3e187b0fee12"></a>

### `TOOLCHAIN_PRAGMA`

```c
#define TOOLCHAIN_PRAGMA ( x)
```

```c
#include <zephyr/toolchain.h>
```

在宏中使用 pragma 指令的辅助接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `x` | pragma 指令正文（Pragma Directive Body）。 |

<a id="gaef9c3722dc2b189226eb2e6223c080bf"></a>

### `TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER`

```c
#define TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：获取紧凑布局成员地址（Address of a Packed Member）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga17e576d00c76be3c3eeaddba5907d0ef"></a>

### `TOOLCHAIN_WARNING_ALWAYS_INLINE`

```c
#define TOOLCHAIN_WARNING_ALWAYS_INLINE
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：内联函数（Inline Functions）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga3e95e267a042393b4a1cada284e3244c"></a>

### `TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER`

```c
#define TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：启用 VFP 时，Arm 中断服务例程（Interrupt Service Routines）可能破坏 VFP 状态。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga8b81dbfdc3dde900a58540709a4f1dff"></a>

### `TOOLCHAIN_WARNING_ARRAY_BOUNDS`

```c
#define TOOLCHAIN_WARNING_ARRAY_BOUNDS
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：数组越界（Array Bounds Violations）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga5f5fef9bda4762c368f26c9028cdd34a"></a>

### `TOOLCHAIN_WARNING_ATTRIBUTES`

```c
#define TOOLCHAIN_WARNING_ATTRIBUTES
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：未知属性（Unknown Attributes）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga2db0c0472e8635d69ada180695da4c1c"></a>

### `TOOLCHAIN_WARNING_CAST_QUAL`

```c
#define TOOLCHAIN_WARNING_CAST_QUAL
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：移除类型限定符（Type Qualifier）的指针转换。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga003b55bfd0a8b95a4e57e419eb980a39"></a>

### `TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR`

```c
#define TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：通过指针删除析构函数非虚的对象（Non-virtual Destructor）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga64d8f26c21ee3639e82d93783e09387e"></a>

### `TOOLCHAIN_WARNING_EXTRA`

```c
#define TOOLCHAIN_WARNING_EXTRA
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：额外警告（Extra Warnings）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="gaf990df9b277505b97d4c9c2549fffa9f"></a>

### `TOOLCHAIN_WARNING_NONNULL`

```c
#define TOOLCHAIN_WARNING_NONNULL
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：向标有 nonnull 的函数传递空指针参数（Null Pointer Arguments）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga9c83552055a1817801dedc6655fc0cbf"></a>

### `TOOLCHAIN_WARNING_POINTER_ARITH`

```c
#define TOOLCHAIN_WARNING_POINTER_ARITH
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：指针运算（Pointer Arithmetic）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="gae917ae1adad468956fa5d28a50d10670"></a>

### `TOOLCHAIN_WARNING_SHADOW`

```c
#define TOOLCHAIN_WARNING_SHADOW
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：遮蔽变量（Shadow Variables）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9"></a>

### `TOOLCHAIN_WARNING_UNUSED_LABEL`

```c
#define TOOLCHAIN_WARNING_UNUSED_LABEL
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：未使用标签（Unused Labels）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。

<a id="gac567335f987f8f89640e22bd8e3e9385"></a>

### `TOOLCHAIN_WARNING_UNUSED_VARIABLE`

```c
#define TOOLCHAIN_WARNING_UNUSED_VARIABLE
```

```c
#include <zephyr/toolchain.h>
```

工具链专用警告：未使用变量（Unused Variables）。

将此项用作 `TOOLCHAIN_DISABLE_WARNING` 和 `TOOLCHAIN_ENABLE_WARNING` 宏族（Macro Family）的参数。


## 20.6\_原页交叉引用（Cross References）

- [toolchain.h](../api_file_clock_network_reference/P025_zephyr__toolchain.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P019_Renesas 事件链接控制器（ELC）.md) · [返回大纲](大纲.md)
