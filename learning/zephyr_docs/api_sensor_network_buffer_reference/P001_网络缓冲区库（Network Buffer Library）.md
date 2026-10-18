---
id: learning.zephyr-docs.api-sensor-network-buffer-reference.page-1
title: 网络缓冲区库（Network Buffer Library）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_网络缓冲区库（Network Buffer Library）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络缓冲区库（Network buffer library）

<a id="details"></a>

网络缓冲区库（Network Buffer Library）。引入版本（Since）：1.0。接口版本（Version）：1.1.0。添加（Add）、前压（Push）、前取（Pull）或移除（Remove）数据的函数，通过断言检查操作是否处于缓冲区容量内。启用 `CONFIG_NET_BUF_HARDENING` 后，始终执行此检查，并检查缓冲区长度与指针是否一致。检查失败时，操作保持缓冲区不变：返回指针的函数返回 `NULL`，返回数值的函数返回 `0`，没有返回值的函数不执行写入。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

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

## 1.2\_宏定义（Macros）

<a id="r_gaf85aa0b705bb4fbe2630191fde802501"></a>

```c
#define NET_BUF_SIMPLE_DEFINE(_name, _size)
```

相关声明：[NET_BUF_SIMPLE_DEFINE](#gaf85aa0b705bb4fbe2630191fde802501)。

定义一个位于栈上的 net_buf_simple 变量（Stack Variable）。

<a id="r_ga21ced8b3082d57bf071008de5fffc0f4"></a>

```c
#define NET_BUF_SIMPLE_DEFINE_STATIC(_name, _size)
```

相关声明：[NET_BUF_SIMPLE_DEFINE_STATIC](#ga21ced8b3082d57bf071008de5fffc0f4)。

定义一个静态 net_buf_simple 变量（Static Variable）。

<a id="r_ga0b01dc80027d13b1895379d4d1397207"></a>

```c
#define NET_BUF_SIMPLE(_size)
```

相关声明：[NET_BUF_SIMPLE](#ga0b01dc80027d13b1895379d4d1397207)。

定义一个位于栈上的 net_buf_simple 变量（Stack Variable），并获取指向它的指针。

<a id="r_gaaeacbdf3cfda12691c75253015e5c19a"></a>

```c
#define NET_BUF_EXTERNAL_DATA BIT(0)
```

相关声明：[NET_BUF_EXTERNAL_DATA](#gaaeacbdf3cfda12691c75253015e5c19a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

指示缓冲区（Buffer）关联的数据指针指向外部分配内存（Externally Allocated Memory）的标志。

<a id="r_ga61671ac866081d31dfe9eddbf3b6f210"></a>

```c
#define NET_BUF_POOL_HEAP_DEFINE(_name, _count, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_HEAP_DEFINE](#ga61671ac866081d31dfe9eddbf3b6f210)。

定义一个使用堆（Heap）存储数据的新缓冲池（Buffer Pool）。

<a id="r_gacc53824e01db7935bcc9cad564b716cd"></a>

```c
#define NET_BUF_POOL_FIXED_DEFINE(_name, _count, _data_size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_FIXED_DEFINE](#gacc53824e01db7935bcc9cad564b716cd)。

定义一个基于固定大小数据（Fixed-size Data）的新缓冲池（Buffer Pool）。

<a id="r_ga90e691e793c964847d737f5ecf7646ec"></a>

```c
#define NET_BUF_POOL_VAR_DEFINE(_name, _count, _data_size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_VAR_DEFINE](#ga90e691e793c964847d737f5ecf7646ec)。

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

<a id="r_gaf9d47aed60bc1da8fa40cc8160251ecd"></a>

```c
#define NET_BUF_POOL_VAR_ALIGN_DEFINE(_name, _count, _data_size, _ud_size, _destroy, _align)
```

相关声明：[NET_BUF_POOL_VAR_ALIGN_DEFINE](#gaf9d47aed60bc1da8fa40cc8160251ecd)。

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

<a id="r_ga810aba8ba321fd012edc238ea9fe19dc"></a>

```c
#define NET_BUF_POOL_DEFINE(_name, _count, _size, _ud_size, _destroy)
```

相关声明：[NET_BUF_POOL_DEFINE](#ga810aba8ba321fd012edc238ea9fe19dc)。

定义一个新的缓冲池（Buffer Pool）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.3\_类型定义（Typedefs）

<a id="r_ga9b74d094a45daf74cd230eaa4fcbc065"></a>

```c
typedef struct net_buf *(* net_buf_allocator_cb) (k_timeout_t timeout, void *user_data)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_allocator_cb](#ga9b74d094a45daf74cd230eaa4fcbc065)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

网络缓冲区分配器回调（Network Buffer Allocator Callback）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.4\_函数（Functions）

<a id="r_ga040279b601191367dee013bab9916d8d"></a>

```c
static void net_buf_simple_init (struct net_buf_simple *buf, size_t reserve_head)
```

相关声明：[net_buf_simple_init](#ga040279b601191367dee013bab9916d8d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

初始化 net_buf_simple 对象（Object）。

<a id="r_ga7fac47a2a25eaca39c5d14f1f55b485d"></a>

```c
void net_buf_simple_init_with_data (struct net_buf_simple *buf, void *data, size_t size)
```

相关声明：[net_buf_simple_init_with_data](#ga7fac47a2a25eaca39c5d14f1f55b485d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

使用数据初始化 net_buf_simple 对象（Object）。

<a id="r_ga4b537e913e132448cbf56976504ddddd"></a>

```c
static void net_buf_simple_reset (struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_reset](#ga4b537e913e132448cbf56976504ddddd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

重置缓冲区（Buffer）。

<a id="r_ga0186c153b72a379affdd3e2e3994b5a7"></a>

```c
void net_buf_simple_clone (const struct net_buf_simple *original, struct net_buf_simple *clone)
```

相关声明：[net_buf_simple_clone](#ga0186c153b72a379affdd3e2e3994b5a7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

克隆缓冲区状态（Buffer State），共用同一个数据缓冲区。

<a id="r_ga1906e637c848948f5780428a99b3341e"></a>

```c
void * net_buf_simple_add (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_add](#ga1906e637c848948f5780428a99b3341e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为在缓冲区（Buffer）末尾追加数据做准备。

<a id="r_gac37209c1e5097e5610860943fb7d0115"></a>

```c
void * net_buf_simple_add_mem (struct net_buf_simple *buf, const void *mem, size_t len)
```

相关声明：[net_buf_simple_add_mem](#gac37209c1e5097e5610860943fb7d0115)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从内存复制指定字节数的数据到缓冲区（Buffer）末尾。

<a id="r_ga8ff9344b8d8deba1b72b8fca048a525c"></a>

```c
uint8_t * net_buf_simple_add_u8 (struct net_buf_simple *buf, uint8_t val)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_add_u8](#ga8ff9344b8d8deba1b72b8fca048a525c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在缓冲区（Buffer）末尾追加一个 8 位字节。

<a id="r_gaa2daf3b20074ff1a23806ce88becebf5"></a>

```c
void net_buf_simple_add_le16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_add_le16](#gaa2daf3b20074ff1a23806ce88becebf5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga910f2b9df58fb0706aa40e3b80f235aa"></a>

```c
void net_buf_simple_add_be16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_add_be16](#ga910f2b9df58fb0706aa40e3b80f235aa)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_gaf1a89eb15eed79003412ba5a32a35cf6"></a>

```c
void net_buf_simple_add_le24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_le24](#gaf1a89eb15eed79003412ba5a32a35cf6)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga5eb09afeff062af577094d2d3f5fdec8"></a>

```c
void net_buf_simple_add_be24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_be24](#ga5eb09afeff062af577094d2d3f5fdec8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga3bf1bcff840dddd721f2c49ef0ed7c56"></a>

```c
void net_buf_simple_add_le32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_le32](#ga3bf1bcff840dddd721f2c49ef0ed7c56)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_gaac5cd20776d8e7bb4db77cbe5366373c"></a>

```c
void net_buf_simple_add_be32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_add_be32](#gaac5cd20776d8e7bb4db77cbe5366373c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga67da71ba5942cc11e95aa5ba02cb8552"></a>

```c
void net_buf_simple_add_le40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le40](#ga67da71ba5942cc11e95aa5ba02cb8552)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga69bdaf4373693bb468cf3876e9edf239"></a>

```c
void net_buf_simple_add_be40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be40](#ga69bdaf4373693bb468cf3876e9edf239)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga5be8c9f33df5b31c15df193a7116ce25"></a>

```c
void net_buf_simple_add_le48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le48](#ga5be8c9f33df5b31c15df193a7116ce25)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_gadb433fb4a1a61702c0615359a4340171"></a>

```c
void net_buf_simple_add_be48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be48](#gadb433fb4a1a61702c0615359a4340171)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_ga79dc411da328b847dcf1903d71eaf011"></a>

```c
void net_buf_simple_add_le64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_le64](#ga79dc411da328b847dcf1903d71eaf011)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga8e31a7b6537d7634e346236534d2a6d0"></a>

```c
void net_buf_simple_add_be64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_add_be64](#ga8e31a7b6537d7634e346236534d2a6d0)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga8473bdffadc05b22335a321df89f4b83"></a>

```c
void * net_buf_simple_remove_mem (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_remove_mem](#ga8473bdffadc05b22335a321df89f4b83)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除数据。

<a id="r_gaf508f74e5e050a7294e8a70bd3725fc3"></a>

```c
uint8_t net_buf_simple_remove_u8 (struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_remove_u8](#gaf508f74e5e050a7294e8a70bd3725fc3)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除一个 8 位值。

<a id="r_ga0b57f9ca2f3837e94cd7862e37efc01c"></a>

```c
uint16_t net_buf_simple_remove_le16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_remove_le16](#ga0b57f9ca2f3837e94cd7862e37efc01c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga93f9f84845601df4ffc118be1ffd2fee"></a>

```c
uint16_t net_buf_simple_remove_be16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_remove_be16](#ga93f9f84845601df4ffc118be1ffd2fee)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga4e2fef883228f7de41af3cf90648c3c5"></a>

```c
uint32_t net_buf_simple_remove_le24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_le24](#ga4e2fef883228f7de41af3cf90648c3c5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga9b39384162a91d7d07e037a9ada782dd"></a>

```c
uint32_t net_buf_simple_remove_be24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_be24](#ga9b39384162a91d7d07e037a9ada782dd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga9e8d016ce384378142fdec6c8dde2457"></a>

```c
uint32_t net_buf_simple_remove_le32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_le32](#ga9e8d016ce384378142fdec6c8dde2457)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_gae8ecc1fbc9dfc007f1b4e932cfaf2f1d"></a>

```c
uint32_t net_buf_simple_remove_be32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_remove_be32](#gae8ecc1fbc9dfc007f1b4e932cfaf2f1d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_ga2c937164e648fe8b854cb1144051b6b9"></a>

```c
uint64_t net_buf_simple_remove_le40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le40](#ga2c937164e648fe8b854cb1144051b6b9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_ga9abd2bccc90cf654556c18322888d131"></a>

```c
uint64_t net_buf_simple_remove_be40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be40](#ga9abd2bccc90cf654556c18322888d131)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_gac0628bbbe5d9c2b82766d5a17e767696"></a>

```c
uint64_t net_buf_simple_remove_le48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le48](#gac0628bbbe5d9c2b82766d5a17e767696)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_gab93d22797c3f406179c4c145241d6abb"></a>

```c
uint64_t net_buf_simple_remove_be48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be48](#gab93d22797c3f406179c4c145241d6abb)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_ga560bd7b181c7f08599ae9241b6ce99fd"></a>

```c
uint64_t net_buf_simple_remove_le64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_le64](#ga560bd7b181c7f08599ae9241b6ce99fd)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga602fae83e2ecf47552a11f9282619932"></a>

```c
uint64_t net_buf_simple_remove_be64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_remove_be64](#ga602fae83e2ecf47552a11f9282619932)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga64df9754665440370340c6dddde625d1"></a>

```c
void * net_buf_simple_push (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_push](#ga64df9754665440370340c6dddde625d1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

为在缓冲区（Buffer）开头添加数据做准备。

<a id="r_gaaa838083c610f7426c509efaae69a511"></a>

```c
void * net_buf_simple_push_mem (struct net_buf_simple *buf, const void *mem, size_t len)
```

相关声明：[net_buf_simple_push_mem](#gaaa838083c610f7426c509efaae69a511)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从内存复制指定字节数的数据到缓冲区（Buffer）开头。

<a id="r_ga50cd64438d8f218e3d1ef8b53b7d41a6"></a>

```c
void net_buf_simple_push_le16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_push_le16](#ga50cd64438d8f218e3d1ef8b53b7d41a6)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga827bd85eba0dbd098790d84d22e8e32d"></a>

```c
void net_buf_simple_push_be16 (struct net_buf_simple *buf, uint16_t val)
```

相关声明：[net_buf_simple_push_be16](#ga827bd85eba0dbd098790d84d22e8e32d)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga0f19da70bfc8f597680ee02c21226a77"></a>

```c
void net_buf_simple_push_u8 (struct net_buf_simple *buf, uint8_t val)
```

相关声明：[net_buf_simple_push_u8](#ga0f19da70bfc8f597680ee02c21226a77)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区（Buffer）开头压入 8 位值。

<a id="r_gabe52d6735d835edc361666bb3413b907"></a>

```c
void net_buf_simple_push_le24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_le24](#gabe52d6735d835edc361666bb3413b907)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_gabfddd4956ec1e356002a3122fea74b72"></a>

```c
void net_buf_simple_push_be24 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_be24](#gabfddd4956ec1e356002a3122fea74b72)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga8662e6bada476c0d48cebea4661b2ac1"></a>

```c
void net_buf_simple_push_le32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_le32](#ga8662e6bada476c0d48cebea4661b2ac1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gad0c3b8fdeaad6437c3dfcbb03fa52426"></a>

```c
void net_buf_simple_push_be32 (struct net_buf_simple *buf, uint32_t val)
```

相关声明：[net_buf_simple_push_be32](#gad0c3b8fdeaad6437c3dfcbb03fa52426)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_ga745ab6f34138b506b42f78e0975a5d2e"></a>

```c
void net_buf_simple_push_le40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le40](#ga745ab6f34138b506b42f78e0975a5d2e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_gad65bcaf8401e6f5ffff81a998cfb8fe5"></a>

```c
void net_buf_simple_push_be40 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be40](#gad65bcaf8401e6f5ffff81a998cfb8fe5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga66b44897e336f31e3ecbf4717bec274e"></a>

```c
void net_buf_simple_push_le48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le48](#ga66b44897e336f31e3ecbf4717bec274e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_ga1ea39c7d7e9ba4e10d31d818e45e192a"></a>

```c
void net_buf_simple_push_be48 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be48](#ga1ea39c7d7e9ba4e10d31d818e45e192a)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_ga771634e50e2bf7c291565ce6b2af7e85"></a>

```c
void net_buf_simple_push_le64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_le64](#ga771634e50e2bf7c291565ce6b2af7e85)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gafea2201655955ab004b5f77106998ae9"></a>

```c
void net_buf_simple_push_be64 (struct net_buf_simple *buf, uint64_t val)
```

相关声明：[net_buf_simple_push_be64](#gafea2201655955ab004b5f77106998ae9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gaf5ab4a5fe4a6226be72a510fea0ed8a8"></a>

```c
void * net_buf_simple_pull (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_pull](#gaf5ab4a5fe4a6226be72a510fea0ed8a8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga9c676fdbd6e999a9eab26b13d3608e0c"></a>

```c
void * net_buf_simple_pull_mem (struct net_buf_simple *buf, size_t len)
```

相关声明：[net_buf_simple_pull_mem](#ga9c676fdbd6e999a9eab26b13d3608e0c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga09a261c615136fd39834cd301fc692e7"></a>

```c
uint8_t net_buf_simple_pull_u8 (struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_pull_u8](#ga09a261c615136fd39834cd301fc692e7)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除一个 8 位值。

<a id="r_gad59d180ae81b55f6d618565a37d25dba"></a>

```c
uint16_t net_buf_simple_pull_le16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_pull_le16](#gad59d180ae81b55f6d618565a37d25dba)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_gae36458ba05a4ab89e429be4cfd264440"></a>

```c
uint16_t net_buf_simple_pull_be16 (struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_pull_be16](#gae36458ba05a4ab89e429be4cfd264440)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga4c9d2ac72a176c49ec224353b5566eb9"></a>

```c
uint32_t net_buf_simple_pull_le24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_le24](#ga4c9d2ac72a176c49ec224353b5566eb9)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga4c24d445d6b75c850a9e95fb242a50e1"></a>

```c
uint32_t net_buf_simple_pull_be24 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_be24](#ga4c24d445d6b75c850a9e95fb242a50e1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga38df82e6ba9bc2c75133200f7fa75353"></a>

```c
uint32_t net_buf_simple_pull_le32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_le32](#ga38df82e6ba9bc2c75133200f7fa75353)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga1a53892ed75f994bbbb3a2bcf1743d3c"></a>

```c
uint32_t net_buf_simple_pull_be32 (struct net_buf_simple *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_simple_pull_be32](#ga1a53892ed75f994bbbb3a2bcf1743d3c)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_gad669c07efe5cb90ebffcc76d9c1029a1"></a>

```c
uint64_t net_buf_simple_pull_le40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le40](#gad669c07efe5cb90ebffcc76d9c1029a1)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_gaa665830dad59ac957f79c7f1cc84aed5"></a>

```c
uint64_t net_buf_simple_pull_be40 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be40](#gaa665830dad59ac957f79c7f1cc84aed5)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga69fbfbd72b17783c5ee12b4b2ac9af46"></a>

```c
uint64_t net_buf_simple_pull_le48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le48](#ga69fbfbd72b17783c5ee12b4b2ac9af46)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga19bdefe740fe94a42fba76d71b4ef6e2"></a>

```c
uint64_t net_buf_simple_pull_be48 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be48](#ga19bdefe740fe94a42fba76d71b4ef6e2)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga7e0e2d0adbe9062d08f5d8afc7acd89e"></a>

```c
uint64_t net_buf_simple_pull_le64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_le64](#ga7e0e2d0adbe9062d08f5d8afc7acd89e)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gad07f0d49a7db99063077de493e7b0712"></a>

```c
uint64_t net_buf_simple_pull_be64 (struct net_buf_simple *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_simple_pull_be64](#gad07f0d49a7db99063077de493e7b0712)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8"></a>

```c
static uint8_t * net_buf_simple_tail (const struct net_buf_simple *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_simple_tail](#gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

获取缓冲区的尾指针（Tail Pointer）。

<a id="r_gadc6ae86245c2a2607c671a524227b026"></a>

```c
static size_t net_buf_simple_headroom (const struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_headroom](#gadc6ae86245c2a2607c671a524227b026)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区的头部预留空间（Headroom）。

<a id="r_ga73e2c42fc23e857a46553084b747c996"></a>

```c
static size_t net_buf_simple_tailroom (const struct net_buf_simple *buf)
```

相关声明：[net_buf_simple_tailroom](#ga73e2c42fc23e857a46553084b747c996)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区的尾部剩余空间（Tailroom）。

<a id="r_ga7476ec7222d074e7dc9783e7ed9cd800"></a>

```c
static uint16_t net_buf_simple_max_len (const struct net_buf_simple *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_simple_max_len](#ga7476ec7222d074e7dc9783e7ed9cd800)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查 net_buf_simple::len 的最大值。

<a id="r_ga5c4038cb3aa506c3cad7a2505392aa50"></a>

```c
static bool net_buf_simple_is_valid (const struct net_buf_simple *buf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf_simple_is_valid](#ga5c4038cb3aa506c3cad7a2505392aa50)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

检查缓冲区（Buffer）的长度与指针是否自洽。

<a id="r_gabf5b098aa0926d9b7fb88baff8a3e2d8"></a>

```c
static void net_buf_simple_save (const struct net_buf_simple *buf, struct net_buf_simple_state *state)
```

相关声明：[net_buf_simple_save](#gabf5b098aa0926d9b7fb88baff8a3e2d8)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

保存缓冲区的解析状态（Parsing State）。

<a id="r_gaedd36481657a7a9d108659d56e131721"></a>

```c
static void net_buf_simple_restore (struct net_buf_simple *buf, struct net_buf_simple_state *state)
```

相关声明：[net_buf_simple_restore](#gaedd36481657a7a9d108659d56e131721)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)、[net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)、[state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)。

恢复缓冲区的解析状态（Parsing State）。

<a id="r_ga145f4b2de7548814eaa7ba86fb123989"></a>

```c
struct net_buf_pool * net_buf_pool_get (int id)
```

相关声明：[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[net_buf_pool_get](#ga145f4b2de7548814eaa7ba86fb123989)。

根据 ID 查找缓冲池（Pool）。

<a id="r_gacdf048dc0afc7ef67027117e0d51d3a3"></a>

```c
int net_buf_id (const struct net_buf *buf)
```

相关声明：[net_buf_id](#gacdf048dc0afc7ef67027117e0d51d3a3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区从零开始的索引（Zero-based Index）。

<a id="r_ga9cd6d30ea47a91647d3c4a60d82b5cd4"></a>

```c
static size_t net_buf_get_available (struct net_buf_pool *pool)
```

相关声明：[net_buf_get_available](#ga9cd6d30ea47a91647d3c4a60d82b5cd4)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取当前可从缓冲池（Pool）申领的缓冲区数量。

<a id="r_gad652ef7d2895f8077c366a564b785291"></a>

```c
static size_t net_buf_get_max_used (struct net_buf_pool *pool)
```

相关声明：[net_buf_get_max_used](#gad652ef7d2895f8077c366a564b785291)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)。

获取从缓冲池（Pool）同时申领的缓冲区数量峰值。

<a id="r_ga686df794ec6881625b54454a33587bab"></a>

```c
struct net_buf * net_buf_alloc_fixed (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_fixed](#ga686df794ec6881625b54454a33587bab)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新的固定大小缓冲区（Fixed Buffer）。

<a id="r_ga534366f3b5c7f41a28372c12149ca005"></a>

```c
static struct net_buf * net_buf_alloc (struct net_buf_pool *pool, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc](#ga534366f3b5c7f41a28372c12149ca005)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

<a id="r_ga11d489aedcca82117965fa6ba9d11ca5"></a>

```c
struct net_buf * net_buf_alloc_len (struct net_buf_pool *pool, size_t size, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_len](#ga11d489aedcca82117965fa6ba9d11ca5)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新的变长缓冲区（Variable Length Buffer）。

<a id="r_ga8c24d0761d6d38facb6cca60c7c13c0c"></a>

```c
struct net_buf * net_buf_alloc_with_data (struct net_buf_pool *pool, void *data, size_t size, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_alloc_with_data](#ga8c24d0761d6d38facb6cca60c7c13c0c)、[net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

从缓冲池（Pool）分配一个新缓冲区，使用外部数据指针（External Data Pointer）。

<a id="r_ga739249547eb37b839b3c1ebdbcb88d28"></a>

```c
static void net_buf_destroy (struct net_buf *buf)
```

相关声明：[net_buf_destroy](#ga739249547eb37b839b3c1ebdbcb88d28)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从自定义销毁回调（Custom Destroy Callback）中销毁缓冲区。

<a id="r_ga1292f38b096fd80e31889aff44b0c021"></a>

```c
void net_buf_reset (struct net_buf *buf)
```

相关声明：[net_buf_reset](#ga1292f38b096fd80e31889aff44b0c021)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

重置缓冲区（Buffer）。

<a id="r_ga0e5d3d938becfefc4f4b4d083cb467aa"></a>

```c
void net_buf_simple_reserve (struct net_buf_simple *buf, size_t reserve)
```

相关声明：[net_buf_simple_reserve](#ga0e5d3d938becfefc4f4b4d083cb467aa)、[net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)。

使用给定的头部预留空间（Headroom）初始化缓冲区。

<a id="r_ga6d2dfc45e1e5acf21fe08359a4f92a18"></a>

```c
void net_buf_slist_put (sys_slist_t *list, struct net_buf *buf)
```

相关声明：[net_buf_slist_put](#ga6d2dfc45e1e5acf21fe08359a4f92a18)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将缓冲区（Buffer）放入列表（List）。

<a id="r_ga218d4a0c160c57a44946154478724cb3"></a>

```c
struct net_buf * net_buf_slist_get (sys_slist_t *list)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_slist_get](#ga218d4a0c160c57a44946154478724cb3)、[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)。

从列表（List）获取缓冲区（Buffer）。

<a id="r_gabedcb728bc2fc0c2b5319a8fd87e8273"></a>

```c
void net_buf_unref (struct net_buf *buf)
```

相关声明：[net_buf_unref](#gabedcb728bc2fc0c2b5319a8fd87e8273)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

递减缓冲区的引用计数（Reference Count）。

<a id="r_ga29387b2a672bf2bb8739046a46f3601f"></a>

```c
struct net_buf * net_buf_ref (struct net_buf *buf)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_ref](#ga29387b2a672bf2bb8739046a46f3601f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

递增缓冲区的引用计数（Reference Count）。

<a id="r_ga4ff24d6ae1aff46e17647ef91db593ca"></a>

```c
static struct net_buf * net_buf_take (struct net_buf **orig)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_take](#ga4ff24d6ae1aff46e17647ef91db593ca)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

移动缓冲区指针（Buffer Pointer），将 orig 设置为 NULL。

<a id="r_ga6b43ad0740b23c0544d706c77c9f1e13"></a>

```c
static void net_buf_drop (struct net_buf **orig)
```

相关声明：[net_buf_drop](#ga6b43ad0740b23c0544d706c77c9f1e13)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放缓冲区引用（Buffer Reference），并清空指针。

<a id="r_gaf4d80e2878e3c790fff206bec820f03f"></a>

```c
struct net_buf * net_buf_clone (struct net_buf *buf, k_timeout_t timeout)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_clone](#gaf4d80e2878e3c790fff206bec820f03f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)。

克隆缓冲区（Clone Buffer）。

<a id="r_gaf2df457abe3e56d47107b76bdc004756"></a>

```c
static void * net_buf_user_data (const struct net_buf *buf)
```

相关声明：[net_buf_user_data](#gaf2df457abe3e56d47107b76bdc004756)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取指向缓冲区用户数据（User Data）的指针。

<a id="r_ga4d1dd56ca8d32d3cfda114fd36761d0d"></a>

```c
int net_buf_user_data_copy (struct net_buf *dst, const struct net_buf *src)
```

相关声明：[net_buf_user_data_copy](#ga4d1dd56ca8d32d3cfda114fd36761d0d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将用户数据（User Data）从一个缓冲区复制到另一个缓冲区。

<a id="r_ga8ac58ad4f73b498bef2ff3ac7e30c6c3"></a>

```c
static void net_buf_reserve (struct net_buf *buf, size_t reserve)
```

相关声明：[net_buf_reserve](#ga8ac58ad4f73b498bef2ff3ac7e30c6c3)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

使用给定的头部预留空间（Headroom）初始化缓冲区。

<a id="r_ga30776d2b21f06d244c083af5c25b0f3e"></a>

```c
static void * net_buf_add (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_add](#ga30776d2b21f06d244c083af5c25b0f3e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

为在缓冲区（Buffer）末尾追加数据做准备。

<a id="r_gacf4e2eba52975ba6728c79274a769d0f"></a>

```c
static void * net_buf_add_mem (struct net_buf *buf, const void *mem, size_t len)
```

相关声明：[net_buf_add_mem](#gacf4e2eba52975ba6728c79274a769d0f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将指定字节数的数据复制到缓冲区（Buffer）末尾。

<a id="r_ga868ac2bea103fed568b461cbcd45eda2"></a>

```c
static uint8_t * net_buf_add_u8 (struct net_buf *buf, uint8_t val)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_add_u8](#ga868ac2bea103fed568b461cbcd45eda2)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在缓冲区（Buffer）末尾追加一个 8 位字节。

<a id="r_gadd6d01a3b1efd0de16f9bef975809404"></a>

```c
static void net_buf_add_le16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_add_le16](#gadd6d01a3b1efd0de16f9bef975809404)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga61878a9bd7462ca925eac39181f2972c"></a>

```c
static void net_buf_add_be16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_add_be16](#ga61878a9bd7462ca925eac39181f2972c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

在缓冲区（Buffer）末尾追加 16 位值。

<a id="r_ga32b90364091ade229830686f03b25d4c"></a>

```c
static void net_buf_add_le24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_le24](#ga32b90364091ade229830686f03b25d4c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_ga0f3cd9f9b364a2d2125aea19221d3e1e"></a>

```c
static void net_buf_add_be24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_be24](#ga0f3cd9f9b364a2d2125aea19221d3e1e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 24 位值。

<a id="r_gae8ba33b6592ef7fd859b35d63b285d87"></a>

```c
static void net_buf_add_le32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_le32](#gae8ba33b6592ef7fd859b35d63b285d87)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga5543d00c96f83970f8dbf3670a9dc3fc"></a>

```c
static void net_buf_add_be32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_add_be32](#ga5543d00c96f83970f8dbf3670a9dc3fc)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

在缓冲区（Buffer）末尾追加 32 位值。

<a id="r_ga62790f9644102f4952c250f6513a2ada"></a>

```c
static void net_buf_add_le40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le40](#ga62790f9644102f4952c250f6513a2ada)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_ga70cb98da91de098a92fbd69712c2bde7"></a>

```c
static void net_buf_add_be40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be40](#ga70cb98da91de098a92fbd69712c2bde7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 40 位值。

<a id="r_gaf19bf75c3d4d645b1eebf9254aa22790"></a>

```c
static void net_buf_add_le48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le48](#gaf19bf75c3d4d645b1eebf9254aa22790)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_ga8fe6feb191ab338e91bd62f44e184deb"></a>

```c
static void net_buf_add_be48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be48](#ga8fe6feb191ab338e91bd62f44e184deb)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 48 位值。

<a id="r_gac3f955f8fecc0e5971d2e5e8176e973e"></a>

```c
static void net_buf_add_le64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_le64](#gac3f955f8fecc0e5971d2e5e8176e973e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_ga055f6eb7d5fbc9a3cf529a9ed00970c4"></a>

```c
static void net_buf_add_be64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_add_be64](#ga055f6eb7d5fbc9a3cf529a9ed00970c4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

在缓冲区（Buffer）末尾追加 64 位值。

<a id="r_gace5ad98eac4772db3b0fa2181912f1f0"></a>

```c
static void * net_buf_remove_mem (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_remove_mem](#gace5ad98eac4772db3b0fa2181912f1f0)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除数据。

<a id="r_gad954b9f37790d5e7087db7db7bdedd41"></a>

```c
static uint8_t net_buf_remove_u8 (struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_remove_u8](#gad954b9f37790d5e7087db7db7bdedd41)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除一个 8 位值。

<a id="r_gaaf654110fb6a8bdfc27433945d4d1308"></a>

```c
static uint16_t net_buf_remove_le16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_remove_le16](#gaaf654110fb6a8bdfc27433945d4d1308)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga5da86c8ea703ab3f01c408cce73b0651"></a>

```c
static uint16_t net_buf_remove_be16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_remove_be16](#ga5da86c8ea703ab3f01c408cce73b0651)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 16 位数据。

<a id="r_ga6f346a9af570528d238592851240fd74"></a>

```c
static uint32_t net_buf_remove_be24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_be24](#ga6f346a9af570528d238592851240fd74)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_ga903f59c8dea1b2c54969b567fe315041"></a>

```c
static uint32_t net_buf_remove_le24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_le24](#ga903f59c8dea1b2c54969b567fe315041)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 24 位数据。

<a id="r_gae9321a469cc751c58cfb532afd57d265"></a>

```c
static uint32_t net_buf_remove_le32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_le32](#gae9321a469cc751c58cfb532afd57d265)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_gacce707d646d7008ec3167af1a0b20da8"></a>

```c
static uint32_t net_buf_remove_be32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_remove_be32](#gacce707d646d7008ec3167af1a0b20da8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 32 位数据。

<a id="r_ga57150a1ba09b28e5c3b04bdefce7ed8e"></a>

```c
static uint64_t net_buf_remove_le40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le40](#ga57150a1ba09b28e5c3b04bdefce7ed8e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_gae2920eab3c56d0d462811b83961df466"></a>

```c
static uint64_t net_buf_remove_be40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be40](#gae2920eab3c56d0d462811b83961df466)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 40 位数据。

<a id="r_ga0c147d9f95e2224696a8ace26f63a300"></a>

```c
static uint64_t net_buf_remove_le48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le48](#ga0c147d9f95e2224696a8ace26f63a300)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_gaab0e3bcc21c958c01ef076cd0efe087c"></a>

```c
static uint64_t net_buf_remove_be48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be48](#gaab0e3bcc21c958c01ef076cd0efe087c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 48 位数据。

<a id="r_ga447b9c6be3fe04a50eb35dd29f190b6d"></a>

```c
static uint64_t net_buf_remove_le64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_le64](#ga447b9c6be3fe04a50eb35dd29f190b6d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga8b9edd213da2d48dfb8d70a8d307ba13"></a>

```c
static uint64_t net_buf_remove_be64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_remove_be64](#ga8b9edd213da2d48dfb8d70a8d307ba13)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）末尾移除并转换 64 位数据。

<a id="r_ga96a2b1f07f3a7958057d9c7cc1f01b73"></a>

```c
static void * net_buf_push (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_push](#ga96a2b1f07f3a7958057d9c7cc1f01b73)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

为在缓冲区（Buffer）起始位置添加数据做准备。

<a id="r_ga7e9daccec8cae1b9bfda52b0758adf0c"></a>

```c
static void * net_buf_push_mem (struct net_buf *buf, const void *mem, size_t len)
```

相关声明：[net_buf_push_mem](#ga7e9daccec8cae1b9bfda52b0758adf0c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将指定字节数的数据复制到缓冲区（Buffer）起始位置。

<a id="r_ga9093202ba0a22bfa519bbe32d4585186"></a>

```c
static void net_buf_push_u8 (struct net_buf *buf, uint8_t val)
```

相关声明：[net_buf_push_u8](#ga9093202ba0a22bfa519bbe32d4585186)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向缓冲区（Buffer）开头压入 8 位值。

<a id="r_gab6c84c6846c06c2b339bc88df35e2655"></a>

```c
static void net_buf_push_le16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_push_le16](#gab6c84c6846c06c2b339bc88df35e2655)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga6dd756ff8332d076f5d37c69e6c534b5"></a>

```c
static void net_buf_push_be16 (struct net_buf *buf, uint16_t val)
```

相关声明：[net_buf_push_be16](#ga6dd756ff8332d076f5d37c69e6c534b5)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向缓冲区（Buffer）开头压入 16 位值。

<a id="r_ga87524ac50e53ba59c6692af10cf001b9"></a>

```c
static void net_buf_push_le24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_le24](#ga87524ac50e53ba59c6692af10cf001b9)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga87338399d8ecd64a894908ed4a2f710b"></a>

```c
static void net_buf_push_be24 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_be24](#ga87338399d8ecd64a894908ed4a2f710b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 24 位值。

<a id="r_ga97c9046185d6a1e9235bf6914c72dfc4"></a>

```c
static void net_buf_push_le32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_le32](#ga97c9046185d6a1e9235bf6914c72dfc4)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gae4e64a23708ed910fb6c3ab8ba481a4c"></a>

```c
static void net_buf_push_be32 (struct net_buf *buf, uint32_t val)
```

相关声明：[net_buf_push_be32](#gae4e64a23708ed910fb6c3ab8ba481a4c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向缓冲区（Buffer）开头压入 32 位值。

<a id="r_gaefab4a755cf4fb7d2b4a142a9351c189"></a>

```c
static void net_buf_push_le40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le40](#gaefab4a755cf4fb7d2b4a142a9351c189)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga512f84e686ff70a5589557575ccda1f8"></a>

```c
static void net_buf_push_be40 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be40](#ga512f84e686ff70a5589557575ccda1f8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 40 位值。

<a id="r_ga852654f7e59951bf3536e3f4e98761bf"></a>

```c
static void net_buf_push_le48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le48](#ga852654f7e59951bf3536e3f4e98761bf)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_gabfbcb051019ff210cc2b85adcf4bc821"></a>

```c
static void net_buf_push_be48 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be48](#gabfbcb051019ff210cc2b85adcf4bc821)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 48 位值。

<a id="r_gad4ee42b023881f80211fbeca53a0f25d"></a>

```c
static void net_buf_push_le64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_le64](#gad4ee42b023881f80211fbeca53a0f25d)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_ga43ff5faab0b099a355b9b96b7b0e3d8c"></a>

```c
static void net_buf_push_be64 (struct net_buf *buf, uint64_t val)
```

相关声明：[net_buf_push_be64](#ga43ff5faab0b099a355b9b96b7b0e3d8c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)。

向缓冲区（Buffer）开头压入 64 位值。

<a id="r_gaef433d92734dd8691c292abdb823ba0e"></a>

```c
static void * net_buf_pull (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_pull](#gaef433d92734dd8691c292abdb823ba0e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_gaedc5ffe19bb0ec438e633023c3c5de74"></a>

```c
static void * net_buf_pull_mem (struct net_buf *buf, size_t len)
```

相关声明：[net_buf_pull_mem](#gaedc5ffe19bb0ec438e633023c3c5de74)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除数据。

<a id="r_ga71bb306d2ce459a60a8c3fc6dac54c90"></a>

```c
static uint8_t net_buf_pull_u8 (struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_pull_u8](#ga71bb306d2ce459a60a8c3fc6dac54c90)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除一个 8 位值。

<a id="r_gaed64e9f2b969f2c0d99cd281e73c860a"></a>

```c
static uint16_t net_buf_pull_le16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_pull_le16](#gaed64e9f2b969f2c0d99cd281e73c860a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga97909a33c374a5c757fd2faf582139b7"></a>

```c
static uint16_t net_buf_pull_be16 (struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_pull_be16](#ga97909a33c374a5c757fd2faf582139b7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 16 位数据。

<a id="r_ga85c505321484a50ed9422f24934ed077"></a>

```c
static uint32_t net_buf_pull_le24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_le24](#ga85c505321484a50ed9422f24934ed077)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga8de937e8775879712ea0acbf60327a95"></a>

```c
static uint32_t net_buf_pull_be24 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_be24](#ga8de937e8775879712ea0acbf60327a95)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 24 位数据。

<a id="r_ga5f051078f1ffcc40e9ad40e7545a084f"></a>

```c
static uint32_t net_buf_pull_le32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_le32](#ga5f051078f1ffcc40e9ad40e7545a084f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga5f8f2e2244eb574b3e57d09d85412967"></a>

```c
static uint32_t net_buf_pull_be32 (struct net_buf *buf)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[net_buf_pull_be32](#ga5f8f2e2244eb574b3e57d09d85412967)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 32 位数据。

<a id="r_ga36b27c6373eb245f777164065386d100"></a>

```c
static uint64_t net_buf_pull_le40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le40](#ga36b27c6373eb245f777164065386d100)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga050bdaccaec842482a02b096aa0c999f"></a>

```c
static uint64_t net_buf_pull_be40 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be40](#ga050bdaccaec842482a02b096aa0c999f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 40 位数据。

<a id="r_ga7eeee45b6639146d1492f92263ee4f51"></a>

```c
static uint64_t net_buf_pull_le48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le48](#ga7eeee45b6639146d1492f92263ee4f51)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga68934e105c4b3a8e27aa61b3ec5526db"></a>

```c
static uint64_t net_buf_pull_be48 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be48](#ga68934e105c4b3a8e27aa61b3ec5526db)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 48 位数据。

<a id="r_ga9a3df35e2287cbcfe1b60e2efa52c64e"></a>

```c
static uint64_t net_buf_pull_le64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_le64](#ga9a3df35e2287cbcfe1b60e2efa52c64e)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_ga3c1e80741a49691e69e57c891d3edb05"></a>

```c
static uint64_t net_buf_pull_be64 (struct net_buf *buf)
```

相关声明：[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[net_buf_pull_be64](#ga3c1e80741a49691e69e57c891d3edb05)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区（Buffer）开头移除并转换 64 位数据。

<a id="r_gaecbc6adf16469e3366c88445ea7a553a"></a>

```c
static size_t net_buf_tailroom (const struct net_buf *buf)
```

相关声明：[net_buf_tailroom](#gaecbc6adf16469e3366c88445ea7a553a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区的尾部剩余空间（Tailroom）。

<a id="r_gac9a09897f44e708f920064826aa2f703"></a>

```c
static size_t net_buf_headroom (const struct net_buf *buf)
```

相关声明：[net_buf_headroom](#gac9a09897f44e708f920064826aa2f703)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区的头部预留空间（Headroom）。

<a id="r_ga65924b8234c91dfc09069ba06242a6b7"></a>

```c
static uint16_t net_buf_max_len (const struct net_buf *buf)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[net_buf_max_len](#ga65924b8234c91dfc09069ba06242a6b7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查 net_buf::len 的最大值。

<a id="r_ga8d258ef1e4241c438a726486bc7fe766"></a>

```c
static bool net_buf_is_valid (const struct net_buf *buf)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[net_buf_is_valid](#ga8d258ef1e4241c438a726486bc7fe766)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

检查缓冲区（Buffer）的长度与指针是否自洽。

<a id="r_gaedb10a84b352a3d7716bef979af2ab31"></a>

```c
static uint8_t * net_buf_tail (const struct net_buf *buf)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_buf_tail](#gaedb10a84b352a3d7716bef979af2ab31)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

获取缓冲区的尾指针（Tail Pointer）。

<a id="r_ga042ce3f2e7e3fd0948ca2623fff36746"></a>

```c
struct net_buf * net_buf_frag_last (struct net_buf *frags)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_last](#ga042ce3f2e7e3fd0948ca2623fff36746)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

在分片列表（Fragment List）中查找最后一个分片。

<a id="r_gac032b44db4a845dba8303fecfe1b63e7"></a>

```c
void net_buf_frag_insert (struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf_frag_insert](#gac032b44db4a845dba8303fecfe1b63e7)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

向缓冲区链（Chain of Buffers）插入新分片（Fragment）。

<a id="r_ga0d7e310802a2bc7b2078f9310827535f"></a>

```c
struct net_buf * net_buf_frag_add (struct net_buf *head, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_add](#ga0d7e310802a2bc7b2078f9310827535f)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将新分片（Fragment）追加到缓冲区链（Chain of Buffers）末尾。

<a id="r_ga602a99833bd401a0ada5bd5defa7a2ff"></a>

```c
struct net_buf * net_buf_frag_del (struct net_buf *parent, struct net_buf *frag)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_frag_del](#ga602a99833bd401a0ada5bd5defa7a2ff)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从缓冲区链（Chain of Buffers）中删除现有分片（Fragment）。

<a id="r_gaffd49f2de8e72d5f7585b4e5167923d8"></a>

```c
size_t net_buf_linearize (void *dst, size_t dst_len, const struct net_buf *src, size_t offset, size_t len)
```

相关声明：[net_buf_linearize](#gaffd49f2de8e72d5f7585b4e5167923d8)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

从 net_buf 链的指定偏移量（Offset）开始，将字节复制到线性缓冲区（Linear Buffer）。

<a id="r_ga646d680491753b3ed29fa83c26732d1a"></a>

```c
size_t net_buf_append_bytes (struct net_buf *buf, size_t len, const void *value, k_timeout_t timeout, net_buf_allocator_cb allocate_cb, void *user_data)
```

相关声明：[net_buf_append_bytes](#ga646d680491753b3ed29fa83c26732d1a)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[k_timeout_t](../timer_reference/P087_内核超时类型.md)、[net_buf_allocator_cb](#ga9b74d094a45daf74cd230eaa4fcbc065)。

向 net_buf 列表追加数据（Append Data）。

<a id="r_gaef938c3ab676a5bd5bf8338b8d7cb30c"></a>

```c
size_t net_buf_data_match (const struct net_buf *buf, size_t offset, const void *data, size_t len)
```

相关声明：[net_buf_data_match](#gaef938c3ab676a5bd5bf8338b8d7cb30c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

将数据与 net_buf 的内容进行匹配（Match）。

<a id="r_ga2d7096280d4fa6f5e32c4674d542889b"></a>

```c
static struct net_buf * net_buf_skip (struct net_buf *buf, size_t len)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[net_buf_skip](#ga2d7096280d4fa6f5e32c4674d542889b)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

跳过 net_buf 中的 N 个字节（Skip）。

<a id="r_gaebb95f08dbd4d38a250170aa78ddeb44"></a>

```c
static size_t net_buf_frags_len (const struct net_buf *buf)
```

相关声明：[net_buf_frags_len](#gaebb95f08dbd4d38a250170aa78ddeb44)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

计算分片（Fragment）中存储的字节数。

## 1.5\_详细说明（Detailed Documentation）

<a id="gaaeacbdf3cfda12691c75253015e5c19a"></a>

### `NET_BUF_EXTERNAL_DATA`

```c
#define NET_BUF_EXTERNAL_DATA BIT(0)
```

```c
#include <zephyr/net_buf.h>
```

指示缓冲区（Buffer）关联的数据指针指向外部分配内存（Externally Allocated Memory）的标志。

因此，当 `ref` 降至零时，无需释放其指向的数据。`net_buf` API 的使用者不必显式设置或清除此标志。这类 `net_buf` 只能通过 `net_buf_alloc_with_data()` 实例化。不过，引用计数（Reference Count）机制仍照常工作：引用计数降至 `0` 时释放 `net_buf`，但不释放其数据指针所指的存储。

<a id="ga810aba8ba321fd012edc238ea9fe19dc"></a>

### `NET_BUF_POOL_DEFINE`

```c
#define NET_BUF_POOL_DEFINE ( _name, _count, _size, _ud_size, _destroy )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
NET_BUF_POOL_FIXED_DEFINE(_name, _count, _size, _ud_size, _destroy)
```

定义一个新的缓冲池（Buffer Pool）。

定义 `net_buf_pool` 结构，以及所需数量缓冲区的必要存储空间，即结构数组。之后，可通过 `net_buf_alloc` 从池中获取缓冲区。池定义为静态变量（Static Variable）；如果需要导出到当前模块之外，应借助单独的指针，而不能使用 `extern` 声明。

如果提供了自定义销毁回调（Destroy Callback），该回调负责最终调用 `net_buf_destroy()`，完成将缓冲区归还池的过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 缓冲池变量名称（Pool Variable Name）。 |
| `_count` | 池中的缓冲区数量（Number of Buffers）。 |
| `_size` | 每个缓冲区的最大数据大小（Maximum Data Size）。 |
| `_ud_size` | 要预留的用户数据空间大小（User Data Space）。 |
| `_destroy` | 缓冲区释放时可选的销毁回调（Destroy Callback）。 |

<a id="gacc53824e01db7935bcc9cad564b716cd"></a>

### `NET_BUF_POOL_FIXED_DEFINE`

```c
#define NET_BUF_POOL_FIXED_DEFINE ( _name, _count, _data_size, _ud_size, _destroy )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
_NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
static uint8_t __noinit net_buf_data_##_name[_count][_data_size] __net_buf_align; \
static const struct net_buf_pool_fixed net_buf_fixed_##_name = {       \
        .data_pool = (uint8_t *)net_buf_data_##_name,                  \
};                                                                     \
static const struct net_buf_data_alloc net_buf_fixed_alloc_##_name = { \
        .cb = &net_buf_fixed_cb,                                       \
        .alloc_data = (void *)&net_buf_fixed_##_name,                  \
        .max_alloc_size = _data_size,                                  \
};                                                                     \
static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
        NET_BUF_POOL_INITIALIZER(_name, &net_buf_fixed_alloc_##_name,  \
                                 _net_buf_##_name, _count, _ud_size,   \
                                 _destroy)
```

定义一个基于固定大小数据（Fixed-size Data）的新缓冲池（Buffer Pool）。

定义 `net_buf_pool` 结构，以及所需数量缓冲区的必要存储空间，即结构数组。之后，可通过 `net_buf_alloc` 从池中获取缓冲区。池定义为静态变量（Static Variable）；如果需要导出到当前模块之外，应借助单独的指针，而不能使用 `extern` 声明。

缓冲区的数据载荷（Data Payload）从由固定大小块组成的字节数组中分配。这类池不支持在数据分配时阻塞，所以尝试分配数据时，传给 `net_buf_alloc` 的超时始终按 `K_NO_WAIT` 处理。因此，必须始终妥善处理分配失败，即返回 `NULL` 的情况。

如果提供了自定义销毁回调（Destroy Callback），该回调负责最终调用 `net_buf_destroy()`，完成将缓冲区归还池的过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 缓冲池变量名称（Pool Variable Name）。 |
| `_count` | 池中的缓冲区数量（Number of Buffers）。 |
| `_data_size` | 每个缓冲区的最大数据载荷（Maximum Data Payload）。 |
| `_ud_size` | 每个缓冲区要预留的用户数据空间（User Data Space）。 |
| `_destroy` | 缓冲区释放时可选的销毁回调（Destroy Callback）。 |

<a id="ga61671ac866081d31dfe9eddbf3b6f210"></a>

### `NET_BUF_POOL_HEAP_DEFINE`

```c
#define NET_BUF_POOL_HEAP_DEFINE ( _name, _count, _ud_size, _destroy )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
_NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                      \
static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                \
        NET_BUF_POOL_INITIALIZER(_name, &net_buf_heap_alloc,         \
                                 _net_buf_##_name, _count, _ud_size, \
                                 _destroy)
```

定义一个使用堆（Heap）存储数据的新缓冲池（Buffer Pool）。

定义 `net_buf_pool` 结构，以及所需数量缓冲区的必要存储空间，即结构数组。之后，可通过 `net_buf_alloc` 从池中获取缓冲区。池定义为静态变量（Static Variable）；如果需要导出到当前模块之外，应借助单独的指针，而不能使用 `extern` 声明。

缓冲区的数据载荷（Data Payload）通过 `k_malloc` 从堆分配，因此 `CONFIG_HEAP_MEM_POOL_SIZE` 必须设置为正值。这类池不支持在数据分配时阻塞，所以尝试分配数据时，传给 `net_buf_alloc` 的超时始终按 `K_NO_WAIT` 处理。因此，必须始终妥善处理分配失败，即返回 `NULL` 的情况。

如果提供了自定义销毁回调（Destroy Callback），该回调负责最终调用 `net_buf_destroy()`，完成将缓冲区归还池的过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 缓冲池变量名称（Pool Variable Name）。 |
| `_count` | 池中的缓冲区数量（Number of Buffers）。 |
| `_ud_size` | 每个缓冲区要预留的用户数据空间（User Data Space）。 |
| `_destroy` | 缓冲区释放时可选的销毁回调（Destroy Callback）。 |

<a id="gaf9d47aed60bc1da8fa40cc8160251ecd"></a>

### `NET_BUF_POOL_VAR_ALIGN_DEFINE`

```c
#define NET_BUF_POOL_VAR_ALIGN_DEFINE ( _name, _count, _data_size, _ud_size, _destroy, _align )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
_NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
K_HEAP_DEFINE(net_buf_mem_pool_##_name, _data_size);                   \
static const struct net_buf_data_alloc net_buf_data_alloc_##_name = {  \
        .cb = &net_buf_var_cb,                                         \
        .alloc_data = &net_buf_mem_pool_##_name,                       \
        .max_alloc_size = 0,                                           \
        .alignment = _align,                                           \
};                                                                     \
static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
        NET_BUF_POOL_INITIALIZER(_name, &net_buf_data_alloc_##_name,   \
                                 _net_buf_##_name, _count, _ud_size,   \
                                 _destroy)
```

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

按指定对齐要求（Alignment）对齐缓冲区长度和起始地址。

定义 `net_buf_pool` 结构，以及所需数量缓冲区的必要存储空间，即结构数组。之后，可通过 `net_buf_alloc` 从池中获取缓冲区。池定义为静态变量（Static Variable）；如果需要导出到当前模块之外，应借助单独的指针，而不能使用 `extern` 声明。

缓冲区的数据载荷（Data Payload）基于内存池分配，该池支持分配可变大小载荷。

如果提供了自定义销毁回调（Destroy Callback），该回调负责最终调用 `net_buf_destroy()`，完成将缓冲区归还池的过程。

缓冲区的长度和起始地址都按指定对齐要求（Alignment）对齐。对齐值必须是 `2` 的幂，且不得大于数据载荷的大小。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 缓冲池变量名称（Pool Variable Name）。 |
| `_count` | 池中的缓冲区数量（Number of Buffers）。 |
| `_data_size` | 可供数据载荷使用的内存总量（Total Memory）。 |
| `_ud_size` | 每个缓冲区要预留的用户数据空间（User Data Space）。 |
| `_destroy` | 缓冲区释放时可选的销毁回调（Destroy Callback）。 |
| `_align` | 缓冲区长度和起始地址的对齐要求（Alignment）。 |

<a id="ga90e691e793c964847d737f5ecf7646ec"></a>

### `NET_BUF_POOL_VAR_DEFINE`

```c
#define NET_BUF_POOL_VAR_DEFINE ( _name, _count, _data_size, _ud_size, _destroy )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
_NET_BUF_ARRAY_DEFINE(_name, _count, _ud_size);                        \
K_HEAP_DEFINE(net_buf_mem_pool_##_name, _data_size);                   \
static const struct net_buf_data_alloc net_buf_data_alloc_##_name = {  \
        .cb = &net_buf_var_cb,                                         \
        .alloc_data = &net_buf_mem_pool_##_name,                       \
        .max_alloc_size = 0,                                           \
};                                                                     \
static STRUCT_SECTION_ITERABLE(net_buf_pool, _name) =                  \
        NET_BUF_POOL_INITIALIZER(_name, &net_buf_data_alloc_##_name,   \
                                 _net_buf_##_name, _count, _ud_size,   \
                                 _destroy)
```

定义一个支持可变大小有效载荷（Variable Size Payload）的新缓冲池（Buffer Pool）。

定义 `net_buf_pool` 结构，以及所需数量缓冲区的必要存储空间，即结构数组。之后，可通过 `net_buf_alloc` 从池中获取缓冲区。池定义为静态变量（Static Variable）；如果需要导出到当前模块之外，应借助单独的指针，而不能使用 `extern` 声明。

缓冲区的数据载荷（Data Payload）基于内存池分配，该池支持分配可变大小载荷。

如果提供了自定义销毁回调（Destroy Callback），该回调负责最终调用 `net_buf_destroy()`，完成将缓冲区归还池的过程。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 缓冲池变量名称（Pool Variable Name）。 |
| `_count` | 池中的缓冲区数量（Number of Buffers）。 |
| `_data_size` | 可供数据载荷使用的内存总量（Total Memory）。 |
| `_ud_size` | 每个缓冲区要预留的用户数据空间（User Data Space）。 |
| `_destroy` | 缓冲区释放时可选的销毁回调（Destroy Callback）。 |

<a id="ga0b01dc80027d13b1895379d4d1397207"></a>

### `NET_BUF_SIMPLE`

```c
#define NET_BUF_SIMPLE ( _size)
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
((struct net_buf_simple *)(&(struct {        \
        struct net_buf_simple buf;           \
        uint8_t data[_size];                 \
}) {                                         \
        .buf.size = _size,                   \
}))
```

定义一个位于栈上的 net_buf_simple 变量（Stack Variable），并获取指向它的指针。

此辅助宏（Helper Macro）用于在栈上定义 `net_buf_simple` 对象，并按以下方式取得其指针：

声明示例（Declaration Example）：`struct net_buf_simple *my_buf = NET_BUF_SIMPLE(10);`

创建对象后，需要调用 `net_buf_simple_init()` 进行初始化（Initialization）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_size` | 缓冲区的最大数据存储容量（Maximum Data Storage）。 |

**返回（Returns）**：返回值（Returns）：栈上分配的 `net_buf_simple` 对象的指针。

<a id="gaf85aa0b705bb4fbe2630191fde802501"></a>

### `NET_BUF_SIMPLE_DEFINE`

```c
#define NET_BUF_SIMPLE_DEFINE ( _name, _size )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
uint8_t net_buf_data_##_name[_size];       \
struct net_buf_simple _name = {         \
        .data   = net_buf_data_##_name, \
        .len    = 0,                    \
        .size   = _size,                \
        .__buf  = net_buf_data_##_name, \
}
```

定义一个位于栈上的 net_buf_simple 变量（Stack Variable）。

此辅助宏（Helper Macro）用于在栈上定义 `net_buf_simple` 对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | net_buf_simple 对象名称。 |
| `_size` | 缓冲区的最大数据存储容量（Maximum Data Storage）。 |

<a id="ga21ced8b3082d57bf071008de5fffc0f4"></a>

### `NET_BUF_SIMPLE_DEFINE_STATIC`

```c
#define NET_BUF_SIMPLE_DEFINE_STATIC ( _name, _size )
```

```c
#include <zephyr/net_buf.h>
```

展开值（Value）：

```c
static __noinit uint8_t net_buf_data_##_name[_size]; \
static struct net_buf_simple _name = {            \
        .data   = net_buf_data_##_name,           \
        .len    = 0,                              \
        .size   = _size,                          \
        .__buf  = net_buf_data_##_name,           \
}
```

定义一个静态 net_buf_simple 变量（Static Variable）。

此辅助宏（Helper Macro）用于定义静态 `net_buf_simple` 对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | net_buf_simple 对象名称。 |
| `_size` | 缓冲区的最大数据存储容量（Maximum Data Storage）。 |

<a id="ga9b74d094a45daf74cd230eaa4fcbc065"></a>

### `net_buf_allocator_cb`

```c
typedef struct net_buf *(* net_buf_allocator_cb) (k_timeout_t timeout, void *user_data)
```

```c
#include <zephyr/net_buf.h>
```

网络缓冲区分配器回调（Network Buffer Allocator Callback）。

当 `net_buf_append_bytes` 需要分配新的 `net_buf` 时，会调用分配器回调（Allocator Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `timeout` | 决定网络缓冲池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时（Timeout）。 |
| `user_data` | 调用 `net_buf_append_bytes` 时提供的用户数据（User Data）。 |

**返回（Returns）**：返回值（Returns）：已分配的 `net_buf` 指针；出错时为 `NULL`。

<a id="ga30776d2b21f06d244c083af5c25b0f3e"></a>

### `net_buf_add()`

```c
void * net_buf_add ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

为在缓冲区（Buffer）末尾追加数据做准备。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要为长度增加的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区原来的尾部（Original Tail）。

<a id="ga61878a9bd7462ca925eac39181f2972c"></a>

### `net_buf_add_be16()`

```c
void net_buf_add_be16 ( struct net_buf * buf, uint16_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 16 位值。

在缓冲区末尾添加 16 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 16 位数值（Value）。 |

<a id="ga0f3cd9f9b364a2d2125aea19221d3e1e"></a>

### `net_buf_add_be24()`

```c
void net_buf_add_be24 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 24 位值。

在缓冲区末尾添加 24 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 24 位数值（Value）。 |

<a id="ga5543d00c96f83970f8dbf3670a9dc3fc"></a>

### `net_buf_add_be32()`

```c
void net_buf_add_be32 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 32 位值。

在缓冲区末尾添加 32 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 32 位数值（Value）。 |

<a id="ga70cb98da91de098a92fbd69712c2bde7"></a>

### `net_buf_add_be40()`

```c
void net_buf_add_be40 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 40 位值。

在缓冲区末尾添加 40 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 40 位数值（Value）。 |

<a id="ga8fe6feb191ab338e91bd62f44e184deb"></a>

### `net_buf_add_be48()`

```c
void net_buf_add_be48 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 48 位值。

在缓冲区末尾添加 48 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 48 位数值（Value）。 |

<a id="ga055f6eb7d5fbc9a3cf529a9ed00970c4"></a>

### `net_buf_add_be64()`

```c
void net_buf_add_be64 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 64 位值。

在缓冲区末尾添加 64 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 64 位数值（Value）。 |

<a id="gadd6d01a3b1efd0de16f9bef975809404"></a>

### `net_buf_add_le16()`

```c
void net_buf_add_le16 ( struct net_buf * buf, uint16_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 16 位值。

在缓冲区末尾添加 16 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 16 位数值（Value）。 |

<a id="ga32b90364091ade229830686f03b25d4c"></a>

### `net_buf_add_le24()`

```c
void net_buf_add_le24 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 24 位值。

在缓冲区末尾添加 24 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 24 位数值（Value）。 |

<a id="gae8ba33b6592ef7fd859b35d63b285d87"></a>

### `net_buf_add_le32()`

```c
void net_buf_add_le32 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 32 位值。

在缓冲区末尾添加 32 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 32 位数值（Value）。 |

<a id="ga62790f9644102f4952c250f6513a2ada"></a>

### `net_buf_add_le40()`

```c
void net_buf_add_le40 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 40 位值。

在缓冲区末尾添加 40 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 40 位数值（Value）。 |

<a id="gaf19bf75c3d4d645b1eebf9254aa22790"></a>

### `net_buf_add_le48()`

```c
void net_buf_add_le48 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 48 位值。

在缓冲区末尾添加 48 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 48 位数值（Value）。 |

<a id="gac3f955f8fecc0e5971d2e5e8176e973e"></a>

### `net_buf_add_le64()`

```c
void net_buf_add_le64 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 64 位值。

在缓冲区末尾添加 64 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 64 位数值（Value）。 |

<a id="gacf4e2eba52975ba6728c79274a769d0f"></a>

### `net_buf_add_mem()`

```c
void * net_buf_add_mem ( struct net_buf * buf, const void * mem, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

将指定字节数的数据复制到缓冲区（Buffer）末尾。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `mem` | 待添加数据的位置（Data Location）。 |
| `len` | 待添加数据的长度（Data Length）。 |

**返回（Returns）**：返回值（Returns）：缓冲区原来的尾部（Original Tail）。

<a id="ga868ac2bea103fed568b461cbcd45eda2"></a>

### `net_buf_add_u8()`

```c
uint8_t * net_buf_add_u8 ( struct net_buf * buf, uint8_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加一个 8 位字节。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 待添加的字节值（Byte Value）。 |

**返回（Returns）**：返回值（Returns）：已添加数值的指针。

<a id="ga534366f3b5c7f41a28372c12149ca005"></a>

### `net_buf_alloc()`

```c
struct net_buf * net_buf_alloc ( struct net_buf_pool * pool, k_timeout_t timeout )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 从哪个池（Pool）分配缓冲区。 |
| `timeout` | 决定池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时。注意，某些数据分配器不支持阻塞（Blocking），例如 `HEAP` 类型；此时即便传入 `K_FOREVER`，`net_buf_alloc()` 仍可能失败并返回 `NULL`。 |

**返回（Returns）**：返回值（Returns）：新缓冲区；缓冲区耗尽时为 `NULL`。

<a id="ga686df794ec6881625b54454a33587bab"></a>

### `net_buf_alloc_fixed()`

```c
struct net_buf * net_buf_alloc_fixed ( struct net_buf_pool * pool, k_timeout_t timeout )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲池（Pool）分配一个新的固定大小缓冲区（Fixed Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 从哪个池（Pool）分配缓冲区。 |
| `timeout` | 决定池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时。注意，某些数据分配器不支持阻塞（Blocking），例如 `HEAP` 类型；此时即便传入 `K_FOREVER`，`net_buf_alloc()` 仍可能失败并返回 `NULL`。 |

**返回（Returns）**：返回值（Returns）：新缓冲区；缓冲区耗尽时为 `NULL`。

<a id="ga11d489aedcca82117965fa6ba9d11ca5"></a>

### `net_buf_alloc_len()`

```c
struct net_buf * net_buf_alloc_len ( struct net_buf_pool * pool, size_t size, k_timeout_t timeout )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲池（Pool）分配一个新的变长缓冲区（Variable Length Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 从哪个池（Pool）分配缓冲区。 |
| `size` | 缓冲区必须能够容纳的数据量（Data Size）。 |
| `timeout` | 决定池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时。注意，某些数据分配器不支持阻塞（Blocking），例如 `HEAP` 类型；此时即便传入 `K_FOREVER`，`net_buf_alloc()` 仍可能失败并返回 `NULL`。 |

**返回（Returns）**：返回值（Returns）：新缓冲区；缓冲区耗尽时为 `NULL`。

<a id="ga8c24d0761d6d38facb6cca60c7c13c0c"></a>

### `net_buf_alloc_with_data()`

```c
struct net_buf * net_buf_alloc_with_data ( struct net_buf_pool * pool, void * data, size_t size, k_timeout_t timeout )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲池（Pool）分配一个新缓冲区，使用外部数据指针（External Data Pointer）。

从池中分配新缓冲区，但数据指针由用户提供，而非来自池。缓冲区初始就包含 `size` 字节数据，且没有尾部余量（Tailroom）。数据不会随缓冲区一同释放；只要缓冲区仍然存在，数据就必须保持有效。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 从哪个池（Pool）分配缓冲区。 |
| `data` | 外部数据指针（External Data Pointer）。 |
| `size` | 所指数据缓冲区能够容纳的数据量（Data Capacity）。 |
| `timeout` | 决定池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时。注意，某些数据分配器不支持阻塞（Blocking），例如 `HEAP` 类型；此时即便传入 `K_FOREVER`，`net_buf_alloc()` 仍可能失败并返回 `NULL`。 |

**返回（Returns）**：返回值（Returns）：新缓冲区；缓冲区耗尽时为 `NULL`。

<a id="ga646d680491753b3ed29fa83c26732d1a"></a>

### `net_buf_append_bytes()`

```c
size_t net_buf_append_bytes ( struct net_buf * buf, size_t len, const void * value, k_timeout_t timeout, net_buf_allocator_cb allocate_cb, void * user_data )
```

```c
#include <zephyr/net_buf.h>
```

向 net_buf 列表追加数据（Append Data）。

向 `net_buf` 追加数据（Append Data）。如果空间不足，会继续添加更多 `net_buf`，除非已无空闲 `net_buf` 且发生超时。如果未提供分配器，将尝试从原缓冲区所在的同一个池中分配。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 网络缓冲区（Network Buffer）。 |
| `len` | 输入数据总长度（Total Input Length）。 |
| `value` | 待添加的数据（Data）。 |
| `timeout` | 每次分配新片段（Fragment）的超时，并非整个函数调用的总超时。该值传递给 `net_buf` 分配器回调。 |
| `allocate_cb` | 需要新的 `net_buf` 时，使用此回调（Callback）。 |
| `user_data` | 要提供给 `allocate_cb` 的用户数据指针（User Data Pointer）。此指针可以指向 `mem_pool`、`net_pkt` 或其他任意对象，具体逻辑由 `allocate_cb` 决定。 |

**返回（Returns）**：返回值（Returns）：实际添加的数据长度。如果无法分配新片段，返回值小于输入长度。即便使用 `K_FOREVER` 也可能发生这种情况，因为某些数据分配器不等待，例如 `HEAP` 类型。

<a id="gaf4d80e2878e3c790fff206bec820f03f"></a>

### `net_buf_clone()`

```c
struct net_buf * net_buf_clone ( struct net_buf * buf, k_timeout_t timeout )
```

```c
#include <zephyr/net_buf.h>
```

克隆缓冲区（Clone Buffer）。

复制给定缓冲区，包括当前保存的全部用户数据及其他数据和头部（Headers）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |
| `timeout` | 决定池为空时的行为：`K_NO_WAIT` 表示立即返回；`K_FOREVER` 表示一直等待到可用；其他值表示等待至指定超时（Timeout）。 |

**返回（Returns）**：返回值（Returns）：克隆的缓冲区（Cloned Buffer）；缓冲区耗尽时为 `NULL`。

<a id="gaef938c3ab676a5bd5bf8338b8d7cb30c"></a>

### `net_buf_data_match()`

```c
size_t net_buf_data_match ( const struct net_buf * buf, size_t offset, const void * data, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

将数据与 net_buf 的内容进行匹配（Match）。

比较给定数据与 `net_buf` 内容，提供两者匹配的字节数量。必要时遍历多个缓冲区片段（Buffer Fragments）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 网络缓冲区（Network Buffer）。 |
| `offset` | 开始比较的偏移量（Offset）。 |
| `data` | 用于比较的数据缓冲区（Data Buffer）。 |
| `len` | 要比较的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：遇到第一个差异之前，已比较的字节数量。

<a id="ga739249547eb37b839b3c1ebdbcb88d28"></a>

### `net_buf_destroy()`

```c
void net_buf_destroy ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从自定义销毁回调（Custom Destroy Callback）中销毁缓冲区。

此辅助函数仅供自定义销毁回调（Destroy Callback）使用。如果未向 `NET_BUF_POOL_*_DEFINE()` 提供自定义销毁回调，则无需使用此 API。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要销毁的缓冲区（Buffer）。 |

<a id="ga6b43ad0740b23c0544d706c77c9f1e13"></a>

### `net_buf_drop()`

```c
void net_buf_drop ( struct net_buf ** orig)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

释放缓冲区引用（Buffer Reference），并清空指针。

对 `orig` 执行原子交换（Atomic Exchange），将其设为 `NULL`；如果原值不是 `NULL`，则释放原值的一次引用（Unreference）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `orig` | 指向待丢弃缓冲区指针的指针；返回时该缓冲区指针被设为 `NULL`。 |

<a id="ga0d7e310802a2bc7b2078f9310827535f"></a>

### `net_buf_frag_add()`

```c
struct net_buf * net_buf_frag_add ( struct net_buf * head, struct net_buf * frag )
```

```c
#include <zephyr/net_buf.h>
```

将新分片（Fragment）追加到缓冲区链（Chain of Buffers）末尾。

向缓冲区片段列表（Buffer Fragments List）追加新片段。

注意（Note）：如果 `head` 非 `NULL`，此函数接管片段引用的所有权（Ownership），调用方无需再释放该引用。如果 `head` 为 `NULL`，则返回带有一个新引用的 `frag`，调用方仍保留自己原有的引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `head` | 片段链（Fragment Chain）的头部。 |
| `frag` | 要添加的分片（Fragment）。 |

**返回（Returns）**：返回值（Returns）：片段链的新头部。若 `head` 原本非 `NULL`，则为 `head`；若原本为 `NULL`，则为 `frag`。

<a id="ga602a99833bd401a0ada5bd5defa7a2ff"></a>

### `net_buf_frag_del()`

```c
struct net_buf * net_buf_frag_del ( struct net_buf * parent, struct net_buf * frag )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区链（Chain of Buffers）中删除现有分片（Fragment）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `parent` | 父缓冲区／片段（Parent Buffer/Fragment）；没有父项时为 `NULL`。 |
| `frag` | 要删除的分片（Fragment）。 |

**返回（Returns）**：返回值（Returns）：该片段之后的缓冲区指针；没有后续片段时为 `NULL`。

<a id="gac032b44db4a845dba8303fecfe1b63e7"></a>

### `net_buf_frag_insert()`

```c
void net_buf_frag_insert ( struct net_buf * parent, struct net_buf * frag )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区链（Chain of Buffers）插入新分片（Fragment）。

在缓冲区片段列表（Buffer Fragments List）中，将新片段插入父项之后。

注意（Note）：此函数接管片段引用的所有权（Ownership），调用方无需再释放该引用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `parent` | 父缓冲区／片段（Parent Buffer/Fragment）。 |
| `frag` | 要插入的分片（Fragment）。 |

<a id="ga042ce3f2e7e3fd0948ca2623fff36746"></a>

### `net_buf_frag_last()`

```c
struct net_buf * net_buf_frag_last ( struct net_buf * frags)
```

```c
#include <zephyr/net_buf.h>
```

在分片列表（Fragment List）中查找最后一个分片。

**返回（Returns）**：返回值（Returns）：列表最后一个片段的指针。

<a id="gaebb95f08dbd4d38a250170aa78ddeb44"></a>

### `net_buf_frags_len()`

```c
size_t net_buf_frags_len ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

计算分片（Fragment）中存储的字节数。

计算给定缓冲区及其链接片段（Linked Fragments）中保存的数据总量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 开始计算的缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区及其片段中的字节数量。

<a id="ga9cd6d30ea47a91647d3c4a60d82b5cd4"></a>

### `net_buf_get_available()`

```c
size_t net_buf_get_available ( struct net_buf_pool * pool)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

获取当前可从缓冲池（Pool）申领的缓冲区数量。

注意，如果其他线程也在从池中分配或释放缓冲区，那么此函数返回时，可用缓冲区数量（Available Buffers）可能已经改变。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要检查的池（Pool）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_NET_BUF_POOL_USAGE` 时可用。

**返回（Returns）**：返回值（Returns）：池中当前可用的缓冲区数量。

<a id="gad652ef7d2895f8077c366a564b785291"></a>

### `net_buf_get_max_used()`

```c
size_t net_buf_get_max_used ( struct net_buf_pool * pool)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

获取从缓冲池（Pool）同时申领的缓冲区数量峰值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `pool` | 要检查的池（Pool）。 |

**注意（Attention）**：注意（Attention）：仅在启用 Kconfig 选项 `CONFIG_NET_BUF_POOL_USAGE` 时可用。

**返回（Returns）**：返回值（Returns）：曾同时从池中占用的缓冲区最大数量。

<a id="gac9a09897f44e708f920064826aa2f703"></a>

### `net_buf_headroom()`

```c
size_t net_buf_headroom ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区的头部预留空间（Headroom）。

检查缓冲区开头有多少空闲空间（Free Space）。

`buf`：指向缓冲区的有效指针（Valid Pointer）。

**返回（Returns）**：返回值（Returns）：缓冲区开头可用的字节数量。

<a id="gacdf048dc0afc7ef67027117e0d51d3a3"></a>

### `net_buf_id()`

```c
int net_buf_id ( const struct net_buf * buf)
```

```c
#include <zephyr/net_buf.h>
```

获取缓冲区从零开始的索引（Zero-based Index）。

此函数根据缓冲区在所属缓冲池中的位置，将其转换为从零开始的索引（Zero-based Index）。如果要将外部元数据上下文数组（Metadata Context Array）与池中的缓冲区关联，此索引会很有用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 网络缓冲区（Network Buffer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区的从零开始索引（Zero-based Index）。

<a id="ga8d258ef1e4241c438a726486bc7fe766"></a>

### `net_buf_is_valid()`

```c
bool net_buf_is_valid ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区（Buffer）的长度与指针是否自洽。

检查缓冲区是否仍被引用，即 `net_buf::ref` 非零、尚未归还池，并检查其底层 `net_buf_simple` 是否通过 `net_buf_simple_is_valid()`。可在实际使用前作为防护，例如发送前或复制出 `len` 字节前，从而丢弃已释放或损坏的缓冲区，避免越界访问（Out-of-bounds Access）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要验证的缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区仍被引用且内部状态自洽（Self-consistent）时为 `true`，否则为 `false`。

<a id="gaffd49f2de8e72d5f7585b4e5167923d8"></a>

### `net_buf_linearize()`

```c
size_t net_buf_linearize ( void * dst, size_t dst_len, const struct net_buf * src, size_t offset, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从 net_buf 链的指定偏移量（Offset）开始，将字节复制到线性缓冲区（Linear Buffer）。

从源 `net_buf` 链 `src` 的 `offset` 偏移处，复制／提取 `len` 字节到线性缓冲区（Linear Buffer）`dst`。返回实际复制的字节数。如果源链数据不足或目标缓冲区过小，该数量可能少于请求值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 目标缓冲区。 |
| `dst_len` | 目标缓冲区长度。 |
| `src` | 源 `net_buf` 链（Source Chain）。 |
| `offset` | 开始复制的偏移量（Offset）。 |
| `len` | 要复制的字节数。 |

**返回（Returns）**：返回值（Returns）：实际复制的字节数。

<a id="ga65924b8234c91dfc09069ba06242a6b7"></a>

### `net_buf_max_len()`

```c
uint16_t net_buf_max_len ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查 net_buf::len 的最大值。

此值取决于为头部余量（Headroom）预留的字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**已弃用（Deprecated）**：已弃用（Deprecated）：使用 `net_buf_tailroom()` 查询末尾还可添加多少数据，使用 `net_buf_headroom()` 查询开头还可压入多少数据。从 `net_buf::data` 开始的暂用区域大小为 `net_buf::len` 加尾部余量（Tailroom）。

**返回（Returns）**：返回值（Returns）：`net_buf::data` 指针后方可用的字节数。

<a id="ga145f4b2de7548814eaa7ba86fb123989"></a>

### `net_buf_pool_get()`

```c
struct net_buf_pool * net_buf_pool_get ( int id)
```

```c
#include <zephyr/net_buf.h>
```

根据 ID 查找缓冲池（Pool）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `id` | 池标识符（Pool ID），例如来自 `buf->pool_id`。 |

**返回（Returns）**：返回值（Returns）：池的指针。

<a id="gaef433d92734dd8691c292abdb823ba0e"></a>

### `net_buf_pull()`

```c
void * net_buf_pull ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除数据。

通过修改数据指针和缓冲区长度，从缓冲区开头移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="ga97909a33c374a5c757fd2faf582139b7"></a>

### `net_buf_pull_be16()`

```c
uint16_t net_buf_pull_be16 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 16 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 16 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga8de937e8775879712ea0acbf60327a95"></a>

### `net_buf_pull_be24()`

```c
uint32_t net_buf_pull_be24 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 24 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 24 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="ga5f8f2e2244eb574b3e57d09d85412967"></a>

### `net_buf_pull_be32()`

```c
uint32_t net_buf_pull_be32 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 32 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 32 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="ga050bdaccaec842482a02b096aa0c999f"></a>

### `net_buf_pull_be40()`

```c
uint64_t net_buf_pull_be40 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 40 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 40 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="ga68934e105c4b3a8e27aa61b3ec5526db"></a>

### `net_buf_pull_be48()`

```c
uint64_t net_buf_pull_be48 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 48 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 48 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga3c1e80741a49691e69e57c891d3edb05"></a>

### `net_buf_pull_be64()`

```c
uint64_t net_buf_pull_be64 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 64 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 64 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="gaed64e9f2b969f2c0d99cd281e73c860a"></a>

### `net_buf_pull_le16()`

```c
uint16_t net_buf_pull_le16 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 16 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 16 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga85c505321484a50ed9422f24934ed077"></a>

### `net_buf_pull_le24()`

```c
uint32_t net_buf_pull_le24 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 24 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 24 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="ga5f051078f1ffcc40e9ad40e7545a084f"></a>

### `net_buf_pull_le32()`

```c
uint32_t net_buf_pull_le32 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 32 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 32 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="ga36b27c6373eb245f777164065386d100"></a>

### `net_buf_pull_le40()`

```c
uint64_t net_buf_pull_le40 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 40 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 40 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="ga7eeee45b6639146d1492f92263ee4f51"></a>

### `net_buf_pull_le48()`

```c
uint64_t net_buf_pull_le48 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 48 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 48 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga9a3df35e2287cbcfe1b60e2efa52c64e"></a>

### `net_buf_pull_le64()`

```c
uint64_t net_buf_pull_le64 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 64 位数据。

与 `net_buf_pull()` 的思路相同，是用于操作 64 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="gaedc5ffe19bb0ec438e633023c3c5de74"></a>

### `net_buf_pull_mem()`

```c
void * net_buf_pull_mem ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除数据。

通过修改数据指针和缓冲区长度，从缓冲区开头移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据原起始位置的指针。

<a id="ga71bb306d2ce459a60a8c3fc6dac54c90"></a>

### `net_buf_pull_u8()`

```c
uint8_t net_buf_pull_u8 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除一个 8 位值。

与 `net_buf_pull()` 的思路相同，是用于操作 8 位数值（8-bit Values）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：已移除的 8 位数值。

<a id="ga96a2b1f07f3a7958057d9c7cc1f01b73"></a>

### `net_buf_push()`

```c
void * net_buf_push ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

为在缓冲区（Buffer）起始位置添加数据做准备。

修改数据指针和缓冲区长度，使其包含缓冲区开头新增的数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要在开头添加的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="ga6dd756ff8332d076f5d37c69e6c534b5"></a>

### `net_buf_push_be16()`

```c
void net_buf_push_be16 ( struct net_buf * buf, uint16_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 16 位值。

在缓冲区开头添加 16 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 16 位数值（Value）。 |

<a id="ga87338399d8ecd64a894908ed4a2f710b"></a>

### `net_buf_push_be24()`

```c
void net_buf_push_be24 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 24 位值。

在缓冲区开头添加 24 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 24 位数值（Value）。 |

<a id="gae4e64a23708ed910fb6c3ab8ba481a4c"></a>

### `net_buf_push_be32()`

```c
void net_buf_push_be32 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 32 位值。

在缓冲区开头添加 32 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 32 位数值（Value）。 |

<a id="ga512f84e686ff70a5589557575ccda1f8"></a>

### `net_buf_push_be40()`

```c
void net_buf_push_be40 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 40 位值。

在缓冲区开头添加 40 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 40 位数值（Value）。 |

<a id="gabfbcb051019ff210cc2b85adcf4bc821"></a>

### `net_buf_push_be48()`

```c
void net_buf_push_be48 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 48 位值。

在缓冲区开头添加 48 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 48 位数值（Value）。 |

<a id="ga43ff5faab0b099a355b9b96b7b0e3d8c"></a>

### `net_buf_push_be64()`

```c
void net_buf_push_be64 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 64 位值。

在缓冲区开头添加 64 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 64 位数值（Value）。 |

<a id="gab6c84c6846c06c2b339bc88df35e2655"></a>

### `net_buf_push_le16()`

```c
void net_buf_push_le16 ( struct net_buf * buf, uint16_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 16 位值。

在缓冲区开头添加 16 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 16 位数值（Value）。 |

<a id="ga87524ac50e53ba59c6692af10cf001b9"></a>

### `net_buf_push_le24()`

```c
void net_buf_push_le24 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 24 位值。

在缓冲区开头添加 24 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 24 位数值（Value）。 |

<a id="ga97c9046185d6a1e9235bf6914c72dfc4"></a>

### `net_buf_push_le32()`

```c
void net_buf_push_le32 ( struct net_buf * buf, uint32_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 32 位值。

在缓冲区开头添加 32 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 32 位数值（Value）。 |

<a id="gaefab4a755cf4fb7d2b4a142a9351c189"></a>

### `net_buf_push_le40()`

```c
void net_buf_push_le40 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 40 位值。

在缓冲区开头添加 40 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 40 位数值（Value）。 |

<a id="ga852654f7e59951bf3536e3f4e98761bf"></a>

### `net_buf_push_le48()`

```c
void net_buf_push_le48 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 48 位值。

在缓冲区开头添加 48 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 48 位数值（Value）。 |

<a id="gad4ee42b023881f80211fbeca53a0f25d"></a>

### `net_buf_push_le64()`

```c
void net_buf_push_le64 ( struct net_buf * buf, uint64_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 64 位值。

在缓冲区开头添加 64 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 64 位数值（Value）。 |

<a id="ga7e9daccec8cae1b9bfda52b0758adf0c"></a>

### `net_buf_push_mem()`

```c
void * net_buf_push_mem ( struct net_buf * buf, const void * mem, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

将指定字节数的数据复制到缓冲区（Buffer）起始位置。

修改数据指针和缓冲区长度，使其包含缓冲区开头新增的数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `mem` | 待添加数据的位置（Data Location）。 |
| `len` | 待添加数据的长度（Data Length）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="ga9093202ba0a22bfa519bbe32d4585186"></a>

### `net_buf_push_u8()`

```c
void net_buf_push_u8 ( struct net_buf * buf, uint8_t val )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 8 位值。

在缓冲区开头添加 8 位数值（8-bit Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 8 位数值（Value）。 |

<a id="ga29387b2a672bf2bb8739046a46f3601f"></a>

### `net_buf_ref()`

```c
struct net_buf * net_buf_ref ( struct net_buf * buf)
```

```c
#include <zephyr/net_buf.h>
```

递增缓冲区的引用计数（Reference Count）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：新增加了引用的缓冲区。

<a id="ga5da86c8ea703ab3f01c408cce73b0651"></a>

### `net_buf_remove_be16()`

```c
uint16_t net_buf_remove_be16 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 16 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 16 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga6f346a9af570528d238592851240fd74"></a>

### `net_buf_remove_be24()`

```c
uint32_t net_buf_remove_be24 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 24 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 24 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="gacce707d646d7008ec3167af1a0b20da8"></a>

### `net_buf_remove_be32()`

```c
uint32_t net_buf_remove_be32 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 32 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 32 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="gae2920eab3c56d0d462811b83961df466"></a>

### `net_buf_remove_be40()`

```c
uint64_t net_buf_remove_be40 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 40 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 40 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="gaab0e3bcc21c958c01ef076cd0efe087c"></a>

### `net_buf_remove_be48()`

```c
uint64_t net_buf_remove_be48 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 48 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 48 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga8b9edd213da2d48dfb8d70a8d307ba13"></a>

### `net_buf_remove_be64()`

```c
uint64_t net_buf_remove_be64 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 64 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 64 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="gaaf654110fb6a8bdfc27433945d4d1308"></a>

### `net_buf_remove_le16()`

```c
uint16_t net_buf_remove_le16 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 16 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 16 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga903f59c8dea1b2c54969b567fe315041"></a>

### `net_buf_remove_le24()`

```c
uint32_t net_buf_remove_le24 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 24 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 24 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="gae9321a469cc751c58cfb532afd57d265"></a>

### `net_buf_remove_le32()`

```c
uint32_t net_buf_remove_le32 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 32 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 32 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="ga57150a1ba09b28e5c3b04bdefce7ed8e"></a>

### `net_buf_remove_le40()`

```c
uint64_t net_buf_remove_le40 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 40 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 40 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="ga0c147d9f95e2224696a8ace26f63a300"></a>

### `net_buf_remove_le48()`

```c
uint64_t net_buf_remove_le48 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 48 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 48 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga447b9c6be3fe04a50eb35dd29f190b6d"></a>

### `net_buf_remove_le64()`

```c
uint64_t net_buf_remove_le64 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 64 位数据。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 64 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="gace5ad98eac4772db3b0fa2181912f1f0"></a>

### `net_buf_remove_mem()`

```c
void * net_buf_remove_mem ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除数据。

通过修改缓冲区长度，从缓冲区末尾移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新结束位置。

<a id="gad954b9f37790d5e7087db7db7bdedd41"></a>

### `net_buf_remove_u8()`

```c
uint8_t net_buf_remove_u8 ( struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除一个 8 位值。

与 `net_buf_remove_mem()` 的思路相同，是用于操作 8 位数值（8-bit Values）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：已移除的 8 位数值。

<a id="ga8ac58ad4f73b498bef2ff3ac7e30c6c3"></a>

### `net_buf_reserve()`

```c
void net_buf_reserve ( struct net_buf * buf, size_t reserve )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

使用给定的头部预留空间（Headroom）初始化缓冲区。

调用此 API 时，缓冲区应不含任何数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要初始化的缓冲区（Buffer）。 |
| `reserve` | 要预留多少头部余量（Headroom）。 |

<a id="ga1292f38b096fd80e31889aff44b0c021"></a>

### `net_buf_reset()`

```c
void net_buf_reset ( struct net_buf * buf)
```

```c
#include <zephyr/net_buf.h>
```

重置缓冲区（Buffer）。

重置缓冲区数据及标志（Flags），以便复用于其他用途。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 待重置的缓冲区。 |

<a id="ga1906e637c848948f5780428a99b3341e"></a>

### `net_buf_simple_add()`

```c
void * net_buf_simple_add ( struct net_buf_simple * buf, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

为在缓冲区（Buffer）末尾追加数据做准备。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要为长度增加的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区原来的尾部（Original Tail）。

<a id="ga910f2b9df58fb0706aa40e3b80f235aa"></a>

### `net_buf_simple_add_be16()`

```c
void net_buf_simple_add_be16 ( struct net_buf_simple * buf, uint16_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 16 位值。

在缓冲区末尾添加 16 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 16 位数值（Value）。 |

<a id="ga5eb09afeff062af577094d2d3f5fdec8"></a>

### `net_buf_simple_add_be24()`

```c
void net_buf_simple_add_be24 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 24 位值。

在缓冲区末尾添加 24 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 24 位数值（Value）。 |

<a id="gaac5cd20776d8e7bb4db77cbe5366373c"></a>

### `net_buf_simple_add_be32()`

```c
void net_buf_simple_add_be32 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 32 位值。

在缓冲区末尾添加 32 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 32 位数值（Value）。 |

<a id="ga69bdaf4373693bb468cf3876e9edf239"></a>

### `net_buf_simple_add_be40()`

```c
void net_buf_simple_add_be40 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 40 位值。

在缓冲区末尾添加 40 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 40 位数值（Value）。 |

<a id="gadb433fb4a1a61702c0615359a4340171"></a>

### `net_buf_simple_add_be48()`

```c
void net_buf_simple_add_be48 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 48 位值。

在缓冲区末尾添加 48 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 48 位数值（Value）。 |

<a id="ga8e31a7b6537d7634e346236534d2a6d0"></a>

### `net_buf_simple_add_be64()`

```c
void net_buf_simple_add_be64 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 64 位值。

在缓冲区末尾添加 64 位大端字节序（Big-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 64 位数值（Value）。 |

<a id="gaa2daf3b20074ff1a23806ce88becebf5"></a>

### `net_buf_simple_add_le16()`

```c
void net_buf_simple_add_le16 ( struct net_buf_simple * buf, uint16_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 16 位值。

在缓冲区末尾添加 16 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 16 位数值（Value）。 |

<a id="gaf1a89eb15eed79003412ba5a32a35cf6"></a>

### `net_buf_simple_add_le24()`

```c
void net_buf_simple_add_le24 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 24 位值。

在缓冲区末尾添加 24 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 24 位数值（Value）。 |

<a id="ga3bf1bcff840dddd721f2c49ef0ed7c56"></a>

### `net_buf_simple_add_le32()`

```c
void net_buf_simple_add_le32 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 32 位值。

在缓冲区末尾添加 32 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 32 位数值（Value）。 |

<a id="ga67da71ba5942cc11e95aa5ba02cb8552"></a>

### `net_buf_simple_add_le40()`

```c
void net_buf_simple_add_le40 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 40 位值。

在缓冲区末尾添加 40 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 40 位数值（Value）。 |

<a id="ga5be8c9f33df5b31c15df193a7116ce25"></a>

### `net_buf_simple_add_le48()`

```c
void net_buf_simple_add_le48 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 48 位值。

在缓冲区末尾添加 48 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 48 位数值（Value）。 |

<a id="ga79dc411da328b847dcf1903d71eaf011"></a>

### `net_buf_simple_add_le64()`

```c
void net_buf_simple_add_le64 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加 64 位值。

在缓冲区末尾添加 64 位小端字节序（Little-endian）数值，并增加缓冲区的数据长度，以包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要添加的 64 位数值（Value）。 |

<a id="gac37209c1e5097e5610860943fb7d0115"></a>

### `net_buf_simple_add_mem()`

```c
void * net_buf_simple_add_mem ( struct net_buf_simple * buf, const void * mem, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从内存复制指定字节数的数据到缓冲区（Buffer）末尾。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `mem` | 待添加数据的位置（Data Location）。 |
| `len` | 待添加数据的长度（Data Length）。 |

**返回（Returns）**：返回值（Returns）：缓冲区原来的尾部（Original Tail）。

<a id="ga8ff9344b8d8deba1b72b8fca048a525c"></a>

### `net_buf_simple_add_u8()`

```c
uint8_t * net_buf_simple_add_u8 ( struct net_buf_simple * buf, uint8_t val )
```

```c
#include <zephyr/net_buf.h>
```

在缓冲区（Buffer）末尾追加一个 8 位字节。

增加缓冲区的数据长度（Data Length），使其包含末尾新增的数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 待添加的字节值（Byte Value）。 |

**返回（Returns）**：返回值（Returns）：已添加数值的指针。

<a id="ga0186c153b72a379affdd3e2e3994b5a7"></a>

### `net_buf_simple_clone()`

```c
void net_buf_simple_clone ( const struct net_buf_simple * original, struct net_buf_simple * clone )
```

```c
#include <zephyr/net_buf.h>
```

克隆缓冲区状态（Buffer State），共用同一个数据缓冲区。

初始化一个缓冲区，使其指向与现有缓冲区相同的数据。这样可以操作同一份数据，而不改变原缓冲区的长度（Length）与偏移量（Offset）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `original` | 要克隆的缓冲区（Buffer）。 |
| `clone` | 新的克隆对象（Clone）。 |

<a id="gadc6ae86245c2a2607c671a524227b026"></a>

### `net_buf_simple_headroom()`

```c
size_t net_buf_simple_headroom ( const struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区的头部预留空间（Headroom）。

检查缓冲区开头有多少空闲空间（Free Space）。

`buf`：指向缓冲区的有效指针（Valid Pointer）。

**返回（Returns）**：返回值（Returns）：缓冲区开头可用的字节数量。

<a id="ga040279b601191367dee013bab9916d8d"></a>

### `net_buf_simple_init()`

```c
void net_buf_simple_init ( struct net_buf_simple * buf, size_t reserve_head )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

初始化 net_buf_simple 对象（Object）。

使用 `NET_BUF_SIMPLE` 宏创建 `net_buf_simple` 对象后，需要调用此函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要初始化的缓冲区（Buffer）。 |
| `reserve_head` | 要预留的头部余量（Headroom）。 |

<a id="ga7fac47a2a25eaca39c5d14f1f55b485d"></a>

### `net_buf_simple_init_with_data()`

```c
void net_buf_simple_init_with_data ( struct net_buf_simple * buf, void * data, size_t size )
```

```c
#include <zephyr/net_buf.h>
```

使用数据初始化 net_buf_simple 对象（Object）。

使用外部数据（External Data）初始化的缓冲区对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要初始化的缓冲区（Buffer）。 |
| `data` | 外部数据指针（External Data Pointer）。 |
| `size` | 所指数据缓冲区能够容纳的数据量（Data Capacity）。 |

<a id="ga5c4038cb3aa506c3cad7a2505392aa50"></a>

### `net_buf_simple_is_valid()`

```c
bool net_buf_simple_is_valid ( const struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区（Buffer）的长度与指针是否自洽。

验证正常缓冲区必须始终满足的不变量（Invariant）：`data` 指向后备存储（Backing Storage）内部，且 `len` 不得延伸到该存储末尾之外。如果 `net_buf_simple::len` 已损坏，例如回绕成很大的值，或 `net_buf_simple::data` 被移到 `__buf..__buf+size` 范围之外，缓冲区将无法通过此检查。

此检查不会、也无法检测被改成其他合法范围内数值的 `len`；它仅检测越界损坏（Out-of-bounds Corruption），因为使用缓冲区时，此类损坏会造成越界读写。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要验证的缓冲区（Buffer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区内部状态自洽（Self-consistent）时为 `true`，否则为 `false`。

<a id="ga7476ec7222d074e7dc9783e7ed9cd800"></a>

### `net_buf_simple_max_len()`

```c
uint16_t net_buf_simple_max_len ( const struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查 net_buf_simple::len 的最大值。

此值取决于为头部余量（Headroom）预留的字节数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**已弃用（Deprecated）**：已弃用（Deprecated）：使用 `net_buf_simple_tailroom()` 查询末尾还可添加多少数据，使用 `net_buf_simple_headroom()` 查询开头还可压入多少数据。从 `net_buf_simple::data` 开始的暂用区域大小为 `net_buf_simple::len` 加尾部余量（Tailroom）。

**返回（Returns）**：返回值（Returns）：`net_buf_simple::data` 指针后方可用的字节数。

<a id="gaf5ab4a5fe4a6226be72a510fea0ed8a8"></a>

### `net_buf_simple_pull()`

```c
void * net_buf_simple_pull ( struct net_buf_simple * buf, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除数据。

通过修改数据指针和缓冲区长度，从缓冲区开头移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="gae36458ba05a4ab89e429be4cfd264440"></a>

### `net_buf_simple_pull_be16()`

```c
uint16_t net_buf_simple_pull_be16 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 16 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 16 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga4c24d445d6b75c850a9e95fb242a50e1"></a>

### `net_buf_simple_pull_be24()`

```c
uint32_t net_buf_simple_pull_be24 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 24 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 24 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="ga1a53892ed75f994bbbb3a2bcf1743d3c"></a>

### `net_buf_simple_pull_be32()`

```c
uint32_t net_buf_simple_pull_be32 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 32 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 32 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="gaa665830dad59ac957f79c7f1cc84aed5"></a>

### `net_buf_simple_pull_be40()`

```c
uint64_t net_buf_simple_pull_be40 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 40 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 40 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="ga19bdefe740fe94a42fba76d71b4ef6e2"></a>

### `net_buf_simple_pull_be48()`

```c
uint64_t net_buf_simple_pull_be48 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 48 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 48 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="gad07f0d49a7db99063077de493e7b0712"></a>

### `net_buf_simple_pull_be64()`

```c
uint64_t net_buf_simple_pull_be64 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 64 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 64 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="gad59d180ae81b55f6d618565a37d25dba"></a>

### `net_buf_simple_pull_le16()`

```c
uint16_t net_buf_simple_pull_le16 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 16 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 16 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga4c9d2ac72a176c49ec224353b5566eb9"></a>

### `net_buf_simple_pull_le24()`

```c
uint32_t net_buf_simple_pull_le24 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 24 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 24 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="ga38df82e6ba9bc2c75133200f7fa75353"></a>

### `net_buf_simple_pull_le32()`

```c
uint32_t net_buf_simple_pull_le32 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 32 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 32 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="gad669c07efe5cb90ebffcc76d9c1029a1"></a>

### `net_buf_simple_pull_le40()`

```c
uint64_t net_buf_simple_pull_le40 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 40 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 40 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="ga69fbfbd72b17783c5ee12b4b2ac9af46"></a>

### `net_buf_simple_pull_le48()`

```c
uint64_t net_buf_simple_pull_le48 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 48 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 48 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga7e0e2d0adbe9062d08f5d8afc7acd89e"></a>

### `net_buf_simple_pull_le64()`

```c
uint64_t net_buf_simple_pull_le64 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除并转换 64 位数据。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 64 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="ga9c676fdbd6e999a9eab26b13d3608e0c"></a>

### `net_buf_simple_pull_mem()`

```c
void * net_buf_simple_pull_mem ( struct net_buf_simple * buf, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除数据。

通过修改数据指针和缓冲区长度，从缓冲区开头移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据原位置的指针。

<a id="ga09a261c615136fd39834cd301fc692e7"></a>

### `net_buf_simple_pull_u8()`

```c
uint8_t net_buf_simple_pull_u8 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）开头移除一个 8 位值。

与 `net_buf_simple_pull()` 的思路相同，是用于操作 8 位数值（8-bit Values）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：已移除的 8 位数值。

<a id="ga64df9754665440370340c6dddde625d1"></a>

### `net_buf_simple_push()`

```c
void * net_buf_simple_push ( struct net_buf_simple * buf, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

为在缓冲区（Buffer）开头添加数据做准备。

修改数据指针和缓冲区长度，使其包含缓冲区开头新增的数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要在开头添加的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="ga827bd85eba0dbd098790d84d22e8e32d"></a>

### `net_buf_simple_push_be16()`

```c
void net_buf_simple_push_be16 ( struct net_buf_simple * buf, uint16_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 16 位值。

在缓冲区开头添加 16 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 16 位数值（Value）。 |

<a id="gabfddd4956ec1e356002a3122fea74b72"></a>

### `net_buf_simple_push_be24()`

```c
void net_buf_simple_push_be24 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 24 位值。

在缓冲区开头添加 24 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 24 位数值（Value）。 |

<a id="gad0c3b8fdeaad6437c3dfcbb03fa52426"></a>

### `net_buf_simple_push_be32()`

```c
void net_buf_simple_push_be32 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 32 位值。

在缓冲区开头添加 32 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 32 位数值（Value）。 |

<a id="gad65bcaf8401e6f5ffff81a998cfb8fe5"></a>

### `net_buf_simple_push_be40()`

```c
void net_buf_simple_push_be40 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 40 位值。

在缓冲区开头添加 40 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 40 位数值（Value）。 |

<a id="ga1ea39c7d7e9ba4e10d31d818e45e192a"></a>

### `net_buf_simple_push_be48()`

```c
void net_buf_simple_push_be48 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 48 位值。

在缓冲区开头添加 48 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 48 位数值（Value）。 |

<a id="gafea2201655955ab004b5f77106998ae9"></a>

### `net_buf_simple_push_be64()`

```c
void net_buf_simple_push_be64 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 64 位值。

在缓冲区开头添加 64 位大端字节序（Big-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 64 位数值（Value）。 |

<a id="ga50cd64438d8f218e3d1ef8b53b7d41a6"></a>

### `net_buf_simple_push_le16()`

```c
void net_buf_simple_push_le16 ( struct net_buf_simple * buf, uint16_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 16 位值。

在缓冲区开头添加 16 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 16 位数值（Value）。 |

<a id="gabe52d6735d835edc361666bb3413b907"></a>

### `net_buf_simple_push_le24()`

```c
void net_buf_simple_push_le24 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 24 位值。

在缓冲区开头添加 24 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 24 位数值（Value）。 |

<a id="ga8662e6bada476c0d48cebea4661b2ac1"></a>

### `net_buf_simple_push_le32()`

```c
void net_buf_simple_push_le32 ( struct net_buf_simple * buf, uint32_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 32 位值。

在缓冲区开头添加 32 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 32 位数值（Value）。 |

<a id="ga745ab6f34138b506b42f78e0975a5d2e"></a>

### `net_buf_simple_push_le40()`

```c
void net_buf_simple_push_le40 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 40 位值。

在缓冲区开头添加 40 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 40 位数值（Value）。 |

<a id="ga66b44897e336f31e3ecbf4717bec274e"></a>

### `net_buf_simple_push_le48()`

```c
void net_buf_simple_push_le48 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 48 位值。

在缓冲区开头添加 48 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 48 位数值（Value）。 |

<a id="ga771634e50e2bf7c291565ce6b2af7e85"></a>

### `net_buf_simple_push_le64()`

```c
void net_buf_simple_push_le64 ( struct net_buf_simple * buf, uint64_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 64 位值。

在缓冲区开头添加 64 位小端字节序（Little-endian）数值。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 64 位数值（Value）。 |

<a id="gaaa838083c610f7426c509efaae69a511"></a>

### `net_buf_simple_push_mem()`

```c
void * net_buf_simple_push_mem ( struct net_buf_simple * buf, const void * mem, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从内存复制指定字节数的数据到缓冲区（Buffer）开头。

修改数据指针和缓冲区长度，使其包含缓冲区开头新增的数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `mem` | 待添加数据的位置（Data Location）。 |
| `len` | 待添加数据的长度（Data Length）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新起始位置。

<a id="ga0f19da70bfc8f597680ee02c21226a77"></a>

### `net_buf_simple_push_u8()`

```c
void net_buf_simple_push_u8 ( struct net_buf_simple * buf, uint8_t val )
```

```c
#include <zephyr/net_buf.h>
```

向缓冲区（Buffer）开头压入 8 位值。

在缓冲区开头添加 8 位数值（8-bit Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `val` | 要压入缓冲区的 8 位数值（Value）。 |

<a id="ga93f9f84845601df4ffc118be1ffd2fee"></a>

### `net_buf_simple_remove_be16()`

```c
uint16_t net_buf_simple_remove_be16 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 16 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 16 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga9b39384162a91d7d07e037a9ada782dd"></a>

### `net_buf_simple_remove_be24()`

```c
uint32_t net_buf_simple_remove_be24 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 24 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 24 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="gae8ecc1fbc9dfc007f1b4e932cfaf2f1d"></a>

### `net_buf_simple_remove_be32()`

```c
uint32_t net_buf_simple_remove_be32 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 32 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 32 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="ga9abd2bccc90cf654556c18322888d131"></a>

### `net_buf_simple_remove_be40()`

```c
uint64_t net_buf_simple_remove_be40 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 40 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 40 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="gab93d22797c3f406179c4c145241d6abb"></a>

### `net_buf_simple_remove_be48()`

```c
uint64_t net_buf_simple_remove_be48 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 48 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 48 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga602fae83e2ecf47552a11f9282619932"></a>

### `net_buf_simple_remove_be64()`

```c
uint64_t net_buf_simple_remove_be64 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 64 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 64 位大端字节序（Big-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从大端字节序（Big-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="ga0b57f9ca2f3837e94cd7862e37efc01c"></a>

### `net_buf_simple_remove_le16()`

```c
uint16_t net_buf_simple_remove_le16 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 16 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 16 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 16 位数值。

<a id="ga4e2fef883228f7de41af3cf90648c3c5"></a>

### `net_buf_simple_remove_le24()`

```c
uint32_t net_buf_simple_remove_le24 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 24 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 24 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 24 位数值。

<a id="ga9e8d016ce384378142fdec6c8dde2457"></a>

### `net_buf_simple_remove_le32()`

```c
uint32_t net_buf_simple_remove_le32 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 32 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 32 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 32 位数值。

<a id="ga2c937164e648fe8b854cb1144051b6b9"></a>

### `net_buf_simple_remove_le40()`

```c
uint64_t net_buf_simple_remove_le40 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 40 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 40 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 40 位数值。

<a id="gac0628bbbe5d9c2b82766d5a17e767696"></a>

### `net_buf_simple_remove_le48()`

```c
uint64_t net_buf_simple_remove_le48 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 48 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 48 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 48 位数值。

<a id="ga560bd7b181c7f08599ae9241b6ce99fd"></a>

### `net_buf_simple_remove_le64()`

```c
uint64_t net_buf_simple_remove_le64 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除并转换 64 位数据。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 64 位小端字节序（Little-endian）数据的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：从小端字节序（Little-endian）转换为主机字节序（Host Endian）的 64 位数值。

<a id="ga8473bdffadc05b22335a321df89f4b83"></a>

### `net_buf_simple_remove_mem()`

```c
void * net_buf_simple_remove_mem ( struct net_buf_simple * buf, size_t len )
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除数据。

通过修改缓冲区长度，从缓冲区末尾移除数据（Remove Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要更新的缓冲区（Buffer）。 |
| `len` | 要移除的字节数（Number of Bytes）。 |

**返回（Returns）**：返回值（Returns）：缓冲区数据的新结束位置。

<a id="gaf508f74e5e050a7294e8a70bd3725fc3"></a>

### `net_buf_simple_remove_u8()`

```c
uint8_t net_buf_simple_remove_u8 ( struct net_buf_simple * buf)
```

```c
#include <zephyr/net_buf.h>
```

从缓冲区（Buffer）末尾移除一个 8 位值。

与 `net_buf_simple_remove_mem()` 的思路相同，是用于操作 8 位数值（8-bit Values）的辅助函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：已移除的 8 位数值。

<a id="ga0e5d3d938becfefc4f4b4d083cb467aa"></a>

### `net_buf_simple_reserve()`

```c
void net_buf_simple_reserve ( struct net_buf_simple * buf, size_t reserve )
```

```c
#include <zephyr/net_buf.h>
```

使用给定的头部预留空间（Headroom）初始化缓冲区。

调用此 API 时，缓冲区应不含任何数据（Data）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要初始化的缓冲区（Buffer）。 |
| `reserve` | 要预留多少头部余量（Headroom）。 |

<a id="ga4b537e913e132448cbf56976504ddddd"></a>

### `net_buf_simple_reset()`

```c
void net_buf_simple_reset ( struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

重置缓冲区（Buffer）。

重置缓冲区数据（Buffer Data），以便复用于其他用途。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 待重置的缓冲区。 |

<a id="gaedd36481657a7a9d108659d56e131721"></a>

### `net_buf_simple_restore()`

```c
void net_buf_simple_restore ( struct net_buf_simple * buf, struct net_buf_simple_state * state )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

恢复缓冲区的解析状态（Parsing State）。

使用先前由 `net_buf_simple_save()` 保存的状态，恢复缓冲区的解析状态（Parsing State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要恢复状态的缓冲区（Buffer）。 |
| `state` | 已保存的状态（Stored State）。 |

<a id="gabf5b098aa0926d9b7fb88baff8a3e2d8"></a>

### `net_buf_simple_save()`

```c
void net_buf_simple_save ( const struct net_buf_simple * buf, struct net_buf_simple_state * state )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

保存缓冲区的解析状态（Parsing State）。

保存缓冲区解析状态（Parsing State），以便稍后恢复。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要保存状态的缓冲区（Buffer）。 |
| `state` | 状态存储空间（State Storage）。 |

<a id="gaaa1f8e7cecbd2fb03b2eb43ff5d4abf8"></a>

### `net_buf_simple_tail()`

```c
uint8_t * net_buf_simple_tail ( const struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

获取缓冲区的尾指针（Tail Pointer）。

获取指向缓冲区数据末尾（End of Data）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 缓冲区。 |

**返回（Returns）**：返回值（Returns）：缓冲区尾指针（Tail Pointer）。

<a id="ga73e2c42fc23e857a46553084b747c996"></a>

### `net_buf_simple_tailroom()`

```c
size_t net_buf_simple_tailroom ( const struct net_buf_simple * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区的尾部剩余空间（Tailroom）。

检查缓冲区末尾有多少空闲空间（Free Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区末尾可用的字节数量。

<a id="ga2d7096280d4fa6f5e32c4674d542889b"></a>

### `net_buf_skip()`

```c
struct net_buf * net_buf_skip ( struct net_buf * buf, size_t len )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

跳过 net_buf 中的 N 个字节（Skip）。

从片段偏移处开始跳过 N 字节。如果数据分布在多个片段（Fragments）中，此函数会逐个跨越片段，直到跳过 N 字节。任何被完整跳过的缓冲区都会从 `net_buf` 列表移除，并释放其引用（Unreference）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 网络缓冲区（Network Buffer）。 |
| `len` | 要跳过的数据总长度（Total Length）。 |

**返回（Returns）**：返回值（Returns）：剩余片段链（Fragment Chain）；全部数据均已跳过时为 `NULL`。

<a id="ga218d4a0c160c57a44946154478724cb3"></a>

### `net_buf_slist_get()`

```c
struct net_buf * net_buf_slist_get ( sys_slist_t * list)
```

```c
#include <zephyr/net_buf.h>
```

从列表（List）获取缓冲区（Buffer）。

修改列表时使用与 `net_buf_slist_put()` 相同的自旋锁（Spinlock）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `list` | 从哪个列表（List）取出缓冲区。 |

**返回（Returns）**：返回值（Returns）：缓冲区；列表为空时为 `NULL`。

<a id="ga6d2dfc45e1e5acf21fe08359a4f92a18"></a>

### `net_buf_slist_put()`

```c
void net_buf_slist_put ( sys_slist_t * list, struct net_buf * buf )
```

```c
#include <zephyr/net_buf.h>
```

将缓冲区（Buffer）放入列表（List）。

修改列表时使用 `net_buf_slist_put()` 和 `net_buf_slist_get()` 共用的自旋锁（Spinlock）。因此，如果一个列表仅通过这两个函数访问，就可以由多个线程和中断处理程序共同使用。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `list` | 将缓冲区追加到哪个列表（List）。 |
| `buf` | 缓冲区。 |

<a id="gaedb10a84b352a3d7716bef979af2ab31"></a>

### `net_buf_tail()`

```c
uint8_t * net_buf_tail ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

获取缓冲区的尾指针（Tail Pointer）。

获取指向缓冲区数据末尾（End of Data）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 缓冲区。 |

**返回（Returns）**：返回值（Returns）：缓冲区尾指针（Tail Pointer）。

<a id="gaecbc6adf16469e3366c88445ea7a553a"></a>

### `net_buf_tailroom()`

```c
size_t net_buf_tailroom ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

检查缓冲区的尾部剩余空间（Tailroom）。

检查缓冲区末尾有多少空闲空间（Free Space）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区末尾可用的字节数量。

<a id="ga4ff24d6ae1aff46e17647ef91db593ca"></a>

### `net_buf_take()`

```c
struct net_buf * net_buf_take ( struct net_buf ** orig)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

移动缓冲区指针（Buffer Pointer），将 orig 设置为 NULL。

对 `orig` 执行原子交换（Atomic Exchange），将其设为 `NULL` 并返回原值。

在引用所有权（Reference Ownership）转移时使用此函数，使原所有者不再持有指向已不归其所有的缓冲区的指针：

原始示例（Example）：

```c
k_fifo_put(&tx_queue, net_buf_take(&buf));
```

仅当被调用函数无条件接管所有权（Ownership）时，将 `net_buf_take(&buf)` 作为参数才是正确的。对于仅在成功时接管所有权的函数，出错时缓冲区仍归调用方，因此调用方必须保留其指针，直到函数返回。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `orig` | 指向待转移缓冲区指针的指针；返回时该缓冲区指针被设为 `NULL`。 |

**返回（Returns）**：返回值（Returns）：`orig` 原来指向的缓冲区。

<a id="gabedcb728bc2fc0c2b5319a8fd87e8273"></a>

### `net_buf_unref()`

```c
void net_buf_unref ( struct net_buf * buf)
```

```c
#include <zephyr/net_buf.h>
```

递减缓冲区的引用计数（Reference Count）。

引用计数（Reference Count）降至零时，将缓冲区归还池。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

<a id="gaf2df457abe3e56d47107b76bdc004756"></a>

### `net_buf_user_data()`

```c
void * net_buf_user_data ( const struct net_buf * buf)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/net_buf.h>
```

获取指向缓冲区用户数据（User Data）的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 指向缓冲区的有效指针（Valid Pointer）。 |

**返回（Returns）**：返回值（Returns）：缓冲区用户数据的指针。

<a id="ga4d1dd56ca8d32d3cfda114fd36761d0d"></a>

### `net_buf_user_data_copy()`

```c
int net_buf_user_data_copy ( struct net_buf * dst, const struct net_buf * src )
```

```c
#include <zephyr/net_buf.h>
```

将用户数据（User Data）从一个缓冲区复制到另一个缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dst` | 指向目标缓冲区的有效指针；其用户数据（User Data）将被覆盖。 |
| `src` | 指向源缓冲区的有效指针；其用户数据（User Data）将被复制。用户数据大小必须大于或等于 `dst` 的用户数据大小。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，失败时为负错误号。


## 1.6\_原页交叉引用（Cross References）

- [net_buf_simple](../network_core_model_reference/P048_net_buf_simple_结构体.md)
- [net_buf_simple_state](../network_core_model_reference/P049_net_buf_simple_state_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [net_buf_pool](../network_core_model_reference/P047_net_buf_pool_结构体.md)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_buf_simple::len](../network_core_model_reference/P048_net_buf_simple_结构体.md#ae8707c50d70c26b53281b40eb1720cf3)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [state](../api_file_reference/P291_zephyr__net__http__parser_state.h_文件参考.md#adc6e5733fc3c22f0a7b2914188c49c90)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [net_buf::len](../network_core_model_reference/P046_net_buf_结构体.md#ae75b7ca728fb7440ea483be8bf88bc38)
- [CONFIG_NET_BUF_HARDENING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_HARDENING)
- [zephyr/net_buf.h](../api_file_coap_phy_reference/P007_zephyr__net_buf.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE](../iterable_reference/P001_可遍历段公共接口.md#ga9104f42cbe4a67a931bed7f7cc8f600f)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [CONFIG_NET_BUF_POOL_USAGE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_BUF_POOL_USAGE)
- [net_buf::ref](../network_core_model_reference/P046_net_buf_结构体.md#a42da518a82f4c37c45814b4f8c5f2731)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000100)
- [net_buf::data](../network_core_model_reference/P046_net_buf_结构体.md#ac6eef59915e7ce167442fdacbbfb5e56)
- [net_buf_simple::data](../network_core_model_reference/P048_net_buf_simple_结构体.md#ad232efff435f425d30ac78f5abf2d8b1)
- [已弃用（Deprecated）。](../api_navigation_reference/P003_弃用接口清单.md#_deprecated000098)
- [k_fifo_put](../queue_reference/P003_FIFO公共接口.md#ga3addb10f86f19e245c23362433d5c913)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__net__buf_html_gacc53824e01db7935bcc9cad564b716cd"></a>
<a id="agroup__iterable__section__apis_html_ga9104f42cbe4a67a931bed7f7cc8f600f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__buf__pool_html"></a>
<a id="astructnet__buf__simple_html"></a>
<a id="astructnet__buf__simple_html_ae8707c50d70c26b53281b40eb1720cf3"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__fifo__apis_html_ga3addb10f86f19e245c23362433d5c913"></a>
<a id="agroup__net__buf_html_ga4ff24d6ae1aff46e17647ef91db593ca"></a>

---

[返回大纲](大纲.md) · [下一章](P002_网络接口抽象层（Network Interface abstraction layer）.md)
