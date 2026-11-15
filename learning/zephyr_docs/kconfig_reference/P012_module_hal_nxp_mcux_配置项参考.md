---
id: learning.zephyr-docs.kconfig-reference.page-12
title: "`<module:hal_nxp>/mcux`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第12章\_`<module:hal_nxp>/mcux`配置项参考

本章翻译官方 Kconfig 数据库中 `<module:hal_nxp>/mcux` 的 20 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_ELE_TRACK_SESSION_STATE"></a>

## 12.1 `CONFIG_ELE_TRACK_SESSION_STATE`

**提示（Prompt）**：在软件中跟踪会话状态（Session State）

**说明（Help）**

对于 KW45/MCXW71 器件，通过反复调用 OPEN SESSION API，提供获取已打开会话（Session）的方式。这通过在软件中跟踪会话状态实现，对其他器件没有影响。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SECURE_SUBSYSTEM
```

**默认值（Defaults）**

```text
y if CONFIG_SOC_MCXW716C
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/middleware/mcux-secure-subsystem/zephyr/Kconfig:38`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 启用安全子系统（Secure Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SECURE_SUBSYSTEM`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_MCUX_SECURE_SUBSYSTEM)、[`CONFIG_SOC_MCXW716C`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_MCXW716C)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_MCXW716C`。

<a id="CONFIG_MCUX_SECURE_SUBSYSTEM"></a>

## 12.2 `CONFIG_MCUX_SECURE_SUBSYSTEM`

**提示（Prompt）**：启用安全子系统（Secure Subsystem）

**说明（Help）**

包含 ELE S200 的安全子系统（Secure Subsystem）组件。此组件是 ELE S200 硬件之上的抽象层，为密码服务（Cryptographic Services）、密钥管理（Key Management）和设备管理（Device Management）提供 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_DEVICE_HAS_ELE_S200
```

**默认值（Defaults）**

```text
y if CONFIG_ENTROPY_NXP_ELE_TRNG
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/middleware/mcux-secure-subsystem/zephyr/Kconfig:7`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_DEVICE_HAS_ELE_S200`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUX_DEVICE_HAS_ELE_S200)、[`CONFIG_ENTROPY_NXP_ELE_TRNG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_ENTROPY_NXP_ELE_TRNG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUX_DEVICE_HAS_ELE_S200`。

<a id="CONFIG_MCUX_SECURE_SUBSYSTEM_FIRMWARE_EL2GO"></a>

## 12.3 `CONFIG_MCUX_SECURE_SUBSYSTEM_FIRMWARE_EL2GO`

**提示（Prompt）**：包含 EdgeLock2Go 固件（Firmware）

**说明（Help）**

在构建中包含 EdgeLock2Go 运行时固件（Runtime Firmware）。该固件为 EdgeLock2Go 服务提供支持，以全局 C 数组的形式提供，并在运行时加载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SECURE_SUBSYSTEM
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/middleware/mcux-secure-subsystem/zephyr/Kconfig:28`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 启用安全子系统（Secure Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SECURE_SUBSYSTEM`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_MCUX_SECURE_SUBSYSTEM)。

<a id="CONFIG_MCUX_SECURE_SUBSYSTEM_LEGACY_CONN_PORT"></a>

## 12.4 `CONFIG_MCUX_SECURE_SUBSYSTEM_LEGACY_CONN_PORT`

**提示（Prompt）**：启用旧版 SSS 连接端口（Legacy Connectivity Port）

**说明（Help）**

此端口是一个封装层（Wrapper Layer），用于方便使用最初为 KW45/MCXW71 开发的连接安全协议栈（Connectivity Security Stacks）。这是旧版封装层，仅作为向后兼容（Backward Compatibility）选项保留。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SECURE_SUBSYSTEM
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/middleware/mcux-secure-subsystem/zephyr/Kconfig:18`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 启用安全子系统（Secure Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SECURE_SUBSYSTEM`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_MCUX_SECURE_SUBSYSTEM)。

<a id="CONFIG_MCUX_SECURE_SUBSYSTEM_SESSION_ID"></a>

## 12.5 `CONFIG_MCUX_SECURE_SUBSYSTEM_SESSION_ID`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

供希望使用同一个会话 ID（Session ID）的驱动和组件使用的辅助符号（Helper Symbol）。它定义为在 KW47/W72 上可重用的会话 ID。对 KW45/W71，该 ID 并不重要，但仍使用相同的 ID。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCUX_SECURE_SUBSYSTEM
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/middleware/mcux-secure-subsystem/zephyr/Kconfig:50`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → 启用安全子系统（Secure Subsystem）

**配置项引用（Symbol References）**：[`CONFIG_MCUX_SECURE_SUBSYSTEM`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_MCUX_SECURE_SUBSYSTEM)。

<a id="CONFIG_RL_ALLOW_CONSUMED_BUFFERS_NOTIFICATION"></a>

## 12.6 `CONFIG_RL_ALLOW_CONSUMED_BUFFERS_NOTIFICATION`

**提示（Prompt）**：`RL_ALLOW_CONSUMED_BUFFERS_NOTIFICATION`（允许已消耗缓冲区通知）

**说明（Help）**

启用后，每当接收缓冲区（Received Buffer）被消耗并放入可用缓冲区队列时，都会通知对端。在 RPMsg-Lite 与 Linux 通信的配置中启用此选项，可解除 Linux 阻塞发送（Blocking Send）的阻塞。默认值为 `0`，对应 RPMsg-Lite 与 RPMsg-Lite 通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:127`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_ALLOW_CUSTOM_SHMEM_CONFIG"></a>

## 12.7 `CONFIG_RL_ALLOW_CUSTOM_SHMEM_CONFIG`

**提示（Prompt）**：`RL_ALLOW_CUSTOM_SHMEM_CONFIG`（允许自定义共享内存配置）

**说明（Help）**

此选项允许定义自定义共享内存配置（Custom Shared Memory Configuration），替换 `rpmsg_config.h` 中与共享内存相关的全局设置。当多个实例并行运行，却需要不同共享内存布局，例如不同的 vring 大小与对齐、缓冲区大小与数量时，此功能很有用。注意，启用后需要在平台层（Platform Layer）实现 `platform_get_custom_shmem_config()` 函数。默认值为 `0`，即所有 RPMsg_Lite 实例均使用由公共配置宏定义的相同共享内存布局。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:40`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_API_HAS_ZEROCOPY"></a>

## 12.8 `CONFIG_RL_API_HAS_ZEROCOPY`

**提示（Prompt）**：`RL_API_HAS_ZEROCOPY`（API 具有零复制功能）

**说明（Help）**

启用或禁用零复制 API（Zero-copy API）函数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:75`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_BUFFER_COUNT"></a>

## 12.9 `CONFIG_RL_BUFFER_COUNT`

**提示（Prompt）**：`RL_BUFFER_COUNT_VALUE`（缓冲区数量值）

**说明（Help）**

缓冲区（Buffer）数量，必须为 2 的幂，例如 2、4 等。注意，此值仅定义 RPMsg 通信单个方向的缓冲区数量；例如，主端（Master）和远端（Remote）的 `rpmsg_config.h` 文件都使用默认值 `2` 时，共享内存中总共会创建 4 个缓冲区。类型为无符号整数（Unsigned）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:64`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_BUFFER_PAYLOAD_SIZE"></a>

## 12.10 `CONFIG_RL_BUFFER_PAYLOAD_SIZE`

**提示（Prompt）**：`RL_BUFFER_PAYLOAD_SIZE_VALUE`（缓冲区载荷大小值）

**说明（Help）**

缓冲区载荷（Buffer Payload）的大小，必须大于 `0`。加上 RPMsg 头部所需的 16 字节后，应按字（Word）对齐；如果尚未对齐，该值将向上按字对齐。请确保 RPMsg 通信两端定义相同的值。类型为无符号整数（Unsigned）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
496
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:53`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_CLEAR_USED_BUFFERS"></a>

## 12.11 `CONFIG_RL_CLEAR_USED_BUFFERS`

**提示（Prompt）**：`RL_CLEAR_USED_BUFFERS`（清除已用缓冲区）

**说明（Help）**

启用或禁用在将已用缓冲区归还空闲缓冲区池（Pool of Free Buffers）之前清除其内容的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:87`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_DEBUG_CHECK_BUFFERS"></a>

## 12.12 `CONFIG_RL_DEBUG_CHECK_BUFFERS`

**提示（Prompt）**：`RL_DEBUG_CHECK_BUFFERS`（调试检查缓冲区）

**说明（Help）**

启用后，将检查传给 `rpmsg_lite_send_nocopy()` 和 `rpmsg_lite_release_rx_buffer()` 的缓冲区指针（Buffer Pointer），避免传入无效指针；这两个函数由 `RL_API_HAS_ZEROCOPY` 配置启用。默认值为 `0`，即禁用。请勿在 RPMsg-Lite 与 Linux 通信的配置中使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:118`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_MS_PER_INTERVAL"></a>

## 12.13 `CONFIG_RL_MS_PER_INTERVAL`

**提示（Prompt）**：`RL_MS_PER_INTERVAL`（每个间隔的毫秒数）

**说明（Help）**

非阻塞 API（Non-blocking API）函数轮询时使用的延迟，以毫秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:34`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_USE_DCACHE"></a>

## 12.14 `CONFIG_RL_USE_DCACHE`

**提示（Prompt）**：`RL_USE_DCACHE`（使用数据缓存）

**说明（Help）**

共享内存（Shared Memory）的内存缓存管理（Memory Cache Management）。共享内存启用数据缓存（Data Cache）时使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:94`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_USE_ENVIRONMENT_CONTEXT"></a>

## 12.15 `CONFIG_RL_USE_ENVIRONMENT_CONTEXT`

**提示（Prompt）**：`RL_USE_ENVIRONMENT_CONTEXT`（使用环境上下文）

**说明（Help）**

启用后，环境层（Environment Layer）使用自身的上下文（Context）。此功能主要为 QNX 移植而添加，也可在有需要时使用。默认值为 `0`，不使用上下文，以节省一些 RAM。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:110`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_USE_MCMGR_IPC_ISR_HANDLER"></a>

## 12.16 `CONFIG_RL_USE_MCMGR_IPC_ISR_HANDLER`

**提示（Prompt）**：`RL_USE_MCMGR_IPC_ISR_HANDLER`（使用 MCMGR IPC 中断服务处理程序）

**说明（Help）**

启用后，IPC 中断由多核管理器（Multicore Manager，即 IPC 中断路由器）管理；禁用时，RPMsg-Lite 自行管理 IPC 中断。默认值为 `0`，不使用 MCMGR IPC 中断服务处理程序（ISR Handler）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:101`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RL_USE_STATIC_API"></a>

## 12.17 `CONFIG_RL_USE_STATIC_API`

**提示（Prompt）**：`RL_USE_STATIC_API`（使用静态 API）

**说明（Help）**

启用或禁用静态 API（Static API）函数，即不进行动态分配的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:81`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support） → RPMSG-Lite 配置（Configuration，`rpmsg_config.h`）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<a id="CONFIG_RPMSGLITE"></a>

## 12.18 `CONFIG_RPMSGLITE`

**提示（Prompt）**：RPMSG-Lite 支持（Support）

**说明（Help）**

此选项启用 RPMSG-Lite 库（Library）。

**类型（Type）**：布尔值（Boolean），`bool`。

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:10`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`）

**配置项引用（Symbol References）**：[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)。

<a id="CONFIG_RPMSGLITE_NS"></a>

## 12.19 `CONFIG_RPMSGLITE_NS`

**提示（Prompt）**：RPMSG-Lite 名称服务（Name Service）

**说明（Help）**

此选项启用 RPMSG-Lite 名称服务（Name Service）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**被选择（Selected by）**

```text
CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:27`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)、[`CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_IPC_SERVICE_BACKEND_RPMSG_LITE)。

<a id="CONFIG_RPMSGLITE_QUEUE"></a>

## 12.20 `CONFIG_RPMSGLITE_QUEUE`

**提示（Prompt）**：RPMSG-Lite 队列（Queue）

**说明（Help）**

此选项启用 RPMSG-Lite 队列（Queue）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RPMSGLITE
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：`<module:hal_nxp>/mcux/mcux-sdk-ng/middleware/mcuxsdk-middleware-multicore/rpmsg-lite/zephyr/Kconfig:21`。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → `hal_nxp`（NXP 硬件抽象层模块；工作区相对路径 `modules/hal/nxp`） → RPMSG-Lite 支持（Support）

**配置项引用（Symbol References）**：[`CONFIG_RPMSGLITE`](P012_module_hal_nxp_mcux_配置项参考.md#CONFIG_RPMSGLITE)。

<!-- kconfig-navigation -->

[上一章](P011_module_hal_intel_zephyr_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P013_module_hal_realtek_ameba_配置项参考.md)
