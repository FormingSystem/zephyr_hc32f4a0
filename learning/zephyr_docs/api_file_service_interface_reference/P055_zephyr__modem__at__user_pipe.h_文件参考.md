---
id: learning.zephyr-docs.api-file-service-interface-reference.page-55
title: zephyr__modem__at__user_pipe.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第55章\_zephyr\_\_modem\_\_at\_\_user\_pipe.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/modem/chat.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 55.1\_函数（Functions）

<a id="r_aa01e3e6354411ce80126ccb26a179887"></a>

```c
int modem_at_user_pipe_claim (struct modem_chat *chat, k_timeout_t timeout)
```

相关声明：[modem_at_user_pipe_claim](#aa01e3e6354411ce80126ccb26a179887)、[modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

申请占用 AT 命令用户管道（User Pipe），以运行命令。

<a id="r_ad543fa2f8518397cde2600a9263b8e6f"></a>

```c
void modem_at_user_pipe_release (void)
```

相关声明：[modem_at_user_pipe_release](#ad543fa2f8518397cde2600a9263b8e6f)。

将 AT 命令用户管道（User Pipe）释放给其他用户。

## 55.2\_详细说明（Detailed Documentation）

<a id="aa01e3e6354411ce80126ccb26a179887"></a>

### `modem_at_user_pipe_claim()`

```c
int modem_at_user_pipe_claim ( struct modem_chat * chat, k_timeout_t timeout )
```

申请占用 AT 命令用户管道（User Pipe），以运行命令。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `chat` | 将与用户管道一起使用的聊天脚本（Chat）实例。 |
| `timeout` | 等待其他用户释放管道的最长时限（Maximum Duration）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EPERM` | 调制解调器（Modem）尚未就绪。 |
| `-EBUSY` | 用户管道（User Pipe）已被占用。 |

**说明（Note）**：**注意（Note）：**若底层管道尚未打开，本函数不会阻塞。在附接聊天脚本（Chat）实例之前，会排空管道中所有待处理数据。

<a id="ad543fa2f8518397cde2600a9263b8e6f"></a>

### `modem_at_user_pipe_release()`

```c
void modem_at_user_pipe_release ( void )
```

将 AT 命令用户管道（User Pipe）释放给其他用户。

在 `modem_at_user_pipe_claim` 之后，管道不再使用时必须调用此函数。


## 55.3\_原页交叉引用（Cross References）

- [zephyr/modem/chat.h](../api_source_interrupt_modem_reference/P002_chat.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P899_user_pipe.h_源码浏览.md)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P054_zephyr__drivers__usb__usb_bc12.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P056_zephyr__net__virtual.h_文件参考.md)
