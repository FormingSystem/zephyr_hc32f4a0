---
id: learning.zephyr-docs.intercore_reference.ipcsvc-112
title: IPC服务回调结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structipc__service__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第112章\_IPC服务回调结构

原文：[structipc__service__cb](https://docs.zephyrproject.org/latest/doxygen/html/structipc__service__cb.html)。读取日期：2026-10-13，`latest`。

`ipc_service_cb`是 IPC 处理器间通信（Inter-Processor Communication）服务的事件回调（Event Callback）结构，包含在[端点配置](P114_IPC服务端点配置.md)中，随端点注册一起注册。头文件为`zephyr/ipc/ipc_service.h`。


```c
struct ipc_service_cb {
        void (*bound)(void *priv);

        void (*unbound)(void *priv);

        void (*received)(const void *data, size_t len, void *priv);

        void (*error)(const char *message, void *priv);
};
```

## 112.1\_绑定成功


```c
void (*bound)(void *priv);
```

端点绑定（Binding）成功时调用。回调返回类型为`void`。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `priv` | 用户私有数据 |

## 112.2\_远端解绑与重新绑定


```c
void (*unbound)(void *priv);
```

端点被远端解绑（Unbound）时调用。绑定被移除可能有多种原因，例如远端注销端点、连接丢失，或远端中央处理器（Central Processing Unit，CPU）复位。

应用可以先进行清理、重置等处理；若希望再次绑定，可以重新注册端点。当远端恢复可用且也注册了端点后，绑定将重新建立，并调用`bound()`回调。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `priv` | 用户私有数据 |

## 112.3\_收到数据


```c
void (*received)(const void *data, size_t len, void *priv);
```

收到新数据包（Packet）时调用。

**未使用`ipc_service_hold_rx_buffer()`时，只有在此回调返回后，数据缓冲区才被视为已释放并再次可用。** 如需保留，参见[公共接口中的接收缓冲区管理](P111_IPC服务公共接口.md)。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `data` | 数据缓冲区指针 |
| 输入（in） | `len` | 数据长度 |
| 输入（in） | `priv` | 用户私有数据 |

## 112.4\_发生错误


```c
void (*error)(const char *message, void *priv);
```

发生错误时调用；`message`提供错误消息，返回类型为`void`。

| 方向 | 参数 | 含义 |
| --- | --- | --- |
| 输入（in） | `message` | 错误消息 |
| 输入（in） | `priv` | 用户私有数据 |

完整可见定义见[IPC服务完整头文件](P118_IPC服务完整头文件.md)。

---

[上一章：IPC服务公共接口](P111_IPC服务公共接口.md) · [下一章：IPC服务端点结构](P113_IPC服务端点结构.md) · [返回大纲](大纲.md)
