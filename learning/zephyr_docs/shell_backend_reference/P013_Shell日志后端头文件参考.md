---
id: learning.zephyr-docs.shell-backend-reference.page-13
title: Shell日志后端头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__log__backend_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_Shell日志后端头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__log__backend_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell日志后端（Log Backend）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/logging/log_backend.h>
#include <zephyr/logging/log_output.h>
#include <zephyr/sys/mpsc_pbuf.h>
#include <zephyr/sys/atomic.h>
```

查看此文件的源码。

Shell日志后端（Log Backend）的头文件。

## 13.1\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_log_backend.h](../../../include/zephyr/shell/shell_log_backend.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：此头文件参考页只公开文件说明和源码入口；源码浏览页还显示内部结构、状态枚举和z_shell_*声明。这里完整保留可见代码，但不把隐藏在Doxygen内部条件中的条目补造为公共API契约。

> 译注——源码核对：日志队列宏用_queue_size除以sizeof(uint32_t)定义数组，再以数组元素个数配置MPSC缓冲。队列大小参数和MPSC字数的单位不同；实际容量受除法取整及消息对齐影响。

> 译注——源码核对：条件编译实际检查CONFIG_SHELL_LOG_BACKEND。原代码两个分支注释写作CONFIG_LOG，译文保留其原名并在此区分，不能据注释反推编译开关。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 13.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/logging/log_backend.h](../log_backend_reference/P003_日志后端头文件源码.md)
- [zephyr/logging/log_output.h](../log_output_reference/P003_日志输出头文件源码.md)
- [zephyr/sys/mpsc_pbuf.h](../intercore_reference/P171_MPSC数据包缓冲区完整头文件.md)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [查看此文件的源码](P014_Shell日志后端头文件源码.md)

<a id="header-details"></a>

---

[上一章](P012_Shell_UART后端头文件源码.md) · [返回大纲](大纲.md) · [下一章](P014_Shell日志后端头文件源码.md)
