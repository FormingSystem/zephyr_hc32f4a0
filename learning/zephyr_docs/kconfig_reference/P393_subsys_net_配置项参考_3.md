---
id: learning.zephyr-docs.kconfig-reference.page-393
title: "`subsys/net`配置项参考（3/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第393章\_`subsys/net`配置项参考（3/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LWM2M_DEVICE_ERROR_CODE_MAX"></a>

## 393.1 `CONFIG_LWM2M_DEVICE_ERROR_CODE_MAX`

**提示（Prompt）**：设备对象可保存的错误码数量上限

**说明（Help）**

设置设备对象（device object）可保存的错误码数量，达到上限后忽略新值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:450`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L450)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_DEVICE_ERROR_CODE_SETTINGS"></a>

## 393.2 `CONFIG_LWM2M_DEVICE_ERROR_CODE_SETTINGS`

**提示（Prompt）**：通过 settings 跨设备复位保存错误码

**说明（Help）**

将设备错误码列表保存在设置子系统（settings）中，确保设备复位后仍可将列表传给 LwM2M 服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SETTINGS && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:434`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L434)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_DEVICE_EXT_DEV_INFO_MAX"></a>

## 393.3 `CONFIG_LWM2M_DEVICE_EXT_DEV_INFO_MAX`

**提示（Prompt）**：设备对象可保存的外部设备信息数量上限

**说明（Help）**

设置设备对象（device object）可保存的外部设备信息（external device info）数量，达到上限后忽略新值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_DEVICE_PWRSRC_MAX"></a>

## 393.4 `CONFIG_LWM2M_DEVICE_PWRSRC_MAX`

**提示（Prompt）**：设备电源记录数量上限（power source records）

**说明（Help）**

设置设备可保存的电源数据（power source data）数量上限，通过设备（Device）对象的 `/3/0/6`、`/3/0/7` 和 `/3/0/8` 资源呈现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:441`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L441)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_DNS_SUPPORT"></a>

## 393.5 `CONFIG_LWM2M_DNS_SUPPORT`

**提示（Prompt）**：LwM2M 客户端的 DNS 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_DNS_RESOLVER
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)。

<a id="CONFIG_LWM2M_DTLS_CID"></a>

## 393.6 `CONFIG_LWM2M_DTLS_CID`

**提示（Prompt）**：DTLS 连接标识符支持（Connection Identifier）

**说明（Help）**

请求 TLS 协议栈启用 DTLS 连接标识符（Connection Identifier）。要求协议栈支持此功能，实际效果还取决于目标服务器。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_DTLS_CONNECTION_ID)。

<a id="CONFIG_LWM2M_DTLS_SUPPORT"></a>

## 393.7 `CONFIG_LWM2M_DTLS_SUPPORT`

**提示（Prompt）**：LwM2M 客户端的 DTLS 支持

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)。

<a id="CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION"></a>

## 393.8 `CONFIG_LWM2M_ENGINE_ALWAYS_REPORT_OBJ_VERSION`

**提示（Prompt）**：LwM2M 引擎始终报告对象版本（object version）

**说明（Help）**

按 LwM2M v1.0 和 v1.1 规范，版本不是 1.0 的非核心对象“必须（must）”提供版本信息，其他版本“可以（may）”提供；v1.2 规范允许客户端“始终附加对象版本信息（can always attach Object Version Information）”。启用本项即可始终报告全部对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME"></a>

## 393.9 `CONFIG_LWM2M_ENGINE_DEFAULT_LIFETIME`

**提示（Prompt）**：LwM2M 引擎默认服务器连接生存时间

**说明（Help）**

设置 LwM2M 库引擎的默认生存时间（lifetime），单位为秒，同时也是客户端可接受的最小值。服务器设置更小值时，客户端会自动提高到此值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[15, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:526`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L526)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_MAX_MESSAGES"></a>

## 393.10 `CONFIG_LWM2M_ENGINE_MAX_MESSAGES`

**提示（Prompt）**：LwM2M 引擎消息对象数量上限

**说明（Help）**

设置 LwM2M 库客户端的消息对象（message objects）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_MAX_OBSERVER"></a>

## 393.11 `CONFIG_LWM2M_ENGINE_MAX_OBSERVER`

**提示（Prompt）**：可观察 LwM2M 资源数量上限（observable resources）

**说明（Help）**

设置可加入观察通知列表（observe notification list）的资源数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[5, 200]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:343`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L343)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_MAX_PENDING"></a>

## 393.12 `CONFIG_LWM2M_ENGINE_MAX_PENDING`

**提示（Prompt）**：LwM2M 引擎待处理对象数量上限

**说明（Help）**

设置 LwM2M 库客户端的待处理对象（pending objects）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_MAX_REPLIES"></a>

## 393.13 `CONFIG_LWM2M_ENGINE_MAX_REPLIES`

**提示（Prompt）**：LwM2M 引擎回复对象数量上限

**说明（Help）**

设置 LwM2M 库客户端的回复对象（reply objects）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:337`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L337)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_ENGINE_STACK_SIZE"></a>

## 393.14 `CONFIG_LWM2M_ENGINE_STACK_SIZE`

**提示（Prompt）**：LwM2M 引擎栈大小（engine stack size）

**说明（Help）**

设置 LwM2M 库引擎的栈大小，用于处理观察（OBSERVE）和通知（NOTIFY）事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2560 if CONFIG_NET_LOG
2048
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:284`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L284)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_NET_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_LOG)。

<a id="CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE"></a>

## 393.15 `CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE`

**提示（Prompt）**：入站数据验证缓冲区大小（validation buffer）

**说明（Help）**

写操作期间，LwM2M 对已注册验证回调（validation callback）的资源，先使用验证缓冲区解码资源值，再进行验证。应设为需要验证、因而已注册验证回调的资源的预期最大大小。设为 `0` 可禁用验证支持。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:320`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L320)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_EVENT_LOG_OBJ_SUPPORT"></a>

## 393.16 `CONFIG_LWM2M_EVENT_LOG_OBJ_SUPPORT`

**提示（Prompt）**：LwM2M 事件日志对象（Event Log Object，ID 20）

**说明（Help）**

加入 LwM2M 事件日志对象（Event Log Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:719`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L719)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_PORT_NONSECURE"></a>

## 393.17 `CONFIG_LWM2M_FIRMWARE_PORT_NONSECURE`

**提示（Prompt）**：LwM2M 固件服务器非安全端口（non-secure port）

**说明（Help）**

通过 CoAP 下载 LwM2M 固件时连接的默认服务器端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5683
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_PORT_SECURE"></a>

## 393.18 `CONFIG_LWM2M_FIRMWARE_PORT_SECURE`

**提示（Prompt）**：LwM2M 固件服务器安全端口（secure port）

**说明（Help）**

通过安全 CoAP（CoAPS）下载 LwM2M 固件时连接的默认服务器端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5684
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_INSTANCE_COUNT"></a>

## 393.19 `CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_INSTANCE_COUNT`

**提示（Prompt）**：LwM2M 固件更新对象实例数量上限

**说明（Help）**

设置客户端可用的 LwM2M 固件更新（Firmware Update）对象实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:634`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L634)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 固件更新对象支持（Firmware Update，ID 5）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT"></a>

## 393.20 `CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`

**提示（Prompt）**：固件更新对象支持（Firmware Update，ID 5）

**说明（Help）**

加入 LwM2M 固件更新对象（Firmware Update Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:621`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L621)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT_MULTIPLE"></a>

## 393.21 `CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT_MULTIPLE`

**提示（Prompt）**：支持多个固件更新对象【实验性 EXPERIMENTAL】

**说明（Help）**

支持多个 LwM2M 固件更新对象（Firmware Update Object）实例。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:628`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L628)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 固件更新对象支持（Firmware Update，ID 5）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_ADDR"></a>

## 393.22 `CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_ADDR`

**提示（Prompt）**：CoAP 代理网络地址（proxy network address）

**说明（Help）**

CoAP 代理服务器（proxy server）的网络地址。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_SUPPORT && CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:656`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L656)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 固件更新对象支持（Firmware Update，ID 5） → 固件更新对象拉取支持（pull support） → 固件更新对象经 CoAP-CoAP／HTTP 代理拉取支持

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_SUPPORT)、[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_SUPPORT"></a>

## 393.23 `CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_COAP_PROXY_SUPPORT`

**提示（Prompt）**：固件更新对象经 CoAP-CoAP／HTTP 代理拉取支持

**说明（Help）**

加入经 CoAP-CoAP／HTTP 代理拉取固件文件的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_SUPPORT && CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:650`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L650)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 固件更新对象支持（Firmware Update，ID 5） → 固件更新对象拉取支持（pull support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_SUPPORT)、[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_SUPPORT"></a>

## 393.24 `CONFIG_LWM2M_FIRMWARE_UPDATE_PULL_SUPPORT`

**提示（Prompt）**：固件更新对象拉取支持（pull support）

**说明（Help）**

允许通过分块传输（block transfer）及“固件包 URI（FIRMWARE PACKAGE URI）”资源，从远程服务器拉取文件。此选项增加一个 UDP 上下文及相应数据包处理。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_HTTP_PARSER || CONFIG_HTTP_PARSER_URL) && CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:641`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L641)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 固件更新对象支持（Firmware Update，ID 5）

**配置项引用（Symbol References）**：[`CONFIG_HTTP_PARSER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER)、[`CONFIG_HTTP_PARSER_URL`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_PARSER_URL)、[`CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_FIRMWARE_UPDATE_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_DEFAULT_DEVICE_ID"></a>

## 393.25 `CONFIG_LWM2M_GATEWAY_DEFAULT_DEVICE_ID`

**提示（Prompt）**：标识桥接到 LwM2M 网关的物联网设备（IoT Device）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Node"
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:737`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L737)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_DEFAULT_DEVICE_PREFIX"></a>

## 393.26 `CONFIG_LWM2M_GATEWAY_DEFAULT_DEVICE_PREFIX`

**提示（Prompt）**：用于访问此物联网设备（IoT Device）的 LwM2M 对象（Objects）。

**说明（Help）**

默认值为 `n0`、`n1`、`n2`，依次到 `n<max instances - 1>`。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
n
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:745`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L745)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_DEFAULT_IOT_DEVICE_OBJECTS"></a>

## 393.27 `CONFIG_LWM2M_GATEWAY_DEFAULT_IOT_DEVICE_OBJECTS`

**提示（Prompt）**：包含网关暴露的对象与对象实例（Objects and Object Instances）

**说明（Help）**

使用与注册接口（Registration Interface）相同的 CoreLnk 格式，必须由网关填充。例如：

```text
  </3>;ver=1.0,</3/0>,</4>;ver=1.0,</4/0>,
  </5>;ver=1.0,</5/0>,</9>;ver=1.0,</9/0>,</3303/0>
```

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:755`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L755)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_DEVICE_ID_MAX_STR_SIZE"></a>

## 393.28 `CONFIG_LWM2M_GATEWAY_DEVICE_ID_MAX_STR_SIZE`

**提示（Prompt）**：设备 ID 最大字符串长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:741`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L741)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_IOT_DEVICE_OBJECTS_MAX_STR_SIZE"></a>

## 393.29 `CONFIG_LWM2M_GATEWAY_IOT_DEVICE_OBJECTS_MAX_STR_SIZE`

**提示（Prompt）**：物联网设备对象（IoT device objects）的最大字符串长度

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:765`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L765)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_MAX_INSTANCES"></a>

## 393.30 `CONFIG_LWM2M_GATEWAY_MAX_INSTANCES`

**提示（Prompt）**：桥接设备数量上限（bridged devices）

**说明（Help）**

设置 LwM2M 客户端可用的网关（Gateway）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:730`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L730)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT"></a>

## 393.31 `CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`

**提示（Prompt）**：LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:724`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L724)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LWM2M_GATEWAY_PREFIX_MAX_STR_SIZE"></a>

## 393.32 `CONFIG_LWM2M_GATEWAY_PREFIX_MAX_STR_SIZE`

**提示（Prompt）**：前缀最大字符串长度（prefix）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:751`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L751)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 网关对象（Gateway Object，ID 25）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_GATEWAY_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_INTERVAL"></a>

## 393.33 `CONFIG_LWM2M_INTERVAL`

**提示（Prompt）**：基于间隔的轮询模式（Interval based polling mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:171`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L171)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → LwM2M 引擎运行模式（Engine operation mode）

<a id="CONFIG_LWM2M_IPSO_ACCELEROMETER"></a>

## 393.34 `CONFIG_LWM2M_IPSO_ACCELEROMETER`

**提示（Prompt）**：IPSO 加速度计支持（Accelerometer Support）

**说明（Help）**

此对象表示 1～3 轴加速度计（accelerometer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_ACCELEROMETER_INSTANCE_COUNT"></a>

## 393.35 `CONFIG_LWM2M_IPSO_ACCELEROMETER_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 加速度计对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 加速度计（Accelerometer）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_ACCELEROMETER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 加速度计支持（Accelerometer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ACCELEROMETER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION"></a>

## 393.36 `CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION`

**提示（Prompt）**：IPSO 加速度计对象版本（object version）

**说明（Help）**

选择使用的 IPSO 加速度计（Accelerometer）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_ACCELEROMETER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0
CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:187`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L187)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 加速度计支持（Accelerometer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ACCELEROMETER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0"></a>

## 393.37 `CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_0`

**提示（Prompt）**：IPSO 加速度计对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:194`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L194)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 加速度计支持（Accelerometer Support） → IPSO 加速度计对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION)。

<a id="CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_1"></a>

## 393.38 `CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION_1_1`

**提示（Prompt）**：IPSO 加速度计对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:197`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L197)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 加速度计支持（Accelerometer Support） → IPSO 加速度计对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ACCELEROMETER_VERSION)。

<a id="CONFIG_LWM2M_IPSO_BUZZER"></a>

## 393.39 `CONFIG_LWM2M_IPSO_BUZZER`

**提示（Prompt）**：IPSO 蜂鸣器支持（Buzzer Support）

**说明（Help）**

此对象用于驱动告警装置，例如蜂鸣器（buzzer）、鸣叫器（beeper）或振动报警器（vibration alarm）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:215`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L215)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_BUZZER_INSTANCE_COUNT"></a>

## 393.40 `CONFIG_LWM2M_IPSO_BUZZER_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 蜂鸣器实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 蜂鸣器（Buzzer）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_BUZZER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 蜂鸣器支持（Buzzer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_BUZZER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_BUZZER_VERSION"></a>

## 393.41 `CONFIG_LWM2M_IPSO_BUZZER_VERSION`

**提示（Prompt）**：IPSO 蜂鸣器对象版本（object version）

**说明（Help）**

选择使用的 IPSO 蜂鸣器（Buzzer）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_BUZZER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0
CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:229`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L229)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 蜂鸣器支持（Buzzer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_BUZZER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0"></a>

## 393.42 `CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_0`

**提示（Prompt）**：IPSO 蜂鸣器对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_BUZZER_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:236`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L236)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 蜂鸣器支持（Buzzer Support） → IPSO 蜂鸣器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_BUZZER_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER_VERSION)。

<a id="CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_1"></a>

## 393.43 `CONFIG_LWM2M_IPSO_BUZZER_VERSION_1_1`

**提示（Prompt）**：IPSO 蜂鸣器对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_BUZZER_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:239`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L239)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 蜂鸣器支持（Buzzer Support） → IPSO 蜂鸣器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_BUZZER_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_BUZZER_VERSION)。

<a id="CONFIG_LWM2M_IPSO_CURRENT_SENSOR"></a>

## 393.44 `CONFIG_LWM2M_IPSO_CURRENT_SENSOR`

**提示（Prompt）**：IPSO 电流传感器支持（Current Sensor Support）

**说明（Help）**

此 IPSO 对象与电流传感器（current sensor）配合使用，报告电流测量值，并提供最小／最大测量值，以及传感器最小／最大可测量范围的资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:315`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L315)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_CURRENT_SENSOR_INSTANCE_COUNT"></a>

## 393.45 `CONFIG_LWM2M_IPSO_CURRENT_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 电流传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 电流传感器（Current Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_CURRENT_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:323`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L323)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电流传感器支持（Current Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION"></a>

## 393.46 `CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION`

**提示（Prompt）**：IPSO 电流对象版本（Current object version）

**说明（Help）**

选择使用的 IPSO 电流（Current）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_CURRENT_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:331`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L331)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电流传感器支持（Current Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0"></a>

## 393.47 `CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 电流对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:338`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L338)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电流传感器支持（Current Sensor Support） → IPSO 电流对象版本（Current object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_1"></a>

## 393.48 `CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 电流对象版本 1.1

**说明（Help）**

添加时间戳与测量质量（timestamp and measurement quality）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:341`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L341)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电流传感器支持（Current Sensor Support） → IPSO 电流对象版本（Current object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_CURRENT_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_FILLING_SENSOR"></a>

## 393.49 `CONFIG_LWM2M_IPSO_FILLING_SENSOR`

**提示（Prompt）**：IPSO 填充度传感器支持（Filling sensor Support）

**说明（Help）**

此 IPSO 对象可与超声波传感器（ultrasonic sensor）配合使用，报告容器的填充程度。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:381`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L381)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_FILLING_SENSOR_INSTANCE_COUNT"></a>

## 393.50 `CONFIG_LWM2M_IPSO_FILLING_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 填充度传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 填充度传感器（filling sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_FILLING_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:387`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L387)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 填充度传感器支持（Filling sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_FILLING_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_FILLING_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR"></a>

## 393.51 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR`

**提示（Prompt）**：IPSO 通用传感器支持（Generic Sensor Support）

**说明（Help）**

此 IPSO 对象可用于制作传感器原型（prototype a sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_INSTANCE_COUNT"></a>

## 393.52 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 通用传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 通用传感器（Generic Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:49`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L49)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_NAME"></a>

## 393.53 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_NAME`

**提示（Prompt）**：创建对象时在调试输出中显示的名称

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Generic"
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_TYPE"></a>

## 393.54 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_TYPE`

**提示（Prompt）**：传感器类型（Sensor type）

**说明（Help）**

传感器类型，例如被动红外（PIR）类型。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Generic sensor"
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION"></a>

## 393.55 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION`

**提示（Prompt）**：IPSO 通用传感器对象版本（object version）

**说明（Help）**

选择使用的 IPSO 通用传感器（Generic Sensor）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:56`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L56)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0"></a>

## 393.56 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 通用传感器对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:62`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L62)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support） → IPSO 通用传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_1"></a>

## 393.57 `CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 通用传感器对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:65`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L65)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 通用传感器支持（Generic Sensor Support） → IPSO 通用传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_GENERIC_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR"></a>

## 393.58 `CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR`

**提示（Prompt）**：IPSO 湿度传感器支持（Humidity Sensor Support）

**说明（Help）**

此 IPSO 对象可用于制作传感器原型（prototype a sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_INSTANCE_COUNT"></a>

## 393.59 `CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 湿度传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 湿度传感器（Humidity Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 湿度传感器支持（Humidity Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION"></a>

## 393.60 `CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION`

**提示（Prompt）**：IPSO 湿度传感器对象版本（object version）

**说明（Help）**

选择使用的 IPSO 湿度传感器（Humidity Sensor）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 湿度传感器支持（Humidity Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0"></a>

## 393.61 `CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 湿度传感器对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 湿度传感器支持（Humidity Sensor Support） → IPSO 湿度传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_1"></a>

## 393.62 `CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 湿度传感器对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 湿度传感器支持（Humidity Sensor Support） → IPSO 湿度传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_HUMIDITY_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_LIGHT_CONTROL"></a>

## 393.63 `CONFIG_LWM2M_IPSO_LIGHT_CONTROL`

**提示（Prompt）**：IPSO 灯光控制支持（Light Control Support）

**说明（Help）**

此对象用于控制 LED 或其他光源，支持开关灯，以及将调光设置（dimmer setting）控制在 0%～100%。可选颜色设置允许通过字符串指定所需颜色。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:158`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L158)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_LIGHT_CONTROL_INSTANCE_COUNT"></a>

## 393.64 `CONFIG_LWM2M_IPSO_LIGHT_CONTROL_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 灯光控制对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 灯光控制（Light Control）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_LIGHT_CONTROL && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:166`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L166)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 灯光控制支持（Light Control Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_LIGHT_CONTROL`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_LIGHT_CONTROL)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_MAGNETOMETER"></a>

## 393.65 `CONFIG_LWM2M_IPSO_MAGNETOMETER`

**提示（Prompt）**：IPSO 磁力计支持（Magnetometer Support）

**说明（Help）**

此对象表示 1～3 轴磁力计（magnetometer）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_MAGNETOMETER_INSTANCE_COUNT"></a>

## 393.66 `CONFIG_LWM2M_IPSO_MAGNETOMETER_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 磁力计对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 磁力计（Magnetometer）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_MAGNETOMETER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 磁力计支持（Magnetometer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_MAGNETOMETER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_MAGNETOMETER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_ONOFF_SWITCH"></a>

## 393.67 `CONFIG_LWM2M_IPSO_ONOFF_SWITCH`

**提示（Prompt）**：IPSO 开关支持（On/Off Switch Support）

**说明（Help）**

此对象与开关（On/Off switch）配合使用，报告其状态。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:257`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L257)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_ONOFF_SWITCH_INSTANCE_COUNT"></a>

## 393.68 `CONFIG_LWM2M_IPSO_ONOFF_SWITCH_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 开关对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 开关（On/Off Switch）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_ONOFF_SWITCH && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 开关支持（On/Off Switch Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION"></a>

## 393.69 `CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION`

**提示（Prompt）**：IPSO 开关对象版本（object version）

**说明（Help）**

选择使用的 IPSO 开关（On/Off Switch）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_ONOFF_SWITCH && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0
CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:270`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L270)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 开关支持（On/Off Switch Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0"></a>

## 393.70 `CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_0`

**提示（Prompt）**：IPSO 开关对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 开关支持（On/Off Switch Support） → IPSO 开关对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION)。

<a id="CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_1"></a>

## 393.71 `CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION_1_1`

**提示（Prompt）**：IPSO 开关对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:280`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L280)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 开关支持（On/Off Switch Support） → IPSO 开关对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_ONOFF_SWITCH_VERSION)。

<a id="CONFIG_LWM2M_IPSO_PRESSURE_SENSOR"></a>

## 393.72 `CONFIG_LWM2M_IPSO_PRESSURE_SENSOR`

**提示（Prompt）**：IPSO 压力传感器支持（Pressure Sensor Support）

**说明（Help）**

此 IPSO 对象可用于制作传感器原型（prototype a sensor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_INSTANCE_COUNT"></a>

## 393.73 `CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 压力传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 压力传感器（Pressure Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_PRESSURE_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 压力传感器支持（Pressure Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION"></a>

## 393.74 `CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION`

**提示（Prompt）**：IPSO 压力传感器对象版本（object version）

**说明（Help）**

选择使用的 IPSO 压力传感器（Pressure Sensor）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_PRESSURE_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:127`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L127)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 压力传感器支持（Pressure Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0"></a>

## 393.75 `CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 压力传感器对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 压力传感器支持（Pressure Sensor Support） → IPSO 压力传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_1"></a>

## 393.76 `CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 压力传感器对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:137`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L137)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 压力传感器支持（Pressure Sensor Support） → IPSO 压力传感器对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PRESSURE_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_PUSH_BUTTON"></a>

## 393.77 `CONFIG_LWM2M_IPSO_PUSH_BUTTON`

**提示（Prompt）**：IPSO 按钮支持（Push Button Support）

**说明（Help）**

此对象用于报告瞬时动作按钮（momentary action push button）的状态，并统计自上次观察（observation）以来按钮被操作的次数。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_PUSH_BUTTON_INSTANCE_COUNT"></a>

## 393.78 `CONFIG_LWM2M_IPSO_PUSH_BUTTON_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 开关对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 按钮（Push Button）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_PUSH_BUTTON && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:292`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L292)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 按钮支持（Push Button Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PUSH_BUTTON`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION"></a>

## 393.79 `CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION`

**提示（Prompt）**：IPSO 按钮对象版本（object version）

**说明（Help）**

选择使用的 IPSO 按钮（Push Button）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_PUSH_BUTTON && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0
CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:300`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L300)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 按钮支持（Push Button Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PUSH_BUTTON`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0"></a>

## 393.80 `CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_0`

**提示（Prompt）**：IPSO 按钮对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:307`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L307)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 按钮支持（Push Button Support） → IPSO 按钮对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION)。

<a id="CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_1"></a>

## 393.81 `CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION_1_1`

**提示（Prompt）**：IPSO 按钮对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:310`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L310)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 按钮支持（Push Button Support） → IPSO 按钮对象版本（object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_PUSH_BUTTON_VERSION)。

<a id="CONFIG_LWM2M_IPSO_SUPPORT"></a>

## 393.82 `CONFIG_LWM2M_IPSO_SUPPORT`

**提示（Prompt）**：IPSO 联盟智能对象支持（Alliance Smart Object Support）

**说明（Help）**

添加对 IPSO 对象的通用支持（general support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TEMP_SENSOR"></a>

## 393.83 `CONFIG_LWM2M_IPSO_TEMP_SENSOR`

**提示（Prompt）**：IPSO 温度传感器支持（Temperature Sensor Support）

**说明（Help）**

此 IPSO 对象与温度传感器（temperature sensor）配合使用，报告温度测量值，并提供最小／最大测量值，以及传感器最小／最大可测量范围的资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TEMP_SENSOR_INSTANCE_COUNT"></a>

## 393.84 `CONFIG_LWM2M_IPSO_TEMP_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 温度传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 温度传感器（Temperature Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_TEMP_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 温度传感器支持（Temperature Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TEMP_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION"></a>

## 393.85 `CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION`

**提示（Prompt）**：IPSO 温度对象版本（Temperature object version）

**说明（Help）**

选择使用的 IPSO 温度（Temperature）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_TEMP_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 温度传感器支持（Temperature Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TEMP_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0"></a>

## 393.86 `CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 温度对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 温度传感器支持（Temperature Sensor Support） → IPSO 温度对象版本（Temperature object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_1"></a>

## 393.87 `CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 温度对象版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 温度传感器支持（Temperature Sensor Support） → IPSO 温度对象版本（Temperature object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TEMP_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_TIME"></a>

## 393.88 `CONFIG_LWM2M_IPSO_TIME`

**提示（Prompt）**：IPSO 时间支持（Time Support）

**说明（Help）**

此对象表示时间源（time source），并将设备时钟与 LwM2M 服务器同步。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:144`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L144)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TIMER"></a>

## 393.89 `CONFIG_LWM2M_IPSO_TIMER`

**提示（Prompt）**：IPSO 定时器支持（Timer Support）

**说明（Help）**

此对象用于对事件／动作计时（time events/actions）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:244`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L244)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TIMER_INSTANCE_COUNT"></a>

## 393.90 `CONFIG_LWM2M_IPSO_TIMER_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 定时器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 定时器（Timer）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_TIMER && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:249`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L249)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 定时器支持（Timer Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TIMER`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TIMER)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_TIME_INSTANCE_COUNT"></a>

## 393.91 `CONFIG_LWM2M_IPSO_TIME_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 时间对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 时间（Time）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_TIME && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 时间支持（Time Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_TIME`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_TIME)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR"></a>

## 393.92 `CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR`

**提示（Prompt）**：IPSO 电压传感器支持（Voltage Sensor Support）

**说明（Help）**

此 IPSO 对象与电压传感器（voltage sensor）配合使用，报告电压测量值，并提供最小／最大测量值，以及传感器最小／最大可测量范围的资源。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:348`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L348)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_INSTANCE_COUNT"></a>

## 393.93 `CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_INSTANCE_COUNT`

**提示（Prompt）**：IPSO 电压传感器对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 IPSO 电压传感器（Voltage Sensor）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L356)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电压传感器支持（Voltage Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION"></a>

## 393.94 `CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION`

**提示（Prompt）**：IPSO 电压对象版本（Voltage object version）

**说明（Help）**

选择使用的 IPSO 电压（Voltage）对象版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR && CONFIG_LWM2M_IPSO_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0
CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电压传感器支持（Voltage Sensor Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR)、[`CONFIG_LWM2M_IPSO_SUPPORT`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0)、[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_1`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_1)。

<a id="CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0"></a>

## 393.95 `CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_0`

**提示（Prompt）**：IPSO 电压对象版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:371`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L371)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电压传感器支持（Voltage Sensor Support） → IPSO 电压对象版本（Voltage object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_1"></a>

## 393.96 `CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION_1_1`

**提示（Prompt）**：IPSO 电压对象版本 1.1

**说明（Help）**

添加时间戳与测量质量（timestamp and measurement quality）

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ipso:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ipso#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → IPSO 联盟智能对象支持（Alliance Smart Object Support） → IPSO 电压传感器支持（Voltage Sensor Support） → IPSO 电压对象版本（Voltage object version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_IPSO_VOLTAGE_SENSOR_VERSION)。

<a id="CONFIG_LWM2M_LOCATION_OBJ_SUPPORT"></a>

## 393.97 `CONFIG_LWM2M_LOCATION_OBJ_SUPPORT`

**提示（Prompt）**：位置对象支持（Location，ID 6）

**说明（Help）**

加入 LwM2M 位置对象（Location Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:664`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L664)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_LOG_ENCODE_BUFFER_ALLOCATIONS"></a>

## 393.98 `CONFIG_LWM2M_LOG_ENCODE_BUFFER_ALLOCATIONS`

**提示（Prompt）**：记录分块传输编码缓冲区的分配情况

**说明（Help）**

跟踪编码缓冲区（encode buffers）分配，以分析使用情况、优化分块上下文（block contexts）数量配置，并间接优化可用编码缓冲区数量。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_COAP_BLOCK_TRANSFER && CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:408`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L408)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_COAP_BLOCK_TRANSFER`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_COAP_BLOCK_TRANSFER)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION`](P001_kernel_配置项参考_1.md#CONFIG_MEM_SLAB_TRACE_MAX_UTILIZATION)。

<a id="CONFIG_LWM2M_LOG_LEVEL_CHOICE"></a>

## 393.99 `CONFIG_LWM2M_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LwM2M 库日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LWM2M_LOG_LEVEL_OFF
CONFIG_LWM2M_LOG_LEVEL_ERR
CONFIG_LWM2M_LOG_LEVEL_WRN
CONFIG_LWM2M_LOG_LEVEL_INF
CONFIG_LWM2M_LOG_LEVEL_DBG
CONFIG_LWM2M_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_LWM2M_LOG_LEVEL_DEFAULT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_LEVEL_DEFAULT)、[`CONFIG_LWM2M_LOG_LEVEL_OFF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_LEVEL_OFF)、[`CONFIG_LWM2M_LOG_LEVEL_ERR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_LEVEL_ERR)、[`CONFIG_LWM2M_LOG_LEVEL_WRN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_LEVEL_WRN)、[`CONFIG_LWM2M_LOG_LEVEL_INF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_LOG_LEVEL_INF)、[`CONFIG_LWM2M_LOG_LEVEL_DBG`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_DBG)。

<a id="CONFIG_LWM2M_LOG_LEVEL_DBG"></a>

## 393.100 `CONFIG_LWM2M_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P392_subsys_net_配置项参考_2.md) · [返回大纲](大纲.md) · [下一章](P394_subsys_net_配置项参考_4.md)
