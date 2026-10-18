---
id: learning.zephyr-docs.intercore_reference.zbusproxyref-201
title: zbus代理IPC后端接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent__ipc__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第201章\_zbus代理IPC后端接口

原文：[group__zbus__proxy__agent__ipc__backend](https://docs.zephyrproject.org/latest/doxygen/html/group__zbus__proxy__agent__ipc__backend.html)。读取日期：2026-10-13，`latest`。

本页介绍 zbus 代理（Proxy Agent）的处理器间通信（Inter-Processor Communication，IPC）后端（Backend）。

**可用条件：** 必须启用 Kconfig 构建配置系统（Build Configuration System）的`CONFIG_ZBUS_PROXY_AGENT_IPC`选项。

## 201.1\_固定大小传输帧

IPC 后端通过`ipc_service`使用共享内存消息传递（Shared-memory Message Passing）模型，因此在不同域（Domain）之间传输固定大小的代理帧`struct zbus_proxy_msg`。

即使`message_size`或`channel_name_len`较小，**实际传输大小仍等于`sizeof(struct zbus_proxy_msg)`**。

## 201.2\_通信双方的配置必须一致

帧大小在编译期（Compile Time）由以下选项决定：

- `CONFIG_ZBUS_PROXY_AGENT_MAX_MESSAGE_SIZE`。
- `CONFIG_ZBUS_PROXY_AGENT_MAX_CHANNEL_NAME_SIZE`。

**所有相互通信的域都必须为这两个选项使用相同的值。** IPC 后端会依据`sizeof(struct zbus_proxy_msg)`校验收到的数据，域间配置不匹配将导致接收消息被拒绝。

## 201.3\_数据结构与源码

| 结构 | 说明 |
| --- | --- |
| [zbus代理IPC运行时结构](P203_zbus代理IPC运行时结构.md) | 代理 IPC 后端的可变运行时数据（Mutable Runtime Data） |
| [zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md) | 代理 IPC 后端的配置结构 |

消息帧布局见[zbus代理消息布局](P197_zbus代理消息布局.md)；头文件参考见[zbus代理IPC头文件参考](P204_zbus代理IPC头文件参考.md)；完整原始源码见[zbus代理IPC完整头文件](P205_zbus代理IPC完整头文件.md)。

---

[上一章：zbus代理完整头文件](P200_zbus代理完整头文件.md) · [下一章：zbus代理IPC配置结构](P202_zbus代理IPC配置结构.md) · [返回大纲](大纲.md)
