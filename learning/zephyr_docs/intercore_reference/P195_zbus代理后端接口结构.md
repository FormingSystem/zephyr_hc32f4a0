---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-195
title: zbus代理后端接口结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__backend__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第195章\_zbus代理后端接口结构

原文：[structzbus__proxy__agent__backend__api](https://docs.zephyrproject.org/latest/doxygen/html/structzbus__proxy__agent__backend__api.html)。读取日期：2026-10-13，`latest`。

`zbus_proxy_agent_backend_api`表示代理后端（Proxy Agent Backend）的应用程序编程接口（Application Programming Interface，API）。来自头文件`zephyr/zbus/proxy_agent/zbus_proxy_agent.h`。

## 195.1\_结构声明

```c
struct zbus_proxy_agent_backend_api {
        int (*backend_init)(const struct zbus_proxy_agent *agent);
        int (*backend_send)(const struct zbus_proxy_agent *agent, struct zbus_proxy_msg *msg);
        int (*backend_set_recv_cb)(const struct zbus_proxy_agent *agent,
                                   zbus_proxy_agent_recv_cb_t recv_cb);
};
```

## 195.2\_成员说明

| 成员 | 类型 | 含义 |
| --- | --- | --- |
| `backend_init` | `int (*)(const struct zbus_proxy_agent *agent)` | 后端初始化函数（Initializer Function） |
| `backend_send` | `int (*)(const struct zbus_proxy_agent *agent, struct zbus_proxy_msg *msg)` | 后端发送函数（Send Function） |
| `backend_set_recv_cb` | `int (*)(const struct zbus_proxy_agent *agent, zbus_proxy_agent_recv_cb_t recv_cb)` | 设置入站消息接收回调（Receive Callback）的函数 |

三个函数指针均返回`int`。原结构页没有给出逐参数或具体错误码契约；接收回调类型的完整说明见[zbus代理接口](P193_zbus代理接口.md)。

完整原始头文件见[zbus代理完整头文件](P200_zbus代理完整头文件.md)。

---

[上一章：zbus代理结构](P194_zbus代理结构.md) · [下一章：zbus代理接收消息结构](P196_zbus代理接收消息结构.md) · [返回大纲](大纲.md)
