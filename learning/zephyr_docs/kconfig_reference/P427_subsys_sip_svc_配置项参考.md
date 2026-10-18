---
id: learning.zephyr-docs.kconfig-reference.page-427
title: "`subsys/sip_svc`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第427章\_`subsys/sip_svc`配置项参考

本章翻译官方 Kconfig 数据库中 `subsys/sip_svc` 的 10 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS"></a>

## 427.1 `CONFIG_ARM_SIP_SVC_SUBSYS`

**提示（Prompt）**：ARM SiP SVC 服务（Service）

**说明（Help）**

通过 SiP SVC 驱动实现平台相关部分，让 Zephyr 能够与原文所称的“较低异常级（Lower exception levels）”通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_HAS_DRIVER
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_HAS_DRIVER`](P170_drivers_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_HAS_DRIVER)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_ASYNC_POLLING_DELAY"></a>

## 427.2 `CONFIG_ARM_SIP_SVC_SUBSYS_ASYNC_POLLING_DELAY`

**提示（Prompt）**：异步任务轮询延迟（Polling delay，微秒）

**说明（Help）**

`sip_svc` 线程每次轮询异步（ASYNC）响应时的休眠延迟。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_INIT_PRIORITY"></a>

## 427.3 `CONFIG_ARM_SIP_SVC_SUBSYS_INIT_PRIORITY`

**提示（Prompt）**：ARM SiP 服务初始化函数优先级（Initialization priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
55
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_MAX_CLIENT_COUNT"></a>

## 427.4 `CONFIG_ARM_SIP_SVC_SUBSYS_MAX_CLIENT_COUNT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个控制器的 `sip_svc` 子系统内客户端（Client）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_MAX_TRANSACTION_ID_COUNT"></a>

## 427.5 `CONFIG_ARM_SIP_SVC_SUBSYS_MAX_TRANSACTION_ID_COUNT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

每个客户端可用的事务 ID（`transaction_id`）最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_MSGQ_DEPTH"></a>

## 427.6 `CONFIG_ARM_SIP_SVC_SUBSYS_MSGQ_DEPTH`

**提示（Prompt）**：ARM SiP 服务请求消息队列深度（Message queue depth）

**说明（Help）**

`sip_svc` 控制器内部消息队列（`msgq`）的深度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_SHELL"></a>

## 427.7 `CONFIG_ARM_SIP_SVC_SUBSYS_SHELL`

**提示（Prompt）**：ARM SiP SVC 服务命令行（Service shell）

**说明（Help）**

启用 ARM SiP SVC 服务命令行（Shell），通过安全监控调用（SMC）或虚拟机监控器调用（HVC）与 EL3/EL2 异常级通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_ARM_SIP_SVC_SUBSYS
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:69`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L69)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](P424_subsys_shell_配置项参考_1.md#CONFIG_SHELL)、[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_SINGLY_OPEN"></a>

## 427.8 `CONFIG_ARM_SIP_SVC_SUBSYS_SINGLY_OPEN`

**提示（Prompt）**：同一时间仅允许一个客户端打开连接（Connection）

**说明（Help）**

每个控制器只允许一个客户端打开会话（Session）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_THREAD_PRIORITY"></a>

## 427.9 `CONFIG_ARM_SIP_SVC_SUBSYS_THREAD_PRIORITY`

**提示（Prompt）**：ARM SiP 服务线程优先级（Thread priority）

**说明（Help）**

ARM SiP 服务的线程优先级。操作完成后，该线程调用请求方的回调（Callback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<a id="CONFIG_ARM_SIP_SVC_SUBSYS_THREAD_STACK_SIZE"></a>

## 427.10 `CONFIG_ARM_SIP_SVC_SUBSYS_THREAD_STACK_SIZE`

**提示（Prompt）**：ARM SiP 服务线程栈大小（Thread stack size）

**说明（Help）**

ARM SiP 服务的线程栈大小。操作完成后，该线程调用请求方的回调（Callback）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_ARM_SIP_SVC_SUBSYS
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`subsys/sip_svc/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/sip_svc/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → ARM SiP SVC 服务（Service）

**配置项引用（Symbol References）**：[`CONFIG_ARM_SIP_SVC_SUBSYS`](P427_subsys_sip_svc_配置项参考.md#CONFIG_ARM_SIP_SVC_SUBSYS)。

<!-- kconfig-navigation -->

[上一章](P426_subsys_shell_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P428_subsys_stats_配置项参考.md)
