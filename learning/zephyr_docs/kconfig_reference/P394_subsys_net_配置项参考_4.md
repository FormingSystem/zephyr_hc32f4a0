---
id: learning.zephyr-docs.kconfig-reference.page-394
title: "`subsys/net`配置项参考（4/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第394章\_`subsys/net`配置项参考（4/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LWM2M_LOG_LEVEL_DEFAULT"></a>

## 394.1 `CONFIG_LWM2M_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_LOG_LEVEL_ERR"></a>

## 394.2 `CONFIG_LWM2M_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_LOG_LEVEL_INF"></a>

## 394.3 `CONFIG_LWM2M_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_LOG_LEVEL_OFF"></a>

## 394.4 `CONFIG_LWM2M_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_LOG_LEVEL_WRN"></a>

## 394.5 `CONFIG_LWM2M_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → LwM2M 库日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_LOG_LEVEL_CHOICE`](P393_subsys_net_配置项参考_3.md#CONFIG_LWM2M_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_MAX_CACHED_RESOURCES"></a>

## 394.6 `CONFIG_LWM2M_MAX_CACHED_RESOURCES`

**提示（Prompt）**：可缓存资源数量上限（cached resources）

**说明（Help）**

定义可启用缓存的不同资源数量，影响引擎的静态内存占用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED"></a>

## 394.7 `CONFIG_LWM2M_MAX_NOTIFIED_NUMERICAL_RES_TRACKED`

**提示（Prompt）**：可为 gt/lt/st 跟踪上次通知值的资源数量上限

**说明（Help）**

指定为处理大于（gt）、小于（lt）和步长（st）属性，而能够跟踪上次已通知资源值的数值型 LwM2M 资源数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:473`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L473)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_NUM_ATTR"></a>

## 394.8 `CONFIG_LWM2M_NUM_ATTR`

**提示（Prompt）**：LwM2M 属性数量上限（attributes）

**说明（Help）**

设置可同时处理的 LwM2M 属性数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
20
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_NUM_BLOCK1_CONTEXT"></a>

## 394.9 `CONFIG_LWM2M_NUM_BLOCK1_CONTEXT`

**提示（Prompt）**：LwM2M Block1 上下文数量上限

**说明（Help）**

设置 CoAP 分块传输中可同时处理的 Block1 上下文（contexts）数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:417`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L417)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_NUM_OUTPUT_BLOCK_CONTEXT"></a>

## 394.10 `CONFIG_LWM2M_NUM_OUTPUT_BLOCK_CONTEXT`

**提示（Prompt）**：出站 LwM2M 消息使用的分块上下文数量上限

**说明（Help）**

将消息拆分为块进行发送时，所需 CoAP 分块上下文（block contexts）的最大数量。这限制了同时处理的、需要分块传输的消息数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_COAP_BLOCK_TRANSFER && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:400`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L400)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_COAP_BLOCK_TRANSFER`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M_COAP_BLOCK_TRANSFER)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_PEER_PORT"></a>

## 394.11 `CONFIG_LWM2M_PEER_PORT`

**提示（Prompt）**：LwM2M 服务器端口（server port）

**说明（Help）**

进行 LwM2M 通信时连接的默认服务器端口。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5683
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:190`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L190)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_PORTFOLIO_OBJ_SUPPORT"></a>

## 394.12 `CONFIG_LWM2M_PORTFOLIO_OBJ_SUPPORT`

**提示（Prompt）**：LwM2M 资料集合对象支持（Portfolio Object，ID 16）

**说明（Help）**

加入 LwM2M 资料集合对象（Portfolio Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:691`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L691)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_QUEUE_MODE_ENABLED"></a>

## 394.13 `CONFIG_LWM2M_QUEUE_MODE_ENABLED`

**提示（Prompt）**：队列模式 UDP 绑定（Queue Mode UDP binding）

**说明（Help）**

将传输绑定设为带队列模式的 UDP（UQ）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_QUEUE_MODE_NO_MSG_BUFFERING"></a>

## 394.14 `CONFIG_LWM2M_QUEUE_MODE_NO_MSG_BUFFERING`

**提示（Prompt）**：在队列模式下禁用通知与消息缓冲【实验性 EXPERIMENTAL】

**说明（Help）**

立即发送消息，而不等待下次注册更新（registration update）。并非所有服务器都支持这种方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:113`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L113)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_LWM2M_QUEUE_MODE_UPTIME"></a>

## 394.15 `CONFIG_LWM2M_QUEUE_MODE_UPTIME`

**提示（Prompt）**：指定 LwM2M 客户端在队列模式下保持在线的时间。

**说明（Help）**

指定设备向服务器发送消息后继续保持在线的时间，单位为秒。LwM2M 规范建议使用 CoAP 的 `MAX_TRANSMIT_WAIT` 参数，默认 93 秒，见 RFC 7252，但并不禁止其他值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
93
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 队列模式 UDP 绑定（Queue Mode UDP binding）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RD_CLIENT_CLOSE_SOCKET_AT_IDLE"></a>

## 394.16 `CONFIG_LWM2M_RD_CLIENT_CLOSE_SOCKET_AT_IDLE`

**提示（Prompt）**：进入接收空闲（RX idle）状态时关闭套接字

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:148`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L148)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 空闲状态下的套接字处理（Socket handling）

<a id="CONFIG_LWM2M_RD_CLIENT_ENDPOINT_NAME_MAX_LENGTH"></a>

## 394.17 `CONFIG_LWM2M_RD_CLIENT_ENDPOINT_NAME_MAX_LENGTH`

**提示（Prompt）**：客户端端点名称最大长度（endpoint name）

**说明（Help）**

默认预留 32 个十六进制数字的通用唯一标识符（UUID），再加一个空字符（NULL）的空间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
33
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:351`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L351)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RD_CLIENT_LISTEN_AT_IDLE"></a>

## 394.18 `CONFIG_LWM2M_RD_CLIENT_LISTEN_AT_IDLE`

**提示（Prompt）**：保持打开并监听（Keep open and listening）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 空闲状态下的套接字处理（Socket handling）

<a id="CONFIG_LWM2M_RD_CLIENT_MAX_RETRIES"></a>

## 394.19 `CONFIG_LWM2M_RD_CLIENT_MAX_RETRIES`

**提示（Prompt）**：指定最大注册重试次数（registration retries）

**说明（Help）**

指定通知应用发生网络故障之前的最大注册重试次数。收到通知后，应用应按具体使用场景处理，例如等待 LTE 链路重新建立。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:225`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L225)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RD_CLIENT_STOP_POLLING_AT_IDLE"></a>

## 394.20 `CONFIG_LWM2M_RD_CLIENT_STOP_POLLING_AT_IDLE`

**提示（Prompt）**：接收空闲时停止轮询套接字（RX idle）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:154`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L154)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 空闲状态下的套接字处理（Socket handling）

<a id="CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP"></a>

## 394.21 `CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP`

**提示（Prompt）**：引导配置支持（Bootstrap support）

**说明（Help）**

启用后，资源目录客户端（RD client）支持引导配置模式（bootstrap mode）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RD_CLIENT_SUSPEND_SOCKET_AT_IDLE"></a>

## 394.22 `CONFIG_LWM2M_RD_CLIENT_SUSPEND_SOCKET_AT_IDLE`

**提示（Prompt）**：接收空闲时停止轮询，仅在恢复时关闭套接字

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 空闲状态下的套接字处理（Socket handling）

<a id="CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT"></a>

## 394.23 `CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`

**提示（Prompt）**：资源时间序列数据缓存支持（Resource Time series data cache）

**说明（Help）**

启用时间序列数据存储（time series data storage），要求 `time()` 提供当前 Unix 时间戳。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_LWM2M_RW_SENML_JSON_SUPPORT || CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT) && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:235`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L235)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_RW_SENML_JSON_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RW_SENML_JSON_SUPPORT)、[`CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RW_CBOR_SUPPORT"></a>

## 394.24 `CONFIG_LWM2M_RW_CBOR_SUPPORT`

**提示（Prompt）**：CBOR 写入器支持（writer）

**说明（Help）**

加入写入简洁二进制对象表示（CBOR）数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR && CONFIG_LWM2M && CONFIG_NETWORKING
```

**被弱选择（Implied by）**

```text
CONFIG_LWM2M_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:503`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L503)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_VERSION_1_1`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION_1_1)。

<a id="CONFIG_LWM2M_RW_JSON_SUPPORT"></a>

## 394.25 `CONFIG_LWM2M_RW_JSON_SUPPORT`

**提示（Prompt）**：JSON 写入器支持（writer）

**说明（Help）**

加入写入 JSON 数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_JSON_LIBRARY && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:489`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L489)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports）

**配置项引用（Symbol References）**：[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RW_OMA_TLV_SUPPORT"></a>

## 394.26 `CONFIG_LWM2M_RW_OMA_TLV_SUPPORT`

**提示（Prompt）**：类型—长度—值数据格式（TLV）

**说明（Help）**

加入写入／解析类型—长度—值（TLV）数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**被弱选择（Implied by）**

```text
CONFIG_LWM2M_VERSION_1_0
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:484`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L484)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_VERSION_1_0`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION_1_0)。

<a id="CONFIG_LWM2M_RW_SENML_CBOR_RECORDS"></a>

## 394.27 `CONFIG_LWM2M_RW_SENML_CBOR_RECORDS`

**提示（Prompt）**：打包进 CBOR 二进制数据的 SenML 记录数量上限

**说明（Help）**

生成编码器和解码器时，CBOR 库要求指定记录数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:516`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L516)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports） → 传感器测量列表 CBOR 写入器支持（SenML CBOR writer）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT"></a>

## 394.28 `CONFIG_LWM2M_RW_SENML_CBOR_SUPPORT`

**提示（Prompt）**：传感器测量列表 CBOR 写入器支持（SenML CBOR writer）

**说明（Help）**

加入写入传感器测量列表（SenML）CBOR 数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZCBOR && CONFIG_ZCBOR_CANONICAL && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:509`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L509)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports）

**配置项引用（Symbol References）**：[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)、[`CONFIG_ZCBOR_CANONICAL`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR_CANONICAL)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_RW_SENML_JSON_SUPPORT"></a>

## 394.29 `CONFIG_LWM2M_RW_SENML_JSON_SUPPORT`

**提示（Prompt）**：传感器测量列表 JSON 数据格式（SENML JSON）

**说明（Help）**

加入写入／解析 SENML JSON 数据的支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_BASE64 && CONFIG_JSON_LIBRARY && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:496`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L496)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内容格式支持（Content format supports）

**配置项引用（Symbol References）**：[`CONFIG_BASE64`](P197_lib_配置项参考_1.md#CONFIG_BASE64)、[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY"></a>

## 394.30 `CONFIG_LWM2M_SECONDS_TO_UPDATE_EARLY`

**提示（Prompt）**：LwM2M 注册更新在超时前的提前发送时间

**说明（Help）**

引擎在注册超时前多少秒发送 LwM2M 注册更新（Registration Update）。在窄带物联网（NB-IoT）等往返时间（round trip time）较长的网络中，可能需要增大此值，以便响应在超时前到达。

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
[1, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:545`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L545)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SECURITY_DTLS_TLS_CIPHERSUITE_MAX"></a>

## 394.31 `CONFIG_LWM2M_SECURITY_DTLS_TLS_CIPHERSUITE_MAX`

**提示（Prompt）**：DTLS／TLS 密码套件资源实例数量上限

**说明（Help）**

设置 LwM2M 1.1 定义的安全对象（security object）中相应资源实例数量上限，影响资源 `0/X/16`，其中 `X` 是对象实例编号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_1 && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:364`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L364)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_1`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_1)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SECURITY_INSTANCE_COUNT"></a>

## 394.32 `CONFIG_LWM2M_SECURITY_INSTANCE_COUNT`

**提示（Prompt）**：LwM2M 安全对象实例数量上限

**说明（Help）**

设置客户端可用的 LwM2M 安全（Security）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2 if CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP
1
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:374`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L374)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP)。

<a id="CONFIG_LWM2M_SECURITY_KEY_SIZE"></a>

## 394.33 `CONFIG_LWM2M_SECURITY_KEY_SIZE`

**提示（Prompt）**：安全密钥资源缓冲区大小（security key resources）

**说明（Help）**

设置安全对象实例中密钥资源的大小，包括预共享密钥（pre-shared key）或公钥（public key）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:357`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L357)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_0"></a>

## 394.34 `CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_0`

**提示（Prompt）**：安全对象版本 1.0（Security object）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 安全对象版本（Security object version）

<a id="CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_1"></a>

## 394.35 `CONFIG_LWM2M_SECURITY_OBJECT_VERSION_1_1`

**提示（Prompt）**：安全对象版本 1.1（Security object）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:48`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L48)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 安全对象版本（Security object version）

<a id="CONFIG_LWM2M_SEND_SCHEDULER"></a>

## 394.36 `CONFIG_LWM2M_SEND_SCHEDULER`

**提示（Prompt）**：LwM2M 发送调度辅助对象（send scheduler helper，10523/10524）

**说明（Help）**

启用可选的发送调度扩展（send scheduler extension），通过厂商对象在缓存资源基础上配置采样规则、缓冲区限制及 SEND 触发策略。需要 LwM2M 1.1 SEND 支持和资源数据缓存。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_VERSION_1_1 && CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:263`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L263)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_VERSION_1_1`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION_1_1)、[`CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RESOURCE_DATA_CACHE_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE"></a>

## 394.37 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：LwM2M 发送调度辅助模块日志级别

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_LWM2M_SEND_SCHEDULER && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_OFF
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_ERR
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_WRN
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_INF
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DBG
CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_LWM2M_SEND_SCHEDULER`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_OFF`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_OFF)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_ERR`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_ERR)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_WRN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_WRN)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_INF`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_INF)、[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DBG`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DBG)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DBG"></a>

## 394.38 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT"></a>

## 394.39 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_ERR"></a>

## 394.40 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_INF"></a>

## 394.41 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_OFF"></a>

## 394.42 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_WRN"></a>

## 394.43 `CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → 资源时间序列数据缓存支持（Resource Time series data cache） → LwM2M 发送调度辅助对象（send scheduler helper，10523/10524） → LwM2M 发送调度辅助模块日志级别

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SEND_SCHEDULER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL"></a>

## 394.44 `CONFIG_LWM2M_SERVER_BOOTSTRAP_ON_FAIL`

**提示（Prompt）**：注册失败时执行引导配置（Bootstrap on Registration Failure）

**说明（Help）**

设为 true 后，LwM2M 客户端在注册失败时尝试重新进行引导配置（re-bootstrap）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:555`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L555)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SERVER_DEFAULT_PMAX"></a>

## 394.45 `CONFIG_LWM2M_SERVER_DEFAULT_PMAX`

**提示（Prompt）**：默认服务器记录 PMAX

**说明（Help）**

客户端两次通知之间允许等待的默认最长时间，单位为秒。该时间到期时，必须发送通知。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:217`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L217)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SERVER_DEFAULT_PMIN"></a>

## 394.46 `CONFIG_LWM2M_SERVER_DEFAULT_PMIN`

**提示（Prompt）**：默认服务器记录 PMIN

**说明（Help）**

客户端两次通知之间必须等待的默认最短时间，单位为秒。如果此期间有资源需要通知，则必须等时间结束后发送。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:208`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L208)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SERVER_DEFAULT_SSID"></a>

## 394.47 `CONFIG_LWM2M_SERVER_DEFAULT_SSID`

**提示（Prompt）**：使用 lwm2m-client 时的默认服务器 SSID，用于访问控制

**说明（Help）**

未启用引导配置（bootstrap）时，访问控制（access control）需要默认所有者（owner）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
101
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:184`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L184)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SERVER_INSTANCE_COUNT"></a>

## 394.48 `CONFIG_LWM2M_SERVER_INSTANCE_COUNT`

**提示（Prompt）**：LwM2M 服务器对象实例数量上限

**说明（Help）**

设置客户端可用的 LwM2M 服务器（Server）实例总数，包括引导配置服务器（bootstrap server）及普通服务器。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2 if CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP
1
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:383`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L383)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RD_CLIENT_SUPPORT_BOOTSTRAP)。

<a id="CONFIG_LWM2M_SERVER_OBJECT_VERSION_1_0"></a>

## 394.49 `CONFIG_LWM2M_SERVER_OBJECT_VERSION_1_0`

**提示（Prompt）**：服务器对象版本 1.0（Server object）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 服务器对象版本（Server object version）

<a id="CONFIG_LWM2M_SERVER_OBJECT_VERSION_1_1"></a>

## 394.50 `CONFIG_LWM2M_SERVER_OBJECT_VERSION_1_1`

**提示（Prompt）**：服务器对象版本 1.1（Server object）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 服务器对象版本（Server object version）

<a id="CONFIG_LWM2M_SHELL"></a>

## 394.51 `CONFIG_LWM2M_SHELL`

**提示（Prompt）**：LwM2M 命令行工具（shell utilities）

**说明（Help）**

启用命令行模块（shell module），向控制台提供 `send` 等 LwM2M 命令。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_SHELL
CONFIG_CRC
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:561`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L561)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL)、[`CONFIG_CRC`](P336_subsys_crc_配置项参考.md#CONFIG_CRC)。

<a id="CONFIG_LWM2M_SWMGMT_MAX_INSTANCE_COUNT"></a>

## 394.52 `CONFIG_LWM2M_SWMGMT_MAX_INSTANCE_COUNT`

**提示（Prompt）**：对象实例数量上限（object instances）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:675`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L675)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 软件管理对象支持（Software Management，ID 9）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT"></a>

## 394.53 `CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT`

**提示（Prompt）**：软件管理对象支持（Software Management，ID 9）

**说明（Help）**

加入 LwM2M 软件管理对象（Software Management Object）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:669`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L669)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SWMGMT_PACKAGE_NAME_LEN"></a>

## 394.54 `CONFIG_LWM2M_SWMGMT_PACKAGE_NAME_LEN`

**提示（Prompt）**：软件管理对象名称字符串的最大大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:680`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L680)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 软件管理对象支持（Software Management，ID 9）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SWMGMT_PACKAGE_URI_LEN"></a>

## 394.55 `CONFIG_LWM2M_SWMGMT_PACKAGE_URI_LEN`

**提示（Prompt）**：固件及软件管理对象 URI 字符串的最大大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
128
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:424`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L424)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 内存与缓冲区大小配置（Memory and buffer size configuration）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_SWMGMT_PACKAGE_VERSION_LEN"></a>

## 394.56 `CONFIG_LWM2M_SWMGMT_PACKAGE_VERSION_LEN`

**提示（Prompt）**：软件管理对象版本字符串的最大大小

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:685`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L685)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 软件管理对象支持（Software Management，ID 9）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_SWMGMT_OBJ_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_TICKLESS"></a>

## 394.57 `CONFIG_LWM2M_TICKLESS`

**提示（Prompt）**：无周期时钟节拍运行模式（Tickless operation mode）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ZVFS_EVENTFD && <choice>
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features） → LwM2M 引擎运行模式（Engine operation mode）

**配置项引用（Symbol References）**：[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)。

<a id="CONFIG_LWM2M_TLS_SESSION_CACHING"></a>

## 394.58 `CONFIG_LWM2M_TLS_SESSION_CACHING`

**提示（Prompt）**：TLS 会话缓存（session caching）

**说明（Help）**

仅在 TLS 库支持此功能时启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:120`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L120)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 引擎功能（Engine features）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_BATTERY"></a>

## 394.59 `CONFIG_LWM2M_UCIFI_BATTERY`

**提示（Prompt）**：uCIFI 电池监控支持（Battery Monitor，3411）

**说明（Help）**

uCIFI 电池对象（battery object）提供监控电池电量和活动状态的属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_BATTERY_INSTANCE_COUNT"></a>

## 394.60 `CONFIG_LWM2M_UCIFI_BATTERY_INSTANCE_COUNT`

**提示（Prompt）**：uCIFI 电池对象实例数量上限

**说明（Help）**

设置 LwM2M 客户端可用的 uCIFI 电池（Battery）实例总数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_BATTERY && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 电池监控支持（Battery Monitor，3411）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_BATTERY`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_BATTERY)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN"></a>

## 394.61 `CONFIG_LWM2M_UCIFI_LPWAN`

**提示（Prompt）**：uCIFI 低功耗广域网支持（LPWAN，3412）

**说明（Help）**

uCIFI 低功耗广域网（Low-Power Wide Area Networks，LPWAN）对象提供监控和维护这些网络的属性。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_INSTANCE_COUNT"></a>

## 394.62 `CONFIG_LWM2M_UCIFI_LPWAN_INSTANCE_COUNT`

**提示（Prompt）**：uCIFI LPWAN 对象实例数量上限

**说明（Help）**

设置允许的低功耗广域网（LPWAN）实例数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 4]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_IPV4_ADDRESS_MAX"></a>

## 394.63 `CONFIG_LWM2M_UCIFI_LPWAN_IPV4_ADDRESS_MAX`

**提示（Prompt）**：IPv4 地址数量上限

**说明（Help）**

设置此对象可存储的、分配给设备的 IPv4 地址数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:43`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L43)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_IPV6_ADDRESS_MAX"></a>

## 394.64 `CONFIG_LWM2M_UCIFI_LPWAN_IPV6_ADDRESS_MAX`

**提示（Prompt）**：IPv6 地址数量上限

**说明（Help）**

设置此对象可存储的、分配给设备的 IPv6 地址数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:51`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L51)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_MULTICAST_GRP_ADDRESS_MAX"></a>

## 394.65 `CONFIG_LWM2M_UCIFI_LPWAN_MULTICAST_GRP_ADDRESS_MAX`

**提示（Prompt）**：组播组地址数量上限（multicast group addresses）

**说明（Help）**

设置此对象可存储的组播组地址数量上限，设备应接受发往这些组的入站消息及／或命令。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:84`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L84)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_MULTICAST_GRP_KEY_MAX"></a>

## 394.66 `CONFIG_LWM2M_UCIFI_LPWAN_MULTICAST_GRP_KEY_MAX`

**提示（Prompt）**：组播组密钥数量上限（multicast group keys）

**说明（Help）**

设置此对象可存储的安全密钥数量上限，例如 AES128 密钥。这些密钥与其他组成员共享，用于加入组播组（multicast group）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:93`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L93)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_NETWORK_ADDRESS_MAX"></a>

## 394.67 `CONFIG_LWM2M_UCIFI_LPWAN_NETWORK_ADDRESS_MAX`

**提示（Prompt）**：网络地址数量上限（network addresses）

**说明（Help）**

设置此对象可存储的、分配给设备的低功耗广域网（LPWAN）网络地址数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:59`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L59)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_PEER_ADDRESS_MAX"></a>

## 394.68 `CONFIG_LWM2M_UCIFI_LPWAN_PEER_ADDRESS_MAX`

**提示（Prompt）**：对等节点地址数量上限（peer node addresses）

**说明（Help）**

设置此对象可存储的对等节点低功耗广域网（LPWAN）地址数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 64]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_LPWAN_SECONDARY_NETWORK_ADDRESS_MAX"></a>

## 394.69 `CONFIG_LWM2M_UCIFI_LPWAN_SECONDARY_NETWORK_ADDRESS_MAX`

**提示（Prompt）**：次级网络地址数量上限（secondary network addresses）

**说明（Help）**

设置此对象可存储的次级地址数量上限，这些地址用于在设备所属的 LPWAN 网络上与设备通信。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M_UCIFI_LPWAN && CONFIG_LWM2M_UCIFI_SUPPORT && CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 20]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → uCIFI 联盟对象支持（Alliance Object Support） → uCIFI 低功耗广域网支持（LPWAN，3412）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_UCIFI_LPWAN`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_LPWAN)、[`CONFIG_LWM2M_UCIFI_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_UCIFI_SUPPORT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UCIFI_SUPPORT"></a>

## 394.70 `CONFIG_LWM2M_UCIFI_SUPPORT`

**提示（Prompt）**：uCIFI 联盟对象支持（Alliance Object Support）

**说明（Help）**

添加对 uCIFI 对象的通用支持（general support）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig.ucifi:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig.ucifi#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_UPDATE_PERIOD"></a>

## 394.71 `CONFIG_LWM2M_UPDATE_PERIOD`

**提示（Prompt）**：LwM2M 引擎更新周期（update period）

**说明（Help）**

从上次更新或注册到发送下次更新消息的时间间隔，使修改生存时间（lifetime）不会影响更新周期。设为 `0` 时，由 `LWM2M_SECONDS_TO_UPDATE_EARLY` 与生存时间决定发送时间。同时设置两种值时，采用较短周期。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 4294967295]
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:535`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L535)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_LWM2M_VERSION"></a>

## 394.72 `CONFIG_LWM2M_VERSION`

**提示（Prompt）**：LwM2M 协议版本（protocol version）

**说明（Help）**

选择所使用的 LwM2M 协议版本。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LWM2M && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_LWM2M_VERSION_1_0
```

**可选项（Choices）**

```text
CONFIG_LWM2M_VERSION_1_0
CONFIG_LWM2M_VERSION_1_1
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LWM2M_VERSION_1_0`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION_1_0)、[`CONFIG_LWM2M_VERSION_1_1`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION_1_1)。

<a id="CONFIG_LWM2M_VERSION_1_0"></a>

## 394.73 `CONFIG_LWM2M_VERSION_1_0`

**提示（Prompt）**：LwM2M 版本 1.0

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_VERSION>
```

**弱选择（Implies）**

```text
CONFIG_LWM2M_RW_OMA_TLV_SUPPORT
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:27`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L27)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 协议版本（protocol version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_VERSION`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION)、[`CONFIG_LWM2M_RW_OMA_TLV_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RW_OMA_TLV_SUPPORT)。

<a id="CONFIG_LWM2M_VERSION_1_1"></a>

## 394.74 `CONFIG_LWM2M_VERSION_1_1`

**提示（Prompt）**：LwM2M 版本 1.1

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LWM2M_VERSION>
```

**弱选择（Implies）**

```text
CONFIG_LWM2M_RW_CBOR_SUPPORT
CONFIG_ZCBOR
```

**定义位置（Location）**：[`subsys/net/lib/lwm2m/Kconfig:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/lwm2m/Kconfig#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 开放移动联盟轻量级机器到机器协议栈（OMA LwM2M） → 协议版本（Protocol versions） → LwM2M 协议版本（protocol version）

**配置项引用（Symbol References）**：[`CONFIG_LWM2M_VERSION`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_VERSION)、[`CONFIG_LWM2M_RW_CBOR_SUPPORT`](P394_subsys_net_配置项参考_4.md#CONFIG_LWM2M_RW_CBOR_SUPPORT)、[`CONFIG_ZCBOR`](P254_modules_zcbor_配置项参考.md#CONFIG_ZCBOR)。

<a id="CONFIG_MCP_ALLOC_HEAP"></a>

## 394.75 `CONFIG_MCP_ALLOC_HEAP`

**提示（Prompt）**：按需堆分配（Heap allocation, on-demand）

**说明（Help）**

MCP 使用 `k_malloc`／`k_free` 分配和释放内存，按需分配，但长期运行可能产生内存碎片（fragmentation）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_ALLOC_METHOD>
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 内存分配方式（memory allocation method）

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_METHOD`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_METHOD)。

<a id="CONFIG_MCP_ALLOC_METHOD"></a>

## 394.76 `CONFIG_MCP_ALLOC_METHOD`

**提示（Prompt）**：MCP 内存分配方式（memory allocation method）

**说明（Help）**

选择模型上下文协议（MCP）内部结构的内存分配方式。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MCP_ALLOC_SLAB
```

**可选项（Choices）**

```text
CONFIG_MCP_ALLOC_SLAB
CONFIG_MCP_ALLOC_HEAP
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:61`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L61)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCP_ALLOC_SLAB`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_SLAB)、[`CONFIG_MCP_ALLOC_HEAP`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_HEAP)。

<a id="CONFIG_MCP_ALLOC_SLAB"></a>

## 394.77 `CONFIG_MCP_ALLOC_SLAB`

**提示（Prompt）**：内存块池，确定性预分配（Memory slabs）

**说明（Help）**

MCP 使用内存块池（memory slabs）分配内存，提供确定的分配时间且不产生碎片，但启动时预先分配内存。无论实际负载如何，内存使用量固定。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_ALLOC_METHOD>
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 内存分配方式（memory allocation method）

**配置项引用（Symbol References）**：[`CONFIG_MCP_ALLOC_METHOD`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_ALLOC_METHOD)。

<a id="CONFIG_MCP_CLIENT_TIMEOUT_MS"></a>

## 394.78 `CONFIG_MCP_CLIENT_TIMEOUT_MS`

**提示（Prompt）**：客户端连接最大空闲时间（毫秒）

**说明（Help）**

允许客户端保持空闲的最长时间，默认 30000 毫秒。译注：原文在 “between” 后未补充对象，这里不补写其具体间隔边界。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:278`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L278)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HEALTH_CHECK_INTERVAL_MS"></a>

## 394.79 `CONFIG_MCP_HEALTH_CHECK_INTERVAL_MS`

**提示（Prompt）**：健康监控检查间隔（毫秒，health monitor）

**说明（Help）**

健康监控线程检查执行上下文（execution contexts）是否超时的间隔，默认 3000 毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:250`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L250)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HEALTH_MONITOR_STACK_SIZE"></a>

## 394.80 `CONFIG_MCP_HEALTH_MONITOR_STACK_SIZE`

**提示（Prompt）**：MCP 健康监控线程栈大小

**说明（Help）**

健康监控线程的栈大小，单位为字节。该线程仅进行简单的周期检查，栈需求很小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:242`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L242)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HTTP_ENDPOINT"></a>

## 394.81 `CONFIG_MCP_HTTP_ENDPOINT`

**提示（Prompt）**：MCP 端点路径（endpoint path）

**说明（Help）**

MCP 端点（endpoint）的 URL 路径。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"/mcp"
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:330`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L330)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HTTP_LOG_ADDRESS"></a>

## 394.82 `CONFIG_MCP_HTTP_LOG_ADDRESS`

**提示（Prompt）**：启动时记录 HTTP 服务器地址

**说明（Help）**

分配到 IP 地址后，记录可访问的 HTTP 服务器地址。适用于事先不知道地址的 DHCP 配置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
CONFIG_NET_MGMT_EVENT
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:365`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L365)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT)、[`CONFIG_NET_MGMT_EVENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_MGMT_EVENT)。

<a id="CONFIG_MCP_HTTP_POLL_INTERVAL_MS"></a>

## 394.83 `CONFIG_MCP_HTTP_POLL_INTERVAL_MS`

**提示（Prompt）**：响应就绪轮询间隔（毫秒）

**说明（Help）**

HTTP 层通过轮询循环检查响应是否就绪，每次迭代结束时休眠 `MCP_HTTP_POLL_INTERVAL_MS`。原文称，若在 `MCP_HTTP_POLL_INTERVAL_MS` 限制内未找到响应，则切换到服务器发送事件（SSE）模式。为保证计时准确，`MCP_HTTP_TIMEOUT_MS` 必须能被 `MCP_HTTP_POLL_INTERVAL_MS` 整除。

译注：原文此段用轮询间隔描述切换限制，而相邻超时项以 `MCP_HTTP_TIMEOUT_MS` 描述总体等待时间；这里保留标识符差异，实际切换条件应对照实现。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HTTP_PORT"></a>

## 394.84 `CONFIG_MCP_HTTP_PORT`

**提示（Prompt）**：HTTP 服务器端口（server port）

**说明（Help）**

MCP HTTP 服务器的端口号。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8080
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:324`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L324)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HTTP_SSE_RETRY_MS"></a>

## 394.85 `CONFIG_MCP_HTTP_SSE_RETRY_MS`

**提示（Prompt）**：SSE 重新连接重试间隔（毫秒）

**说明（Help）**

通过服务器发送事件（SSE）的 `retry` 字段传给客户端的时间间隔，单位为毫秒。在此实现中，重试机制指示客户端多久通过 GET 请求轮询新响应。客户端收到带此值的 SSE 事件后，应等待相应时间，再发送下一个 GET 请求以检查其他服务器响应。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:354`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L354)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_HTTP_TIMEOUT_MS"></a>

## 394.86 `CONFIG_MCP_HTTP_TIMEOUT_MS`

**提示（Prompt）**：HTTP 请求超时（毫秒，request timeout）

**说明（Help）**

HTTP 请求从阻塞模式切换到轮询模式之前的最长等待时间，单位为毫秒。阻塞模式直接向客户端响应；轮询模式使用服务器发送事件（SSE），客户端必须按 `MCP_HTTP_SSE_RETRY_MS` 间隔发送 GET 请求。为保证计时准确，`MCP_HTTP_TIMEOUT_MS` 必须能被 `MCP_HTTP_POLL_INTERVAL_MS` 整除。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_HTTP && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
500
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:336`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L336)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_MAX_CLIENTS"></a>

## 394.87 `CONFIG_MCP_MAX_CLIENTS`

**提示（Prompt）**：每个服务器的客户端数量上限

**说明（Help）**

设置服务器能够同时处理的客户端数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_MAX_CLIENT_REQUESTS"></a>

## 394.88 `CONFIG_MCP_MAX_CLIENT_REQUESTS`

**提示（Prompt）**：MCP 请求队列大小（request queue size）

**说明（Help）**

可排队等待处理的 MCP 请求数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_MAX_MESSAGE_SIZE"></a>

## 394.89 `CONFIG_MCP_MAX_MESSAGE_SIZE`

**提示（Prompt）**：MCP 消息最大大小（message size）

**说明（Help）**

MCP 消息缓冲区大小，单位为字节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_MAX_TOOLS"></a>

## 394.90 `CONFIG_MCP_MAX_TOOLS`

**提示（Prompt）**：已注册工具数量上限（registered tools）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_MOCK_MAX_CLIENTS"></a>

## 394.91 `CONFIG_MCP_MOCK_MAX_CLIENTS`

**提示（Prompt）**：模拟客户端数量上限（mock clients）

**说明（Help）**

模拟传输测试（mock transport testing）可用的客户端数量上限。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_TRANSPORT_MOCK && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:377`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L377)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_TRANSPORT_MOCK`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_MOCK)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_REQUEST_WORKERS"></a>

## 394.92 `CONFIG_MCP_REQUEST_WORKERS`

**提示（Prompt）**：MCP 请求工作线程数量（worker threads）

**说明（Help）**

处理入站 MCP 请求的工作线程数量。增加工作线程可改善客户端请求的并发处理能力。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:37`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L37)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_REQUEST_WORKER_STACK_SIZE"></a>

## 394.93 `CONFIG_MCP_REQUEST_WORKER_STACK_SIZE`

**提示（Prompt）**：MCP 请求工作线程栈大小

**说明（Help）**

每个请求工作线程的栈大小，单位为字节。工作线程本身较轻量，但会调用用户提供的工具回调（tool callbacks），其栈需求可能不同。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:45`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L45)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER"></a>

## 394.94 `CONFIG_MCP_SERVER`

**提示（Prompt）**：模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**说明（Help）**

支持模型上下文协议服务器（MCP Server）功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_EXPERIMENTAL
CONFIG_JSON_LIBRARY
CONFIG_UUID
CONFIG_UUID_V4
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)、[`CONFIG_JSON_LIBRARY`](P197_lib_配置项参考_1.md#CONFIG_JSON_LIBRARY)、[`CONFIG_UUID`](P199_lib_配置项参考_3.md#CONFIG_UUID)、[`CONFIG_UUID_V4`](P199_lib_配置项参考_3.md#CONFIG_UUID_V4)。

<a id="CONFIG_MCP_SERVER_COUNT"></a>

## 394.95 `CONFIG_MCP_SERVER_COUNT`

**提示（Prompt）**：MCP 服务器实例数量（server instances）

**说明（Help）**

能够同时创建并运行的 MCP 服务器实例数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 10]
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_INSTRUCTIONS"></a>

## 394.96 `CONFIG_MCP_SERVER_INFO_INSTRUCTIONS`

**提示（Prompt）**：在 serverInfo 中包含服务器使用说明（instructions）

**说明（Help）**

在 `serverInfo` 部分包含可选的 `instructions` 字段。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:168`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L168)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_INSTRUCTIONS_MAX_LEN"></a>

## 394.97 `CONFIG_MCP_SERVER_INFO_INSTRUCTIONS_MAX_LEN`

**提示（Prompt）**：服务器信息中使用说明的最大长度

**说明（Help）**

`serverInfo` 中服务器使用说明（instructions）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER_INFO_INSTRUCTIONS && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → 在 serverInfo 中包含服务器使用说明（instructions）

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER_INFO_INSTRUCTIONS`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER_INFO_INSTRUCTIONS)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_INSTRUCTIONS_VALUE"></a>

## 394.98 `CONFIG_MCP_SERVER_INFO_INSTRUCTIONS_VALUE`

**提示（Prompt）**：服务器使用说明（Server instructions）

**说明（Help）**

在 `serverInfo` 中报告的 MCP 服务器使用说明（instructions）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER_INFO_INSTRUCTIONS && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"This is a Zephyr-based MCP server providing tool capabilities."
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → 在 serverInfo 中包含服务器使用说明（instructions）

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER_INFO_INSTRUCTIONS`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER_INFO_INSTRUCTIONS)、[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_NAME"></a>

## 394.99 `CONFIG_MCP_SERVER_INFO_NAME`

**提示（Prompt）**：服务器名称（Server name）

**说明（Help）**

在 `serverInfo` 中报告的 MCP 服务器名称。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"Zephyr MCP Server"
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:129`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L129)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_MCP_SERVER_INFO_NAME_MAX_LEN"></a>

## 394.100 `CONFIG_MCP_SERVER_INFO_NAME_MAX_LEN`

**提示（Prompt）**：服务器信息中名称的最大长度

**说明（Help）**

`serverInfo` 中服务器名称（name）字段的最大长度。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**定义位置（Location）**：[`subsys/net/lib/mcp/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/mcp/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_MCP_SERVER`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P393_subsys_net_配置项参考_3.md) · [返回大纲](大纲.md) · [下一章](P395_subsys_net_配置项参考_5.md)
