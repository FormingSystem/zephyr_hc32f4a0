---
id: learning.zephyr-docs.api-source-reference.page-899
title: user_pipe.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第899章\_user\_pipe.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html)。

## 899.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="achat_8h_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructmodem__chat_html"></a>
<a id="auser__pipe_8h_html_aa01e3e6354411ce80126ccb26a179887"></a>
<a id="auser__pipe_8h_html_ad543fa2f8518397cde2600a9263b8e6f"></a>

```c
/*
 * Copyright (c) 2025 Embeint Holdings Pty Ltd
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MODEM_AT_USER_PIPE_H_
#define ZEPHYR_INCLUDE_MODEM_AT_USER_PIPE_H_

#include <zephyr/modem/chat.h>

int modem_at_user_pipe_claim(struct modem_chat *chat, k_timeout_t timeout);

void modem_at_user_pipe_release(void);

#endif /* ZEPHYR_INCLUDE_MODEM_AT_USER_PIPE_H_ */
```

## 899.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Embeint Holdings Pty Ltd。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 36 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MODEM_AT_USER_PIPE_H_`。

## 899.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html)
- [zephyr/modem/chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)
- [modem_at_user_pipe_claim](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html#aa01e3e6354411ce80126ccb26a179887)
- [modem_chat](../modem_wireless_model_reference/P052_modem_chat_结构体.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [modem_at_user_pipe_release](https://docs.zephyrproject.org/latest/doxygen/html/user__pipe_8h.html#ad543fa2f8518397cde2600a9263b8e6f)
- [chat.h](https://docs.zephyrproject.org/latest/doxygen/html/chat_8h.html)

---

[上一章](P898_usbd_uvc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P900_v2m-musca-b1-pinctrl.h_源码浏览.md)
