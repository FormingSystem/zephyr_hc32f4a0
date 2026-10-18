---
id: learning.zephyr-docs.intercore_reference.ipcremainder-192
title: RPMsg文件系统完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpmsgfs_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第192章\_RPMsg文件系统完整头文件

原文：[rpmsgfs_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/rpmsgfs_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留 RPMsg 文件系统（RPMsg File System，RPMsgFS）的`zephyr/fs/rpmsgfs.h`完整官方可见源码（Source Code）。RPMsg 为远程处理器消息传递（Remote Processor Messaging）。仅去除网页行号与行尾空白，2026年 NXP 版权及`Apache-2.0`许可证声明保留。

## 192.1\_完整头文件

```c
/*
 * Copyright 2026 NXP
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_FS_RPMSGFS_H_
#define ZEPHYR_INCLUDE_FS_RPMSGFS_H_

#include <openamp/rpmsg.h>

void rpmsgfs_init_rpmsg(struct rpmsg_device *rpmsg_dev);

#endif /* ZEPHYR_INCLUDE_FS_RPMSGFS_H_ */
```

## 192.2\_接口与可见注释

`rpmsgfs_init_rpmsg()`接收`struct rpmsg_device *rpmsg_dev`，将 RPMsg 设备传入初始化过程，以创建 RPMsgFS 所需端点（Endpoint）。对应原页的完整接口翻译见[RPMsgFS 初始化接口](../storage/P045_RPMsgFS初始化接口.md)。

网页可见源码没有展开函数文档注释；此处接口解释来自已翻译的文件参考，不冒充源码中可见的注释。末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_FS_RPMSGFS_H_`结束。

---

[上一章：TFM的IPC服务示例](P191_TFM的IPC服务示例.md) · [下一章：zbus代理接口](P193_zbus代理接口.md) · [返回大纲](大纲.md)
