---
id: learning.zephyr-docs.rtio-model-reference.page-8
title: RTIO完成事件标志
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__cqe__flags.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_RTIO完成事件标志

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__rtio__cqe__flags.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

RTIO完成队列事件标志（CQE Flags）。

<a id="details"></a>

RTIO完成队列事件标志（CQE Flags）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_ga0f212500447a5e37e225a6997953b609"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_BUFFER BIT(0)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_BUFFER](#ga0f212500447a5e37e225a6997953b609)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

该条目的缓冲区由RTIO内存池（Memory Pool）分配。

<a id="r_gaef64ea020a20ac22a0edcb6eca032efc"></a>

```c
#define RTIO_CQE_FLAG_GET(flags)
```

相关声明：[RTIO_CQE_FLAG_GET](#gaef64ea020a20ac22a0edcb6eca032efc)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从CQE标志值中取得标志位。

<a id="r_ga0b5f3f7e7be472ecf87bd2b08c1888da"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX(flags)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX](#ga0b5f3f7e7be472ecf87bd2b08c1888da)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从内存池标志中取得块索引（Block Index）。

<a id="r_ga087465f866d417d5332602bb582cc1a7"></a>

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT(flags)
```

相关声明：[RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT](#ga087465f866d417d5332602bb582cc1a7)、[flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)。

从内存池标志中取得块数（Block Count）。

<a id="r_ga28b3a5661248b6b3763aab47417114d6"></a>

```c
#define RTIO_CQE_FLAG_PREP_MEMPOOL(blk_idx, blk_cnt)
```

相关声明：[RTIO_CQE_FLAG_PREP_MEMPOOL](#ga28b3a5661248b6b3763aab47417114d6)。

为内存池读操作准备CQE标志。

## 8.2\_详细说明（Detailed Documentation）

<a id="gaef64ea020a20ac22a0edcb6eca032efc"></a>

### `RTIO_CQE_FLAG_GET`

```c
#define RTIO_CQE_FLAG_GET ( flags)
```

```c
#include <zephyr/rtio/cqe.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(7, 0), (flags))
```

从CQE标志值中取得标志位。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `flags` | CQE标志值。 |

返回（Returns）：`flags`字段中的标志部分。

<a id="ga0f212500447a5e37e225a6997953b609"></a>

### `RTIO_CQE_FLAG_MEMPOOL_BUFFER`

```c
#define RTIO_CQE_FLAG_MEMPOOL_BUFFER BIT(0)
```

```c
#include <zephyr/rtio/cqe.h>
```

该条目的缓冲区由RTIO内存池（Memory Pool）分配。

如果设置了此位，表示缓冲区由内存池分配；应用用完后应尽快回收该缓冲区。

<a id="ga087465f866d417d5332602bb582cc1a7"></a>

### `RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT`

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT ( flags)
```

```c
#include <zephyr/rtio/cqe.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(31, 20), (flags))
```

从内存池标志中取得块数（Block Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `flags` | CQE标志值。 |

返回（Returns）：`flags`字段中的块数部分。

<a id="ga0b5f3f7e7be472ecf87bd2b08c1888da"></a>

### `RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX`

```c
#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX ( flags)
```

```c
#include <zephyr/rtio/cqe.h>
```

展开值（Value）：

```c
FIELD_GET(GENMASK(19, 8), (flags))
```

从内存池标志中取得块索引（Block Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `flags` | CQE标志值。 |

返回（Returns）：`flags`字段中的块索引部分。

<a id="ga28b3a5661248b6b3763aab47417114d6"></a>

### `RTIO_CQE_FLAG_PREP_MEMPOOL`

```c
#define RTIO_CQE_FLAG_PREP_MEMPOOL ( blk_idx, blk_cnt )
```

```c
#include <zephyr/rtio/cqe.h>
```

展开值（Value）：

```c
(FIELD_PREP(GENMASK(7, 0), RTIO_CQE_FLAG_MEMPOOL_BUFFER) |                                 \
 FIELD_PREP(GENMASK(19, 8), blk_idx) | FIELD_PREP(GENMASK(31, 20), blk_cnt))
```

为内存池读操作准备CQE标志。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `blk_idx` | 内存池块索引。 |
| `blk_cnt` | 内存池块数。 |

返回（Returns）：一个经过移位和掩码处理的值，可以通过按位或（OR）运算合入`flags`字段。

## 8.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：本次`cqe.h`将32位CQE flags分成三个区间：位7..0为标志，位19..8为块索引，位31..20为块数；内存池标志位是BIT(0)。两个块字段各12位，其编码范围有限，不能把任意大的索引或块数直接塞入而认为没有截断。

> 译注——源码核对：这里编码的是内存块位置与数量，不是数据缓冲区地址，也不是有效数据长度。`rtio_cqe_get_mempool_buffer()`结合原上下文的块池还原指针和分配长度。取得信息后应按该指针和分配长度归还缓冲区，另行释放CQE；标志位本身不会替应用回收内存。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 8.4\_原页交叉引用（Cross References）

- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [zephyr/rtio/cqe.h](../rtio_headers_reference/P003_RTIO完成事件头文件参考.md)
- [FIELD_GET](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa49a456f06f7bdbedfcf3517e461947e)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [FIELD_PREP](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa03c8b31bf67a097dd9f8153a04ef86b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__sys-util_html_ga58530d20924859d16358c7400c37738d"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="agroup__rtio__cqe__flags_html_ga0f212500447a5e37e225a6997953b609"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>

---

[上一章](P007_RTIO提交事件.md) · [返回大纲](大纲.md) · [下一章](P009_RTIO操作码.md)
