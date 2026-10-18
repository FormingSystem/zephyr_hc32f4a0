---
id: learning.zephyr-docs.kconfig-reference.page-25
title: "`<module:xenlib>/Kconfig`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第25章\_`<module:xenlib>/Kconfig`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:xenlib>/Kconfig` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DOMU_MAX"></a>

## 25.1 `CONFIG_DOMU_MAX`

**提示（Prompt）**：DomU 最大数量（Maximum Number of DomUs）

**说明（Help）**

可创建并启动的非特权域（DomU）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 32]
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:122`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_PARTIAL_DEVICE_TREE_SIZE"></a>

## 25.2 `CONFIG_PARTIAL_DEVICE_TREE_SIZE`

**提示（Prompt）**：域设备树大小（Domain Device Tree Size）

**说明（Help）**

域设备树（Domain Device Tree）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
8192
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_PFN_CHUNK_SIZE"></a>

## 25.3 `CONFIG_PFN_CHUNK_SIZE`

**提示（Prompt）**：内存映射操作的数据块大小（Chunk Size）

**说明（Help）**

将客户域（Guest Domain）内存映射到 Dom0 或取消该映射的辅助函数所使用的数据块大小（Chunk Size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:115`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_VCH_PATH_MAXLEN"></a>

## 25.4 `CONFIG_VCH_PATH_MAXLEN`

**提示（Prompt）**：从 XenStore 读取的虚拟通道 ID 最大长度（Maximum Vchannel ID Length）

**说明（Help）**

用于标识单个虚拟通道（Vchannel）的 XenStore 路径最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:109`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XENSTORE_SHELL_READ_SIZE"></a>

## 25.5 `CONFIG_XENSTORE_SHELL_READ_SIZE`

**提示（Prompt）**：`xs` 读取缓冲区大小（Read Buffer Size）

**说明（Help）**

设置 `xs read` 命令可处理的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_SHELL && CONFIG_XEN
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:89`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 Xen 命令行命令（Shell Commands）

**配置项引用（Symbol References）**：[`CONFIG_XEN_SHELL`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_SHELL)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XENSTORE_TREE_TRAVERSE_DEPTH"></a>

## 25.6 `CONFIG_XENSTORE_TREE_TRAVERSE_DEPTH`

**提示（Prompt）**：`xs` 最大遍历深度（Maximum Traverse Depth）

**说明（Help）**

设置 `xs` 最大遍历深度（Traverse Depth），避免 XenStore（XS）树嵌套过深时发生栈溢出（Stack Overflow）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:96`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_CONSOLE_SRV"></a>

## 25.7 `CONFIG_XEN_CONSOLE_SRV`

**提示（Prompt）**：启用 Xen 控制台服务器（Console Server）

**说明（Help）**

启用 Xen 控制台服务器（Console Server）。如果将 Zephyr 作为特权域 Dom0 运行，应包含此服务器，否则任何使用 Xen 半虚拟化控制台（Para-virtual Console，PVC）的 DomU 都可能卡死。反之，如果确定 DomU 永远不会访问 PV 控制台，则可省略此服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:74`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_DOM0LESS_BOOT"></a>

## 25.8 `CONFIG_XEN_DOM0LESS_BOOT`

**提示（Prompt）**：Xen 无 Dom0 启动（Dom0less Boot）支持［实验性］

**说明（Help）**

启用 Xen 无 Dom0 启动（Dom0less Boot）支持。将识别由 Xen 启动的域（Domain），将其加入 xenlib 域管理子系统，并为每个域初始化 XenStore。此功能属于实验性（Experimental），依赖 Xen 主线开发工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:141`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_DOMAIN_MANAGEMENT"></a>

## 25.9 `CONFIG_XEN_DOMAIN_MANAGEMENT`

**提示（Prompt）**：启用 Xen 域管理（Domain Management）

**说明（Help）**

启用域管理库（Domain Management Library），用于创建、销毁和管理 Xen 域（Domain）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:40`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_DOMAIN_MANAGEMENT_SHELL_CMDS"></a>

## 25.10 `CONFIG_XEN_DOMAIN_MANAGEMENT_SHELL_CMDS`

**提示（Prompt）**：启用 Xen 域管理命令行（Domain Management Shell）

**说明（Help）**

启用 Xen 域管理（Domain Management）的命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_XEN_DOMAIN_MANAGEMENT && CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:46`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 Xen 域管理（Domain Management）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_XEN_DOMAIN_MANAGEMENT`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_DOMAIN_MANAGEMENT)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_DOMCFG_READ_PDT"></a>

## 25.11 `CONFIG_XEN_DOMCFG_READ_PDT`

**提示（Prompt）**：启用域局部设备树（Partial Device-tree，PDT）二进制文件读取

**说明（Help）**

通过 `struct xen_domain_cfg` 中的回调（Callback）启用域局部设备树（Partial Device-tree，PDT）二进制文件读取。也会在 `xu create` 命令行命令中启用此功能，该命令将尝试使用 `struct xen_domain_cfg` 回调加载 PDT 二进制文件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_DOMAIN_MANAGEMENT && CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:64`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 Xen 域管理（Domain Management）

**配置项引用（Symbol References）**：[`CONFIG_XEN_DOMAIN_MANAGEMENT`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_DOMAIN_MANAGEMENT)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_DOMCFG_SECTION"></a>

## 25.12 `CONFIG_XEN_DOMCFG_SECTION`

**提示（Prompt）**：启用 Xen 域配置段（Domain Config Section）

**说明（Help）**

启用将域配置（Domain Configuration）集中到公共段（Common Section）的功能。这样可使用 `DECL_CONFIG` 宏声明多个域配置，随后按名称访问它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN_DOMAIN_MANAGEMENT && CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:54`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 Xen 域管理（Domain Management）

**配置项引用（Symbol References）**：[`CONFIG_XEN_DOMAIN_MANAGEMENT`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_DOMAIN_MANAGEMENT)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_LIBFDT"></a>

## 25.13 `CONFIG_XEN_LIBFDT`

**提示（Prompt）**：启用 libfdt 支持（Support）

**说明（Help）**

启用 libfdt 模块（Module），可根据域配置（Domain Config）中的参数生成域设备树（Domain Device Tree），并提供操作扁平设备树（Flattened Device Tree）的完整工具集。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:26`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_SHELL"></a>

## 25.14 `CONFIG_XEN_SHELL`

**提示（Prompt）**：启用 Xen 命令行命令（Shell Commands）

**说明（Help）**

启用用于域管理（Domain Management）的一组 Xen 命令行命令（Shell Commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**主动选择（Selects）**

```text
CONFIG_SHELL
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:83`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_XEN_STORE_COMMON"></a>

## 25.15 `CONFIG_XEN_STORE_COMMON`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

处理 XenStore 的公共代码（Common Code）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**被选择（Selected by）**

```text
CONFIG_XEN_STORE_SRV
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)、[`CONFIG_XEN_STORE_SRV`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_STORE_SRV)。

<a id="CONFIG_XEN_STORE_SRV"></a>

## 25.16 `CONFIG_XEN_STORE_SRV`

**提示（Prompt）**：启用 XenStore 服务器（Server）

**说明（Help）**

启用 XenStore 服务器库（Server Library）。如果将 Zephyr 作为 Dom0 运行，应包含此库。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**主动选择（Selects）**

```text
CONFIG_XEN_STORE_COMMON
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:11`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)、[`CONFIG_XEN_STORE_COMMON`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_STORE_COMMON)。

<a id="CONFIG_XEN_STORE_SRV_SHELL_CMDS"></a>

## 25.17 `CONFIG_XEN_STORE_SRV_SHELL_CMDS`

**提示（Prompt）**：启用 XenStore 服务器命令行（Server Shell）

**说明（Help）**

启用 XenStore 服务器的命令行（Shell）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_XEN_STORE_SRV && CONFIG_XEN
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:18`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 XenStore 服务器（Server）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_XEN_STORE_SRV`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XEN_STORE_SRV)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XEN_VCH"></a>

## 25.18 `CONFIG_XEN_VCH`

**提示（Prompt）**：启用 Xen 虚拟通道（Vchannels）支持

**说明（Help）**

启用虚拟通道通信库（Vchannel Communication Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:104`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XSTAT"></a>

## 25.19 `CONFIG_XSTAT`

**提示（Prompt）**：启用 XSTAT 统计支持（Support）

**说明（Help）**

启用 XSTAT 支持，以获取正在运行的域（Domain）的统计信息（Statistic Information）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:129`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`）

**配置项引用（Symbol References）**：[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<a id="CONFIG_XSTAT_SHELL_CMDS"></a>

## 25.20 `CONFIG_XSTAT_SHELL_CMDS`

**提示（Prompt）**：启用 XSTAT 命令行命令（Shell Commands）

**说明（Help）**

启用一组 XSTAT 命令行命令（Shell Commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_XSTAT && CONFIG_SHELL && CONFIG_XEN
```

**定义位置（Location）**：`<module:xenlib>/Kconfig:134`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `xenlib`（Xen 库模块；工作区相对路径 `modules/lib/zephyr-xenlib`） → 启用 XSTAT 统计支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_XSTAT`](P025_module_xenlib_Kconfig_配置项参考.md#CONFIG_XSTAT)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_XEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_XEN)。

<!-- kconfig-navigation -->

[上一章](P024_module_picolibc_zephyr_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P026_arch_Kconfig_配置项参考_1.md)
