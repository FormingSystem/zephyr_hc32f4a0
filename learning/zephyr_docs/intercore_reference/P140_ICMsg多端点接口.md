---
id: learning.zephyr-docs.intercore_reference.icmsgref-140
title: ICMsg多端点接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__me__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第140章\_ICMsg多端点接口

原文：[group__ipc__icmsg__me__api](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__icmsg__me__api.html)。读取日期：2026-10-13，`latest`。

本页介绍 ICMsg 核间消息传递（Inter-core Messaging）库的多端点扩展（Multi-endpoint Extension，ME）。IPC 指处理器间通信（Inter-Processor Communication），API 指应用程序编程接口（Application Programming Interface）。

头文件为`zephyr/ipc/icmsg_me.h`。底层配置为[`icmsg_config_t`](P136_ICMsg配置结构.md)，多端点运行时数据为[`icmsg_me_data_t`](P141_ICMsg多端点运行时结构.md)。事件回调和端点配置分别使用[`ipc_service_cb`](P112_IPC服务回调结构.md)和[`ipc_ept_cfg`](P114_IPC服务端点配置.md)。

## 140.1\_端点标识类型

```c
typedef uint8_t icmsg_me_ept_id_t;
```

`icmsg_me_ept_id_t`是端点标识（Endpoint ID）类型，底层类型`uint8_t`为8位无符号整数。原页没有额外类型说明。[源码](P143_ICMsg多端点完整头文件.md)的注释要求：若标识改用超过1字节，必须考虑字节序（Endianness）。

下文参数方向`in`、`out`、`in,out`分别表示输入、输出、输入／输出；`other`表示依赖模块返回的其他错误码。运行时数据的初始化和存活要求在各接口中完整保留。

## 140.2\_初始化多端点实例


```c
int icmsg_me_init(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data);
```

初始化多端点实例。此函数预期在系统初始化期间调用；初始化底层 ICMsg 实例是其中一个步骤。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | 将要创建的底层 ICMsg 实例的配置参数结构 |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；**调用此函数时必须已全部填零，实例活动期间必须保留其内容** |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `other` | 来自依赖模块的其他错误码（errno） |


## 140.3\_打开多端点实例


```c
int icmsg_me_open(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data,
                  const struct ipc_service_cb *cb,
                  void *ctx);
```

打开多端点实例，使其能够与远端实例收发消息。**原文规定此函数会阻塞，直到与远端握手完成。** 预期在初始化后期调用，例如从一个可在远端握手期间安全阻塞的线程中调用。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | 底层 ICMsg 实例的配置参数结构 |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `cb` | 多端点实例发生事件时调用的回调函数结构；**实例活动期间必须保留所指向的内存** |
| 输入（in） | `ctx` | 作为参数传给回调的上下文（Context）指针 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `other` | 来自依赖模块的其他错误码（errno） |


## 140.4\_等待底层绑定


```c
void icmsg_me_wait_for_icmsg_bind(struct icmsg_me_data_t *data);
```

等待底层 ICMsg 实例调用绑定回调（Bound Callback）。此函数阻塞调用线程，直到 ICMsg 连接完成绑定；**若调用前已经绑定，则立即返回，不产生延迟**。

它用于端点握手流程，确保 ICMsg 通道已经能够传递握手消息之后，才执行端点握手。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |


## 140.5\_通知底层已绑定


```c
void icmsg_me_icmsg_bound(struct icmsg_me_data_t *data);
```

通知多端点实例：底层 ICMsg 已经完成绑定。多端点 API 用户负责实现底层 ICMsg 实例调用的各个回调；**绑定回调必须执行的动作之一，就是调用本函数**。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |


## 140.6\_分发收到的数据


```c
void icmsg_me_received_data(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                            const void *msg, size_t len);
```

通知多端点实例：已经收到某个端点的数据。多端点 API 用户负责实现底层 ICMsg 实例调用的回调。如果底层 ICMsg 收到的数据包含发给某个端点的数据帧（Data Frame），**必须调用本函数**。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `id` | 标识端点的值 |
| 输入（in） | `msg` | 从对端收到的数据帧（Data Frame），**已经去除多端点头部（Multi-endpoint Header）** |
| 输入（in） | `len` | `msg`所指数据的大小 |


## 140.7\_选择空槽位并设置配置


```c
int icmsg_me_set_empty_ept_cfg_slot(struct icmsg_me_data_t *data,
                                    const struct ipc_ept_cfg *ept_cfg,
                                    icmsg_me_ept_id_t *id);
```

把端点配置放到空闲槽位（Slot）。端点握手发起端（Handshake Initiator）必须选择一个标识，并保存完成握手和维持连接所需的端点元数据（Metadata）。此辅助函数把配置写入一个空槽位，并返回与所选槽位关联的唯一标识。

**对同一个多端点实例，此函数不可重入（Non-reentrant）。** 调用者必须通过互斥锁（Mutex）、临界区（Critical Section）、自旋锁（Spinlock）或类似机制保护调用。不同实例之间允许重入，保护范围可以限定为单个实例。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `ept_cfg` | 正在发起握手流程的端点配置数据 |
| 输出（out） | `id` | 唯一标识此端点的值 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-ENOMEM` | 没有空闲的端点配置槽位 |


## 140.8\_设置指定槽位配置


```c
int icmsg_me_set_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg *ept_cfg);
```

把端点配置写入选定槽位。端点握手跟随端（Handshake Follower）必须保存端点标识及完成握手、维持连接所需的元数据；此辅助函数把配置存入与端点标识关联的配置槽位。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `id` | 唯一标识此端点的值 |
| 输入（in） | `ept_cfg` | 正在进行握手流程的端点配置数据 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-ENOENT` | 标识超出可用槽位范围 |


## 140.9\_取得指定槽位配置


```c
int icmsg_me_get_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                         const struct ipc_ept_cfg **ept_cfg);
```

从选定槽位取得端点配置。多端点实例收到远端端点的数据时，需要根据端点标识取得相应配置，本函数即用于此目的。**若该端点配置尚未设置，返回的配置指针为`NULL`**。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `id` | 唯一标识端点的值 |
| 输入（in） | `ept_cfg` | 给定标识对应端点的配置数据；原参数方向标注问题见本节译注 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-ENOENT` | 标识超出可用槽位范围 |

译注：原参数表将`ept_cfg`标成`[in]`，但本函数用于取得配置，声明为双重指针`const struct ipc_ept_cfg **`，正文也规定未设置时返回空指针。本页保留原表方向并指出这一矛盾；调用后检查的是`*ept_cfg`。


## 140.10\_清空指定槽位配置


```c
void icmsg_me_reset_ept_cfg(struct icmsg_me_data_t *data, icmsg_me_ept_id_t id);
```

清空选定端点槽位的配置。握手失败或端点断开连接后，应腾空该端点的配置槽位，本函数即用于此目的。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `id` | 唯一标识端点的值 |


## 140.11\_发送端点消息


```c
int icmsg_me_send(const struct icmsg_config_t *conf,
                  struct icmsg_me_data_t *data, icmsg_me_ept_id_t id,
                  const void *msg, size_t len);
```

向远端多端点实例的指定端点发送消息。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `conf` | 底层 ICMsg 实例的配置参数结构 |
| 输入／输出（in,out） | `data` | 多端点实例的运行时数据结构；由`icmsg_me_init()`初始化，**实例活动期间必须保留其内容** |
| 输入（in） | `id` | 要使用的端点标识 |
| 输入（in） | `msg` | 包含待发送数据的缓冲区指针 |
| 输入（in） | `len` | `msg`缓冲区中的数据大小 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功 |
| `-EBADMSG` | 请求发送的数据过大 |
| `other` | 来自依赖模块的其他错误码（errno） |

返回值译注：本页原文写成功返回`0`，底层`icmsg_send()`则写返回已发送字节数。两项接口的原返回约定分别保留，不相互替换。

---

[上一章：ICMsg完整头文件](P139_ICMsg完整头文件.md) · [下一章：ICMsg多端点运行时结构](P141_ICMsg多端点运行时结构.md) · [返回大纲](大纲.md)
