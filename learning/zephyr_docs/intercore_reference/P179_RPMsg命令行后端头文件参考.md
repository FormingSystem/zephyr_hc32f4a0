---
id: learning.zephyr-docs.intercore_reference.ipchostref-179
title: RPMsg命令行后端头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__rpmsg_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第179章\_RPMsg命令行后端头文件参考

原文：[shell__rpmsg_8h](https://docs.zephyrproject.org/latest/doxygen/html/shell__rpmsg_8h.html)。读取日期：2026-10-13，`latest`。

本页对应远程消息传递（Remote Processor Messaging，RPMsg）命令行（Shell）后端的`zephyr/shell/shell_rpmsg.h`头文件参考（Header Reference）。

## 179.1\_依赖头文件

```c
#include <zephyr/kernel.h>
#include <zephyr/shell/shell.h>
#include <openamp/rpmsg.h>
```

## 179.2\_宏定义

`SHELL_RPMSG_DEFINE(_name)`定义一个 RPMsg 命令行传输实例（Transport Instance）；`_name`是实例名称。宏展开见[RPMsg命令行后端接口](P178_RPMsg命令行后端接口.md)。

## 179.3\_函数接口

```c
int shell_backend_rpmsg_init_transport(struct rpmsg_device *rpmsg_dev);
```

使用给定的 RPMsg 设备初始化命令行后端。

```c
const struct shell *shell_backend_rpmsg_get_ptr(void);
```

取得 RPMsg 命令行后端实例的指针。完整参数与返回值说明见[RPMsg命令行后端接口](P178_RPMsg命令行后端接口.md)，原始源码见[RPMsg命令行后端完整头文件](P180_RPMsg命令行后端完整头文件.md)。

---

[上一章：RPMsg命令行后端接口](P178_RPMsg命令行后端接口.md) · [下一章：RPMsg命令行后端完整头文件](P180_RPMsg命令行后端完整头文件.md) · [返回大纲](大纲.md)
