---
id: learning.zephyr-docs.kconfig-reference.page-248
title: "`modules/openthread`配置项参考（3/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第248章\_`modules/openthread`配置项参考（3/3）

本章翻译官方 Kconfig 数据库中 `modules/openthread` 的 40 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPENTHREAD_STORE_FRAME_COUNTER_AHEAD"></a>

## 248.1 `CONFIG_OPENTHREAD_STORE_FRAME_COUNTER_AHEAD`

**提示（Prompt）**：OpenThread 帧计数器提前值（frame counter ahead value）

**说明（Help）**

OpenThread 用于持久存储（persistent storage）的值相对于当前帧计数器（frame counter）的提前量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
100000
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SYS_INIT"></a>

## 248.2 `CONFIG_OPENTHREAD_SYS_INIT`

**提示（Prompt）**：在系统初始化期间初始化 OpenThread 协议栈（system initialization）

**说明（Help）**

此选项在系统初始化期间调用 `openthread_init()` 函数，自动初始化 OpenThread。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_L2_OPENTHREAD && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SYS_INIT_PRIORITY"></a>

## 248.3 `CONFIG_OPENTHREAD_SYS_INIT_PRIORITY`

**提示（Prompt）**：OpenThread 系统初始化优先级（system initialization priority）

**说明（Help）**

此选项设置 OpenThread 系统初始化的优先级（priority）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_SYS_INIT && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`modules/openthread/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 在系统初始化期间初始化 OpenThread 协议栈（system initialization）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SYS_INIT`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_SYS_INIT)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TCAT_MULTIRADIO_CAPABILITIES"></a>

## 248.4 `CONFIG_OPENTHREAD_TCAT_MULTIRADIO_CAPABILITIES`

**提示（Prompt）**：OpenThread 多无线电能力（multiradio capability）

**说明（Help）**

OpenThread 多无线电能力（multiradio capability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_BLE_TCAT
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:251`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L251)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_BLE_TCAT`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_BLE_TCAT)。

<a id="CONFIG_OPENTHREAD_TCP_ENABLE"></a>

## 248.5 `CONFIG_OPENTHREAD_TCP_ENABLE`

**提示（Prompt）**：TCP 支持（TCP support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_THREAD_PREEMPTIVE"></a>

## 248.6 `CONFIG_OPENTHREAD_THREAD_PREEMPTIVE`

**提示（Prompt）**：将 OpenThread 线程设为抢占式（preemptive）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_THREAD_PRIORITY"></a>

## 248.7 `CONFIG_OPENTHREAD_THREAD_PRIORITY`

**提示（Prompt）**：OpenThread 线程优先级（thread priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
0 if CONFIG_OPENTHREAD_THREAD_PREEMPTIVE
8
```

**定义位置（Location）**：[`modules/openthread/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_THREAD_PREEMPTIVE`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_PREEMPTIVE)。

<a id="CONFIG_OPENTHREAD_THREAD_STACK_SIZE"></a>

## 248.8 `CONFIG_OPENTHREAD_THREAD_STACK_SIZE`

**提示（Prompt）**：OpenThread 线程栈大小（thread stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
6144 if CONFIG_OPENTHREAD_COMMISSIONER || CONFIG_OPENTHREAD_JOINER
6240 if (CONFIG_OPENTHREAD_COMMISSIONER || CONFIG_OPENTHREAD_JOINER) && CONFIG_MPU_STACK_GUARD && CONFIG_FPU_SHARING && CONFIG_CPU_CORTEX_M
3168 if CONFIG_MPU_STACK_GUARD && CONFIG_FPU_SHARING && CONFIG_CPU_CORTEX_M
3072
```

**定义位置（Location）**：[`modules/openthread/Kconfig:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_COMMISSIONER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COMMISSIONER)、[`CONFIG_OPENTHREAD_JOINER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_JOINER)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)。

<a id="CONFIG_OPENTHREAD_THREAD_VERSION_1_1"></a>

## 248.9 `CONFIG_OPENTHREAD_THREAD_VERSION_1_1`

**提示（Prompt）**：版本 1.1（Version 1.1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_STACK_VERSION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:12`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L12)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 协议栈版本（stack version）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_STACK_VERSION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_STACK_VERSION)。

<a id="CONFIG_OPENTHREAD_THREAD_VERSION_1_2"></a>

## 248.10 `CONFIG_OPENTHREAD_THREAD_VERSION_1_2`

**提示（Prompt）**：版本 1.2（Version 1.2）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_STACK_VERSION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 协议栈版本（stack version）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_STACK_VERSION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_STACK_VERSION)。

<a id="CONFIG_OPENTHREAD_THREAD_VERSION_1_3"></a>

## 248.11 `CONFIG_OPENTHREAD_THREAD_VERSION_1_3`

**提示（Prompt）**：版本 1.3（Version 1.3）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_STACK_VERSION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 协议栈版本（stack version）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_STACK_VERSION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_STACK_VERSION)。

<a id="CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1"></a>

## 248.12 `CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1`

**提示（Prompt）**：版本 1.3.1（Version 1.3.1）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_STACK_VERSION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 协议栈版本（stack version）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_STACK_VERSION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_STACK_VERSION)。

<a id="CONFIG_OPENTHREAD_THREAD_VERSION_1_4"></a>

## 248.13 `CONFIG_OPENTHREAD_THREAD_VERSION_1_4`

**提示（Prompt）**：版本 1.4（Version 1.4）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_STACK_VERSION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 协议栈版本（stack version）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_STACK_VERSION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_STACK_VERSION)。

<a id="CONFIG_OPENTHREAD_TIME_SYNC"></a>

## 248.14 `CONFIG_OPENTHREAD_TIME_SYNC`

**提示（Prompt）**：时间同步服务功能（time synchronization service feature）［实验性，EXPERIMENTAL］

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_OPENTHREAD_TMF_ADDRESS_CACHE_ENTRIES"></a>

## 248.15 `CONFIG_OPENTHREAD_TMF_ADDRESS_CACHE_ENTRIES`

**提示（Prompt）**：端点标识到路由定位器的缓存条目数（EID-to-RLOC cache entries）

**说明（Help）**

端点标识（EID）到路由定位器（RLOC）的缓存条目数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`modules/openthread/Kconfig:365`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L365)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TMF_ADDRESS_CACHE_MAX_SNOOP_ENTRIES"></a>

## 248.16 `CONFIG_OPENTHREAD_TMF_ADDRESS_CACHE_MAX_SNOOP_ENTRIES`

**提示（Prompt）**：端点标识到路由定位器的缓存条目最大数量（maximum EID-to-RLOC cache entries）

**说明（Help）**

可用于侦听优化（snoop optimization）的端点标识到路由定位器缓存条目（EID-to-RLOC cache entry）的最大数量；此优化会通过检查收到的消息创建条目。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`modules/openthread/Kconfig:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TREL"></a>

## 248.17 `CONFIG_OPENTHREAD_TREL`

**提示（Prompt）**：通过基础设施承载 Thread 功能的 TREL 无线电链路（Thread over Infrastructure）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:426`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L426)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TREL_MANAGE_DNSSD"></a>

## 248.18 `CONFIG_OPENTHREAD_TREL_MANAGE_DNSSD`

**提示（Prompt）**：由 TREL 管理基于 DNS 的服务发现和对等节点发现（DNSSD and peer discovery）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:429`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L429)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TX_BEACON_PAYLOAD"></a>

## 248.19 `CONFIG_OPENTHREAD_TX_BEACON_PAYLOAD`

**提示（Prompt）**：发送信标载荷支持（TX beacon payload support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:432`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L432)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_TX_QUEUE_STATISTICS"></a>

## 248.20 `CONFIG_OPENTHREAD_TX_QUEUE_STATISTICS`

**提示（Prompt）**：发送队列统计支持（TX queue statistics support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:435`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L435)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_UDP_FORWARD"></a>

## 248.21 `CONFIG_OPENTHREAD_UDP_FORWARD`

**提示（Prompt）**：UDP 转发支持（UDP forward support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:438`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L438)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_UPTIME"></a>

## 248.22 `CONFIG_OPENTHREAD_UPTIME`

**提示（Prompt）**：OpenThread 运行时间计数器（uptime counter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_FTD || CONFIG_OPENTHREAD_MTD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:441`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L441)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_FTD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_FTD)、[`CONFIG_OPENTHREAD_MTD`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MTD)。

<a id="CONFIG_OPENTHREAD_VERHOEFF_CHECKSUM"></a>

## 248.23 `CONFIG_OPENTHREAD_VERHOEFF_CHECKSUM`

**提示（Prompt）**：Verhoeff 校验和（Verhoeff checksum）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:445`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L445)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_WAKEUP_COORDINATOR"></a>

## 248.24 `CONFIG_OPENTHREAD_WAKEUP_COORDINATOR`

**提示（Prompt）**：唤醒协调器支持（Wake-up Coordinator support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_CSL_RECEIVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CSL_RECEIVER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CSL_RECEIVER)。

<a id="CONFIG_OPENTHREAD_WAKEUP_END_DEVICE"></a>

## 248.25 `CONFIG_OPENTHREAD_WAKEUP_END_DEVICE`

**提示（Prompt）**：唤醒终端设备支持（Wake-up End Device support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**弱选择（Implies）**

```text
CONFIG_OPENTHREAD_CSL_RECEIVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CSL_RECEIVER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CSL_RECEIVER)。

<a id="CONFIG_OPENTHREAD_XPANID"></a>

## 248.26 `CONFIG_OPENTHREAD_XPANID`

**提示（Prompt）**：默认扩展个域网标识（Default Extended PAN ID）

**说明（Help）**

OpenThread 扩展个域网标识（Extended PAN ID），格式为 `"de:ad:00:be:ef:00:ca:fe"`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"de:ad:00:be:ef:00:ca:fe"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER"></a>

## 248.27 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`

**提示（Prompt）**：添加边界路由器功能支持（Border Router functionality）

**说明（Help）**

使用 OpenThread 的实现启用边界路由器支持（Border Router support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_NET_IPV6_FORWARDING
```

**定义位置（Location）**：[`modules/openthread/Kconfig:453`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L453)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NET_IPV6_FORWARDING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6_FORWARDING)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_BASE_SERVICE_NAME"></a>

## 248.28 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_BASE_SERVICE_NAME`

**提示（Prompt）**：用于派生服务实例名称的基础名称（Base name）

**说明（Help）**

此值表示将在 OpenThread 边界路由器中注册的服务实例名称（service instance name）的一部分。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr-BorderRouter"
```

**定义位置（Location）**：[`modules/openthread/Kconfig:468`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L468)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_DHCP6_PD_SERVICES"></a>

## 248.29 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_DHCP6_PD_SERVICES`

**提示（Prompt）**：在平台代码中注册的可轮询 DHCP6_PD 套接字最大数量（pollable DHCP6_PD sockets）

**说明（Help）**

此配置定义平台 DHCP6_PD 模块使用的可轮询 DHCP6_PD 套接字（pollable socket）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`modules/openthread/Kconfig:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4"></a>

## 248.30 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4`

**提示（Prompt）**：边界路由器具备 IPv4 能力（IPV4 capabilities）

**说明（Help）**

此配置启用 IPv4 通信（IPV4 communication）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_UDP && CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_NET_DHCPV4
```

**定义位置（Location）**：[`modules/openthread/Kconfig:534`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L534)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)、[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NET_DHCPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_DHCPV4)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MAX_MDNS_SERVICES"></a>

## 248.31 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MAX_MDNS_SERVICES`

**提示（Prompt）**：在平台代码中注册的可轮询 mDNS 套接字最大数量（pollable mDNS sockets）

**说明（Help）**

此配置定义平台 mDNS 模块使用的可轮询 mDNS 套接字（pollable socket）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1 if CONFIG_NET_IPV6 && !CONFIG_NET_IPV4
2 if CONFIG_NET_IPV6 && CONFIG_NET_IPV4
```

**定义位置（Location）**：[`modules/openthread/Kconfig:488`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L488)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NET_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IPV4)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MAX_UDP_SERVICES"></a>

## 248.32 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MAX_UDP_SERVICES`

**提示（Prompt）**：在平台代码中注册的可轮询 UDP 套接字最大数量（pollable UDP sockets）

**说明（Help）**

此配置定义平台 UDP 模块使用的可轮询 UDP 套接字（pollable socket）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`modules/openthread/Kconfig:481`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L481)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MDNS_AUTO_NAMING"></a>

## 248.33 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MDNS_AUTO_NAMING`

**提示（Prompt）**：自动生成并注册 OpenThread mDNS 主机名（mDNS hostname）

**说明（Help）**

启用后，OpenThread 边界路由器会代表应用自动生成并注册本地 mDNS 主机名（hostname）。若主机名的生命周期由外部应用层管理，则禁用此选项；例如 Matter 应用会在入网配置过程（commissioning）中分配设备专用主机名。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig:542`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L542)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MDNS_BUFFER_THRESHOLD"></a>

## 248.34 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MDNS_BUFFER_THRESHOLD`

**提示（Prompt）**：决定是否处理 mDNS 数据包的阈值（Threshold value）

**说明（Help）**

此值用于计算 OpenThread mDNS 模块是否应接受传入消息。具体而言，它用于判断：如果接受并处理该 mDNS 数据包，可用的 OpenThread 消息缓冲区（OT message buffer）数量是否会降至某一阈值以下。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`modules/openthread/Kconfig:525`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L525)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MODEL_NAME"></a>

## 248.35 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MODEL_NAME`

**提示（Prompt）**：边界代理产品型号名称（Border Agent product model）

**说明（Help）**

此值表示边界代理的产品型号（Border Agent's product model）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"BorderRouter"
```

**定义位置（Location）**：[`modules/openthread/Kconfig:475`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L475)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MSG_POOL_NUM"></a>

## 248.36 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_MSG_POOL_NUM`

**提示（Prompt）**：骨干网消息池的最大条目数（Maximum entries of backbone message pool）

**说明（Help）**

此值表示来自骨干网接口（backbone interface）、尚未处理时可存储的消息最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`modules/openthread/Kconfig:518`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L518)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_SERVICES"></a>

## 248.37 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_SERVICES`

**提示（Prompt）**：在平台代码中注册的可轮询原始 IPv4 套接字最大数量（pollable RAW IPV4 sockets）

**说明（Help）**

此配置定义平台基础设施接口模块（Infrastructure Interface module）使用的可轮询原始 IPv4 套接字（pollable RAW IPV4 socket）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_NAT64_TRANSLATOR && CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`modules/openthread/Kconfig:510`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L510)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_NAT64_TRANSLATOR`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_NAT64_TRANSLATOR)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR"></a>

## 248.38 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`

**提示（Prompt）**：边界路由器 NAT64 转换器（Border Router NAT64 translator）

**说明（Help）**

此配置启用 OpenThread 提供的 NAT64 转换器（NAT64 translator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4 && CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_NAT64_TRANSLATOR
CONFIG_OPENTHREAD_NAT64_BORDER_ROUTING
CONFIG_NET_PKT_FILTER
CONFIG_NET_PKT_FILTER_IPV4_HOOK
```

**定义位置（Location）**：[`modules/openthread/Kconfig:553`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L553)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_IPV4)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_NAT64_TRANSLATOR`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_NAT64_TRANSLATOR)、[`CONFIG_OPENTHREAD_NAT64_BORDER_ROUTING`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_NAT64_BORDER_ROUTING)、[`CONFIG_NET_PKT_FILTER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_FILTER)、[`CONFIG_NET_PKT_FILTER_IPV4_HOOK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_FILTER_IPV4_HOOK)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_TREL_SERVICES"></a>

## 248.39 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_TREL_SERVICES`

**提示（Prompt）**：在平台代码中注册的可轮询 TREL 套接字最大数量（pollable TREL sockets）

**说明（Help）**

此配置定义平台 TREL 模块使用的可轮询 TREL 套接字（pollable socket）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`modules/openthread/Kconfig:496`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L496)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_VENDOR_NAME"></a>

## 248.40 `CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_VENDOR_NAME`

**提示（Prompt）**：用于派生 mDNS 主机名的基础名称（Base name）

**说明（Help）**

此值表示将在 OpenThread 边界路由器中注册的 mDNS 主机名（mDNS host）的一部分。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr-OTBR"
```

**定义位置（Location）**：[`modules/openthread/Kconfig:461`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L461)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 边界路由器（Border Router） → 添加边界路由器功能支持（Border Router functionality）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<!-- kconfig-navigation -->

[上一章](P247_modules_openthread_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P249_modules_segger_配置项参考.md)
