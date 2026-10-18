---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-198
title: zbus影子通道结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__shadow__channel.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第198章\_zbus影子通道结构

原文：[structzbus__shadow__channel](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__shadow__channel.html)。读取日期：2026-10-13，`latest`。

结构体`zbus_shadow_channel`表示影子通道（Shadow Channel）的元数据（Metadata），用于跟踪它所属的代理（Proxy Agent）。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

## 198.1\_结构声明

```c
struct zbus_shadow_channel {
        const struct zbus_channel *chan;
        const struct zbus_proxy_agent *proxy_agent;
};
```

## 198.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `chan` | `const struct zbus_channel *` | 影子通道指针 |
| `proxy_agent` | `const struct zbus_proxy_agent *` | 拥有该影子通道的代理指针 |

发布权限由关联代理控制，定义宏和约束见[zbus代理接口](P193_zbus代理接口.md)。

完整原始头文件见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus代理消息布局](P197_zbus代理消息布局.md) · [下一章：zbus代理头文件参考](P199_zbus代理头文件参考.md) · [返回大纲](大纲.md)
