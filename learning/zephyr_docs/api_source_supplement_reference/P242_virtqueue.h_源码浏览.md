---
id: learning.zephyr-docs.api-source-supplement-reference.page-242
title: virtqueue.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/virtqueue_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第242章\_virtqueue.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/virtqueue_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P595_VirtIO队列头文件.md)。

## 242.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00034"></a>
<a id="l00038"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00053"></a>
<a id="l00057"></a>
<a id="l00061"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00081"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00109"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00117"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00138"></a>
<a id="l00138"></a>
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00163"></a>
<a id="l00167"></a>
<a id="l00171"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00181"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="foldopen00222"></a>
<a id="l00222"></a>
<a id="l00226"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="agroup__virtqueue__interface_html_ga311909fbebf3cb96ace6c751fabcf708"></a>
<a id="agroup__virtqueue__interface_html_ga3dce3b5099fc117a94da63a24571b6c3"></a>
<a id="agroup__virtqueue__interface_html_ga55abe7b8204cf0b57cd1c2380dcd66fb"></a>
<a id="agroup__virtqueue__interface_html_ga5e01b141e28aec876c298047f8d623a6"></a>
<a id="agroup__virtqueue__interface_html_ga79b1b54f0ea6fe8b5110712488f663eb"></a>
<a id="agroup__virtqueue__interface_html_ga9443eb15529fa16d1024a70075daca28"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__spinlock_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructvirtq__avail_html"></a>
<a id="astructvirtq__avail_html_a03f0bc25a3459316bd166f3cbf9a66c3"></a>
<a id="astructvirtq__avail_html_a70caebae8d3a86d05cb718c5e0a9f88d"></a>
<a id="astructvirtq__avail_html_ab013600ebaa7a4c855112599755ce607"></a>
<a id="astructvirtq__buf_html"></a>
<a id="astructvirtq__buf_html_aaa047b4296f5c104d5a8f5eaf48aaaac"></a>
<a id="astructvirtq__buf_html_ad05060db8d467017fca4af593bab9417"></a>
<a id="astructvirtq__desc_html"></a>
<a id="astructvirtq__desc_html_a1d5146808360ff5e359673c193fe4d53"></a>
<a id="astructvirtq__desc_html_a1dcd1400d72aa7b628920258e226a7ce"></a>
<a id="astructvirtq__desc_html_a2703fcd4eb5bf97530687444203e8ee6"></a>
<a id="astructvirtq__desc_html_a9731d25acdd201e07e4362f79fb5ba9e"></a>
<a id="astructvirtq__receive__callback__entry_html"></a>
<a id="astructvirtq__receive__callback__entry_html_adc164ebec52cd00cc15839b1cda4be56"></a>
<a id="astructvirtq__receive__callback__entry_html_ae892b29ffebb17cba4154e342278908d"></a>
<a id="astructvirtq__used__elem_html"></a>
<a id="astructvirtq__used__elem_html_a7f1f8b4bc3590a00e85bed3657a9fbdc"></a>
<a id="astructvirtq__used__elem_html_ad61ce7642ec40dba74c2f8ffd28ba8ed"></a>
<a id="astructvirtq__used_html"></a>
<a id="astructvirtq__used_html_a36575313c28554dda228a32ed58156e8"></a>
<a id="astructvirtq__used_html_a77e64d4bc15ae058515aa96987794f90"></a>
<a id="astructvirtq__used_html_ad3e466c8aee5efcfef250e907717e656"></a>
<a id="astructvirtq_html"></a>
<a id="astructvirtq_html_a2cd048d18e1f8f30a197f33f24f53575"></a>
<a id="astructvirtq_html_a441e32c89c78d6b432469957cb38db25"></a>
<a id="astructvirtq_html_a540cc380e0e9ec5fc92cf1ea7f3252fe"></a>
<a id="astructvirtq_html_a7f12283618d0acc418d378a8d554215d"></a>
<a id="astructvirtq_html_a811241bbc1032b299f303c96e45e39c8"></a>
<a id="astructvirtq_html_a872b79dd002eb3adf0f680c252323346"></a>
<a id="astructvirtq_html_aa299da6b7d7b4ede53423d17d3973a92"></a>
<a id="astructvirtq_html_aa4a4101177743201210ec1267df31b57"></a>
<a id="astructvirtq_html_afeb3f726fe78a18574d7ddd77a1837f9"></a>

```c
/*
 * Copyright (c) 2024 Antmicro <www.antmicro.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_VIRTIO_VIRTQUEUE_H_
#define ZEPHYR_VIRTIO_VIRTQUEUE_H_
#include <stdint.h>
#include <stddef.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Based on Virtual I/O Device (VIRTIO) Version 1.3 specification:
 * https://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.pdf
 */


#define VIRTQ_DESC_F_NEXT 1
#define VIRTQ_DESC_F_WRITE 2

struct virtq_desc {
        uint64_t addr;
        uint32_t len;
        uint16_t flags;
        uint16_t next;
};

struct virtq_avail {
        uint16_t flags;
        uint16_t idx;
        uint16_t ring[];
};

struct virtq_used_elem {
        uint32_t id;
        uint32_t len;
};

struct virtq_used {
        uint16_t flags;
        uint16_t idx;
        struct virtq_used_elem ring[];
};

typedef void (*virtq_receive_callback)(void *opaque, uint32_t used_len);

struct virtq_receive_callback_entry {
        virtq_receive_callback cb;
        void *opaque;
};

struct virtq {
        struct k_spinlock lock;

        uint16_t num;
        struct virtq_desc *desc;
        struct virtq_avail *avail;
        struct virtq_used *used;

        uint16_t last_used_idx;
        struct k_stack free_desc_stack;

        uint16_t free_desc_n;

        struct virtq_receive_callback_entry *recv_cbs;
};


int virtq_create(struct virtq *v, size_t size);

void virtq_free(struct virtq *v);

struct virtq_buf {
        void *addr;
        uint32_t len;
};

int virtq_add_buffer_chain(
        struct virtq *v, struct virtq_buf *bufs, uint16_t bufs_size,
        uint16_t device_readable_count, virtq_receive_callback cb, void *cb_opaque,
        k_timeout_t timeout
);

void virtq_add_free_desc(struct virtq *v, uint16_t desc_idx);

int virtq_get_free_desc(struct virtq *v, uint16_t *desc_idx, k_timeout_t timeout);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_VIRTIO_VIRTQUEUE_H_ */
```

## 242.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Antmicro <www.antmicro.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 23 行

依据《虚拟 I/O 设备（Virtual I/O Device，VIRTIO）1.3 版规范》：[官方规范](https://docs.oasis-open.org/virtio/virtio/v1.3/csd01/virtio-v1.3-csd01.pdf)。

### 注释 3：原第 284 行

头文件保护宏（Header guard）标记：`ZEPHYR_VIRTIO_VIRTQUEUE_H_`。

## 242.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P595_VirtIO队列头文件.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [virtq_desc](../hardware/P573_VirtIO队列描述符.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1d5146808360ff5e359673c193fe4d53)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1dcd1400d72aa7b628920258e226a7ce)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a9731d25acdd201e07e4362f79fb5ba9e)
- [next](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a2703fcd4eb5bf97530687444203e8ee6)
- [virtq_avail](../hardware/P574_VirtIO可用环.md)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#ab013600ebaa7a4c855112599755ce607)
- [idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#a70caebae8d3a86d05cb718c5e0a9f88d)
- [ring](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#a03f0bc25a3459316bd166f3cbf9a66c3)
- [virtq_used_elem](../hardware/P575_VirtIO已用链条目.md)
- [id](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#a7f1f8b4bc3590a00e85bed3657a9fbdc)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#ad61ce7642ec40dba74c2f8ffd28ba8ed)
- [virtq_used](../hardware/P576_VirtIO已用环.md)
- [flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#a77e64d4bc15ae058515aa96987794f90)
- [idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#ad3e466c8aee5efcfef250e907717e656)
- [ring](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#a36575313c28554dda228a32ed58156e8)
- [virtq_receive_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga311909fbebf3cb96ace6c751fabcf708)
- [virtq_receive_callback_entry](../hardware/P577_VirtIO接收回调条目.md)
- [cb](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#ae892b29ffebb17cba4154e342278908d)
- [opaque](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#adc164ebec52cd00cc15839b1cda4be56)
- [virtq](../hardware/P578_VirtIO队列结构.md)
- [k_spinlock](../kernel/P066_自旋锁结构参考.md)
- [lock](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa4a4101177743201210ec1267df31b57)
- [num](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#afeb3f726fe78a18574d7ddd77a1837f9)
- [desc](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa299da6b7d7b4ede53423d17d3973a92)
- [avail](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a872b79dd002eb3adf0f680c252323346)
- [used](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a7f12283618d0acc418d378a8d554215d)
- [last_used_idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a811241bbc1032b299f303c96e45e39c8)
- [free_desc_stack](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a441e32c89c78d6b432469957cb38db25)
- [free_desc_n](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a540cc380e0e9ec5fc92cf1ea7f3252fe)
- [recv_cbs](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a2cd048d18e1f8f30a197f33f24f53575)
- [virtq_create](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga3dce3b5099fc117a94da63a24571b6c3)
- [virtq_free](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga9443eb15529fa16d1024a70075daca28)
- [virtq_buf](../hardware/P579_VirtIO缓冲区结构.md)
- [addr](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#ad05060db8d467017fca4af593bab9417)
- [len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#aaa047b4296f5c104d5a8f5eaf48aaaac)
- [virtq_add_buffer_chain](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga5e01b141e28aec876c298047f8d623a6)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [virtq_add_free_desc](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga55abe7b8204cf0b57cd1c2380dcd66fb)
- [virtq_get_free_desc](https://docs.zephyrproject.org/latest/doxygen/html/group__virtqueue__interface.html#ga79b1b54f0ea6fe8b5110712488f663eb)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [virtq_avail::ring](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#a03f0bc25a3459316bd166f3cbf9a66c3)
- [virtq_avail::idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#a70caebae8d3a86d05cb718c5e0a9f88d)
- [virtq_avail::flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__avail.html#ab013600ebaa7a4c855112599755ce607)
- [virtq_buf::len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#aaa047b4296f5c104d5a8f5eaf48aaaac)
- [virtq_buf::addr](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__buf.html#ad05060db8d467017fca4af593bab9417)
- [virtq_desc::addr](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1d5146808360ff5e359673c193fe4d53)
- [virtq_desc::len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a1dcd1400d72aa7b628920258e226a7ce)
- [virtq_desc::next](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a2703fcd4eb5bf97530687444203e8ee6)
- [virtq_desc::flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__desc.html#a9731d25acdd201e07e4362f79fb5ba9e)
- [virtq_receive_callback_entry::opaque](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#adc164ebec52cd00cc15839b1cda4be56)
- [virtq_receive_callback_entry::cb](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__receive__callback__entry.html#ae892b29ffebb17cba4154e342278908d)
- [virtq_used_elem::id](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#a7f1f8b4bc3590a00e85bed3657a9fbdc)
- [virtq_used_elem::len](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used__elem.html#ad61ce7642ec40dba74c2f8ffd28ba8ed)
- [virtq_used::ring](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#a36575313c28554dda228a32ed58156e8)
- [virtq_used::flags](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#a77e64d4bc15ae058515aa96987794f90)
- [virtq_used::idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq__used.html#ad3e466c8aee5efcfef250e907717e656)
- [virtq::recv_cbs](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a2cd048d18e1f8f30a197f33f24f53575)
- [virtq::free_desc_stack](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a441e32c89c78d6b432469957cb38db25)
- [virtq::free_desc_n](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a540cc380e0e9ec5fc92cf1ea7f3252fe)
- [virtq::used](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a7f12283618d0acc418d378a8d554215d)
- [virtq::last_used_idx](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a811241bbc1032b299f303c96e45e39c8)
- [virtq::avail](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#a872b79dd002eb3adf0f680c252323346)
- [virtq::desc](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa299da6b7d7b4ede53423d17d3973a92)
- [virtq::lock](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#aa4a4101177743201210ec1267df31b57)
- [virtq::num](https://docs.zephyrproject.org/latest/doxygen/html/structvirtq.html#afeb3f726fe78a18574d7ddd77a1837f9)

---

[上一章](P241_utsname.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P243_word_granular_access.h_源码浏览.md)
