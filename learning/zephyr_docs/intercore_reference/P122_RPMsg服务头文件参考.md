---
id: learning.zephyr-docs.intercore_reference.rpmsgref-122
title: RPMsg服务头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rpmsg__service_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第122章\_RPMsg服务头文件参考

原文：[rpmsg__service_8h](https://docs.zephyrproject.org/latest/doxygen/html/rpmsg__service_8h.html)。读取日期：2026-10-13，`latest`。

本页是远程处理器消息传递（Remote Processor Messaging，RPMsg）服务头文件`zephyr/ipc/rpmsg_service.h`的参考索引。

## 122.1\_包含文件

```c
#include <openamp/open_amp.h>
```

该文件包含 OpenAMP 框架头文件；OpenAMP 是开放式非对称多处理（Open Asymmetric Multi Processing）框架。

## 122.2\_接口声明

注册端点（Endpoint）的函数，回调（Callback）类型为`rpmsg_ept_cb`：

```c
int rpmsg_service_register_endpoint(const char *name, rpmsg_ept_cb cb);
```

通过给定端点发送数据的函数：

```c
int rpmsg_service_send(int endpoint_id, const void *data, size_t len);
```

检查端点是否已绑定（Bound）的函数，返回布尔值：

```c
bool rpmsg_service_endpoint_is_bound(int endpoint_id);
```

参数与返回值完整译文见[RPMsg服务公共接口](P121_RPMsg服务公共接口.md)，原文件完整可见代码见[完整头文件](P123_RPMsg服务完整头文件.md)。

---

[上一章：RPMsg服务公共接口](P121_RPMsg服务公共接口.md) · [下一章：RPMsg服务完整头文件](P123_RPMsg服务完整头文件.md) · [返回大纲](大纲.md)
