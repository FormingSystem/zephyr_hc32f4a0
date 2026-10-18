---
id: learning.zephyr-docs.rtio-headers-reference.page-1
title: RTIO提交事件头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/sqe_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_RTIO提交事件头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/sqe_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入SQE、CQE和IODEV三个头文件的参考与源码浏览页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

RTIO提交队列事件（Submission Queue Events）及相关函数。

<a id="details"></a>

```c
#include <stdint.h>
#include <string.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/atomic.h>
#include <zephyr/sys/mpsc_lockfree.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

RTIO提交队列事件（Submission Queue Events）及相关函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_rtio_5Fsqe"></a>

```c
struct rtio_sqe
```

相关声明：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

一个提交队列事件（Submission Queue Event，SQE）。

<a id="r_rtio_5Fiodev_5Fsqe"></a>

```c
struct rtio_iodev_sqe
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.2\_宏定义（Macros）

<a id="r_gabc81232a7d4b7145d9898afd6ff2ae48"></a>

```c
#define RTIO_PRIO_LOW 0U
```

相关声明：[RTIO_PRIO_LOW](../rtio_model_reference/P011_RTIO优先级.md#gabc81232a7d4b7145d9898afd6ff2ae48)。

低优先级（Low Priority）。

<a id="r_gab02e27e01b7dd4eb3439df557899ce92"></a>

```c
#define RTIO_PRIO_NORM 127U
```

相关声明：[RTIO_PRIO_NORM](../rtio_model_reference/P011_RTIO优先级.md#gab02e27e01b7dd4eb3439df557899ce92)。

普通优先级（Normal Priority）。

<a id="r_ga220baa9bf2c8ff0cb6f52f0220e72b30"></a>

```c
#define RTIO_PRIO_HIGH 255U
```

相关声明：[RTIO_PRIO_HIGH](../rtio_model_reference/P011_RTIO优先级.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)。

高优先级（High Priority）。

<a id="r_gae9191d521d4ab602b53fefb74020d06b"></a>

```c
#define RTIO_SQE_CHAINED BIT(0)
```

相关声明：[RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

队列中的下一个请求应等待此请求。

<a id="r_ga07f09cc0c95be6cfdddb23f8acacb1ea"></a>

```c
#define RTIO_SQE_TRANSACTION BIT(1)
```

相关声明：[RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

队列中的下一个请求属于同一事务（Transaction）。

<a id="r_ga2802b46584220afffa0e959e149d5a4d"></a>

```c
#define RTIO_SQE_MEMPOOL_BUFFER BIT(2)
```

相关声明：[RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

缓冲区应由RTIO内存池分配。

<a id="r_ga7f7f9b038ab8409f271b1aebc1b95ee6"></a>

```c
#define RTIO_SQE_CANCELED BIT(3)
```

相关声明：[RTIO_SQE_CANCELED](../rtio_model_reference/P010_RTIO提交事件标志.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

如果可能，不应执行该SQE。

<a id="r_ga00f8ead8f043fe40d49d0bc3325fb299"></a>

```c
#define RTIO_SQE_MULTISHOT BIT(4)
```

相关声明：[RTIO_SQE_MULTISHOT](../rtio_model_reference/P010_RTIO提交事件标志.md#ga00f8ead8f043fe40d49d0bc3325fb299)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该SQE应持续产生CQE，直到被取消。

<a id="r_ga8578ffdb8f53a51b94fa86a6f02d4a11"></a>

```c
#define RTIO_SQE_NO_RESPONSE BIT(5)
```

相关声明：[RTIO_SQE_NO_RESPONSE](../rtio_model_reference/P010_RTIO提交事件标志.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该SQE不产生CQE。

<a id="r_gad5f073978f641413989d1c6b405d6c36"></a>

```c
#define RTIO_OP_NOP 0
```

相关声明：[RTIO_OP_NOP](../rtio_model_reference/P009_RTIO操作码.md#gad5f073978f641413989d1c6b405d6c36)。

不执行任何动作并立即完成的操作。

<a id="r_gafeb05c351207cd1638fa78f6607e1a4a"></a>

```c
#define RTIO_OP_RX (RTIO_OP_NOP+1)
```

相关声明：[RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)、[RTIO_OP_NOP](../rtio_model_reference/P009_RTIO操作码.md#gad5f073978f641413989d1c6b405d6c36)。

执行接收（读取）的操作。

<a id="r_ga8dcaef0cda159e16520a95543ff62827"></a>

```c
#define RTIO_OP_TX (RTIO_OP_RX+1)
```

相关声明：[RTIO_OP_TX](../rtio_model_reference/P009_RTIO操作码.md#ga8dcaef0cda159e16520a95543ff62827)、[RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)。

执行发送（写入）的操作。

<a id="r_ga6f95c0a5fbcc020a0d1102d3b08934bd"></a>

```c
#define RTIO_OP_TINY_TX (RTIO_OP_TX+1)
```

相关声明：[RTIO_OP_TINY_TX](../rtio_model_reference/P009_RTIO操作码.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)、[RTIO_OP_TX](../rtio_model_reference/P009_RTIO操作码.md#ga8dcaef0cda159e16520a95543ff62827)。

通过复制待写数据执行微量写入（Tiny Write）的发送操作。

<a id="r_ga18e0ff7d44e4c33900106aefad0a8508"></a>

```c
#define RTIO_OP_CALLBACK (RTIO_OP_TINY_TX+1)
```

相关声明：[RTIO_OP_CALLBACK](../rtio_model_reference/P009_RTIO操作码.md#ga18e0ff7d44e4c33900106aefad0a8508)、[RTIO_OP_TINY_TX](../rtio_model_reference/P009_RTIO操作码.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)。

调用给定函数，即回调（Callback）的操作。

<a id="r_ga9f0e70f5a28be65a8ed67c0257a72692"></a>

```c
#define RTIO_OP_TXRX (RTIO_OP_CALLBACK+1)
```

相关声明：[RTIO_OP_TXRX](../rtio_model_reference/P009_RTIO操作码.md#ga9f0e70f5a28be65a8ed67c0257a72692)、[RTIO_OP_CALLBACK](../rtio_model_reference/P009_RTIO操作码.md#ga18e0ff7d44e4c33900106aefad0a8508)。

执行收发（Transceive），即同时读取和写入的操作。

<a id="r_gae8da4da54f32963190f52c7533d4c951"></a>

```c
#define RTIO_OP_DELAY (RTIO_OP_TXRX+1)
```

相关声明：[RTIO_OP_DELAY](../rtio_model_reference/P009_RTIO操作码.md#gae8da4da54f32963190f52c7533d4c951)、[RTIO_OP_TXRX](../rtio_model_reference/P009_RTIO操作码.md#ga9f0e70f5a28be65a8ed67c0257a72692)。

异步等待指定时长后才完成的操作。

<a id="r_ga3b4f9b1ee1612290323161ecc16e0859"></a>

```c
#define RTIO_OP_I2C_RECOVER (RTIO_OP_DELAY+1)
```

相关声明：[RTIO_OP_I2C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#ga3b4f9b1ee1612290323161ecc16e0859)、[RTIO_OP_DELAY](../rtio_model_reference/P009_RTIO操作码.md#gae8da4da54f32963190f52c7533d4c951)。

恢复I2C总线的操作。

<a id="r_gad987be3acfe406b11419c7e8cd068cf5"></a>

```c
#define RTIO_OP_I2C_CONFIGURE (RTIO_OP_I2C_RECOVER+1)
```

相关声明：[RTIO_OP_I2C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gad987be3acfe406b11419c7e8cd068cf5)、[RTIO_OP_I2C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#ga3b4f9b1ee1612290323161ecc16e0859)。

配置I2C总线的操作。

<a id="r_gac69023c6902570e7511edd044d6d9d94"></a>

```c
#define RTIO_OP_I3C_RECOVER (RTIO_OP_I2C_CONFIGURE+1)
```

相关声明：[RTIO_OP_I3C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#gac69023c6902570e7511edd044d6d9d94)、[RTIO_OP_I2C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gad987be3acfe406b11419c7e8cd068cf5)。

恢复I3C总线的操作。

<a id="r_gaa77874941380a8215ec57b30d993d437"></a>

```c
#define RTIO_OP_I3C_CONFIGURE (RTIO_OP_I3C_RECOVER+1)
```

相关声明：[RTIO_OP_I3C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gaa77874941380a8215ec57b30d993d437)、[RTIO_OP_I3C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#gac69023c6902570e7511edd044d6d9d94)。

配置I3C总线的操作。

<a id="r_ga691ea387929db1224d6343fd91dfd2c5"></a>

```c
#define RTIO_OP_I3C_CCC (RTIO_OP_I3C_CONFIGURE+1)
```

相关声明：[RTIO_OP_I3C_CCC](../rtio_model_reference/P009_RTIO操作码.md#ga691ea387929db1224d6343fd91dfd2c5)、[RTIO_OP_I3C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gaa77874941380a8215ec57b30d993d437)。

发送I3C公共命令码（Common Command Code，CCC）的操作。

<a id="r_gad74290935595b83040676b426cd07161"></a>

```c
#define RTIO_OP_AWAIT (RTIO_OP_I3C_CCC+1)
```

相关声明：[RTIO_OP_AWAIT](../rtio_model_reference/P009_RTIO操作码.md#gad74290935595b83040676b426cd07161)、[RTIO_OP_I3C_CCC](../rtio_model_reference/P009_RTIO操作码.md#ga691ea387929db1224d6343fd91dfd2c5)。

等待信号的操作；如果提供了IODEV，则在等待期间阻塞该IODEV。

<a id="r_gaf923e862d2c6a3fbce5eb96781cf86d8"></a>

```c
#define RTIO_IODEV_I2C_STOP BIT(1)
```

相关声明：[RTIO_IODEV_I2C_STOP](../hardware/P442_RTIO的I2C标志.md#gaf923e862d2c6a3fbce5eb96781cf86d8)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I2C_MSG_STOP`停止（Stop）标志。

<a id="r_gadba1c5eddeecc431000bd92054f55c3a"></a>

```c
#define RTIO_IODEV_I2C_RESTART BIT(2)
```

相关声明：[RTIO_IODEV_I2C_RESTART](../hardware/P442_RTIO的I2C标志.md#gadba1c5eddeecc431000bd92054f55c3a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I2C_MSG_RESTART`重新开始（Restart）标志。

<a id="r_gaa0c3b047c7205d12775d8d38907119b9"></a>

```c
#define RTIO_IODEV_I2C_10_BITS BIT(3)
```

相关声明：[RTIO_IODEV_I2C_10_BITS](../hardware/P442_RTIO的I2C标志.md#gaa0c3b047c7205d12775d8d38907119b9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I2C_MSG_ADDR_10_BITS`，使用10位地址（10-bit Address）。

<a id="r_ga671a479885f4d9abbdad677ddfbc47df"></a>

```c
#define RTIO_IODEV_I3C_STOP BIT(1)
```

相关声明：[RTIO_IODEV_I3C_STOP](../hardware/P434_RTIO的I3C标志.md#ga671a479885f4d9abbdad677ddfbc47df)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I3C_MSG_STOP`停止（Stop）标志。

<a id="r_ga9d30e1b8f22da07a25fd379c27dc2afe"></a>

```c
#define RTIO_IODEV_I3C_RESTART BIT(2)
```

相关声明：[RTIO_IODEV_I3C_RESTART](../hardware/P434_RTIO的I3C标志.md#ga9d30e1b8f22da07a25fd379c27dc2afe)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I3C_MSG_RESTART`重新开始（Restart）标志。

<a id="r_ga857a1b2a766faa1438b4b07d73ca05ed"></a>

```c
#define RTIO_IODEV_I3C_HDR BIT(3)
```

相关声明：[RTIO_IODEV_I3C_HDR](../hardware/P434_RTIO的I3C标志.md#ga857a1b2a766faa1438b4b07d73ca05ed)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I3C_MSG_HDR`高数据速率（High Data Rate，HDR）标志。

<a id="r_ga258aae8fdda81c71d08dc3e26feb843d"></a>

```c
#define RTIO_IODEV_I3C_NBCH BIT(4)
```

相关声明：[RTIO_IODEV_I3C_NBCH](../hardware/P434_RTIO的I3C标志.md#ga258aae8fdda81c71d08dc3e26feb843d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I3C_MSG_NBCH`，省略广播头（No Broadcast Header）。

<a id="r_gaeea22dddf91eb4e9de44a907d799044e"></a>

```c
#define RTIO_IODEV_I3C_NOACK_EXPECTED BIT(5)
```

相关声明：[RTIO_IODEV_I3C_NOACK_EXPECTED](../hardware/P434_RTIO的I3C标志.md#gaeea22dddf91eb4e9de44a907d799044e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

等效于`I3C_MSG_NOACK_EXPECTED`，不期望收到确认（No ACK Expected）。

<a id="r_ga5e278e6ec0c31de2246c0fa9a96425c8"></a>

```c
#define RTIO_IODEV_I3C_HDR_MODE_MASK GENMASK(15, 8)
```

相关声明：[RTIO_IODEV_I3C_HDR_MODE_MASK](../hardware/P434_RTIO的I3C标志.md#ga5e278e6ec0c31de2246c0fa9a96425c8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

I3C高数据速率（High Data Rate，HDR）模式掩码（Mode Mask）。

<a id="r_gae2b6caf5fa82cc7dc07508dccfeb423b"></a>

```c
#define RTIO_IODEV_I3C_HDR_MODE_SET(flags)
```

相关声明：[RTIO_IODEV_I3C_HDR_MODE_SET](../hardware/P434_RTIO的I3C标志.md#gae2b6caf5fa82cc7dc07508dccfeb423b)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

I3C高数据速率（High Data Rate，HDR）模式掩码（Mode Mask）。

<a id="r_ga902a66ba8772f7a2395069e6725776da"></a>

```c
#define RTIO_IODEV_I3C_HDR_MODE_GET(flags)
```

相关声明：[RTIO_IODEV_I3C_HDR_MODE_GET](../hardware/P434_RTIO的I3C标志.md#ga902a66ba8772f7a2395069e6725776da)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

I3C高数据速率（High Data Rate，HDR）模式掩码（Mode Mask）。

<a id="r_ga0642bb5c69d01ea0fe148da9b8475328"></a>

```c
#define RTIO_IODEV_I3C_HDR_CMD_CODE_MASK GENMASK(22, 16)
```

相关声明：[RTIO_IODEV_I3C_HDR_CMD_CODE_MASK](../hardware/P434_RTIO的I3C标志.md#ga0642bb5c69d01ea0fe148da9b8475328)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

I3C高数据速率（HDR）7位命令码（7-bit Command Code）。

<a id="r_ga4d0b165eb8f4a7cc63c35e9f9438ee5a"></a>

```c
#define RTIO_IODEV_I3C_HDR_CMD_CODE_SET(flags)
```

相关声明：[RTIO_IODEV_I3C_HDR_CMD_CODE_SET](../hardware/P434_RTIO的I3C标志.md#ga4d0b165eb8f4a7cc63c35e9f9438ee5a)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

I3C高数据速率（HDR）7位命令码（7-bit Command Code）。

<a id="r_ga881fcb3d955aece099266ef5b57e767b"></a>

```c
#define RTIO_IODEV_I3C_HDR_CMD_CODE_GET(flags)
```

相关声明：[RTIO_IODEV_I3C_HDR_CMD_CODE_GET](../hardware/P434_RTIO的I3C标志.md#ga881fcb3d955aece099266ef5b57e767b)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

I3C高数据速率（HDR）7位命令码（7-bit Command Code）。

<a id="r_gad45b80544e4e894cf170fe44fb752930"></a>

```c
#define rtio_sqe_prep_delay(sqe, timeout, userdata)
```

相关声明：[rtio_sqe_prep_delay](../rtio_core_reference/P001_RTIO公共接口.md#gad45b80544e4e894cf170fe44fb752930)。

准备一个延时操作（Delay Operation）提交，在指定超时后完成。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga5d5b7d440eab064918424b0261455a9f"></a>

```c
typedef void(* rtio_callback_t) (struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0)
```

相关声明：[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

`RTIO_OP_CALLBACK`的回调函数签名（Callback Signature）。

<a id="r_gab254ffa4d10bfb670bacd1c47c1f8711"></a>

```c
typedef void(* rtio_signaled_t) (struct rtio_iodev_sqe *iodev_sqe, void *userdata)
```

相关声明：[rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

`RTIO_OP_AWAIT`收到信号时的回调函数签名（Callback Signature）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga599ee43fdf35e1cf895cbbe9272e4c50"></a>

```c
static void rtio_sqe_prep_nop (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, void *userdata)
```

相关声明：[rtio_sqe_prep_nop](../rtio_core_reference/P001_RTIO公共接口.md#ga599ee43fdf35e1cf895cbbe9272e4c50)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

准备一个空操作（No Operation，NOP）提交。

<a id="r_ga89c7cc2494e3dda50737f78f1a1376cf"></a>

```c
static void rtio_sqe_prep_read (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint8_t *buf, uint32_t len, void *userdata)
```

相关声明：[rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个读操作（Read Operation）提交。

<a id="r_ga15c1f623658d27d300d1a31a6f3d6b9d"></a>

```c
static void rtio_sqe_prep_read_with_pool (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_read_with_pool](../rtio_core_reference/P001_RTIO公共接口.md#ga15c1f623658d27d300d1a31a6f3d6b9d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个使用上下文内存池的读操作提交。

<a id="r_ga9803aa829f8c0eeee746ea7d872c20cc"></a>

```c
static void rtio_sqe_prep_read_multishot (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_read_multishot](../rtio_core_reference/P001_RTIO公共接口.md#ga9803aa829f8c0eeee746ea7d872c20cc)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个使用上下文内存池的多次完成读操作（Multishot Read）提交。

<a id="r_ga7f7856d1f4fd1d8c4f6eebcccfe77701"></a>

```c
static void rtio_sqe_prep_write (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *buf, uint32_t len, void *userdata)
```

相关声明：[rtio_sqe_prep_write](../rtio_core_reference/P001_RTIO公共接口.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个写操作（Write Operation）提交。

<a id="r_ga31be14ece09e061a8d42ca8f2395286a"></a>

```c
static void rtio_sqe_prep_tiny_write (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tiny_write_data, uint8_t tiny_write_len, void *userdata)
```

相关声明：[rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

准备一个微量写操作（Tiny Write）提交。

<a id="r_ga9d0dd7d0e2e3d281092f2350d6e1713e"></a>

```c
static void rtio_sqe_prep_callback (struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

相关声明：[rtio_sqe_prep_callback](../rtio_core_reference/P001_RTIO公共接口.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)。

准备一个回调操作（Callback Operation）提交。

<a id="r_gae87be354087d038953dae07c7f9cd3b0"></a>

```c
static void rtio_sqe_prep_callback_no_cqe (struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

相关声明：[rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)。

准备一个不产生CQE的回调操作提交。

<a id="r_gab9b605dcbb01d21c88f9ae70588ea3b5"></a>

```c
static void rtio_sqe_prep_transceive (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tx_buf, uint8_t *rx_buf, uint32_t buf_len, void *userdata)
```

相关声明：[rtio_sqe_prep_transceive](../rtio_core_reference/P001_RTIO公共接口.md#gab9b605dcbb01d21c88f9ae70588ea3b5)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个收发操作（Transceive Operation）提交。

<a id="r_gafd97c145b8525895494a31a87610f65d"></a>

```c
static void rtio_sqe_prep_await (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await](../rtio_core_reference/P001_RTIO公共接口.md#gafd97c145b8525895494a31a87610f65d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作（Await Operation）提交。

<a id="r_ga5e55583901cd13d24f60744747c5c72b"></a>

```c
static void rtio_sqe_prep_await_iodev (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await_iodev](../rtio_core_reference/P001_RTIO公共接口.md#ga5e55583901cd13d24f60744747c5c72b)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作提交，该操作会阻塞`rtio_iodev`直至完成。

<a id="r_gaa2f35d2909f4a19003199a3fd759fc41"></a>

```c
static void rtio_sqe_prep_await_executor (struct rtio_sqe *sqe, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_await_executor](../rtio_core_reference/P001_RTIO公共接口.md#gaa2f35d2909f4a19003199a3fd759fc41)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个等待操作提交，该操作在收到信号后完成SQE。

<a id="r_gabcb356e1df7b39bbb6f732d6fa6cc97d"></a>

```c
static void rtio_sqe_prep_i2c_configure (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint32_t dev_config, void *userdata)
```

相关声明：[rtio_sqe_prep_i2c_configure](../rtio_core_reference/P001_RTIO公共接口.md#gabcb356e1df7b39bbb6f732d6fa6cc97d)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

准备一个I2C配置操作（Configure Operation）提交。

<a id="r_ga274cb5490582b38682f255cac4703143"></a>

```c
static void rtio_sqe_prep_i2c_recover (struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, void *userdata)
```

相关声明：[rtio_sqe_prep_i2c_recover](../rtio_core_reference/P001_RTIO公共接口.md#ga274cb5490582b38682f255cac4703143)、[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)。

准备一个I2C总线恢复操作（Recover Operation）提交。

<a id="r_gaef904eb6a8810d8c3ea537c4d6edbee5"></a>

```c
static struct rtio_iodev_sqe * rtio_txn_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_txn_next](../rtio_core_reference/P001_RTIO公共接口.md#gaef904eb6a8810d8c3ea537c4d6edbee5)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取事务（Transaction）中的下一个SQE。

<a id="r_gada1e3abf92a46e376138435debc8baf4"></a>

```c
static struct rtio_iodev_sqe * rtio_chain_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_chain_next](../rtio_core_reference/P001_RTIO公共接口.md#gada1e3abf92a46e376138435debc8baf4)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取链（Chain）中的下一个SQE。

<a id="r_gae690e3dc0fc40dda57257b2eed432719"></a>

```c
static struct rtio_iodev_sqe * rtio_iodev_sqe_next (const struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_iodev_sqe_next](../rtio_core_reference/P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

获取链或事务中的下一个SQE。

<a id="r_ga7d2e5673582f32b630e2294dfbf0fe44"></a>

```c
static void rtio_iodev_sqe_await_signal (struct rtio_iodev_sqe *iodev_sqe, rtio_signaled_t callback, void *userdata)
```

相关声明：[rtio_iodev_sqe_await_signal](../rtio_core_reference/P001_RTIO公共接口.md#ga7d2e5673582f32b630e2294dfbf0fe44)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)。

从RTIO IODEV等待一个AWAIT SQE信号。

## 1.5\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：准备（Prepare）与提交（Submit）分开：prep函数只设置SQE，不启动硬件。多数准备函数直接或通过共同辅助函数先memset清零整个公开SQE，再写操作字段；因此CHAINED、TRANSACTION和总线iodev_flags等附加标志应在准备之后按需要设置，不能先设置再假定prep会保留。参考[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)和[SQE结构](../rtio_model_reference/P007_RTIO提交事件.md)。

> 译注——源码核对：普通读写及收发准备函数只保存缓冲区指针，内存必须在异步使用期间有效。微量写（Tiny Write）通过memcpy复制到本次为7字节的内嵌数组中；长度和非空检查使用断言，不是返回错误码的运行时校验。不能因为关闭断言就传入越界长度或无效指针。

> 译注——源码核对：内存池读准备函数先保存NULL缓冲区和0长度，再设置MEMPOOL_BUFFER；并非准备完成就已经取得内存块。多次完成读（Multishot Read）另外设置MULTISHOT，后续分配、重提与错误清理由驱动、核心辅助函数和执行器完成。

> 译注——源码核对：回调（Callback）准备函数把iodev设为NULL，交给执行器执行。no_cqe变体额外设置NO_RESPONSE，避免完成回调本身再产生一个CQE；此标志也影响提交等待时能收到的完成事件数量。用户模式支持范围另由系统调用校验限制，不能把任意内核回调地址提交为用户操作。

> 译注——源码核对：AWAIT准备函数清零状态；注册等待回调与发送信号分别尝试0→1的原子比较并交换（CAS），后到的一方调用回调。它不是累计任意多次通知的计数器，重复发信号或在SQE回收后继续使用句柄不在此前提内。提供IODEV时是否正确保持总线阻塞仍由该设备驱动负责。

> 译注——源码核对：DELAY启用时，同名准备函数保存timeout并指向共享rtio_timeout_iodev；禁用时宏分支触发BUILD_ASSERT。共享超时实现从IODEV接收提交时计算到期点，不能把准备时刻当作延时起点。

> 译注——源码核对：`rtio_txn_next()`和`rtio_chain_next()`先检查当前SQE对应标志再返回next；`rtio_iodev_sqe_next()`直接返回next。原接口说明中前两者的返回类型写作rtio_sqe*，当前声明实际为rtio_iodev_sqe*。链与事务链接由执行器建立，不能对尚未链接的孤立SQE假定next有效。

> 译注——源码核对：SQE对象池分配只取出空闲节点并减少pool_free，不在这个内部函数中清零整个对象；公开prep函数负责设置操作字段。对象回收后旧指针不可继续代表原请求。对象池宏仅建立存储及元数据，启动时的rtio_init()把各节点加入空闲队列。

> 译注——源码核对：缓存行注释提到常见64字节，但当前检查由CONFIG_RTIO_SQE_CACHELINE_CHECK控制，比较的是sizeof(struct rtio_iodev_sqe)；若定义CONFIG_DCACHE_LINE_SIZE则使用该值，否则回退到64。断言条件为小于等于，并不证明所有构建中条目恰为64字节。SQE内存放置选项也不等同于任意数据缓冲区自动满足DMA或缓存一致性要求。

> 译注——源码核对：源码中的操作优先级字段是uint8_t，而部分准备函数参数使用int8_t，本页原样保留声明；不要擅自改成另一套接口。操作优先级是否用于仲裁由驱动决定，不能与线程优先级混同。I2C／I3C设备标志位于iodev_flags，不能与SQE的链、事务或内存池标志相互替代。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界。仓库相对链接用于定位同名文件，不将本机环境或任意本地版本作为读者前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h_source.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/sys/atomic.h](../atomic_reference/P003_原子操作公共头文件源码.md)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P162_MPSC无锁队列完整头文件.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码](P002_RTIO提交事件头文件源码.md)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [RTIO_PRIO_LOW](../rtio_model_reference/P011_RTIO优先级.md#gabc81232a7d4b7145d9898afd6ff2ae48)
- [RTIO_PRIO_NORM](../rtio_model_reference/P011_RTIO优先级.md#gab02e27e01b7dd4eb3439df557899ce92)
- [RTIO_PRIO_HIGH](../rtio_model_reference/P011_RTIO优先级.md#ga220baa9bf2c8ff0cb6f52f0220e72b30)
- [RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)
- [RTIO_SQE_MEMPOOL_BUFFER](../rtio_model_reference/P010_RTIO提交事件标志.md#ga2802b46584220afffa0e959e149d5a4d)
- [RTIO_SQE_CANCELED](../rtio_model_reference/P010_RTIO提交事件标志.md#ga7f7f9b038ab8409f271b1aebc1b95ee6)
- [RTIO_SQE_MULTISHOT](../rtio_model_reference/P010_RTIO提交事件标志.md#ga00f8ead8f043fe40d49d0bc3325fb299)
- [RTIO_SQE_NO_RESPONSE](../rtio_model_reference/P010_RTIO提交事件标志.md#ga8578ffdb8f53a51b94fa86a6f02d4a11)
- [RTIO_OP_NOP](../rtio_model_reference/P009_RTIO操作码.md#gad5f073978f641413989d1c6b405d6c36)
- [RTIO_OP_RX](../rtio_model_reference/P009_RTIO操作码.md#gafeb05c351207cd1638fa78f6607e1a4a)
- [RTIO_OP_TX](../rtio_model_reference/P009_RTIO操作码.md#ga8dcaef0cda159e16520a95543ff62827)
- [RTIO_OP_TINY_TX](../rtio_model_reference/P009_RTIO操作码.md#ga6f95c0a5fbcc020a0d1102d3b08934bd)
- [RTIO_OP_CALLBACK](../rtio_model_reference/P009_RTIO操作码.md#ga18e0ff7d44e4c33900106aefad0a8508)
- [RTIO_OP_TXRX](../rtio_model_reference/P009_RTIO操作码.md#ga9f0e70f5a28be65a8ed67c0257a72692)
- [RTIO_OP_DELAY](../rtio_model_reference/P009_RTIO操作码.md#gae8da4da54f32963190f52c7533d4c951)
- [RTIO_OP_I2C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#ga3b4f9b1ee1612290323161ecc16e0859)
- [RTIO_OP_I2C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gad987be3acfe406b11419c7e8cd068cf5)
- [RTIO_OP_I3C_RECOVER](../rtio_model_reference/P009_RTIO操作码.md#gac69023c6902570e7511edd044d6d9d94)
- [RTIO_OP_I3C_CONFIGURE](../rtio_model_reference/P009_RTIO操作码.md#gaa77874941380a8215ec57b30d993d437)
- [RTIO_OP_I3C_CCC](../rtio_model_reference/P009_RTIO操作码.md#ga691ea387929db1224d6343fd91dfd2c5)
- [RTIO_OP_AWAIT](../rtio_model_reference/P009_RTIO操作码.md#gad74290935595b83040676b426cd07161)
- [RTIO_IODEV_I2C_STOP](../hardware/P442_RTIO的I2C标志.md#gaf923e862d2c6a3fbce5eb96781cf86d8)
- [RTIO_IODEV_I2C_RESTART](../hardware/P442_RTIO的I2C标志.md#gadba1c5eddeecc431000bd92054f55c3a)
- [RTIO_IODEV_I2C_10_BITS](../hardware/P442_RTIO的I2C标志.md#gaa0c3b047c7205d12775d8d38907119b9)
- [RTIO_IODEV_I3C_STOP](../hardware/P434_RTIO的I3C标志.md#ga671a479885f4d9abbdad677ddfbc47df)
- [RTIO_IODEV_I3C_RESTART](../hardware/P434_RTIO的I3C标志.md#ga9d30e1b8f22da07a25fd379c27dc2afe)
- [RTIO_IODEV_I3C_HDR](../hardware/P434_RTIO的I3C标志.md#ga857a1b2a766faa1438b4b07d73ca05ed)
- [RTIO_IODEV_I3C_NBCH](../hardware/P434_RTIO的I3C标志.md#ga258aae8fdda81c71d08dc3e26feb843d)
- [RTIO_IODEV_I3C_NOACK_EXPECTED](../hardware/P434_RTIO的I3C标志.md#gaeea22dddf91eb4e9de44a907d799044e)
- [RTIO_IODEV_I3C_HDR_MODE_MASK](../hardware/P434_RTIO的I3C标志.md#ga5e278e6ec0c31de2246c0fa9a96425c8)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [RTIO_IODEV_I3C_HDR_MODE_SET](../hardware/P434_RTIO的I3C标志.md#gae2b6caf5fa82cc7dc07508dccfeb423b)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [RTIO_IODEV_I3C_HDR_MODE_GET](../hardware/P434_RTIO的I3C标志.md#ga902a66ba8772f7a2395069e6725776da)
- [RTIO_IODEV_I3C_HDR_CMD_CODE_MASK](../hardware/P434_RTIO的I3C标志.md#ga0642bb5c69d01ea0fe148da9b8475328)
- [RTIO_IODEV_I3C_HDR_CMD_CODE_SET](../hardware/P434_RTIO的I3C标志.md#ga4d0b165eb8f4a7cc63c35e9f9438ee5a)
- [RTIO_IODEV_I3C_HDR_CMD_CODE_GET](../hardware/P434_RTIO的I3C标志.md#ga881fcb3d955aece099266ef5b57e767b)
- [rtio_sqe_prep_delay](../rtio_core_reference/P001_RTIO公共接口.md#gad45b80544e4e894cf170fe44fb752930)
- [rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)
- [rtio_sqe_prep_nop](../rtio_core_reference/P001_RTIO公共接口.md#ga599ee43fdf35e1cf895cbbe9272e4c50)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)
- [int8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#accbd6432732c88ad6adc5365800433b6)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rtio_sqe_prep_read_with_pool](../rtio_core_reference/P001_RTIO公共接口.md#ga15c1f623658d27d300d1a31a6f3d6b9d)
- [rtio_sqe_prep_read_multishot](../rtio_core_reference/P001_RTIO公共接口.md#ga9803aa829f8c0eeee746ea7d872c20cc)
- [rtio_sqe_prep_write](../rtio_core_reference/P001_RTIO公共接口.md#ga7f7856d1f4fd1d8c4f6eebcccfe77701)
- [rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)
- [rtio_sqe_prep_callback](../rtio_core_reference/P001_RTIO公共接口.md#ga9d0dd7d0e2e3d281092f2350d6e1713e)
- [rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)
- [rtio_sqe_prep_transceive](../rtio_core_reference/P001_RTIO公共接口.md#gab9b605dcbb01d21c88f9ae70588ea3b5)
- [rtio_sqe_prep_await](../rtio_core_reference/P001_RTIO公共接口.md#gafd97c145b8525895494a31a87610f65d)
- [rtio_sqe_prep_await_iodev](../rtio_core_reference/P001_RTIO公共接口.md#ga5e55583901cd13d24f60744747c5c72b)
- [rtio_sqe_prep_await_executor](../rtio_core_reference/P001_RTIO公共接口.md#gaa2f35d2909f4a19003199a3fd759fc41)
- [rtio_sqe_prep_i2c_configure](../rtio_core_reference/P001_RTIO公共接口.md#gabcb356e1df7b39bbb6f732d6fa6cc97d)
- [rtio_sqe_prep_i2c_recover](../rtio_core_reference/P001_RTIO公共接口.md#ga274cb5490582b38682f255cac4703143)
- [rtio_txn_next](../rtio_core_reference/P001_RTIO公共接口.md#gaef904eb6a8810d8c3ea537c4d6edbee5)
- [rtio_chain_next](../rtio_core_reference/P001_RTIO公共接口.md#gada1e3abf92a46e376138435debc8baf4)
- [rtio_iodev_sqe_next](../rtio_core_reference/P001_RTIO公共接口.md#gae690e3dc0fc40dda57257b2eed432719)
- [rtio_iodev_sqe_await_signal](../rtio_core_reference/P001_RTIO公共接口.md#ga7d2e5673582f32b630e2294dfbf0fe44)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_RTIO提交事件头文件源码.md)
