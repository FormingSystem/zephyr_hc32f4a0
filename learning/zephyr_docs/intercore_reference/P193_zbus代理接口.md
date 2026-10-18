---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-193
title: zbus代理接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第193章\_zbus代理接口

原文：[group__zbus__proxy__agent](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent.html)。读取日期：2026-10-13，`latest`。

本页介绍 zbus 消息总线（Message Bus）的跨域代理（Proxy Agent）应用程序编程接口（Application Programming Interface，API）。头文件为`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

**可用条件：** 必须启用 Kconfig 构建配置系统（Build Configuration System）的`CONFIG_ZBUS_PROXY_AGENT`选项。

## 193.1\_数据结构与后端

| 结构 | 用途 |
| --- | --- |
| [zbus影子通道结构](P198_zbus影子通道结构.md) | 记录影子通道（Shadow Channel）所属代理的元数据（Metadata） |
| [zbus代理消息布局](P197_zbus代理消息布局.md) | 代理消息与传输帧（Transport Frame）的结构 |
| [zbus代理接收消息结构](P196_zbus代理接收消息结构.md) | 已验证接收消息的内部线程载荷（Thread Payload） |
| [zbus代理结构](P194_zbus代理结构.md) | 代理实例及配置 |
| [zbus代理后端接口结构](P195_zbus代理后端接口结构.md) | 代理后端（Backend）的接口结构 |

处理器间通信（Inter-Processor Communication，IPC）后端详见[zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md)。

## 193.2\_添加转发通道

`ZBUS_PROXY_ADD_CHAN(_agent, _chan)`将通道添加到代理的转发范围。宏展开为：

```c
ZBUS_CHAN_ADD_OBS(_chan, _agent##_listener, zz)
```

| 参数 | 含义 |
| --- | --- |
| `_agent` | 负责转发该通道的代理实例 |
| `_chan` | 需要代理转发的通道 |

**观察者执行顺序：** 此宏以`zz`作为观察者优先级。可迭代段（Iterable Section）中的观察者优先级按字典序（Lexicographic Order）排序，因此代理监听器（Listener）安排在该通道的其他观察者之后，以避免潜在的阻塞行为。同一通道的其他观察者应使用字典序小于`zz`的优先级，确保它们先于代理监听器执行。

## 193.3\_定义代理实例

`ZBUS_PROXY_AGENT_DEFINE(_name, _type, _backend_dt_node)`以指定名称、后端类型和后端设备树节点定义一个代理。

| 参数 | 含义 |
| --- | --- |
| `_name` | 代理实例名称 |
| `_type` | 代理后端类型，例如`ZBUS_PROXY_AGENT_BACKEND_IPC` |
| `_backend_dt_node` | 后端配置使用的设备树（Devicetree）节点 |

原接口页未展示此宏的展开，完整定义见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

## 193.4\_定义影子通道

宏`ZBUS_SHADOW_CHAN_DEFINE(_name, _type, _proxy_name, _user_data, _observers, _init_val)`定义与代理关联的影子通道：

```c
ZBUS_CHAN_DEFINE(_name, _type, _ZBUS_PROXY_AGENT_VALIDATOR(_proxy_name), _user_data,       \
                 _observers, _init_val);                                                   \
_ZBUS_SHADOW_CHAN_REGISTER(_name, _proxy_name)
```

影子通道是其他域（Domain）中远端通道的本地镜像（Local Mirror）。为保证数据完整性，**只有与它关联的代理能够向它发布消息**。

| 参数 | 含义 |
| --- | --- |
| `_name` | 通道（Channel）名称 |
| `_type` | 消息类型结构 |
| `_proxy_name` | 关联的代理名称 |
| `_user_data` | 用户数据（User Data）指针 |
| `_observers` | 静态观察者列表（Static Observer List） |
| `_init_val` | 通道初始值 |

## 193.5\_定义具有指定标识的影子通道

宏`ZBUS_SHADOW_CHAN_DEFINE_WITH_ID(_name, _id, _type, _proxy_name, _user_data, _observers, _init_val)`定义具有指定通道标识（Channel ID）、并与代理关联的影子通道；内部通过`ZBUS_CHAN_DEFINE_WITH_ID`宏建立带标识的通道：

```c
ZBUS_CHAN_DEFINE_WITH_ID(_name, _id, _type, _ZBUS_PROXY_AGENT_VALIDATOR(_proxy_name),      \
                         _user_data, _observers, _init_val);                               \
_ZBUS_SHADOW_CHAN_REGISTER(_name, _proxy_name)
```

该通道同样是其他域中远端通道的本地镜像，而且只允许关联代理向其发布，以保证数据完整性。

| 参数 | 含义 |
| --- | --- |
| `_name` | 通道（Channel）名称 |
| `_id` | 通道标识（ID） |
| `_type` | 消息类型结构 |
| `_proxy_name` | 关联的代理名称 |
| `_user_data` | 用户数据（User Data）指针 |
| `_observers` | 静态观察者列表（Static Observer List） |
| `_init_val` | 通道初始值 |

## 193.6\_接收回调类型

```c
typedef int (*zbus_proxy_agent_recv_cb_t)(const struct zbus_proxy_agent *agent,
                                          const struct zbus_proxy_msg *msg);
```

代理收到消息时调用此接收回调（Receive Callback）。回调应处理消息，成功返回0，失败返回负错误码。

| 参数 | 含义 |
| --- | --- |
| `agent` | 代理实例指针 |
| `msg` | 收到的代理消息指针 |

返回类型为`int`；0表示成功，负错误码表示失败。

## 193.7\_支持的后端类型

```c
enum zbus_proxy_agent_backend_type {
    ZBUS_PROXY_AGENT_BACKEND_IPC
};
```

`zbus_proxy_agent_backend_type`列出支持的代理后端类型。唯一列出的枚举项`ZBUS_PROXY_AGENT_BACKEND_IPC`是 IPC 后端；原枚举说明称其用于进程间通信（Inter-process Communication）。在本代理的跨核使用场景中，具体传输由 IPC 服务承担。

## 193.8\_初始化内部接口

```c
int zbus_init_proxy_agent(const struct zbus_proxy_agent *agent);
```

原简介为“内部代理接收回调（Internal Proxy Agent Receive Callback）”。

**译注：** 原详细说明和函数名称表明，此函数用于初始化代理：设置后端并启动专用线程（Dedicated Thread）。它由`sys_init`流程中的生成初始化函数调用，**不应直接调用**；原简介与详细用途不一致，已在此明确保留和说明。

| 参数 | 含义 |
| --- | --- |
| `agent` | 代理配置 |

返回类型为`int`；成功返回0，失败返回负错误码。

## 193.9\_内部监听器回调

```c
void zbus_proxy_agent_listener_cb(const struct zbus_channel *chan,
                                  const struct zbus_proxy_agent *agent);
```

这是内部代理监听器回调，由生成的监听器回调调用，**不应直接调用**。

| 参数 | 含义 |
| --- | --- |
| `agent` | 代理配置 |
| `chan` | 触发回调的通道 |

上述参数说明沿用原页表格顺序；实际函数签名中的顺序为`chan`在前、`agent`在后。

---

[上一章：RPMsg文件系统完整头文件](P192_RPMsg文件系统完整头文件.md) · [下一章：zbus代理结构](P194_zbus代理结构.md) · [返回大纲](大纲.md)
