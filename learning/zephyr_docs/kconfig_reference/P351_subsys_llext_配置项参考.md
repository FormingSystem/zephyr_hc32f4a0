---
id: learning.zephyr-docs.kconfig-reference.page-351
title: "`subsys/llext`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第351章\_`subsys/llext`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/llext` 的 45 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LLEXT"></a>

## 351.1 `CONFIG_LLEXT`

**提示（Prompt）**：可链接、可加载扩展（Linkable loadable extensions）

**说明（Help）**

启用可链接可加载扩展子系统（linkable loadable extension subsystem）

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_CACHE_MANAGEMENT if CONFIG_DCACHE
CONFIG_KERNEL_WHOLE_ARCHIVE
```

**定义位置（Location）**：[`subsys/llext/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_CACHE_MANAGEMENT`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_CACHE_MANAGEMENT)、[`CONFIG_DCACHE`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_DCACHE)、[`CONFIG_KERNEL_WHOLE_ARCHIVE`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_WHOLE_ARCHIVE)。

<a id="CONFIG_LLEXT_BINARY_TYPE"></a>

## 351.2 `CONFIG_LLEXT_BINARY_TYPE`

**提示（Prompt）**：llext 二进制目标类型（Binary object type）

**说明（Help）**

llext 目标类型（Object type）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
CONFIG_LLEXT_TYPE_ELF_OBJECT if CONFIG_ARM || CONFIG_ARM64
CONFIG_LLEXT_TYPE_ELF_SHAREDLIB if CONFIG_XTENSA
CONFIG_LLEXT_TYPE_ELF_RELOCATABLE if CONFIG_RISCV
```

**可选项（Choices）**

```text
CONFIG_LLEXT_TYPE_ELF_OBJECT
CONFIG_LLEXT_TYPE_ELF_RELOCATABLE
CONFIG_LLEXT_TYPE_ELF_SHAREDLIB
```

**定义位置（Location）**：[`subsys/llext/Kconfig:13`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L13)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_TYPE_ELF_OBJECT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_TYPE_ELF_OBJECT)、[`CONFIG_ARM`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM)、[`CONFIG_ARM64`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARM64)、[`CONFIG_LLEXT_TYPE_ELF_SHAREDLIB`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_TYPE_ELF_SHAREDLIB)、[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_LLEXT_TYPE_ELF_RELOCATABLE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_TYPE_ELF_RELOCATABLE)、[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)。

<a id="CONFIG_LLEXT_BUILD_PIC"></a>

## 351.3 `CONFIG_LLEXT_BUILD_PIC`

**提示（Prompt）**：构建 LLEXT 时使用 -fPIC

**说明（Help）**

默认使用 `-fno-pic -fno-pie` 编译选项构建 LLEXT。某些平台改用 `-fPIC` 后可受益：大多数内部链接由链接器（linker）在构建时完成。选择 `y` 可利用这一优势。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XTENSA && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
y if CONFIG_LLEXT_TYPE_ELF_SHAREDLIB
```

**定义位置（Location）**：[`subsys/llext/Kconfig:143`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L143)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_XTENSA`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_XTENSA)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_TYPE_ELF_SHAREDLIB`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_TYPE_ELF_SHAREDLIB)。

<a id="CONFIG_LLEXT_CODEGEN_VLIW"></a>

## 351.4 `CONFIG_LLEXT_CODEGEN_VLIW`

**提示（Prompt）**：超长指令字代码生成（VLIW code generation）

**说明（Help）**

允许自定义全局编译器设置，决定是否为所有 LLEXT 模块生成超长指令字（Very Long Instruction Word，VLIW）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
CONFIG_LLEXT_CODEGEN_VLIW_INHERIT
```

**可选项（Choices）**

```text
CONFIG_LLEXT_CODEGEN_VLIW_INHERIT
CONFIG_LLEXT_CODEGEN_VLIW_ENABLED
CONFIG_LLEXT_CODEGEN_VLIW_DISABLED
```

**定义位置（Location）**：[`subsys/llext/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 自定义 LLEXT 编译器选项（compiler options）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_CODEGEN_VLIW_INHERIT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW_INHERIT)、[`CONFIG_LLEXT_CODEGEN_VLIW_ENABLED`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW_ENABLED)、[`CONFIG_LLEXT_CODEGEN_VLIW_DISABLED`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW_DISABLED)。

<a id="CONFIG_LLEXT_CODEGEN_VLIW_DISABLED"></a>

## 351.5 `CONFIG_LLEXT_CODEGEN_VLIW_DISABLED`

**提示（Prompt）**：不生成超长指令字（VLIW）。

**说明（Help）**

自定义全局编译器设置，要求编译器绝不为 LLEXT 模块生成超长指令字（VLIW）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_CODEGEN_VLIW>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:273`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L273)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 自定义 LLEXT 编译器选项（compiler options） → 超长指令字代码生成（VLIW code generation）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_CODEGEN_VLIW`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW)。

<a id="CONFIG_LLEXT_CODEGEN_VLIW_ENABLED"></a>

## 351.6 `CONFIG_LLEXT_CODEGEN_VLIW_ENABLED`

**提示（Prompt）**：生成超长指令字（VLIW）。

**说明（Help）**

自定义全局编译器设置，要求编译器尽可能为 LLEXT 模块生成超长指令字（VLIW）指令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_CODEGEN_VLIW>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 自定义 LLEXT 编译器选项（compiler options） → 超长指令字代码生成（VLIW code generation）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_CODEGEN_VLIW`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW)。

<a id="CONFIG_LLEXT_CODEGEN_VLIW_INHERIT"></a>

## 351.7 `CONFIG_LLEXT_CODEGEN_VLIW_INHERIT`

**提示（Prompt）**：继承设置（Inherit settings）

**说明（Help）**

保留全局编译器的超长指令字（VLIW）设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_CODEGEN_VLIW>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 自定义 LLEXT 编译器选项（compiler options） → 超长指令字代码生成（VLIW code generation）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_CODEGEN_VLIW`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_CODEGEN_VLIW)。

<a id="CONFIG_LLEXT_CUSTOM_HEAP_PLACEMENT"></a>

## 351.8 `CONFIG_LLEXT_CUSTOM_HEAP_PLACEMENT`

**提示（Prompt）**：自定义 llext 堆段位置（heap sections placement）

**说明（Help）**

移除链接器脚本（linker script）对 LLEXT 堆段的默认放置规则，允许用户自行安排各个堆的位置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_DATA_HEAP_SIZE"></a>

## 351.9 `CONFIG_LLEXT_DATA_HEAP_SIZE`

**提示（Prompt）**：llext 数据堆内存大小（千字节，data heap）

**说明（Help）**

可供 llext 使用的数据堆（data heap）大小，单位为千字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LLEXT_HEAP_DYNAMIC && CONFIG_HARVARD && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/llext/Kconfig:136`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L136)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_DYNAMIC`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_DYNAMIC)、[`CONFIG_HARVARD`](P028_arch_arc_配置项参考.md#CONFIG_HARVARD)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EDK"></a>

## 351.10 `CONFIG_LLEXT_EDK`

**提示（Prompt）**：可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK）

**说明（Help）**

为可链接可加载扩展（Linkable Loadable Extension）子系统生成扩展开发包（Extension Development Kit，EDK）。EDK 是包含必要文件和构建设置的归档包，使开发者无需完整 Zephyr 源码树即可构建 Zephyr 扩展。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
y if CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EDK_FORMAT"></a>

## 351.11 `CONFIG_LLEXT_EDK_FORMAT`

**提示（Prompt）**：EDK 压缩及输出格式（compression and output format）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_EDK
```

**默认值（Defaults）**

```text
CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD if CONFIG_LLEXT_EDK_PRESERVE_INPUT_FOLDER
CONFIG_LLEXT_EDK_FORMAT_TAR_XZ
```

**可选项（Choices）**

```text
CONFIG_LLEXT_EDK_FORMAT_TAR_XZ
CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD
CONFIG_LLEXT_EDK_FORMAT_ZIP
```

**定义位置（Location）**：[`subsys/llext/Kconfig:344`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L344)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK)、[`CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD)、[`CONFIG_LLEXT_EDK_PRESERVE_INPUT_FOLDER`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_PRESERVE_INPUT_FOLDER)、[`CONFIG_LLEXT_EDK_FORMAT_TAR_XZ`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT_TAR_XZ)、[`CONFIG_LLEXT_EDK_FORMAT_ZIP`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT_ZIP)。

<a id="CONFIG_LLEXT_EDK_FORMAT_TAR_XZ"></a>

## 351.12 `CONFIG_LLEXT_EDK_FORMAT_TAR_XZ`

**提示（Prompt）**：.tar.xz 格式

**说明（Help）**

对 EDK 文件使用 GNU tar 和 XZ 压缩。压缩率最高，但速度较慢。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_EDK_FORMAT>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:349`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L349)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK） → EDK 压缩及输出格式（compression and output format）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK_FORMAT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT)。

<a id="CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD"></a>

## 351.13 `CONFIG_LLEXT_EDK_FORMAT_TAR_ZSTD`

**提示（Prompt）**：.tar.Z 格式

**说明（Help）**

对 EDK 文件使用 GNU tar 和 Zstd 压缩，比 XZ 快得多，同时仍有较高压缩率。译注：原文选项标题使用 `.tar.Z`，正文指定 Zstd；此处均保留，不自行改写输出扩展名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_EDK_FORMAT>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:355`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L355)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK） → EDK 压缩及输出格式（compression and output format）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK_FORMAT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT)。

<a id="CONFIG_LLEXT_EDK_FORMAT_ZIP"></a>

## 351.14 `CONFIG_LLEXT_EDK_FORMAT_ZIP`

**提示（Prompt）**：.zip 格式

**说明（Help）**

对 EDK 文件使用 Zip 格式和压缩。这是可移植性最好的选项，但压缩效果可能不如 XZ 或 Zstd。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_EDK_FORMAT>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK） → EDK 压缩及输出格式（compression and output format）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK_FORMAT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK_FORMAT)。

<a id="CONFIG_LLEXT_EDK_NAME"></a>

## 351.15 `CONFIG_LLEXT_EDK_NAME`

**提示（Prompt）**：llext 扩展开发包（EDK）的名称

**说明（Help）**

生成 EDK 文件时使用 `<name>`，并根据所选输出格式追加适当的扩展名。此名称经规范化后，还用作 EDK 位置变量的前缀，该变量用于生成的 `Makefile.cflags`。例如，默认名称 `llext-edk` 会生成 `LLEXT_EDK_INSTALL_DIR`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_EDK
```

**默认值（Defaults）**

```text
"llext-edk"
```

**定义位置（Location）**：[`subsys/llext/Kconfig:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK)。

<a id="CONFIG_LLEXT_EDK_PRESERVE_INPUT_FOLDER"></a>

## 351.16 `CONFIG_LLEXT_EDK_PRESERVE_INPUT_FOLDER`

**提示（Prompt）**：不删除 EDK 源文件夹（source folder）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_EDK
```

**定义位置（Location）**：[`subsys/llext/Kconfig:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK)。

<a id="CONFIG_LLEXT_EDK_USERSPACE_ONLY"></a>

## 351.17 `CONFIG_LLEXT_EDK_USERSPACE_ONLY`

**提示（Prompt）**：EDK 的系统调用桩只生成用户空间代码路径（Userspace codepath）

**说明（Help）**

系统调用桩（syscall stubs）可包含判断当前代码运行于用户空间还是内核空间的代码，并据此分派调用。如果 EDK 只供用户空间扩展使用，此选项可使 EDK 调用桩不含分派代码，仅生成用户空间路径。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_EDK
```

**定义位置（Location）**：[`subsys/llext/Kconfig:369`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L369)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接可加载扩展开发包（Linkable loadable Extension Development Kit，EDK）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EDK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EDK)。

<a id="CONFIG_LLEXT_EXPERIMENTAL"></a>

## 351.18 `CONFIG_LLEXT_EXPERIMENTAL`

**提示（Prompt）**：LLEXT 实验性功能（experimental functionality）

**说明（Help）**

包含 LLEXT 的实验性及不稳定功能，这些功能将来极有可能改变。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:246`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L246)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID"></a>

## 351.19 `CONFIG_LLEXT_EXPORT_BUILTINS_BY_SLID`

**提示（Prompt）**：通过符号链接标识符（SLIDs）向 llext 导出内置符号

**说明（Help）**

启用后，通过 `EXPORT_SYMBOL` 从 Zephyr 内核或应用导出的符号，会使用符号链接标识符（Symbol Link Identifiers，SLIDs）与 LLEXT 链接，而不按名称链接。这样可大幅减小体积、加快链接过程，并因二进制中移除了导出符号名称而增强保密性。

不过，这可能使 LLEXT 调试更困难，也无法再使用 `llext_find_sym` 按名称查找内置符号表中的符号。此外，LLEXT 构建后还需要进行后处理（post-processing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:201`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L201)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS"></a>

## 351.20 `CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS`

**提示（Prompt）**：导出默认的 Zephyr 应用符号集（symbol set）

**说明（Help）**

导出默认符号、系统调用（syscall）符号及 C 标准库（libc）符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/llext/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 导出符号组（Exported symbol groups）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EXPORT_DEVICES"></a>

## 351.21 `CONFIG_LLEXT_EXPORT_DEVICES`

**提示（Prompt）**：向 llext 导出所有设备树（DT）设备

**说明（Help）**

启用后，设备树中定义的所有 Zephyr 设备均可由 llext 通过标准 `DT_`／`DEVICE_*` 宏访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**主动选择（Selects）**

```text
CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE
```

**定义位置（Location）**：[`subsys/llext/Kconfig:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE)。

<a id="CONFIG_LLEXT_EXPORT_DEV_IDS_BY_HASH"></a>

## 351.22 `CONFIG_LLEXT_EXPORT_DEV_IDS_BY_HASH`

**提示（Prompt）**：在设备名称中使用设备路径的散列值（hash）

**说明（Help）**

启用后，导出设备的名称由节点路径的散列值（hash）生成，而不是使用序号（ordinal number）。这种标识符在多次重新构建之间保持稳定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE && CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE"></a>

## 351.23 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_DEVICE`

**提示（Prompt）**：导出 Zephyr 设备（devices）

**说明（Help）**

启用后，设备树中定义的所有 Zephyr 设备均可由 llext 通过标准 `DT_`／`DEVICE_*` 宏访问。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**被选择（Selected by）**

```text
CONFIG_LLEXT_EXPORT_DEVICES
```

**定义位置（Location）**：[`subsys/llext/Kconfig:309`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L309)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 导出符号组（Exported symbol groups）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_EXPORT_DEVICES`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_DEVICES)。

<a id="CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_LIBC"></a>

## 351.24 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_LIBC`

**提示（Prompt）**：导出标准库符号（standard library symbols）

**说明（Help）**

导出 `memcpy`、`memset`、`strlen` 等符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
y if CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS
```

**定义位置（Location）**：[`subsys/llext/Kconfig:303`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L303)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 导出符号组（Exported symbol groups）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS)。

<a id="CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_SYSCALL"></a>

## 351.25 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_SYSCALL`

**提示（Prompt）**：导出所有系统调用（syscalls）

**说明（Help）**

导出所有系统调用符号（syscall symbols）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
y if CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS
```

**定义位置（Location）**：[`subsys/llext/Kconfig:297`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L297)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 导出符号组（Exported symbol groups）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS)。

<a id="CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_UNASSIGNED"></a>

## 351.26 `CONFIG_LLEXT_EXPORT_SYMBOL_GROUP_UNASSIGNED`

**提示（Prompt）**：导出 UNASSIGNED 组中的所有符号

**说明（Help）**

导出所有声明时未明确指定分组的符号。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
y if CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS
```

**定义位置（Location）**：[`subsys/llext/Kconfig:291`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L291)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → 导出符号组（Exported symbol groups）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_EXPORT_DEFAULT_GROUPS)。

<a id="CONFIG_LLEXT_EXT_HEAP_SIZE"></a>

## 351.27 `CONFIG_LLEXT_EXT_HEAP_SIZE`

**提示（Prompt）**：llext 扩展堆内存大小（千字节，extension heap）

**说明（Help）**

供 LLEXT 扩展区域使用的堆大小，单位为千字节。必须是 `LLEXT_HEAP_MEMBLK_BLOCK_SIZE` 的整数倍。选择 `HARVARD` 后，由 `LLEXT_INSTR_HEAP_SIZE` 和 `LLEXT_DATA_HEAP_SIZE` 取代。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_HARVARD && CONFIG_LLEXT_HEAP_MEMBLK && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/llext/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_HARVARD`](P028_arch_arc_配置项参考.md#CONFIG_HARVARD)、[`CONFIG_LLEXT_HEAP_MEMBLK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MEMBLK)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_HEAP_DYNAMIC"></a>

## 351.28 `CONFIG_LLEXT_HEAP_DYNAMIC`

**提示（Prompt）**：不分配静态 LLEXT 堆（static heap）

**说明（Help）**

某些应用需要将扩展加载到启动时不存在、无法静态分配的内存中。此项将 LLEXT 堆的分配责任交给应用，不再静态分配。应用必须调用 `llext_heap_init()`，指定用作 LLEXT 堆的缓冲区，否则 LLEXT 模块将无法加载。应用不再需要 LLEXT 功能时，应调用 `llext_heap_uninit()`，将缓冲区控制权交还应用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_HEAP_K_HEAP"></a>

## 351.29 `CONFIG_LLEXT_HEAP_K_HEAP`

**提示（Prompt）**：使用 k_heap

**说明（Help）**

使用 `k_heap` API 管理扩展区域所用的 LLEXT 堆内存。`k_heap` 会在请求分配的空间之后额外分配管理数据（bookkeeping data），略微增加内存开销，并可能导致与内存保护单元（MPU）区域不对齐。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_HEAP_MANAGEMENT>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 堆内存管理（heap memory management）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_MANAGEMENT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MANAGEMENT)。

<a id="CONFIG_LLEXT_HEAP_MANAGEMENT"></a>

## 351.30 `CONFIG_LLEXT_HEAP_MANAGEMENT`

**提示（Prompt）**：llext 堆内存管理（heap memory management）

**说明（Help）**

选择用于在 LLEXT 堆内存中存储扩展区域的内存管理 API。此选择不影响 LLEXT 元数据（metadata），后者始终由 `k_heap` 管理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**默认值（Defaults）**

```text
CONFIG_LLEXT_HEAP_K_HEAP
```

**可选项（Choices）**

```text
CONFIG_LLEXT_HEAP_K_HEAP
CONFIG_LLEXT_HEAP_MEMBLK
```

**定义位置（Location）**：[`subsys/llext/Kconfig:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)、[`CONFIG_LLEXT_HEAP_K_HEAP`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_K_HEAP)、[`CONFIG_LLEXT_HEAP_MEMBLK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MEMBLK)。

<a id="CONFIG_LLEXT_HEAP_MEMBLK"></a>

## 351.31 `CONFIG_LLEXT_HEAP_MEMBLK`

**提示（Prompt）**：使用 sys_mem_blocks

**说明（Help）**

使用 `sys_mem_blocks` API 管理扩展区域所用的 LLEXT 堆内存。每个区域至少分配一个块。必须谨慎选择块大小，以确保扩展区域正确对齐（alignment）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_LLEXT_HEAP_DYNAMIC && <choice CONFIG_LLEXT_HEAP_MANAGEMENT>
```

**主动选择（Selects）**

```text
CONFIG_SYS_MEM_BLOCKS
```

**定义位置（Location）**：[`subsys/llext/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 堆内存管理（heap memory management）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_DYNAMIC`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_DYNAMIC)、[`CONFIG_LLEXT_HEAP_MANAGEMENT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MANAGEMENT)、[`CONFIG_SYS_MEM_BLOCKS`](P199_lib_配置项参考_3.md#CONFIG_SYS_MEM_BLOCKS)。

<a id="CONFIG_LLEXT_HEAP_MEMBLK_BLOCK_SIZE"></a>

## 351.32 `CONFIG_LLEXT_HEAP_MEMBLK_BLOCK_SIZE`

**提示（Prompt）**：llext sys_mem_blocks 块大小（字节）

**说明（Help）**

LLEXT 的 `sys_mem_blocks` 堆所用块大小，单位为字节。启用内存管理单元（MMU）或内存保护单元（MPU）时，必须等于 `LLEXT_PAGE_SIZE` 或为其整数倍；还必须等于任何扩展区域所需的最大对齐大小，或为其整数倍。若选择 `MPU_REQUIRES_POWER_OF_TWO_ALIGNMENT` 且区域较大，为满足对齐要求，可能需要不合理地增大块大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_HEAP_MEMBLK && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/llext/Kconfig:116`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L116)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_MEMBLK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MEMBLK)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_HEAP_SIZE"></a>

## 351.33 `CONFIG_LLEXT_HEAP_SIZE`

**提示（Prompt）**：llext 堆内存大小（千字节，heap memory size）

**说明（Help）**

可供 llext 动态分配使用的堆大小，单位为千字节。选择 `HARVARD` 后，由 `LLEXT_INSTR_HEAP_SIZE` 和 `LLEXT_DATA_HEAP_SIZE` 取代。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LLEXT_HEAP_DYNAMIC && !CONFIG_HARVARD && !CONFIG_LLEXT_HEAP_MEMBLK && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`subsys/llext/Kconfig:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_DYNAMIC`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_DYNAMIC)、[`CONFIG_HARVARD`](P028_arch_arc_配置项参考.md#CONFIG_HARVARD)、[`CONFIG_LLEXT_HEAP_MEMBLK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MEMBLK)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_IMPORT_ALL_GLOBALS"></a>

## 351.34 `CONFIG_LLEXT_IMPORT_ALL_GLOBALS`

**提示（Prompt）**：从扩展导入所有全局符号（global symbols）

**说明（Help）**

加载扩展时，默认只有 `.exported_sym` 段中列出的符号可供 Zephyr 核心使用，这些符号可能通过 `EXPORT_SYMBOL` 声明。启用此项后，主应用可以使用扩展中的所有全局符号。对于未使用完整 Zephyr EDK 编译的基础扩展，这有助于加载和使用它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_INSTR_HEAP_SIZE"></a>

## 351.35 `CONFIG_LLEXT_INSTR_HEAP_SIZE`

**提示（Prompt）**：llext 指令堆内存大小（千字节，instruction heap）

**说明（Help）**

可供 llext 使用的指令堆（instruction heap）大小，单位为千字节。此堆中只放置可执行区域（executable regions）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_LLEXT_HEAP_DYNAMIC && CONFIG_HARVARD && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/llext/Kconfig:128`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L128)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_DYNAMIC`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_DYNAMIC)、[`CONFIG_HARVARD`](P028_arch_arc_配置项参考.md#CONFIG_HARVARD)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_METADATA_HEAP_SIZE"></a>

## 351.36 `CONFIG_LLEXT_METADATA_HEAP_SIZE`

**提示（Prompt）**：llext 元数据堆内存大小（千字节，metadata heap）

**说明（Help）**

可供 LLEXT 元数据（metadata）使用的堆大小，单位为千字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_HEAP_MEMBLK && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/llext/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_HEAP_MEMBLK`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_HEAP_MEMBLK)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_RODATA_NO_RELOC"></a>

## 351.37 `CONFIG_LLEXT_RODATA_NO_RELOC`

**提示（Prompt）**：将不含重定位的只读数据保留在闪存中

**说明（Help）**

启用后，不含任何重定位（relocations）的只读数据段（`.rodata`）会保留在原位置，通常是闪存，而不复制到 RAM。适用于不包含指针的大型常量数据，例如证书、查找表或字符串字面量。扩展必须手动用 `LLEXT_RODATA_NO_RELOC` 宏标记这些数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_MMU && !CONFIG_USERSPACE && CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_MMU`](P001_kernel_配置项参考_1.md#CONFIG_MMU)、[`CONFIG_USERSPACE`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_USERSPACE)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_SEMIHOST_LOADER"></a>

## 351.38 `CONFIG_LLEXT_SEMIHOST_LOADER`

**提示（Prompt）**：扩展的半主机加载器（Semihost loader）

**说明（Help）**

启用后，可通过半主机（semihosting）接口加载扩展，有助于开发和调试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SEMIHOST && CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_SEMIHOST`](P032_arch_common_配置项参考.md#CONFIG_SEMIHOST)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_SHELL"></a>

## 351.39 `CONFIG_LLEXT_SHELL`

**提示（Prompt）**：llext 命令行命令（shell commands）

**说明（Help）**

通过命令行命令（shell commands）管理 llext，包括加载（loading）、卸载（unloading）和内省（introspection）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_SHELL_MAX_SIZE"></a>

## 351.40 `CONFIG_LLEXT_SHELL_MAX_SIZE`

**提示（Prompt）**：llext 最大大小（字节）

**说明（Help）**

通过命令行（shell）加载 llext 时，使用本项指定大小的临时缓冲区存储它。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT_SHELL && CONFIG_LLEXT
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：[`subsys/llext/Kconfig:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 命令行命令（shell commands）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_SHELL`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_SHELL)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_STORAGE_WRITABLE"></a>

## 351.41 `CONFIG_LLEXT_STORAGE_WRITABLE`

**提示（Prompt）**：llext 存储可写（storage is writable）

**说明（Help）**

LLEXT 存储可写时选择本项，例如扩展保存在 RAM 中且可原地修改（modified in place）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

<a id="CONFIG_LLEXT_TYPE_ELF_OBJECT"></a>

## 351.42 `CONFIG_LLEXT_TYPE_ELF_OBJECT`

**提示（Prompt）**：单个目标 ELF 文件（Single object ELF file）

**说明（Help）**

为 llext 子系统构建并使用目标文件（object files）作为二进制目标类型。通过一次编译器调用生成目标文件。当前不支持 RISC-V。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_RISCV && <choice CONFIG_LLEXT_BINARY_TYPE>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 二进制目标类型（Binary object type）

**配置项引用（Symbol References）**：[`CONFIG_RISCV`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_RISCV)、[`CONFIG_LLEXT_BINARY_TYPE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_BINARY_TYPE)。

<a id="CONFIG_LLEXT_TYPE_ELF_RELOCATABLE"></a>

## 351.43 `CONFIG_LLEXT_TYPE_ELF_RELOCATABLE`

**提示（Prompt）**：可重定位 ELF 文件（Relocatable ELF file）

**说明（Help）**

为 llext 子系统构建并使用可重定位、部分链接（partially linked）的文件作为二进制目标类型。链接器将多个目标文件合并为一个，生成这种文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_BINARY_TYPE>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:29`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L29)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 二进制目标类型（Binary object type）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_BINARY_TYPE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_BINARY_TYPE)。

<a id="CONFIG_LLEXT_TYPE_ELF_SHAREDLIB"></a>

## 351.44 `CONFIG_LLEXT_TYPE_ELF_SHAREDLIB`

**提示（Prompt）**：共享库 ELF 文件（Shared library ELF file）

**说明（Help）**

为 llext 子系统构建并使用共享库（shared libraries）作为二进制目标类型。通过通常的链接过程，将多个目标文件生成共享库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LLEXT_BINARY_TYPE>
```

**定义位置（Location）**：[`subsys/llext/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions） → llext 二进制目标类型（Binary object type）

**配置项引用（Symbol References）**：[`CONFIG_LLEXT_BINARY_TYPE`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT_BINARY_TYPE)。

<a id="CONFIG_LLEXT_VENEERS"></a>

## 351.45 `CONFIG_LLEXT_VENEERS`

**提示（Prompt）**：用于超范围重定位的跳板桩（Veneer stubs）

**说明（Help）**

启用后，对于目标超出指令可达范围的分支重定位（branch relocations），体系结构专用的 LLEXT 重定位处理程序会生成跳板桩（veneer stubs）。这样便可将加载到 SRAM 的扩展与闪存中的内核符号链接，而无需 `-mlong-calls`。仅在已知所有外部符号调用均在可达范围内，或已使用 `-mlong-calls` 时，才应禁用本项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_HAS_LLEXT_VENEERS && CONFIG_LLEXT
```

**定义位置（Location）**：[`subsys/llext/Kconfig:227`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/llext/Kconfig#L227)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可链接、可加载扩展（Linkable loadable extensions）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_HAS_LLEXT_VENEERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARCH_HAS_LLEXT_VENEERS)、[`CONFIG_LLEXT`](P351_subsys_llext_配置项参考.md#CONFIG_LLEXT)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_ARCH_HAS_LLEXT_VENEERS`。

<!-- kconfig-navigation -->

[上一章](P350_subsys_kvss_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P352_subsys_logging_配置项参考_1.md)
