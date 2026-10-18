---
id: learning.zephyr-docs.intercore_reference.rpmsgref-123
title: RPMsg服务完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpmsg__service_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第123章\_RPMsg服务完整头文件

原文：[rpmsg__service_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/rpmsg__service_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留官方源码浏览页中`zephyr/ipc/rpmsg_service.h`的完整可见代码，用于RPMsg 服务。RPMsg 为远程处理器消息传递（Remote Processor Messaging），IPC 为处理器间通信（Inter-Processor Communication）。展示行号已移除，声明、版权和许可证均保留。

## 123.1\_完整可见源码

```c
/*
 * Copyright (c) 2020 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_IPC_RPMSG_SERVICE_H_
#define ZEPHYR_INCLUDE_IPC_RPMSG_SERVICE_H_

#include <openamp/open_amp.h>

#ifdef __cplusplus
extern "C" {
#endif


int rpmsg_service_register_endpoint(const char *name, rpmsg_ept_cb cb);

int rpmsg_service_send(int endpoint_id, const void *data, size_t len);

bool rpmsg_service_endpoint_is_bound(int endpoint_id);



#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_IPC_RPMSG_SERVICE_H_ */
```

## 123.2\_源码说明与对应译文

原文件版权为2020年 Nordic Semiconductor ASA，许可证为 Apache-2.0。头文件保护宏（Header Guard）为`ZEPHYR_INCLUDE_IPC_RPMSG_SERVICE_H_`；文件末尾注释标识该保护宏的结束。
`__cplusplus`条件分支和`extern "C"`用于保持 C++ 环境下的 C 语言链接方式。官方 Doxygen 源码浏览页把文档注释提取到说明页，相关中文译文见[公共接口](P121_RPMsg服务公共接口.md)和[文件参考](P122_RPMsg服务头文件参考.md)。

---

[上一章：RPMsg服务头文件参考](P122_RPMsg服务头文件参考.md) · [下一章：IPC的RPMsg公共层接口](P124_IPC的RPMsg公共层接口.md) · [返回大纲](大纲.md)
