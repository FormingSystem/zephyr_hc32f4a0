---
id: learning.zephyr-docs.intercore_reference.icmsgref-136
title: ICMsg配置结构
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__config__t.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第136章\_ICMsg配置结构

原文：[structicmsg__config__t](https://docs.zephyrproject.org/latest/doxygen/html/structicmsg__config__t.html)。读取日期：2026-10-13，`latest`。

`icmsg_config_t`是 ICMsg 核间消息传递（Inter-core Messaging）实例的配置结构（Configuration Structure），来自`zephyr/ipc/icmsg.h`。

原结构参考页只列成员与类型，没有逐字段说明。下表“阅读说明”依据成员名称、类型和同一头文件的接口／枚举，方便对照，不添加未给出的硬件配置要求。

```c
struct icmsg_config_t {
        struct mbox_dt_spec mbox_tx;
        struct mbox_dt_spec mbox_rx;
        enum icmsg_unbound_mode unbound_mode;
};
```

## 136.1\_配置成员

| 类型 | 成员 | 阅读说明 |
| --- | --- | --- |
| `struct mbox_dt_spec` | `mbox_tx` | 发送邮箱的设备树说明（Mailbox Devicetree Specification，TX） |
| `struct mbox_dt_spec` | `mbox_rx` | 接收邮箱的设备树说明（Mailbox Devicetree Specification，RX） |
| `enum icmsg_unbound_mode` | `unbound_mode` | 解绑模式枚举（Unbound Mode Enumeration），赋值关系见[基础接口](P135_ICMsg基础接口.md) |

TX 表示发送（Transmit），RX 表示接收（Receive）。`mbox_dt_spec`是邮箱设备树说明结构，具体字段见[邮箱设备树说明](P017_邮箱设备树规格结构.md)。

打开、关闭和发送都使用此配置结构，详见[ICMsg基础接口](P135_ICMsg基础接口.md)；完整可见定义见[头文件源码](P139_ICMsg完整头文件.md)。

---

[上一章：ICMsg基础接口](P135_ICMsg基础接口.md) · [下一章：ICMsg运行时结构](P137_ICMsg运行时结构.md) · [返回大纲](大纲.md)
