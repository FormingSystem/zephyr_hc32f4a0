---
id: learning.zephyr-docs.rtio-model-reference.page-4
title: RTIO设备函数表
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_RTIO设备函数表

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__iodev__api.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

RTIO输入输出设备应实现的API。

```c
#include <zephyr/rtio/iodev.h>
```

<a id="details"></a>

RTIO输入输出设备应实现的API。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 4.1\_数据成员（Data Fields）

<a id="r_a6cd795906753535571ec1ecc0e0c430c"></a>

```c
void(* submit )(struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[submit](#a6cd795906753535571ec1ecc0e0c430c)、[rtio_iodev_sqe](P005_RTIO设备提交条目.md)。

向IODEV提交一个待处理的条目。

## 4.2\_详细说明（Detailed Documentation）

<a id="a6cd795906753535571ec1ecc0e0c430c"></a>

### `submit`

```c
void(* rtio_iodev_api::submit) (struct rtio_iodev_sqe *iodev_sqe)
```

向IODEV提交一个待处理的条目。

此调用应当很快返回，通常只是把条目入队，或启动硬件处理该条目。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iodev_sqe` | 提交队列条目（Submission Queue Entry）。 |

## 4.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：此函数指针返回`void`。驱动通常在submit中排队或启动硬件，然后通过`rtio_iodev_sqe_ok()`或`rtio_iodev_sqe_err()`向执行器报告最终结果。submit返回本身不是I/O完成，也没有整数返回码可直接当作操作结果。

> 译注——源码核对：原文要求调用持续时间较短，没有把submit声明为始终运行在某个专用线程。当前执行器在推进链、事务或完成回调时可能继续提交，驱动必须按其实际调用上下文安排阻塞工作。完整生命周期见[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.4\_原页交叉引用（Cross References）

- [zephyr/rtio/iodev.h](../rtio_headers_reference/P006_RTIO设备头文件源码.md)
- [rtio_iodev_sqe](P005_RTIO设备提交条目.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P003_RTIO输入输出设备.md) · [返回大纲](大纲.md) · [下一章](P005_RTIO设备提交条目.md)
