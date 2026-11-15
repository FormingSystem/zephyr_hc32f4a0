---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-170
title: MPSC数据包缓冲区头文件参考
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mpsc__pbuf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第170章\_MPSC数据包缓冲区头文件参考

原文：[mpsc__pbuf_8h](https://docs.zephyrproject.org/latest/doxygen/html/mpsc__pbuf_8h.html)。读取日期：2026-10-13，`latest`。

本页对应多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包缓冲区的`zephyr/sys/mpsc_pbuf.h`头文件参考（Header Reference）。

## 170.1\_依赖文件

```c
#include <zephyr/kernel.h>
#include <zephyr/sys/mpsc_packet.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>
```

## 170.2\_结构与宏

[MPSC数据包缓冲区运行时结构](P168_MPSC数据包缓冲区运行时结构.md)保存缓冲区数据，[MPSC数据包缓冲区配置](P169_MPSC数据包缓冲区配置.md)保存初始化配置。`BIT(n)`为选择第 n 位的位掩码（Bit Mask）宏。

| 宏 | 值 | 含义 |
| --- | --- | --- |
| `MPSC_PBUF_SIZE_POW2` | `BIT(0)` | 表示缓冲区大小是2的幂；大小为2的幂时会应用相应优化 |
| `MPSC_PBUF_MODE_OVERWRITE` | `BIT(1)` | 表示缓冲区满时的处理策略：置位时从已满缓冲区分配会丢弃最旧的数据包；未置位时分配返回空指针 |
| `MPSC_PBUF_MAX_UTILIZATION` | `BIT(2)` | 表示跟踪缓冲区的最大使用量（Maximum Buffer Usage） |
| `MPSC_PBUF_FULL` | `BIT(3)` | 表示缓冲区当前已满（Full） |

## 170.3\_回调类型


```c
typedef uint32_t (*mpsc_pbuf_get_wlen)(const union mpsc_pbuf_generic *packet);
```

获取数据包长度的回调（Callback）原型。返回数据包大小，单位为32位字（32-bit Word）。


```c
typedef void (*mpsc_pbuf_notify_drop)(const struct mpsc_pbuf_buffer *buffer,
                                      const union mpsc_pbuf_generic *packet);
```

数据包被丢弃（Drop）时调用此回调。

## 170.4\_全部函数


```c
void mpsc_pbuf_init(struct mpsc_pbuf_buffer *buffer,
                    const struct mpsc_pbuf_buffer_config *config);
```

初始化数据包缓冲区。


```c
union mpsc_pbuf_generic *mpsc_pbuf_alloc(struct mpsc_pbuf_buffer *buffer,
                                         size_t wlen, k_timeout_t timeout);
```

分配数据包。


```c
void mpsc_pbuf_commit(struct mpsc_pbuf_buffer *buffer,
                        union mpsc_pbuf_generic *packet);
```

提交数据包。


```c
void mpsc_pbuf_put_word(struct mpsc_pbuf_buffer *buffer,
                        const union mpsc_pbuf_generic word);
```

写入单字数据包。


```c
void mpsc_pbuf_put_word_ext(struct mpsc_pbuf_buffer *buffer,
                            const union mpsc_pbuf_generic word,
                            const void *data);
```

写入字与指针组成的数据包。


```c
void mpsc_pbuf_put_data(struct mpsc_pbuf_buffer *buffer,
                        const uint32_t *data, size_t wlen);
```

复制数据包。


```c
const union mpsc_pbuf_generic *mpsc_pbuf_claim(struct mpsc_pbuf_buffer *buffer);
```

领取首个待处理数据包。


```c
void mpsc_pbuf_free(struct mpsc_pbuf_buffer *buffer,
                    const union mpsc_pbuf_generic *packet);
```

释放数据包。


```c
bool mpsc_pbuf_is_pending(struct mpsc_pbuf_buffer *buffer);
```

检查待处理消息。


```c
void mpsc_pbuf_get_utilization(struct mpsc_pbuf_buffer *buffer,
                               uint32_t *size, uint32_t *now);
```

查询当前内存使用量。


```c
int mpsc_pbuf_get_max_utilization(struct mpsc_pbuf_buffer *buffer, uint32_t *max);
```

查询最大内存使用量。

以上11个函数的参数、单位和返回值见[MPSC数据包缓冲区接口](P166_MPSC数据包缓冲区接口.md)，完整源码见[MPSC数据包缓冲区完整头文件](P171_MPSC数据包缓冲区完整头文件.md)。

---

[上一章：MPSC数据包缓冲区配置](P169_MPSC数据包缓冲区配置.md) · [下一章：MPSC数据包缓冲区完整头文件](P171_MPSC数据包缓冲区完整头文件.md) · [返回大纲](大纲.md)
