---
id: learning.zephyr-docs.kconfig-reference.page-246
title: "`modules/openthread`配置项参考（1/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第246章\_`modules/openthread`配置项参考（1/3）

本章翻译官方 Kconfig 数据库中 `modules/openthread` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPENTHREAD"></a>

## 246.1 `CONFIG_OPENTHREAD`

**提示（Prompt）**：OpenThread 支持（OpenThread Support）

**说明（Help）**

此选项启用 OpenThread 库。

**类型（Type）**：布尔值（Boolean），`bool`。

**主动选择（Selects）**

```text
CONFIG_SETTINGS if CONFIG_FLASH
CONFIG_OPENTHREAD_SETTINGS_RAM if !CONFIG_FLASH
CONFIG_CPP
CONFIG_REBOOT
CONFIG_ENTROPY_GENERATOR
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_OPENTHREAD
```

**弱选择（Implies）**

```text
CONFIG_FLASH
CONFIG_FLASH_MAP
CONFIG_MPU_ALLOW_FLASH_WRITE
```

**定义位置（Location）**：[`modules/openthread/Kconfig:5`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L5)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_OPENTHREAD_SETTINGS_RAM`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SETTINGS_RAM)、[`CONFIG_CPP`](P197_lib_配置项参考_1.md#CONFIG_CPP)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_FLASH_MAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FLASH_MAP)、[`CONFIG_MPU_ALLOW_FLASH_WRITE`](P030_arch_arm_配置项参考_2.md#CONFIG_MPU_ALLOW_FLASH_WRITE)。

<a id="CONFIG_OPENTHREAD_ALARM_COUNTER"></a>

## 246.2 `CONFIG_OPENTHREAD_ALARM_COUNTER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用计数器驱动 API（counter driver API），为平台实现的闹钟（alarm）定时器提供微秒精度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
n && CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_COUNTER
```

**定义位置（Location）**：[`modules/openthread/Kconfig:443`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L443)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_COUNTER`](P068_drivers_counter_配置项参考_1.md#CONFIG_COUNTER)。

<a id="CONFIG_OPENTHREAD_ANYCAST_LOCATOR"></a>

## 246.3 `CONFIG_OPENTHREAD_ANYCAST_LOCATOR`

**提示（Prompt）**：任播定位器支持（Anycast locator support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BACKBONE_ROUTER"></a>

## 246.4 `CONFIG_OPENTHREAD_BACKBONE_ROUTER`

**提示（Prompt）**：骨干路由器功能（Backbone Router functionality）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BACKBONE_ROUTER_DUA_NDPROXYING"></a>

## 246.5 `CONFIG_OPENTHREAD_BACKBONE_ROUTER_DUA_NDPROXYING`

**提示（Prompt）**：骨干路由器的域单播地址邻居发现代理支持（BBR DUA ND Proxy support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BACKBONE_ROUTER_MULTICAST_ROUTING"></a>

## 246.6 `CONFIG_OPENTHREAD_BACKBONE_ROUTER_MULTICAST_ROUTING`

**提示（Prompt）**：骨干路由器的多播路由支持（BBR MR support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BLE_TCAT"></a>

## 246.7 `CONFIG_OPENTHREAD_BLE_TCAT`

**提示（Prompt）**：低功耗蓝牙 TCAT 支持（BLE TCAT support）［实验性，EXPERIMENTAL］

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

**定义位置（Location）**：[`modules/openthread/Kconfig.features:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_OPENTHREAD_BLE_TCAT_RING_BUF_SIZE"></a>

## 246.8 `CONFIG_OPENTHREAD_BLE_TCAT_RING_BUF_SIZE`

**提示（Prompt）**：OpenThread BLE 环形缓冲区大小（ringbuffer size）

**说明（Help）**

OpenThread BLE TCAT 环形缓冲区大小（ringbuffer size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
512
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:264`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L264)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BLE_TCAT_THREAD_STACK_SIZE"></a>

## 246.9 `CONFIG_OPENTHREAD_BLE_TCAT_THREAD_STACK_SIZE`

**提示（Prompt）**：OpenThread 默认 TCAT 栈大小（default TCAT stack size）

**说明（Help）**

OpenThread 默认 TCAT 栈大小（default TCAT stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
5120 if CONFIG_OPENTHREAD_CRYPTO_PSA
4200
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CRYPTO_PSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CRYPTO_PSA)。

<a id="CONFIG_OPENTHREAD_BORDER_AGENT"></a>

## 246.10 `CONFIG_OPENTHREAD_BORDER_AGENT`

**提示（Prompt）**：边界代理支持（Border Agent support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_AGENT_EPHEMERAL_KEY_ENABLE"></a>

## 246.11 `CONFIG_OPENTHREAD_BORDER_AGENT_EPHEMERAL_KEY_ENABLE`

**提示（Prompt）**：边界代理临时 PSKc（Border agent ephemeral PSKc）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:52`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L52)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_AGENT_ID"></a>

## 246.12 `CONFIG_OPENTHREAD_BORDER_AGENT_ID`

**提示（Prompt）**：创建并保存边界代理标识（border agent ID）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_AGENT_MESHCOP_SERVICE"></a>

## 246.13 `CONFIG_OPENTHREAD_BORDER_AGENT_MESHCOP_SERVICE`

**提示（Prompt）**：边界代理 MeshCoP 服务（border agent meshcop service）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_ROUTER"></a>

## 246.14 `CONFIG_OPENTHREAD_BORDER_ROUTER`

**提示（Prompt）**：边界路由器支持（Border Router support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_ROUTING"></a>

## 246.15 `CONFIG_OPENTHREAD_BORDER_ROUTING`

**提示（Prompt）**：边界路由支持（Border routing support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_ROUTING_COUNTERS"></a>

## 246.16 `CONFIG_OPENTHREAD_BORDER_ROUTING_COUNTERS`

**提示（Prompt）**：边界路由计数器支持（Border routing counters support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD"></a>

## 246.17 `CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD`

**提示（Prompt）**：边界路由中的 DHCPv6 前缀委派支持（DHCPv6-PD support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD_CLIENT"></a>

## 246.18 `CONFIG_OPENTHREAD_BORDER_ROUTING_DHCP6_PD_CLIENT`

**提示（Prompt）**：边界路由中的 DHCPv6 前缀委派客户端支持（DHCPv6-PD client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:73`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L73)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHANNEL"></a>

## 246.19 `CONFIG_OPENTHREAD_CHANNEL`

**提示（Prompt）**：默认信道（Default Channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
11
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:10`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L10)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHANNEL_MANAGER"></a>

## 246.20 `CONFIG_OPENTHREAD_CHANNEL_MANAGER`

**提示（Prompt）**：信道管理器支持（Channel manager support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_CHANNEL_MONITOR && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_CHANNEL_MONITOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CHANNEL_MONITOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHANNEL_MANAGER_CSL"></a>

## 246.21 `CONFIG_OPENTHREAD_CHANNEL_MANAGER_CSL`

**提示（Prompt）**：用于协调采样监听信道的信道管理器（Channel manager for CSL channel）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:86`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L86)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHANNEL_MONITOR"></a>

## 246.22 `CONFIG_OPENTHREAD_CHANNEL_MONITOR`

**提示（Prompt）**：信道监视器支持（Channel monitor support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHANNEL_MONITOR_AUTO_START"></a>

## 246.23 `CONFIG_OPENTHREAD_CHANNEL_MONITOR_AUTO_START`

**提示（Prompt）**：随接口启动信道监视器（channel monitor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHILD_SUPERVISION_CHECK_TIMEOUT"></a>

## 246.24 `CONFIG_OPENTHREAD_CHILD_SUPERVISION_CHECK_TIMEOUT`

**提示（Prompt）**：OpenThread 子设备监督检查超时时间，单位为秒（child supervision check timeout）

**说明（Help）**

处于子设备状态（child state）的设备所使用的监督检查超时间隔，单位为秒。设为零可禁用子设备上的监督检查过程（supervision check process）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
190
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:286`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L286)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CHILD_SUPERVISION_INTERVAL"></a>

## 246.25 `CONFIG_OPENTHREAD_CHILD_SUPERVISION_INTERVAL`

**提示（Prompt）**：OpenThread 子设备监督间隔，单位为秒（child supervision interval）

**说明（Help）**

父设备（parent device）使用的监督间隔；若在此间隔内没有向子设备发送数据，则向子设备发送监督消息（supervision message）。设为零可禁用子设备上的监督检查过程。译注：原文此处也写作禁用子设备上的检查，保留其表述。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
129
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CLI_LINK_METRICS_ENH_ACK_VERBOSE"></a>

## 246.26 `CONFIG_OPENTHREAD_CLI_LINK_METRICS_ENH_ACK_VERBOSE`

**提示（Prompt）**：在 CLI 中主动输出增强确认帧中的链路指标数据（Link Metrics data from Enhanced-ACK frames）

**说明（Help）**

启用在命令行接口（CLI）中主动输出增强确认帧（Enhanced-ACK frame）收到的链路指标（Link Metrics）数据。禁用时（默认），内部仍会处理这些数据，并可通过 `linkmetrics show` 查询。启用后会在时序敏感的 MAC 发送完成路径（transmit-done path）内增加 CLI 输出调用；在使用同步／阻塞式 CLI 传输的平台上，这可能破坏休眠终端设备（SED）的快速轮询时序（fast-poll timing）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_LINK_METRICS_INITIATOR && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LINK_METRICS_INITIATOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LINK_METRICS_INITIATOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CLI_MAX_LINE_LENGTH"></a>

## 246.27 `CONFIG_OPENTHREAD_CLI_MAX_LINE_LENGTH`

**提示（Prompt）**：CLI 行的最大大小，单位为字节（maximum CLI line size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
384
```

**取值范围（Ranges）**

```text
[16, 65535]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CLI_TCP_ENABLE"></a>

## 246.28 `CONFIG_OPENTHREAD_CLI_TCP_ENABLE`

**提示（Prompt）**：CLI 工具中的 TCP（TCP in the CLI tool）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_TCP_ENABLE && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_SHELL
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:224`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L224)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → TCP 支持（TCP support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_TCP_ENABLE`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_TCP_ENABLE)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)。

<a id="CONFIG_OPENTHREAD_CLI_VENDOR_EXTENSION"></a>

## 246.29 `CONFIG_OPENTHREAD_CLI_VENDOR_EXTENSION`

**提示（Prompt）**：用于定义并链接 OpenThread CLI 厂商扩展的 CMake 文件路径（vendor extension）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:448`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L448)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COAP"></a>

## 246.30 `CONFIG_OPENTHREAD_COAP`

**提示（Prompt）**：OpenThread CoAP 支持（CoAP support）

**说明（Help）**

通过 OpenThread 协议栈为应用启用受限应用协议 API（CoAP API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COAPS"></a>

## 246.31 `CONFIG_OPENTHREAD_COAPS`

**提示（Prompt）**：安全 CoAP API 支持（Secure CoAP API support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_COAP && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COAP`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COAP)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COAP_BLOCK"></a>

## 246.32 `CONFIG_OPENTHREAD_COAP_BLOCK`

**提示（Prompt）**：CoAP 分块传输选项支持（Block-wise option support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:94`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L94)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COAP_OBSERVE"></a>

## 246.33 `CONFIG_OPENTHREAD_COAP_OBSERVE`

**提示（Prompt）**：CoAP 观察选项支持（Observe option support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COMMISSIONER"></a>

## 246.34 `CONFIG_OPENTHREAD_COMMISSIONER`

**提示（Prompt）**：入网委托方功能支持（Commissioner functions support）

**说明（Help）**

在 OpenThread 协议栈中启用入网委托方能力（commissioner capability）。注意，入网配置过程（commissioning）使用的 DTLS 握手需要比默认值更大的 Mbed TLS 堆（heap）。用于该过程的 `CONFIG_MBEDTLS_HEAP_SIZE` 建议最小值为 10KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:104`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L104)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CONFIG_PLATFORM_INFO"></a>

## 246.35 `CONFIG_OPENTHREAD_CONFIG_PLATFORM_INFO`

**提示（Prompt）**：插入 OpenThread 版本字符串的平台专用字符串（platform-specific string）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR"></a>

## 246.36 `CONFIG_OPENTHREAD_COPROCESSOR`

**提示（Prompt）**：OpenThread 协处理器（Co-Processor）

**说明（Help）**

在 OpenThread 协议栈中启用协处理器（Co-Processor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_MANUAL_START
CONFIG_UART_INTERRUPT_DRIVEN if !CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC
```

**定义位置（Location）**：[`modules/openthread/Kconfig:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_MANUAL_START`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MANUAL_START)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_CHOICE"></a>

## 246.37 `CONFIG_OPENTHREAD_COPROCESSOR_CHOICE`

**提示（Prompt）**：OpenThread 协处理器类型（Co-Processor type）

**说明（Help）**

此选项选择 Thread 网络协处理器类型（network co-processor type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_COPROCESSOR && CONFIG_OPENTHREAD
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_COPROCESSOR_NCP
CONFIG_OPENTHREAD_COPROCESSOR_RCP
CONFIG_OPENTHREAD_COPROCESSOR_NCP
CONFIG_OPENTHREAD_COPROCESSOR_RCP
```

**定义位置（Location）**：[`modules/openthread/Kconfig:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_COPROCESSOR_NCP`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_NCP)、[`CONFIG_OPENTHREAD_COPROCESSOR_RCP`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_RCP)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_NCP"></a>

## 246.38 `CONFIG_OPENTHREAD_COPROCESSOR_NCP`

**提示（Prompt）**：NCP：网络协处理器（Network Co-Processor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_COPROCESSOR_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor） → OpenThread 协处理器类型（Co-Processor type）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_CHOICE)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_RCP"></a>

## 246.39 `CONFIG_OPENTHREAD_COPROCESSOR_RCP`

**提示（Prompt）**：RCP：无线电协处理器（Radio Co-Processor）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_COPROCESSOR_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor） → OpenThread 协处理器类型（Co-Processor type）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_CHOICE)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC"></a>

## 246.40 `CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC`

**提示（Prompt）**：为 OpenThread 协处理器使用异步 UART API（async UART API）

**说明（Help）**

为 OpenThread 协处理器接口启用 Zephyr 异步 UART API（asynchronous UART API）。禁用时改用中断驱动 UART API（interrupt-driven UART API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_OPENTHREAD_COPROCESSOR && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor）

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_ASYNC_API)、[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_UART_RING_BUFFER_SIZE"></a>

## 246.41 `CONFIG_OPENTHREAD_COPROCESSOR_UART_RING_BUFFER_SIZE`

**提示（Prompt）**：设置协处理器 UART 环形缓冲区大小（ring buffer size）

**说明（Help）**

OpenThread 协处理器 UART 的发送缓冲区大小（TX buffer size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_COPROCESSOR && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`modules/openthread/Kconfig:287`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L287)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_UART_RX_BUFFER_SIZE"></a>

## 246.42 `CONFIG_OPENTHREAD_COPROCESSOR_UART_RX_BUFFER_SIZE`

**提示（Prompt）**：设置协处理器 UART 接收缓冲区大小（RX buffer size）

**说明（Help）**

使用异步 UART API 时，OpenThread 协处理器 UART 的接收缓冲区大小（RX buffer size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC && CONFIG_OPENTHREAD_COPROCESSOR && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
256
```

**取值范围（Ranges）**

```text
[0, 4096]
```

**定义位置（Location）**：[`modules/openthread/Kconfig:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L301)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor） → 为 OpenThread 协处理器使用异步 UART API（async UART API）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_UART_ASYNC)、[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_COPROCESSOR_VENDOR_HOOK_SOURCE"></a>

## 246.43 `CONFIG_OPENTHREAD_COPROCESSOR_VENDOR_HOOK_SOURCE`

**提示（Prompt）**：厂商钩子源文件路径（vendor hook source file）

**说明（Help）**

提供用于编译的厂商钩子文件路径（vendor hook file）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_COPROCESSOR && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协处理器（Co-Processor）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CRYPTO_PSA"></a>

## 246.44 `CONFIG_OPENTHREAD_CRYPTO_PSA`

**提示（Prompt）**：平台安全架构密码 API（PSA Crypto API）

**说明（Help）**

使用 PSA Crypto API 作为加密操作的后端（backend），替代传统 Mbed TLS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_PSA_CRYPTO
CONFIG_OPENTHREAD_PLATFORM_KEY_REF
```

**弱选择（Implies）**

```text
CONFIG_OPENTHREAD_PLATFORM_KEYS_EXPORTABLE_ENABLE
```

**定义位置（Location）**：[`modules/openthread/Kconfig:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_OPENTHREAD_PLATFORM_KEY_REF`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_KEY_REF)、[`CONFIG_OPENTHREAD_PLATFORM_KEYS_EXPORTABLE_ENABLE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_KEYS_EXPORTABLE_ENABLE)。

<a id="CONFIG_OPENTHREAD_CSL_AUTO_SYNC"></a>

## 246.45 `CONFIG_OPENTHREAD_CSL_AUTO_SYNC`

**提示（Prompt）**：协调采样监听自动同步（CSL autosync）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_CSL_RECEIVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CSL_RECEIVER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CSL_RECEIVER)。

<a id="CONFIG_OPENTHREAD_CSL_DEBUG"></a>

## 246.46 `CONFIG_OPENTHREAD_CSL_DEBUG`

**提示（Prompt）**：协调采样监听调试（CSL debugging）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:112`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L112)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CSL_RECEIVER"></a>

## 246.47 `CONFIG_OPENTHREAD_CSL_RECEIVER`

**提示（Prompt）**：协调采样监听接收端支持（CSL Receiver support）

**说明（Help）**

启用 Thread 1.2 的协调采样监听接收端支持（CSL Receiver support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_WAKEUP_COORDINATOR
CONFIG_OPENTHREAD_WAKEUP_COORDINATOR
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD_WAKEUP_END_DEVICE
CONFIG_OPENTHREAD_WAKEUP_END_DEVICE
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_WAKEUP_COORDINATOR`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_WAKEUP_COORDINATOR)、[`CONFIG_OPENTHREAD_WAKEUP_END_DEVICE`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_WAKEUP_END_DEVICE)。

<a id="CONFIG_OPENTHREAD_CSL_RECEIVER_LOCAL_TIME_SYNC"></a>

## 246.48 `CONFIG_OPENTHREAD_CSL_RECEIVER_LOCAL_TIME_SYNC`

**提示（Prompt）**：使用本地时间进行 CSL 同步（local time for CSL synchronization）

**说明（Help）**

使用主机时间（host time）而非无线电平台时间，跟踪自上次 CSL 同步以来经过的时间。这会减少无线电 API 的调用次数，适用于调用此类 API 开销较大的平台。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CSL_RECEIVE_TIME_AHEAD"></a>

## 246.49 `CONFIG_OPENTHREAD_CSL_RECEIVE_TIME_AHEAD`

**提示（Prompt）**：CSL 接收端唤醒裕量，单位为微秒（receiver wake up margin）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CSL_REQUEST_TIME_AHEAD"></a>

## 246.50 `CONFIG_OPENTHREAD_CSL_REQUEST_TIME_AHEAD`

**提示（Prompt）**：CSL 发送端请求提前量（transmitter request time ahead）

**说明（Help）**

定义 MAC 应提前多少微秒将 CSL 帧交给子 MAC 层（sub-MAC layer）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
2000
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CSL_TIMEOUT"></a>

## 246.51 `CONFIG_OPENTHREAD_CSL_TIMEOUT`

**提示（Prompt）**：CSL 超时时间，单位为秒（CSL timeout）

**说明（Help）**

默认 CSL 超时时间（timeout），单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_CUSTOM_PARAMETERS"></a>

## 246.52 `CONFIG_OPENTHREAD_CUSTOM_PARAMETERS`

**提示（Prompt）**：传递给 OpenThread 构建系统的自定义参数（Custom Parameters）

**说明（Help）**

此选项仅供高级用户使用。向 OpenThread 构建系统传递没有对应 Kconfig 选项的附加参数。多个值之间以空格 `" "` 分隔，例如：`"OPENTHREAD_CONFIG_JOINER_ENABLE=1 OPENTHREAD_CONFIG_JOINER_MAX_CANDIDATES=3"`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`modules/openthread/Kconfig:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DATASET_UPDATER"></a>

## 246.53 `CONFIG_OPENTHREAD_DATASET_UPDATER`

**提示（Prompt）**：数据集更新器（Dataset updater）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DEBUG"></a>

## 246.54 `CONFIG_OPENTHREAD_DEBUG`

**提示（Prompt）**：OpenThread 协议栈日志支持（stack logging support）

**说明（Help）**

此选项启用 OpenThread 日志支持（logging support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DEFAULT_RX_SENSITIVITY"></a>

## 246.55 `CONFIG_OPENTHREAD_DEFAULT_RX_SENSITIVITY`

**提示（Prompt）**：OpenThread 默认接收灵敏度，单位为 dBm（default RX sensitivity）

**说明（Help）**

设置无线电驱动中的默认接收灵敏度（receive sensitivity），单位为 dBm。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
-100
```

**取值范围（Ranges）**

```text
[-128, 127]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DEFAULT_TX_POWER"></a>

## 246.56 `CONFIG_OPENTHREAD_DEFAULT_TX_POWER`

**提示（Prompt）**：OpenThread 默认发送功率，单位为 dBm（default tx power）

**说明（Help）**

设置无线电驱动供 OpenThread 使用的默认发送输出功率（TX output power），单位为 dBm。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[-40, 20] if CONFIG_NRF_802154_RADIO_DRIVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NRF_802154_RADIO_DRIVER`](P228_modules_hal_nordic_配置项参考_2.md#CONFIG_NRF_802154_RADIO_DRIVER)。

<a id="CONFIG_OPENTHREAD_DEVICE_PROP_LEADER_WEIGHT"></a>

## 246.57 `CONFIG_OPENTHREAD_DEVICE_PROP_LEADER_WEIGHT`

**提示（Prompt）**：用于领导者权重的设备属性（Device props for leader weight）

**说明（Help）**

启用设备属性（device properties），以便据此确定并设置领导者权重（Leader Weight）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
n if CONFIG_OPENTHREAD_THREAD_VERSION_1_1 || CONFIG_OPENTHREAD_THREAD_VERSION_1_2 || CONFIG_OPENTHREAD_THREAD_VERSION_1_3
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_1`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_1)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_2`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_2)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_3`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_3)。

<a id="CONFIG_OPENTHREAD_DEVICE_TYPE"></a>

## 246.58 `CONFIG_OPENTHREAD_DEVICE_TYPE`

**提示（Prompt）**：OpenThread 设备类型（device type）

**说明（Help）**

此选项选择 Thread 网络设备类型（network device type）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_FTD
CONFIG_OPENTHREAD_MTD
CONFIG_OPENTHREAD_FTD
CONFIG_OPENTHREAD_MTD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_FTD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_FTD)、[`CONFIG_OPENTHREAD_MTD`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MTD)。

<a id="CONFIG_OPENTHREAD_DHCP6_CLIENT"></a>

## 246.59 `CONFIG_OPENTHREAD_DHCP6_CLIENT`

**提示（Prompt）**：DHCPv6 客户端支持（client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DHCP6_SERVER"></a>

## 246.60 `CONFIG_OPENTHREAD_DHCP6_SERVER`

**提示（Prompt）**：DHCPv6 服务器支持（server support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DIAG"></a>

## 246.61 `CONFIG_OPENTHREAD_DIAG`

**提示（Prompt）**：诊断功能支持（Diagnostic functions support）

**说明（Help）**

启用 OpenThread CLI 诊断命令（diagnostic commands）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNSSD_DISCOVERY_PROXY"></a>

## 246.62 `CONFIG_OPENTHREAD_DNSSD_DISCOVERY_PROXY`

**提示（Prompt）**：基于 DNS 的服务发现代理支持（DNS-SD discovery proxy support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:173`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L173)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNSSD_SERVER"></a>

## 246.63 `CONFIG_OPENTHREAD_DNSSD_SERVER`

**提示（Prompt）**：基于 DNS 的服务发现服务器支持（DNS-SD server support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNS_CLIENT"></a>

## 246.64 `CONFIG_OPENTHREAD_DNS_CLIENT`

**提示（Prompt）**：DNS 客户端支持（client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNS_CLIENT_OVER_TCP"></a>

## 246.65 `CONFIG_OPENTHREAD_DNS_CLIENT_OVER_TCP`

**提示（Prompt）**：通过 TCP 进行 DNS 查询（DNS query over tcp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNS_DSO"></a>

## 246.66 `CONFIG_OPENTHREAD_DNS_DSO`

**提示（Prompt）**：DNS 有状态操作支持（DNS Stateful Operations，DSO）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:165`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L165)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DNS_UPSTREAM_QUERY"></a>

## 246.67 `CONFIG_OPENTHREAD_DNS_UPSTREAM_QUERY`

**提示（Prompt）**：向上游转发 DNS 查询（Forwarding DNS queries to upstream）

**说明（Help）**

启用将 DNS 查询转发给平台 DNS 上游 API（DNS upstream API）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DUA"></a>

## 246.68 `CONFIG_OPENTHREAD_DUA`

**提示（Prompt）**：域单播地址支持（Domain Unicast Address support）

**说明（Help）**

启用 Thread 1.2 的域单播地址功能（Domain Unicast Address）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_DYNAMIC_STORE_FRAME_AHEAD_COUNTER"></a>

## 246.69 `CONFIG_OPENTHREAD_DYNAMIC_STORE_FRAME_AHEAD_COUNTER`

**提示（Prompt）**：动态存储帧计数器提前值（Dynamic store frame ahead counter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ECDSA"></a>

## 246.70 `CONFIG_OPENTHREAD_ECDSA`

**提示（Prompt）**：椭圆曲线数字签名算法支持（ECDSA support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_SRP_CLIENT
CONFIG_OPENTHREAD_SRP_SERVER
CONFIG_OPENTHREAD_SRP_CLIENT
CONFIG_OPENTHREAD_SRP_SERVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_SRP_CLIENT`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SRP_CLIENT)、[`CONFIG_OPENTHREAD_SRP_SERVER`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SRP_SERVER)。

<a id="CONFIG_OPENTHREAD_ENABLE_SERVICE"></a>

## 246.71 `CONFIG_OPENTHREAD_ENABLE_SERVICE`

**提示（Prompt）**：服务支持（Service support）

**说明（Help）**

在 OpenThread 协议栈中启用 Thread 服务能力（Thread Services capability）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_EXTERNAL_HEAP"></a>

## 246.72 `CONFIG_OPENTHREAD_EXTERNAL_HEAP`

**提示（Prompt）**：外部堆支持（External heap support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:195`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L195)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_EXTERNAL_HEAP_SHARED_MULTI_HEAP"></a>

## 246.73 `CONFIG_OPENTHREAD_EXTERNAL_HEAP_SHARED_MULTI_HEAP`

**提示（Prompt）**：从外部内存分配 OpenThread 堆（external memory）

**说明（Help）**

通过共享多堆（shared multi-heap）使用外部内存，满足 OpenThread 动态内存分配需求（`otPlatCAlloc`／`otPlatFree`）。平台必须向共享多堆池注册一个外部内存区域。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_EXTERNAL_HEAP && CONFIG_SHARED_MULTI_HEAP && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 外部堆支持（External heap support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_EXTERNAL_HEAP`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_EXTERNAL_HEAP)、[`CONFIG_SHARED_MULTI_HEAP`](P198_lib_配置项参考_2.md#CONFIG_SHARED_MULTI_HEAP)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_FIREWALL"></a>

## 246.74 `CONFIG_OPENTHREAD_FIREWALL`

**提示（Prompt）**：防火墙支持（Firewall support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_FTD"></a>

## 246.75 `CONFIG_OPENTHREAD_FTD`

**提示（Prompt）**：FTD：完整 Thread 设备（Full Thread Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_DEVICE_TYPE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:68`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L68)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → OpenThread 设备类型（device type）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_DEVICE_TYPE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_DEVICE_TYPE)。

<a id="CONFIG_OPENTHREAD_FULL_LOGS"></a>

## 246.76 `CONFIG_OPENTHREAD_FULL_LOGS`

**提示（Prompt）**：OpenThread 完整日志（full logs）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:210`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L210)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_HISTORY_TRACKER"></a>

## 246.77 `CONFIG_OPENTHREAD_HISTORY_TRACKER`

**提示（Prompt）**：历史跟踪器支持（History tracker support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_IMPLEMENTATION"></a>

## 246.78 `CONFIG_OPENTHREAD_IMPLEMENTATION`

**提示（Prompt）**：OpenThread 来源选择（origin selection）

**说明（Help）**

选择构建所用的 OpenThread 协议栈。可以将自定义 OpenThread 实现添加到应用 Kconfig 中。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_SOURCES
CONFIG_OPENTHREAD_SOURCES
```

**定义位置（Location）**：[`modules/openthread/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_SOURCES`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SOURCES)。

<a id="CONFIG_OPENTHREAD_INTERFACE_EARLY_UP"></a>

## 246.79 `CONFIG_OPENTHREAD_INTERFACE_EARLY_UP`

**提示（Prompt）**：启用 Thread 后立即使 OpenThread 接口就绪（interface ready）

**说明（Help）**

启用后，一旦启用 Thread，就将 OpenThread 接口标记为就绪（运行状态 UP，operational UP）。这意味着在网格链路建立（Mesh Link Establishment）阶段，接口已可发送应用数据包。否则，只有在设备加入 Thread 网络后，才将接口标记为运行状态 UP。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:410`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L410)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_IP6_FRAGM"></a>

## 246.80 `CONFIG_OPENTHREAD_IP6_FRAGM`

**提示（Prompt）**：IPv6 分片支持（fragmentation support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:213`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L213)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_IP6_MAX_EXT_MCAST_ADDRS"></a>

## 246.81 `CONFIG_OPENTHREAD_IP6_MAX_EXT_MCAST_ADDRS`

**提示（Prompt）**：允许从外部添加的 IPv6 多播地址最大数量（maximum IPv6 multicast addresses）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[0, 32]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_IP6_MAX_EXT_UCAST_ADDRS"></a>

## 246.82 `CONFIG_OPENTHREAD_IP6_MAX_EXT_UCAST_ADDRS`

**提示（Prompt）**：允许从外部添加的 IPv6 地址最大数量（maximum IPv6 addresses）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[0, 32]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:211`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L211)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_JAM_DETECTION"></a>

## 246.83 `CONFIG_OPENTHREAD_JAM_DETECTION`

**提示（Prompt）**：干扰检测支持（Jam detection support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_JOINER"></a>

## 246.84 `CONFIG_OPENTHREAD_JOINER`

**提示（Prompt）**：入网设备功能支持（Joiner functions support）

**说明（Help）**

在 OpenThread 协议栈中启用入网设备能力（joiner capability）。注意，入网配置过程（commissioning）使用的 DTLS 握手需要比默认值更大的 Mbed TLS 堆（heap）。用于该过程的 `CONFIG_MBEDTLS_HEAP_SIZE` 建议最小值为 10KB。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:219`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L219)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_JOINER_AUTOSTART"></a>

## 246.85 `CONFIG_OPENTHREAD_JOINER_AUTOSTART`

**提示（Prompt）**：自动启动入网设备（Automatic joiner start）

**说明（Help）**

当设备没有保存的运行数据集（operational dataset）时，在初始化期间启动 Thread 入网设备（commissioning joiner）。入网设备会与通信范围内任何持有已配置 PSKd 的入网委托方（commissioner）进行认证，然后使用该委托方提供的数据集启用 Thread。启用此项前，必须将 `CONFIG_OPENTHREAD_JOINER_PSKD` 设为他人不知道的凭据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_JOINER && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_JOINER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_JOINER)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_JOINER_PSKD"></a>

## 246.86 `CONFIG_OPENTHREAD_JOINER_PSKD`

**提示（Prompt）**：入网设备预共享密钥（Pre-Shared Key for the Joiner，PSKd）

**说明（Help）**

供 `CONFIG_OPENTHREAD_JOINER_AUTOSTART` 使用的入网设备凭据（Joining Device Credential），编码为 6～32 个大写字母或数字字符（0～9、A～Z，但不含 I、O、Q、Z）。此项特意不提供默认值；在设置该值之前，构建会失败。PSKd 是对设备所加入网络进行认证的唯一依据；Thread 规范要求每台设备的 PSKd 唯一，并且仅与预期的入网委托方（commissioner）共享。此处设置的值会编译到镜像中，因此运行该固件的所有设备都会使用相同值，所以该选项仅适合开发使用。产品固件应从工厂数据（factory data）读取每台设备独有的 PSKd，并由应用调用 `otJoinerStart()`，而不是启用 `CONFIG_OPENTHREAD_JOINER_AUTOSTART`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_JOINER_AUTOSTART && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 自动启动入网设备（Automatic joiner start）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_JOINER_AUTOSTART`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_JOINER_AUTOSTART)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LEGACY"></a>

## 246.87 `CONFIG_OPENTHREAD_LEGACY`

**提示（Prompt）**：传统网络支持（Legacy network support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LINK_METRICS_INITIATOR"></a>

## 246.88 `CONFIG_OPENTHREAD_LINK_METRICS_INITIATOR`

**提示（Prompt）**：链路指标发起方（Link Metrics initiator）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LINK_METRICS_MANAGER"></a>

## 246.89 `CONFIG_OPENTHREAD_LINK_METRICS_MANAGER`

**提示（Prompt）**：链路指标管理器（Link Metrics manager）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LINK_METRICS_SUBJECT"></a>

## 246.90 `CONFIG_OPENTHREAD_LINK_METRICS_SUBJECT`

**提示（Prompt）**：链路指标测量对象（Link Metrics subject）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:241`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L241)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL"></a>

## 246.91 `CONFIG_OPENTHREAD_LOG_LEVEL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenThread 协议栈的日志级别（log level）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1 if CONFIG_OPENTHREAD_LOG_LEVEL_CRIT
2 if CONFIG_OPENTHREAD_LOG_LEVEL_WARN
3 if CONFIG_OPENTHREAD_LOG_LEVEL_NOTE
4 if CONFIG_OPENTHREAD_LOG_LEVEL_INFO
5 if CONFIG_OPENTHREAD_LOG_LEVEL_DEBG
0
```

**定义位置（Location）**：[`modules/openthread/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_LOG_LEVEL_CRIT`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CRIT)、[`CONFIG_OPENTHREAD_LOG_LEVEL_WARN`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_WARN)、[`CONFIG_OPENTHREAD_LOG_LEVEL_NOTE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_NOTE)、[`CONFIG_OPENTHREAD_LOG_LEVEL_INFO`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_INFO)、[`CONFIG_OPENTHREAD_LOG_LEVEL_DEBG`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_DEBG)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE"></a>

## 246.92 `CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：OpenThread 协议栈日志级别（stack log level）

**说明（Help）**

此选项选择 OpenThread 协议栈的日志级别（log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_DEBUG && CONFIG_OPENTHREAD
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_LOG_LEVEL_CRIT
CONFIG_OPENTHREAD_LOG_LEVEL_WARN
CONFIG_OPENTHREAD_LOG_LEVEL_NOTE
CONFIG_OPENTHREAD_LOG_LEVEL_INFO
CONFIG_OPENTHREAD_LOG_LEVEL_DEBG
CONFIG_OPENTHREAD_LOG_LEVEL_CRIT
CONFIG_OPENTHREAD_LOG_LEVEL_WARN
CONFIG_OPENTHREAD_LOG_LEVEL_NOTE
CONFIG_OPENTHREAD_LOG_LEVEL_INFO
CONFIG_OPENTHREAD_LOG_LEVEL_DEBG
```

**定义位置（Location）**：[`modules/openthread/Kconfig:90`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L90)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_DEBUG`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_DEBUG)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_LOG_LEVEL_CRIT`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CRIT)、[`CONFIG_OPENTHREAD_LOG_LEVEL_WARN`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_WARN)、[`CONFIG_OPENTHREAD_LOG_LEVEL_NOTE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_NOTE)、[`CONFIG_OPENTHREAD_LOG_LEVEL_INFO`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_INFO)、[`CONFIG_OPENTHREAD_LOG_LEVEL_DEBG`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_DEBG)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_CRIT"></a>

## 246.93 `CONFIG_OPENTHREAD_LOG_LEVEL_CRIT`

**提示（Prompt）**：严重（Critical）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support） → OpenThread 协议栈日志级别（stack log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_DEBG"></a>

## 246.94 `CONFIG_OPENTHREAD_LOG_LEVEL_DEBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:108`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L108)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support） → OpenThread 协议栈日志级别（stack log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_DYNAMIC"></a>

## 246.95 `CONFIG_OPENTHREAD_LOG_LEVEL_DYNAMIC`

**提示（Prompt）**：动态日志级别控制（Dynamic log level control）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_INFO"></a>

## 246.96 `CONFIG_OPENTHREAD_LOG_LEVEL_INFO`

**提示（Prompt）**：信息（Informational）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:105`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L105)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support） → OpenThread 协议栈日志级别（stack log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_NOTE"></a>

## 246.97 `CONFIG_OPENTHREAD_LOG_LEVEL_NOTE`

**提示（Prompt）**：通知（Notice）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:102`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L102)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support） → OpenThread 协议栈日志级别（stack log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_LOG_LEVEL_WARN"></a>

## 246.98 `CONFIG_OPENTHREAD_LOG_LEVEL_WARN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:99`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L99)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。 → OpenThread 协议栈日志支持（stack logging support） → OpenThread 协议栈日志级别（stack log level）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_OPENTHREAD_LOG_PREPEND_LEVEL_ENABLE"></a>

## 246.99 `CONFIG_OPENTHREAD_LOG_PREPEND_LEVEL_ENABLE`

**提示（Prompt）**：在所有 OpenThread 日志消息前添加日志级别（log level）

**说明（Help）**

启用后，OpenThread 日志会加上对应的日志级别前缀（log level prefix），即 `[CRIT]`、`[WARN]`、`[NOTE]`、`[INFO]`、`[DEBG]`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:379`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L379)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAC_BEACON_PAYLOAD_PARSING"></a>

## 246.100 `CONFIG_OPENTHREAD_MAC_BEACON_PAYLOAD_PARSING`

**提示（Prompt）**：MAC 信标载荷解析支持（beacon payload parsing support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:253`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L253)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<!-- kconfig-navigation -->

[上一章](P245_modules_nrf_wifi_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P247_modules_openthread_配置项参考_2.md)
