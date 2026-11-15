---
id: learning.zephyr-docs.rtio-headers-reference.page-4
title: RTIO完成事件头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/cqe_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_RTIO完成事件头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/cqe_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P003_RTIO完成事件头文件参考.md)和[公共API](../rtio_core_reference/P001_RTIO公共接口.md)。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00079"></a>
<a id="foldopen00090"></a>
<a id="agroup__mpsc__lockfree_html_ga403add133841ef88e10d74141e782b37"></a>
<a id="agroup__mpsc__lockfree_html_ga823ec37b84ac43e46167aac954bce9d7"></a>
<a id="agroup__sys-util_html_gac5bc561d1bfd1bf68877fe577779bd2f"></a>
<a id="ampsc__lockfree_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astring_8h_html"></a>
<a id="astring_8h_html_a4137694174d4ca2fad886a1db355015c"></a>
<a id="astructmpsc__node_html"></a>
<a id="astructmpsc_html"></a>
<a id="astructrtio__cqe_html"></a>
<a id="astructrtio__cqe_html_a15128387ccbea55812ef229eab7241e7"></a>
<a id="astructrtio__cqe_html_a8a7632ef1cfd31529d782bd761908d93"></a>
<a id="astructrtio__cqe_html_acbe2e6607a752b676d9336b9ca6ce435"></a>
<a id="asys_2iterable__sections_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * SPDX-Copyright: Copyright (c) 2022 Intel Corporation
<a id="l00003"></a> * SPDX-FileCopyrightText: Copyright (c) 2026 Infineon Technologies AG,
<a id="l00004"></a> * SPDX-FileCopyrightText: or an affiliate of Infineon Technologies AG. All rights reserved.
<a id="l00005"></a> *
<a id="l00006"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00007"></a> */
<a id="l00008"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>#ifndef ZEPHYR_INCLUDE_RTIO_CQE_H_
<a id="l00017"></a>#define ZEPHYR_INCLUDE_RTIO_CQE_H_
<a id="l00018"></a>
<a id="l00019"></a>#include &lt;stdint.h&gt;
<a id="l00020"></a>#include &lt;string.h&gt;
<a id="l00021"></a>#include &lt;zephyr/sys/mpsc_lockfree.h&gt;
<a id="l00022"></a>#include &lt;zephyr/sys/iterable_sections.h&gt;
<a id="l00023"></a>
<a id="l00024"></a>#ifdef __cplusplus
<a id="l00025"></a>extern "C" {
<a id="l00026"></a>#endif
<a id="l00027"></a>
<a id="l00032"></a>
<a id="l00039"></a>
<a id="l00046"></a>#define RTIO_CQE_FLAG_MEMPOOL_BUFFER BIT(0)
<a id="l00047"></a>
<a id="l00054"></a>#define RTIO_CQE_FLAG_GET(flags) FIELD_GET(GENMASK(7, 0), (flags))
<a id="l00055"></a>
<a id="l00062"></a>#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_IDX(flags) FIELD_GET(GENMASK(19, 8), (flags))
<a id="l00063"></a>
<a id="l00070"></a>#define RTIO_CQE_FLAG_MEMPOOL_GET_BLK_CNT(flags) FIELD_GET(GENMASK(31, 20), (flags))
<a id="l00071"></a>
<a id="l00079"></a>#define RTIO_CQE_FLAG_PREP_MEMPOOL(blk_idx, blk_cnt)                                               \
<a id="l00080"></a>        (FIELD_PREP(GENMASK(7, 0), RTIO_CQE_FLAG_MEMPOOL_BUFFER) |                                 \
<a id="l00081"></a>         FIELD_PREP(GENMASK(19, 8), blk_idx) | FIELD_PREP(GENMASK(31, 20), blk_cnt))
<a id="l00082"></a>
<a id="l00086"></a>
<a id="l00090"></a>struct rtio_cqe {
<a id="l00092"></a>        struct mpsc_node q;
<a id="l00094"></a>
<a id="l00095"></a>        int32_t result;
<a id="l00096"></a>        void *userdata;
<a id="l00097"></a>        uint32_t flags;
<a id="l00098"></a>};
<a id="l00099"></a>
<a id="l00100"></a>/* Private structures and functions used for the pool of cqe structures */
<a id="l00102"></a>
<a id="l00103"></a>struct rtio_cqe_pool {
<a id="l00104"></a>        struct mpsc free_q;
<a id="l00105"></a>        const uint16_t pool_size;
<a id="l00106"></a>        uint16_t pool_free;
<a id="l00107"></a>        struct rtio_cqe *pool;
<a id="l00108"></a>};
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>static inline struct rtio_cqe *rtio_cqe_pool_alloc(struct rtio_cqe_pool *pool)
<a id="l00112"></a>{
<a id="l00113"></a>        struct mpsc_node *node = mpsc_pop(&amp;pool-&gt;free_q);
<a id="l00114"></a>
<a id="l00115"></a>        if (node == NULL) {
<a id="l00116"></a>                return NULL;
<a id="l00117"></a>        }
<a id="l00118"></a>
<a id="l00119"></a>        struct rtio_cqe *cqe = CONTAINER_OF(node, struct rtio_cqe, q);
<a id="l00120"></a>
<a id="l00121"></a>        memset(cqe, 0, sizeof(struct rtio_cqe));
<a id="l00122"></a>
<a id="l00123"></a>        pool-&gt;pool_free--;
<a id="l00124"></a>
<a id="l00125"></a>        return cqe;
<a id="l00126"></a>}
<a id="l00127"></a>
<a id="l00128"></a>static inline void rtio_cqe_pool_free(struct rtio_cqe_pool *pool, struct rtio_cqe *cqe)
<a id="l00129"></a>{
<a id="l00130"></a>        mpsc_push(&amp;pool-&gt;free_q, &amp;cqe-&gt;q);
<a id="l00131"></a>
<a id="l00132"></a>        pool-&gt;pool_free++;
<a id="l00133"></a>}
<a id="l00134"></a>
<a id="l00135"></a>/* Do not try and reformat the macros */
<a id="l00136"></a>/* clang-format off */
<a id="l00137"></a>
<a id="l00138"></a>#define Z_RTIO_CQE_POOL_DEFINE(name, sz)                        \
<a id="l00139"></a>        static struct rtio_cqe CONCAT(_cqe_pool_, name)[sz];    \
<a id="l00140"></a>        STRUCT_SECTION_ITERABLE(rtio_cqe_pool, name) = {        \
<a id="l00141"></a>                .free_q = MPSC_INIT((name.free_q)),     \
<a id="l00142"></a>                .pool_size = sz,                                \
<a id="l00143"></a>                .pool_free = sz,                                \
<a id="l00144"></a>                .pool = CONCAT(_cqe_pool_, name),               \
<a id="l00145"></a>        }
<a id="l00146"></a>
<a id="l00147"></a>/* clang-format on */
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00154"></a>
<a id="l00155"></a>#ifdef __cplusplus
<a id="l00156"></a>}
<a id="l00157"></a>#endif
<a id="l00158"></a>
<a id="l00159"></a>#endif /* ZEPHYR_INCLUDE_RTIO_CQE_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权属于Intel Corporation（2022年）以及Infineon Technologies AG或其关联公司（2026年）；保留全部权利，许可证为Apache-2.0。原始SPDX记录完整保留。

2. 供CQE结构体池使用的内部结构与函数。

3. 不要尝试重新格式化这些宏。

4. 关闭clang-format自动格式化。

5. 恢复clang-format自动格式化。

6. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_CQE_H_`结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `mpsc_push`

```c
static ALWAYS_INLINE void mpsc_push(struct mpsc *q, struct mpsc_node *n)
```

压入一个节点（Node）。

定义位置（Definition）：mpsc_lockfree.h:126。

符号定位：[mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)。

### `mpsc_pop`

```c
static struct mpsc_node * mpsc_pop(struct mpsc *q)
```

从链表中弹出一个节点。

定义位置（Definition）：mpsc_lockfree.h:145。

符号定位：[mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)。

### `CONTAINER_OF`

```c
#define CONTAINER_OF(ptr, type, field)
```

取得包含指定成员的结构体指针。

定义位置（Definition）：util.h:281。

符号定位：[CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)。

### `mpsc_lockfree.h`

使用单向链表（Singly Linked List）的无等待（Wait-free）侵入式多生产者单消费者队列（Multi-Producer Single-Consumer Queue，MPSC）。

符号定位：[mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)。

### `stdint.h`

符号定位：[stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)。

### `uint32_t`

```c
__UINT32_TYPE__ uint32_t
```

定义位置（Definition）：stdint.h:90。

符号定位：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

### `int32_t`

```c
__INT32_TYPE__ int32_t
```

定义位置（Definition）：stdint.h:74。

符号定位：[int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)。

### `uint16_t`

```c
__UINT16_TYPE__ uint16_t
```

定义位置（Definition）：stdint.h:89。

符号定位：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)。

### `string.h`

符号定位：[string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)。

### `memset`

```c
void * memset(void *buf, int c, size_t n)
```

符号定位：[memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)。

### `mpsc_node`

队列成员（Queue Member）。

定义位置（Definition）：mpsc_lockfree.h:79。

符号定位：[mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)。

### `mpsc`

多生产者单消费者队列（Multi-Producer Single-Consumer Queue，MPSC Queue）。

定义位置（Definition）：mpsc_lockfree.h:86。

符号定位：[mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)。

### `rtio_cqe`

一个完成队列事件（Completion Queue Event，CQE）。

定义位置（Definition）：cqe.h:90。

符号定位：[rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)。

### `rtio_cqe::userdata`

```c
void * userdata
```

与操作关联的用户数据。

定义位置（Definition）：cqe.h:96。

符号定位：[rtio_cqe::userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)。

### `rtio_cqe::flags`

```c
uint32_t flags
```

与操作关联的标志。

定义位置（Definition）：cqe.h:97。

符号定位：[rtio_cqe::flags](../rtio_model_reference/P002_RTIO完成事件.md#a8a7632ef1cfd31529d782bd761908d93)。

### `rtio_cqe::result`

```c
int32_t result
```

操作的结果。

定义位置（Definition）：cqe.h:95。

符号定位：[rtio_cqe::result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)。

### `iterable_sections.h`

可迭代段（Iterable Sections）辅助工具。

符号定位：[iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)。

## 4.4\_源码跟踪译注

> 译注——CQE对象记录result、userdata和flags，并含内部队列节点。对象池分配会清零CQE，归还时把节点放回空闲队列并增加pool_free；完成队列消费与CQE对象归还仍需按核心接口成对处理。不能在归还后继续读取旧CQE指针。

> 译注——CQE对象与数据缓冲区分别管理。RTIO_CQE_FLAG_MEMPOOL_BUFFER指明缓冲区来自内存池，flags编码块索引和块数；取得并处理数据后用rtio_release_buffer归还缓冲区，再按需要释放CQE槽。释放CQE不会自动释放有效载荷。完整约定见[核心接口](../rtio_core_reference/P001_RTIO公共接口.md)。

> 译注——本次编码使用位7..0保存标志、位19..8保存块索引、位31..20保存块数。准备宏只做移位与掩码组合，没有内存分配动作；字段宽度限制与分配长度由使用方遵守，不能把有效数据字节数直接当成块数。

> 译注——本页内部pool_free是普通uint16_t计数；即使队列使用MPSC算法，也不能仅凭队列名称就推断所有对象池API都适用于任意数量的并发消费者或无外部协调的重复释放。使用范围按RTIO核心和调用上下文约定。

头文件相对定位：[include/zephyr/rtio/cqe.h](../../../include/zephyr/rtio/cqe.h)，关联实现／接口：[include/zephyr/rtio/rtio.h](../../../include/zephyr/rtio/rtio.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/cqe.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/rtio.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_RTIO完成事件头文件参考.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [string.h](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html)
- [zephyr/sys/mpsc_lockfree.h](../intercore_reference/P161_MPSC无锁队列头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [rtio_cqe](../rtio_model_reference/P002_RTIO完成事件.md)
- [mpsc_node](../intercore_reference/P160_MPSC无锁队列节点.md)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [result](../rtio_model_reference/P002_RTIO完成事件.md#acbe2e6607a752b676d9336b9ca6ce435)
- [userdata](../rtio_model_reference/P002_RTIO完成事件.md#a15128387ccbea55812ef229eab7241e7)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [flags](../rtio_model_reference/P002_RTIO完成事件.md#a8a7632ef1cfd31529d782bd761908d93)
- [mpsc](../intercore_reference/P159_MPSC无锁队列结构.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [mpsc_pop](../intercore_reference/P158_MPSC无锁队列接口.md#ga823ec37b84ac43e46167aac954bce9d7)
- [CONTAINER_OF](../util_reference/P001_通用工具公共接口.md#gac5bc561d1bfd1bf68877fe577779bd2f)
- [memset](https://docs.zephyrproject.org/latest/doxygen/html/string_8h.html#a4137694174d4ca2fad886a1db355015c)
- [mpsc_push](../intercore_reference/P158_MPSC无锁队列接口.md#ga403add133841ef88e10d74141e782b37)

---

[上一章](P003_RTIO完成事件头文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_RTIO设备头文件参考.md)
