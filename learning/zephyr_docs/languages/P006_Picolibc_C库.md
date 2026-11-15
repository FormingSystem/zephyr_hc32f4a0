---
id: learning.zephyr-docs.languages.libc-pico
title: Picolibc_C库
kind: reference
status: maintained
domains: [zephyr, languages]
source_url: https://docs.zephyrproject.org/latest/develop/languages/c/picolibc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第6章\_Picolibc_C库

原文：[Picolibc](https://docs.zephyrproject.org/latest/develop/languages/c/picolibc.html)。读取日期：2026-10-12，`latest`。

**Picolibc（面向嵌入式系统的C标准库项目）**以 [C17（ISO/IEC 9899:2018）](https://www.iso.org/standard/74528.html)和 [POSIX 2018（IEEE Std 1003.1-2017）](https://pubs.opengroup.org/onlinepubs/9699919799/functions/printf.html)为目标。**可移植操作系统接口（Portable Operating System Interface，POSIX）**在此规定相关标准库接口行为。

Picolibc 是[外部开源项目](https://github.com/picolibc/picolibc)，以模块形式提供给 Zephyr；**Zephyr软件开发工具包（Software Development Kit，SDK）**也为支持的目标架构提供预编译 `libc.a`。其他工具链，例如 GNU Arm Embedded，同样可使用 Picolibc。

Zephyr 在 [lib/libc/picolibc/](https://github.com/zephyrproject-rtos/zephyr/blob/main/lib/libc/picolibc/) 中实现标准函数所调用的 **API钩子（Application Programming Interface Hook）**，将库内部系统调用转成对应 Zephyr 接口。

## 6.1\_作为模块构建

把 Picolibc 作为 Zephyr 模块构建时，可通过多个配置项调整功能集合，在功能支持与生成代码体积之间取舍。这会增加应用编译时间。

由于 C++ 标准库必须针对所用 C 库编译，使用标准 C++ 库的应用不能使用这里的 Picolibc 模块构建方式。

应用配置中启用 Kconfig 选项 [CONFIG_PICOLIBC_USE_MODULE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_USE_MODULE)，即可选择模块版本。

> 译注：这里两种来源选择的前提，是应用已经选用 Picolibc 作为 C 库。`CONFIG_PICOLIBC_USE_MODULE` 控制它来自模块还是工具链，不是一个可以脱离 C 库选择、单独切换所有运行库的总开关。

更新 Picolibc 模块版本时，Zephyr SDK 随附的 Picolibc 也必须更新为相同版本。

## 6.2\_使用工具链随附版本

从 0.16 版本开始，Zephyr SDK 为各目标架构提供预编译 Picolibc，并随附预编译 `libstdc++`。在应用配置中不启用 `CONFIG_PICOLIBC_USE_MODULE`，可使用工具链版本。

每个 Zephyr 发布版本在使用其[推荐SDK版本](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html#toolchain-zephyr-sdk-compatibility)时，保证工具链 Picolibc 与模块 Picolibc 版本同步。

> 译注：这项保证附带“所用 SDK 是该 Zephyr 版本推荐版本”的条件，不适用于任意混搭。选择模块还是预编译库，与是否安装完整 SDK 或 Minimal SDK 是不同问题。

### 6.2.1\_工具链没有随附Picolibc时

即使工具链没有预编译 Picolibc，也可通过模块从源码构建；上一节的模块限制仍适用。

工具链接入必须启用 Kconfig 支持能力 `PICOLIBC_SUPPORTED`，应用看到的配置形式为 [CONFIG_PICOLIBC_SUPPORTED](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_SUPPORTED)。例如工具链的 Kconfig 文件可添加：

```kconfig
config TOOLCHAIN_<name>_PICOLIBC_SUPPORTED
   def_bool y
   select PICOLIBC_SUPPORTED
```

启用该支持能力后，若工具链未随附 Picolibc，构建系统会自动从模块源码构建。

> 译注：`TOOLCHAIN_<name>_PICOLIBC_SUPPORTED` 是由工具链维护者替换 `<name>` 后定义的能力符号。设置能力标志并不安装编译器，也不意味着任意尚未适配的工具链已能构建库；本页只是给出已适配工具链的接入配置。

## 6.3\_格式化输入输出

Picolibc 支持 [printf()](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html#a6c67912b5a18e7d7ac03ca4e77425715)、[fprintf()](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html#af097ff94eaf1896faa4664dd91858778)、[sprintf()](https://docs.zephyrproject.org/latest/doxygen/html/stdio_8h.html#aa6f061fe9cbedf135d97a91b0f7c0ca8)、`sscanf()` 等标准**格式化输入输出（Formatted Input/Output）**函数。

其实现支持 C17 和 POSIX 2018 规定的格式说明符，但需注意：

- `%f` 等浮点格式需要 Kconfig 选项 [CONFIG_PICOLIBC_IO_FLOAT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_IO_FLOAT)。
- `%lld` 等 `long long` 格式需要 [CONFIG_PICOLIBC_IO_LONG_LONG](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PICOLIBC_IO_LONG_LONG)。启用浮点格式时会自动启用这一选项。

## 6.4\_Zephyr格式化函数的接入

使用 Picolibc 时，以下 Zephyr 格式化函数基于 **标准输入输出（Standard Input/Output，stdio）**调用实现：

- `printk`、`snprintk`、`vsnprintk`。
- `cbprintf`、`cbvprintf`。
- `fprintfcb`、`vfprintfcb`、`printfcb`、`vprintfcb`、`snprintfcb`、`vsnprintfcb`。

但使用**带类型标签的参数（Tagged Arguments）**时，即启用 Kconfig 选项 [CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CBPRINTF_PACKAGE_SUPPORT_TAGGED_ARGUMENTS) 并使用标志 [CBPRINTF_PACKAGE_ARGS_ARE_TAGGED](../cbprintf_reference/P013_格式化包创建标志.md#gaa8edaf31e7acfb7cb113afa873efa126)，`cbpprintf` 调用不会使用 Picolibc。

因此这条路径的输出可能与 Picolibc 不同，因为 cbprintf 系列并非完全符合 C/POSIX 的所有要求。

## 6.5\_数学函数

Picolibc 为 `float`、`double`、`long double` 数学运算提供 C17 与 [IEEE 754-2019](https://ieeexplore.ieee.org/document/8766229)支持，例外是缺少 `long double` 版本的**贝塞尔函数（Bessel Function）**。

## 6.6\_线程局部存储

在支持的平台上，Picolibc 使用**线程局部存储（Thread Local Storage，TLS）**保存应当属于各线程的数据，例如错误状态 [errno](../error_reference/P003_系统错误号公共接口.md#gab03f640d90fbc5bcb75285d08a0f25ed)。因此使用 Picolibc 时会启用 TLS 支持。

这些 TLS 变量从线程栈区域分配，会让栈空间需求增加若干字节。

> 译注：这里 TLS 是线程局部存储，与网络加密协议中的同名缩写不同。实际栈开销取决于所用实现和线程局部对象，不能把“若干字节”当作所有应用的固定预算。

## 6.7\_C库内部变量

Picolibc 有少量用于堆管理等工作的内部变量，集中在专用内存分区 `z_libc_partition`。

使用 Kconfig 选项 [CONFIG_USERSPACE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USERSPACE) 与**内存域（Memory Domain）**的应用，必须确保执行 Picolibc 调用时所在的内存域包含该分区。

> 译注：`z_libc_partition` 保存库内部状态，`z_malloc_partition` 则用于标准动态分配器内存。两者名称相近，但职责不同。

## 6.8\_动态内存管理

Picolibc 使用[C库公共代码](P003_C库公共代码.md)实现的 `malloc` 函数族，其底层是[内核内存堆接口](https://docs.zephyrproject.org/latest/kernel/memory_management/heap.html#heap-v2)。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Newlib_C库](P005_Newlib_C库.md) · [本模块主线目录](../reading/languages.md) · [全部主线](../reading/README.md) · [下一篇：C加加语言支持](P007_C加加语言支持.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：Newlib](P005_Newlib_C库.md) · [下一章：C++语言支持](P007_C加加语言支持.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
