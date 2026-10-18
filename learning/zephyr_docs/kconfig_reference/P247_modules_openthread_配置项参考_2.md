---
id: learning.zephyr-docs.kconfig-reference.page-247
title: "`modules/openthread`配置项参考（2/3）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第247章\_`modules/openthread`配置项参考（2/3）

本章翻译官方 Kconfig 数据库中 `modules/openthread` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_OPENTHREAD_MAC_FILTER"></a>

## 247.1 `CONFIG_OPENTHREAD_MAC_FILTER`

**提示（Prompt）**：MAC 过滤器支持（filter support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAC_SOFTWARE_ACK_TIMEOUT_ENABLE"></a>

## 247.2 `CONFIG_OPENTHREAD_MAC_SOFTWARE_ACK_TIMEOUT_ENABLE`

**提示（Prompt）**：软件确认超时逻辑（Software ACK timeout logic）

**说明（Help）**

若无线电支持 AckTime 事件（AckTime event），则设为 `y`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig:385`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L385)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAC_SOFTWARE_CSMA_BACKOFF_ENABLE"></a>

## 247.3 `CONFIG_OPENTHREAD_MAC_SOFTWARE_CSMA_BACKOFF_ENABLE`

**提示（Prompt）**：软件载波侦听多路访问退避逻辑（Software CSMA backoff logic）

**说明（Help）**

设为 `y` 可启用软件 CSMA 退避（software CSMA backoff）。若无线电对此功能提供硬件支持（`IEEE802154_HW_CSMA`），可禁用此选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAC_SOFTWARE_RETRANSMIT_ENABLE"></a>

## 247.4 `CONFIG_OPENTHREAD_MAC_SOFTWARE_RETRANSMIT_ENABLE`

**提示（Prompt）**：软件重传逻辑（Software retransmission logic）

**说明（Help）**

若无线电支持具有冲突避免（CSMA）的发送重试逻辑（tx retry logic），则设为 `y`。译注：此处按原始帮助正文翻译；其表述与“软件重传逻辑”标题之间的关系，应结合实际无线电实现判断。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAC_SOFTWARE_TX_SECURITY_ENABLE"></a>

## 247.5 `CONFIG_OPENTHREAD_MAC_SOFTWARE_TX_SECURITY_ENABLE`

**提示（Prompt）**：软件传输安全逻辑（Software transmission security logic）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if !CONFIG_OPENTHREAD_THREAD_VERSION_1_1
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:140`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L140)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_1`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_1)。

<a id="CONFIG_OPENTHREAD_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS"></a>

## 247.6 `CONFIG_OPENTHREAD_MAC_STAY_AWAKE_BETWEEN_FRAGMENTS`

**提示（Prompt）**：数据包分片之间保持唤醒（Stay awake between packet fragments）

**说明（Help）**

此优化以增加休眠终端设备／同步休眠终端设备（SED／SSED）的功耗为代价。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:232`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L232)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MANUAL_START"></a>

## 247.7 `CONFIG_OPENTHREAD_MANUAL_START`

**提示（Prompt）**：手动启动 OpenThread 协议栈（Start OpenThread stack manually）

**说明（Help）**

启用后，必须通过相应 API 调用或 CLI／NCP 命令手动配置并启动 OpenThread 协议栈。否则，OpenThread 会在初始化期间自动配置网络参数并尝试加入 Thread 网络；具体使用持久存储中保存的凭据、入网配置过程中获取的凭据，或通过其他 Kconfig 选项预先配置的凭据，取决于所用配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_COPROCESSOR
CONFIG_OPENTHREAD_COPROCESSOR
```

**定义位置（Location）**：[`modules/openthread/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_COPROCESSOR`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR)。

<a id="CONFIG_OPENTHREAD_MAX_CHILDREN"></a>

## 247.8 `CONFIG_OPENTHREAD_MAX_CHILDREN`

**提示（Prompt）**：子设备的最大数量（maximum number of children）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
32
```

**取值范围（Ranges）**

```text
[1, 511]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:83`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L83)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAX_IP_ADDR_PER_CHILD"></a>

## 247.9 `CONFIG_OPENTHREAD_MAX_IP_ADDR_PER_CHILD`

**提示（Prompt）**：每个子设备可注册的 IPv6 地址最大数量（maximum IPv6 address registrations per child）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
6
```

**取值范围（Ranges）**

```text
[4, 255]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:88`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L88)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MAX_STATECHANGE_HANDLERS"></a>

## 247.10 `CONFIG_OPENTHREAD_MAX_STATECHANGE_HANDLERS`

**提示（Prompt）**：状态变化回调处理函数的最大数量（maximum state-changed callback handlers）

**说明（Help）**

使用 `otSetStateChangedCallback` 设置的状态变化回调处理函数（state-changed callback handler）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`modules/openthread/Kconfig:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MBEDTLS_LIB_NAME"></a>

## 247.11 `CONFIG_OPENTHREAD_MBEDTLS_LIB_NAME`

**提示（Prompt）**：mbedtls 库名称（lib name）

**说明（Help）**

此选项允许指定一个或多个要与 OpenThread 链接的 mbedtls 库文件（library file）。多个值之间用空格 `" "` 分隔。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"mbedtls_iface"
```

**定义位置（Location）**：[`modules/openthread/Kconfig:258`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L258)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG"></a>

## 247.12 `CONFIG_OPENTHREAD_MBEDTLS_TLS_CONFIG`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

Mbed TLS 的 TLS 配置（TLS configuration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
CONFIG_MBEDTLS_MD_C
CONFIG_MBEDTLS_ASN1_PARSE_C
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 if CONFIG_OPENTHREAD_COMMISSIONER_JOINER
CONFIG_MBEDTLS_SSL_PROTO_DTLS if CONFIG_OPENTHREAD_COMMISSIONER_JOINER
CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED if CONFIG_OPENTHREAD_COMMISSIONER_JOINER
CONFIG_MBEDTLS_X509_CRT_PARSE_C if CONFIG_OPENTHREAD_ECDSA
CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED if CONFIG_OPENTHREAD_ECDSA
CONFIG_MBEDTLS_PK_WRITE_C if CONFIG_OPENTHREAD_ECDSA
CONFIG_MBEDTLS_ECP_NIST_OPTIM if CONFIG_OPENTHREAD_COMMISSIONER_JOINER || CONFIG_OPENTHREAD_ECDSA
```

**弱选择（Implies）**

```text
CONFIG_MBEDTLS_ENABLE_HEAP
```

**定义位置（Location）**：[`modules/openthread/Kconfig:238`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L238)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_MD_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_MD_C)、[`CONFIG_MBEDTLS_ASN1_PARSE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ASN1_PARSE_C)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_OPENTHREAD_COMMISSIONER_JOINER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_OPENTHREAD_COMMISSIONER_JOINER)、[`CONFIG_MBEDTLS_SSL_PROTO_DTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_DTLS)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECJPAKE_ENABLED)、[`CONFIG_MBEDTLS_X509_CRT_PARSE_C`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_MBEDTLS_X509_CRT_PARSE_C)、[`CONFIG_OPENTHREAD_ECDSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_ECDSA)、[`CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_KEY_EXCHANGE_ECDHE_ECDSA_ENABLED)、[`CONFIG_MBEDTLS_PK_WRITE_C`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_PK_WRITE_C)、[`CONFIG_MBEDTLS_ECP_NIST_OPTIM`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ECP_NIST_OPTIM)、[`CONFIG_MBEDTLS_ENABLE_HEAP`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_ENABLE_HEAP)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_OPENTHREAD_COMMISSIONER_JOINER`。

<a id="CONFIG_OPENTHREAD_MESH_DIAG"></a>

## 247.13 `CONFIG_OPENTHREAD_MESH_DIAG`

**提示（Prompt）**：网格网络诊断（Mesh Diagnostics）

**说明（Help）**

启用网格网络诊断（Mesh Diagnostics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_FTD && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:259`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L259)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_FTD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_FTD)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MESSAGE_BUFFER_SIZE"></a>

## 247.14 `CONFIG_OPENTHREAD_MESSAGE_BUFFER_SIZE`

**提示（Prompt）**：消息缓冲区大小，单位为字节（message buffer size）

**说明（Help）**

“消息缓冲区大小，单位为字节”（The size of a message buffer in bytes）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`modules/openthread/Kconfig:340`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L340)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MESSAGE_POOL_CUSTOM_SECTION"></a>

## 247.15 `CONFIG_OPENTHREAD_MESSAGE_POOL_CUSTOM_SECTION`

**提示（Prompt）**：将消息池缓冲区放入自定义链接器节（custom linker section）

**说明（Help）**

将 OpenThread 消息池缓冲区（message pool buffer）放入自定义链接器节 `.ot_msg_pool`。这样可以将其重定位到外部内存（external memory）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 使用平台消息管理（platform message management）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MESSAGE_USE_HEAP"></a>

## 247.16 `CONFIG_OPENTHREAD_MESSAGE_USE_HEAP`

**提示（Prompt）**：消息缓冲区的堆分配器（Heap allocator for message buffers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:265`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L265)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MIN_RECEIVE_ON_AFTER"></a>

## 247.17 `CONFIG_OPENTHREAD_MIN_RECEIVE_ON_AFTER`

**提示（Prompt）**：MAC 头部开始后的最短接收时间（Minimum receiving time after start of MHR）

**说明（Help）**

从 MAC 头部（MHR）开始后，无线电应保持接收模式的最短时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
5504
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MIN_RECEIVE_ON_AHEAD"></a>

## 247.18 `CONFIG_OPENTHREAD_MIN_RECEIVE_ON_AHEAD`

**提示（Prompt）**：MAC 头部开始前的最短接收时间（Minimum receiving time before start of MHR）

**说明（Help）**

在 MAC 头部（MHR）开始前，无线电必须已处于接收模式的最短时间，单位为微秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
192
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MLE_CHILD_TIMEOUT"></a>

## 247.19 `CONFIG_OPENTHREAD_MLE_CHILD_TIMEOUT`

**提示（Prompt）**：OpenThread 网格链路建立子设备超时时间，单位为秒（MLE child timeout）

**说明（Help）**

网格链路建立子设备超时时间（MLE child timeout）的值，单位为秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
240
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:301`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L301)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MLE_INFORM_PREVIOUS_PARENT_ON_REATTACH"></a>

## 247.20 `CONFIG_OPENTHREAD_MLE_INFORM_PREVIOUS_PARENT_ON_REATTACH`

**提示（Prompt）**：重新附着时通知原父设备（Inform previous parent on reattach）

**说明（Help）**

若希望 Thread 网络中的终端设备（End Device，ED）在附着到新父路由器后通知原父路由器，请启用重新附着时通知原父设备功能（Inform Previous Parent on Reattach）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_PARENT_SEARCH
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_PARENT_SEARCH`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PARENT_SEARCH)。

<a id="CONFIG_OPENTHREAD_MLE_LONG_ROUTES"></a>

## 247.21 `CONFIG_OPENTHREAD_MLE_LONG_ROUTES`

**提示（Prompt）**：网格链路建立长路由扩展（MLE long routes extension）［实验性，EXPERIMENTAL］

**说明（Help）**

启用网格链路建立长路由扩展（MLE long routes extension）；此功能为实验性，会破坏 Thread 一致性（Thread conformance）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:268`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L268)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_OPENTHREAD_MLR"></a>

## 247.22 `CONFIG_OPENTHREAD_MLR`

**提示（Prompt）**：多播监听者注册支持（Multicast Listener Registration support）

**说明（Help）**

启用 Thread 1.2 的多播监听者注册支持（Multicast Listener Registration support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:274`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L274)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MTD"></a>

## 247.23 `CONFIG_OPENTHREAD_MTD`

**提示（Prompt）**：MTD：最小 Thread 设备（Minimal Thread Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_DEVICE_TYPE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → OpenThread 设备类型（device type）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_DEVICE_TYPE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_DEVICE_TYPE)。

<a id="CONFIG_OPENTHREAD_MTD_SED"></a>

## 247.24 `CONFIG_OPENTHREAD_MTD_SED`

**提示（Prompt）**：SED：休眠终端设备（Sleepy End Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_MTD && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_MTD`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MTD)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MULTICAST_DNS"></a>

## 247.25 `CONFIG_OPENTHREAD_MULTICAST_DNS`

**提示（Prompt）**：多播 DNS（Multicast DNS，mDNS）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:256`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L256)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MULTIPAN_RCP"></a>

## 247.26 `CONFIG_OPENTHREAD_MULTIPAN_RCP`

**提示（Prompt）**：OpenThread 多 PAN 无线电协处理器（multipan rcp）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:279`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L279)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MULTIPLE_INSTANCE"></a>

## 247.27 `CONFIG_OPENTHREAD_MULTIPLE_INSTANCE`

**提示（Prompt）**：OpenThread 多实例（multiple instances）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:282`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L282)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_MULTIPLE_INSTANCE_NUM"></a>

## 247.28 `CONFIG_OPENTHREAD_MULTIPLE_INSTANCE_NUM`

**提示（Prompt）**：OpenThread 实例数量（number of instances）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_MULTIPLE_INSTANCE && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → OpenThread 多实例（multiple instances）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_MULTIPLE_INSTANCE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MULTIPLE_INSTANCE)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NAT64_BORDER_ROUTING"></a>

## 247.29 `CONFIG_OPENTHREAD_NAT64_BORDER_ROUTING`

**提示（Prompt）**：边界路由 NAT64 支持（Border routing NAT64 support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:290`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L290)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR)。

<a id="CONFIG_OPENTHREAD_NAT64_CIDR"></a>

## 247.30 `CONFIG_OPENTHREAD_NAT64_CIDR`

**提示（Prompt）**：设置 NAT64 使用的 IPv4 CIDR（IPv4 CIDR used by NAT64）

**说明（Help）**

设置 NAT64 使用的 IPv4 无类别域间路由（Classless Inter-Domain Routing，CIDR），以确定转换后向外发送的 IPv4 数据包的源地址。CIDR 地址必须含有四个字节，且前缀长度非零，例如 `"127.0.0.1/24"`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_BORDER_ROUTING && CONFIG_OPENTHREAD_NAT64_TRANSLATOR && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"192.168.255.0/24"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_BORDER_ROUTING`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_BORDER_ROUTING)、[`CONFIG_OPENTHREAD_NAT64_TRANSLATOR`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_NAT64_TRANSLATOR)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NAT64_TRANSLATOR"></a>

## 247.31 `CONFIG_OPENTHREAD_NAT64_TRANSLATOR`

**提示（Prompt）**：NAT64 转换器支持（translator support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR)。

<a id="CONFIG_OPENTHREAD_NEIGHBOR_DISCOVERY_AGENT"></a>

## 247.32 `CONFIG_OPENTHREAD_NEIGHBOR_DISCOVERY_AGENT`

**提示（Prompt）**：邻居发现代理支持（Neighbor discovery agent support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:302`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L302)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NETDATA_PUBLISHER"></a>

## 247.33 `CONFIG_OPENTHREAD_NETDATA_PUBLISHER`

**提示（Prompt）**：Thread 网络数据发布者（Network Data publisher）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_SRP_SERVER
CONFIG_OPENTHREAD_SRP_SERVER
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:305`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L305)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_SRP_SERVER`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SRP_SERVER)。

<a id="CONFIG_OPENTHREAD_NETDIAG_CLIENT"></a>

## 247.34 `CONFIG_OPENTHREAD_NETDIAG_CLIENT`

**提示（Prompt）**：客户端上的 Thread 管理框架网络诊断（TMF network diagnostics）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:296`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L296)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NETDIAG_VENDOR_INFO"></a>

## 247.35 `CONFIG_OPENTHREAD_NETDIAG_VENDOR_INFO`

**提示（Prompt）**：允许运行时设置厂商信息（vendor info at runtime）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:299`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L299)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NETWORKKEY"></a>

## 247.36 `CONFIG_OPENTHREAD_NETWORKKEY`

**提示（Prompt）**：默认 Thread 网络密钥（Default Thread Network Key）

**说明（Help）**

OpenThread 网络密钥（Network Key），格式为 `"00:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee:ff"`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NETWORK_NAME"></a>

## 247.37 `CONFIG_OPENTHREAD_NETWORK_NAME`

**提示（Prompt）**：默认网络名称（Default network name）

**说明（Help）**

OpenThread 的网络名称（Network name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"ot_zephyr"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NET_DIAG_VENDOR_MODEL"></a>

## 247.38 `CONFIG_OPENTHREAD_NET_DIAG_VENDOR_MODEL`

**提示（Prompt）**：填入 OpenThread 网络诊断 TLV 的厂商型号（Vendor model）

**说明（Help）**

此值表示将在网络诊断类型－长度－值字段（network diagnostic TLV）中公开的厂商型号（vendor model）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr-OpenThread"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:328`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L328)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NET_DIAG_VENDOR_NAME"></a>

## 247.39 `CONFIG_OPENTHREAD_NET_DIAG_VENDOR_NAME`

**提示（Prompt）**：填入 OpenThread 网络诊断 TLV 的厂商名称（Vendor name）

**说明（Help）**

此值表示将在网络诊断类型－长度－值字段（network diagnostic TLV）中公开的厂商名称（vendor name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:322`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L322)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NET_DIAG_VENDOR_SW_VERSION"></a>

## 247.40 `CONFIG_OPENTHREAD_NET_DIAG_VENDOR_SW_VERSION`

**提示（Prompt）**：填入 OpenThread 网络诊断 TLV 的厂商软件版本（Vendor software version）

**说明（Help）**

此值表示将在网络诊断类型－长度－值字段（network diagnostic TLV）中公开的厂商软件版本（vendor software version）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"Zephyr-OT-v1.0"
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_NUM_MESSAGE_BUFFERS"></a>

## 247.41 `CONFIG_OPENTHREAD_NUM_MESSAGE_BUFFERS`

**提示（Prompt）**：缓冲池中的消息缓冲区数量（number of message buffers）

**说明（Help）**

“缓冲池中的消息缓冲区数量”（The number of message buffers in the buffer pool）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
512 if CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER
128
```

**定义位置（Location）**：[`modules/openthread/Kconfig:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER)。

<a id="CONFIG_OPENTHREAD_OPERATIONAL_DATASET_AUTO_INIT"></a>

## 247.42 `CONFIG_OPENTHREAD_OPERATIONAL_DATASET_AUTO_INIT`

**提示（Prompt）**：运行数据集自动初始化（Operational dataset auto init）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:308`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L308)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_OTNS"></a>

## 247.43 `CONFIG_OPENTHREAD_OTNS`

**提示（Prompt）**：OpenThread 网络模拟器支持（OTNS support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:312`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L312)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PANID"></a>

## 247.44 `CONFIG_OPENTHREAD_PANID`

**提示（Prompt）**：默认个域网标识（Default PAN ID）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
43981
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PARENT_SEARCH"></a>

## 247.45 `CONFIG_OPENTHREAD_PARENT_SEARCH`

**提示（Prompt）**：周期性父设备搜索支持（Periodic parent search support）

**说明（Help）**

若希望 Thread 网络中的终端设备（End Device，ED）在保持网络连接的同时切换到比当前父路由器更优的父路由器，请启用周期性父设备搜索功能（Periodic Parent Search）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:152`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L152)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PARENT_SEARCH_BACKOFF_INTERVAL"></a>

## 247.46 `CONFIG_OPENTHREAD_PARENT_SEARCH_BACKOFF_INTERVAL`

**提示（Prompt）**：防止父设备搜索重试的退避间隔，单位为秒（Backoff interval）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_PARENT_SEARCH && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
36000
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:164`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L164)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 周期性父设备搜索支持（Periodic parent search support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PARENT_SEARCH`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PARENT_SEARCH)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PARENT_SEARCH_CHECK_INTERVAL"></a>

## 247.47 `CONFIG_OPENTHREAD_PARENT_SEARCH_CHECK_INTERVAL`

**提示（Prompt）**：触发父设备搜索的间隔，单位为秒（Interval to trigger parent search）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_PARENT_SEARCH && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
540
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:159`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L159)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 周期性父设备搜索支持（Periodic parent search support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PARENT_SEARCH`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PARENT_SEARCH)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PARENT_SEARCH_RSS_THRESHOLD"></a>

## 247.48 `CONFIG_OPENTHREAD_PARENT_SEARCH_RSS_THRESHOLD`

**提示（Prompt）**：触发父设备搜索的接收信号强度指示阈值（RSSI threshold）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_PARENT_SEARCH && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
-65
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 周期性父设备搜索支持（Periodic parent search support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PARENT_SEARCH`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PARENT_SEARCH)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PING_SENDER"></a>

## 247.49 `CONFIG_OPENTHREAD_PING_SENDER`

**提示（Prompt）**：Ping 发送端支持（Ping sender support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PKT_LIST_SIZE"></a>

## 247.50 `CONFIG_OPENTHREAD_PKT_LIST_SIZE`

**提示（Prompt）**：IPv6 数据包缓冲列表大小（List size for IPv6 packet buffering）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`modules/openthread/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE"></a>

## 247.51 `CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

平台引导加载程序模式支持（Platform bootloader mode support）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO)。

<a id="CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE"></a>

## 247.52 `CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE`

**提示（Prompt）**：平台引导加载程序模式配置（Platform bootloader mode configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:329`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L329)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO)。

<a id="CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO"></a>

## 247.53 `CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_GPIO`

**提示（Prompt）**：通过 GPIO 引脚触发的引导加载程序模式支持（Bootloader mode support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 平台引导加载程序模式配置（Platform bootloader mode configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE)。

<a id="CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION"></a>

## 247.54 `CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_RETENTION`

**提示（Prompt）**：通过启动模式保留 API 提供的引导加载程序模式支持（boot mode retention API）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_RETENTION_BOOT_MODE && CONFIG_REBOOT && <choice CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE>
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:333`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L333)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 平台引导加载程序模式配置（Platform bootloader mode configuration）

**配置项引用（Symbol References）**：[`CONFIG_RETENTION_BOOT_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RETENTION_BOOT_MODE)、[`CONFIG_REBOOT`](P198_lib_配置项参考_2.md#CONFIG_REBOOT)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE_CHOICE)、[`CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_BOOTLOADER_MODE)。

<a id="CONFIG_OPENTHREAD_PLATFORM_CARRIER_FUNCTIONS"></a>

## 247.55 `CONFIG_OPENTHREAD_PLATFORM_CARRIER_FUNCTIONS`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用调制载波（Modulated Carrier）和连续载波（Continuous Carrier）等功能支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_OPENTHREAD_DIAG && CONFIG_IEEE802154_CARRIER_FUNCTIONS
```

**定义位置（Location）**：[`modules/openthread/Kconfig:427`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L427)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_DIAG`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_DIAG)、[`CONFIG_IEEE802154_CARRIER_FUNCTIONS`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154_CARRIER_FUNCTIONS)。

<a id="CONFIG_OPENTHREAD_PLATFORM_CSL_UNCERT"></a>

## 247.56 `CONFIG_OPENTHREAD_PLATFORM_CSL_UNCERT`

**提示（Prompt）**：协调采样监听不确定度（CSL uncertainty）

**说明（Help）**

设备调度 CSL 传输时的固定不确定度（fixed uncertainty），以 10 微秒为单位。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
255
```

**取值范围（Ranges）**

```text
[0, 255]
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_INFO"></a>

## 247.57 `CONFIG_OPENTHREAD_PLATFORM_INFO`

**提示（Prompt）**：OpenThread 平台信息（Platform information）

**说明（Help）**

OpenThread 平台信息（Platform information）

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"ZEPHYR"
```

**定义位置（Location）**：[`modules/openthread/Kconfig:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_KEYS_EXPORTABLE_ENABLE"></a>

## 247.58 `CONFIG_OPENTHREAD_PLATFORM_KEYS_EXPORTABLE_ENABLE`

**提示（Prompt）**：使 MAC 密钥可导出（Make MAC keys exportable）

**说明（Help）**

允许在 OpenThread 密钥管理器（Key Manager）中创建可导出的 MAC 密钥（exportable MAC keys）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_PLATFORM_KEY_REF && CONFIG_OPENTHREAD
```

**被弱选择（Implied by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA
```

**定义位置（Location）**：[`modules/openthread/Kconfig:404`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L404)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_PLATFORM_KEY_REF`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_PLATFORM_KEY_REF)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CRYPTO_PSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CRYPTO_PSA)。

<a id="CONFIG_OPENTHREAD_PLATFORM_KEY_REF"></a>

## 247.59 `CONFIG_OPENTHREAD_PLATFORM_KEY_REF`

**提示（Prompt）**：平台加密密钥引用支持（Platform cryptographic key reference support）

**说明（Help）**

启用使用加密密钥引用（cryptographic key reference）而非直接保存的密钥值（literal key）。这要求加密后端库支持密钥引用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_CRYPTO_PSA
CONFIG_OPENTHREAD_CRYPTO_PSA
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CRYPTO_PSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CRYPTO_PSA)。

<a id="CONFIG_OPENTHREAD_PLATFORM_LOG_CRASH_DUMP"></a>

## 247.60 `CONFIG_OPENTHREAD_PLATFORM_LOG_CRASH_DUMP`

**提示（Prompt）**：平台日志崩溃转储（Platform log crash dump）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_LOG_LEVEL"></a>

## 247.61 `CONFIG_OPENTHREAD_PLATFORM_LOG_LEVEL`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

OpenThread Zephyr 平台的日志级别（log level）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
1 if CONFIG_OPENTHREAD_LOG_LEVEL_CRIT
2 if CONFIG_OPENTHREAD_LOG_LEVEL_WARN
3 if CONFIG_OPENTHREAD_LOG_LEVEL_NOTE || CONFIG_OPENTHREAD_LOG_LEVEL_INFO
4 if CONFIG_OPENTHREAD_LOG_LEVEL_DEBG
0
```

**定义位置（Location）**：[`modules/openthread/Kconfig:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 日志（Logging）。

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_LOG_LEVEL_CRIT`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_CRIT)、[`CONFIG_OPENTHREAD_LOG_LEVEL_WARN`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_WARN)、[`CONFIG_OPENTHREAD_LOG_LEVEL_NOTE`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_NOTE)、[`CONFIG_OPENTHREAD_LOG_LEVEL_INFO`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_INFO)、[`CONFIG_OPENTHREAD_LOG_LEVEL_DEBG`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_LOG_LEVEL_DEBG)。

<a id="CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT"></a>

## 247.62 `CONFIG_OPENTHREAD_PLATFORM_MESSAGE_MANAGEMENT`

**提示（Prompt）**：使用平台消息管理（platform message management）

**说明（Help）**

消息池（message pool）由平台定义的逻辑管理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:346`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L346)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_NETIF"></a>

## 247.63 `CONFIG_OPENTHREAD_PLATFORM_NETIF`

**提示（Prompt）**：平台网络接口支持（Platform netif support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_PKT_TXTIME"></a>

## 247.64 `CONFIG_OPENTHREAD_PLATFORM_PKT_TXTIME`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用数据包发送时间支持（packet TX time support）。当应用需要设置数据包应当发送的精确时间时，需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if CONFIG_NET_PKT_TXTIME
```

**定义位置（Location）**：[`modules/openthread/Kconfig:420`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L420)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_NET_PKT_TXTIME`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PKT_TXTIME)。

<a id="CONFIG_OPENTHREAD_PLATFORM_RADIO_COEX_ENABLE"></a>

## 247.65 `CONFIG_OPENTHREAD_PLATFORM_RADIO_COEX_ENABLE`

**提示（Prompt）**：平台无线电共存支持（Platform radio coexistence support）

**说明（Help）**

在平台中启用无线电共存支持（radio coexistence support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:318`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L318)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_UDP"></a>

## 247.66 `CONFIG_OPENTHREAD_PLATFORM_UDP`

**提示（Prompt）**：平台 UDP 支持（Platform UDP support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER"></a>

## 247.67 `CONFIG_OPENTHREAD_PLATFORM_USEC_TIMER`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

启用平台实现的微秒级退避定时器（microsecond backoff timer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y if (CONFIG_OPENTHREAD_CSL_RECEIVER && !CONFIG_OPENTHREAD_THREAD_VERSION_1_1) || CONFIG_OPENTHREAD_WAKEUP_END_DEVICE
y if (CONFIG_OPENTHREAD_COPROCESSOR_RCP || CONFIG_OPENTHREAD_RAW) && !CONFIG_OPENTHREAD_THREAD_VERSION_1_1
```

**定义位置（Location）**：[`modules/openthread/Kconfig:433`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L433)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_CSL_RECEIVER`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_CSL_RECEIVER)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_1`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_1)、[`CONFIG_OPENTHREAD_WAKEUP_END_DEVICE`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_WAKEUP_END_DEVICE)、[`CONFIG_OPENTHREAD_COPROCESSOR_RCP`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_COPROCESSOR_RCP)、[`CONFIG_OPENTHREAD_RAW`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_RAW)。

<a id="CONFIG_OPENTHREAD_POLL_PERIOD"></a>

## 247.68 `CONFIG_OPENTHREAD_POLL_PERIOD`

**提示（Prompt）**：休眠终端设备轮询周期，单位为毫秒（Poll period for sleepy end devices）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_MTD_SED && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
236000
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:78`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L78)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → SED：休眠终端设备（Sleepy End Device）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_MTD_SED`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_MTD_SED)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY"></a>

## 247.69 `CONFIG_OPENTHREAD_POWER_SUPPLY`

**提示（Prompt）**：供电配置（Power supply configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
"BATTERY" if CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY
"EXTERNAL" if CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL
"EXTERNAL_STABLE" if CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE
"EXTERNAL_UNSTABLE" if CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE
""
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY"></a>

## 247.70 `CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY`

**提示（Prompt）**：电池供电（battery）：`OT_POWER_SUPPLY_BATTERY`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:358`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L358)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 供电配置（Power supply configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE"></a>

## 247.71 `CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE`

**提示（Prompt）**：供电配置（Power supply configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE
CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE
CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_BATTERY)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE)、[`CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL"></a>

## 247.72 `CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL`

**提示（Prompt）**：外部供电（external）：`OT_POWER_SUPPLY_EXTERNAL`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:361`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L361)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 供电配置（Power supply configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE"></a>

## 247.73 `CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_STABLE`

**提示（Prompt）**：稳定外部供电（external stable）：`OT_POWER_SUPPLY_EXTERNAL_STABLE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 供电配置（Power supply configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE)。

<a id="CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE"></a>

## 247.74 `CONFIG_OPENTHREAD_POWER_SUPPLY_EXTERNAL_UNSTABLE`

**提示（Prompt）**：不稳定外部供电（external unstable）：`OT_POWER_SUPPLY_EXTERNAL_UNSTABLE`

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE>
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:367`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L367)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features） → 供电配置（Power supply configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_POWER_SUPPLY_CHOICE)。

<a id="CONFIG_OPENTHREAD_RADIO_LINK_IEEE_802_15_4_ENABLE"></a>

## 247.75 `CONFIG_OPENTHREAD_RADIO_LINK_IEEE_802_15_4_ENABLE`

**提示（Prompt）**：IEEE 802.15.4 无线电链路支持（radio link）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:97`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L97)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_RADIO_STATS"></a>

## 247.76 `CONFIG_OPENTHREAD_RADIO_STATS`

**提示（Prompt）**：无线电统计支持（Radio Statistics）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:380`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L380)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION"></a>

## 247.77 `CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION`

**提示（Prompt）**：选择厂商无线电实现（vendor radio implementation）

**说明（Help）**

使用厂商专用的无线电平台抽象层（radio platform abstraction layer）替代默认 Zephyr `radio.c` 实现。启用后，构建系统会编译 `OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION_FILE` 指定的源文件，替代标准 OpenThread 无线电驱动，使厂商能够提供自定义物理层集成（PHY-layer integration）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_L2_OPENTHREAD && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_OPENTHREAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_OPENTHREAD)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION_FILE"></a>

## 247.78 `CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION_FILE`

**提示（Prompt）**：包含厂商专用 radio.c 实现的源文件（vendor-specific implementation）

**说明（Help）**

提供厂商专用 OpenThread 无线电平台抽象（radio platform abstraction）的源文件名称。此文件必须放在 `modules/openthread/platform/vendor/` 目录，并实现 OpenThread 无线电 API（`otPlatRadio*`，以及 `platformRadioInit` 和 `platformRadioProcess` 函数）。构建时将编译此文件，替代默认 `radio.c` 驱动。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`modules/openthread/Kconfig:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → 选择厂商无线电实现（vendor radio implementation）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_RADIO_VENDOR_IMPLEMENTATION)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_RADIO_WORKQUEUE_PRIORITY"></a>

## 247.79 `CONFIG_OPENTHREAD_RADIO_WORKQUEUE_PRIORITY`

**提示（Prompt）**：OpenThread 无线电发送工作队列优先级（radio transmit workqueue priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
0 if CONFIG_OPENTHREAD_THREAD_PREEMPTIVE
7
```

**定义位置（Location）**：[`modules/openthread/Kconfig:162`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L162)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_THREAD_PREEMPTIVE`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_PREEMPTIVE)。

<a id="CONFIG_OPENTHREAD_RADIO_WORKQUEUE_STACK_SIZE"></a>

## 247.80 `CONFIG_OPENTHREAD_RADIO_WORKQUEUE_STACK_SIZE`

**提示（Prompt）**：OpenThread 无线电发送工作队列栈大小（radio transmit workqueue stack size）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
608 if CONFIG_MPU_STACK_GUARD && CONFIG_FPU_SHARING && CONFIG_CPU_CORTEX_M
512
```

**定义位置（Location）**：[`modules/openthread/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Zephyr 优化（Zephyr optimizations）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_MPU_STACK_GUARD`](P028_arch_arc_配置项参考.md#CONFIG_MPU_STACK_GUARD)、[`CONFIG_FPU_SHARING`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_FPU_SHARING)、[`CONFIG_CPU_CORTEX_M`](P029_arch_arm_配置项参考_1.md#CONFIG_CPU_CORTEX_M)。

<a id="CONFIG_OPENTHREAD_RAW"></a>

## 247.81 `CONFIG_OPENTHREAD_RAW`

**提示（Prompt）**：原始链路支持（Raw Link support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_RCP_RESTORATION_MAX_COUNT"></a>

## 247.82 `CONFIG_OPENTHREAD_RCP_RESTORATION_MAX_COUNT`

**提示（Prompt）**：OpenThread RCP 恢复最大次数（RCP restoration maximum count）

**说明（Help）**

尝试恢复无线电协处理器连接（RCP connection）的最大次数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
2
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_REFERENCE_DEVICE"></a>

## 247.83 `CONFIG_OPENTHREAD_REFERENCE_DEVICE`

**提示（Prompt）**：参考设备支持（Reference Device support）

**说明（Help）**

在 OpenThread 协议栈中启用 Thread 认证参考设备支持（Thread Certification reference device support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:386`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L386)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER"></a>

## 247.84 `CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER`

**提示（Prompt）**：OpenThread 路由器选择抖动，单位为秒（router selection jitter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER_OVERRIDE && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
120
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:317`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L317)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 覆盖默认路由器选择抖动（router selection jitter）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER_OVERRIDE`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER_OVERRIDE)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER_OVERRIDE"></a>

## 247.85 `CONFIG_OPENTHREAD_ROUTER_SELECTION_JITTER_OVERRIDE`

**提示（Prompt）**：覆盖默认路由器选择抖动（router selection jitter）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_FTD && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_FTD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_FTD)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SECURITY_CONFIG"></a>

## 247.86 `CONFIG_OPENTHREAD_SECURITY_CONFIG`

**提示（Prompt）**：OpenThread 安全配置（security configuration）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG
CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG
CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG
CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG
```

**定义位置（Location）**：[`modules/openthread/Kconfig:176`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L176)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG)、[`CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG)。

<a id="CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG"></a>

## 247.87 `CONFIG_OPENTHREAD_SECURITY_CUSTOM_CONFIG`

**提示（Prompt）**：自定义配置（Custom configuration）

**说明（Help）**

安全设置（security settings）由用户直接控制。启用此设置可获得对 Mbed TLS 配置的完整控制权。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_SECURITY_CONFIG>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:180`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L180)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 安全配置（security configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SECURITY_CONFIG`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SECURITY_CONFIG)。

<a id="CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG"></a>

## 247.88 `CONFIG_OPENTHREAD_SECURITY_DEFAULT_CONFIG`

**提示（Prompt）**：默认配置（Default configuration）

**说明（Help）**

使用 OpenThread Mbed TLS 配置中预定义的安全方案（pre-defined security scheme）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_SECURITY_CONFIG>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 安全配置（security configuration）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SECURITY_CONFIG`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SECURITY_CONFIG)。

<a id="CONFIG_OPENTHREAD_SETTINGS_RAM"></a>

## 247.89 `CONFIG_OPENTHREAD_SETTINGS_RAM`

**提示（Prompt）**：仅以易失方式存储设置（Volatile-only storage of settings）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:391`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L391)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SHELL"></a>

## 247.90 `CONFIG_OPENTHREAD_SHELL`

**提示（Prompt）**：OpenThread 命令解释器（shell）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig:169`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L169)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT"></a>

## 247.91 `CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT`

**提示（Prompt）**：延迟输出 OpenThread CLI shell 内容（Deferred shell output）

**说明（Help）**

将 OpenThread CLI 控制台输出延迟到系统工作队列（system workqueue）执行，而不是由 OpenThread 线程同步写出。输出先积累到环形缓冲区（ring buffer），再由工作队列逐行取出。这样可避免同步 shell UART 写操作阻塞 OpenThread 线程，并消除 OpenThread 互斥锁与 shell 互斥锁之间的 ABBA 死锁风险（ABBA deadlock）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SHELL && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration）

**配置项引用（Symbol References）**：[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT_BUF_SIZE"></a>

## 247.92 `CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT_BUF_SIZE`

**提示（Prompt）**：OpenThread CLI shell 延迟输出环形缓冲区大小（Deferred output ring buffer size）

**说明（Help）**

用于暂存 OpenThread CLI 控制台延迟输出的环形缓冲区大小，单位为字节；其内容随后由系统工作队列取出。详细输出命令（例如 `router table`、`netdata show`）可能突发产生大量内容，因此应确保此缓冲区足够大，以免丢弃输出。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT && CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
4096
```

**定义位置（Location）**：[`modules/openthread/Kconfig.thread:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.thread#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → Thread 网络配置（Thread Network configuration） → 延迟输出 OpenThread CLI shell 内容（Deferred shell output）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SHELL_DEFERRED_OUTPUT)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SLAAC"></a>

## 247.93 `CONFIG_OPENTHREAD_SLAAC`

**提示（Prompt）**：无状态地址自动配置支持（SLAAC support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:394`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L394)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SNTP_CLIENT"></a>

## 247.94 `CONFIG_OPENTHREAD_SNTP_CLIENT`

**提示（Prompt）**：简单网络时间协议客户端支持（SNTP Client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:397`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L397)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SOURCES"></a>

## 247.95 `CONFIG_OPENTHREAD_SOURCES`

**提示（Prompt）**：从源码构建 OpenThread（OpenThread from sources）

**说明（Help）**

从源码构建 Zephyr 的 OpenThread 移植实现（OpenThread port）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_OPENTHREAD_IMPLEMENTATION>
```

**定义位置（Location）**：[`modules/openthread/Kconfig:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 来源选择（origin selection）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_IMPLEMENTATION`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_IMPLEMENTATION)。

<a id="CONFIG_OPENTHREAD_SRP_ADV_PROXY"></a>

## 247.96 `CONFIG_OPENTHREAD_SRP_ADV_PROXY`

**提示（Prompt）**：服务注册协议服务器通告代理支持（SRP Server Advertising Proxy support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD_SRP_SERVER && CONFIG_OPENTHREAD_BORDER_ROUTING && CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:400`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L400)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD_SRP_SERVER`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_SRP_SERVER)、[`CONFIG_OPENTHREAD_BORDER_ROUTING`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_BORDER_ROUTING)、[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_SRP_CLIENT"></a>

## 247.97 `CONFIG_OPENTHREAD_SRP_CLIENT`

**提示（Prompt）**：服务注册协议客户端支持（SRP Client support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_ECDSA
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:405`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L405)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_ECDSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_ECDSA)。

<a id="CONFIG_OPENTHREAD_SRP_SERVER"></a>

## 247.98 `CONFIG_OPENTHREAD_SRP_SERVER`

**提示（Prompt）**：服务注册协议服务器支持（SRP Server support）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**主动选择（Selects）**

```text
CONFIG_OPENTHREAD_NETDATA_PUBLISHER
CONFIG_OPENTHREAD_ECDSA
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:409`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L409)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_NETDATA_PUBLISHER`](P247_modules_openthread_配置项参考_2.md#CONFIG_OPENTHREAD_NETDATA_PUBLISHER)、[`CONFIG_OPENTHREAD_ECDSA`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD_ECDSA)。

<a id="CONFIG_OPENTHREAD_SRP_SERVER_FAST_START"></a>

## 247.99 `CONFIG_OPENTHREAD_SRP_SERVER_FAST_START`

**提示（Prompt）**：服务注册协议服务器快速启动（SRP server fast start）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:419`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L419)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)。

<a id="CONFIG_OPENTHREAD_STACK_VERSION"></a>

## 247.100 `CONFIG_OPENTHREAD_STACK_VERSION`

**提示（Prompt）**：OpenThread 协议栈版本（stack version）

**说明（Help）**

此选项选择 Thread 协议栈版本（stack version）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OPENTHREAD
```

**默认值（Defaults）**

```text
CONFIG_OPENTHREAD_THREAD_VERSION_1_1
```

**可选项（Choices）**

```text
CONFIG_OPENTHREAD_THREAD_VERSION_1_1
CONFIG_OPENTHREAD_THREAD_VERSION_1_2
CONFIG_OPENTHREAD_THREAD_VERSION_1_3
CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1
CONFIG_OPENTHREAD_THREAD_VERSION_1_4
CONFIG_OPENTHREAD_THREAD_VERSION_1_1
CONFIG_OPENTHREAD_THREAD_VERSION_1_2
CONFIG_OPENTHREAD_THREAD_VERSION_1_3
CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1
CONFIG_OPENTHREAD_THREAD_VERSION_1_4
```

**定义位置（Location）**：[`modules/openthread/Kconfig.features:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/modules/openthread/Kconfig.features#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → openthread（模块路径 `modules/lib/openthread`，相对于 west 工作区顶层目录） → OpenThread 支持（OpenThread Support） → OpenThread 协议栈功能（stack features）

**配置项引用（Symbol References）**：[`CONFIG_OPENTHREAD`](P246_modules_openthread_配置项参考_1.md#CONFIG_OPENTHREAD)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_1`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_1)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_2`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_2)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_3`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_3)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_3_1)、[`CONFIG_OPENTHREAD_THREAD_VERSION_1_4`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_THREAD_VERSION_1_4)。

<!-- kconfig-navigation -->

[上一章](P246_modules_openthread_配置项参考_1.md) · [返回大纲](大纲.md) · [下一章](P248_modules_openthread_配置项参考_3.md)
