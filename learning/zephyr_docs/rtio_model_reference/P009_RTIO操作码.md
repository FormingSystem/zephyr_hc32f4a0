---
id: learning.zephyr-docs.rtio-model-reference.page-9
title: RTIO操作码
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__ops.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_RTIO操作码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__ops.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

RTIO提交队列事件操作码（SQE Operation Codes）。

<a id="details"></a>

RTIO提交队列事件操作码（SQE Operation Codes）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.1\_宏定义（Macros）

<a id="r_gad5f073978f641413989d1c6b405d6c36"></a>

```c
#define RTIO_OP_NOP 0
```

相关声明：[RTIO_OP_NOP](#gad5f073978f641413989d1c6b405d6c36)。

不执行任何动作并立即完成的操作。

<a id="r_gafeb05c351207cd1638fa78f6607e1a4a"></a>

```c
#define RTIO_OP_RX (RTIO_OP_NOP+1)
```

相关声明：[RTIO_OP_RX](#gafeb05c351207cd1638fa78f6607e1a4a)、[RTIO_OP_NOP](#gad5f073978f641413989d1c6b405d6c36)。

执行接收（读取）的操作。

<a id="r_ga8dcaef0cda159e16520a95543ff62827"></a>

```c
#define RTIO_OP_TX (RTIO_OP_RX+1)
```

相关声明：[RTIO_OP_TX](#ga8dcaef0cda159e16520a95543ff62827)、[RTIO_OP_RX](#gafeb05c351207cd1638fa78f6607e1a4a)。

执行发送（写入）的操作。

<a id="r_ga6f95c0a5fbcc020a0d1102d3b08934bd"></a>

```c
#define RTIO_OP_TINY_TX (RTIO_OP_TX+1)
```

相关声明：[RTIO_OP_TINY_TX](#ga6f95c0a5fbcc020a0d1102d3b08934bd)、[RTIO_OP_TX](#ga8dcaef0cda159e16520a95543ff62827)。

通过复制待写数据执行微量写入（Tiny Write）的发送操作。

<a id="r_ga18e0ff7d44e4c33900106aefad0a8508"></a>

```c
#define RTIO_OP_CALLBACK (RTIO_OP_TINY_TX+1)
```

相关声明：[RTIO_OP_CALLBACK](#ga18e0ff7d44e4c33900106aefad0a8508)、[RTIO_OP_TINY_TX](#ga6f95c0a5fbcc020a0d1102d3b08934bd)。

调用给定函数，即回调（Callback）的操作。

<a id="r_ga9f0e70f5a28be65a8ed67c0257a72692"></a>

```c
#define RTIO_OP_TXRX (RTIO_OP_CALLBACK+1)
```

相关声明：[RTIO_OP_TXRX](#ga9f0e70f5a28be65a8ed67c0257a72692)、[RTIO_OP_CALLBACK](#ga18e0ff7d44e4c33900106aefad0a8508)。

执行收发（Transceive），即同时读取和写入的操作。

<a id="r_gae8da4da54f32963190f52c7533d4c951"></a>

```c
#define RTIO_OP_DELAY (RTIO_OP_TXRX+1)
```

相关声明：[RTIO_OP_DELAY](#gae8da4da54f32963190f52c7533d4c951)、[RTIO_OP_TXRX](#ga9f0e70f5a28be65a8ed67c0257a72692)。

异步等待指定时长后才完成的操作。

<a id="r_ga3b4f9b1ee1612290323161ecc16e0859"></a>

```c
#define RTIO_OP_I2C_RECOVER (RTIO_OP_DELAY+1)
```

相关声明：[RTIO_OP_I2C_RECOVER](#ga3b4f9b1ee1612290323161ecc16e0859)、[RTIO_OP_DELAY](#gae8da4da54f32963190f52c7533d4c951)。

恢复I2C总线的操作。

<a id="r_gad987be3acfe406b11419c7e8cd068cf5"></a>

```c
#define RTIO_OP_I2C_CONFIGURE (RTIO_OP_I2C_RECOVER+1)
```

相关声明：[RTIO_OP_I2C_CONFIGURE](#gad987be3acfe406b11419c7e8cd068cf5)、[RTIO_OP_I2C_RECOVER](#ga3b4f9b1ee1612290323161ecc16e0859)。

配置I2C总线的操作。

<a id="r_gac69023c6902570e7511edd044d6d9d94"></a>

```c
#define RTIO_OP_I3C_RECOVER (RTIO_OP_I2C_CONFIGURE+1)
```

相关声明：[RTIO_OP_I3C_RECOVER](#gac69023c6902570e7511edd044d6d9d94)、[RTIO_OP_I2C_CONFIGURE](#gad987be3acfe406b11419c7e8cd068cf5)。

恢复I3C总线的操作。

<a id="r_gaa77874941380a8215ec57b30d993d437"></a>

```c
#define RTIO_OP_I3C_CONFIGURE (RTIO_OP_I3C_RECOVER+1)
```

相关声明：[RTIO_OP_I3C_CONFIGURE](#gaa77874941380a8215ec57b30d993d437)、[RTIO_OP_I3C_RECOVER](#gac69023c6902570e7511edd044d6d9d94)。

配置I3C总线的操作。

<a id="r_ga691ea387929db1224d6343fd91dfd2c5"></a>

```c
#define RTIO_OP_I3C_CCC (RTIO_OP_I3C_CONFIGURE+1)
```

相关声明：[RTIO_OP_I3C_CCC](#ga691ea387929db1224d6343fd91dfd2c5)、[RTIO_OP_I3C_CONFIGURE](#gaa77874941380a8215ec57b30d993d437)。

发送I3C公共命令码（Common Command Code，CCC）的操作。

<a id="r_gad74290935595b83040676b426cd07161"></a>

```c
#define RTIO_OP_AWAIT (RTIO_OP_I3C_CCC+1)
```

相关声明：[RTIO_OP_AWAIT](#gad74290935595b83040676b426cd07161)、[RTIO_OP_I3C_CCC](#ga691ea387929db1224d6343fd91dfd2c5)。

等待信号的操作；如果提供了IODEV，则在等待期间阻塞该IODEV。

## 9.2\_详细说明（Detailed Documentation）

<a id="gad74290935595b83040676b426cd07161"></a>

### `RTIO_OP_AWAIT`

```c
#define RTIO_OP_AWAIT (RTIO_OP_I3C_CCC+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

等待信号的操作；如果提供了IODEV，则在等待期间阻塞该IODEV。

<a id="ga18e0ff7d44e4c33900106aefad0a8508"></a>

### `RTIO_OP_CALLBACK`

```c
#define RTIO_OP_CALLBACK (RTIO_OP_TINY_TX+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

调用给定函数，即回调（Callback）的操作。

<a id="gae8da4da54f32963190f52c7533d4c951"></a>

### `RTIO_OP_DELAY`

```c
#define RTIO_OP_DELAY (RTIO_OP_TXRX+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

异步等待指定时长后才完成的操作。

<a id="gad987be3acfe406b11419c7e8cd068cf5"></a>

### `RTIO_OP_I2C_CONFIGURE`

```c
#define RTIO_OP_I2C_CONFIGURE (RTIO_OP_I2C_RECOVER+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

配置I2C总线的操作。

<a id="ga3b4f9b1ee1612290323161ecc16e0859"></a>

### `RTIO_OP_I2C_RECOVER`

```c
#define RTIO_OP_I2C_RECOVER (RTIO_OP_DELAY+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

恢复I2C总线的操作。

<a id="ga691ea387929db1224d6343fd91dfd2c5"></a>

### `RTIO_OP_I3C_CCC`

```c
#define RTIO_OP_I3C_CCC (RTIO_OP_I3C_CONFIGURE+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

发送I3C公共命令码（Common Command Code，CCC）的操作。

<a id="gaa77874941380a8215ec57b30d993d437"></a>

### `RTIO_OP_I3C_CONFIGURE`

```c
#define RTIO_OP_I3C_CONFIGURE (RTIO_OP_I3C_RECOVER+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

配置I3C总线的操作。

<a id="gac69023c6902570e7511edd044d6d9d94"></a>

### `RTIO_OP_I3C_RECOVER`

```c
#define RTIO_OP_I3C_RECOVER (RTIO_OP_I2C_CONFIGURE+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

恢复I3C总线的操作。

<a id="gad5f073978f641413989d1c6b405d6c36"></a>

### `RTIO_OP_NOP`

```c
#define RTIO_OP_NOP 0
```

```c
#include <zephyr/rtio/sqe.h>
```

不执行任何动作并立即完成的操作。

<a id="gafeb05c351207cd1638fa78f6607e1a4a"></a>

### `RTIO_OP_RX`

```c
#define RTIO_OP_RX (RTIO_OP_NOP+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

执行接收（读取）的操作。

<a id="ga6f95c0a5fbcc020a0d1102d3b08934bd"></a>

### `RTIO_OP_TINY_TX`

```c
#define RTIO_OP_TINY_TX (RTIO_OP_TX+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

通过复制待写数据执行微量写入（Tiny Write）的发送操作。

<a id="ga8dcaef0cda159e16520a95543ff62827"></a>

### `RTIO_OP_TX`

```c
#define RTIO_OP_TX (RTIO_OP_RX+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

执行发送（写入）的操作。

<a id="ga9f0e70f5a28be65a8ed67c0257a72692"></a>

### `RTIO_OP_TXRX`

```c
#define RTIO_OP_TXRX (RTIO_OP_CALLBACK+1)
```

```c
#include <zephyr/rtio/sqe.h>
```

执行收发（Transceive），即同时读取和写入的操作。

## 9.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：这些宏定义操作标识，并不保证每个IODEV都支持所有操作。执行器对无IODEV的条目只专门处理CALLBACK与AWAIT，其他操作走错误分支；有IODEV时由其submit处理。因此NOP的“立即完成”描述也要结合所选IODEV实现，不能把NULL设备的任意操作当成通用执行器服务。

> 译注——源码核对：`RTIO_OP_DELAY`由配置启用的共享超时IODEV处理，准备辅助函数会填入该设备；在IODEV接收提交时才计算到期时间。`RTIO_OP_AWAIT`则等待显式信号，是否阻塞总线由提供的IODEV及其驱动决定，两个操作不能相互替代。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 9.4\_原页交叉引用（Cross References）

- [zephyr/rtio/sqe.h](../rtio_headers_reference/P001_RTIO提交事件头文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P008_RTIO完成事件标志.md) · [返回大纲](大纲.md) · [下一章](P010_RTIO提交事件标志.md)
