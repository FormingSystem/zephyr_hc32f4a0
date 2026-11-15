---
id: learning.zephyr-docs.stream-flash-reference.page-1
title: 流式Flash头文件参考
kind: reference
status: maintained
domains: [zephyr, storage, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stream__flash_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_流式Flash头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/stream__flash_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入流式Flash头文件、上下文和公共接口页，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

向Flash（闪存）进行流式写入（Stream Writes）的公共API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/drivers/flash.h>
```

查看此文件的源码。

向Flash（闪存）进行流式写入（Stream Writes）的公共API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_stream_5Fflash_5Fctx"></a>

```c
struct stream_flash_ctx
```

相关声明：[stream_flash_ctx](P003_流式Flash上下文.md)。

流式Flash上下文（Context）结构。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.2\_类型定义（Typedefs）

<a id="r_ga0bf1914bba75d4d799d546b917e35705"></a>

```c
typedef int(* stream_flash_callback_t) (uint8_t *buf, size_t len, size_t offset)
```

相关声明：[stream_flash_callback_t](P004_流式Flash公共接口.md#ga0bf1914bba75d4d799d546b917e35705)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

Flash写入完成后调用的回调（Callback）函数签名。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ga63e6418e220136a9a0ab2992d9d8f937"></a>

```c
int stream_flash_init (struct stream_flash_ctx *ctx, const struct device *fdev, uint8_t *buf, size_t buf_len, size_t offset, size_t size, stream_flash_callback_t cb)
```

相关声明：[stream_flash_init](P004_流式Flash公共接口.md#ga63e6418e220136a9a0ab2992d9d8f937)、[stream_flash_ctx](P003_流式Flash上下文.md)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[stream_flash_callback_t](P004_流式Flash公共接口.md#ga0bf1914bba75d4d799d546b917e35705)。

初始化向Flash进行流式写入所需的上下文。

<a id="r_gaece0b1df3d2bf4f46df588e409c3664b"></a>

```c
size_t stream_flash_bytes_written (const struct stream_flash_ctx *ctx)
```

相关声明：[stream_flash_bytes_written](P004_流式Flash公共接口.md#gaece0b1df3d2bf4f46df588e409c3664b)、[stream_flash_ctx](P003_流式Flash上下文.md)。

读取已写入Flash的字节数。

<a id="r_ga6cae2e02897480a6d63d82e80d0211ee"></a>

```c
size_t stream_flash_bytes_buffered (const struct stream_flash_ctx *ctx)
```

相关声明：[stream_flash_bytes_buffered](P004_流式Flash公共接口.md#ga6cae2e02897480a6d63d82e80d0211ee)、[stream_flash_ctx](P003_流式Flash上下文.md)。

读取为下一次Flash写入缓存的字节数。

<a id="r_gaa23d33939f344fcd42a281afa5e6f1db"></a>

```c
int stream_flash_buffered_write (struct stream_flash_ctx *ctx, const uint8_t *data, size_t len, bool flush)
```

相关声明：[stream_flash_buffered_write](P004_流式Flash公共接口.md#gaa23d33939f344fcd42a281afa5e6f1db)、[stream_flash_ctx](P003_流式Flash上下文.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)。

处理输入缓冲区，将数据按单个块写入Flash设备。

<a id="r_ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f"></a>

```c
int stream_flash_progress_load (struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_load](P004_流式Flash公共接口.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)、[stream_flash_ctx](P003_流式Flash上下文.md)。

加载以settings_key为键存储的持久化流式写入进度。

<a id="r_ga44d5791cc2e8f9bacba723d6645b0d46"></a>

```c
int stream_flash_progress_save (const struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_save](P004_流式Flash公共接口.md#ga44d5791cc2e8f9bacba723d6645b0d46)、[stream_flash_ctx](P003_流式Flash上下文.md)。

使用settings_key为键保存持久化流式写入进度。

<a id="r_ga94d230f73434e90eb692b02f3fbf9ff8"></a>

```c
int stream_flash_progress_clear (const struct stream_flash_ctx *ctx, const char *settings_key)
```

相关声明：[stream_flash_progress_clear](P004_流式Flash公共接口.md#ga94d230f73434e90eb692b02f3fbf9ff8)、[stream_flash_ctx](P003_流式Flash上下文.md)。

清除以settings_key为键存储的持久化流式写入进度。

## 1.4\_源码定位与版本边界

相对源码定位：[流式Flash头文件](../../../include/zephyr/storage/stream_flash.h)、[流式写入实现](../../../subsys/storage/stream/stream_flash.c)和[配置选项](../../../subsys/storage/stream/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：会话与计数：初始化将bytes_written及buf_bytes清零，只建立写入会话，没有直接擦除或写入Flash。两项查询分别返回已经计入成功写入的有效载荷字节数和仍在RAM缓冲区中的字节数；它们不计算为写对齐追加的填充值，也不校验ctx是否为空。原文仅为bytes_written查询标注pre-kernel-ok／isr-ok，不能把这两个标签推广到实际写入或设置存储操作。

> 译注——源码核对：缓冲与刷新：实现先填满用户提供的缓冲区，再同步写入，余量留待下一次调用。flush=true同步最后的不足一块数据，并按write_block_size以设备的erase_value补齐物理写入长度；bytes_written只增加有效载荷长度。必须遵守原文“刷新后重新初始化才能开始新会话”的约定，即使实现没有单独的已刷新状态位，也不能继续追加而假定对齐和旧填充区不受影响。

> 译注——源码核对：不透明上下文：官方结构参考页用INTERNAL_HIDDEN隐藏成员文档，要求通过API操作；源码浏览页则显示实际字段。本册分别保留两种原始页面的内容，不把字段变成受支持的公开修改接口。源码中的条件字段由Kconfig决定，结构布局和持久化size_t格式不可假定跨任意配置、架构或版本不变。

> 译注——源码核对：版本边界：本批依据实际读取的latest四页与公共头文件、实现、Kconfig三份官方源码，记录各自摘要。此版本公开页及头文件没有stream_flash_erase_page声明；旧快照可能不同，不将旧接口补写为本次原文。仓库相对定位只用于源码跟踪，不能证明仓库副本与滚动main逐字一致。本次未构建固件、擦写Flash或执行断电恢复实验。

本次验证范围为文档与源码对照，未构建固件、擦写Flash或执行断电恢复实验。

## 1.5\_原页交叉引用（Cross References）

- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h_source.html)
- [zephyr/drivers/flash.h](../flash_reference/P010_Flash公共头文件源码.md)
- [查看此文件的源码](P002_流式Flash头文件源码.md)
- [stream_flash_ctx](P003_流式Flash上下文.md)
- [stream_flash_callback_t](P004_流式Flash公共接口.md#ga0bf1914bba75d4d799d546b917e35705)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stream_flash_init](P004_流式Flash公共接口.md#ga63e6418e220136a9a0ab2992d9d8f937)
- [device](../device_reference/P002_设备对象结构.md)
- [stream_flash_bytes_written](P004_流式Flash公共接口.md#gaece0b1df3d2bf4f46df588e409c3664b)
- [stream_flash_bytes_buffered](P004_流式Flash公共接口.md#ga6cae2e02897480a6d63d82e80d0211ee)
- [stream_flash_buffered_write](P004_流式Flash公共接口.md#gaa23d33939f344fcd42a281afa5e6f1db)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [stream_flash_progress_load](P004_流式Flash公共接口.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)
- [stream_flash_progress_save](P004_流式Flash公共接口.md#ga44d5791cc2e8f9bacba723d6645b0d46)
- [stream_flash_progress_clear](P004_流式Flash公共接口.md#ga94d230f73434e90eb692b02f3fbf9ff8)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_流式Flash头文件源码.md)
