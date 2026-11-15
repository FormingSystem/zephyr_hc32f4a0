---
id: learning.zephyr-docs.rtio-model-reference.page-3
title: RTIO输入输出设备
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_RTIO输入输出设备

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

```c
#include <zephyr/rtio/iodev.h>
```

<a id="details"></a>

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 3.1\_数据成员（Data Fields）

<a id="r_a6dfedbfb58356e0647e5c20632656977"></a>

```c
const struct rtio_iodev_api * api
```

相关声明：[rtio_iodev_api](P004_RTIO设备函数表.md)、[api](#a6dfedbfb58356e0647e5c20632656977)。

函数指针表（Function Pointer Table）。

<a id="r_af0f3a27fe8dea2161c9a73cb838bdeec"></a>

```c
void * data
```

相关声明：[data](#af0f3a27fe8dea2161c9a73cb838bdeec)。

与此IODEV关联的数据。

## 3.2\_详细说明（Detailed Documentation）

<a id="a6dfedbfb58356e0647e5c20632656977"></a>

### `api`

```c
const struct rtio_iodev_api* rtio_iodev::api
```

函数指针表（Function Pointer Table）。

<a id="af0f3a27fe8dea2161c9a73cb838bdeec"></a>

### `data`

```c
void* rtio_iodev::data
```

与此IODEV关联的数据。

## 3.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：RTIO的IODEV由`api`函数表和不透明`data`指针组成。它不是Zephyr设备模型`struct device`的同义词；总线或传感器适配层可以通过`data`保存具体设备描述。`RTIO_IODEV_DEFINE()`保存传入指针，不替调用者分配或深复制其对象，相关对象需在异步使用期间有效。

> 译注——源码核对：执行器通过`sqe.iodev->api->submit()`调用设备。IODEV对象、函数表及必要的数据必须已按对应驱动要求初始化。用户空间访问上下文的权限也不代表自动具备所有IODEV的权限；系统调用校验单独检查被引用的IODEV。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.4\_原页交叉引用（Cross References）

- [zephyr/rtio/iodev.h](../rtio_headers_reference/P006_RTIO设备头文件源码.md)
- [rtio_iodev_api](P004_RTIO设备函数表.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P002_RTIO完成事件.md) · [返回大纲](大纲.md) · [下一章](P004_RTIO设备函数表.md)
