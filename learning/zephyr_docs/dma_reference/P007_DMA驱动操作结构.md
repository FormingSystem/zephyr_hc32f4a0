---
id: learning.zephyr-docs.dma-reference.page-7
title: DMA驱动操作结构
kind: reference
status: maintained
domains: [zephyr, dma, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdma__driver__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_DMA驱动操作结构

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdma__driver__api.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：本页是直接内存访问（Direct Memory Access，DMA）应用程序接口（Application Programming Interface，API）参考。先读[DMA概述](../hardware/P011_DMA直接内存访问.md)，再按[本册大纲](大纲.md)区分通道配置（Channel Configuration）、传输块（Transfer Block）、运行状态（Runtime Status）与驱动后端（Driver Backend）。原始标识符、类型与常量保持不变；重复的接口摘要与详细说明均保留。

驱动操作（Driver Operations）：DMA驱动操作。

```c
#include <zephyr/drivers/dma.h>
```

<a id="details"></a>

驱动操作（Driver Operations）：DMA驱动操作。这是每个DMA驱动都需要定义的驱动API结构，包含驱动所实现操作的函数指针，以及其他驱动专用常量数据。标为REQ的成员必须由驱动设置，标为OPT的成员则为可选。另请参阅DEVICE_DT_INST_DEFINE()、DEVICE_DT_DEFINE()和DEVICE_API()。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a0a2ca7aae0cf9bc65d34c2332c646296"></a>

```c
dma_api_config config
```

相关声明：[dma_api_config](P002_DMA驱动后端接口.md#gab15e273c0f3b1978d17ad448d98f56bb)、[config](#a0a2ca7aae0cf9bc65d34c2332c646296)。

必需（REQ）：DMA配置结构。

<a id="r_a5fb4a9ee5dbffb3d71a5bc1b81c5728b"></a>

```c
dma_api_reload reload
```

相关声明：[dma_api_reload](P002_DMA驱动后端接口.md#gab00e7199fa8dafa541e4ef5f63c391b4)、[reload](#a5fb4a9ee5dbffb3d71a5bc1b81c5728b)。

可选（OPT）：重新装载DMA通道的缓冲区。

<a id="r_a812b5d3118965c0387f362de31b6debb"></a>

```c
dma_api_start start
```

相关声明：[dma_api_start](P002_DMA驱动后端接口.md#ga1cd1fc992eb0e95690a50e2696247da0)、[start](#a812b5d3118965c0387f362de31b6debb)。

必需（REQ）：使能DMA通道并启动传输；必须事先配置该通道。

<a id="r_a282e408e1fee4f63dea11a8b10e43986"></a>

```c
dma_api_stop stop
```

相关声明：[dma_api_stop](P002_DMA驱动后端接口.md#gad63e7dc2e41adc03f4a338bda760f2ff)、[stop](#a282e408e1fee4f63dea11a8b10e43986)。

可选（OPT）：停止DMA传输并禁用通道。

<a id="r_a56d9d2f5dfe9638691c43dd2e8a9a84d"></a>

```c
dma_api_suspend suspend
```

相关声明：[dma_api_suspend](P002_DMA驱动后端接口.md#gad3742f6c4218b6a648e9aa5734516818)、[suspend](#a56d9d2f5dfe9638691c43dd2e8a9a84d)。

可选（OPT）：挂起DMA通道传输。

<a id="r_ad51378a0d3e4f74ecb9c56e85984aec2"></a>

```c
dma_api_resume resume
```

相关声明：[dma_api_resume](P002_DMA驱动后端接口.md#ga5073bb15b75cbbbcdbd3f859f28e3473)、[resume](#ad51378a0d3e4f74ecb9c56e85984aec2)。

可选（OPT）：恢复DMA通道传输。

<a id="r_ac526f6bca144e3fa4366b232cd694a1c"></a>

```c
dma_api_get_status get_status
```

相关声明：[dma_api_get_status](P002_DMA驱动后端接口.md#ga06781c37590c23e6df82471aac4923dc)、[get_status](#ac526f6bca144e3fa4366b232cd694a1c)。

可选（OPT）：取得DMA传输的当前运行状态。

<a id="r_aebc286d4576223b1d1873d5b0ebe225e"></a>

```c
dma_api_get_attribute get_attribute
```

相关声明：[dma_api_get_attribute](P002_DMA驱动后端接口.md#ga2cc72d829ce7f47eb2a326faaedf3fc5)、[get_attribute](#aebc286d4576223b1d1873d5b0ebe225e)。

可选（OPT）：取得DMA控制器属性。

<a id="r_a6c5e9147e23ab14ff00c35da101ab5c3"></a>

```c
dma_api_chan_filter chan_filter
```

相关声明：[dma_api_chan_filter](P002_DMA驱动后端接口.md#ga1c65fe109d52e477f3bafa56e4afefb7)、[chan_filter](#a6c5e9147e23ab14ff00c35da101ab5c3)。

可选（OPT）：DMA通道筛选器。

<a id="r_a2daa5d977f3d62b910bcd188d9fe535c"></a>

```c
dma_api_chan_release chan_release
```

相关声明：[dma_api_chan_release](P002_DMA驱动后端接口.md#ga035b4982cae52df4ce1911ad007d3a64)、[chan_release](#a2daa5d977f3d62b910bcd188d9fe535c)。

可选（OPT）：释放申请阶段分配的通道资源。

## 7.2\_详细说明（Detailed Documentation）

<a id="a6c5e9147e23ab14ff00c35da101ab5c3"></a>

### `chan_filter`

```c
dma_api_chan_filter dma_driver_api::chan_filter
```

可选（OPT）：DMA通道筛选器。

<a id="a2daa5d977f3d62b910bcd188d9fe535c"></a>

### `chan_release`

```c
dma_api_chan_release dma_driver_api::chan_release
```

可选（OPT）：释放申请阶段分配的通道资源。

详情见dma_release_channel()。

<a id="a0a2ca7aae0cf9bc65d34c2332c646296"></a>

### `config`

```c
dma_api_config dma_driver_api::config
```

必需（REQ）：DMA配置结构。

> 译注——源码核对：本成员类型为dma_api_config函数指针；官方由同名符号复制摘要而显示“DMA配置结构”，不表示该成员嵌入一个struct dma_config对象。驱动须提供配置操作。

<a id="aebc286d4576223b1d1873d5b0ebe225e"></a>

### `get_attribute`

```c
dma_api_get_attribute dma_driver_api::get_attribute
```

可选（OPT）：取得DMA控制器属性。

<a id="ac526f6bca144e3fa4366b232cd694a1c"></a>

### `get_status`

```c
dma_api_get_status dma_driver_api::get_status
```

可选（OPT）：取得DMA传输的当前运行状态。

<a id="a5fb4a9ee5dbffb3d71a5bc1b81c5728b"></a>

### `reload`

```c
dma_api_reload dma_driver_api::reload
```

可选（OPT）：重新装载DMA通道的缓冲区。

<a id="ad51378a0d3e4f74ecb9c56e85984aec2"></a>

### `resume`

```c
dma_api_resume dma_driver_api::resume
```

可选（OPT）：恢复DMA通道传输。

<a id="a812b5d3118965c0387f362de31b6debb"></a>

### `start`

```c
dma_api_start dma_driver_api::start
```

必需（REQ）：使能DMA通道并启动传输；必须事先配置该通道。

<a id="a282e408e1fee4f63dea11a8b10e43986"></a>

### `stop`

```c
dma_api_stop dma_driver_api::stop
```

可选（OPT）：停止DMA传输并禁用通道。

<a id="a56d9d2f5dfe9638691c43dd2e8a9a84d"></a>

### `suspend`

```c
dma_api_suspend dma_driver_api::suspend
```

可选（OPT）：挂起DMA通道传输。

## 7.3\_源码定位与版本边界

接口、配置结构和内联包装均可在仓库的[dma.h](../../../include/zephyr/drivers/dma.h)中相对定位。本次译注核对了[官方main头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/dma.h)，摘要见[来源记录](../SOURCES.md)；本地源码、滚动更新的main与latest网页不能自动视为同一版本。原始头文件法律署名为Copyright (c) 2016 Intel Corporation，许可证为Apache-2.0。

> 译注——必需与可选：config和start由公共包装直接调用；reload、stop、suspend、resume、get_status、get_attribute等可选操作不存在时相应包装返回-ENOSYS。没有chan_filter时，dma_request_channel仍可接受空闲通道，而直接调用dma_chan_filter会返回-ENOSYS。停止传输与释放申请资源是不同操作。

本批只翻译和核对官方源码，没有构建、执行DMA搬运、运行驱动测试或进行实板验证；这组参考也不声明本仓库已实现HC32 DMA驱动。

## 7.4\_原页交叉引用（Cross References）

- [zephyr/drivers/dma.h](P010_DMA驱动头文件源码.md)
- [dma_api_config](P002_DMA驱动后端接口.md#gab15e273c0f3b1978d17ad448d98f56bb)
- [dma_api_reload](P002_DMA驱动后端接口.md#gab00e7199fa8dafa541e4ef5f63c391b4)
- [dma_api_start](P002_DMA驱动后端接口.md#ga1cd1fc992eb0e95690a50e2696247da0)
- [dma_api_stop](P002_DMA驱动后端接口.md#gad63e7dc2e41adc03f4a338bda760f2ff)
- [dma_api_suspend](P002_DMA驱动后端接口.md#gad3742f6c4218b6a648e9aa5734516818)
- [dma_api_resume](P002_DMA驱动后端接口.md#ga5073bb15b75cbbbcdbd3f859f28e3473)
- [dma_api_get_status](P002_DMA驱动后端接口.md#ga06781c37590c23e6df82471aac4923dc)
- [dma_api_get_attribute](P002_DMA驱动后端接口.md#ga2cc72d829ce7f47eb2a326faaedf3fc5)
- [dma_api_chan_filter](P002_DMA驱动后端接口.md#ga1c65fe109d52e477f3bafa56e4afefb7)
- [dma_api_chan_release](P002_DMA驱动后端接口.md#ga035b4982cae52df4ce1911ad007d3a64)
- [DEVICE_DT_INST_DEFINE()](../device_reference/P001_设备模型公共接口.md#gada5ba4aca9e0662ccebb2232c7256419)
- [DEVICE_DT_DEFINE()](../device_reference/P001_设备模型公共接口.md#gac49e26fbe91a14307d5ea08d41561dd1)
- [DEVICE_API()](../device_reference/P007_设备模型头文件参考.md#aa0cdc799fc0b9c80eb29f989eec86707)
- [dma_release_channel()](P001_DMA公共接口.md#ga93b49d4d0910ceed88fa8aaa22b73098)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_DMA通道分配上下文.md) · [返回大纲](大纲.md) · [下一章](P008_DMA设备树宏.md)
