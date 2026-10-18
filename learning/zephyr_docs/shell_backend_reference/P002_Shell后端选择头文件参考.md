---
id: learning.zephyr-docs.shell-backend-reference.page-2
title: Shell后端选择头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/shell__backend_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_Shell后端选择头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/shell__backend_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入Shell后端选择、虚拟后端、RTT、UART和日志后端的参考与源码。源码跟踪译注与官方原文分开标示。

Shell后端访问函数（Backend Accessors）的头文件。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <zephyr/shell/shell.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

Shell后端访问函数（Backend Accessors）的头文件。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.1\_函数（Functions）

<a id="r_gad299b24f7d116d733c3f9ccc839fdb2b"></a>

```c
static const struct shell * shell_backend_get (uint32_t idx)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_get](P001_Shell后端目录.md#gad299b24f7d116d733c3f9ccc839fdb2b)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

按索引取得Shell后端（Backend）。

<a id="r_gafcf533acf3e0540c6798e58d4c1f7528"></a>

```c
static int shell_backend_count_get (void)
```

相关声明：[shell_backend_count_get](P001_Shell后端目录.md#gafcf533acf3e0540c6798e58d4c1f7528)。

取得后端数量（Backend Count）。

<a id="r_ga34edbd459f8acce386a2f953bc6c795f"></a>

```c
const struct shell * shell_backend_get_by_name (const char *backend_name)
```

相关声明：[shell](../shell_core_reference/P004_Shell实例结构.md)、[shell_backend_get_by_name](P001_Shell后端目录.md#ga34edbd459f8acce386a2f953bc6c795f)。

按名称取得后端（Backend）。

## 2.2\_源码定位与版本边界

源码定位：[include/zephyr/shell/shell_backend.h](../../../include/zephyr/shell/shell_backend.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中登记的官方main文件。

> 译注——源码核对：后端索引（Backend Index）来自可遍历链接段（Iterable Section）。应先读取count并保证索引落在接口约定范围内；接口没有承诺越界时返回NULL。按名称查找则遍历Shell实例并用strcmp精确比较，未找到返回NULL。

> 译注——源码核对：传输后端（Transport Backend）连接Shell与通信通道；日志后端（Log Backend）将日志交给Shell输出。两者职责不同，启用某种传输本身不等价于启用日志输出。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.3\_原页交叉引用（Cross References）

- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/shell/shell.h](../shell_core_reference/P003_Shell核心头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码](P003_Shell后端选择头文件源码.md)
- [shell](../shell_core_reference/P004_Shell实例结构.md)
- [shell_backend_get](P001_Shell后端目录.md#gad299b24f7d116d733c3f9ccc839fdb2b)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [shell_backend_count_get](P001_Shell后端目录.md#gafcf533acf3e0540c6798e58d4c1f7528)
- [shell_backend_get_by_name](P001_Shell后端目录.md#ga34edbd459f8acce386a2f953bc6c795f)

<a id="header-details"></a>

---

[上一章](P001_Shell后端目录.md) · [返回大纲](大纲.md) · [下一章](P003_Shell后端选择头文件源码.md)
