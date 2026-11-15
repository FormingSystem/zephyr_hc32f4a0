---
id: learning.zephyr-docs.network-core-model-reference.page-46
title: net_buf_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_net\_buf\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structnet__buf.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

网络缓冲区（Network Buffer）的表示。

```c
#include <zephyr/net_buf.h>
```

<a id="details"></a>

网络缓冲区（Network Buffer）的表示。此结构用于表示网络缓冲区；通常通过NET_BUF_POOL_*_DEFINE()系列API定义，并通过net_buf_alloc()分配。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 46.1\_数据成员（Data Fields）

<a id="r_a5cc70f57e5b776cfa12b2d556e5958f3"></a>

```c
sys_snode_t node
```

相关声明：[sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)、[node](#a5cc70f57e5b776cfa12b2d556e5958f3)。

允许将缓冲区放入sys_slist_t。

<a id="r_a1fa032cc23854c35eae013020823fa88"></a>

```c
struct net_buf * frags
```

相关声明：[net_buf](P046_net_buf_结构体.md)、[frags](#a1fa032cc23854c35eae013020823fa88)。

与此缓冲区关联的片段（Fragments）。

```c
union {
```

```c
struct {
```

<a id="r_a9c6ff829605ff396423c8a5890ee4c66"></a>

```c
uint8_t ref
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[ref](#a42da518a82f4c37c45814b4f8c5f2731)。

引用计数（Reference Count）。

<a id="r_a32522abf75ba53d9b8d6706d9fa6aab8"></a>

```c
uint8_t flags
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[flags](#aa4fcce2e2894fc5dbd9cc74fc020647e)。

缓冲区标志（Buffer Flags）的位域。

<a id="r_a54ac84ddc76698520598130522993ac7"></a>

```c
uint8_t pool_id
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[pool_id](#a45f294bac054d64034bddcc4c6574d29)。

缓冲区释放后应归还的位置。

<a id="r_a256c40c781af11bb26362290a8b909c8"></a>

```c
uint8_t user_data_size
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[user_data_size](#a65db7bed62d7211114767e6ce58dad75)。

此缓冲区上用户数据（User Data）的大小。

<a id="r_ab682df9333efb5d977ddd51f273362a0"></a>

```c
}
```

<a id="r_acd1c7c21fe5b7a1e0f7ea10140200a1b"></a>

```c
};
```

引用计数（Reference Count），与相邻的三个uint8_t字段flags、pool_id和user_data_size一起，打包到一个atomic_t大小的存储槽中。

```c
union {
```

```c
struct {
```

<a id="r_a82fe72cbed83c49ccda380f49455ccb9"></a>

```c
uint8_t * data
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[data](#ac6eef59915e7ce167442fdacbbfb5e56)。

指向缓冲区数据起点的指针。

<a id="r_a6700ac377416ce71501e6bda67ee62be"></a>

```c
uint16_t len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[len](#ae75b7ca728fb7440ea483be8bf88bc38)。

数据指针（Data Pointer）之后的数据长度。

<a id="r_a2d4031c6a346bf50da0bfcb8504423ab"></a>

```c
uint16_t size
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[size](#a1522d81a002804223e25300a6961f527)。

此缓冲区可以存储的数据量。

<a id="r_a5b8539be6b3e0cd9e8348febd764a3e8"></a>

```c
}
```

<a id="r_a8c65a7216a0c3139005104b441b253f8"></a>

```c
};
```

用于方便访问net_buf_simple成员的联合体，同时保留旧API。

<a id="r_ade8055f804d5a1fea13e55d71d92a5e7"></a>

```c
uint8_t user_data []
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[user_data](#ade8055f804d5a1fea13e55d71d92a5e7)。

此缓冲区的系统元数据（System Metadata）。

## 46.2\_详细说明（Detailed Documentation）

<a id="a8c65a7216a0c3139005104b441b253f8"></a>

### `[union]`

```c
union { ... } net_buf
```

用于方便访问net_buf_simple成员的联合体，同时保留旧API。

<a id="acd1c7c21fe5b7a1e0f7ea10140200a1b"></a>

### `[union]`

```c
union { ... } net_buf
```

引用计数（Reference Count），与相邻的三个uint8_t字段flags、pool_id和user_data_size一起，打包到一个atomic_t大小的存储槽中。

ref_word是net_buf内部执行引用/解除引用时使用的atomic_t视图；ref、flags、pool_id和user_data_size则是同一存储区域的字节级视图（Byte-Level Views）。

对ref_word执行atomic_inc/dec会使整个字加1或减1。不过，无论大小端序如何，下面的字节结构布局都会把ref放在ref_word的最低有效字节（Least-Significant Byte），且引用计数不会溢出超过254（这已隐含在其uint8_t取值域约束中），因此只有ref字节变化，其他三个字节保持不变。

32位架构上的atomic_t为4字节，字节结构恰好填满该存储槽。64位架构上的atomic_t为8字节；高4字节是struct net_buf原本就需要的对齐填充（Alignment Padding），因为下一字段是按8字节对齐的指针，所以此联合体也不会增大64位架构上的struct net_buf。对于64位大端架构，字节结构通过4字节显式填充进行移位，使ref仍位于ref_word的最低有效字节（LSB）。

flags、pool_id和user_data_size只在分配时由单个线程各写入一次，之后均为只读，因此非原子调用点直接以uint8_t读取仍然安全。在独占缓冲区的上下文中写入flags也合法，例如对刚分配的视图调用bt_buf_make_view。

<a id="ac6eef59915e7ce167442fdacbbfb5e56"></a>

### `data`

```c
uint8_t* net_buf::data
```

指向缓冲区数据起点的指针。

<a id="aa4fcce2e2894fc5dbd9cc74fc020647e"></a>

### `flags`

```c
uint8_t net_buf::flags
```

缓冲区标志（Buffer Flags）的位域。

<a id="a1fa032cc23854c35eae013020823fa88"></a>

### `frags`

```c
struct net_buf* net_buf::frags
```

与此缓冲区关联的片段（Fragments）。

<a id="ae75b7ca728fb7440ea483be8bf88bc38"></a>

### `len`

```c
uint16_t net_buf::len
```

数据指针（Data Pointer）之后的数据长度。

<a id="a5cc70f57e5b776cfa12b2d556e5958f3"></a>

### `node`

```c
sys_snode_t net_buf::node
```

允许将缓冲区放入sys_slist_t。

<a id="a45f294bac054d64034bddcc4c6574d29"></a>

### `pool_id`

```c
uint8_t net_buf::pool_id
```

缓冲区释放后应归还的位置。

<a id="a42da518a82f4c37c45814b4f8c5f2731"></a>

### `ref`

```c
uint8_t net_buf::ref
```

引用计数（Reference Count）。

<a id="a1522d81a002804223e25300a6961f527"></a>

### `size`

```c
uint16_t net_buf::size
```

此缓冲区可以存储的数据量。

<a id="ade8055f804d5a1fea13e55d71d92a5e7"></a>

### `user_data`

```c
uint8_t net_buf::user_data[]
```

此缓冲区的系统元数据（System Metadata）。

分配时清零。

<a id="a65db7bed62d7211114767e6ce58dad75"></a>

### `user_data_size`

```c
uint8_t net_buf::user_data_size
```

此缓冲区上用户数据（User Data）的大小。

本数据类型文档由以下文件生成：

- `zephyr/net_buf.h`

## 46.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h_source.html)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)
- [net_buf](P046_net_buf_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [net_buf_simple](P048_net_buf_simple_结构体.md)
- [net_buf_alloc()](https://docs.zephyrproject.org/latest/doxygen/html/group__net__buf.html#ga534366f3b5c7f41a28372c12149ca005)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P045_ieee802154_security_params_结构体.md) · [返回大纲](大纲.md) · [下一章](P047_net_buf_pool_结构体.md)
