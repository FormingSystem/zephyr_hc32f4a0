---
id: learning.zephyr-docs.rtio-headers-reference.page-5
title: RTIO设备头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/iodev_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_RTIO设备头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/iodev_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SQE、CQE和IODEV三个头文件的参考与源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

RTIO输入输出设备（I/O Device）及相关函数。

查看此文件的源码。

<a id="details"></a>

RTIO输入输出设备（I/O Device）及相关函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.1\_数据结构（Data Structures）

<a id="r_rtio_5Fiodev_5Fapi"></a>

```c
struct rtio_iodev_api
```

相关声明：[rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)。

RTIO输入输出设备应实现的API。

<a id="r_rtio_5Fiodev"></a>

```c
struct rtio_iodev
```

相关声明：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.2\_宏定义（Macros）

<a id="r_gaae51e2a679d37bc1cfba79961688c406"></a>

```c
#define RTIO_IODEV_DEFINE(name, iodev_api, iodev_data)
```

相关声明：[RTIO_IODEV_DEFINE](../rtio_core_reference/P001_RTIO公共接口.md#gaae51e2a679d37bc1cfba79961688c406)。

静态定义并初始化一个RTIO输入输出设备（IODev）。

## 5.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：IODEV提供api函数表与不透明data指针；RTIO_IODEV_DEFINE宏把它们静态保存到可迭代段（Iterable Section）中的对象，不深复制数据，也不启动硬件。data应按具体适配层要求指向有效对象，它不是固定类型的通用外设地址。

> 译注——源码核对：IODEV是RTIO提交目标，不是Zephyr struct device的类型别名。执行器调用api->submit，驱动通常排队或启动硬件后尽快返回，再通过rtio_iodev_sqe_ok／err报告完成。void返回类型没有提供同步的操作结果。

> 译注——源码核对：函数表及数据的生命周期必须覆盖异步请求，用户空间还需拥有相关IODEV访问权限。更多约定见[设备函数表](../rtio_model_reference/P004_RTIO设备函数表.md)和[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界。仓库相对链接用于定位同名文件，不将本机环境或任意本地版本作为读者前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 5.4\_原页交叉引用（Cross References）

- [查看此文件的源码](P006_RTIO设备头文件源码.md)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [RTIO_IODEV_DEFINE](../rtio_core_reference/P001_RTIO公共接口.md#gaae51e2a679d37bc1cfba79961688c406)

<a id="header-details"></a>

---

[上一章](P004_RTIO完成事件头文件源码.md) · [返回大纲](大纲.md) · [下一章](P006_RTIO设备头文件源码.md)
