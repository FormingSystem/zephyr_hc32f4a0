---
id: learning.zephyr-docs.shell-util-reference.page-3
title: Shell命令历史头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__history_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Shell命令历史头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__history_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell格式化输出、命令历史、字符串转换和终端类型的参考与源码。源码跟踪译注与官方原文分开标示。

Shell命令历史（Command History）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/dlist.h>
#include <zephyr/sys/ring_buffer.h>
#include <stdbool.h>
```

查看此文件的源码。

Shell命令历史（Command History）的头文件。

## 3.1\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_history.h](../../../include/zephyr/shell/shell_history.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：历史实例使用内核堆（Kernel Heap）存储双向链表条目。当前put忽略空行和与最新条目完全相同的命令，空间不足时移除最旧条目以尝试分配；这不是按固定命令条数构造的队列。

> 译注——源码核对：当前get把整条历史命令复制到dst并追加NUL，虽然原始头文件把len写作输入输出容量，该版本实现没有读取其输入值来限制复制。调用方必须保证目标空间可容纳命令和终止字符，不能把len当作已实现的截断保护。

> 译注——源码核对：mode_exit仅将当前浏览指针置空；purge才删除全部条目。active表示是否处于历史浏览模式，不表示历史中是否保存了命令。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/sys/dlist.h](../dlist_reference/P003_双向链表头文件源码.md)
- [zephyr/sys/ring_buffer.h](../ringbuffer_reference/P004_环形缓冲区头文件源码.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [查看此文件的源码](P004_Shell命令历史头文件源码.md)

<a id="header-details"></a>

---

[上一章](P002_Shell格式化输出头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_Shell命令历史头文件源码.md)
