---
id: learning.zephyr-docs.intercore_reference.ipcsvc-116
title: IPC服务后端操作结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__service__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第116章\_IPC服务后端操作结构

原文：[structipc__service__backend](https://docs.zephyrproject.org/latest/doxygen/html/structipc__service__backend.html)。读取日期：2026-10-13，`latest`。

`ipc_service_backend`是 IPC 处理器间通信（Inter-Processor Communication）服务的后端配置结构（Backend Configuration Structure），用于注册期间配置后端，来自`zephyr/ipc/ipc_service_backend.h`。各成员均为函数指针，完整布局见[后端完整头文件](P120_IPC服务后端完整头文件.md)。

下文实例（Instance）用`const struct device *`表示，后端专用令牌（Backend-specific Token）用`token`传递。注册回调通过输出参数`void **token`返回令牌，其他相关回调以`void *token`接收。端点配置（Endpoint Configuration）见[`ipc_ept_cfg`](P114_IPC服务端点配置.md)。

TX 表示发送（Transmit），RX 表示接收（Receive）；`k_timeout_t`为内核超时类型，`uint32_t`为32位无符号整数类型，`size_t`用于表示大小。`in`、`out`、`in,out`依次表示输入、输出、输入／输出。以下参数、返回值属于后端回调，与[公共接口](P111_IPC服务公共接口.md)的校验和错误码说明分别保留；`bytes`和`size`表示返回的数量。

返回值表中的`other`表示其他实现相关错误码。形如`-EINVAL`的标识是原接口的错误码（Error Code），下表逐函数解释其触发条件；保留原符号，便于与源码对应。

## 116.1\_打开实例


```c
int (*open_instance)(const struct device *instance);
```

打开实例的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EALREADY` | 实例已经打开 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.2\_关闭实例


```c
int (*close_instance)(const struct device *instance);
```

关闭实例的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EALREADY` | 实例尚未初始化 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.3\_发送数据


```c
int (*send)(const struct device *instance, void *token,
                    const void *data, size_t len);
```

向端点发送数据的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 待发送缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 消息无效 |
| `-EBUSY` | 实例正忙或尚未就绪 |
| `-ENOMEM` | 没有可用内存或缓冲区 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.4\_发送关键消息


```c
int (*send_critical)(const struct device *instance, void *token,
                             const void *data, size_t len);
```

直接发送高优先级关键消息（Critical Message）的函数指针，绕过流量控制（Flow Control）、忙碌检查和正常排队机制。仅应用于崩溃报告（Crash Report）或致命错误（Fatal Error）等关键系统通知。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 待发送缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 消息无效 |
| `-ENOTSUP` | 不支持关键消息发送 |
| `-ENOMEM` | 连关键消息缓冲区也不可用 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.5\_注册端点


```c
int (*register_endpoint)(const struct device *instance,
                                 void **token,
                                 const struct ipc_ept_cfg *cfg);
```

注册端点的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 要注册端点的目标实例 |
| 输出（out） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `cfg` | 端点配置 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 端点配置或实例无效 |
| `-EBUSY` | 实例正忙或尚未就绪 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.6\_注销端点


```c
int (*deregister_endpoint)(const struct device *instance, void *token);
```

注销端点的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 要从中注销端点的实例 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 端点配置或实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBUSY` | 实例正忙或尚未就绪 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.7\_查询发送缓冲区大小


```c
int (*get_tx_buffer_size)(const struct device *instance, void *token);
```

返回发送缓冲区大小的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 不支持此操作 |
| `size` | 成功时返回发送缓冲区大小 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.8\_取得发送缓冲区


```c
int (*get_tx_buffer)(const struct device *instance, void *token,
                             void **data, uint32_t *len, k_timeout_t wait);
```

返回空发送缓冲区的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输出（out） | `data` | 用于返回空发送缓冲区指针的输出参数 |
| 输入／输出（in,out） | `len` | 用于保存发送缓冲区大小的输入／输出指针 |
| 输入（in） | `wait` | 等待可用发送缓冲区的超时（Timeout） |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 不支持该操作或所指定的超时 |
| `-ENOBUFS` | 没有可用的发送缓冲区 |
| `-EALREADY` | 已经取得一个缓冲区且尚未释放 |
| `-ENOMEM` | 请求大小过大；`size`参数包含允许的最大大小 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |

译注：此后端函数的大小参数名为`len`，但原文`-ENOMEM`说明仍写`size`。上表按原文保留；与公共函数中实际名为`size`的参数区分。


## 116.9\_丢弃发送缓冲区


```c
int (*drop_tx_buffer)(const struct device *instance, void *token,
                              const void *data);
```

丢弃发送缓冲区的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 发送缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-ENOTSUP` | 不支持此函数 |
| `-EALREADY` | 缓冲区已经丢弃 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.10\_无拷贝发送


```c
int (*send_nocopy)(const struct device *instance, void *token,
                           const void *data, size_t len);
```

用于无拷贝（No-copy）发送的函数指针：发送缓冲区已通过`ipc_service_get_tx_buffer()`取得，随后借此将数据发送给端点。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 待发送缓冲区指针 |
| 输入（in） | `len` | 待发送字节数 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EBADMSG` | 数据无效，例如格式、长度等不正确 |
| `-EBUSY` | 实例正忙或尚未就绪 |
| `bytes` | 成功时返回已发送字节数 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.11\_保留接收缓冲区


```c
int (*hold_rx_buffer)(const struct device *instance, void *token,
                              void *data);
```

保留接收缓冲区的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 要保留的接收缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EALREADY` | 该数据缓冲区已经被保留 |
| `-ENOTSUP` | 不支持此函数 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |


## 116.12\_释放接收缓冲区


```c
int (*release_rx_buffer)(const struct device *instance, void *token,
                                 void *data);
```

释放接收缓冲区的函数指针。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `instance` | 实例指针 |
| 输入（in） | `token` | 后端专用令牌（Backend-specific Token） |
| 输入（in） | `data` | 要释放的接收缓冲区指针 |

| 返回值 | 含义 |
| --- | --- |
| `-EINVAL` | 实例无效 |
| `-ENOENT` | 端点未注册到此实例 |
| `-EALREADY` | 该数据缓冲区已经释放 |
| `-ENOTSUP` | 不支持此函数 |
| `0` | 成功 |
| `other` | 其他错误码（errno），由后端具体实现决定 |

---

[上一章：IPC服务后端接口](P115_IPC服务后端接口.md) · [下一章：IPC服务头文件参考](P117_IPC服务头文件参考.md) · [返回大纲](大纲.md)
