---
id: learning.zephyr-docs.stream-flash-reference.page-2
title: 流式Flash头文件源码
kind: reference
status: maintained
domains: [zephyr, storage, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/stream__flash_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_流式Flash头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/stream__flash_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_流式Flash头文件参考.md)和[公共API](P004_流式Flash公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00056"></a>
<a id="aflash_8h_html"></a>
<a id="agroup__stream__flash_html_ga0bf1914bba75d4d799d546b917e35705"></a>
<a id="agroup__stream__flash_html_ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f"></a>
<a id="agroup__stream__flash_html_ga44d5791cc2e8f9bacba723d6645b0d46"></a>
<a id="agroup__stream__flash_html_ga63e6418e220136a9a0ab2992d9d8f937"></a>
<a id="agroup__stream__flash_html_ga6cae2e02897480a6d63d82e80d0211ee"></a>
<a id="agroup__stream__flash_html_ga94d230f73434e90eb692b02f3fbf9ff8"></a>
<a id="agroup__stream__flash_html_gaa23d33939f344fcd42a281afa5e6f1db"></a>
<a id="agroup__stream__flash_html_gaece0b1df3d2bf4f46df588e409c3664b"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructdevice_html_a27573cbd10ee145f8bb1396242b27a3e"></a>
<a id="astructstream__flash__ctx_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2017, 2020 Nordic Semiconductor ASA
<a id="l00003"></a> * Copyright (c) 2017 Linaro Limited
<a id="l00004"></a> *
<a id="l00005"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00006"></a> */
<a id="l00007"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_STORAGE_STREAM_FLASH_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_STORAGE_STREAM_FLASH_H_
<a id="l00015"></a>
<a id="l00025"></a>
<a id="l00026"></a>#include &lt;stdbool.h&gt;
<a id="l00027"></a>#include &lt;zephyr/drivers/flash.h&gt;
<a id="l00028"></a>
<a id="l00029"></a>#ifdef __cplusplus
<a id="l00030"></a>extern "C" {
<a id="l00031"></a>#endif
<a id="l00032"></a>
<a id="l00048"></a>typedef int (*stream_flash_callback_t)(uint8_t *buf, size_t len, size_t offset);
<a id="l00049"></a>
<a id="l00056"></a>struct stream_flash_ctx {
<a id="l00058"></a>        uint8_t *buf; /* Write buffer */
<a id="l00059"></a>        size_t buf_len; /* Length of write buffer */
<a id="l00060"></a>        size_t buf_bytes; /* Number of bytes currently stored in write buf */
<a id="l00061"></a>        const struct device *fdev; /* Flash device */
<a id="l00062"></a>        size_t bytes_written; /* Number of bytes written to flash */
<a id="l00063"></a>        size_t offset; /* Offset from base of flash device to write area */
<a id="l00064"></a>        size_t available; /* Available bytes in write area */
<a id="l00065"></a>#ifdef CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK
<a id="l00066"></a>        stream_flash_callback_t callback; /* Callback invoked after write op */
<a id="l00067"></a>#endif
<a id="l00068"></a>#ifdef CONFIG_STREAM_FLASH_ERASE
<a id="l00069"></a>        size_t erased_up_to;            /* First offset in continuous range,
<a id="l00070"></a>                                         * relative to the stream_flash_ctx.offset,
<a id="l00071"></a>                                         * that has not yet been erased while
<a id="l00072"></a>                                         * preparing Stream Flash designated area
<a id="l00073"></a>                                         * for write.
<a id="l00074"></a>                                         */
<a id="l00075"></a>#endif
<a id="l00076"></a>        size_t write_block_size;        /* Offset/size device write alignment */
<a id="l00077"></a>        uint8_t erase_value;
<a id="l00079"></a>};
<a id="l00080"></a>
<a id="l00097"></a>int stream_flash_init(struct stream_flash_ctx *ctx, const struct device *fdev,
<a id="l00098"></a>                      uint8_t *buf, size_t buf_len, size_t offset, size_t size,
<a id="l00099"></a>                      stream_flash_callback_t cb);
<a id="l00109"></a>size_t stream_flash_bytes_written(const struct stream_flash_ctx *ctx);
<a id="l00110"></a>
<a id="l00118"></a>size_t stream_flash_bytes_buffered(const struct stream_flash_ctx *ctx);
<a id="l00119"></a>
<a id="l00141"></a>int stream_flash_buffered_write(struct stream_flash_ctx *ctx, const uint8_t *data,
<a id="l00142"></a>                                size_t len, bool flush);
<a id="l00143"></a>
<a id="l00159"></a>int stream_flash_progress_load(struct stream_flash_ctx *ctx,
<a id="l00160"></a>                               const char *settings_key);
<a id="l00161"></a>
<a id="l00171"></a>int stream_flash_progress_save(const struct stream_flash_ctx *ctx,
<a id="l00172"></a>                               const char *settings_key);
<a id="l00173"></a>
<a id="l00183"></a>int stream_flash_progress_clear(const struct stream_flash_ctx *ctx,
<a id="l00184"></a>                                const char *settings_key);
<a id="l00185"></a>
<a id="l00186"></a>#ifdef __cplusplus
<a id="l00187"></a>}
<a id="l00188"></a>#endif
<a id="l00189"></a>
<a id="l00193"></a>
<a id="l00194"></a>#endif /* ZEPHYR_INCLUDE_STORAGE_STREAM_FLASH_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2017, 2020 Nordic Semiconductor ASA；Copyright (c) 2017 Linaro Limited；Apache-2.0许可证原文保留。

2. 写缓冲区（Write Buffer）。

3. 写缓冲区长度。

4. 当前保存在写缓冲区中的字节数。

5. Flash设备。

6. 已写入Flash的字节数。

7. 写入区域相对Flash设备基址的偏移。

8. 写入区域中可用的字节数。

9. 写操作后调用的回调。

10. 为流式Flash指定区域准备写入空间时，连续范围中第一个尚未擦除位置的偏移；此偏移相对于stream_flash_ctx.offset。

11. 设备写入操作对偏移与长度的对齐要求。

12. 结束流式Flash头文件包含保护（Include Guard）ZEPHYR_INCLUDE_STORAGE_STREAM_FLASH_H_。

## 2.3\_原页符号提示（Symbol Descriptions）

### `flash.h`

Flash（闪存）驱动API的主头文件。

符号定位：[flash.h](../flash_reference/P009_Flash公共头文件参考.md)。

### `stream_flash_callback_t`

```c
int(* stream_flash_callback_t)(uint8_t *buf, size_t len, size_t offset)
```

Flash写入完成后调用的回调（Callback）函数签名。

定义位置（Definition）：stream_flash.h:48。

符号定位：[stream_flash_callback_t](P004_流式Flash公共接口.md#ga0bf1914bba75d4d799d546b917e35705)。

### `stream_flash_progress_load`

```c
int stream_flash_progress_load(struct stream_flash_ctx *ctx, const char *settings_key)
```

加载以settings_key为键存储的持久化流式写入进度。

符号定位：[stream_flash_progress_load](P004_流式Flash公共接口.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)。

### `stream_flash_progress_save`

```c
int stream_flash_progress_save(const struct stream_flash_ctx *ctx, const char *settings_key)
```

使用settings_key为键保存持久化流式写入进度。

符号定位：[stream_flash_progress_save](P004_流式Flash公共接口.md#ga44d5791cc2e8f9bacba723d6645b0d46)。

### `stream_flash_init`

```c
int stream_flash_init(struct stream_flash_ctx *ctx, const struct device *fdev, uint8_t *buf, size_t buf_len, size_t offset, size_t size, stream_flash_callback_t cb)
```

初始化向Flash进行流式写入所需的上下文。

符号定位：[stream_flash_init](P004_流式Flash公共接口.md#ga63e6418e220136a9a0ab2992d9d8f937)。

### `stream_flash_bytes_buffered`

```c
size_t stream_flash_bytes_buffered(const struct stream_flash_ctx *ctx)
```

读取为下一次Flash写入缓存的字节数。

符号定位：[stream_flash_bytes_buffered](P004_流式Flash公共接口.md#ga6cae2e02897480a6d63d82e80d0211ee)。

### `stream_flash_progress_clear`

```c
int stream_flash_progress_clear(const struct stream_flash_ctx *ctx, const char *settings_key)
```

清除以settings_key为键存储的持久化流式写入进度。

符号定位：[stream_flash_progress_clear](P004_流式Flash公共接口.md#ga94d230f73434e90eb692b02f3fbf9ff8)。

### `stream_flash_buffered_write`

```c
int stream_flash_buffered_write(struct stream_flash_ctx *ctx, const uint8_t *data, size_t len, bool flush)
```

处理输入缓冲区，将数据按单个块写入Flash设备。

符号定位：[stream_flash_buffered_write](P004_流式Flash公共接口.md#gaa23d33939f344fcd42a281afa5e6f1db)。

### `stream_flash_bytes_written`

```c
size_t stream_flash_bytes_written(const struct stream_flash_ctx *ctx)
```

读取已写入Flash的字节数。

符号定位：[stream_flash_bytes_written](P004_流式Flash公共接口.md#gaece0b1df3d2bf4f46df588e409c3664b)。

### `stdbool.h`

符号定位：[stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `device`

每个驱动实例的运行时设备结构，位于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `device::data`

```c
void * data
```

设备实例私有数据的地址。

定义位置（Definition）：device.h:553。

符号定位：[device::data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)。

### `stream_flash_ctx`

流式Flash上下文（Context）结构。

定义位置（Definition）：stream_flash.h:56。

符号定位：[stream_flash_ctx](P003_流式Flash上下文.md)。

## 2.4\_源码跟踪译注

> 译注——会话与计数：初始化将bytes_written及buf_bytes清零，只建立写入会话，没有直接擦除或写入Flash。两项查询分别返回已经计入成功写入的有效载荷字节数和仍在RAM缓冲区中的字节数；它们不计算为写对齐追加的填充值，也不校验ctx是否为空。原文仅为bytes_written查询标注pre-kernel-ok／isr-ok，不能把这两个标签推广到实际写入或设置存储操作。

> 译注——缓冲与刷新：实现先填满用户提供的缓冲区，再同步写入，余量留待下一次调用。flush=true同步最后的不足一块数据，并按write_block_size以设备的erase_value补齐物理写入长度；bytes_written只增加有效载荷长度。必须遵守原文“刷新后重新初始化才能开始新会话”的约定，即使实现没有单独的已刷新状态位，也不能继续追加而假定对齐和旧填充区不受影响。

> 译注——初始化前提：buf_len、offset和size应满足设备写块对齐，size必须非零，buf_len不得超过适用的Flash页大小。实现检查对齐、指针及offset+size溢出；CONFIG_STREAM_FLASH_INSPECT启用时还遍历页检查缓冲区与页大小、总区域范围。该选项默认启用但依赖FLASH_PAGE_LAYOUT，关闭时不执行这部分布局检查。当前实现没有单独拒绝零长度缓冲区；调用者仍须提供能容纳数据的有效缓冲区，不应把模运算通过视为配置可用。

> 译注——回读校验：启用CONFIG_STREAM_FLASH_POST_WRITE_CALLBACK且cb非空时，写入成功后会反转缓冲区中的有效载荷字节，再把相同范围读回该缓冲区，然后同步调用cb。回调offset是Flash设备内的写入地址offset+bytes_written，len仅为有效载荷长度，不包含对齐填充；缓冲区被复用，不能将回调视为另一个长期保留的数据副本。

> 译注——失败不是回滚：flash_write成功后，回读或回调仍可能失败；这时Flash已经改变，但bytes_written尚未增加，buf_bytes也未清零。单次大写入还可能先完成若干缓冲块再在后续块失败。错误返回不保证未写入任何数据，重试、恢复和校验策略必须结合当前进度及存储器约束设计。

> 译注——擦除边界：CONFIG_STREAM_FLASH_ERASE启用时，同步写入前按页准备空间，erased_up_to记录相对会话起点的已擦除连续范围终点；关闭此选项时，需要外部调用者满足设备写前擦除要求。混合含擦除与无需擦除设备时，ERASE_ONLY_WHEN_SUPPORTED根据设备能力跳过不需要的显式擦除。实现按整页擦除，并不保护同页中会话区域之外的其他数据；应选择符合设备擦除粒度且专供本次用途的区域。

> 译注——持久化的内容：CONFIG_STREAM_FLASH_PROGRESS依赖Settings子系统。save只保存bytes_written这个size_t值，不保存RAM中的余量、缓冲区内容、Flash设备、起点、区域大小或校验摘要，也不自动在每次写入后保存。clear删除设置项，不擦除有效载荷，也不重置当前上下文。重新初始化后，应在新数据写入前加载属于同一会话区域与数据流的进度。

> 译注——恢复范围需要核对：加载器只接受与设置键精确匹配的数据；已保存字节数小于当前上下文计数时忽略旧值，否则更新计数，启用自动擦除时再据最后一个已写字节所在页恢复擦除边界。当前加载器没有先独立核对保存值是否超过ctx->available；原返回说明提到off越界与-ERANGE，但此函数签名没有off参数，实现直接传播Settings或页信息查询错误，译文保留原说明并在此明确差异。调用者不能将返回成功视为已完成完整性或区域一致性校验。

> 译注——不透明上下文：官方结构参考页用INTERNAL_HIDDEN隐藏成员文档，要求通过API操作；源码浏览页则显示实际字段。本册分别保留两种原始页面的内容，不把字段变成受支持的公开修改接口。源码中的条件字段由Kconfig决定，结构布局和持久化size_t格式不可假定跨任意配置、架构或版本不变。

> 译注——版本边界：本批依据实际读取的latest四页与公共头文件、实现、Kconfig三份官方源码，记录各自摘要。此版本公开页及头文件没有stream_flash_erase_page声明；旧快照可能不同，不将旧接口补写为本次原文。仓库相对定位只用于源码跟踪，不能证明仓库副本与滚动main逐字一致。本次未构建固件、擦写Flash或执行断电恢复实验。

头文件相对定位：[include/zephyr/storage/stream_flash.h](../../../include/zephyr/storage/stream_flash.h)，关联实现／接口：[subsys/storage/stream/stream_flash.c](../../../subsys/storage/stream/stream_flash.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/storage/stream_flash.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/storage/stream/stream_flash.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、擦写Flash或执行断电恢复实验。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_流式Flash头文件参考.md)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/drivers/flash.h](../flash_reference/P009_Flash公共头文件参考.md)
- [stream_flash_callback_t](P004_流式Flash公共接口.md#ga0bf1914bba75d4d799d546b917e35705)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [stream_flash_ctx](P003_流式Flash上下文.md)
- [device](../device_reference/P002_设备对象结构.md)
- [stream_flash_init](P004_流式Flash公共接口.md#ga63e6418e220136a9a0ab2992d9d8f937)
- [stream_flash_bytes_written](P004_流式Flash公共接口.md#gaece0b1df3d2bf4f46df588e409c3664b)
- [stream_flash_bytes_buffered](P004_流式Flash公共接口.md#ga6cae2e02897480a6d63d82e80d0211ee)
- [stream_flash_buffered_write](P004_流式Flash公共接口.md#gaa23d33939f344fcd42a281afa5e6f1db)
- [data](../device_reference/P002_设备对象结构.md#a27573cbd10ee145f8bb1396242b27a3e)
- [stream_flash_progress_load](P004_流式Flash公共接口.md#ga2d90ef00da4ded8c2d0ffb1b2e4c2a2f)
- [stream_flash_progress_save](P004_流式Flash公共接口.md#ga44d5791cc2e8f9bacba723d6645b0d46)
- [stream_flash_progress_clear](P004_流式Flash公共接口.md#ga94d230f73434e90eb692b02f3fbf9ff8)

---

[上一章](P001_流式Flash头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_流式Flash上下文.md)
