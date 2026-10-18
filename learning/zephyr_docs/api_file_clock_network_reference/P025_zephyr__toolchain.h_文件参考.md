---
id: learning.zephyr-docs.api-file-clock-network-reference.page-25
title: zephyr__toolchain.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_toolchain.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/toolchain_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

抽象工具链专有能力（Toolchain Specific Capabilities）的宏。

查看此文件的源码。

<a id="details"></a>

抽象工具链专用能力（Toolchain-specific Capabilities）的宏。本文件包含多种宏，通过工具链专用属性及／或 pragma 指令抽象编译器能力（Compiler Capabilities）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 25.1\_宏定义（Macros）

<a id="define-members-0"></a>

### 编译器内建功能、版本与特性探测（Compiler Builtins, Versions, and Feature Probes）

<a id="r_ga474a719388efd0578c7c98a0961e23dd"></a>

```c
#define HAS_BUILTIN(x)
```

相关声明：[HAS_BUILTIN](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga474a719388efd0578c7c98a0961e23dd)。

检查编译器是否支持内建函数（Built-in Function）x。

<a id="r_gacbf8a21b471b2086cbe276789c5061d5"></a>

```c
#define TOOLCHAIN_GCC_VERSION 0
```

相关声明：[TOOLCHAIN_GCC_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gacbf8a21b471b2086cbe276789c5061d5)。

将 GCC 版本 xx.yy.zz 表示为 xxyyzz。

<a id="r_gacdbda8f5e81a320dfdbc32bda1b33fad"></a>

```c
#define TOOLCHAIN_CLANG_VERSION 0
```

相关声明：[TOOLCHAIN_CLANG_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gacdbda8f5e81a320dfdbc32bda1b33fad)。

将 Clang 版本 xx.yy.zz 表示为 xxyyzz。

<a id="r_ga763b60a74b3b8917b8a91614f1d443e4"></a>

```c
#define TOOLCHAIN_HAS_PRAGMA_DIAG 0
```

相关声明：[TOOLCHAIN_HAS_PRAGMA_DIAG](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga763b60a74b3b8917b8a91614f1d443e4)。

指示工具链是否支持 #pragma diagnostics（诊断指令）。

<a id="r_ga49263980cf39cd330a9e9976dccb4c90"></a>

```c
#define TOOLCHAIN_HAS_C_GENERIC 0
```

相关声明：[TOOLCHAIN_HAS_C_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga49263980cf39cd330a9e9976dccb4c90)。

指示工具链是否支持 C 泛型（C Generic）。

<a id="r_ga9502cad506e0dfb7c3a7b51b5eeb5eeb"></a>

```c
#define TOOLCHAIN_HAS_C_AUTO_TYPE 0
```

相关声明：[TOOLCHAIN_HAS_C_AUTO_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga9502cad506e0dfb7c3a7b51b5eeb5eeb)。

指示工具链是否支持 C __auto_type。

<a id="r_ga90e5fd6ed234d1494c7f156635c2e6e1"></a>

```c
#define TOOLCHAIN_HAS_ZLA 0
```

相关声明：[TOOLCHAIN_HAS_ZLA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga90e5fd6ed234d1494c7f156635c2e6e1)。

指示工具链是否支持零长度数组（Zero Length Arrays）。

<a id="r_ga4bd2473c4ecff861c6bc3e187b0fee12"></a>

```c
#define TOOLCHAIN_PRAGMA(x)
```

相关声明：[TOOLCHAIN_PRAGMA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga4bd2473c4ecff861c6bc3e187b0fee12)。

在宏中使用 pragma 指令的辅助接口。

<a id="define-members-1"></a>

### 编译器警告标识符（Compiler Warning Identifiers）

<a id="r_gaef9c3722dc2b189226eb2e6223c080bf"></a>

```c
#define TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER
```

相关声明：[TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaef9c3722dc2b189226eb2e6223c080bf)。

工具链专用警告：获取紧凑布局成员地址（Address of a Packed Member）。

<a id="r_ga8b81dbfdc3dde900a58540709a4f1dff"></a>

```c
#define TOOLCHAIN_WARNING_ARRAY_BOUNDS
```

相关声明：[TOOLCHAIN_WARNING_ARRAY_BOUNDS](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga8b81dbfdc3dde900a58540709a4f1dff)。

工具链专用警告：数组越界（Array Bounds Violations）。

<a id="r_ga5f5fef9bda4762c368f26c9028cdd34a"></a>

```c
#define TOOLCHAIN_WARNING_ATTRIBUTES
```

相关声明：[TOOLCHAIN_WARNING_ATTRIBUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5f5fef9bda4762c368f26c9028cdd34a)。

工具链专用警告：未知属性（Unknown Attributes）。

<a id="r_ga003b55bfd0a8b95a4e57e419eb980a39"></a>

```c
#define TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR
```

相关声明：[TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga003b55bfd0a8b95a4e57e419eb980a39)。

工具链专用警告：通过指针删除析构函数非虚的对象（Non-virtual Destructor）。

<a id="r_ga64d8f26c21ee3639e82d93783e09387e"></a>

```c
#define TOOLCHAIN_WARNING_EXTRA
```

相关声明：[TOOLCHAIN_WARNING_EXTRA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga64d8f26c21ee3639e82d93783e09387e)。

工具链专用警告：额外警告（Extra Warnings）。

<a id="r_ga3e95e267a042393b4a1cada284e3244c"></a>

```c
#define TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER
```

相关声明：[TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga3e95e267a042393b4a1cada284e3244c)。

工具链专用警告：启用 VFP 时，Arm 中断服务例程（Interrupt Service Routines）可能破坏 VFP 状态。

<a id="r_gaf990df9b277505b97d4c9c2549fffa9f"></a>

```c
#define TOOLCHAIN_WARNING_NONNULL
```

相关声明：[TOOLCHAIN_WARNING_NONNULL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaf990df9b277505b97d4c9c2549fffa9f)。

工具链专用警告：向标有 nonnull 的函数传递空指针参数（Null Pointer Arguments）。

<a id="r_ga9c83552055a1817801dedc6655fc0cbf"></a>

```c
#define TOOLCHAIN_WARNING_POINTER_ARITH
```

相关声明：[TOOLCHAIN_WARNING_POINTER_ARITH](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga9c83552055a1817801dedc6655fc0cbf)。

工具链专用警告：指针运算（Pointer Arithmetic）。

<a id="r_gae917ae1adad468956fa5d28a50d10670"></a>

```c
#define TOOLCHAIN_WARNING_SHADOW
```

相关声明：[TOOLCHAIN_WARNING_SHADOW](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gae917ae1adad468956fa5d28a50d10670)。

工具链专用警告：遮蔽变量（Shadow Variables）。

<a id="r_ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9"></a>

```c
#define TOOLCHAIN_WARNING_UNUSED_LABEL
```

相关声明：[TOOLCHAIN_WARNING_UNUSED_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9)。

工具链专用警告：未使用标签（Unused Labels）。

<a id="r_gac567335f987f8f89640e22bd8e3e9385"></a>

```c
#define TOOLCHAIN_WARNING_UNUSED_VARIABLE
```

相关声明：[TOOLCHAIN_WARNING_UNUSED_VARIABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gac567335f987f8f89640e22bd8e3e9385)。

工具链专用警告：未使用变量（Unused Variables）。

<a id="r_ga17e576d00c76be3c3eeaddba5907d0ef"></a>

```c
#define TOOLCHAIN_WARNING_ALWAYS_INLINE
```

相关声明：[TOOLCHAIN_WARNING_ALWAYS_INLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga17e576d00c76be3c3eeaddba5907d0ef)。

工具链专用警告：内联函数（Inline Functions）。

<a id="r_ga2db0c0472e8635d69ada180695da4c1c"></a>

```c
#define TOOLCHAIN_WARNING_CAST_QUAL
```

相关声明：[TOOLCHAIN_WARNING_CAST_QUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga2db0c0472e8635d69ada180695da4c1c)。

工具链专用警告：移除类型限定符（Type Qualifier）的指针转换。

<a id="define-members-2"></a>

### 编译器警告控制（Compiler Warning Control）

<a id="r_ga1f08471f8dba6ce2a3e0f38bea73d7b5"></a>

```c
#define TOOLCHAIN_DISABLE_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga1f08471f8dba6ce2a3e0f38bea73d7b5)。

对所有编译器禁用指定编译器警告（Compiler Warning）。

<a id="r_ga5365fdbb6323f48ddca9ab4149e9a561"></a>

```c
#define TOOLCHAIN_ENABLE_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5365fdbb6323f48ddca9ab4149e9a561)。

对所有编译器重新启用指定编译器警告（Compiler Warning）。

<a id="r_gac4bfe24556e3dd2bfb093434a4e98517"></a>

```c
#define TOOLCHAIN_DISABLE_CLANG_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_CLANG_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gac4bfe24556e3dd2bfb093434a4e98517)。

对 Clang 禁用指定编译器警告（Compiler Warning）。

<a id="r_ga35eaaf7a69eae890687c196e81304667"></a>

```c
#define TOOLCHAIN_ENABLE_CLANG_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_CLANG_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga35eaaf7a69eae890687c196e81304667)。

对 Clang 重新启用指定编译器警告（Compiler Warning）。

<a id="r_ga245aa1544cf704ac88da3904e0982f05"></a>

```c
#define TOOLCHAIN_DISABLE_GCC_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_GCC_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga245aa1544cf704ac88da3904e0982f05)。

对 GCC 禁用指定编译器警告（Compiler Warning）。

<a id="r_ga57a000da2786521299f7bc9460977c60"></a>

```c
#define TOOLCHAIN_ENABLE_GCC_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_GCC_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga57a000da2786521299f7bc9460977c60)。

对 GCC 重新启用指定编译器警告（Compiler Warning）。

<a id="r_gaace39dc11f4da885c3a75210519cff13"></a>

```c
#define TOOLCHAIN_DISABLE_IAR_WARNING(warning)
```

相关声明：[TOOLCHAIN_DISABLE_IAR_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaace39dc11f4da885c3a75210519cff13)。

对 IAR 编译器禁用指定编译器警告（Compiler Warning）。

<a id="r_ga8a1fc59f2665be53c4e183d295d91e15"></a>

```c
#define TOOLCHAIN_ENABLE_IAR_WARNING(warning)
```

相关声明：[TOOLCHAIN_ENABLE_IAR_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga8a1fc59f2665be53c4e183d295d91e15)。

对 IAR 编译器重新启用指定编译器警告（Compiler Warning）。


## 25.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [HAS_BUILTIN](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga474a719388efd0578c7c98a0961e23dd)
- [TOOLCHAIN_GCC_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gacbf8a21b471b2086cbe276789c5061d5)
- [TOOLCHAIN_CLANG_VERSION](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gacdbda8f5e81a320dfdbc32bda1b33fad)
- [TOOLCHAIN_HAS_PRAGMA_DIAG](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga763b60a74b3b8917b8a91614f1d443e4)
- [TOOLCHAIN_HAS_C_GENERIC](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga49263980cf39cd330a9e9976dccb4c90)
- [TOOLCHAIN_HAS_C_AUTO_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga9502cad506e0dfb7c3a7b51b5eeb5eeb)
- [TOOLCHAIN_HAS_ZLA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga90e5fd6ed234d1494c7f156635c2e6e1)
- [TOOLCHAIN_PRAGMA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga4bd2473c4ecff861c6bc3e187b0fee12)
- [TOOLCHAIN_WARNING_ADDRESS_OF_PACKED_MEMBER](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaef9c3722dc2b189226eb2e6223c080bf)
- [TOOLCHAIN_WARNING_ARRAY_BOUNDS](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga8b81dbfdc3dde900a58540709a4f1dff)
- [TOOLCHAIN_WARNING_ATTRIBUTES](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5f5fef9bda4762c368f26c9028cdd34a)
- [TOOLCHAIN_WARNING_DELETE_NON_VIRTUAL_DTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga003b55bfd0a8b95a4e57e419eb980a39)
- [TOOLCHAIN_WARNING_EXTRA](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga64d8f26c21ee3639e82d93783e09387e)
- [TOOLCHAIN_WARNING_ARM_INTERRUPT_VFP_CLOBBER](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga3e95e267a042393b4a1cada284e3244c)
- [TOOLCHAIN_WARNING_NONNULL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaf990df9b277505b97d4c9c2549fffa9f)
- [TOOLCHAIN_WARNING_POINTER_ARITH](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga9c83552055a1817801dedc6655fc0cbf)
- [TOOLCHAIN_WARNING_SHADOW](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gae917ae1adad468956fa5d28a50d10670)
- [TOOLCHAIN_WARNING_UNUSED_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga49dfbc1f801e1f3ae9a0dfaee4b1b5c9)
- [TOOLCHAIN_WARNING_UNUSED_VARIABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gac567335f987f8f89640e22bd8e3e9385)
- [TOOLCHAIN_WARNING_ALWAYS_INLINE](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga17e576d00c76be3c3eeaddba5907d0ef)
- [TOOLCHAIN_WARNING_CAST_QUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga2db0c0472e8635d69ada180695da4c1c)
- [TOOLCHAIN_DISABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga1f08471f8dba6ce2a3e0f38bea73d7b5)
- [TOOLCHAIN_ENABLE_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga5365fdbb6323f48ddca9ab4149e9a561)
- [TOOLCHAIN_DISABLE_CLANG_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gac4bfe24556e3dd2bfb093434a4e98517)
- [TOOLCHAIN_ENABLE_CLANG_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga35eaaf7a69eae890687c196e81304667)
- [TOOLCHAIN_DISABLE_GCC_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga245aa1544cf704ac88da3904e0982f05)
- [TOOLCHAIN_ENABLE_GCC_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga57a000da2786521299f7bc9460977c60)
- [TOOLCHAIN_DISABLE_IAR_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#gaace39dc11f4da885c3a75210519cff13)
- [TOOLCHAIN_ENABLE_IAR_WARNING](https://docs.zephyrproject.org/latest/doxygen/html/group__toolchain.html#ga8a1fc59f2665be53c4e183d295d91e15)

<a id="header-details"></a>

---

[上一章](P024_zephyr__stats__stats.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__drivers__usb__uhc.h_文件参考.md)
