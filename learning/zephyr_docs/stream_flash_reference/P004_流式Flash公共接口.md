---
id: learning.zephyr-docs.stream-flash-reference.page-4
title: 流式Flash公共接口
kind: reference
status: maintained
domains: [zephyr, storage, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__stream__flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_流式Flash公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__stream__flash.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入流式Flash头文件、上下文和公共接口页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

对向Flash进行流式写入的抽象（Abstraction）。

<a id="details"></a>

对向Flash进行流式写入的抽象。自Zephyr 2.3提供（Since）；接口版本（Version）为0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_stream_5Fflash_5Fctx"></a>

```c
struct stream_flash_ctx
```

相关声明：[stream_flash_ctx](P003_流式Flash上下文.md)。

流式Flash上下文（Context）结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.2\_类型定义（Typedefs）

<a id="r_ga0bf1914bba75d4d799d546b917e35705"></a>

```c
typedef int(* stream_flash_callback_t) (uint8_t *buf, size_t len, size_t offset)
```

相关声明：[stream_flash_callback_t](#ga0bf1914bba75d4d799d546b917e35705)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

Flash写入完成后调用的回调（Callback）函数签名。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.3\_函数（Functions）

<a id="r_ga63e6418e220136a9a0ab2992d9d8f937"></a>

```c
int stream_flash_init (struct stream_flash_ctx *ctx, const struct device *fdev, uint8_t *buf, size_t buf_len, size_t offset, size_t size, stream_flash_callback_t cb)
```

相关声明：[stream_flash_init](#ga63e6418e220136a9a0ab2992d9d8f937)、[stream_flash_ctx](P003_流式Flash上下文.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[stream_flash_callback_t](#ga0bf1914bba75d4d799d546b917e35705)。

初始化向Flash进行流式写入所需的上下文。

<a id="r_gaece0b1df3d2bf4f46df588e409c3664b"></a>

```c
size_t stream_flash_bytes_written (const struct stream_flash_ctx *ctx)
```

相关声明：[stream_flash_bytes_written](#gaece0b1df3d2bf4f46df588e409c3664b)、[stream_flash_ctx](P003_流式Flash上下文.md)。

读取已写入Flash的字节数。

<a id="r_ga6cae2e02897480a6d63d82e80d0211ee"></a>

```c
size_t stream_flash_bytes_buffered (const struct stream_flash_ctx *ctx)
```

相关声明：[stream_flash_bytes_buffered](#ga6cae2e02897480a6d63d82e80d0211ee)、[stream_flash_ctx](P003_流式Flash上下文.md)。

读取为下一次Flash写入缓存的字节数。

<a id="r_gaa23d33939f344fcd42a281afa5e6f1db"></a>

```c
int stream_flash_buffered_write (struct stream_flash_ctx *ctx, const uint8_t *data, size_t len, bool flush)
```

相关声明：[stream_flash_buffered_write](#gaa23d33939f344fcd42a281afa5e6f1db)、[stream_flash_ctx](P003_流式Flash上下文.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

处理输入缓冲区，将数据按单个块写入Flash设备。

<a id="r_ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f"></a>

```c
int stream_flash_progress_load (struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_load](#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)、[stream_flash_ctx](P003_流式Flash上下文.md)。

加载以settings_key为键存储的持久化流式写入进度。

<a id="r_ga44d5791cc2e8f9bacba723d6645b0d46"></a>

```c
int stream_flash_progress_save (const struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_save](#ga44d5791cc2e8f9bacba723d6645b0d46)、[stream_flash_ctx](P003_流式Flash上下文.md)。

使用settings_key为键保存持久化流式写入进度。

<a id="r_ga94d230f73434e90eb692b02f3fbf9ff8"></a>

```c
int stream_flash_progress_clear (const struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_clear](#ga94d230f73434e90eb692b02f3fbf9ff8)、[stream_flash_ctx](P003_流式Flash上下文.md)。

清除以settings_key为键存储的持久化流式写入进度。

## 4.4\_详细说明（Detailed Documentation）

<a id="ga0bf1914bba75d4d799d546b917e35705"></a>

### `stream_flash_callback_t`

```c
typedef int(* stream_flash_callback_t) (uint8_t *buf, size_t len, size_t offset)
```

```c
#include <zephyr/storage/stream_flash.h>
```

Flash写入完成后调用的回调（Callback）函数签名。

Flash写入完成后，调用此类型的函数，并向其传递包含Flash回读数据的缓冲区。这使调用者能够验证数据是否正确存储，例如使用SHA（安全散列算法，Secure Hash Algorithm）函数。在stream_flash_init中提供的写缓冲区buf会为此用作读缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向回读数据的指针。 |
| `len` | 回读数据的长度。 |
| `offset` | 回读数据所在的偏移（Offset）。 |

<a id="gaa23d33939f344fcd42a281afa5e6f1db"></a>

### `stream_flash_buffered_write()`

```c
int stream_flash_buffered_write ( struct stream_flash_ctx * ctx, const uint8_t * data, size_t len, bool flush )
```

```c
#include <zephyr/storage/stream_flash.h>
```

处理输入缓冲区，将数据按单个块写入Flash设备。

在各次调用之间保存剩余数据。

对于给定上下文，最后一次写入请求必须将flush设为true；该请求结束一次流式写入，并将缓冲区数据刷新（Flush）到存储设备。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |
| `data` | 要写入的数据。 |
| `len` | 要写入的字节数。 |
| `flush` | 为true时，强制将所有已缓存的数据写入Flash。 |

**警告（Warning）**：对于已刷新的上下文，除非重新初始化，否则不得再提交写入请求；这样的写入尝试可能导致函数失败并返回错误。上下文刷新后，可以重新初始化，并用于新的流式Flash会话（Session）。

返回（Returns）：成功时返回非负值，失败时返回负errno错误码。

<a id="ga6cae2e02897480a6d63d82e80d0211ee"></a>

### `stream_flash_bytes_buffered()`

```c
size_t stream_flash_bytes_buffered ( const struct stream_flash_ctx * ctx)
```

```c
#include <zephyr/storage/stream_flash.h>
```

读取为下一次Flash写入缓存的字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |

返回（Returns）：为下一次Flash写入缓存的有效载荷（Payload）字节数。

<a id="gaece0b1df3d2bf4f46df588e409c3664b"></a>

### `stream_flash_bytes_written()`

```c
size_t stream_flash_bytes_written ( const struct stream_flash_ctx * ctx)
```

```c
#include <zephyr/storage/stream_flash.h>
```

读取已写入Flash的字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |

说明（Note）：API标签为pre-kernel-ok与isr-ok，表示可在内核启动前及中断服务程序（ISR）中调用。

返回（Returns）：已写入Flash的有效载荷字节数。

<a id="ga63e6418e220136a9a0ab2992d9d8f937"></a>

### `stream_flash_init()`

```c
int stream_flash_init ( struct stream_flash_ctx * ctx, const struct device * fdev, uint8_t * buf, size_t buf_len, size_t offset, size_t size, stream_flash_callback_t cb )
```

```c
#include <zephyr/storage/stream_flash.h>
```

初始化向Flash进行流式写入所需的上下文。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 待初始化的上下文。 |
| `fdev` | 要操作的Flash设备。 |
| `buf` | 写缓冲区（Write Buffer）。 |
| `buf_len` | 写缓冲区长度。不得大于页大小（Page Size），必须是Flash设备写块大小（Write-block-size）的整数倍。 |
| `offset` | 在Flash设备内开始写入的偏移。 |
| `size` | 可用于缓冲写入的字节数。 |
| `cb` | Flash写操作完成时调用的回调。启用CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK时支持此回调。 |

返回（Returns）：成功时返回非负值，失败时返回负errno错误码。

<a id="ga94d230f73434e90eb692b02f3fbf9ff8"></a>

### `stream_flash_progress_clear()`

```c
int stream_flash_progress_clear ( const struct stream_flash_ctx * ctx, const char * settings_key )
```

```c
#include <zephyr/storage/stream_flash.h>
```

清除以settings_key为键存储的持久化流式写入进度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |
| `settings_key` | 此前用于存储流式写入进度的键。 |

返回（Returns）：成功时返回非负值，失败时返回负errno错误码。

<a id="ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f"></a>

### `stream_flash_progress_load()`

```c
int stream_flash_progress_load ( struct stream_flash_ctx * ctx, const char * settings_key )
```

```c
#include <zephyr/storage/stream_flash.h>
```

加载以settings_key为键存储的持久化流式写入进度。

应在stream_flash_init之后立即调用此函数，在写入任何数据之前加载先前的流式写入进度。如果加载进度中的已写入字节数少于ctx中的值，则忽略该进度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |
| `settings_key` | 供设置模块（Settings）加载流式写入进度时使用的键。 |

返回（Returns）：成功时返回非负值；off超出为流式写入指定的区域时返回-ERANGE，其他失败返回负errno错误码。

<a id="ga44d5791cc2e8f9bacba723d6645b0d46"></a>

### `stream_flash_progress_save()`

```c
int stream_flash_progress_save ( const struct stream_flash_ctx * ctx, const char * settings_key )
```

```c
#include <zephyr/storage/stream_flash.h>
```

使用settings_key为键保存持久化流式写入进度。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctx` | 上下文。 |
| `settings_key` | 供设置模块（Settings）存储流式写入进度时使用的键。 |

返回（Returns）：成功时返回非负值，失败时返回负errno错误码。

## 4.5\_源码定位与版本边界

相对源码定位：[流式Flash头文件](../../../include/zephyr/storage/stream_flash.h)、[流式写入实现](../../../subsys/storage/stream/stream_flash.c)和[配置选项](../../../subsys/storage/stream/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：会话与计数：初始化将bytes_written及buf_bytes清零，只建立写入会话，没有直接擦除或写入Flash。两项查询分别返回已经计入成功写入的有效载荷字节数和仍在RAM缓冲区中的字节数；它们不计算为写对齐追加的填充值，也不校验ctx是否为空。原文仅为bytes_written查询标注pre-kernel-ok／isr-ok，不能把这两个标签推广到实际写入或设置存储操作。

> 译注——源码核对：缓冲与刷新：实现先填满用户提供的缓冲区，再同步写入，余量留待下一次调用。flush=true同步最后的不足一块数据，并按write_block_size以设备的erase_value补齐物理写入长度；bytes_written只增加有效载荷长度。必须遵守原文“刷新后重新初始化才能开始新会话”的约定，即使实现没有单独的已刷新状态位，也不能继续追加而假定对齐和旧填充区不受影响。

> 译注——源码核对：初始化前提：buf_len、offset和size应满足设备写块对齐，size必须非零，buf_len不得超过适用的Flash页大小。实现检查对齐、指针及offset+size溢出；CONFIG_STREAM_FLASH_INSPECT启用时还遍历页检查缓冲区与页大小、总区域范围。该选项默认启用但依赖FLASH_PAGE_LAYOUT，关闭时不执行这部分布局检查。当前实现没有单独拒绝零长度缓冲区；调用者仍须提供能容纳数据的有效缓冲区，不应把模运算通过视为配置可用。

> 译注——源码核对：回读校验：启用CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK且cb非空时，写入成功后会反转缓冲区中的有效载荷字节，再把相同范围读回该缓冲区，然后同步调用cb。回调offset是Flash设备内的写入地址offset+bytes_written，len仅为有效载荷长度，不包含对齐填充；缓冲区被复用，不能将回调视为另一个长期保留的数据副本。

> 译注——源码核对：失败不是回滚：flash_write成功后，回读或回调仍可能失败；这时Flash已经改变，但bytes_written尚未增加，buf_bytes也未清零。单次大写入还可能先完成若干缓冲块再在后续块失败。错误返回不保证未写入任何数据，重试、恢复和校验策略必须结合当前进度及存储器约束设计。

> 译注——源码核对：擦除边界：CONFIG_STREAM_FLASH_ERASE启用时，同步写入前按页准备空间，erased_up_to记录相对会话起点的已擦除连续范围终点；关闭此选项时，需要外部调用者满足设备写前擦除要求。混合含擦除与无需擦除设备时，ERASE_ONLY_WHEN_SUPPORTED根据设备能力跳过不需要的显式擦除。实现按整页擦除，并不保护同页中会话区域之外的其他数据；应选择符合设备擦除粒度且专供本次用途的区域。

> 译注——源码核对：持久化的内容：CONFIG_STREAM_FLASH_PROGRESS依赖Settings子系统。save只保存bytes_written这个size_t值，不保存RAM中的余量、缓冲区内容、Flash设备、起点、区域大小或校验摘要，也不自动在每次写入后保存。clear删除设置项，不擦除有效载荷，也不重置当前上下文。重新初始化后，应在新数据写入前加载属于同一会话区域与数据流的进度。

> 译注——源码核对：恢复范围需要核对：加载器只接受与设置键精确匹配的数据；已保存字节数小于当前上下文计数时忽略旧值，否则更新计数，启用自动擦除时再据最后一个已写字节所在页恢复擦除边界。当前加载器没有先独立核对保存值是否超过ctx->available；原返回说明提到off越界与-ERANGE，但此函数签名没有off参数，实现直接传播Settings或页信息查询错误，译文保留原说明并在此明确差异。调用者不能将返回成功视为已完成完整性或区域一致性校验。

> 译注——源码核对：不透明上下文：官方结构参考页用INTERNAL_HIDDEN隐藏成员文档，要求通过API操作；源码浏览页则显示实际字段。本册分别保留两种原始页面的内容，不把字段变成受支持的公开修改接口。源码中的条件字段由Kconfig决定，结构布局和持久化size_t格式不可假定跨任意配置、架构或版本不变。

> 译注——源码核对：版本边界：本批依据实际读取的latest四页与公共头文件、实现、Kconfig三份官方源码，记录各自摘要。此版本公开页及头文件没有stream_flash_erase_page声明；旧快照可能不同，不将旧接口补写为本次原文。仓库相对定位只用于源码跟踪，不能证明仓库副本与滚动main逐字一致。本次未构建固件、擦写Flash或执行断电恢复实验。

本次验证范围为文档与源码对照，未构建固件、擦写Flash或执行断电恢复实验。

## 4.6\_原页交叉引用（Cross References）

- [stream_flash_ctx](P003_流式Flash上下文.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [device](../device_reference/P002_设备对象结构.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [zephyr/storage/stream_flash.h](P001_流式Flash头文件参考.md)

<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P003_流式Flash上下文.md) · [返回大纲](大纲.md)
