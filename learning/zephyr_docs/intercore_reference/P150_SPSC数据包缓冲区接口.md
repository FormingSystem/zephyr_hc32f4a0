---
id: learning.zephyr-docs.intercore_reference.pbufref-150
title: SPSC数据包缓冲区接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第150章\_SPSC数据包缓冲区接口

原文：[group__spsc__buf](https://docs.zephyrproject.org/latest/doxygen/html/group__spsc__buf.html)。读取日期：2026-10-13，`latest`。

本页介绍单生产者、单消费者（Single Producer, Single Consumer，SPSC）数据包缓冲区（Packet Buffer）的应用程序编程接口（Application Programming Interface，API）。使用头文件`zephyr/sys/spsc_pbuf.h`。

相关主题为[SPSC 数据包缓冲区标志（Flags）](P157_SPSC数据包缓冲区标志.md)；结构见[SPSC数据包缓冲区结构](P151_SPSC数据包缓冲区结构.md)、[SPSC数据包缓冲区公共布局](P152_SPSC数据包缓冲区公共布局.md)、[SPSC数据包缓冲区缓存扩展](P153_SPSC数据包缓冲区缓存扩展.md)和[SPSC数据包缓冲区无缓存扩展](P154_SPSC数据包缓冲区无缓存扩展.md)。

名称以`CONFIG_`开头的宏由 Kconfig 构建配置系统（Build Configuration System）提供。本文的分配（Allocation）、提交（Commit）、领取（Claim）和释放（Free）分别是生产者与消费者操作数据包的阶段。

## 150.1\_宏定义

| 宏 | 原页取值 | 含义 |
| --- | --- | --- |
| `CONFIG_SPSC_PBUF_REMOTE_DCACHE_LINE` | `0` | 原参考页展示的定义；完整头文件仅在该配置未定义时补充此默认值 |
| `SPSC_PBUF_MAX_LEN` | `0xFF00` | 最大数据包长度（Maximum Packet Length） |

## 150.2\_查询容量

```c
static inline uint32_t spsc_pbuf_capacity(struct spsc_pbuf *pb)
{
        return pb->common.len - sizeof(uint32_t);
}
```

容量（Capacity）是专门用于存储数据包的数据空间大小。**每个数据包前面还有2字节长度头部**，所以能够存储的最长数据包小于此容量。

| 参数 | 含义 |
| --- | --- |
| `pb` | 数据包缓冲区 |

| 返回值 | 含义 |
| --- | --- |
| `uint32_t` | 数据包缓冲区容量 |

## 150.3\_初始化缓冲区

```c
struct spsc_pbuf *spsc_pbuf_init(void *buf, size_t blen, uint32_t flags);
```

在专用内存区域上初始化数据包缓冲区。

| 参数 | 含义 |
| --- | --- |
| `buf` | 创建缓冲区的内存区域指针；使用缓存时必须按`Z_SPSC_PBUF_DCACHE_LINE`对齐，否则必须按32位字（32-bit Word）对齐 |
| `blen` | 缓冲区长度，必须足以容纳内部结构以及至少两个字节的数据；原文补充：“其中一个保留给已写入消息的长度” |
| `flags` | 选项标志（Option Flags），参见 SPSC 数据包缓冲区标志 |

| 返回值 | 含义 |
| --- | --- |
| `struct spsc_pbuf *` | 所创建缓冲区的指针，**与`buf`指向相同地址** |
| `NULL` | 缓冲区对齐无效 |

译注：这里保留原文“至少两个字节、其中一个保留给长度”的表述；容量接口另明确写有2字节长度头部。两处原始表述不一致，不能据初始化段落推导长度头部只有1字节。

## 150.4\_写入数据

```c
int spsc_pbuf_write(struct spsc_pbuf *pb, const char *buf, uint16_t len);
```

将`spsc_pbuf_alloc()`分配和`spsc_pbuf_commit()`提交合并为一次调用，向数据包缓冲区写入指定数量的数据。

| 参数 | 含义 |
| --- | --- |
| `pb` | 目标数据包缓冲区 |
| `buf` | 待写入数据的指针 |
| `len` | 待写入字节数，**必须为正数且小于`SPSC_PBUF_MAX_LEN`** |

| 返回值 | 含义 |
| --- | --- |
| `int` | 成功返回已写入字节数，失败返回负错误码 |
| `-EINVAL` | `len == 0` |
| `-ENOMEM` | `len`大于缓冲区能够容纳的长度 |

## 150.5\_分配连续空间

```c
int spsc_pbuf_alloc(struct spsc_pbuf *pb, uint16_t len, char **buf);
```

尝试在数据包缓冲区内分配`len`字节连续内存（Contiguous Memory）。分配发生回绕（Wrap）时，在缓冲区末尾加入内部填充（Padding）。除了填充，分配不改变缓冲区状态，因此分配后若不再需要该数据包，就不必提交。

必须通过`spsc_pbuf_commit()`提交已分配缓冲区，数据包才可供读取。分配出来的缓冲区保证按32位字对齐。

**原文注意事项：使用数据缓存（Data Cache）时，用户负责将新数据写回（Writeback）。**

| 参数 | 含义 |
| --- | --- |
| `pb` | 输入（in）：目标数据包缓冲区 |
| `len` | 输入（in）：分配长度，必须为正数。小于`SPSC_PBUF_MAX_LEN`而无法满足请求长度时，会尝试分配尽可能大的空间，可能加入回绕填充；等于`SPSC_PBUF_MAX_LEN`时，会尝试分配**不加入回绕填充**所能取得的最大缓冲区 |
| `buf` | 输出（out）：分配成功后写入缓冲区地址的位置 |

| 返回值 | 含义 |
| --- | --- |
| `非负值` | 实际分配的空间大小，可能等于或小于`len` |
| `-EINVAL` | `len`为不允许的值 |

## 150.6\_提交数据包

```c
void spsc_pbuf_commit(struct spsc_pbuf *pb, uint16_t len);
```

提交先前由`spsc_pbuf_alloc()`分配的数据包。若使用缓存，会对已写入的数据执行缓存写回。

| 参数 | 含义 |
| --- | --- |
| `pb` | 目标数据包缓冲区 |
| `len` | 数据包长度，必须等于或小于分配时使用的长度 |

译注：分配接口提醒用户负责新数据写回，提交接口则明确说明会执行写回。本译文保留两处原文要求，没有据其中一处删去另一处。

## 150.7\_读取完整消息

```c
int spsc_pbuf_read(struct spsc_pbuf *pb, char *buf, uint16_t len);
```

一次读取对应一次写入发送的消息，提供的`buf`必须足够容纳整条消息。本函数将`spsc_pbuf_claim()`领取和`spsc_pbuf_free()`释放合并为一次调用。

| 参数 | 含义 |
| --- | --- |
| `pb` | 要从中读取数据的数据包缓冲区 |
| `buf` | 保存读取数据的指针；为`NULL`时返回已存储消息的长度 |
| `len` | 要从缓冲区读取的字节数 |

| 返回值 | 含义 |
| --- | --- |
| `int` | 成功返回已读字节数，失败返回负错误码；`buf == NULL`时返回待读字节数 |
| `-ENOMEM` | 消息无法放入提供的`buf` |
| `-EAGAIN` | 整条消息尚未准备好 |

## 150.8\_领取数据包

```c
uint16_t spsc_pbuf_claim(struct spsc_pbuf *pb, char **buf);
```

按`spsc_pbuf_commit()`的提交顺序领取单个数据包，先提交的先领取，即先进先出（First In, First Out，FIFO）。返回的缓冲区按32位字对齐，指向连续内存。领取（Claim）的数据包必须通过`spsc_pbuf_free()`释放。

使用数据缓存时，会对该数据包执行缓存失效（Cache Invalidation）。

| 参数 | 含义 |
| --- | --- |
| `pb` | 输入（in）：要从中领取数据包的缓冲区 |
| `buf` | 输入／输出（in,out）：写入已领取数据包地址的位置；该地址按32位字对齐并指向连续内存 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 缓冲区中没有数据包 |
| `正值` | 数据包长度 |

## 150.9\_释放数据包

```c
void spsc_pbuf_free(struct spsc_pbuf *pb, uint16_t len);
```

将数据包释放回缓冲区。**释放前必须通过`spsc_pbuf_claim()`领取数据包。**

| 参数 | 含义 |
| --- | --- |
| `pb` | 先前从中领取数据包的数据包缓冲区 |
| `len` | 已领取数据包的长度 |

## 150.10\_查询最大使用量

```c
int spsc_pbuf_get_utilization(struct spsc_pbuf *pb);
```

获取数据包缓冲区的最大使用量（Maximum Utilization），可用于调整缓冲区大小。此功能由`CONFIG_SPSC_PBUF_UTILIZATION`启用，**使用量由消费者（Consumer）更新**。

| 参数 | 含义 |
| --- | --- |
| `pb` | 数据包缓冲区 |

| 返回值 | 含义 |
| --- | --- |
| `-ENOTSUP` | 未启用该功能 |
| `非负值` | 最大使用量 |

---

[上一章：核间数据包缓冲区完整头文件](P149_核间数据包缓冲区完整头文件.md) · [下一章：SPSC数据包缓冲区结构](P151_SPSC数据包缓冲区结构.md) · [返回大纲](大纲.md)
