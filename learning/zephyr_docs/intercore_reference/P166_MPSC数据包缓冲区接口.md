---
id: learning.zephyr-docs.intercore_reference.mpscpbufref-166
title: MPSC数据包缓冲区接口
kind: reference
status: maintained
domains: [zephyr, intercore_reference]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第166章\_MPSC数据包缓冲区接口

原文：[group__mpsc__buf](https://docs.zephyrproject.org/latest/doxygen/html/group__mpsc__buf.html)。读取日期：2026-10-13，`latest`。

本页介绍多生产者、单消费者（Multiple Producer, Single Consumer，MPSC）数据包缓冲区（Packet Buffer）的应用程序编程接口（Application Programming Interface，API）。头文件为`zephyr/sys/mpsc_pbuf.h`。

数据包头部见[MPSC数据包描述接口](P172_MPSC数据包描述接口.md)，模式标志见[MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md)，运行时结构与配置分别见[MPSC数据包缓冲区运行时结构](P168_MPSC数据包缓冲区运行时结构.md)和[MPSC数据包缓冲区配置](P169_MPSC数据包缓冲区配置.md)。

阅读时区分两个单位：分配长度、数据包字长以及结构中的容量以32位字（32-bit Word）计；两个使用量查询函数的输出以字节（Byte）计。分配超时的类型为`k_timeout_t`，即内核超时类型（Kernel Timeout Type）。

## 166.1\_获取数据包字长的回调

```c
typedef uint32_t (*mpsc_pbuf_get_wlen)(const union mpsc_pbuf_generic *packet);
```

获取数据包长度的回调（Callback）原型。

| 参数 | 含义 |
| --- | --- |
| `packet` | 用户数据包 |

返回数据包大小，单位为32位字（32-bit Word）。

## 166.2\_数据包丢弃通知回调

```c
typedef void (*mpsc_pbuf_notify_drop)(const struct mpsc_pbuf_buffer *buffer,
                                      const union mpsc_pbuf_generic *packet);
```

数据包被丢弃（Drop）时调用此回调。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 数据包缓冲区 |
| `packet` | 正在被丢弃的数据包 |

## 166.3\_初始化数据包缓冲区

```c
void mpsc_pbuf_init(struct mpsc_pbuf_buffer *buffer,
                    const struct mpsc_pbuf_buffer_config *config);
```

初始化数据包缓冲区。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `config` | 配置 |

## 166.4\_分配数据包

```c
union mpsc_pbuf_generic *mpsc_pbuf_alloc(struct mpsc_pbuf_buffer *buffer,
                                         size_t wlen, k_timeout_t timeout);
```

分配（Allocate）一个数据包。配置为覆盖模式（Overwrite Mode）时，如果没有空间分配新的缓冲区，就丢弃最旧的数据包；未配置覆盖模式时，分配失败并返回空指针（Null Pointer）。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `wlen` | 要分配的字数，单位为32位字（32-bit Word） |
| `timeout` | 超时（Timeout）。在线程上下文（Thread Context）中调用且不能立即分配数据包时，先按给定超时等待，再丢弃最旧的数据包或返回空指针 |

返回所分配空间的指针；无法分配时返回`NULL`。

## 166.5\_提交数据包

```c
void mpsc_pbuf_commit(struct mpsc_pbuf_buffer *buffer,
                        union mpsc_pbuf_generic *packet);
```

提交（Commit）一个数据包。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `packet` | 指向`mpsc_pbuf_alloc()`分配的数据包的指针 |

## 166.6\_写入单字数据包

```c
void mpsc_pbuf_put_word(struct mpsc_pbuf_buffer *buffer,
                        const union mpsc_pbuf_generic word);
```

将单字数据包放入缓冲区。本函数针对能放进一个字（Word）的数据包进行了优化。**这个字中的2位由缓冲区使用。**

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `word` | 数据包内容：包含`MPSC_PBUF_HDR`且有效位（Valid Bit）已置位，其余位保存数据 |

## 166.7\_写入字与指针组成的数据包

```c
void mpsc_pbuf_put_word_ext(struct mpsc_pbuf_buffer *buffer,
                            const union mpsc_pbuf_generic word,
                            const void *data);
```

将由一个字和一个指针（Pointer）组成的数据包放入缓冲区，本函数针对这种数据包进行优化。**第一个字中的2位由缓冲区使用。**

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `word` | 数据包的第一个字：包含`MPSC_PBUF_HDR`且有效位已置位，其余位保存数据 |
| `data` | 用户数据（User Data）指针 |

阅读说明：原文描述的是“字与指针”组成的数据包，没有承诺复制该指针指向的全部用户数据；不要把它与`mpsc_pbuf_put_data()`混淆。

## 166.8\_复制数据包

```c
void mpsc_pbuf_put_data(struct mpsc_pbuf_buffer *buffer,
                        const uint32_t *data, size_t wlen);
```

将数据复制到缓冲区。**第一个字中的2位由缓冲区使用。**

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `data` | 数据的第一个字必须包含`MPSC_PBUF_HDR`，且有效位已置位 |
| `wlen` | 数据包大小，单位为32位字 |

## 166.9\_领取首个待处理数据包

```c
const union mpsc_pbuf_generic *mpsc_pbuf_claim(struct mpsc_pbuf_buffer *buffer);
```

领取（Claim）第一个待处理（Pending）的数据包。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |

返回所领取数据包的指针；没有可用数据包时返回`NULL`。

## 166.10\_释放数据包

```c
void mpsc_pbuf_free(struct mpsc_pbuf_buffer *buffer,
                    const union mpsc_pbuf_generic *packet);
```

释放（Free）一个数据包。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |
| `packet` | 要释放的数据包 |

## 166.11\_检查待处理消息

```c
bool mpsc_pbuf_is_pending(struct mpsc_pbuf_buffer *buffer);
```

检查是否有待处理消息。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 缓冲区 |

| 返回值 | 含义 |
| --- | --- |
| `true` | 有待处理消息 |
| `false` | 没有待处理消息 |



## 166.12\_查询当前内存使用量

```c
void mpsc_pbuf_get_utilization(struct mpsc_pbuf_buffer *buffer,
                               uint32_t *size, uint32_t *now);
```

获取当前内存使用量（Current Memory Utilization）。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 输入／输出（in,out）：缓冲区 |
| `size` | 输出（out）：缓冲区大小，单位为字节（Byte） |
| `now` | 输出（out）：当前缓冲区使用量，单位为字节 |

## 166.13\_查询最大内存使用量

```c
int mpsc_pbuf_get_max_utilization(struct mpsc_pbuf_buffer *buffer, uint32_t *max);
```

获取最大内存使用量（Maximum Memory Utilization）。

| 参数 | 含义 |
| --- | --- |
| `buffer` | 输入／输出（in,out）：缓冲区 |
| `max` | 输出（out）：最大缓冲区使用量，单位为字节 |

| 返回值 | 含义 |
| --- | --- |
| `0` | 成功收集使用量数据 |
| `-ENOTSUP` | 不支持收集使用量数据 |



译注：原页把两项`retval`写成普通正文，这里按其原意整理为返回值表，没有新增错误条件。

---

[上一章：SPSC无锁队列完整头文件](P165_SPSC无锁队列完整头文件.md) · [下一章：MPSC数据包缓冲区标志](P167_MPSC数据包缓冲区标志.md) · [返回大纲](大纲.md)
