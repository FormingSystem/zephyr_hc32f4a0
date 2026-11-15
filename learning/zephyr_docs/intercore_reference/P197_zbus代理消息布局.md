---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-197
title: zbus代理消息布局
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第197章\_zbus代理消息布局

原文：[structzbus__proxy__msg](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__msg.html)。读取日期：2026-10-13，`latest`。

`zbus_proxy_msg`表示代理消息（Proxy Agent Message）的结构。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

数组容量由 Kconfig 构建配置系统（Build Configuration System）的配置宏确定：`CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE`用于消息缓冲区容量，`CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE`用于通道名称缓冲区容量。

## 197.1\_结构声明

```c
struct zbus_proxy_msg {
        uint32_t message_size;
        uint8_t message[CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE];
        uint32_t channel_name_len;
        char channel_name[CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE];
};
```

## 197.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `message_size` | `uint32_t` | 消息数据的大小 |
| `message` | `uint8_t [CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE]` | 二进制消息数据（Binary Message Data） |
| `channel_name_len` | `uint32_t` | 通道名称长度，**包含空字符终止符（NUL Terminator）** |
| `channel_name` | `char [CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE]` | 与消息关联的通道名称（Channel Name） |

## 197.3\_传输帧大小

此类型用固定大小缓冲区（Fixed-size Buffer）定义代理传输帧（Transport Frame）。原文建议后端考虑在线路上传输时序列化／紧凑化（Serializing/Compacting）消息，以减少传输量。

这一建议是通用后端设计说明；当前 IPC 后端的实际传输大小固定为`sizeof(struct zbus_proxy_msg)`，相关配置一致性要求见[zbus代理IPC后端接口](P201_zbus代理IPC后端接口.md)。

完整原始头文件见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus代理接收消息结构](P196_zbus代理接收消息结构.md) · [下一章：zbus影子通道结构](P198_zbus影子通道结构.md) · [返回大纲](大纲.md)
