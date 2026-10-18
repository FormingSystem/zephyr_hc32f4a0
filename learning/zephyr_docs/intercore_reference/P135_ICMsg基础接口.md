---
id: learning.zephyr-docs.intercore_reference.icmsgref-135
title: ICMsg基础接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第135章\_ICMsg基础接口

原文：[group__ipc__icmsg__api](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__api.html)。读取日期：2026-10-13，`latest`。

本页介绍 ICMsg 核间消息传递（Inter-core Messaging）库的 IPC 应用程序编程接口（Application Programming Interface，API）。IPC 指处理器间通信（Inter-Processor Communication），头文件为`zephyr/ipc/icmsg.h`。配置与运行时数据分别见[`icmsg_config_t`](P136_ICMsg配置结构.md)和[`icmsg_data_t`](P137_ICMsg运行时结构.md)，协议说明见 [ICMsg 消息后端](P093_ICMsg消息后端.md)。

实例（Instance）通过握手（Handshake）建立连接；回调（Callback）使用[`ipc_service_cb`](P112_IPC服务回调结构.md)。下文 SID 是会话标识（Session ID），`unbound()`是解绑回调；TX 为发送（Transmit），RX 为接收（Receive）。

## 135.1\_实例状态

`icmsg_state`枚举（Enumeration）的各个状态如下，发送和打开的行为按原文逐项保留。

| 枚举项 | 状态含义 | 此状态下的行为 |
| --- | --- | --- |
| `ICMSG_STATE_OFF` | 实例尚未初始化 | 发送失败；允许打开 |
| `ICMSG_STATE_INITIALIZING_SID_DISABLED` | 不进行会话握手（Session Handshake），正在初始化 | 发送失败；打开失败 |
| `ICMSG_STATE_INITIALIZING_SID_ENABLED` | 进行会话握手，等待远端确认本地会话标识（Session ID，SID） | 发送失败；允许打开，但本地会话标识会改变，远端可能收到`unbound()`解绑回调 |
| `ICMSG_STATE_INITIALIZING_SID_DETECT` | 正在初始化并检测远端是否支持会话握手；等待远端确认本地会话标识或发送魔数字节（Magic Bytes） | 发送失败；允许打开，但本地会话标识会改变，远端若支持解绑机制则可能收到`unbound()` |
| `ICMSG_STATE_DISCONNECTED` | 远端已关闭实例，本地已经发出`unbound()`回调 | 发送会被静默丢弃（Silently Discarded），因为可能仍有过时的发送请求；允许打开 |
| `ICMSG_STATE_CONNECTED_SID_DISABLED` | 已连接，但不支持会话握手 | 发送成功；打开失败 |
| `ICMSG_STATE_CONNECTED_SID_ENABLED` | 已连接，支持会话握手 | 发送成功；允许打开，此时会话改变，远端会收到`unbound()`回调 |


```c
enum icmsg_state {
        ICMSG_STATE_OFF,

        ICMSG_STATE_INITIALIZING_SID_DISABLED,

        ICMSG_STATE_INITIALIZING_SID_ENABLED,

        ICMSG_STATE_INITIALIZING_SID_DETECT,

        ICMSG_STATE_DISCONNECTED,

        /* Connected states must be at the end. */

        ICMSG_STATE_CONNECTED_SID_DISABLED,

        ICMSG_STATE_CONNECTED_SID_ENABLED,
};
```

源码注释明确要求：**已连接状态（Connected States）必须放在枚举末尾。** 上方原始枚举顺序和注释均保留。

## 135.2\_解绑模式

模式名中的`DISABLE`、`ENABLE`、`DETECT`分别表示禁用（Disable）、启用（Enable）和检测（Detect）；它们的赋值对应初始化状态。

`icmsg_unbound_mode`枚举中的三个模式直接取对应初始化状态的值；原页未给出额外描述，以下保留其完整赋值关系。

```c
enum icmsg_unbound_mode {
        ICMSG_UNBOUND_MODE_DISABLE = ICMSG_STATE_INITIALIZING_SID_DISABLED,
        ICMSG_UNBOUND_MODE_ENABLE = ICMSG_STATE_INITIALIZING_SID_ENABLED,
        ICMSG_UNBOUND_MODE_DETECT = ICMSG_STATE_INITIALIZING_SID_DETECT,
};
```


下文`in`、`out`、`in,out`是参数方向，依次为输入、输出、输入／输出；`other`表示依赖模块报告的其他错误码，原错误码标识和具体触发条件逐项保留。

## 135.3\_打开实例


```c
int icmsg_open(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const struct ipc_service_cb *cb, void *ctx);
```

打开 ICMsg 实例，以便与远端实例收发消息。**原文规定此函数会阻塞，直到与远端的握手完成。** 预期在初始化后期调用，例如从一个可在握手期间安全阻塞的线程（Thread）中调用。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | ICMsg 实例的配置参数结构 |
| 输入／输出（in,out） | `dev_data` | ICMsg 实例使用的运行时数据（Run-time Data）结构 |
| 输入（in） | `cb` | ICMsg 实例发生事件时调用的回调函数结构；**实例活动期间必须保留所指向的内存** |
| 输入（in） | `ctx` | 作为参数传给回调的上下文（Context）指针 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EALREADY` | 实例已经打开 |
| `other` | 来自依赖模块的其他错误码（errno） |


## 135.4\_关闭实例


```c
int icmsg_close(const struct icmsg_config_t *conf,
                struct icmsg_data_t *dev_data);
```

关闭 ICMsg 实例会释放该实例使用的全部资源，包括共享内存区域（Shared Memory Region）和邮箱设备（Mailbox Device）。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | 待关闭 ICMsg 实例的配置结构；**内容必须与使用`icmsg_open()`创建该实例时相同** |
| 输入／输出（in,out） | `dev_data` | ICMsg 实例使用的运行时数据（Run-time Data）结构 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `other` | 来自依赖模块的其他错误码（errno） |


## 135.5\_发送消息


```c
int icmsg_send(const struct icmsg_config_t *conf,
               struct icmsg_data_t *dev_data,
               const void *msg, size_t len);
```

向远端 ICMsg 实例发送消息。返回值表中的`Number`表示返回已发送字节数，而`other`表示来自依赖模块的其他错误码。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | ICMsg 实例的配置参数结构 |
| 输入／输出（in,out） | `dev_data` | ICMsg 实例使用的运行时数据（Run-time Data）结构 |
| 输入（in） | `msg` | 包含待发送数据的缓冲区指针 |
| 输入（in） | `len` | `msg`缓冲区中的数据大小 |

| 返回值 | 含义 |
| --- | --- |
| `Number` | 已发送字节数 |
| `-EBUSY` | 实例尚未完成与远端的握手 |
| `-ENODATA` | 请求发送的数据为空 |
| `-EBADMSG` | 请求发送的数据过大 |
| `-ENOBUFS` | 没有可用的发送缓冲区（TX Buffer） |
| `other` | 来自依赖模块的其他错误码（errno） |

译注：原文打开函数的错误码概括为“实例已经打开”时返回`-EALREADY`，而状态表允许若干启用会话握手的状态再次打开。两处原始说明均保留，不能把这一概括误读为覆盖所有状态的无条件规则。完整可见声明见[ICMsg完整头文件](P139_ICMsg完整头文件.md)。

---

[上一章：静态虚拟环常量完整头文件](P134_静态虚拟环常量完整头文件.md) · [下一章：ICMsg配置结构](P136_ICMsg配置结构.md) · [返回大纲](大纲.md)
