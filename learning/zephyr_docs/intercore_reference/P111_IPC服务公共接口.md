---
id: learning.zephyr-docs.intercore_reference.ipcsvc-111
title: IPC服务公共接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第111章\_IPC服务公共接口

原文：[group__ipc__service__api](https://docs.zephyrproject.org/latest/doxygen/html/group__ipc__service__api.html)。读取日期：2026-10-13，`latest`。

本页是处理器间通信（Inter-Processor Communication，IPC）服务的应用程序编程接口（Application Programming Interface，API），自版本2.7提供，接口版本为1.0.0。所有函数来自`zephyr/ipc/ipc_service.h`。实例（Instance）代表使用的服务设备，端点（Endpoint）承载与对端的通信；具体实现由后端（Backend）提供。

配套数据结构为[事件回调`ipc_service_cb`](P112_IPC服务回调结构.md)、[端点`ipc_ept`](P113_IPC服务端点结构.md)和[端点配置`ipc_ept_cfg`](P114_IPC服务端点配置.md)。使用流程见 [IPC 服务使用指南](P092_IPC服务使用指南.md)，完整声明见[头文件源码](P118_IPC服务完整头文件.md)。

下文 TX 表示发送（Transmit），RX 表示接收（Receive），无拷贝（No-copy）指应用直接使用通信缓冲区。参数方向`in`、`out`、`in,out`依次表示输入、输出、输入／输出；`k_timeout_t`是内核超时类型，`uint32_t`是32位无符号整数类型，`size_t`用于表示大小。返回值表中的`bytes`和`size`是返回的数量，不是额外的错误码常量。

返回值表中的`other`表示其他实现相关错误码。形如`-EINVAL`的标识是原接口的错误码（Error Code），下表逐函数解释其触发条件；保留原符号，便于与源码对应。

## 111.1\_打开实例


```c
int ipc_service_open_instance(const struct device *instance);
```

在注册新端点之前，必须先打开实例。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 要打开的实例 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例配置无效 |
| `-EIO` | 没有已注册的后端 |
| `-EALREADY` | 实例已经打开或正在打开 |
| `0` | 成功，或后端不需要此操作而没有实现它 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.2\_关闭实例


```c
int ipc_service_close_instance(const struct device *instance);
```

关闭实例。调用前必须通过`ipc_service_deregister_endpoint()`注销所有已绑定的端点。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 要关闭的实例 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例配置无效 |
| `-EIO` | 没有已注册的后端 |
| `-EALREADY` | 实例尚未打开 |
| `-EBUSY` | 仍存在尚未注销的端点 |
| `0` | 成功，或后端不需要此操作而没有实现它 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.3\_注册端点


```c
int ipc_service_register_endpoint(const struct device *instance,
                                  struct ipc_ept *ept,
                                  const struct ipc_ept_cfg *cfg);
```

把端点注册到实例，使其能够与远端设备通信。主机（Host）和远端（Remote）设备均使用同一函数注册端点。

**端点使用期间，必须让`cfg`所指向的配置变量保持存活。**

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 要注册端点的目标实例 |
| 输入（in） | `ept` | 端点对象 |
| 输入（in） | `cfg` | 端点配置 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端 |
| `-EINVAL` | 实例、端点或配置无效 |
| `-EBUSY` | 实例正忙 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.4\_注销端点


```c
int ipc_service_deregister_endpoint(struct ipc_ept *ept);
```

从所属实例中注销 IPC 端点。主机（Host）和远端（Remote）设备均使用同一函数注销端点。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 端点对象 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端 |
| `-EINVAL` | 实例、端点或配置无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBUSY` | 实例正忙 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.5\_发送数据


```c
int ipc_service_send(struct ipc_ept *ept, const void *data, size_t len);
```

通过给定的已注册端点发送数据。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 待发送缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少发送钩子（Send Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 数据无效，例如格式、长度等不正确 |
| `-EBUSY` | 实例正忙 |
| `-ENOMEM` | 没有可用内存或缓冲区 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.6\_发送关键消息


```c
int ipc_service_send_critical(struct ipc_ept *ept, const void *data, size_t len);
```

通过后端的特殊快速路径（Fast Path）发送高优先级消息，跳过通常的状态检查和忙碌检查。此接口用于崩溃报告（Crash Report）、致命错误（Fatal Error）或紧急关机信号（Emergency Shutdown Signal）等关键系统通知，即使 IPC 通道被视为忙碌或阻塞，也需要交付这些通知。

**原文警告：此函数只能用于关键系统通知。误用可能导致数据损坏或系统不稳定，且后端必须支持该操作。**

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 待发送关键消息缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少`send_critical`钩子 |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 数据无效，例如格式不正确、长度超过后端上限等 |
| `-ENOTSUP` | 后端不支持此操作 |
| `-ENOMEM` | 连关键路径（Critical Path）的缓冲区也已耗尽 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.7\_查询发送缓冲区大小


```c
int ipc_service_get_tx_buffer_size(struct ipc_ept *ept);
```

查询能够通过`ipc_service_get_tx_buffer()`取得的发送缓冲区的最大大小。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少发送钩子（Send Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 后端不支持此操作 |
| `size` | 成功时返回发送缓冲区大小 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.8\_取得发送缓冲区


```c
int ipc_service_get_tx_buffer(struct ipc_ept *ept, void **data, uint32_t *size, k_timeout_t wait);
```

取得供`ipc_service_send_nocopy()`发送的空缓冲区。应用可以直接把数据放进发送缓冲区，避免从应用缓冲区再复制一次；应用负责正确填充已分配缓冲区，并向无拷贝发送函数传入正确参数。

`size`可用于请求特定大小的缓冲区：

- 请求大小能够满足时，函数成功并分配缓冲区。
- 请求大小过大时，返回`-ENOMEM`，不分配缓冲区。
- 请求大小为`0`时，按允许的最大大小分配缓冲区。

原文说明：各情况下返回时，`size`包含所返回缓冲区的最大大小；参数和错误码说明特别指出，返回`-ENOMEM`时也通过它返回允许的最大大小。

函数成功后，缓冲区视为已分配。释放有两条路径：通过`ipc_service_send_nocopy()`发送后由后端自动释放，或对尚未发送的缓冲区调用`ipc_service_drop_tx_buffer()`。发送失败时的所有权规则见无拷贝发送一节。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输出（out） | `data` | 用于返回空发送缓冲区指针的输出参数 |
| 输入／输出（in,out） | `size` | 指向所请求发送缓冲区大小的输入／输出参数；函数返回`-ENOMEM`时，它返回允许的最大大小 |
| 输入（in） | `wait` | 等待可用发送缓冲区的超时（Timeout） |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少发送钩子（Send Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 后端不支持该操作或所指定的超时 |
| `-ENOBUFS` | 没有可用的发送缓冲区 |
| `-EALREADY` | 已经取得一个缓冲区且尚未释放 |
| `-ENOMEM` | 请求大小过大；`size`参数包含允许的最大大小 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.9\_丢弃发送缓冲区


```c
int ipc_service_drop_tx_buffer(struct ipc_ept *ept, const void *data);
```

丢弃并释放发送缓冲区。**只能丢弃通过`ipc_service_get_tx_buffer()`取得的发送缓冲区。**

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 发送缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少发送钩子（Send Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 后端不支持此功能 |
| `-EALREADY` | 缓冲区已经丢弃 |
| `-ENXIO` | 缓冲区不是通过`ipc_service_get_tx_buffer()`取得的 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.10\_无拷贝发送


```c
int ipc_service_send_nocopy(struct ipc_ept *ept, const void *data, size_t len);
```

通过指定端点发送已经由`ipc_service_get_tx_buffer()`预留的发送缓冲区。它与`ipc_service_send()`功能相当，但应用必须自行取得并填充发送缓冲区。

**调用`ipc_service_send_nocopy()`之后，发送任务不再拥有该缓冲区，不能再访问它；只有函数失败并返回错误时例外。** 失败时可以用`ipc_service_drop_tx_buffer()`丢弃该缓冲区。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 通过`ipc_service_get_tx_buffer()`取得的待发送缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少发送钩子（Send Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 数据无效，例如格式、长度等不正确 |
| `-EBUSY` | 实例正忙 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.11\_保留接收缓冲区


```c
int ipc_service_hold_rx_buffer(struct ipc_ept *ept, void *data);
```

保留接收缓冲区，使其能在接收回调（Receive Callback）之外继续使用。该操作防止缓冲区被释放回共享内存缓冲池（Shared Memory Buffer Pool）。不希望在回调内复制消息时，可以在回调中调用此函数。

**消息处理完成后，应用必须调用`ipc_service_release_rx_buffer()`释放缓冲区。**

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 要保留的接收缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少释放钩子（Release Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EALREADY` | 该数据缓冲区已经被保留 |
| `-ENOTSUP` | 后端不支持此功能 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 111.12\_释放接收缓冲区


```c
int ipc_service_release_rx_buffer(struct ipc_ept *ept, void *data);
```

释放接收缓冲区以供后续复用。后端支持时，应用可在处理完收到的消息后调用此函数，使缓冲区再次成为可复用状态。

**只能释放此前通过`ipc_service_hold_rx_buffer()`保留的接收缓冲区。**

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `ept` | 通过`ipc_service_register_endpoint()`注册的端点 |
| 输入（in） | `data` | 要释放的接收缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EIO` | 没有已注册的后端，或后端缺少释放钩子（Release Hook） |
| `-EINVAL` | 实例或端点无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EALREADY` | 该数据缓冲区已经释放 |
| `-ENOTSUP` | 后端不支持此功能 |
| `-ENXIO` | 缓冲区此前没有通过`ipc_service_hold_rx_buffer()`保留 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |

**原文用语译注：**若干缓冲区接口的`-EIO`说明统一写成缺少发送钩子（Send Hook），保留接收缓冲区接口则写成缺少释放钩子（Release Hook）。本页按原文保留这些描述，具体后端操作成员的名称见[后端操作结构](P116_IPC服务后端操作结构.md)，不把通用描述擅自替换为某个成员名。

---

[上一章：ZephyrOpenAMP静态虚拟环绑定](P110_ZephyrOpenAMP静态虚拟环绑定.md) · [下一章：IPC服务回调结构](P112_IPC服务回调结构.md) · [返回大纲](大纲.md)
