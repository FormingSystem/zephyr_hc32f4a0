---
id: learning.zephyr-docs.intercore_reference.ipcsvc-117
title: IPC服务头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ipc__service_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第117章\_IPC服务头文件参考

原文：[ipc__service_8h](https://docs.zephyrproject.org/latest/doxygen/html/ipc__service_8h.html)。读取日期：2026-10-13，`latest`。

本页是 IPC 处理器间通信（Inter-Processor Communication）服务头文件`zephyr/ipc/ipc_service.h`的参考索引。应用程序编程接口（Application Programming Interface，API）的完整参数、生命周期和返回值说明见[公共接口](P111_IPC服务公共接口.md)；完整可见代码见[头文件源码](P118_IPC服务完整头文件.md)。

## 117.1\_包含文件

```c
#include <stdio.h>
#include <zephyr/device.h>
#include <zephyr/kernel.h>
```

## 117.2\_数据结构

| 结构 | 用途 |
| --- | --- |
| [`ipc_service_cb`](P112_IPC服务回调结构.md) | 事件回调（Event Callback） |
| [`ipc_ept`](P113_IPC服务端点结构.md) | 端点实例（Endpoint Instance） |
| [`ipc_ept_cfg`](P114_IPC服务端点配置.md) | 端点配置（Endpoint Configuration） |

## 117.3\_函数声明

TX 为发送（Transmit），RX 为接收（Receive）；无拷贝（No-copy）发送直接使用已取得的通信缓冲区。`k_timeout_t`为内核超时类型。

```c
int ipc_service_open_instance(const struct device *instance);
```

打开实例。


```c
int ipc_service_close_instance(const struct device *instance);
```

关闭实例。


```c
int ipc_service_register_endpoint(const struct device *instance,
                                  struct ipc_ept *ept,
                                  const struct ipc_ept_cfg *cfg);
```

注册端点。


```c
int ipc_service_deregister_endpoint(struct ipc_ept *ept);
```

注销端点。


```c
int ipc_service_send(struct ipc_ept *ept, const void *data, size_t len);
```

发送数据。


```c
int ipc_service_send_critical(struct ipc_ept *ept, const void *data, size_t len);
```

发送关键消息。发送高优先级消息并绕过正常状态检查。


```c
int ipc_service_get_tx_buffer_size(struct ipc_ept *ept);
```

查询发送缓冲区大小。


```c
int ipc_service_get_tx_buffer(struct ipc_ept *ept, void **data, uint32_t *size, k_timeout_t wait);
```

取得发送缓冲区。取得供无拷贝发送函数`ipc_service_send_nocopy()`发送的空缓冲区。


```c
int ipc_service_drop_tx_buffer(struct ipc_ept *ept, const void *data);
```

丢弃发送缓冲区。


```c
int ipc_service_send_nocopy(struct ipc_ept *ept, const void *data, size_t len);
```

无拷贝发送。使用给定端点发送通过缓冲区获取函数`ipc_service_get_tx_buffer()`预留的缓冲区。


```c
int ipc_service_hold_rx_buffer(struct ipc_ept *ept, void *data);
```

保留接收缓冲区。供接收回调之外继续使用。


```c
int ipc_service_release_rx_buffer(struct ipc_ept *ept, void *data);
```

释放接收缓冲区。使其可以再次复用。

---

[上一章：IPC服务后端操作结构](P116_IPC服务后端操作结构.md) · [下一章：IPC服务完整头文件](P118_IPC服务完整头文件.md) · [返回大纲](大纲.md)
