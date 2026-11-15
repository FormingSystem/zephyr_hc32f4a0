---
id: learning.zephyr-docs.dma-reference.page-9
title: DMA驱动头文件参考
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_DMA驱动头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/drivers_2dma_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

DMA（Direct Memory Access，直接内存访问）驱动API的主头文件。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
#include <zephyr/device.h>
```

[查看此文件的源码。](P010_DMA驱动头文件源码.md)

DMA（Direct Memory Access，直接内存访问）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 9.1\_数据结构（Data Structures）

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

<a id="r_dma_5Fdriver_5Fapi"></a>

```c
struct dma_driver_api
```

相关声明：[dma_driver_api](P007_DMA驱动操作结构.md)。

驱动操作（Driver Operations）：DMA驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 9.2\_宏定义（Macros）

<a id="r_gad4fc9a9c59f4e07c81a4c2f3b57c9ccb"></a>

```c
#define DMA_STATUS_COMPLETE 0
```

相关声明：[DMA_STATUS_COMPLETE](P001_DMA公共接口.md#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)。

在传输列表（Transfer List）完成时发生的DMA回调事件。

<a id="r_gab74c89289c8429071522cb89ac066eea"></a>

```c
#define DMA_STATUS_BLOCK 1
```

相关声明：[DMA_STATUS_BLOCK](P001_DMA公共接口.md#gab74c89289c8429071522cb89ac066eea)。

在传输列表中的单个传输块（Transfer Block）完成时发生的DMA回调事件。

<a id="r_gaa2544dbb8d5e36f413d47b61268daf1a"></a>

```c
#define DMA_STATUS_HALF_COMPLETE 2
```

相关声明：[DMA_STATUS_HALF_COMPLETE](P001_DMA公共接口.md#gaa2544dbb8d5e36f413d47b61268daf1a)。

在单个传输块完成一半时发生的DMA回调事件。

<a id="r_gae28ba5114dc2e9ecb89ccf9b623e938f"></a>

```c
#define DMA_MAGIC 0x47494749
```

相关声明：[DMA_MAGIC](P001_DMA公共接口.md#gae28ba5114dc2e9ecb89ccf9b623e938f)。

用于识别上下文内容的魔数（Magic Code）。

<a id="r_ga542e1a0fa0d851a51e4c8abf9a820e0c"></a>

```c
#define DMA_BUF_ADDR_ALIGNMENT(node)
```

相关声明：[DMA_BUF_ADDR_ALIGNMENT](P001_DMA公共接口.md#ga542e1a0fa0d851a51e4c8abf9a820e0c)。

取得描述缓冲区地址对齐（Buffer Address Alignment）的设备树属性。

<a id="r_ga76dfdfecc732319908f381883c630a2b"></a>

```c
#define DMA_BUF_SIZE_ALIGNMENT(node)
```

相关声明：[DMA_BUF_SIZE_ALIGNMENT](P001_DMA公共接口.md#ga76dfdfecc732319908f381883c630a2b)。

取得描述缓冲区大小对齐（Buffer Size Alignment）的设备树属性。

<a id="r_ga083e8b0a863b0833c55158053d286f15"></a>

```c
#define DMA_COPY_ALIGNMENT(node)
```

相关声明：[DMA_COPY_ALIGNMENT](P001_DMA公共接口.md#ga083e8b0a863b0833c55158053d286f15)。

取得描述最小可复制数据块（Minimum Copy Chunk）的设备树属性。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 9.3\_类型定义（Typedefs）

<a id="r_ga94745b4472ee1addd4f82db4e59e9fb5"></a>

```c
typedef void(* dma_callback_t) (const struct device *dev, void *user_data, uint32_t channel, int status)
```

相关声明：[dma_callback_t](P001_DMA公共接口.md#ga94745b4472ee1addd4f82db4e59e9fb5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

DMA传输完成回调函数（Callback）。

<a id="r_gab15e273c0f3b1978d17ad448d98f56bb"></a>

```c
typedef int(* dma_api_config) (const struct device *dev, uint32_t channel, struct dma_config *config)
```

相关声明：[dma_api_config](P002_DMA驱动后端接口.md#gab15e273c0f3b1978d17ad448d98f56bb)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_config](P004_DMA通道配置.md)。

为DMA传输配置单个通道（Channel）。

<a id="r_gab00e7199fa8dafa541e4ef5f63c391b4"></a>

```c
typedef int(* dma_api_reload) (const struct device *dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size)
```

相关声明：[dma_api_reload](P002_DMA驱动后端接口.md#gab00e7199fa8dafa541e4ef5f63c391b4)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

重新装载（Reload）DMA通道的缓冲区。

<a id="r_ga1cd1fc992eb0e95690a50e2696247da0"></a>

```c
typedef int(* dma_api_start) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_start](P002_DMA驱动后端接口.md#ga1cd1fc992eb0e95690a50e2696247da0)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

使能DMA通道并启动传输。

<a id="r_gad63e7dc2e41adc03f4a338bda760f2ff"></a>

```c
typedef int(* dma_api_stop) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_stop](P002_DMA驱动后端接口.md#gad63e7dc2e41adc03f4a338bda760f2ff)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

停止DMA传输并禁用通道。

<a id="r_gad3742f6c4218b6a648e9aa5734516818"></a>

```c
typedef int(* dma_api_suspend) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_suspend](P002_DMA驱动后端接口.md#gad3742f6c4218b6a648e9aa5734516818)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

挂起（Suspend）DMA通道传输。

<a id="r_ga5073bb15b75cbbbcdbd3f859f28e3473"></a>

```c
typedef int(* dma_api_resume) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_resume](P002_DMA驱动后端接口.md#ga5073bb15b75cbbbcdbd3f859f28e3473)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

恢复（Resume）DMA通道传输。

<a id="r_ga06781c37590c23e6df82471aac4923dc"></a>

```c
typedef int(* dma_api_get_status) (const struct device *dev, uint32_t channel, struct dma_status *status)
```

相关声明：[dma_api_get_status](P002_DMA驱动后端接口.md#ga06781c37590c23e6df82471aac4923dc)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_status](P005_DMA运行状态.md)。

取得DMA传输的当前运行时状态。

<a id="r_ga2cc72d829ce7f47eb2a326faaedf3fc5"></a>

```c
typedef int(* dma_api_get_attribute) (const struct device *dev, uint32_t type, uint32_t *value)
```

相关声明：[dma_api_get_attribute](P002_DMA驱动后端接口.md#ga2cc72d829ce7f47eb2a326faaedf3fc5)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得DMA控制器的属性。

<a id="r_ga1c65fe109d52e477f3bafa56e4afefb7"></a>

```c
typedef bool(* dma_api_chan_filter) (const struct device *dev, int channel, void *filter_param)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[dma_api_chan_filter](P002_DMA驱动后端接口.md#ga1c65fe109d52e477f3bafa56e4afefb7)、[device](../device_reference/P002_设备对象结构.md)。

通道筛选函数调用（Channel Filter）。

<a id="r_ga035b4982cae52df4ce1911ad007d3a64"></a>

```c
typedef void(* dma_api_chan_release) (const struct device *dev, uint32_t channel)
```

相关声明：[dma_api_chan_release](P002_DMA驱动后端接口.md#ga035b4982cae52df4ce1911ad007d3a64)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

通道释放函数调用（Channel Release）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 9.4\_枚举（Enumerations）

<a id="r_gae442d8ba73be7e53b68165647b0ea402"></a>

```c
enum dma_channel_direction { MEMORY_TO_MEMORY = 0x0 , MEMORY_TO_PERIPHERAL , PERIPHERAL_TO_MEMORY , PERIPHERAL_TO_PERIPHERAL , HOST_TO_MEMORY , MEMORY_TO_HOST , DMA_CHANNEL_DIRECTION_COMMON_COUNT , DMA_CHANNEL_DIRECTION_PRIV_START = DMA_CHANNEL_DIRECTION_COMMON_COUNT , DMA_CHANNEL_DIRECTION_MAX = 0x7 }
```

相关声明：[dma_channel_direction](P001_DMA公共接口.md#gae442d8ba73be7e53b68165647b0ea402)、[MEMORY_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)、[MEMORY_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)、[PERIPHERAL_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)、[PERIPHERAL_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)、[HOST_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)、[MEMORY_TO_HOST](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)、[DMA_CHANNEL_DIRECTION_COMMON_COUNT](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)、[DMA_CHANNEL_DIRECTION_PRIV_START](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)、[DMA_CHANNEL_DIRECTION_MAX](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)。

DMA通道传输方向（Channel Direction）。

<a id="r_gafe0877ef4bd7790a4bcd46052088231c"></a>

```c
enum dma_addr_adj { DMA_ADDR_ADJ_INCREMENT , DMA_ADDR_ADJ_DECREMENT , DMA_ADDR_ADJ_NO_CHANGE }
```

相关声明：[dma_addr_adj](P001_DMA公共接口.md#gafe0877ef4bd7790a4bcd46052088231c)、[DMA_ADDR_ADJ_INCREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)、[DMA_ADDR_ADJ_DECREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)、[DMA_ADDR_ADJ_NO_CHANGE](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)。

DMA地址调整方式（Address Adjustment）。

<a id="r_gade594552920aabbfd2106059a338498b"></a>

```c
enum dma_channel_filter { DMA_CHANNEL_NORMAL , DMA_CHANNEL_PERIODIC }
```

相关声明：[dma_channel_filter](P001_DMA公共接口.md#gade594552920aabbfd2106059a338498b)、[DMA_CHANNEL_NORMAL](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)、[DMA_CHANNEL_PERIODIC](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)。

DMA通道属性（Channel Attributes）。

<a id="r_ga08c366c8d47672eeeb37b258af20101b"></a>

```c
enum dma_attribute_type { DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT , DMA_ATTR_BUFFER_SIZE_ALIGNMENT , DMA_ATTR_COPY_ALIGNMENT , DMA_ATTR_MAX_BLOCK_COUNT }
```

相关声明：[dma_attribute_type](P001_DMA公共接口.md#ga08c366c8d47672eeeb37b258af20101b)、[DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)、[DMA_ATTR_BUFFER_SIZE_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)、[DMA_ATTR_COPY_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)、[DMA_ATTR_MAX_BLOCK_COUNT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)。

DMA属性（Attributes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 9.5\_函数（Functions）

<a id="r_ga6df1a6b89f271a0eae01c17b748bd2df"></a>

```c
static int dma_config (const struct device *dev, uint32_t channel, struct dma_config *config)
```

相关声明：[dma_config](P001_DMA公共接口.md#ga6df1a6b89f271a0eae01c17b748bd2df)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

为DMA传输配置单个通道（Channel）。

<a id="r_ga55bd5d550349c11c63ef47c2ed861f36"></a>

```c
static int dma_reload (const struct device *dev, uint32_t channel, uint32_t src, uint32_t dst, size_t size)
```

相关声明：[dma_reload](P001_DMA公共接口.md#ga55bd5d550349c11c63ef47c2ed861f36)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

重新装载（Reload）DMA通道的缓冲区。

<a id="r_gaf1184de07811702ffe89737b79e4a338"></a>

```c
static int dma_start (const struct device *dev, uint32_t channel)
```

相关声明：[dma_start](P001_DMA公共接口.md#gaf1184de07811702ffe89737b79e4a338)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

使能DMA通道并启动传输；必须事先配置该通道。

<a id="r_gafd602ee8386e10bb9ac7d386b3dc6a83"></a>

```c
static int dma_stop (const struct device *dev, uint32_t channel)
```

相关声明：[dma_stop](P001_DMA公共接口.md#gafd602ee8386e10bb9ac7d386b3dc6a83)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

停止DMA传输并禁用通道。

<a id="r_ga97bf9807b7fde7671a378333f01463d6"></a>

```c
static int dma_suspend (const struct device *dev, uint32_t channel)
```

相关声明：[dma_suspend](P001_DMA公共接口.md#ga97bf9807b7fde7671a378333f01463d6)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

挂起（Suspend）DMA通道传输。

<a id="r_ga1b1eeef68f1aa4818c9baf95b83b9e1e"></a>

```c
static int dma_resume (const struct device *dev, uint32_t channel)
```

相关声明：[dma_resume](P001_DMA公共接口.md#ga1b1eeef68f1aa4818c9baf95b83b9e1e)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

恢复（Resume）DMA通道传输。

<a id="r_gaadc34e0ea92d9fd2f1242789367b1dd5"></a>

```c
static int dma_request_channel (const struct device *dev, void *filter_param)
```

相关声明：[dma_request_channel](P001_DMA公共接口.md#gaadc34e0ea92d9fd2f1242789367b1dd5)、[device](../device_reference/P002_设备对象结构.md)。

申请DMA通道（Request Channel）。

<a id="r_ga93b49d4d0910ceed88fa8aaa22b73098"></a>

```c
static void dma_release_channel (const struct device *dev, uint32_t channel)
```

相关声明：[dma_release_channel](P001_DMA公共接口.md#ga93b49d4d0910ceed88fa8aaa22b73098)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

释放DMA通道（Release Channel）。

<a id="r_ga6d4c3e63bc4382215774e86893bc3072"></a>

```c
static int dma_chan_filter (const struct device *dev, int channel, void *filter_param)
```

相关声明：[dma_chan_filter](P001_DMA公共接口.md#ga6d4c3e63bc4382215774e86893bc3072)、[device](../device_reference/P002_设备对象结构.md)。

DMA通道筛选器（Channel Filter）。

<a id="r_ga2cae500f1f9ed42ad338a40ec8655544"></a>

```c
static int dma_get_status (const struct device *dev, uint32_t channel, struct dma_status *stat)
```

相关声明：[dma_get_status](P001_DMA公共接口.md#ga2cae500f1f9ed42ad338a40ec8655544)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_status](P005_DMA运行状态.md)、[stat](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)。

取得DMA传输的当前运行状态。

<a id="r_ga641f3fa492bfb17cf9f0a0361d429257"></a>

```c
static int dma_get_attribute (const struct device *dev, uint32_t type, uint32_t *value)
```

相关声明：[dma_get_attribute](P001_DMA公共接口.md#ga641f3fa492bfb17cf9f0a0361d429257)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

取得DMA控制器的属性。

<a id="r_gadd1724a843bba4ccc1c65c9fb9d3d921"></a>

```c
static uint32_t dma_width_index (uint32_t size)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_width_index](P001_DMA公共接口.md#gadd1724a843bba4ccc1c65c9fb9d3d921)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

查找用于寄存器的通用传输宽度索引（Width Index）。

<a id="r_gaac27f2ee664671884087ee3d2a2863ce"></a>

```c
static uint32_t dma_burst_index (uint32_t burst)
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[dma_burst_index](P001_DMA公共接口.md#gaac27f2ee664671884087ee3d2a2863ce)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

查找用于寄存器的通用突发传输索引（Burst Index）。

## 9.6\_源码定位与配置边界

本页为[公共DMA接口](P001_DMA公共接口.md)和[驱动后端](P002_DMA驱动后端接口.md)的头文件总览，详细参数与位字段说明见本册前七页，完整可见代码见[头文件源码](P010_DMA驱动头文件源码.md)。仓库相对定位：[drivers/dma.h](../../../include/zephyr/drivers/dma.h)。

> 译注——配置与实现：网页展示的是默认32位地址声明；源码页同时包含CONFIG_DMA_64BIT的64位分支。dma_chan_filter的布尔结果、dma_release_channel不自动停止传输，以及dma_burst_index的代码／注释不一致，均在[公共接口译注](P001_DMA公共接口.md)逐项说明，不能仅凭头文件摘要判断完整行为。

各页官方HTML及源码摘要见[来源记录](../SOURCES.md)。本地源码、main和latest不能自动视为同一版本；本批只翻译和核对，不编译设备树、运行DMA或进行实板验证。

## 9.7\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [Go to the source code of this file.](P010_DMA驱动头文件源码.md)
- [dma_block_config](P003_DMA传输块配置.md)
- [dma_config](P004_DMA通道配置.md)
- [dma_status](P005_DMA运行状态.md)
- [dma_context](P006_DMA通道分配上下文.md)
- [dma_driver_api](P007_DMA驱动操作结构.md)
- [DMA_STATUS_COMPLETE](P001_DMA公共接口.md#gad4fc9a9c59f4e07c81a4c2f3b57c9ccb)
- [DMA_STATUS_BLOCK](P001_DMA公共接口.md#gab74c89289c8429071522cb89ac066eea)
- [DMA_STATUS_HALF_COMPLETE](P001_DMA公共接口.md#gaa2544dbb8d5e36f413d47b61268daf1a)
- [DMA_MAGIC](P001_DMA公共接口.md#gae28ba5114dc2e9ecb89ccf9b623e938f)
- [DMA_BUF_ADDR_ALIGNMENT](P001_DMA公共接口.md#ga542e1a0fa0d851a51e4c8abf9a820e0c)
- [DMA_BUF_SIZE_ALIGNMENT](P001_DMA公共接口.md#ga76dfdfecc732319908f381883c630a2b)
- [DMA_COPY_ALIGNMENT](P001_DMA公共接口.md#ga083e8b0a863b0833c55158053d286f15)
- [dma_callback_t](P001_DMA公共接口.md#ga94745b4472ee1addd4f82db4e59e9fb5)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [dma_api_config](P002_DMA驱动后端接口.md#gab15e273c0f3b1978d17ad448d98f56bb)
- [dma_api_reload](P002_DMA驱动后端接口.md#gab00e7199fa8dafa541e4ef5f63c391b4)
- [dma_api_start](P002_DMA驱动后端接口.md#ga1cd1fc992eb0e95690a50e2696247da0)
- [dma_api_stop](P002_DMA驱动后端接口.md#gad63e7dc2e41adc03f4a338bda760f2ff)
- [dma_api_suspend](P002_DMA驱动后端接口.md#gad3742f6c4218b6a648e9aa5734516818)
- [dma_api_resume](P002_DMA驱动后端接口.md#ga5073bb15b75cbbbcdbd3f859f28e3473)
- [dma_api_get_status](P002_DMA驱动后端接口.md#ga06781c37590c23e6df82471aac4923dc)
- [dma_api_get_attribute](P002_DMA驱动后端接口.md#ga2cc72d829ce7f47eb2a326faaedf3fc5)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [dma_api_chan_filter](P002_DMA驱动后端接口.md#ga1c65fe109d52e477f3bafa56e4afefb7)
- [dma_api_chan_release](P002_DMA驱动后端接口.md#ga035b4982cae52df4ce1911ad007d3a64)
- [dma_channel_direction](P001_DMA公共接口.md#gae442d8ba73be7e53b68165647b0ea402)
- [MEMORY_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a52f28a5eff23fcddd2a138092d9f7cd5)
- [MEMORY_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a4617446ef0e7c2bced585b309011a25a)
- [PERIPHERAL_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a5fbc19c9e12c11973c0cf0a593ccf165)
- [PERIPHERAL_TO_PERIPHERAL](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae23cbfefccef9d19dd91f0c746004449)
- [HOST_TO_MEMORY](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a7e2b4150c28b057598975e95e8b7494c)
- [MEMORY_TO_HOST](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a61e65f3065bf7cdb40efc9039debbb60)
- [DMA_CHANNEL_DIRECTION_COMMON_COUNT](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402ae7c3dacfd3496576c41f9c663537419a)
- [DMA_CHANNEL_DIRECTION_PRIV_START](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)
- [DMA_CHANNEL_DIRECTION_MAX](P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a9114b4138c9dfb506b9428a229c55a02)
- [dma_addr_adj](P001_DMA公共接口.md#gafe0877ef4bd7790a4bcd46052088231c)
- [DMA_ADDR_ADJ_INCREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cac1fe38db8443f6d8e406c66ba6bdd15e)
- [DMA_ADDR_ADJ_DECREMENT](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231caacc38507d8ef3eb8021ae85d9b61b717)
- [DMA_ADDR_ADJ_NO_CHANGE](P001_DMA公共接口.md#ggafe0877ef4bd7790a4bcd46052088231cafeb870c1a6f9db8238a97f3ac9c6da4f)
- [dma_channel_filter](P001_DMA公共接口.md#gade594552920aabbfd2106059a338498b)
- [DMA_CHANNEL_NORMAL](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498ba54326b41a55d7a64c808cea83520b94f)
- [DMA_CHANNEL_PERIODIC](P001_DMA公共接口.md#ggade594552920aabbfd2106059a338498bacffe4591bb7577cd8596d4dc1b51838c)
- [dma_attribute_type](P001_DMA公共接口.md#ga08c366c8d47672eeeb37b258af20101b)
- [DMA_ATTR_BUFFER_ADDRESS_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101ba486ede0649882311fd344a52983d5f3f)
- [DMA_ATTR_BUFFER_SIZE_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa6b28cfc17b80884dddc18fcaa2b6873)
- [DMA_ATTR_COPY_ALIGNMENT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101baa07cc26d400fa919df133552eb2e317b)
- [DMA_ATTR_MAX_BLOCK_COUNT](P001_DMA公共接口.md#gga08c366c8d47672eeeb37b258af20101bafcaffeb0a1c7be27d258d73968196d18)
- [dma_config](P001_DMA公共接口.md#ga6df1a6b89f271a0eae01c17b748bd2df)
- [dma_reload](P001_DMA公共接口.md#ga55bd5d550349c11c63ef47c2ed861f36)
- [dma_start](P001_DMA公共接口.md#gaf1184de07811702ffe89737b79e4a338)
- [dma_stop](P001_DMA公共接口.md#gafd602ee8386e10bb9ac7d386b3dc6a83)
- [dma_suspend](P001_DMA公共接口.md#ga97bf9807b7fde7671a378333f01463d6)
- [dma_resume](P001_DMA公共接口.md#ga1b1eeef68f1aa4818c9baf95b83b9e1e)
- [dma_request_channel](P001_DMA公共接口.md#gaadc34e0ea92d9fd2f1242789367b1dd5)
- [dma_release_channel](P001_DMA公共接口.md#ga93b49d4d0910ceed88fa8aaa22b73098)
- [dma_chan_filter](P001_DMA公共接口.md#ga6d4c3e63bc4382215774e86893bc3072)
- [dma_get_status](P001_DMA公共接口.md#ga2cae500f1f9ed42ad338a40ec8655544)
- [stat](https://docs.zephyrproject.org/latest/doxygen/html/structstat.html)
- [dma_get_attribute](P001_DMA公共接口.md#ga641f3fa492bfb17cf9f0a0361d429257)
- [dma_width_index](P001_DMA公共接口.md#gadd1724a843bba4ccc1c65c9fb9d3d921)
- [dma_burst_index](P001_DMA公共接口.md#gaac27f2ee664671884087ee3d2a2863ce)

<a id="header-details"></a>

---

[上一章](P008_DMA设备树宏.md) · [返回大纲](大纲.md) · [下一章](P010_DMA驱动头文件源码.md)
