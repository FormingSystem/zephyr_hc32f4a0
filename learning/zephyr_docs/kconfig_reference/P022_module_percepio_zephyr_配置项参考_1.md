---
id: learning.zephyr-docs.kconfig-reference.page-22
title: "`<module:percepio>/zephyr`配置项参考（1/2）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第22章\_`<module:percepio>/zephyr`配置项参考（1/2）

本章翻译官方 Kconfig 数据库中 `<module:percepio>/zephyr` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_PERCEPIO_DFM"></a>

## 22.1 `CONFIG_PERCEPIO_DFM`

**提示（Prompt）**：Percepio DevAlert（DFM）支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/Kconfig:12`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`）

<a id="CONFIG_PERCEPIO_DFM_CFG_ADD_TRACE"></a>

## 22.2 `CONFIG_PERCEPIO_DFM_CFG_ADD_TRACE`

**提示（Prompt）**：保存跟踪（Save Trace）

**说明（Help）**

启用后，崩溃捕获器（Crashcatcher）会始终尝试随告警（Alert）保存跟踪（Trace）。请注意，此功能还要求项目包含 Percepio 跟踪记录器（Trace Recorder）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER && CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:226`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER)、[`CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT"></a>

## 22.3 `CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT`

**提示（Prompt）**：云端口（Cloudport）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_SERIAL
CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:23`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 云端口配置（Cloudport Config）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE)、[`CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_SERIAL`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_SERIAL)。

<a id="CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE"></a>

## 22.4 `CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

不通过云端口（Cloudport）发送告警。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:33`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 云端口配置（Cloudport Config） → 云端口（Cloudport）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT)。

<a id="CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_SERIAL"></a>

## 22.5 `CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT_SERIAL`

**提示（Prompt）**：串行端口（Serial）

**说明（Help）**

通过串行端口（Serial Port）发送告警（Alert）和数据块（Chunk），配合串行终端及附带脚本使用。这些脚本对数据进行后处理，使其可在 DevAlert 中使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:27`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 云端口配置（Cloudport Config） → 云端口（Cloudport）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_CLOUDPORT)。

<a id="CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN"></a>

## 22.6 `CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN`

**提示（Prompt）**：保存到保留内存（Retained Memory）

**说明（Help）**

要求已启用并正确配置保留内存（Retained Memory）。更多详情参见入门指南（Getting Started Guide）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:199`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持 → 核心转储策略（Core Dump Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STORE"></a>

## 22.7 `CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STORE`

**提示（Prompt）**：使用所选存储端口（Storageport）保存

**说明（Help）**

核心转储（Core Dump）将通过所选存储端口（Storageport）保存。如果该端口不兼容产生核心转储时的执行上下文（Context），则无法工作。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:205`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持 → 核心转储策略（Core Dump Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY"></a>

## 22.8 `CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STRATEGY`

**提示（Prompt）**：核心转储策略（Core Dump Strategy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN
CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STORE
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:195`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_COREDUMP_RETAIN)、[`CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STORE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_COREDUMP_STORE)。

<a id="CONFIG_PERCEPIO_DFM_CFG_DELAY_BETWEEN_SEND"></a>

## 22.9 `CONFIG_PERCEPIO_DFM_CFG_DELAY_BETWEEN_SEND`

**提示（Prompt）**：发送间隔（Delay between Sends）

**说明（Help）**

在各次传输之间加入延迟（Delay），通常不需要。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:108`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_DESCRIPTION_MAX_LEN"></a>

## 22.10 `CONFIG_PERCEPIO_DFM_CFG_DESCRIPTION_MAX_LEN`

**提示（Prompt）**：描述字符串最大长度（Description String Maximum Length）

**说明（Help）**

描述字符串（Description String）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:102`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_DEVICE_NAME_MAX_LEN"></a>

## 22.11 `CONFIG_PERCEPIO_DFM_CFG_DEVICE_NAME_MAX_LEN`

**提示（Prompt）**：设备名称最大长度（Maximum Device Name Length）

**说明（Help）**

设备名称（Device Name）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:78`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS"></a>

## 22.12 `CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS`

**提示（Prompt）**：启用核心转储（Core Dump）支持

**说明（Help）**

支持向告警（Alert）添加核心转储（Core Dump）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_DEBUG_COREDUMP && CONFIG_DEBUG_COREDUMP_BACKEND_OTHER && CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:186`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务

**配置项引用（Symbol References）**：[`CONFIG_DEBUG_COREDUMP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP)、[`CONFIG_DEBUG_COREDUMP_BACKEND_OTHER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_BACKEND_OTHER)、[`CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_DEBUG_COREDUMP_MEMORY_DUMP_MIN)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_ENABLE_DEBUG_PRINT"></a>

## 22.13 `CONFIG_PERCEPIO_DFM_CFG_ENABLE_DEBUG_PRINT`

**提示（Prompt）**：启用调试消息（Debug Messages）

**说明（Help）**

启用 `DFM_DEBUG( .)` 产生的诊断消息（Diagnostic Messages）。将使用 `DFM_ERROR` 输出调试信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:15`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_FIRMWARE_VERSION"></a>

## 22.14 `CONFIG_PERCEPIO_DFM_CFG_FIRMWARE_VERSION`

**提示（Prompt）**：固件版本（Firmware Version）

**说明（Help）**

固件版本（Firmware Version）。需要设置此值，以区分不同版本产生的告警（Alert）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
"X.Y.Z"
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:3`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_FIRMWARE_VERSION_MAX_LEN"></a>

## 22.15 `CONFIG_PERCEPIO_DFM_CFG_FIRMWARE_VERSION_MAX_LEN`

**提示（Prompt）**：固件版本字符串最大长度（Maximum Firmware Version String Length）

**说明（Help）**

固件版本字符串（Firmware Version String）的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:96`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_MAX_COREDUMP_SIZE"></a>

## 22.16 `CONFIG_PERCEPIO_DFM_CFG_MAX_COREDUMP_SIZE`

**提示（Prompt）**：核心转储大小（Core Dump Size）

**说明（Help）**

核心转储（Core Dump）的最大总大小。由于使用内存缓冲区作为临时工作区，此值会影响内存占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:219`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_MAX_PAYLOADS"></a>

## 22.17 `CONFIG_PERCEPIO_DFM_CFG_MAX_PAYLOADS`

**提示（Prompt）**：最大载荷数（Max Payloads）

**说明（Help）**

单个告警（Alert）可附加的最大载荷（Payload）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:84`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_MAX_PAYLOAD_CHUNK_SIZE"></a>

## 22.18 `CONFIG_PERCEPIO_DFM_CFG_MAX_PAYLOAD_CHUNK_SIZE`

**提示（Prompt）**：最大载荷块大小（Maximum Payload Chunk Size）

**说明（Help）**

要存储或发送的数据块（Chunk）的最大大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:72`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_MAX_SYMPTOMS"></a>

## 22.19 `CONFIG_PERCEPIO_DFM_CFG_MAX_SYMPTOMS`

**提示（Prompt）**：最大症状数（Max Symptoms）

**说明（Help）**

单个告警（Alert）可附加的最大症状（Symptom）数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:90`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 缓冲区设置（Buffer Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_PRODUCTID"></a>

## 22.20 `CONFIG_PERCEPIO_DFM_CFG_PRODUCTID`

**提示（Prompt）**：产品标识（Product ID）

**说明（Help）**

用于识别产品类型（Product Type）的标识符。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:9`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_RETAINED_MEMORY"></a>

## 22.21 `CONFIG_PERCEPIO_DFM_CFG_RETAINED_MEMORY`

**提示（Prompt）**：保留内存（Retained Memory）支持

**说明（Help）**

启用将告警（Alert）临时保存在保留 RAM（Retained RAM）中的能力。当前执行上下文，例如硬故障（Hardfault）上下文，无法使用存储端口（Storageport）时，可使用此功能。重新启动后，可将告警发送到云端口（Cloudport）或保存到存储端口。需要在设备树覆盖文件（Devicetree Overlay）中设置名为 `retention0` 的保留内存区域。根据使用场景，可能需要禁用保护该内存的互斥锁（Mutex），才能写入它，例如从硬故障上下文写入时。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETAINED_MEM && CONFIG_RETENTION && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:173`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务

**配置项引用（Symbol References）**：[`CONFIG_RETAINED_MEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETAINED_MEM)、[`CONFIG_RETENTION`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY"></a>

## 22.22 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY`

**提示（Prompt）**：云端策略（Cloud Strategy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE
CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_OFFLINE
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:139`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_OFFLINE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_OFFLINE)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_OFFLINE"></a>

## 22.23 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_OFFLINE`

**提示（Prompt）**：离线（Offline）

**说明（Help）**

不尝试发送告警／载荷（Alerts/Payloads）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:148`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 云端策略（Cloud Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE"></a>

## 22.24 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY_ONLINE`

**提示（Prompt）**：在线（Online）

**说明（Help）**

尝试发送告警／载荷（Alerts/Payloads）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:143`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 云端策略（Cloud Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_CLOUD_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY"></a>

## 22.25 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY`

**提示（Prompt）**：会话 ID 策略（Session ID Strategy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONSTARTUP
CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:155`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONSTARTUP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONSTARTUP)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT"></a>

## 22.26 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONALERT`

**提示（Prompt）**：告警时（On Alert）

**说明（Help）**

生成告警（Alert）时设置会话 ID（Session ID）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:164`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 会话 ID 策略（Session ID Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONSTARTUP"></a>

## 22.27 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY_ONSTARTUP`

**提示（Prompt）**：启动时（On Startup）

**说明（Help）**

启动时设置会话 ID（Session ID）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:159`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 会话 ID 策略（Session ID Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_SESSIONID_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY"></a>

## 22.28 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY`

**提示（Prompt）**：存储策略（Storage Strategy）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE
CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_OVERWRITE
CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_SKIP
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:118`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_OVERWRITE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_OVERWRITE)、[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_SKIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_SKIP)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE"></a>

## 22.29 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_IGNORE`

**提示（Prompt）**：忽略（Ignore）

**说明（Help）**

从不存储告警／载荷（Alerts/Payloads）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:122`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 存储策略（Storage Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_OVERWRITE"></a>

## 22.30 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_OVERWRITE`

**提示（Prompt）**：覆盖（Overwrite）

**说明（Help）**

Flash 循环缓冲区（FCB）已满时，覆盖旧告警／载荷（Alerts/Payloads）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:127`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 存储策略（Storage Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_SKIP"></a>

## 22.31 `CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY_SKIP`

**提示（Prompt）**：跳过（Skip）

**说明（Help）**

Flash 循环缓冲区（FCB）已满时，不保存新的告警／载荷（Alert/Payload）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:132`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 策略设置（Strategy Settings） → 存储策略（Storage Strategy）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_SELECTED_STORAGE_STRATEGY)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STACKDUMP_SIZE"></a>

## 22.32 `CONFIG_PERCEPIO_DFM_CFG_STACKDUMP_SIZE`

**提示（Prompt）**：栈转储大小（Stack Dump Size）

**说明（Help）**

从栈（Stack）中转储的字节数，相对于当前栈指针（Stack Pointer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
300
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:213`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 启用核心转储（Core Dump）支持

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_ENABLE_COREDUMPS)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT"></a>

## 22.33 `CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT`

**提示（Prompt）**：存储端口（Storageport）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:44`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 存储端口配置（Storageport Config）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)、[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE)、[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH)、[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM"></a>

## 22.34 `CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM`

**提示（Prompt）**：文件系统（Filesystem）

**说明（Help）**

在文件系统中的某个位置存储告警（Alert），使用 Zephyr 文件系统抽象（File System Abstraction）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_FLASH_MAP && CONFIG_FILE_SYSTEM && <choice CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:59`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 存储端口配置（Storageport Config） → 存储端口（Storageport）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FILE_SYSTEM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FILE_SYSTEM)、[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH"></a>

## 22.35 `CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH`

**提示（Prompt）**：通过 Flash 循环缓冲区（FCB）使用 Flash

**说明（Help）**

通过 Zephyr Flash 循环缓冲区（FCB）模块，将告警（Alert）存储到 Flash。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_FLASH && CONFIG_FLASH_MAP && CONFIG_FCB && <choice CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:53`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 存储端口配置（Storageport Config） → 存储端口（Storageport）

**配置项引用（Symbol References）**：[`CONFIG_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_FCB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FCB)、[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE"></a>

## 22.36 `CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_NONE`

**提示（Prompt）**：无（None）

**说明（Help）**

不存储告警（Alerts）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/Kconfig:48`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 存储端口配置（Storageport Config） → 存储端口（Storageport）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FCB_SECTOR_COUNT"></a>

## 22.37 `CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FCB_SECTOR_COUNT`

**提示（Prompt）**：扇区数量（Sector Count）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/storageports/Flash/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → Flash 循环缓冲区配置（FCB Config）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FCB_SECTOR_SIZE"></a>

## 22.38 `CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FCB_SECTOR_SIZE`

**提示（Prompt）**：扇区大小（Sector Size）

**说明（Help）**

指定 `dfm_partition` 中 Flash 循环缓冲区（FCB）使用的扇区大小，应为该分区所在底层 Flash 扇区大小的整数倍；底层扇区大小取决于 Flash 硬件组织。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
0x10000
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/storageports/Flash/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → Flash 循环缓冲区配置（FCB Config）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FLASH)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FILESYSTEM_PATH"></a>

## 22.39 `CONFIG_PERCEPIO_DFM_CFG_STORAGE_PORT_FILESYSTEM_PATH`

**提示（Prompt）**：告警存储路径（Alert Storage Path）

**说明（Help）**

指定 DFM 告警（Alert）的存储位置。DFM 会在初始化时，在指定路径下创建名为 `alerts` 的目录。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM && CONFIG_PERCEPIO_DFM && CONFIG_PERCEPIO_DFM
```

**默认值（Defaults）**

```text
"/dfm"
```

**定义位置（Location）**：`<module:percepio>/zephyr/../DFM/kernelports/Zephyr/storageports/Filesystem/Kconfig:6`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → DevAlert 告警服务 → 文件系统配置（Filesystem Config）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM_CFG_STORAGEPORT_FILESYSTEM)、[`CONFIG_PERCEPIO_DFM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_DFM)。

<a id="CONFIG_PERCEPIO_TRC_CFG_AUTOISR"></a>

## 22.40 `CONFIG_PERCEPIO_TRC_CFG_AUTOISR`

**提示（Prompt）**：自动 ISR 跟踪（Automatic ISR Tracing）

**说明（Help）**

启用后，自动跟踪所有中断服务例程（ISR），无需手动注册，也无需手动添加 `xTraceISRBegin()` / `xTraceISREnd()`。ISR 及其属性取自设备树（Devicetree）。注意，跟踪高频中断可能显著影响实时性能（Real-time Performance）。如需忽略某些 ISR，可使用“IRQ 过滤器（IRQ Filter）”子属性。构建目录中会生成 `AutoISR-v1.1.0.xml`，加载跟踪时需要此文件。若发生 IRQ 编号冲突，将发出警告并使用第一个设备。可定义覆盖文件（Overlay），用 `/delete-property/` 删除多余的 `interrupts` 和 `interrupt-names` 属性来解决冲突。还可在 `zephyr,user` 节点中添加额外 ISR。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY && CONFIG_CPU_CORTEX_M && CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.ISR:35`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 中断服务例程（ISR）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY)、[`CONFIG_CPU_CORTEX_M`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CPU_CORTEX_M)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_AUTOISR_FILTER"></a>

## 22.41 `CONFIG_PERCEPIO_TRC_CFG_AUTOISR_FILTER`

**提示（Prompt）**：IRQ 过滤器（Filter）

**说明（Help）**

启用用户定义函数 `int32_t iTraceIRQFilter(int32_t)`，允许更改传给跟踪记录器（Trace Recorder）的 IRQ 编号。如果返回的编号为负数，该 ISR 将不被跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_AUTOISR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.ISR:60`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 中断服务例程（ISR） → 自动 ISR 跟踪（Automatic ISR Tracing）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_AUTOISR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_AUTOISR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_DELAY"></a>

## 22.42 `CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_DELAY`

**提示（Prompt）**：控制任务延迟（Control Task Delay）

**说明（Help）**

TzCtrl 任务每轮循环之间的延迟，参见 `PERCEPIO_TRC_CFG_CTRL_TASK_PRIORITY`，会影响栈监测（Stack Monitoring）的频率。如果使用 TCP/IP 等利用内部缓冲区的流端口（Stream Port），此值也会影响跟踪数据传输。较短延迟会略微增加 TzCtrl 的 CPU 负载，但可能提高跟踪流传输（Trace Streaming）性能，尤其在跟踪缓冲区较小时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 1000000000]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceControl:17`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪控制任务（Trace Control Task）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_PRIORITY"></a>

## 22.43 `CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_PRIORITY`

**提示（Prompt）**：控制任务优先级（Control Task Priority）

**说明（Help）**

TzCtrl 用于接收 Tracealyzer 的启动／停止命令；在使用 TCP/IP 等采用内部缓冲区的流端口（Stream Port）时，它还负责传输跟踪数据。对于这类流端口，应确保 TzCtrl 优先级（Priority）足够高，能够可靠地周期执行和传输数据，同时又足够低，避免干扰对时序敏感的功能。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 32] if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX
[-32, 32] if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceControl:5`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪控制任务（Trace Control Task）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)。

<a id="CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_STACK_SIZE"></a>

## 22.44 `CONFIG_PERCEPIO_TRC_CFG_CTRL_TASK_STACK_SIZE`

**提示（Prompt）**：控制任务栈大小（Control Task Stack Size）

**说明（Help）**

Tracealyzer 控制任务（Tracealyzer Control，TzCtrl）的栈大小。有关 TzCtrl 的更多信息，参见 `PERCEPIO_TRC_CFG_CTRL_TASK_PRIORITY`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
768 if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS
1024 if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
512
```

**取值范围（Ranges）**

```text
[1, 1048576]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceControl:30`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪控制任务（Trace Control Task）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)。

<a id="CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR"></a>

## 22.45 `CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR`

**提示（Prompt）**：栈监测器（Stack Monitor）

**说明（Help）**

启用（设为 `1`）后，记录器（Recorder）会定期报告所有活动任务未使用的栈空间。栈监测在 Tracealyzer 控制任务 TzCtrl 中运行。流模式（Streaming Mode）下，记录器始终创建此任务；快照模式（Snapshot Mode）下，TzCtrl 仅用于栈监测，只有启用此选项才创建。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**主动选择（Selects）**

```text
CONFIG_TRACING_STACK if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
CONFIG_THREAD_STACK_INFO if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StackMonitor:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_TRACING_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING_STACK)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_THREAD_STACK_INFO`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_STACK_INFO)。

<a id="CONFIG_PERCEPIO_TRC_CFG_ENABLE_TASK_MONITOR"></a>

## 22.46 `CONFIG_PERCEPIO_TRC_CFG_ENABLE_TASK_MONITOR`

**提示（Prompt）**：任务监测器（Task Monitor）

**说明（Help）**

启用（设为 `1`）后，记录器会跟踪通过 `xTraceTaskMonitorRegister()` 注册的所有任务使用的时钟周期（Clock Cycle）。注意，必须在每个任务内部调用 `xTraceTaskMonitorRegister()`，以访问线程局部存储（ThreadLocalStorage）。在用户函数中定期调用 `xTraceTaskMonitorPoll()`，验证自上次检查以来，没有任务使用不可接受比例的时钟周期。如果出现这种情况，会通过回调（Callback）通知应用程序；该回调通过 `xTraceTaskMonitorSetCallback()` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR || CONFIG_THREAD_LOCAL_STORAGE) && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TaskMonitor:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_ENTRY_SYMBOL_MAX_LENGTH"></a>

## 22.47 `CONFIG_PERCEPIO_TRC_CFG_ENTRY_SYMBOL_MAX_LENGTH`

**提示（Prompt）**：符号名称最大长度（Symbol Max Length）

**说明（Help）**

符号名称（Symbol Name）的最大长度，包括任务名称、具名 ISR（`xTraceISRRegister`）、具名内核对象（`xTraceObjectSetNameWithoutHandleandle`）和已注册字符串（`xTraceStringRegister`）。如果使用更长的符号名称，记录器会截断名称，影响跟踪显示。此时负责监测的 TzCtrl 任务会以用户事件（User Event）的形式发出警告。注意，设置得过大也会导致名称通过事件传输时被截断。

译注：`xTraceObjectSetNameWithoutHandleandle` 按本项原文保留；相邻条目使用 `xTraceObjectSetNameWithoutHandle`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
28
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.EntryTable:20`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 条目表（Entry Table）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_ENTRY_TABLE_SLOTS"></a>

## 22.48 `CONFIG_PERCEPIO_TRC_CFG_ENTRY_TABLE_SLOTS`

**提示（Prompt）**：条目表槽位数（Entry Table Slots）

**说明（Help）**

可存储的对象和符号（Objects and Symbols）最大数量，包括任务名称、具名 ISR（`xTraceISRRegister`）、具名内核对象（`xTraceObjectSetNameWithoutHandle`）和已注册字符串（`xTraceRegisterString`）。如果此值过小，部分对象和符号名称无法保存，影响跟踪显示。此时负责监测的 TzCtrl 任务会以用户事件（User Event）的形式发出警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
40
```

**取值范围（Ranges）**

```text
[1, 4194304]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.EntryTable:5`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 条目表（Entry Table）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_BUSY_WAIT"></a>

## 22.49 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_BUSY_WAIT`

**提示（Prompt）**：包含 `k_busy_wait()` 事件（Events）

**说明（Help）**

默认不跟踪 `k_busy_wait()` 事件，因为它们往往非常频繁，跟踪成本较高。启用此选项可将它们加入跟踪（Trace）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:16`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_EVENT_GROUP_EVENTS"></a>

## 22.50 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_EVENT_GROUP_EVENTS`

**提示（Prompt）**：跟踪事件组事件（Event Group Events）

**说明（Help）**

禁用后，跟踪（Trace）将排除所有事件组（Event Group）事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS) && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:75`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_ISR_TRACING"></a>

## 22.51 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_ISR_TRACING`

**提示（Prompt）**：跟踪 ISR 事件（ISR Events）

**说明（Help）**

禁用后，为减小代码体积，将排除记录中断服务例程（Interrupt Service Routine，ISR）的代码，任何 `xTraceISRBegin` / `xTraceISREnd` 调用都会被忽略。但这并不完全禁用 ISR 跟踪：如果 ISR 调用了被跟踪的内核服务，这些事件仍会记录，并在 Tracealyzer 中显示为匿名 ISR 实例，例如名称为 `ISR sending to <queue name>` 的实例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:43`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_MEMMANG_EVENTS"></a>

## 22.52 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_MEMMANG_EVENTS`

**提示（Prompt）**：跟踪内存管理事件（Memory Management Events）

**说明（Help）**

控制是否跟踪 `malloc` 和 `free` 调用。禁用以排除这些调用，启用则将相应事件纳入跟踪（Trace）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:14`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_OSTICK_EVENTS"></a>

## 22.53 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_OSTICK_EVENTS`

**提示（Prompt）**：跟踪操作系统滴答事件（OS Tick Events）

**说明（Help）**

启用后，每当操作系统时钟（OS Clock）增加时都会生成事件。禁用后，不生成 OS 滴答事件（Tick Event），可在相同 RAM 容量下记录更长的跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:66`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_PEND_FUNC_CALL_EVENTS"></a>

## 22.54 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_PEND_FUNC_CALL_EVENTS`

**提示（Prompt）**：跟踪待执行函数事件（Pend Function Events）

**说明（Help）**

禁用后，跟踪将排除所有待执行函数调用（Pending Function Call）事件，例如 `xTimerPendFunctionCall()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS) && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:89`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_READY_EVENTS"></a>

## 22.55 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_READY_EVENTS`

**提示（Prompt）**：跟踪任务就绪事件（Task Ready Events）

**说明（Help）**

启用后，任务进入就绪（Ready）调度状态时会记录事件，使 Tracealyzer 能显示任务进入执行状态之前的初始等待时间，并提供准确的响应时间（Response Time）。禁用后，不生成就绪事件，可在相同 RAM 容量下记录更长的跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:56`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_SCHED_LOCK"></a>

## 22.56 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_SCHED_LOCK`

**提示（Prompt）**：包含 `k_thread_sched_lock()` 和 `unlock()` 事件

**说明（Help）**

设为 `n` 可排除 `k_thread_sched_lock()` 和 `unlock()` 事件，有助于降低事件产生速率（Event Rate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:29`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_STREAM_BUFFER_EVENTS"></a>

## 22.57 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_STREAM_BUFFER_EVENTS`

**提示（Prompt）**：跟踪流缓冲区事件（Stream Buffer Events）

**说明（Help）**

禁用后，跟踪将排除所有流缓冲区（Stream Buffer）或消息缓冲区（Message Buffer）事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS) && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:97`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_TIMER_EVENTS"></a>

## 22.58 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_TIMER_EVENTS`

**提示（Prompt）**：跟踪定时器事件（Timer Events）

**说明（Help）**

禁用后，跟踪将排除所有定时器（Timer）事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS) && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:82`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_USER_EVENTS"></a>

## 22.59 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_USER_EVENTS`

**提示（Prompt）**：跟踪用户事件（User Events）

**说明（Help）**

禁用后，为减小代码体积，将排除所有与用户事件（User Event）相关的代码；此后任何保存用户事件的尝试都会被静默忽略。用户事件由应用程序生成，类似面向跟踪日志的 `printf`，使用 `xTracePrint` 和 `xTracePrintF` 生成，格式化由主机侧的 Tracealyzer 完成。因此，用户事件比控制台 `printf` 快得多，通常可用于时序关键代码。

注意：流模式（Streaming Mode）下，记录器会利用用户事件提供配置错误等情况下的错误消息和警告，以在 Tracealyzer 中显示。禁用用户事件也会禁用这些警告；但仍可通过调用 `xTraceGetLastError`，或在 `prvTraceError` 和 `prvTraceWarning` 中设置断点来捕获它们。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:22`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INCLUDE_YIELD"></a>

## 22.60 `CONFIG_PERCEPIO_TRC_CFG_INCLUDE_YIELD`

**提示（Prompt）**：包含 `k_thread_yield()` 事件（Events）

**说明（Help）**

设为 `n` 可排除 `k_thread_yield()` 事件，有助于降低事件产生速率（Event Rate）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:23`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_SIZE"></a>

## 22.61 `CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_SIZE`

**提示（Prompt）**：数据块大小（Chunk Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK && CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
2048
```

**取值范围（Ranges）**

```text
[4, 10485760]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:32`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_TRANSFER_AGAIN_COUNT_LIMIT"></a>

## 22.62 `CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_TRANSFER_AGAIN_COUNT_LIMIT`

**提示（Prompt）**：立即重传次数上限（Immediate Re-transfer Count Limit）

**说明（Help）**

定义返回 `xTraceTzCtrl()` 之前，最多可以触发多少次立即再次传输（Immediate Re-transfer）。通过立即传输而不等待下一轮 `xTraceTzCtrl()` 循环，可提高吞吐量（Throughput）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK && CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:45`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_TRANSFER_AGAIN_SIZE_LIMIT"></a>

## 22.63 `CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_CHUNK_TRANSFER_AGAIN_SIZE_LIMIT`

**提示（Prompt）**：触发立即重传的传输量阈值（Transfer Size Limit for Immediate Re-transfer）

**说明（Help）**

定义触发立即再次传输（Immediate Re-transfer）所需的已传输字节数。通过立即传输而不等待下一轮 `xTraceTzCtrl()` 循环，可提高吞吐量（Throughput）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK && CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[4, 10485760]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:37`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_SIZE"></a>

## 22.64 `CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_SIZE`

**提示（Prompt）**：内部缓冲区大小（Internal Buffer Size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
10240
```

**取值范围（Ranges）**

```text
[32, 10485760]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:15`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE"></a>

## 22.65 `CONFIG_PERCEPIO_TRC_CFG_INTERNAL_BUFFER_TRANSFER_MODE`

**提示（Prompt）**：内部缓冲区传输模式（Internal Buffer Transfer Mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL
CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.InternalBuffer:20`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 内部缓冲区（Internal Buffer）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_ALL)、[`CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_INTERNAL_EVENT_BUFFER_OPTION_TRANSFER_MODE_CHUNK)。

<a id="CONFIG_PERCEPIO_TRC_CFG_ISR_TAILCHAINING_THRESHOLD"></a>

## 22.66 `CONFIG_PERCEPIO_TRC_CFG_ISR_TAILCHAINING_THRESHOLD`

**提示（Prompt）**：ISR 尾链阈值（ISR Tailchaining Threshold）

**说明（Help）**

跟踪多个 ISR 时，此设置可使直接连续执行的 ISR 之间的上下文切换（Context Switching）也被准确显示。`xTraceISREnd` 通常假定 ISR 返回前一个上下文，即任务或被抢占的 ISR。但如果另一个被跟踪的 ISR 紧接着执行，Tracealyzer 可能错误地在两个 ISR 之间显示前一上下文的一小段片段。使用 `PERCEPIO_TRC_CFG_ISR_TAILCHAINING_THRESHOLD` 可避免此现象，但此阈值必须针对具体配置实测。默认值为 `0`，表示禁用，此时尾链（Tail-chained）ISR 之间可能出现额外的前一上下文片段。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4194304]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.ISR:16`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 中断服务例程（ISR）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_MAX_ISR_NESTING"></a>

## 22.67 `CONFIG_PERCEPIO_TRC_CFG_MAX_ISR_NESTING`

**提示（Prompt）**：最大 ISR 嵌套层数（Max ISR Nesting）

**说明（Help）**

在跟踪多个 ISR 且可能发生中断嵌套（Interrupt Nesting）时，定义记录器可处理的嵌套层数。超过此值时，相应 ISR 不会被跟踪，记录器会记录错误消息。此设置用于分配内部栈（Internal Stack），跟踪此前的执行上下文，每个条目占 4 字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
8
```

**取值范围（Ranges）**

```text
[1, 1048576]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.ISR:5`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 中断服务例程（ISR）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION"></a>

## 22.68 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_BUFFER_ALLOCATION`

**提示（Prompt）**：记录器分配模式（Recorder Allocation Mode）

**说明（Help）**

指定记录器缓冲区（Recorder Buffer）的分配方式，也适用于流模式中使用记录器内部临时缓冲区的端口。取值如下：

- `PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC`：内部静态分配（Static Allocation）。
- `PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC`：在 `xTraceEnable` 中通过 `malloc` 分配。
- `PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM`：使用 `xTraceSetBuffer`。

静态和动态模式分别在编译时、运行时通过 `malloc` 为你完成分配。自定义模式（Custom Mode）允许控制分配方式和位置，详情参见 `PERCEPIO_TRC_ALLOC_CUSTOM_BUFFER` 与 `xTraceSetBuffer()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC
CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC
CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.BufferAllocation:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_STATIC)、[`CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_DYNAMIC)、[`CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_RECORDER_BUFFER_ALLOCATION_CUSTOM)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_DATA_INIT"></a>

## 22.69 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_DATA_INIT`

**提示（Prompt）**：数据初始化（Data Init）

**说明（Help）**

此宏声明记录器数据（Recorder Data）是否应具有初始值。

在某些特殊情况下，被跟踪对象在 `main()` 之前创建，记录器还需要在这之前启动。此时，记录器数据会由 `xTraceInitialize()` 初始化，却可能随后又被初始化值覆盖。如果遇到此问题，请将 `PERCEPIO_TRC_CFG_RECORDER_DATA_INIT` 设为 `0`，然后在创建任何被跟踪对象之前使用以下代码：

```c
extern uint32_t RecorderEnabled;
RecorderEnabled = 0;
xTraceInitialize();
```

时钟正确初始化后，使用 `xTraceEnable(...)` 开始跟踪（Tracing）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.Debug:5`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 调试（Debug）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS"></a>

## 22.70 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`

**提示（Prompt）**：将 `ESP-IDF_FREERTOS` 设为假（False）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:45`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 实时操作系统隐藏设置（RTOS Hidden Settings）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS"></a>

## 22.71 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`

**提示（Prompt）**：将 `FREERTOS` 设为假（False）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:41`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 实时操作系统隐藏设置（RTOS Hidden Settings）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX"></a>

## 22.72 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX`

**提示（Prompt）**：将 `THREADX` 设为假（False）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:49`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 实时操作系统隐藏设置（RTOS Hidden Settings）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR"></a>

## 22.73 `CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`

**提示（Prompt）**：Zephyr

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/Kconfig:37`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 实时操作系统隐藏设置（RTOS Hidden Settings）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY"></a>

## 22.74 `CONFIG_PERCEPIO_TRC_CFG_SCHEDULING_ONLY`

**提示（Prompt）**：仅记录调度事件（Scheduling Events）

**说明（Help）**

启用后，仅记录调度事件（Scheduling Event）；禁用后，记录所有事件，除非通过其他方式过滤。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.TraceCoverage:7`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 跟踪覆盖范围（Trace Coverage）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STACK_MONITOR_MAX_REPORTS"></a>

## 22.75 `CONFIG_PERCEPIO_TRC_CFG_STACK_MONITOR_MAX_REPORTS`

**提示（Prompt）**：栈监测最大报告数（Stack Monitor Max Reports）

**说明（Help）**

定义 Tracealyzer 控制任务（TzCtrl）每次执行时，要分析栈使用情况的任务数量。注意，栈监测（Stack Monitoring）会在各任务之间轮流进行，因此这不会改变哪些任务受监测，而是改变每个任务的栈多久分析一次。可将此设置与 `PERCEPIO_TRC_CFG_CTRL_TASK_DELAY` 结合使用，以调整栈监测频率。这样设计是因为栈分析可能需要一定执行时间。不过，栈分析运行在独立的 TzCtrl 任务中，可将其设为低优先级，从而避免干扰对时序敏感的任务。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StackMonitor:26`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 栈监测器（Stack Monitor）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STACK_MONITOR_MAX_TASKS"></a>

## 22.76 `CONFIG_PERCEPIO_TRC_CFG_STACK_MONITOR_MAX_TASKS`

**提示（Prompt）**：栈监测最大任务数（Stack Monitor Max Tasks）

**说明（Help）**

控制栈监测器（Stack Monitor）可以监测的任务数量。如果此值过小，部分任务将被排除，并显示警告。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
15
```

**取值范围（Ranges）**

```text
[1, 64]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StackMonitor:18`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 栈监测器（Stack Monitor）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_ENABLE_STACK_MONITOR)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_START_MODE"></a>

## 22.77 `CONFIG_PERCEPIO_TRC_CFG_START_MODE`

**提示（Prompt）**：记录器启动模式（Recorder Start Mode）

**说明（Help）**

决定跟踪记录器（Trace Recorder）何时开始跟踪。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST if CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
CONFIG_PERCEPIO_TRC_START_MODE_START if !CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_START_MODE_START
CONFIG_PERCEPIO_TRC_START_MODE_START_AWAIT_HOST
CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST
CONFIG_PERCEPIO_TRC_START_MODE_MANUAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StartMode:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_START_MODE_START_FROM_HOST)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)、[`CONFIG_PERCEPIO_TRC_START_MODE_START`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_START_MODE_START)、[`CONFIG_PERCEPIO_TRC_START_MODE_START_AWAIT_HOST`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_START_MODE_START_AWAIT_HOST)、[`CONFIG_PERCEPIO_TRC_START_MODE_MANUAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_START_MODE_MANUAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT"></a>

## 22.78 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`

**提示（Prompt）**：流端口（StreamPort）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER if !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_UDP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE"></a>

## 22.79 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ESP_IDF_APPTRACE`

**提示（Prompt）**：ESP-IDF 应用跟踪（APPTRACE）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:15`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE"></a>

## 22.80 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE`

**提示（Prompt）**：文件（File）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:38`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM"></a>

## 22.81 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`

**提示（Prompt）**：指令跟踪宏单元（ITM）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(((CONFIG_ARM || CONFIG_ARM64) && CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR) || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS) && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL if CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_INPUT
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:28`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_INPUT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_INPUT)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_INPUT"></a>

## 22.82 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_INPUT`

**提示（Prompt）**：启用命令输入（Command Input）

**说明（Help）**

启用后，可使用调试器脚本（Debugger Script）向跟踪记录器发送启动／停止跟踪命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/ARM_ITM/Kconfig:14`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_PORT"></a>

## 22.83 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM_PORT`

**提示（Prompt）**：ITM 端口（Port）

**说明（Help）**

用于 ITM 软件事件（Software Event）的 ITM 端口。请确保 IDE／调试器配置为同一个通道（Channel）。默认值为 `1`；`0` 通常用于终端输出。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 31]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/ARM_ITM/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ITM)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER"></a>

## 22.84 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER`

**提示（Prompt）**：环形缓冲区（Ring Buffer）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:35`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE"></a>

## 22.85 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE`

**提示（Prompt）**：环形缓冲区模式（Ring Buffer Mode）

**说明（Help）**

将 `PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_MODE` 设为 `PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL` 时，事件保存在环形缓冲区（Ring Buffer）中；缓冲区满后，最旧事件会被覆盖。这样无需保存自启动以来的全部运行记录，就可获取错误等感兴趣状态发生前的最后一批事件。

设为 `PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL` 时，缓冲区满后停止记录。这适合记录某个特定状态之后的事件，例如启动序列（Startup Sequence）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL
CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/RingBuffer/Kconfig:11`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_OVERWRITE_WHEN_FULL)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_RINGBUFFER_MODE_STOP_WHEN_FULL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_SIZE"></a>

## 22.86 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER_SIZE`

**提示（Prompt）**：环形缓冲区大小（Ring Buffer Size）

**说明（Help）**

定义用于保存跟踪事件（Trace Event）的环形缓冲区（Ring Buffer）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
10240
```

**取值范围（Ranges）**

```text
[0, 10485760]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/RingBuffer/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RINGBUFFER)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT"></a>

## 22.87 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`

**提示（Prompt）**：实时传输（RTT）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(((CONFIG_ARM || CONFIG_ARM64) && CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR) || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX || CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS) && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_USE_SEGGER_RTT if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:20`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_ARM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM)、[`CONFIG_ARM64`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ARM64)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_THREADX)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_USE_SEGGER_RTT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USE_SEGGER_RTT)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_DOWN_BUFFER_INDEX"></a>

## 22.88 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_DOWN_BUFFER_INDEX`

**提示（Prompt）**：RTT 下行缓冲区索引（Down Buffer Index）

**说明（Help）**

定义用于读取跟踪数据（Trace Data）的 RTT 缓冲区。请确保 PC 应用程序中的设置一致，位置为文件→设置（File→Settings）。默认值为 `1`。不建议使用 RTT 缓冲区 `0`，因为它主要供终端使用。如果要使用缓冲区 `0`，必须在 `SEGGER_RTT_Conf.h` 中配置。

译注：本项原文使用“读取跟踪数据”；相邻的下行大小选项将下行方向定义为主机到目标，用于读取命令。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 32]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:46`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_DOWN_BUFFER_SIZE"></a>

## 22.89 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_DOWN_BUFFER_SIZE`

**提示（Prompt）**：RTT 下行缓冲区大小（Down Buffer Size）

**说明（Help）**

定义用于从 Tracealyzer 读取命令的下行 RTT 缓冲区（Down RTT Buffer，主机→目标）大小，适用于 RTT 缓冲区 `1` 或更高编号。Tracealyzer 默认缓冲区大小为 32 字节。此设置对缓冲区 `0` 无效：它无法在运行时重新配置，固定使用 `SEGGER_RTT_Conf.h` 中的定义。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[0, 1048576]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:20`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE"></a>

## 22.90 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE`

**提示（Prompt）**：RTT 阻塞模式（Blocking Mode）

**说明（Help）**

此用于 J-Link 流传输（Streaming）的流端口依赖 SEGGER RTT，后者包含一个由 J-Link 探针在执行期间读取的内部 RAM 缓冲区。可选值为：

- `PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL`。
- `PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP`，默认值。

使用 `PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL` 可确保获得完整有效的跟踪，但如果流传输接口速度不够，可能引起阻塞，干扰实时行为（Real-time Behavior）。因此建议使用 `PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP`。此模式下，如果传输不够快，Tracealyzer 会报告事件丢失；此时可尝试增大上行缓冲区（Up Buffer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP
```

**可选项（Choices）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:59`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL"></a>

## 22.91 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_BLOCK_IF_FIFO_FULL`

**提示（Prompt）**：阻塞（Block）：等待缓冲区出现可用空间。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:81`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → RTT 阻塞模式（Blocking Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP"></a>

## 22.92 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE_NO_BLOCK_SKIP`

**提示（Prompt）**：跳过（Skip）：不阻塞，也不输出。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE>
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:78`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → RTT 阻塞模式（Blocking Mode）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_MODE)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_NO_LOCK_WRITE"></a>

## 22.93 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_NO_LOCK_WRITE`

**提示（Prompt）**：无锁写入（No Lock Write）

**说明（Help）**

设置写入 RTT 数据时是否不加锁（Without Locking）。通常应禁用；Zephyr 是例外，因为在 Zephyr 中 SEGGER RTT 的锁没有必要，启用反而会引起问题。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
y if CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:85`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_UP_BUFFER_INDEX"></a>

## 22.94 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_UP_BUFFER_INDEX`

**提示（Prompt）**：RTT 上行缓冲区索引（Up Buffer Index）

**说明（Help）**

定义用于写入跟踪数据（Trace Data）的 RTT 缓冲区。请确保 PC 应用程序中的设置一致，位置为文件→设置（File→Settings）。默认值为 `1`。不建议使用 RTT 缓冲区 `0`，因为它主要供终端使用。如果要使用缓冲区 `0`，必须在 `SEGGER_RTT_Conf.h` 中配置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[0, 32]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:33`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_UP_BUFFER_SIZE"></a>

## 22.95 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT_UP_BUFFER_SIZE`

**提示（Prompt）**：RTT 上行缓冲区大小（Up Buffer Size）

**说明（Help）**

定义用于写入跟踪数据的上行 RTT 缓冲区（Up RTT Buffer，目标→主机）大小，适用于 RTT 缓冲区 `1` 或更高编号。此设置对缓冲区 `0` 无效：它无法在运行时重新配置，固定使用 `SEGGER_RTT_Conf.h` 中的定义。Tracealyzer 默认缓冲区大小为 5000 字节。如果使用独立 J-Link 探针，可减小到约 1 KB；集成式 J-Link OB 接口速度较慢，根据产生的数据量，需要约 5～10 KB。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[0, 1048576]
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/Jlink_RTT/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_RTT)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_SEMIHOST_TRACE_FILE"></a>

## 22.96 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_SEMIHOST_TRACE_FILE`

**提示（Prompt）**：跟踪文件路径（Trace File Path）

**说明（Help）**

Tracealyzer 跟踪文件（`.psf`）的保存路径，最大长度为 12 个字符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
"./trace.psf"
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../kernelports/Zephyr/streamports/Semihost/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_ZEPHYR_SEMIHOST)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC"></a>

## 22.97 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_STM32_USB_CDC`

**提示（Prompt）**：STM32 USB 通信设备类（CDC）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && !CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:53`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ESPIDF_FREERTOS)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP"></a>

## 22.98 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP`

**提示（Prompt）**：TCP/IP 协议栈

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR && <choice CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT>
```

**主动选择（Selects）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER
CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/Kconfig.StreamPort:41`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings） → 流端口（StreamPort）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_RECORDER_RTOS_ZEPHYR)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT)、[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_USE_INTERNAL_BUFFER)、[`CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL`](P023_module_percepio_zephyr_配置项参考_2.md#CONFIG_PERCEPIO_TRC_STREAM_PORT_BIDIRECTIONAL)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP_PORT"></a>

## 22.99 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP_PORT`

**提示（Prompt）**：TCP 端口（Port）

**说明（Help）**

设置用于跟踪数据传输（Trace Data Transfer）的 TCP 端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
18419
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/TCPIP/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TCPIP)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<a id="CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TRACE_FILE"></a>

## 22.100 `CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_TRACE_FILE`

**提示（Prompt）**：跟踪文件路径（Trace File Path）

**说明（Help）**

Tracealyzer 跟踪文件（`.psf`）的保存路径，最大长度为 12 个字符。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE && CONFIG_TRACING && CONFIG_PERCEPIO_TRACERECORDER && CONFIG_PERCEPIO_TRACERECORDER
```

**默认值（Defaults）**

```text
"./trace.psf"
```

**定义位置（Location）**：`<module:percepio>/zephyr/../TraceRecorder/kernelports/Zephyr/../../config/Kconfig/../../streamports/File/Kconfig:4`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `percepio`（Percepio 调试模块；工作区相对路径 `modules/debug/percepio`） → 跟踪记录器（TraceRecorder） → 流端口设置（StreamPort Settings）

**配置项引用（Symbol References）**：[`CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE`](P022_module_percepio_zephyr_配置项参考_1.md#CONFIG_PERCEPIO_TRC_CFG_STREAM_PORT_FILE)、[`CONFIG_TRACING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TRACING)、[`CONFIG_PERCEPIO_TRACERECORDER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PERCEPIO_TRACERECORDER)。

<!-- kconfig-navigation -->

[上一章](P021_module_lvgl_zephyr_配置项参考_7.md) · [返回大纲](大纲.md) · [下一章](P023_module_percepio_zephyr_配置项参考_2.md)
