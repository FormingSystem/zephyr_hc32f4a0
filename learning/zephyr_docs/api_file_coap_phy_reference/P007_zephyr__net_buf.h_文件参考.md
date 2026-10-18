---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-7
title: zephyr__net_buf.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_zephyr\_\_net\_buf.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

缓冲区管理（Buffer Management）。

<a id="details"></a>

```c
#include <stddef.h>
#include <zephyr/types.h>
#include <zephyr/sys/util.h>
#include <zephyr/kernel.h>
#include <zephyr/sys/iterable_sections.h>
```

查看此文件的源码。

缓冲区管理（Buffer Management）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 7.1\_数据结构（Data Structures）

<a id="r_net_5Fbuf_5Fsimple"></a>

```c
struct net_buf_simple
```

相关声明：[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

简单网络缓冲区（Simple Network Buffer）的表示。

<a id="r_net_5Fbuf_5Fsimple_5Fstate"></a>

```c
struct net_buf_simple_state
```

相关声明：[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)。

缓冲区的解析状态（Parsing State）。

<a id="r_net_5Fbuf"></a>

```c
struct net_buf
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

网络缓冲区（Network Buffer）的表示。

<a id="r_net_5Fbuf_5Fpool"></a>

```c
struct net_buf_pool
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

网络缓冲池（Network Buffer Pool）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 7.2\_宏定义（Macros）

<a id="r_gaf85aa0b705bb4fbe2630191fde802501"></a>

```c
#define NET_BUF_SIMPLE_DEFINE(_name, _size)
```

相关声明：[NET_BUF_SIMPLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf85aa0b705bb4fbe2630191fde802501)。

定义一个位于栈上的 net_buf_simple 变量（Stack Variable）。

<a id="r_ga21ced8b3082d57bf071008de5fffc0f4"></a>

```c
#define NET_BUF_SIMPLE_DEFINE_STATIC(_name, _size)
```

相关声明：[NET_BUF_SIMPLE_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga21ced8b3082d57bf071008de5fffc0f4)。

定义一个静态 net_buf_simple 变量（Static Variable）。

<a id="r_ga0b01dc80027d13b1895379d4d1397207"></a>

```c
#define NET_BUF_SIMPLE(_size)
```

相关声明：[NET_BUF_SIMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0b01dc80027d13b1895379d4d1397207)。

定义一个位于栈上的 net_buf_simple 变量（Stack Variable），并获取指向它的指针。

<a id="r_gaaeacbdf3cfda12691c75253015e5c19a"></a>

```c
#define NET_BUF_EXTERNAL_DATA BIT(0)
```

相关声明：[NET_BUF_EXTERNAL_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaeacbdf3cfda12691c75253015e5c19a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示缓冲区（Buffer）关联的数据指针指向外部分配内存（Externally Allocated Memory）的标志。

<a id="r_ga61671ac866081d31dfe9eddbf3b6f210"></a>

```c
#define NET_BUF_POOL_HEAP_DEFINE(_name, _count, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_HEAP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga61671ac866081d31dfe9eddbf3b6f210)。

定义一个使用堆（Heap）存储数据的新缓冲池（Buffer Pool）。

<a id="r_gacc53824e01db7935bcc9cad564b716cd"></a>

```c
#define NET_BUF_POOL_FIXED_DEFINE(_name, _count, _data_size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_FIXED_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacc53824e01db7935bcc9cad564b716cd)。

定义一个基于固定大小数据（Fixed-size Data）的新缓冲池（Buffer Pool）。

<a id="r_ga90e691e793c964847d737f5ecf7646ec"></a>

```c
#define NET_BUF_POOL_VAR_DEFINE(_name, _count, _data_size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_VAR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga90e691e793c964847d737f5ecf7646ec)。

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

<a id="r_gaf9d47aed60bc1da8fa40cc8160251ecd"></a>

```c
#define NET_BUF_POOL_VAR_ALIGN_DEFINE(_name, _count, _data_size, _ud_size, _destroy, _align)
```

相关声明：[NET_BUF_POOL_VAR_ALIGN_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf9d47aed60bc1da8fa40cc8160251ecd)。

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

<a id="r_ga810aba8ba321fd012edc238ea9fe19dc"></a>

```c
#define NET_BUF_POOL_DEFINE(_name, _count, _size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga810aba8ba321fd012edc238ea9fe19dc)。

定义一个新的缓冲池（Buffer Pool）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 7.3\_类型定义（Typedefs）

<a id="r_ga9b74d094a45daf74cd230eaa4fcbc065"></a>

```c
typedef struct net_buf *(* net_buf_allocator_cb) (k_timeout_t timeout, void *user_data)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_allocator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b74d094a45daf74cd230eaa4fcbc065)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

网络缓冲区分配器回调（Network Buffer Allocator Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 7.4\_函数（Functions）

<a id="r_ga040279b601191367dee013bab9916d8d"></a>

```c
static void net_buf_simple_init (struct net_buf_simple *buf, size_t reserve_head)
```

相关声明：[net_buf_simple_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga040279b601191367dee013bab9916d8d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

初始化 net_buf_simple 对象（Object）。

<a id="r_ga7fac47a2a25eaca39c5d14f1f55b485d"></a>

```c
void net_buf_simple_init_with_data (struct net_buf_simple *buf, void *data, size_t size)
```

相关声明：[net_buf_simple_init_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7fac47a2a25eaca39c5d14f1f55b485d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

使用数据初始化 net_buf_simple 对象（Object）。

<a id="r_ga4b537e913e132448cbf56976504ddddd"></a>

```c
static void net_buf_simple_reset (struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4b537e913e132448cbf56976504ddddd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

重置缓冲区（Buffer）。

<a id="r_ga0186c153b72a379affdd3e2e3994b5a7"></a>

```c
void net_buf_simple_clone (const struct net_buf_simple *original, struct net_buf_simple *clone)
```

相关声明：[net_buf_simple_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0186c153b72a379affdd3e2e3994b5a7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

克隆缓冲区状态（Buffer State），共用同一个数据缓冲区。

<a id="r_ga1906e637c848948f5780428a99b3341e"></a>

```c
void * net_buf_simple_add (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1906e637c848948f5780428a99b3341e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为在缓冲区（Buffer）末尾追加数据做准备。

<a id="r_gac37209c1e5097e5610860943fb7d0115"></a>

```c
void * net_buf_simple_add_mem (struct net_buf_simple *buf, const void *mem, size_t len)
```

相关声明：[net_buf_simple_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac37209c1e5097e5610860943fb7d0115)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从内存复制指定字节数的数据到缓冲区（Buffer）末尾。

<a id="r_ga8ff9344b8d8deba1b72b8fca048a525c"></a>

```c
uint8_t * net_buf_simple_add_u8 (struct net_buf_simple *buf, uint8_t val)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ff9344b8d8deba1b72b8fca048a525c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在缓冲区（Buffer）末尾追加一个 8 位字节。

<a id="r_gaa2daf3b20074ff1a23806ce88becebf5"></a>

```c
void net_buf_simple_add_le16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa2daf3b20074ff1a23806ce88becebf5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga910f2b9df58fb0706aa40e3b80f235aa"></a>

```c
void net_buf_simple_add_be16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga910f2b9df58fb0706aa40e3b80f235aa)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_gaf1a89eb15eed79003412ba5a32a35cf6"></a>

```c
void net_buf_simple_add_le24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf1a89eb15eed79003412ba5a32a35cf6)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga5eb09afeff062af577094d2d3f5fdec8"></a>

```c
void net_buf_simple_add_be24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5eb09afeff062af577094d2d3f5fdec8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga3bf1bcff840dddd721f2c49ef0ed7c56"></a>

```c
void net_buf_simple_add_le32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3bf1bcff840dddd721f2c49ef0ed7c56)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_gaac5cd20776d8e7bb4db77cbe5366373c"></a>

```c
void net_buf_simple_add_be32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaac5cd20776d8e7bb4db77cbe5366373c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga67da71ba5942cc11e95aa5ba02cb8552"></a>

```c
void net_buf_simple_add_le40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga67da71ba5942cc11e95aa5ba02cb8552)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga69bdaf4373693bb468cf3876e9edf239"></a>

```c
void net_buf_simple_add_be40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69bdaf4373693bb468cf3876e9edf239)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga5be8c9f33df5b31c15df193a7116ce25"></a>

```c
void net_buf_simple_add_le48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5be8c9f33df5b31c15df193a7116ce25)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_gadb433fb4a1a61702c0615359a4340171"></a>

```c
void net_buf_simple_add_be48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadb433fb4a1a61702c0615359a4340171)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_ga79dc411da328b847dcf1903d71eaf011"></a>

```c
void net_buf_simple_add_le64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga79dc411da328b847dcf1903d71eaf011)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga8e31a7b6537d7634e346236534d2a6d0"></a>

```c
void net_buf_simple_add_be64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8e31a7b6537d7634e346236534d2a6d0)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga8473bdffadc05b22335a321df89f4b83"></a>

```c
void * net_buf_simple_remove_mem (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8473bdffadc05b22335a321df89f4b83)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除数据。

<a id="r_gaf508f74e5e050a7294e8a70bd3725fc3"></a>

```c
uint8_t net_buf_simple_remove_u8 (struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf508f74e5e050a7294e8a70bd3725fc3)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除一个 8 位值。

<a id="r_ga0b57f9ca2f3837e94cd7862e37efc01c"></a>

```c
uint16_t net_buf_simple_remove_le16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0b57f9ca2f3837e94cd7862e37efc01c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga93f9f84845601df4ffc118be1ffd2fee"></a>

```c
uint16_t net_buf_simple_remove_be16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga93f9f84845601df4ffc118be1ffd2fee)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga4e2fef883228f7de41af3cf90648c3c5"></a>

```c
uint32_t net_buf_simple_remove_le24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4e2fef883228f7de41af3cf90648c3c5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga9b39384162a91d7d07e037a9ada782dd"></a>

```c
uint32_t net_buf_simple_remove_be24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b39384162a91d7d07e037a9ada782dd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga9e8d016ce384378142fdec6c8dde2457"></a>

```c
uint32_t net_buf_simple_remove_le32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9e8d016ce384378142fdec6c8dde2457)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_gae8ecc1fbc9dfc007f1b4e932cfaf2f1d"></a>

```c
uint32_t net_buf_simple_remove_be32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_ga2c937164e648fe8b854cb1144051b6b9"></a>

```c
uint64_t net_buf_simple_remove_le40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2c937164e648fe8b854cb1144051b6b9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_ga9abd2bccc90cf654556c18322888d131"></a>

```c
uint64_t net_buf_simple_remove_be40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9abd2bccc90cf654556c18322888d131)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_gac0628bbbe5d9c2b82766d5a17e767696"></a>

```c
uint64_t net_buf_simple_remove_le48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac0628bbbe5d9c2b82766d5a17e767696)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_gab93d22797c3f406179c4c145241d6abb"></a>

```c
uint64_t net_buf_simple_remove_be48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab93d22797c3f406179c4c145241d6abb)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_ga560bd7b181c7f08599ae9241b6ce99fd"></a>

```c
uint64_t net_buf_simple_remove_le64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga560bd7b181c7f08599ae9241b6ce99fd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga602fae83e2ecf47552a11f9282619932"></a>

```c
uint64_t net_buf_simple_remove_be64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602fae83e2ecf47552a11f9282619932)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga64df9754665440370340c6dddde625d1"></a>

```c
void * net_buf_simple_push (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga64df9754665440370340c6dddde625d1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为在缓冲区（Buffer）开头添加数据做准备。

<a id="r_gaaa838083c610f7426c509efaae69a511"></a>

```c
void * net_buf_simple_push_mem (struct net_buf_simple *buf, const void *mem, size_t len)
```

相关声明：[net_buf_simple_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa838083c610f7426c509efaae69a511)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从内存复制指定字节数的数据到缓冲区（Buffer）开头。

<a id="r_ga50cd64438d8f218e3d1ef8b53b7d41a6"></a>

```c
void net_buf_simple_push_le16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga50cd64438d8f218e3d1ef8b53b7d41a6)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga827bd85eba0dbd098790d84d22e8e32d"></a>

```c
void net_buf_simple_push_be16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga827bd85eba0dbd098790d84d22e8e32d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga0f19da70bfc8f597680ee02c21226a77"></a>

```c
void net_buf_simple_push_u8 (struct net_buf_simple *buf, uint8_t val)
```

相关声明：[net_buf_simple_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f19da70bfc8f597680ee02c21226a77)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区（Buffer）开头压入 8 位值。

<a id="r_gabe52d6735d835edc361666bb3413b907"></a>

```c
void net_buf_simple_push_le24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabe52d6735d835edc361666bb3413b907)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_gabfddd4956ec1e356002a3122fea74b72"></a>

```c
void net_buf_simple_push_be24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfddd4956ec1e356002a3122fea74b72)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga8662e6bada476c0d48cebea4661b2ac1"></a>

```c
void net_buf_simple_push_le32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8662e6bada476c0d48cebea4661b2ac1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gad0c3b8fdeaad6437c3dfcbb03fa52426"></a>

```c
void net_buf_simple_push_be32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad0c3b8fdeaad6437c3dfcbb03fa52426)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_ga745ab6f34138b506b42f78e0975a5d2e"></a>

```c
void net_buf_simple_push_le40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga745ab6f34138b506b42f78e0975a5d2e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_gad65bcaf8401e6f5ffff81a998cfb8fe5"></a>

```c
void net_buf_simple_push_be40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad65bcaf8401e6f5ffff81a998cfb8fe5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga66b44897e336f31e3ecbf4717bec274e"></a>

```c
void net_buf_simple_push_le48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga66b44897e336f31e3ecbf4717bec274e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_ga1ea39c7d7e9ba4e10d31d818e45e192a"></a>

```c
void net_buf_simple_push_be48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1ea39c7d7e9ba4e10d31d818e45e192a)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_ga771634e50e2bf7c291565ce6b2af7e85"></a>

```c
void net_buf_simple_push_le64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga771634e50e2bf7c291565ce6b2af7e85)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gafea2201655955ab004b5f77106998ae9"></a>

```c
void net_buf_simple_push_be64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gafea2201655955ab004b5f77106998ae9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gaf5ab4a5fe4a6226be72a510fea0ed8a8"></a>

```c
void * net_buf_simple_pull (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf5ab4a5fe4a6226be72a510fea0ed8a8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga9c676fdbd6e999a9eab26b13d3608e0c"></a>

```c
void * net_buf_simple_pull_mem (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9c676fdbd6e999a9eab26b13d3608e0c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga09a261c615136fd39834cd301fc692e7"></a>

```c
uint8_t net_buf_simple_pull_u8 (struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga09a261c615136fd39834cd301fc692e7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除一个 8 位值。

<a id="r_gad59d180ae81b55f6d618565a37d25dba"></a>

```c
uint16_t net_buf_simple_pull_le16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad59d180ae81b55f6d618565a37d25dba)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_gae36458ba05a4ab89e429be4cfd264440"></a>

```c
uint16_t net_buf_simple_pull_be16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae36458ba05a4ab89e429be4cfd264440)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga4c9d2ac72a176c49ec224353b5566eb9"></a>

```c
uint32_t net_buf_simple_pull_le24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c9d2ac72a176c49ec224353b5566eb9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga4c24d445d6b75c850a9e95fb242a50e1"></a>

```c
uint32_t net_buf_simple_pull_be24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c24d445d6b75c850a9e95fb242a50e1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga38df82e6ba9bc2c75133200f7fa75353"></a>

```c
uint32_t net_buf_simple_pull_le32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga38df82e6ba9bc2c75133200f7fa75353)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga1a53892ed75f994bbbb3a2bcf1743d3c"></a>

```c
uint32_t net_buf_simple_pull_be32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1a53892ed75f994bbbb3a2bcf1743d3c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_gad669c07efe5cb90ebffcc76d9c1029a1"></a>

```c
uint64_t net_buf_simple_pull_le40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad669c07efe5cb90ebffcc76d9c1029a1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_gaa665830dad59ac957f79c7f1cc84aed5"></a>

```c
uint64_t net_buf_simple_pull_be40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa665830dad59ac957f79c7f1cc84aed5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga69fbfbd72b17783c5ee12b4b2ac9af46"></a>

```c
uint64_t net_buf_simple_pull_le48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69fbfbd72b17783c5ee12b4b2ac9af46)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga19bdefe740fe94a42fba76d71b4ef6e2"></a>

```c
uint64_t net_buf_simple_pull_be48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga19bdefe740fe94a42fba76d71b4ef6e2)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga7e0e2d0adbe9062d08f5d8afc7acd89e"></a>

```c
uint64_t net_buf_simple_pull_le64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e0e2d0adbe9062d08f5d8afc7acd89e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gad07f0d49a7db99063077de493e7b0712"></a>

```c
uint64_t net_buf_simple_pull_be64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad07f0d49a7db99063077de493e7b0712)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8"></a>

```c
static uint8_t * net_buf_simple_tail (const struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取缓冲区的尾指针（Tail Pointer）。

<a id="r_gadc6ae86245c2a2607c671a524227b026"></a>

```c
static size_t net_buf_simple_headroom (const struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadc6ae86245c2a2607c671a524227b026)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区的头部预留空间（Headroom）。

<a id="r_ga73e2c42fc23e857a46553084b747c996"></a>

```c
static size_t net_buf_simple_tailroom (const struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区的尾部剩余空间（Tailroom）。

<a id="r_ga7476ec7222d074e7dc9783e7ed9cd800"></a>

```c
static uint16_t net_buf_simple_max_len (const struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7476ec7222d074e7dc9783e7ed9cd800)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查 net_buf_simple::len 的最大值。

<a id="r_ga5c4038cb3aa506c3cad7a2505392aa50"></a>

```c
static bool net_buf_simple_is_valid (const struct net_buf_simple *buf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf_simple_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5c4038cb3aa506c3cad7a2505392aa50)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区（Buffer）的长度与指针是否自洽。

<a id="r_gabf5b098aa0926d9b7fb88baff8a3e2d8"></a>

```c
static void net_buf_simple_save (const struct net_buf_simple *buf, struct net_buf_simple_state *state)
```

相关声明：[net_buf_simple_save](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabf5b098aa0926d9b7fb88baff8a3e2d8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

保存缓冲区的解析状态（Parsing State）。

<a id="r_gaedd36481657a7a9d108659d56e131721"></a>

```c
static void net_buf_simple_restore (struct net_buf_simple *buf, struct net_buf_simple_state *state)
```

相关声明：[net_buf_simple_restore](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedd36481657a7a9d108659d56e131721)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

恢复缓冲区的解析状态（Parsing State）。

<a id="r_ga145f4b2de7548814eaa7ba86fb123989"></a>

```c
struct net_buf_pool * net_buf_pool_get (int id)
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_buf_pool_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga145f4b2de7548814eaa7ba86fb123989)。

根据 ID 查找缓冲池（Pool）。

<a id="r_gacdf048dc0afc7ef67027117e0d51d3a3"></a>

```c
int net_buf_id (const struct net_buf *buf)
```

相关声明：[net_buf_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacdf048dc0afc7ef67027117e0d51d3a3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区从零开始的索引（Zero-based Index）。

<a id="r_ga9cd6d30ea47a91647d3c4a60d82b5cd4"></a>

```c
static size_t net_buf_get_available (struct net_buf_pool *pool)
```

相关声明：[net_buf_get_available](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9cd6d30ea47a91647d3c4a60d82b5cd4)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取当前可从缓冲池（Pool）申领的缓冲区数量。

<a id="r_gad652ef7d2895f8077c366a564b785291"></a>

```c
static size_t net_buf_get_max_used (struct net_buf_pool *pool)
```

相关声明：[net_buf_get_max_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad652ef7d2895f8077c366a564b785291)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取从缓冲池（Pool）同时申领的缓冲区数量峰值。

<a id="r_ga686df794ec6881625b54454a33587bab"></a>

```c
struct net_buf * net_buf_alloc_fixed (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga686df794ec6881625b54454a33587bab)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新的固定大小缓冲区（Fixed Buffer）。

<a id="r_ga534366f3b5c7f41a28372c12149ca005"></a>

```c
static struct net_buf * net_buf_alloc (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga534366f3b5c7f41a28372c12149ca005)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

<a id="r_ga11d489aedcca82117965fa6ba9d11ca5"></a>

```c
struct net_buf * net_buf_alloc_len (struct net_buf_pool *pool, size_t size, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga11d489aedcca82117965fa6ba9d11ca5)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新的变长缓冲区（Variable Length Buffer）。

<a id="r_ga8c24d0761d6d38facb6cca60c7c13c0c"></a>

```c
struct net_buf * net_buf_alloc_with_data (struct net_buf_pool *pool, void *data, size_t size, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8c24d0761d6d38facb6cca60c7c13c0c)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新缓冲区，使用外部数据指针（External Data Pointer）。

<a id="r_ga739249547eb37b839b3c1ebdbcb88d28"></a>

```c
static void net_buf_destroy (struct net_buf *buf)
```

相关声明：[net_buf_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga739249547eb37b839b3c1ebdbcb88d28)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从自定义销毁回调（Custom Destroy Callback）中销毁缓冲区。

<a id="r_ga1292f38b096fd80e31889aff44b0c021"></a>

```c
void net_buf_reset (struct net_buf *buf)
```

相关声明：[net_buf_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1292f38b096fd80e31889aff44b0c021)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

重置缓冲区（Buffer）。

<a id="r_ga0e5d3d938becfefc4f4b4d083cb467aa"></a>

```c
void net_buf_simple_reserve (struct net_buf_simple *buf, size_t reserve)
```

相关声明：[net_buf_simple_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0e5d3d938becfefc4f4b4d083cb467aa)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

使用给定的头部预留空间（Headroom）初始化缓冲区。

<a id="r_ga6d2dfc45e1e5acf21fe08359a4f92a18"></a>

```c
void net_buf_slist_put (sys_slist_t *list, struct net_buf *buf)
```

相关声明：[net_buf_slist_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6d2dfc45e1e5acf21fe08359a4f92a18)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将缓冲区（Buffer）放入列表（List）。

<a id="r_ga218d4a0c160c57a44946154478724cb3"></a>

```c
struct net_buf * net_buf_slist_get (sys_slist_t *list)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_slist_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga218d4a0c160c57a44946154478724cb3)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)。

从列表（List）获取缓冲区（Buffer）。

<a id="r_gabedcb728bc2fc0c2b5319a8fd87e8273"></a>

```c
void net_buf_unref (struct net_buf *buf)
```

相关声明：[net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

递减缓冲区的引用计数（Reference Count）。

<a id="r_ga29387b2a672bf2bb8739046a46f3601f"></a>

```c
struct net_buf * net_buf_ref (struct net_buf *buf)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

递增缓冲区的引用计数（Reference Count）。

<a id="r_ga4ff24d6ae1aff46e17647ef91db593ca"></a>

```c
static struct net_buf * net_buf_take (struct net_buf **orig)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_take](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4ff24d6ae1aff46e17647ef91db593ca)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

移动缓冲区指针（Buffer Pointer），将 orig 设置为 NULL。

<a id="r_ga6b43ad0740b23c0544d706c77c9f1e13"></a>

```c
static void net_buf_drop (struct net_buf **orig)
```

相关声明：[net_buf_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6b43ad0740b23c0544d706c77c9f1e13)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放缓冲区引用（Buffer Reference），并清空指针。

<a id="r_gaf4d80e2878e3c790fff206bec820f03f"></a>

```c
struct net_buf * net_buf_clone (struct net_buf *buf, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf4d80e2878e3c790fff206bec820f03f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆缓冲区（Clone Buffer）。

<a id="r_gaf2df457abe3e56d47107b76bdc004756"></a>

```c
static void * net_buf_user_data (const struct net_buf *buf)
```

相关声明：[net_buf_user_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf2df457abe3e56d47107b76bdc004756)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取指向缓冲区用户数据（User Data）的指针。

<a id="r_ga4d1dd56ca8d32d3cfda114fd36761d0d"></a>

```c
int net_buf_user_data_copy (struct net_buf *dst, const struct net_buf *src)
```

相关声明：[net_buf_user_data_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4d1dd56ca8d32d3cfda114fd36761d0d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将用户数据（User Data）从一个缓冲区复制到另一个缓冲区。

<a id="r_ga8ac58ad4f73b498bef2ff3ac7e30c6c3"></a>

```c
static void net_buf_reserve (struct net_buf *buf, size_t reserve)
```

相关声明：[net_buf_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

使用给定的头部预留空间（Headroom）初始化缓冲区。

<a id="r_ga30776d2b21f06d244c083af5c25b0f3e"></a>

```c
static void * net_buf_add (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga30776d2b21f06d244c083af5c25b0f3e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

为在缓冲区（Buffer）末尾追加数据做准备。

<a id="r_gacf4e2eba52975ba6728c79274a769d0f"></a>

```c
static void * net_buf_add_mem (struct net_buf *buf, const void *mem, size_t len)
```

相关声明：[net_buf_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacf4e2eba52975ba6728c79274a769d0f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将指定字节数的数据复制到缓冲区（Buffer）末尾。

<a id="r_ga868ac2bea103fed568b461cbcd45eda2"></a>

```c
static uint8_t * net_buf_add_u8 (struct net_buf *buf, uint8_t val)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga868ac2bea103fed568b461cbcd45eda2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在缓冲区（Buffer）末尾追加一个 8 位字节。

<a id="r_gadd6d01a3b1efd0de16f9bef975809404"></a>

```c
static void net_buf_add_le16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadd6d01a3b1efd0de16f9bef975809404)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga61878a9bd7462ca925eac39181f2972c"></a>

```c
static void net_buf_add_be16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga61878a9bd7462ca925eac39181f2972c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga32b90364091ade229830686f03b25d4c"></a>

```c
static void net_buf_add_le24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga32b90364091ade229830686f03b25d4c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga0f3cd9f9b364a2d2125aea19221d3e1e"></a>

```c
static void net_buf_add_be24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f3cd9f9b364a2d2125aea19221d3e1e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_gae8ba33b6592ef7fd859b35d63b285d87"></a>

```c
static void net_buf_add_le32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ba33b6592ef7fd859b35d63b285d87)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga5543d00c96f83970f8dbf3670a9dc3fc"></a>

```c
static void net_buf_add_be32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5543d00c96f83970f8dbf3670a9dc3fc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga62790f9644102f4952c250f6513a2ada"></a>

```c
static void net_buf_add_le40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga62790f9644102f4952c250f6513a2ada)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga70cb98da91de098a92fbd69712c2bde7"></a>

```c
static void net_buf_add_be40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga70cb98da91de098a92fbd69712c2bde7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_gaf19bf75c3d4d645b1eebf9254aa22790"></a>

```c
static void net_buf_add_le48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf19bf75c3d4d645b1eebf9254aa22790)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_ga8fe6feb191ab338e91bd62f44e184deb"></a>

```c
static void net_buf_add_be48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8fe6feb191ab338e91bd62f44e184deb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_gac3f955f8fecc0e5971d2e5e8176e973e"></a>

```c
static void net_buf_add_le64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac3f955f8fecc0e5971d2e5e8176e973e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga055f6eb7d5fbc9a3cf529a9ed00970c4"></a>

```c
static void net_buf_add_be64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga055f6eb7d5fbc9a3cf529a9ed00970c4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_gace5ad98eac4772db3b0fa2181912f1f0"></a>

```c
static void * net_buf_remove_mem (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gace5ad98eac4772db3b0fa2181912f1f0)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除数据。

<a id="r_gad954b9f37790d5e7087db7db7bdedd41"></a>

```c
static uint8_t net_buf_remove_u8 (struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad954b9f37790d5e7087db7db7bdedd41)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除一个 8 位值。

<a id="r_gaaf654110fb6a8bdfc27433945d4d1308"></a>

```c
static uint16_t net_buf_remove_le16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaf654110fb6a8bdfc27433945d4d1308)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga5da86c8ea703ab3f01c408cce73b0651"></a>

```c
static uint16_t net_buf_remove_be16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5da86c8ea703ab3f01c408cce73b0651)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga6f346a9af570528d238592851240fd74"></a>

```c
static uint32_t net_buf_remove_be24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6f346a9af570528d238592851240fd74)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga903f59c8dea1b2c54969b567fe315041"></a>

```c
static uint32_t net_buf_remove_le24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga903f59c8dea1b2c54969b567fe315041)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_gae9321a469cc751c58cfb532afd57d265"></a>

```c
static uint32_t net_buf_remove_le32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae9321a469cc751c58cfb532afd57d265)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_gacce707d646d7008ec3167af1a0b20da8"></a>

```c
static uint32_t net_buf_remove_be32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacce707d646d7008ec3167af1a0b20da8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_ga57150a1ba09b28e5c3b04bdefce7ed8e"></a>

```c
static uint64_t net_buf_remove_le40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga57150a1ba09b28e5c3b04bdefce7ed8e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_gae2920eab3c56d0d462811b83961df466"></a>

```c
static uint64_t net_buf_remove_be40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae2920eab3c56d0d462811b83961df466)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_ga0c147d9f95e2224696a8ace26f63a300"></a>

```c
static uint64_t net_buf_remove_le48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0c147d9f95e2224696a8ace26f63a300)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_gaab0e3bcc21c958c01ef076cd0efe087c"></a>

```c
static uint64_t net_buf_remove_be48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaab0e3bcc21c958c01ef076cd0efe087c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_ga447b9c6be3fe04a50eb35dd29f190b6d"></a>

```c
static uint64_t net_buf_remove_le64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga447b9c6be3fe04a50eb35dd29f190b6d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga8b9edd213da2d48dfb8d70a8d307ba13"></a>

```c
static uint64_t net_buf_remove_be64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8b9edd213da2d48dfb8d70a8d307ba13)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga96a2b1f07f3a7958057d9c7cc1f01b73"></a>

```c
static void * net_buf_push (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga96a2b1f07f3a7958057d9c7cc1f01b73)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

为在缓冲区（Buffer）起始位置添加数据做准备。

<a id="r_ga7e9daccec8cae1b9bfda52b0758adf0c"></a>

```c
static void * net_buf_push_mem (struct net_buf *buf, const void *mem, size_t len)
```

相关声明：[net_buf_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e9daccec8cae1b9bfda52b0758adf0c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将指定字节数的数据复制到缓冲区（Buffer）起始位置。

<a id="r_ga9093202ba0a22bfa519bbe32d4585186"></a>

```c
static void net_buf_push_u8 (struct net_buf *buf, uint8_t val)
```

相关声明：[net_buf_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9093202ba0a22bfa519bbe32d4585186)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区（Buffer）开头压入 8 位值。

<a id="r_gab6c84c6846c06c2b339bc88df35e2655"></a>

```c
static void net_buf_push_le16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab6c84c6846c06c2b339bc88df35e2655)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga6dd756ff8332d076f5d37c69e6c534b5"></a>

```c
static void net_buf_push_be16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6dd756ff8332d076f5d37c69e6c534b5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga87524ac50e53ba59c6692af10cf001b9"></a>

```c
static void net_buf_push_le24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87524ac50e53ba59c6692af10cf001b9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga87338399d8ecd64a894908ed4a2f710b"></a>

```c
static void net_buf_push_be24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87338399d8ecd64a894908ed4a2f710b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga97c9046185d6a1e9235bf6914c72dfc4"></a>

```c
static void net_buf_push_le32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97c9046185d6a1e9235bf6914c72dfc4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gae4e64a23708ed910fb6c3ab8ba481a4c"></a>

```c
static void net_buf_push_be32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae4e64a23708ed910fb6c3ab8ba481a4c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gaefab4a755cf4fb7d2b4a142a9351c189"></a>

```c
static void net_buf_push_le40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaefab4a755cf4fb7d2b4a142a9351c189)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga512f84e686ff70a5589557575ccda1f8"></a>

```c
static void net_buf_push_be40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga512f84e686ff70a5589557575ccda1f8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga852654f7e59951bf3536e3f4e98761bf"></a>

```c
static void net_buf_push_le48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga852654f7e59951bf3536e3f4e98761bf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_gabfbcb051019ff210cc2b85adcf4bc821"></a>

```c
static void net_buf_push_be48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfbcb051019ff210cc2b85adcf4bc821)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_gad4ee42b023881f80211fbeca53a0f25d"></a>

```c
static void net_buf_push_le64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad4ee42b023881f80211fbeca53a0f25d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_ga43ff5faab0b099a355b9b96b7b0e3d8c"></a>

```c
static void net_buf_push_be64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga43ff5faab0b099a355b9b96b7b0e3d8c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gaef433d92734dd8691c292abdb823ba0e"></a>

```c
static void * net_buf_pull (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef433d92734dd8691c292abdb823ba0e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_gaedc5ffe19bb0ec438e633023c3c5de74"></a>

```c
static void * net_buf_pull_mem (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedc5ffe19bb0ec438e633023c3c5de74)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga71bb306d2ce459a60a8c3fc6dac54c90"></a>

```c
static uint8_t net_buf_pull_u8 (struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga71bb306d2ce459a60a8c3fc6dac54c90)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除一个 8 位值。

<a id="r_gaed64e9f2b969f2c0d99cd281e73c860a"></a>

```c
static uint16_t net_buf_pull_le16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaed64e9f2b969f2c0d99cd281e73c860a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga97909a33c374a5c757fd2faf582139b7"></a>

```c
static uint16_t net_buf_pull_be16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97909a33c374a5c757fd2faf582139b7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga85c505321484a50ed9422f24934ed077"></a>

```c
static uint32_t net_buf_pull_le24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga85c505321484a50ed9422f24934ed077)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga8de937e8775879712ea0acbf60327a95"></a>

```c
static uint32_t net_buf_pull_be24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8de937e8775879712ea0acbf60327a95)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga5f051078f1ffcc40e9ad40e7545a084f"></a>

```c
static uint32_t net_buf_pull_le32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f051078f1ffcc40e9ad40e7545a084f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga5f8f2e2244eb574b3e57d09d85412967"></a>

```c
static uint32_t net_buf_pull_be32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f8f2e2244eb574b3e57d09d85412967)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga36b27c6373eb245f777164065386d100"></a>

```c
static uint64_t net_buf_pull_le40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga36b27c6373eb245f777164065386d100)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga050bdaccaec842482a02b096aa0c999f"></a>

```c
static uint64_t net_buf_pull_be40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga050bdaccaec842482a02b096aa0c999f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga7eeee45b6639146d1492f92263ee4f51"></a>

```c
static uint64_t net_buf_pull_le48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7eeee45b6639146d1492f92263ee4f51)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga68934e105c4b3a8e27aa61b3ec5526db"></a>

```c
static uint64_t net_buf_pull_be48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga68934e105c4b3a8e27aa61b3ec5526db)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga9a3df35e2287cbcfe1b60e2efa52c64e"></a>

```c
static uint64_t net_buf_pull_le64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9a3df35e2287cbcfe1b60e2efa52c64e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_ga3c1e80741a49691e69e57c891d3edb05"></a>

```c
static uint64_t net_buf_pull_be64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3c1e80741a49691e69e57c891d3edb05)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gaecbc6adf16469e3366c88445ea7a553a"></a>

```c
static size_t net_buf_tailroom (const struct net_buf *buf)
```

相关声明：[net_buf_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区的尾部剩余空间（Tailroom）。

<a id="r_gac9a09897f44e708f920064826aa2f703"></a>

```c
static size_t net_buf_headroom (const struct net_buf *buf)
```

相关声明：[net_buf_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac9a09897f44e708f920064826aa2f703)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区的头部预留空间（Headroom）。

<a id="r_ga65924b8234c91dfc09069ba06242a6b7"></a>

```c
static uint16_t net_buf_max_len (const struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga65924b8234c91dfc09069ba06242a6b7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查 net_buf::len 的最大值。

<a id="r_ga8d258ef1e4241c438a726486bc7fe766"></a>

```c
static bool net_buf_is_valid (const struct net_buf *buf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8d258ef1e4241c438a726486bc7fe766)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区（Buffer）的长度与指针是否自洽。

<a id="r_gaedb10a84b352a3d7716bef979af2ab31"></a>

```c
static uint8_t * net_buf_tail (const struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedb10a84b352a3d7716bef979af2ab31)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区的尾指针（Tail Pointer）。

<a id="r_ga042ce3f2e7e3fd0948ca2623fff36746"></a>

```c
struct net_buf * net_buf_frag_last (struct net_buf *frags)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_last](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga042ce3f2e7e3fd0948ca2623fff36746)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在分片列表（Fragment List）中查找最后一个分片。

<a id="r_gac032b44db4a845dba8303fecfe1b63e7"></a>

```c
void net_buf_frag_insert (struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf_frag_insert](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac032b44db4a845dba8303fecfe1b63e7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向缓冲区链（Chain of Buffers）插入新分片（Fragment）。

<a id="r_ga0d7e310802a2bc7b2078f9310827535f"></a>

```c
struct net_buf * net_buf_frag_add (struct net_buf *head, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0d7e310802a2bc7b2078f9310827535f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将新分片（Fragment）追加到缓冲区链（Chain of Buffers）末尾。

<a id="r_ga602a99833bd401a0ada5bd5defa7a2ff"></a>

```c
struct net_buf * net_buf_frag_del (struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_del](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602a99833bd401a0ada5bd5defa7a2ff)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区链（Chain of Buffers）中删除现有分片（Fragment）。

<a id="r_gaffd49f2de8e72d5f7585b4e5167923d8"></a>

```c
size_t net_buf_linearize (void *dst, size_t dst_len, const struct net_buf *src, size_t offset, size_t len)
```

相关声明：[net_buf_linearize](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaffd49f2de8e72d5f7585b4e5167923d8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 net_buf 链的指定偏移量（Offset）开始，将字节复制到线性缓冲区（Linear Buffer）。

<a id="r_ga646d680491753b3ed29fa83c26732d1a"></a>

```c
size_t net_buf_append_bytes (struct net_buf *buf, size_t len, const void *value, k_timeout_t timeout, net_buf_allocator_cb allocate_cb, void *user_data)
```

相关声明：[net_buf_append_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga646d680491753b3ed29fa83c26732d1a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[net_buf_allocator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b74d094a45daf74cd230eaa4fcbc065)。

向 net_buf 列表追加数据（Append Data）。

<a id="r_gaef938c3ab676a5bd5bf8338b8d7cb30c"></a>

```c
size_t net_buf_data_match (const struct net_buf *buf, size_t offset, const void *data, size_t len)
```

相关声明：[net_buf_data_match](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef938c3ab676a5bd5bf8338b8d7cb30c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将数据与 net_buf 的内容进行匹配（Match）。

<a id="r_ga2d7096280d4fa6f5e32c4674d542889b"></a>

```c
static struct net_buf * net_buf_skip (struct net_buf *buf, size_t len)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2d7096280d4fa6f5e32c4674d542889b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

跳过 net_buf 中的 N 个字节（Skip）。

<a id="r_gaebb95f08dbd4d38a250170aa78ddeb44"></a>

```c
static size_t net_buf_frags_len (const struct net_buf *buf)
```

相关声明：[net_buf_frags_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaebb95f08dbd4d38a250170aa78ddeb44)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

计算分片（Fragment）中存储的字节数。


## 7.5\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [查看此文件的源码。](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [NET_BUF_SIMPLE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf85aa0b705bb4fbe2630191fde802501)
- [NET_BUF_SIMPLE_DEFINE_STATIC](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga21ced8b3082d57bf071008de5fffc0f4)
- [NET_BUF_SIMPLE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0b01dc80027d13b1895379d4d1397207)
- [NET_BUF_EXTERNAL_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaeacbdf3cfda12691c75253015e5c19a)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [NET_BUF_POOL_HEAP_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga61671ac866081d31dfe9eddbf3b6f210)
- [NET_BUF_POOL_FIXED_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacc53824e01db7935bcc9cad564b716cd)
- [NET_BUF_POOL_VAR_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga90e691e793c964847d737f5ecf7646ec)
- [NET_BUF_POOL_VAR_ALIGN_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf9d47aed60bc1da8fa40cc8160251ecd)
- [NET_BUF_POOL_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga810aba8ba321fd012edc238ea9fe19dc)
- [net_buf_allocator_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b74d094a45daf74cd230eaa4fcbc065)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_buf_simple_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga040279b601191367dee013bab9916d8d)
- [net_buf_simple_init_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7fac47a2a25eaca39c5d14f1f55b485d)
- [net_buf_simple_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4b537e913e132448cbf56976504ddddd)
- [net_buf_simple_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0186c153b72a379affdd3e2e3994b5a7)
- [net_buf_simple_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1906e637c848948f5780428a99b3341e)
- [net_buf_simple_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac37209c1e5097e5610860943fb7d0115)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [net_buf_simple_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ff9344b8d8deba1b72b8fca048a525c)
- [net_buf_simple_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa2daf3b20074ff1a23806ce88becebf5)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga910f2b9df58fb0706aa40e3b80f235aa)
- [net_buf_simple_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf1a89eb15eed79003412ba5a32a35cf6)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [net_buf_simple_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5eb09afeff062af577094d2d3f5fdec8)
- [net_buf_simple_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3bf1bcff840dddd721f2c49ef0ed7c56)
- [net_buf_simple_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaac5cd20776d8e7bb4db77cbe5366373c)
- [net_buf_simple_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga67da71ba5942cc11e95aa5ba02cb8552)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_buf_simple_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69bdaf4373693bb468cf3876e9edf239)
- [net_buf_simple_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5be8c9f33df5b31c15df193a7116ce25)
- [net_buf_simple_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadb433fb4a1a61702c0615359a4340171)
- [net_buf_simple_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga79dc411da328b847dcf1903d71eaf011)
- [net_buf_simple_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8e31a7b6537d7634e346236534d2a6d0)
- [net_buf_simple_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8473bdffadc05b22335a321df89f4b83)
- [net_buf_simple_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf508f74e5e050a7294e8a70bd3725fc3)
- [net_buf_simple_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0b57f9ca2f3837e94cd7862e37efc01c)
- [net_buf_simple_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga93f9f84845601df4ffc118be1ffd2fee)
- [net_buf_simple_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4e2fef883228f7de41af3cf90648c3c5)
- [net_buf_simple_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9b39384162a91d7d07e037a9ada782dd)
- [net_buf_simple_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9e8d016ce384378142fdec6c8dde2457)
- [net_buf_simple_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)
- [net_buf_simple_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2c937164e648fe8b854cb1144051b6b9)
- [net_buf_simple_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9abd2bccc90cf654556c18322888d131)
- [net_buf_simple_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac0628bbbe5d9c2b82766d5a17e767696)
- [net_buf_simple_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab93d22797c3f406179c4c145241d6abb)
- [net_buf_simple_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga560bd7b181c7f08599ae9241b6ce99fd)
- [net_buf_simple_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602fae83e2ecf47552a11f9282619932)
- [net_buf_simple_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga64df9754665440370340c6dddde625d1)
- [net_buf_simple_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa838083c610f7426c509efaae69a511)
- [net_buf_simple_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga50cd64438d8f218e3d1ef8b53b7d41a6)
- [net_buf_simple_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga827bd85eba0dbd098790d84d22e8e32d)
- [net_buf_simple_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f19da70bfc8f597680ee02c21226a77)
- [net_buf_simple_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabe52d6735d835edc361666bb3413b907)
- [net_buf_simple_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfddd4956ec1e356002a3122fea74b72)
- [net_buf_simple_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8662e6bada476c0d48cebea4661b2ac1)
- [net_buf_simple_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad0c3b8fdeaad6437c3dfcbb03fa52426)
- [net_buf_simple_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga745ab6f34138b506b42f78e0975a5d2e)
- [net_buf_simple_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad65bcaf8401e6f5ffff81a998cfb8fe5)
- [net_buf_simple_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga66b44897e336f31e3ecbf4717bec274e)
- [net_buf_simple_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1ea39c7d7e9ba4e10d31d818e45e192a)
- [net_buf_simple_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga771634e50e2bf7c291565ce6b2af7e85)
- [net_buf_simple_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gafea2201655955ab004b5f77106998ae9)
- [net_buf_simple_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf5ab4a5fe4a6226be72a510fea0ed8a8)
- [net_buf_simple_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9c676fdbd6e999a9eab26b13d3608e0c)
- [net_buf_simple_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga09a261c615136fd39834cd301fc692e7)
- [net_buf_simple_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad59d180ae81b55f6d618565a37d25dba)
- [net_buf_simple_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae36458ba05a4ab89e429be4cfd264440)
- [net_buf_simple_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c9d2ac72a176c49ec224353b5566eb9)
- [net_buf_simple_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4c24d445d6b75c850a9e95fb242a50e1)
- [net_buf_simple_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga38df82e6ba9bc2c75133200f7fa75353)
- [net_buf_simple_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1a53892ed75f994bbbb3a2bcf1743d3c)
- [net_buf_simple_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad669c07efe5cb90ebffcc76d9c1029a1)
- [net_buf_simple_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaa665830dad59ac957f79c7f1cc84aed5)
- [net_buf_simple_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga69fbfbd72b17783c5ee12b4b2ac9af46)
- [net_buf_simple_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga19bdefe740fe94a42fba76d71b4ef6e2)
- [net_buf_simple_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e0e2d0adbe9062d08f5d8afc7acd89e)
- [net_buf_simple_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad07f0d49a7db99063077de493e7b0712)
- [net_buf_simple_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)
- [net_buf_simple_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadc6ae86245c2a2607c671a524227b026)
- [net_buf_simple_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga73e2c42fc23e857a46553084b747c996)
- [net_buf_simple_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7476ec7222d074e7dc9783e7ed9cd800)
- [net_buf_simple::len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_buf_simple_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5c4038cb3aa506c3cad7a2505392aa50)
- [net_buf_simple_save](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabf5b098aa0926d9b7fb88baff8a3e2d8)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [net_buf_simple_restore](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedd36481657a7a9d108659d56e131721)
- [net_buf_pool_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga145f4b2de7548814eaa7ba86fb123989)
- [net_buf_id](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacdf048dc0afc7ef67027117e0d51d3a3)
- [net_buf_get_available](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9cd6d30ea47a91647d3c4a60d82b5cd4)
- [net_buf_get_max_used](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad652ef7d2895f8077c366a564b785291)
- [net_buf_alloc_fixed](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga686df794ec6881625b54454a33587bab)
- [net_buf_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga534366f3b5c7f41a28372c12149ca005)
- [net_buf_alloc_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga11d489aedcca82117965fa6ba9d11ca5)
- [net_buf_alloc_with_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8c24d0761d6d38facb6cca60c7c13c0c)
- [net_buf_destroy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga739249547eb37b839b3c1ebdbcb88d28)
- [net_buf_reset](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga1292f38b096fd80e31889aff44b0c021)
- [net_buf_simple_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0e5d3d938becfefc4f4b4d083cb467aa)
- [net_buf_slist_put](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6d2dfc45e1e5acf21fe08359a4f92a18)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [net_buf_slist_get](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga218d4a0c160c57a44946154478724cb3)
- [net_buf_unref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabedcb728bc2fc0c2b5319a8fd87e8273)
- [net_buf_ref](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga29387b2a672bf2bb8739046a46f3601f)
- [net_buf_take](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4ff24d6ae1aff46e17647ef91db593ca)
- [net_buf_drop](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6b43ad0740b23c0544d706c77c9f1e13)
- [net_buf_clone](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf4d80e2878e3c790fff206bec820f03f)
- [net_buf_user_data](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf2df457abe3e56d47107b76bdc004756)
- [net_buf_user_data_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga4d1dd56ca8d32d3cfda114fd36761d0d)
- [net_buf_reserve](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)
- [net_buf_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga30776d2b21f06d244c083af5c25b0f3e)
- [net_buf_add_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacf4e2eba52975ba6728c79274a769d0f)
- [net_buf_add_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga868ac2bea103fed568b461cbcd45eda2)
- [net_buf_add_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gadd6d01a3b1efd0de16f9bef975809404)
- [net_buf_add_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga61878a9bd7462ca925eac39181f2972c)
- [net_buf_add_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga32b90364091ade229830686f03b25d4c)
- [net_buf_add_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0f3cd9f9b364a2d2125aea19221d3e1e)
- [net_buf_add_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae8ba33b6592ef7fd859b35d63b285d87)
- [net_buf_add_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5543d00c96f83970f8dbf3670a9dc3fc)
- [net_buf_add_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga62790f9644102f4952c250f6513a2ada)
- [net_buf_add_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga70cb98da91de098a92fbd69712c2bde7)
- [net_buf_add_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaf19bf75c3d4d645b1eebf9254aa22790)
- [net_buf_add_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8fe6feb191ab338e91bd62f44e184deb)
- [net_buf_add_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac3f955f8fecc0e5971d2e5e8176e973e)
- [net_buf_add_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga055f6eb7d5fbc9a3cf529a9ed00970c4)
- [net_buf_remove_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gace5ad98eac4772db3b0fa2181912f1f0)
- [net_buf_remove_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad954b9f37790d5e7087db7db7bdedd41)
- [net_buf_remove_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaaf654110fb6a8bdfc27433945d4d1308)
- [net_buf_remove_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5da86c8ea703ab3f01c408cce73b0651)
- [net_buf_remove_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6f346a9af570528d238592851240fd74)
- [net_buf_remove_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga903f59c8dea1b2c54969b567fe315041)
- [net_buf_remove_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae9321a469cc751c58cfb532afd57d265)
- [net_buf_remove_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gacce707d646d7008ec3167af1a0b20da8)
- [net_buf_remove_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga57150a1ba09b28e5c3b04bdefce7ed8e)
- [net_buf_remove_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae2920eab3c56d0d462811b83961df466)
- [net_buf_remove_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0c147d9f95e2224696a8ace26f63a300)
- [net_buf_remove_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaab0e3bcc21c958c01ef076cd0efe087c)
- [net_buf_remove_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga447b9c6be3fe04a50eb35dd29f190b6d)
- [net_buf_remove_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8b9edd213da2d48dfb8d70a8d307ba13)
- [net_buf_push](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga96a2b1f07f3a7958057d9c7cc1f01b73)
- [net_buf_push_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7e9daccec8cae1b9bfda52b0758adf0c)
- [net_buf_push_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9093202ba0a22bfa519bbe32d4585186)
- [net_buf_push_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gab6c84c6846c06c2b339bc88df35e2655)
- [net_buf_push_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga6dd756ff8332d076f5d37c69e6c534b5)
- [net_buf_push_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87524ac50e53ba59c6692af10cf001b9)
- [net_buf_push_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga87338399d8ecd64a894908ed4a2f710b)
- [net_buf_push_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97c9046185d6a1e9235bf6914c72dfc4)
- [net_buf_push_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gae4e64a23708ed910fb6c3ab8ba481a4c)
- [net_buf_push_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaefab4a755cf4fb7d2b4a142a9351c189)
- [net_buf_push_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga512f84e686ff70a5589557575ccda1f8)
- [net_buf_push_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga852654f7e59951bf3536e3f4e98761bf)
- [net_buf_push_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gabfbcb051019ff210cc2b85adcf4bc821)
- [net_buf_push_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gad4ee42b023881f80211fbeca53a0f25d)
- [net_buf_push_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga43ff5faab0b099a355b9b96b7b0e3d8c)
- [net_buf_pull](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef433d92734dd8691c292abdb823ba0e)
- [net_buf_pull_mem](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedc5ffe19bb0ec438e633023c3c5de74)
- [net_buf_pull_u8](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga71bb306d2ce459a60a8c3fc6dac54c90)
- [net_buf_pull_le16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaed64e9f2b969f2c0d99cd281e73c860a)
- [net_buf_pull_be16](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga97909a33c374a5c757fd2faf582139b7)
- [net_buf_pull_le24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga85c505321484a50ed9422f24934ed077)
- [net_buf_pull_be24](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8de937e8775879712ea0acbf60327a95)
- [net_buf_pull_le32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f051078f1ffcc40e9ad40e7545a084f)
- [net_buf_pull_be32](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga5f8f2e2244eb574b3e57d09d85412967)
- [net_buf_pull_le40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga36b27c6373eb245f777164065386d100)
- [net_buf_pull_be40](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga050bdaccaec842482a02b096aa0c999f)
- [net_buf_pull_le48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga7eeee45b6639146d1492f92263ee4f51)
- [net_buf_pull_be48](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga68934e105c4b3a8e27aa61b3ec5526db)
- [net_buf_pull_le64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga9a3df35e2287cbcfe1b60e2efa52c64e)
- [net_buf_pull_be64](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga3c1e80741a49691e69e57c891d3edb05)
- [net_buf_tailroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaecbc6adf16469e3366c88445ea7a553a)
- [net_buf_headroom](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac9a09897f44e708f920064826aa2f703)
- [net_buf_max_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga65924b8234c91dfc09069ba06242a6b7)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [net_buf_is_valid](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga8d258ef1e4241c438a726486bc7fe766)
- [net_buf_tail](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaedb10a84b352a3d7716bef979af2ab31)
- [net_buf_frag_last](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga042ce3f2e7e3fd0948ca2623fff36746)
- [net_buf_frag_insert](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gac032b44db4a845dba8303fecfe1b63e7)
- [net_buf_frag_add](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga0d7e310802a2bc7b2078f9310827535f)
- [net_buf_frag_del](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga602a99833bd401a0ada5bd5defa7a2ff)
- [net_buf_linearize](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaffd49f2de8e72d5f7585b4e5167923d8)
- [net_buf_append_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga646d680491753b3ed29fa83c26732d1a)
- [net_buf_data_match](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaef938c3ab676a5bd5bf8338b8d7cb30c)
- [net_buf_skip](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga2d7096280d4fa6f5e32c4674d542889b)
- [net_buf_frags_len](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#gaebb95f08dbd4d38a250170aa78ddeb44)

<a id="header-details"></a>

---

[上一章](P006_zephyr__net__mdio.h_文件参考.md) · [返回大纲](大纲.md)
