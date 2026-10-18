---
id: learning.zephyr-docs.storage.fstypes-4
title: RPMsgFS初始化接口
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpmsgfs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第45章\_RPMsgFS初始化接口

原文：[rpmsgfs_8h](https://docs.zephyrproject.org/latest/doxygen/html/rpmsgfs_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/fs/rpmsgfs.h` 声明 RPMsgFS 的初始化函数。RPMsgFS 使用**远程处理器消息（Remote Processor Messaging，RPMsg）**设备通信。

```c
#include <openamp/rpmsg.h>
```

## 45.1\_提供RPMsg设备

```c
void rpmsgfs_init_rpmsg(struct rpmsg_device *rpmsg_dev);
```

初始化 RPMsgFS，将 RPMsg 设备传入，以创建 RPMsgFS 所需的**端点（Endpoint）**。

参数 `rpmsg_dev` 指向 RPMsg 设备。此函数没有返回值。

---

[上一章：Ext2格式化配置](P044_Ext2格式化配置.md) · [下一章：闪存循环缓冲区参考目录](P046_闪存循环缓冲区参考目录.md) · [返回大纲](大纲.md)
