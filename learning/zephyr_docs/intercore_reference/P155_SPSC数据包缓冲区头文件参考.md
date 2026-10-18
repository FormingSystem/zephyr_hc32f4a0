---
id: learning.zephyr-docs.intercore_reference.pbufref-155
title: SPSC数据包缓冲区头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/spsc__pbuf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第155章\_SPSC数据包缓冲区头文件参考

原文：[spsc__pbuf_8h](https://docs.zephyrproject.org/latest/doxygen/html/spsc__pbuf_8h.html)。读取日期：2026-10-13，`latest`。

本页对应`zephyr/sys/spsc_pbuf.h`头文件参考（Header Reference）。SPSC 表示单生产者、单消费者（Single Producer, Single Consumer）。原文件包含以下依赖：

```c
#include <zephyr/cache.h>
#include <zephyr/devicetree.h>
```

## 155.1\_数据结构

- [SPSC数据包缓冲区公共布局](P152_SPSC数据包缓冲区公共布局.md)。
- [SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md)。
- [SPSC数据包缓冲区无缓存扩展](P154_SPSC数据包缓冲区无缓存扩展.md)。
- [SPSC数据包缓冲区结构](P151_SPSC数据包缓冲区结构.md)。

下表的`BIT`是生成指定位掩码（Bit Mask）的宏，`BIT(0)`选中第0位；它是代码标识符，不是需要另行展开的产品缩写。`CONFIG_`前缀表示 Kconfig 构建配置系统（Build Configuration System）的配置宏。

## 155.2\_宏定义

| 宏 | 原页取值或定义位置 | 含义 |
| --- | --- | --- |
| `SPSC_PBUF_CACHE` | `BIT(0)` | 表示需要处理缓存的标志 |
| `SPSC_PBUF_UTILIZATION_BITS` | `24` | 保存最大使用量字段的位数 |
| `SPSC_PBUF_UTILIZATION_OFFSET` | `8` | 保存最大使用量字段的位偏移 |
| `CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE` | `0` | 未配置时的远端数据缓存行默认值 |
| `SPSC_PBUF_MAX_LEN` | `0xFF00` | 最大数据包长度 |

## 155.3\_函数接口


```c
static inline uint32_t spsc_pbuf_capacity(struct spsc_pbuf *pb);
```

查询容量。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
struct spsc_pbuf *spsc_pbuf_init(void *buf, size_t blen, uint32_t flags);
```

初始化缓冲区。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
int spsc_pbuf_write(struct spsc_pbuf *pb, const char *buf, uint16_t len);
```

写入数据。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
int spsc_pbuf_alloc(struct spsc_pbuf *pb, uint16_t len, char **buf);
```

分配连续空间。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
void spsc_pbuf_commit(struct spsc_pbuf *pb, uint16_t len);
```

提交数据包。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
int spsc_pbuf_read(struct spsc_pbuf *pb, char *buf, uint16_t len);
```

读取完整消息。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
uint16_t spsc_pbuf_claim(struct spsc_pbuf *pb, char **buf);
```

领取数据包。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
void spsc_pbuf_free(struct spsc_pbuf *pb, uint16_t len);
```

释放数据包。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。


```c
int spsc_pbuf_get_utilization(struct spsc_pbuf *pb);
```

查询最大使用量。参数、返回值及使用条件见[SPSC数据包缓冲区接口](P150_SPSC数据包缓冲区接口.md)。

完整官方可见源码见[SPSC数据包缓冲区完整头文件](P156_SPSC数据包缓冲区完整头文件.md)。

---

[上一章：SPSC数据包缓冲区无缓存扩展](P154_SPSC数据包缓冲区无缓存扩展.md) · [下一章：SPSC数据包缓冲区完整头文件](P156_SPSC数据包缓冲区完整头文件.md) · [返回大纲](大纲.md)
