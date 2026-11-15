---
id: learning.zephyr-docs.shell-util-reference.page-1
title: Shell格式化输出头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__fprintf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_Shell格式化输出头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__fprintf_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell格式化输出、命令历史、字符串转换和终端类型的参考与源码。源码跟踪译注与官方原文分开标示。

Shell格式化输出辅助函数（Formatted Output Helpers）的头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <stdbool.h>
#include <stddef.h>
```

查看此文件的源码。

Shell格式化输出辅助函数（Formatted Output Helpers）的头文件。

## 1.1\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_fprintf.h](../../../include/zephyr/shell/shell_fprintf.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：格式化辅助函数的参考页没有列出内部z_shell_*接口详细说明；源码页仍完整保留它们的可见声明、宏和控制结构。输出缓冲区与用户上下文由调用方提供，不由DEFINE宏复制其内容。

> 译注——源码核对：当前flush调用fwrite传出已有缓冲内容，随后把buffer_cnt清零。fwrite回调返回void，不能从这次刷新推断串口、网络或远端终端已确认接收。autoflush控制一次格式化结束后的刷新，缓冲区满时也会刷新。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.2\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [查看此文件的源码](P002_Shell格式化输出头文件源码.md)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_Shell格式化输出头文件源码.md)
