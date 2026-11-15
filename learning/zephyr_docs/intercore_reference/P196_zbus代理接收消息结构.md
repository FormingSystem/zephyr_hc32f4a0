---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-196
title: zbus代理接收消息结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__rx__msg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第196章\_zbus代理接收消息结构

原文：[structzbus__proxy__agent__rx__msg](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__rx__msg.html)。读取日期：2026-10-13，`latest`。

`zbus_proxy_agent_rx_msg`表示已验证接收消息的内部线程载荷（Internal Thread Payload）。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

数组容量由 Kconfig 构建配置系统（Build Configuration System）的配置宏确定：`CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE`用于消息缓冲区容量。

## 196.1\_结构声明

```c
struct zbus_proxy_agent_rx_msg {
        const struct zbus_channel *chan;
        uint8_t message[CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE];
};
```

## 196.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `chan` | `const struct zbus_channel *` | 已解析出的、将接收消息的影子通道（Shadow Channel） |
| `message` | `uint8_t [CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE]` | 二进制消息数据（Binary Message Data） |

完整原始头文件见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus代理后端接口结构](P195_zbus代理后端接口结构.md) · [下一章：zbus代理消息布局](P197_zbus代理消息布局.md) · [返回大纲](大纲.md)
