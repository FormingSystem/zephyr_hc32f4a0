---
id: learning.zephyr-docs.intercore_reference.pbufref-156
title: SPSC数据包缓冲区完整头文件
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spsc__pbuf_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第156章\_SPSC数据包缓冲区完整头文件

原文：[spsc__pbuf_8h_source](https://docs.zephyrproject.org/latest/doxygen/html/spsc__pbuf_8h_source.html)。读取日期：2026-10-13，`latest`。

本页保留`zephyr/sys/spsc_pbuf.h`的完整官方可见源码（Source Code），仅去除网页行号与行尾空白。SPSC 表示单生产者、单消费者（Single Producer, Single Consumer）。版权为2022年 Nordic Semiconductor ASA，许可证标识（License Identifier）为`Apache-2.0`，原声明完整保留。

阅读说明：`CONFIG_`前缀表示 Kconfig 构建配置系统（Build Configuration System）的配置宏。`BIT(0)`通过位掩码（Bit Mask）宏选中第0位，`MAX`宏取较大值。名称中的 LOCAL 为本地（Local），REMOTE 为远端（Remote），DCACHE 为数据缓存（Data Cache），PADDING 为填充（Padding）。缓存处理标志、使用量字段和最大长度宏的数值及含义在后文逐项说明。

## 156.1\_完整源码

```c
/*
 * Copyright (c) 2022 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_SYS_SPSC_PBUF_H_
#define ZEPHYR_INCLUDE_SYS_SPSC_PBUF_H_

#include <zephyr/cache.h>
#include <zephyr/devicetree.h>

#ifdef __cplusplus
extern "C" {
#endif



#define SPSC_PBUF_CACHE BIT(0)

#define SPSC_PBUF_UTILIZATION_BITS 24

#define SPSC_PBUF_UTILIZATION_OFFSET 8


#ifdef CONFIG_DCACHE_LINE_SIZE
#define Z_SPSC_PBUF_LOCAL_DCACHE_LINE CONFIG_DCACHE_LINE_SIZE
#else
#define Z_SPSC_PBUF_LOCAL_DCACHE_LINE 0
#endif

#ifndef CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE
#define CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE 0
#endif

#define Z_SPSC_PBUF_DCACHE_LINE \
        MAX(CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE, Z_SPSC_PBUF_LOCAL_DCACHE_LINE)

#define SPSC_PBUF_MAX_LEN 0xFF00

struct spsc_pbuf_common {
        uint32_t len;           /* Length of data[] in bytes. */
        uint32_t flags;         /* Flags. See @ref SPSC_PBUF_FLAGS */
        uint32_t rd_idx;        /* Index of the first valid byte in data[] */
};

/* Padding to fill cache line. */
#define Z_SPSC_PBUF_PADDING \
        MAX(0, Z_SPSC_PBUF_DCACHE_LINE - (int)sizeof(struct spsc_pbuf_common))

struct spsc_pbuf_ext_cache {
        uint8_t reserved[Z_SPSC_PBUF_PADDING];
        uint32_t wr_idx;        /* Index of the first free byte in data[] */
        uint8_t data[];         /* Buffer data. */
};

struct spsc_pbuf_ext_nocache {
        uint32_t wr_idx;        /* Index of the first free byte in data[] */
        uint8_t data[];         /* Buffer data. */
};

struct spsc_pbuf {
        struct spsc_pbuf_common common;
        union {
                struct spsc_pbuf_ext_cache cache;
                struct spsc_pbuf_ext_nocache nocache;
        } ext;
};

static inline uint32_t spsc_pbuf_capacity(struct spsc_pbuf *pb)
{
        return pb->common.len - sizeof(uint32_t);
}

struct spsc_pbuf *spsc_pbuf_init(void *buf, size_t blen, uint32_t flags);

int spsc_pbuf_write(struct spsc_pbuf *pb, const char *buf, uint16_t len);

int spsc_pbuf_alloc(struct spsc_pbuf *pb, uint16_t len, char **buf);

void spsc_pbuf_commit(struct spsc_pbuf *pb, uint16_t len);

int spsc_pbuf_read(struct spsc_pbuf *pb, char *buf, uint16_t len);

uint16_t spsc_pbuf_claim(struct spsc_pbuf *pb, char **buf);

void spsc_pbuf_free(struct spsc_pbuf *pb, uint16_t len);

int spsc_pbuf_get_utilization(struct spsc_pbuf *pb);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_SYS_SPSC_PBUF_H_ */
```

## 156.2\_可见注释与条件定义

`spsc_pbuf_common.len`是`data[]`的字节长度，`flags`为标志（Flags），参见 SPSC 数据包缓冲区标志；`rd_idx`是`data[]`中第一个有效字节的索引。

`Z_SPSC_PBUF_PADDING`前的注释表示“用于填满缓存行（Cache Line）的填充（Padding）”。缓存扩展及无缓存扩展中的`wr_idx`都是`data[]`第一个空闲字节的索引，`data[]`为缓冲区数据（Buffer Data）。

阅读说明：定义`CONFIG_DCACHE_LINE_SIZE`时，本地数据缓存行大小取该配置值，否则为0；未定义`CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE`时补充默认值0。最终`Z_SPSC_PBUF_DCACHE_LINE`取本地与远端数据缓存行大小的最大值。填充宏再根据公共结构大小计算所需填充，不能把参考页某次展开结果推广到所有目标平台。

`SPSC_PBUF_CACHE`取第0位，要求处理缓存；最大使用量（Maximum Utilization）的字段宽度为24位、偏移为8位。`SPSC_PBUF_MAX_LEN`为`0xFF00`。这几项含义来自[SPSC数据包缓冲区头文件参考](P155_SPSC数据包缓冲区头文件参考.md)中的宏说明。

`__cplusplus`分支提供 C++ 的 C 语言链接约定；末尾注释标记头文件保护宏`ZEPHYR_INCLUDE_SYS_SPSC_PBUF_H_`的结束。网页没有显示的接口文档注释不补造为源码，函数参数与约束见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。

---

[上一章：SPSC数据包缓冲区头文件参考](P155_SPSC数据包缓冲区头文件参考.md) · [下一章：SPSC数据包缓冲区标志](P157_SPSC数据包缓冲区标志.md) · [返回大纲](大纲.md)
