---
id: learning.zephyr-docs.intercore_reference.api-214
title: IVSHMEM共享内存接口
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ivshmem.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第214章\_IVSHMEM共享内存接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__ivshmem.html)。读取日期：2026-10-14；以保存的latest网页为依据，HTML摘要见[来源记录](../SOURCES.md)。

## 214.1\_阅读说明与导航

> 译注：本组说明虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）的公共接口、头文件及源码。先结合[门铃示例](../driver_samples/P067_IVSHMEM门铃示例.md)或[以太网示例](../driver_samples/P060_IVSHMEM以太网示例.md)理解数据与通知的关系，再查询各参数和返回值。

本组：[IVSHMEM共享内存接口](P214_IVSHMEM共享内存接口.md) · [IVSHMEM头文件参考](P215_IVSHMEM头文件参考.md) · [IVSHMEM头文件源码](P216_IVSHMEM头文件源码.md)。

虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）接口。

虚拟机间共享内存（Inter-VM Shared Memory，IVSHMEM）接口。

## 214.2\_函数（Functions）

<a id="r_gaef043cbfbe0aa5061db57f9bbae02eca"></a>

```c
size_t ivshmem_get_mem (const struct device *dev, uintptr_t *memmap)
```

获取虚拟机间共享内存。

相关声明：[ivshmem_get_mem](P214_IVSHMEM共享内存接口.md#gaef043cbfbe0aa5061db57f9bbae02eca)。

<a id="r_gab2f0ccd5a2b8203a54ee5707b3afd6cc"></a>

```c
uint32_t ivshmem_get_id (const struct device *dev)
```

获取本虚拟机（Virtual Machine，VM）的ID。

相关声明：[ivshmem_get_id](P214_IVSHMEM共享内存接口.md#gab2f0ccd5a2b8203a54ee5707b3afd6cc)。

<a id="r_gafee360f2c35abb9a203dd9f4838b8846"></a>

```c
uint16_t ivshmem_get_vectors (const struct device *dev)
```

获取可使用的中断向量（Interrupt Vector）数量。

相关声明：[ivshmem_get_vectors](P214_IVSHMEM共享内存接口.md#gafee360f2c35abb9a203dd9f4838b8846)。

<a id="r_gab4e02271f8b854c783c359aca240d20c"></a>

```c
int ivshmem_int_peer (const struct device *dev, uint32_t peer_id, uint16_t vector)
```

向另一个虚拟机发送中断。

相关声明：[ivshmem_int_peer](P214_IVSHMEM共享内存接口.md#gab4e02271f8b854c783c359aca240d20c)。

<a id="r_ga88aacb71bff0375c10fdb48e34b359fe"></a>

```c
int ivshmem_register_handler (const struct device *dev, struct k_poll_signal *signal, uint16_t vector)
```

注册向量通知（中断）处理程序。

相关声明：[ivshmem_register_handler](P214_IVSHMEM共享内存接口.md#ga88aacb71bff0375c10fdb48e34b359fe)。

<a id="r_ga8b5175861401e5eb5d322f904172b963"></a>

```c
size_t ivshmem_get_rw_mem_section (const struct device *dev, uintptr_t *memmap)
```

获取IVSHMEM读写区（Read/Write Section）；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_rw_mem_section](P214_IVSHMEM共享内存接口.md#ga8b5175861401e5eb5d322f904172b963)。

<a id="r_ga42a6649e852d9b81f8729fb4297043e2"></a>

```c
size_t ivshmem_get_output_mem_section (const struct device *dev, uint32_t peer_id, uintptr_t *memmap)
```

获取某个对端（Peer）的IVSHMEM输出区（Output Section）；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_output_mem_section](P214_IVSHMEM共享内存接口.md#ga42a6649e852d9b81f8729fb4297043e2)。

<a id="r_ga94673f449d111364cfade9192669a5a8"></a>

```c
uint32_t ivshmem_get_state (const struct device *dev, uint32_t peer_id)
```

获取某个对端的状态值；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_state](P214_IVSHMEM共享内存接口.md#ga94673f449d111364cfade9192669a5a8)。

<a id="r_ga144506b762865c6bd451c09f6407fb86"></a>

```c
int ivshmem_set_state (const struct device *dev, uint32_t state)
```

设置本虚拟机的状态；仅适用于ivshmem-v2。

相关声明：[ivshmem_set_state](P214_IVSHMEM共享内存接口.md#ga144506b762865c6bd451c09f6407fb86)。

<a id="r_gaaa7e99f4844f270d1f1d2271b43d607c"></a>

```c
uint32_t ivshmem_get_max_peers (const struct device *dev)
```

获取所支持的最大对端数量；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_max_peers](P214_IVSHMEM共享内存接口.md#gaaa7e99f4844f270d1f1d2271b43d607c)。

<a id="r_ga940ffec4ae0380d774c05107afe41994"></a>

```c
uint16_t ivshmem_get_protocol (const struct device *dev)
```

获取此IVSHMEM实例使用的协议；仅适用于ivshmem-v2。

相关声明：[ivshmem_get_protocol](P214_IVSHMEM共享内存接口.md#ga940ffec4ae0380d774c05107afe41994)。

<a id="r_ga67dc8b24f863c3e9a8ac6a89753fd4c9"></a>

```c
int ivshmem_enable_interrupts (const struct device *dev, bool enable)
```

设置本虚拟机的中断使能状态；仅适用于ivshmem-v2。

相关声明：[ivshmem_enable_interrupts](P214_IVSHMEM共享内存接口.md#ga67dc8b24f863c3e9a8ac6a89753fd4c9)。

## 214.3\_详细说明（Detailed Documentation）

<a id="ga67dc8b24f863c3e9a8ac6a89753fd4c9"></a>

### `ivshmem\_enable\_interrupts()`

```c
int ivshmem_enable_interrupts ( const struct device * dev, bool enable )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

设置本虚拟机的中断使能状态；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `enable` | true表示使能中断，false表示禁用中断。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：成功返回0，否则返回负的errno错误码。

<a id="gab2f0ccd5a2b8203a54ee5707b3afd6cc"></a>

### `ivshmem\_get\_id()`

```c
uint32_t ivshmem_get_id ( const struct device * dev)
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取本虚拟机（Virtual Machine，VM）的ID。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |

**返回（Returns）**：本虚拟机的ID；若运行的不是门铃（Doorbell）版本，则返回0。

> 译注——源码核对：ID 0也可以是有效的对端标识，不能仅用返回0来判定没有门铃支持。当前驱动对v2实例读取v2寄存器中的id，对其他实例读取iv_position；接口原文的门铃返回说明保留，实例能力还应结合配置和向量数量判断。

<a id="gaaa7e99f4844f270d1f1d2271b43d607c"></a>

### `ivshmem\_get\_max\_peers()`

```c
uint32_t ivshmem_get_max_peers ( const struct device * dev)
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取所支持的最大对端数量；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：所支持的最大对端数量，或0。

<a id="gaef043cbfbe0aa5061db57f9bbae02eca"></a>

### `ivshmem\_get\_mem()`

```c
size_t ivshmem_get_mem ( const struct device * dev, uintptr_t * memmap )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取虚拟机间共享内存。

注意：ivshmem-v2不支持此API，因为读写区（R/W）与只读区（R/O）可能不是连续映射的。对ivshmem-v2，应使用`ivshmem_get_rw_mem_section`、[`ivshmem_get_output_mem_section`](P214_IVSHMEM共享内存接口.md#ga42a6649e852d9b81f8729fb4297043e2)和`ivshmem_get_state`接口访问共享内存。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `memmap` | 用于填入内存地址的指针。 |

**返回（Returns）**：已映射内存的大小，或0。

> 译注——源码核对：当前官方驱动遇到v2实例时把输出地址设为0并返回0；不能用这个旧接口获取v2实例的统一连续地址。其他分区查询也必须检查返回大小，而不能只观察输出指针是否被修改。

<a id="ga42a6649e852d9b81f8729fb4297043e2"></a>

### `ivshmem\_get\_output\_mem\_section()`

```c
size_t ivshmem_get_output_mem_section ( const struct device * dev, uint32_t peer_id, uintptr_t * memmap )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取某个对端（Peer）的IVSHMEM输出区（Output Section）；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `peer_id` | 要获取其输出内存区的虚拟机ID。 |
| `memmap` | 用于填入内存地址的指针。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：已映射内存的大小，或0。

<a id="ga940ffec4ae0380d774c05107afe41994"></a>

### `ivshmem\_get\_protocol()`

```c
uint16_t ivshmem_get_protocol ( const struct device * dev)
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取此IVSHMEM实例使用的协议；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：协议。

<a id="ga8b5175861401e5eb5d322f904172b963"></a>

### `ivshmem\_get\_rw\_mem\_section()`

```c
size_t ivshmem_get_rw_mem_section ( const struct device * dev, uintptr_t * memmap )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取IVSHMEM读写区（Read/Write Section）；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `memmap` | 用于填入内存地址的指针。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：已映射内存的大小，或0。

<a id="ga94673f449d111364cfade9192669a5a8"></a>

### `ivshmem\_get\_state()`

```c
uint32_t ivshmem_get_state ( const struct device * dev, uint32_t peer_id )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取某个对端的状态值；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `peer_id` | 要获取其状态的虚拟机ID。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：对端的状态值。

> 译注——源码核对：当前驱动对非v2实例或超出max_peers的peer_id返回0；状态0本身也可能是合法值。这一无符号返回值不是通用errno结果，不能用“非负即成功”的规则解释。

<a id="gafee360f2c35abb9a203dd9f4838b8846"></a>

### `ivshmem\_get\_vectors()`

```c
uint16_t ivshmem_get_vectors ( const struct device * dev)
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

获取可使用的中断向量（Interrupt Vector）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |

**返回（Returns）**：可用中断向量数量。

<a id="gab4e02271f8b854c783c359aca240d20c"></a>

### `ivshmem\_int\_peer()`

```c
int ivshmem_int_peer ( const struct device * dev, uint32_t peer_id, uint16_t vector )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

向另一个虚拟机发送中断。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| `peer_id` | 要向其发送中断的虚拟机ID。 |
| `vector` | 要使用的中断向量。 |

**返回（Returns）**：成功返回0，否则返回负的errno错误码。

> 译注——源码核对：当前驱动未启用CONFIG_IVSHMEM_DOORBELL时返回-ENOSYS；向量超界返回-EINVAL，v2实例还检查peer_id是否超界。这是所读取实现的具体行为，不能替代原文对其他实现的通用约定。

<a id="ga88aacb71bff0375c10fdb48e34b359fe"></a>

### `ivshmem\_register\_handler()`

```c
int ivshmem_register_handler ( const struct device * dev, struct k_poll_signal * signal, uint16_t vector )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

注册向量通知（中断）处理程序。

注意：被触发的信号所携带的返回状态如果为正，就是产生该信号的向量。调用方因而可以让所有向量共享一个信号，也可以让每个向量各使用一个信号。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| [`signal`](https://docs.zephyrproject.org/latest/doxygen/html/signal_8h.html#a5d326f119f87d0facaa662520f8c322a) | 指向有效且已准备好接收通知的`struct k_poll_signal`对象的指针；也可以传入`NULL`，注销为指定向量注册的任意处理程序。 |
| `vector` | 要从中接收通知的中断向量。 |

**返回（Returns）**：成功返回0，否则返回负的errno错误码。

> 译注——源码核对：原说明使用“如果为正”的措辞。当前驱动实际调用k_poll_signal_raise(signal, vector)，向量0也会作为有效结果传递；信号是否触发与它携带的结果值应分别判断。NULL注销是原API约定，但当前用户态验证包装直接调用K_SYSCALL_OBJ(signal, K_OBJ_POLL_SIGNAL)，没有跳过NULL的分支，因此不能把内核调用的NULL注销用法直接视为用户态也已验证可用。

<a id="ga144506b762865c6bd451c09f6407fb86"></a>

### `ivshmem\_set\_state()`

```c
int ivshmem_set_state ( const struct device * dev, uint32_t state )
```

```c
#include <zephyr/drivers/virtualization/ivshmem.h>
```

设置本虚拟机的状态；仅适用于ivshmem-v2。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例设备结构的指针。 |
| [`state`](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90) | 要设置的状态值。 |

**注意（Attention）**：仅当启用Kconfig选项`CONFIG_IVSHMEM_V2`时可用。

**返回（Returns）**：成功返回0，否则返回负的errno错误码。

## 214.4\_源码跟踪与验证边界

本仓库[对应头文件](../../../include/zephyr/drivers/virtualization/ivshmem.h)、[驱动实现](../../../drivers/virtualization/virt_ivshmem.c)和[系统调用验证包装](../../../drivers/virtualization/virt_ivshmem_handlers.c)可用于源码跟踪；本仓库版本不自动等同于网页版本。本批译注依据保存的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/virtualization/ivshmem.h)、[官方驱动](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem.c)和[官方包装](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/virtualization/virt_ivshmem_handlers.c)，摘要见[来源记录](../SOURCES.md)。main分支会变化，以上实现结论不能当作所有版本的接口保证。

项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。本文未安装、构建、运行虚拟机、配置共享内存或进行接线测量。

<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P213_zbus核心接口.md) · [返回大纲](大纲.md) · [下一章](P215_IVSHMEM头文件参考.md)
