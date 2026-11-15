---
id: learning.zephyr-docs.dma-reference.page-1
title: DMA公共接口
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dma__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_DMA公共接口

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__interface.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

直接内存访问（Direct Memory Access，DMA）控制器接口。

<a id="details"></a>

直接内存访问（Direct Memory Access，DMA）控制器接口。自1.5起提供；接口版本为1.1.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 1.1\_主题（Topics）

<a id="r_dma_5Fsf32lb"></a>

相关声明：[DMA的SF32LB专用功能（SF32LB Specifics）](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html)。

DMA的SF32LB专用功能（SF32LB Specifics）。

<a id="r_dma_5Finterface_5Fbackend"></a>

相关声明：[DMA驱动后端接口（Backend API）](P002_DMA驱动后端接口.md)。



<a id="r_devicetree-dmas"></a>

相关声明：[设备树DMA接口（Devicetree DMA API）](P008_DMA设备树宏.md)。



<a id="r_dma_5Fbee_5Fmacros"></a>

相关声明：[Realtek Bee DMA宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html)。

用于从设备树（Devicetree）提取DMA配置的宏。

<a id="r_dma_5Fxilinx_5Fadma"></a>

相关声明：[Xilinx ADMA专用功能](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html)。



<a id="header-files"></a>
<a id="files"></a>

## 1.2\_文件（Files）

<a id="r_dma_2Eh"></a>

```c
file dma.h
```

相关声明：[dma.h](P009_DMA驱动头文件参考.md)。

DMA（Direct Memory Access，直接内存访问）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.3\_数据结构（Data Structures）

<a id="r_dma_5Fblock_5Fconfig"></a>

```c
struct dma_block_config
```

相关声明：[dma_block_config](P003_DMA传输块配置.md)。

DMA传输块配置结构（Block Configuration）。

<a id="r_dma_5Fconfig"></a>

```c
struct dma_config
```

相关声明：[dma_config](P004_DMA通道配置.md)。

DMA配置结构（Configuration）。

<a id="r_dma_5Fstatus"></a>

```c
struct dma_status
```

相关声明：[dma_status](P005_DMA运行状态.md)。

DMA运行时状态结构（Runtime Status）。

<a id="r_dma_5Fcontext"></a>

```c
struct dma_context
```

相关声明：[dma_context](P006_DMA通道分配上下文.md)。

DMA上下文结构（Context）。注意：dma_context必须是通过dev->data取得的DMA客户端驱动数据的第一个成员。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.4\_宏定义（Macros）

<a id="r_gad4fc9a9c59f4e07c81a4c2f3b57c9ccb"></a>

```c
#define DMA_STATUS_COMPLETE 0
```

相关声明：[DMA_STATUS_COMPLETE](#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)。

在传输列表（Transfer List）完成时发生的DMA回调事件。

<a id="r_gab74c89289c8429071522cb89ac066eea"></a>

```c
#define DMA_STATUS_BLOCK 1
```

相关声明：[DMA_STATUS_BLOCK](#gab74c89289c8429071522cb89ac066eea)。

在传输列表中的单个传输块（Transfer Block）完成时发生的DMA回调事件。

<a id="r_gaa2544dbb8d5e36f413d47b61268daf1a"></a>

```c
#define DMA_STATUS_HALF_COMPLETE 2
```

相关声明：[DMA_STATUS_HALF_COMPLETE](#gaa2544dbb8d5e36f413d47b61268daf1a)。

在单个传输块完成一半时发生的DMA回调事件。

<a id="r_gae28ba5114dc2e9ecb89ccf9b623e938f"></a>

```c
#define DMA_MAGIC 0x47494749
```

相关声明：[DMA_MAGIC](#gae28ba5114dc2e9ecb89ccf9b623e938f)。

用于识别上下文内容的魔数（Magic Code）。

<a id="r_ga542e1a0fa0d851a51e4c8abf9a820e0c"></a>

```c
#define DMA_BUF_ADDR_ALIGNMENT(node)
```

相关声明：[DMA_BUF_ADDR_ALIGNMENT](#ga542e1a0fa0d851a51e4c8abf9a820e0c)。

取得描述缓冲区地址对齐（Buffer Address Alignment）的设备树属性。

<a id="r_ga76dfdfecc732319908f381883c630a2b"></a>

```c
#define DMA_BUF_SIZE_ALIGNMENT(node)
```

相关声明：[DMA_BUF_SIZE_ALIGNMENT](#ga76dfdfecc732319908f381883c630a2b)。

取得描述缓冲区大小对齐（Buffer Size Alignment）的设备树属性。

<a id="r_ga083e8b0a863b0833c55158053d286f15"></a>

```c
#define DMA_COPY_ALIGNMENT(node)
```

相关声明：[DMA_COPY_ALIGNMENT](#ga083e8b0a863b0833c55158053d286f15)。

取得描述最小可复制数据块（Minimum Copy Chunk）的设备树属性。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 1.5\_类型定义（Typedefs）

<a id="r_ga94745b4472ee1addd4f82db4e59e9fb5"></a>

```c
typedef void(* dma_callback_t) (const struct device *dev, void *user_data, uint32_t channel, int status)
```

相关声明：[dma_callback_t](#ga94745b4472ee1addd4f82db4e59e9fb5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

DMA传输完成回调函数（Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.6\_枚举（Enumerations）

<a id="r_gae442d8ba73be7e53b68165647b0ea402"></a>

```c
enum dma_channel_direction { MEMORY_TO_MEMORY = 0x0 , MEMORY_TO_PERIPHERAL , PERIPHERAL_TO_MEMORY , PERIPHERAL_TO_PERIPHERAL , HOST_TO_MEMORY , MEMORY_TO_HOST , DMA_CHANNEL_DIRECTION_COMMON_COUNT , DMA_CHANNEL_DIRECTION_PRIV_START = DMA_CHANNEL_DIRECTION_COMMON_COUNT , DMA_CHANNEL_DIRECTION_MAX = 0x7 }
```

相关声明：[dma_channel_direction](#gae442d8ba73be7e53b68165647b0ea402)、[MEMORY_TO_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)、[MEMORY_TO_PERIPHERAL](#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)、[PERIPHERAL_TO_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)、[PERIPHERAL_TO_PERIPHERAL](#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)、[HOST_TO_MEMORY](#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)、[MEMORY_TO_HOST](#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)、[DMA_CHANNEL_DIRECTION_COMMON_COUNT](#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)、[DMA_CHANNEL_DIRECTION_PRIV_START](#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)、[DMA_CHANNEL_DIRECTION_MAX](#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)。

DMA通道传输方向（Channel Direction）。

<a id="r_gafe0877ef4bd7790a4bcd46052088231c"></a>

```c
enum dma_addr_adj { DMA_ADDR_ADJ_INCREMENT , DMA_ADDR_ADJ_DECREMENT , DMA_ADDR_ADJ_NO_CHANGE }
```

相关声明：[dma_addr_adj](#gafe0877ef4bd7790a4bcd46052088231c)、[DMA_ADDR_ADJ_INCREMENT](#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)、[DMA_ADDR_ADJ_DECREMENT](#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)、[DMA_ADDR_ADJ_NO_CHANGE](#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)。

DMA地址调整方式（Address Adjustment）。

<a id="r_gade594552920aabbfd2106059a338498b"></a>

```c
enum dma_channel_filter { DMA_CHANNEL_NORMAL , DMA_CHANNEL_PERIODIC }
```

相关声明：[dma_channel_filter](#gade594552920aabbfd2106059a338498b)、[DMA_CHANNEL_NORMAL](#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)、[DMA_CHANNEL_PERIODIC](#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)。

DMA通道属性（Channel Attributes）。

<a id="r_ga08c366c8d47672eeeb37b258af20101b"></a>

```c
enum dma_attribute_type { DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT , DMA_ATTR_BUFFER_SIZE_ALIGNMENT , DMA_ATTR_COPY_ALIGNMENT , DMA_ATTR_MAX_BLOCK_COUNT }
```

相关声明：[dma_attribute_type](#ga08c366c8d47672eeeb37b258af20101b)、[DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)、[DMA_ATTR_BUFFER_SIZE_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)、[DMA_ATTR_COPY_ALIGNMENT](#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)、[DMA_ATTR_MAX_BLOCK_COUNT](#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)。

DMA属性（Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.7\_函数（Functions）

<a id="r_ga6df1a6b89f271a0eae01c17b748bd2df"></a>

```c
static int dma_config (const struct device *dev, uint32_t channel, struct dma_config *config)
```

相关声明：[dma_config](#ga6df1a6b89f271a0eae01c17b748bd2df)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

为DMA传输配置单个通道（Channel）。

<a id="r_ga55bd5d550349c11c63ef47c2ed861f36"></a>

```c
static int dma_reload (const struct device *dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size)
```

相关声明：[dma_reload](#ga55bd5d550349c11c63ef47c2ed861f36)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

重新装载（Reload）DMA通道的缓冲区。

<a id="r_gaf1184de07811702ffe89737b79e4a338"></a>

```c
static int dma_start (const struct device *dev, uint32_t channel)
```

相关声明：[dma_start](#gaf1184de07811702ffe89737b79e4a338)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

使能DMA通道并启动传输；必须事先配置该通道。

<a id="r_gafd602ee8386e10bb9ac7d386b3dc6a83"></a>

```c
static int dma_stop (const struct device *dev, uint32_t channel)
```

相关声明：[dma_stop](#gafd602ee8386e10bb9ac7d386b3dc6a83)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

停止DMA传输并禁用通道。

<a id="r_ga97bf9807b7fde7671a378333f01463d6"></a>

```c
static int dma_suspend (const struct device *dev, uint32_t channel)
```

相关声明：[dma_suspend](#ga97bf9807b7fde7671a378333f01463d6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

挂起（Suspend）DMA通道传输。

<a id="r_ga1b1eeef68f1aa4818c9baf95b83b9e1e"></a>

```c
static int dma_resume (const struct device *dev, uint32_t channel)
```

相关声明：[dma_resume](#ga1b1eeef68f1aa4818c9baf95b83b9e1e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

恢复（Resume）DMA通道传输。

<a id="r_gaadc34e0ea92d9fd2f1242789367b1dd5"></a>

```c
static int dma_request_channel (const struct device *dev, void *filter_param)
```

相关声明：[dma_request_channel](#gaadc34e0ea92d9fd2f1242789367b1dd5)、[device](../device_reference/P002_设备对象结构.md)。

申请DMA通道（Request Channel）。

<a id="r_ga93b49d4d0910ceed88fa8aaa22b73098"></a>

```c
static void dma_release_channel (const struct device *dev, uint32_t channel)
```

相关声明：[dma_release_channel](#ga93b49d4d0910ceed88fa8aaa22b73098)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

释放DMA通道（Release Channel）。

<a id="r_ga6d4c3e63bc4382215774e86893bc3072"></a>

```c
static int dma_chan_filter (const struct device *dev, int channel, void *filter_param)
```

相关声明：[dma_chan_filter](#ga6d4c3e63bc4382215774e86893bc3072)、[device](../device_reference/P002_设备对象结构.md)。

DMA通道筛选器（Channel Filter）。

<a id="r_ga2cae500f1f9ed42ad338a40ec8655544"></a>

```c
static int dma_get_status (const struct device *dev, uint32_t channel, struct dma_status *stat)
```

相关声明：[dma_get_status](#ga2cae500f1f9ed42ad338a40ec8655544)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_status](P005_DMA运行状态.md)、[stat](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)。

取得DMA传输的当前运行状态。

<a id="r_ga641f3fa492bfb17cf9f0a0361d429257"></a>

```c
static int dma_get_attribute (const struct device *dev, uint32_t type, uint32_t *value)
```

相关声明：[dma_get_attribute](#ga641f3fa492bfb17cf9f0a0361d429257)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得DMA控制器的属性。

<a id="r_gadd1724a843bba4ccc1c65c9fb9d3d921"></a>

```c
static uint32_t dma_width_index (uint32_t size)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_width_index](#gadd1724a843bba4ccc1c65c9fb9d3d921)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

查找用于寄存器的通用传输宽度索引（Width Index）。

<a id="r_gaac27f2ee664671884087ee3d2a2863ce"></a>

```c
static uint32_t dma_burst_index (uint32_t burst)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_burst_index](#gaac27f2ee664671884087ee3d2a2863ce)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

查找用于寄存器的通用突发传输索引（Burst Index）。

## 1.8\_详细说明（Detailed Documentation）

<a id="ga542e1a0fa0d851a51e4c8abf9a820e0c"></a>

### `DMA_BUF_ADDR_ALIGNMENT`

```c
#define DMA_BUF_ADDR_ALIGNMENT ( node)
```

```c
#include <zephyr/drivers/dma.h>
```

展开值（Value）：

```c
DT_PROP(node, dma_buf_addr_alignment)
```

取得描述缓冲区地址对齐（Buffer Address Alignment）的设备树属性。

静态定义或分配DMA缓冲区时很有用，因为这类缓冲区通常有内存对齐要求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 节点标识符（Node Identifier），例如DT_NODELABEL(dma_0)。 |

**返回（Returns）**：返回alignment：DMA缓冲区要求的内存对齐，单位为字节。

<a id="ga76dfdfecc732319908f381883c630a2b"></a>

### `DMA_BUF_SIZE_ALIGNMENT`

```c
#define DMA_BUF_SIZE_ALIGNMENT ( node)
```

```c
#include <zephyr/drivers/dma.h>
```

展开值（Value）：

```c
DT_PROP(node, dma_buf_size_alignment)
```

取得描述缓冲区大小对齐（Buffer Size Alignment）的设备树属性。

静态定义或分配DMA缓冲区时很有用，因为这类缓冲区通常有内存对齐要求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 节点标识符（Node Identifier），例如DT_NODELABEL(dma_0)。 |

**返回（Returns）**：返回alignment：DMA缓冲区要求的内存对齐，单位为字节。

<a id="ga083e8b0a863b0833c55158053d286f15"></a>

### `DMA_COPY_ALIGNMENT`

```c
#define DMA_COPY_ALIGNMENT ( node)
```

```c
#include <zephyr/drivers/dma.h>
```

展开值（Value）：

```c
DT_PROP(node, dma_copy_alignment)
```

取得描述最小可复制数据块（Minimum Copy Chunk）的设备树属性。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `node` | 节点标识符（Node Identifier），例如DT_NODELABEL(dma_0)。 |

**返回（Returns）**：返回minimal：可复制的最小数据块大小。

<a id="gae28ba5114dc2e9ecb89ccf9b623e938f"></a>

### `DMA_MAGIC`

```c
#define DMA_MAGIC 0x47494749
```

```c
#include <zephyr/drivers/dma.h>
```

用于识别上下文内容的魔数（Magic Code）。

<a id="gab74c89289c8429071522cb89ac066eea"></a>

### `DMA_STATUS_BLOCK`

```c
#define DMA_STATUS_BLOCK 1
```

```c
#include <zephyr/drivers/dma.h>
```

在传输列表中的单个传输块（Transfer Block）完成时发生的DMA回调事件。

<a id="gad4fc9a9c59f4e07c81a4c2f3b57c9ccb"></a>

### `DMA_STATUS_COMPLETE`

```c
#define DMA_STATUS_COMPLETE 0
```

```c
#include <zephyr/drivers/dma.h>
```

在传输列表（Transfer List）完成时发生的DMA回调事件。

<a id="gaa2544dbb8d5e36f413d47b61268daf1a"></a>

### `DMA_STATUS_HALF_COMPLETE`

```c
#define DMA_STATUS_HALF_COMPLETE 2
```

```c
#include <zephyr/drivers/dma.h>
```

在单个传输块完成一半时发生的DMA回调事件。

<a id="ga94745b4472ee1addd4f82db4e59e9fb5"></a>

### `dma_callback_t`

```c
typedef void(* dma_callback_t) (const struct device *dev, void *user_data, uint32_t channel, int status)
```

```c
#include <zephyr/drivers/dma.h>
```

DMA传输完成回调函数（Callback）。

启用后，回调会在传输或传输块完成时调用，也会在出错时调用。在循环模式（Circular Mode）下，status表示DMA设备已到达缓冲区末尾（DMA_STATUS_COMPLETE）或水位点（Water Mark，DMA_STATUS_BLOCK）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向发起此次回调的DMA设备。 |
| `user_data` | 指向用户数据的指针，或NULL。 |
| `channel` | 通道编号。 |
| `status` | 传输状态：DMA_STATUS_COMPLETE表示缓冲区已全部消耗；DMA_STATUS_BLOCK表示缓冲区消耗达到已配置的块边界或水位点；其他错误以负errno值表示。 |

> 译注——源码核对：回调status和同步API返回值是两种不同语义。原页还定义DMA_STATUS_HALF_COMPLETE=2，但本回调参数段未逐项列出它；不能据“否则为负errno”推断所有非零回调状态都是错误。实际事件与回调启用条件须结合驱动支持。

<a id="gafe0877ef4bd7790a4bcd46052088231c"></a>

### `dma_addr_adj`

```c
enum dma_addr_adj
```

```c
#include <zephyr/drivers/dma.h>
```

DMA地址调整方式（Address Adjustment）。

source_addr_adj与dest_addr_adj的有效取值。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMA_ADDR_ADJ_INCREMENT` | 递增地址（Increment）。 |
| `DMA_ADDR_ADJ_DECREMENT` | 递减地址（Decrement）。 |
| `DMA_ADDR_ADJ_NO_CHANGE` | 地址保持不变（No Change）。 |

<a id="ga08c366c8d47672eeeb37b258af20101b"></a>

### `dma_attribute_type`

```c
enum dma_attribute_type
```

```c
#include <zephyr/drivers/dma.h>
```

DMA属性（Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT` | 缓冲区地址要求的对齐，单位为字节。 |
| `DMA_ATTR_BUFFER_SIZE_ALIGNMENT` | 缓冲区大小要求的对齐，单位为字节。 |
| `DMA_ATTR_COPY_ALIGNMENT` | 内存到内存复制要求的对齐，单位为字节。 |
| `DMA_ATTR_MAX_BLOCK_COUNT` | 一次传输允许的最大块数。 |

<a id="gae442d8ba73be7e53b68165647b0ea402"></a>

### `dma_channel_direction`

```c
enum dma_channel_direction
```

```c
#include <zephyr/drivers/dma.h>
```

DMA通道传输方向（Channel Direction）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MEMORY_TO_MEMORY` | 内存到内存（Memory to Memory）。 |
| `MEMORY_TO_PERIPHERAL` | 内存到外设（Memory to Peripheral）。 |
| `PERIPHERAL_TO_MEMORY` | 外设到内存（Peripheral to Memory）。 |
| `PERIPHERAL_TO_PERIPHERAL` | 外设到外设（Peripheral to Peripheral）。 |
| `HOST_TO_MEMORY` | 主机到内存（Host to Memory）。 |
| `MEMORY_TO_HOST` | 内存到主机（Memory to Host）。 |
| `DMA_CHANNEL_DIRECTION_COMMON_COUNT` | 所有通用通道方向的数量。 |
| `DMA_CHANNEL_DIRECTION_PRIV_START` | 从此值开始的更高取值由DMA控制器或片上系统（System on Chip，SoC）专门定义。请参阅相应DMA驱动的头文件。 |
| `DMA_CHANNEL_DIRECTION_MAX` | 允许的最大值；此字段只有3位。 |

<a id="gade594552920aabbfd2106059a338498b"></a>

### `dma_channel_filter`

```c
enum dma_channel_filter
```

```c
#include <zephyr/drivers/dma.h>
```

DMA通道属性（Channel Attributes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DMA_CHANNEL_NORMAL` | 普通DMA通道（Normal Channel）。 |
| `DMA_CHANNEL_PERIODIC` | 可由周期性源触发的通道（Periodic Channel）。 |

<a id="gaac27f2ee664671884087ee3d2a2863ce"></a>

### `dma_burst_index()`

```c
uint32_t dma_burst_index ( uint32_t burst)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

查找用于寄存器的通用突发传输索引（Burst Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `burst` | 一次突发传输（Burst）发送的字节数。 |

**警告（Warning）**：警告：这种查找适用于多数控制器，但未必适用于你的控制器。使用此辅助函数前，必须确认控制器采用最常见的寄存器位编码；若不支持这些编码，就需要在控制器驱动中自行实现查找。

**返回（Returns）**：返回要写入寄存器的通用DMA索引。

> 译注——源码核对：本次读取的头文件在1～256范围检查后使用if (!(burst & (burst - 1))) return 0，实际对2的幂返回0，而非拒绝非2的幂；其他范围内取值进入find_msb_set。它与源码“确保为2的幂”的注释不一致。这里如实记录当前代码，不能将该函数当作通用正确编码器；应核对目标版本和控制器寄存器定义。

<a id="ga6d4c3e63bc4382215774e86893bc3072"></a>

### `dma_chan_filter()`

```c
int dma_chan_filter ( const struct device * dev, int channel, void * filter_param )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

DMA通道筛选器（Channel Filter）。

按属性筛选通道。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 通道编号。 |
| `filter_param` | 筛选属性（Filter Attribute）。 |

**返回（Returns）**：成功返回非负值，失败返回负errno值。

> 译注——源码核对：原文把非负值统一描述为成功；当前包装实际直接返回bool类型chan_filter回调的结果：1表示匹配，0表示不匹配，没有回调时为-ENOSYS。这里不能用ret>=0判断匹配，也不能把筛选本身当作通道申请；它不设置分配位。

<a id="ga6df1a6b89f271a0eae01c17b748bd2df"></a>

### `dma_config()`

```c
int dma_config ( const struct device * dev, uint32_t channel, struct dma_config * config )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

为DMA传输配置单个通道（Channel）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 待配置通道的数字标识。 |
| `config` | 包含选定通道预期配置的数据结构。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

<a id="ga641f3fa492bfb17cf9f0a0361d429257"></a>

### `dma_get_attribute()`

```c
int dma_get_attribute ( const struct device * dev, uint32_t type, uint32_t * value )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

取得DMA控制器的属性。

此函数可取得设备专用的静态或运行时属性，例如缓冲区要求的地址对齐和大小对齐。实现必须检查传入type的有效性：无效时返回-EINVAL，不支持时返回-ENOSYS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `type` | 属性的数字标识。 |
| `value` | 用于接收读取值的变量指针，不得为NULL。 |

**返回（Returns）**：成功返回非负值，失败返回负errno值。

<a id="ga2cae500f1f9ed42ad338a40ec8655544"></a>

### `dma_get_status()`

```c
int dma_get_status ( const struct device * dev, uint32_t channel, struct dma_status * stat )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

取得DMA传输的当前运行状态。

实现必须检查传入通道ID的有效性：无效时返回-EINVAL，不支持时返回-ENOSYS。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 正在处理该传输的通道的数字标识。 |
| `stat` | 用于保存DMA状态的dma_status对象，不得为NULL。 |

**返回（Returns）**：成功返回非负值，失败返回负errno值。

<a id="ga93b49d4d0910ceed88fa8aaa22b73098"></a>

### `dma_release_channel()`

```c
void dma_release_channel ( const struct device * dev, uint32_t channel )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

释放DMA通道（Release Channel）。

释放DMA通道资源。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 通道编号。 |

**说明（Note）**：注意：只要释放函数的实现不阻塞，就可以在禁止阻塞的上下文中安全调用本函数，例如中断服务例程（Interrupt Service Routine，ISR）。

> 译注——源码核对：当前实现调用可选chan_release后清除占用位，不调用dma_stop，也不验证调用者是否拥有通道。调用前应按驱动约定停止正在使用的传输，并只释放自己成功申请的通道。源码使用(int)channel < dma_channels判断上界，不能把它理解为对任意uint32_t输入的完整校验；尤其不要把申请失败的负值转成无符号编号后传入。

<a id="ga55bd5d550349c11c63ef47c2ed861f36"></a>

### `dma_reload()`

```c
int dma_reload ( const struct device * dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

重新装载（Reload）DMA通道的缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 选定的待配置通道的数字标识。 |
| `src` | DMA传输的源地址（Source Address）。 |
| `dst` | DMA传输的目标地址（Destination Address）。 |
| `size` | DMA传输大小。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

> 译注——源码核对：网页原型显示32位src和dst；本次头文件在CONFIG_DMA_64BIT启用时使用uint64_t，否则使用uint32_t。传输块结构的source_address和dest_address具有同样的条件类型。应按构建配置与驱动能力选择地址类型，不能把网页中的一种展示当作所有配置。

<a id="gaadc34e0ea92d9fd2f1242789367b1dd5"></a>

### `dma_request_channel()`

```c
int dma_request_channel ( const struct device * dev, void * filter_param )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

申请DMA通道（Request Channel）。

申请DMA通道资源；没有可用的有效通道时返回-EINVAL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `filter_param` | 筛选函数的参数（Filter Parameter）。 |

**说明（Note）**：注意：只要筛选函数的实现不阻塞，就可以在禁止阻塞的上下文中安全调用本函数，例如中断服务例程（Interrupt Service Routine，ISR）。

**返回（Returns）**：成功返回DMA通道编号，失败返回负errno值。

> 译注——源码核对：本次头文件先把dev->data转换为dma_context并检查DMA_MAGIC，再以atomic_test_and_set_bit尝试占用空闲通道；筛选回调返回false时清除该位并继续寻找。未提供筛选回调时可直接接受空闲通道。成功结果可能是通道0，须用返回值<0判断失败。该函数不调用dma_config或dma_start。

<a id="ga1b1eeef68f1aa4818c9baf95b83b9e1e"></a>

### `dma_resume()`

```c
int dma_resume ( const struct device * dev, uint32_t channel )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

恢复（Resume）DMA通道传输。

实现必须检查传入通道状态和ID的有效性，任一无效都应返回-EINVAL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 待恢复通道的数字标识。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现（Not Implemented）。 |
| `-EINVAL` | 通道ID或状态无效。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

<a id="gaf1184de07811702ffe89737b79e4a338"></a>

### `dma_start()`

```c
int dma_start ( const struct device * dev, uint32_t channel )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

使能DMA通道并启动传输；必须事先配置该通道。

实现必须检查传入通道ID的有效性，无效时返回-EINVAL。

允许对已经启动的通道再次调用启动操作，并且必须报告成功。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 将处理该传输的通道的数字标识。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

<a id="gafd602ee8386e10bb9ac7d386b3dc6a83"></a>

### `dma_stop()`

```c
int dma_stop ( const struct device * dev, uint32_t channel )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

停止DMA传输并禁用通道。

实现必须检查传入通道ID的有效性，无效时返回-EINVAL。

允许对已经停止的通道再次调用停止操作，并且必须报告成功。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 正在处理该传输的通道的数字标识。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现（Not Implemented）。 |
| `-EINVAL` | 通道ID无效。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

<a id="ga97bf9807b7fde7671a378333f01463d6"></a>

### `dma_suspend()`

```c
int dma_suspend ( const struct device * dev, uint32_t channel )
```

声明属性：`inline`、`static`、`isr-ok`。

```c
#include <zephyr/drivers/dma.h>
```

挂起（Suspend）DMA通道传输。

实现必须检查传入通道状态和ID的有效性，任一无效都应返回-EINVAL。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `channel` | 待挂起通道的数字标识。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-ENOSYS` | 未实现（Not Implemented）。 |
| `-EINVAL` | 通道ID或状态无效。 |

**返回（Returns）**：成功返回0，失败返回负errno值。

<a id="gadd1724a843bba4ccc1c65c9fb9d3d921"></a>

### `dma_width_index()`

```c
uint32_t dma_width_index ( uint32_t size)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/drivers/dma.h>
```

查找用于寄存器的通用传输宽度索引（Width Index）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `size` | 总线宽度，单位为字节。 |

**警告（Warning）**：警告：这种查找适用于多数控制器，但未必适用于你的控制器。使用此辅助函数前，必须确认控制器采用最常见的寄存器位编码；若不支持这些编码，就需要在控制器驱动中自行实现查找。

**返回（Returns）**：返回要写入寄存器的通用DMA索引。

> 译注——源码核对：本次实现仅接受1～32范围内的2的幂，返回find_msb_set(size)，即1、2、4、8、16、32分别映射到1～6；其他输入返回0。源码把回退0注释为默认8字节，但这不构成所有控制器的寄存器编码保证，应按实际硬件定义核对。

## 1.9\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 1.10\_原页交叉引用（Cross References）

- [DMA的SF32LB专用功能（SF32LB Specifics）](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__sf32lb.html)
- [DMA驱动后端接口（Backend API）](P002_DMA驱动后端接口.md)
- [设备树DMA接口（Devicetree DMA API）](P008_DMA设备树宏.md)
- [Realtek Bee DMA宏](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__bee__macros.html)
- [Xilinx ADMA专用功能](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html)
- [dma.h](P009_DMA驱动头文件参考.md)
- [dma_block_config](P003_DMA传输块配置.md)
- [dma_config](P004_DMA通道配置.md)
- [dma_status](P005_DMA运行状态.md)
- [dma_context](P006_DMA通道分配上下文.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [stat](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)
- [DT_PROP](../dt_property_reference/P001_设备树属性读取宏.md#ga8e1fd9ebacd85d2013df027d041d506b)
- [DT_NODELABEL(dma_0)](../dt_identity_reference/P001_设备树节点标识宏.md#gab7d23294a6bf7fd44a98b48ec47d8a79)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__devicetree-generic-prop_html_ga8e1fd9ebacd85d2013df027d041d506b"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e"></a>
<a id="ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717"></a>
<a id="ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f"></a>
<a id="gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f"></a>
<a id="gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873"></a>
<a id="gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b"></a>
<a id="gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037"></a>
<a id="ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02"></a>
<a id="ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f"></a>
<a id="ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_DMA驱动后端接口.md)
