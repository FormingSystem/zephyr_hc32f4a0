---
id: learning.zephyr-docs.intercore_reference.ipchostref-178
title: RPMsg命令行后端接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__shell__rpmsg.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第178章\_RPMsg命令行后端接口

原文：[group__shell__rpmsg](https://docs.zephyrproject.org/latest/doxygen/html/group__shell__rpmsg.html)。读取日期：2026-10-13，`latest`。

本页介绍通过远程消息传递（Remote Processor Messaging，RPMsg）端点（Endpoint）访问命令行（Shell）的后端接口。头文件为`zephyr/shell/shell_rpmsg.h`。

## 178.1\_定义传输实例

`SHELL_RPMSG_DEFINE(_name)`宏定义一个 RPMsg 命令行传输实例（Transport Instance）：

```c
static struct shell_rpmsg _name##_shell_rpmsg;                  \
struct shell_transport _name = {                                \
        .api = &shell_rpmsg_transport_api,                      \
        .ctx = (struct shell_rpmsg *)&_name##_shell_rpmsg,      \
}
```

| 参数 | 含义 |
| --- | --- |
| `_name` | 传输实例名称 |

阅读说明：宏创建对应的`shell_rpmsg`上下文，并把传输对象的应用程序编程接口（Application Programming Interface，API）指针指向`shell_rpmsg_transport_api`。`##`是预处理器的记号拼接（Token Pasting）运算符。

## 178.2\_取得后端实例

```c
const struct shell *shell_backend_rpmsg_get_ptr(void);
```

返回 RPMsg 命令行后端实例的指针。之后可以把这个实例用于`shell_execute_cmd()`函数，以测试命令行为（Command Behavior）。

返回值：指向命令行实例的指针。

## 178.3\_初始化传输

```c
int shell_backend_rpmsg_init_transport(struct rpmsg_device *rpmsg_dev);
```

使用传入的`rpmsg_dev`设备初始化命令行后端。

| 参数 | 含义 |
| --- | --- |
| `rpmsg_dev` | 指向 RPMsg 设备（Device）的指针 |

返回值：成功为0，发生错误时为负值。原页未列举具体错误码，译文不额外推断。

完整原始头文件见[RPMsg命令行后端完整头文件](P180_RPMsg命令行后端完整头文件.md)。

---

[上一章：MPSC数据包描述完整头文件](P177_MPSC数据包描述完整头文件.md) · [下一章：RPMsg命令行后端头文件参考](P179_RPMsg命令行后端头文件参考.md) · [返回大纲](大纲.md)
