---
id: learning.zephyr-docs.api-extension-topic-reference.page-11
title: Xilinx ADMA 专用功能（Specifics）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_Xilinx ADMA 专用功能（Specifics）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__dma__xilinx__adma.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.1\_宏定义（Macros）

<a id="r_ga0f6ec265ce1ffc6a072e4ea1fa598864"></a>

```c
#define XILINX_ADMA_DIR_WRITE_ONLY (DMA_CHANNEL_DIRECTION_PRIV_START)
```

相关声明：[XILINX_ADMA_DIR_WRITE_ONLY](#ga0f6ec265ce1ffc6a072e4ea1fa598864)、[DMA_CHANNEL_DIRECTION_PRIV_START](../dma_reference/P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)。

只写模式（Write-Only Mode）的通道方向（Channel Direction）。

## 11.2\_详细说明（Detailed Documentation）

<a id="ga0f6ec265ce1ffc6a072e4ea1fa598864"></a>

### `XILINX_ADMA_DIR_WRITE_ONLY`

```c
#define XILINX_ADMA_DIR_WRITE_ONLY (DMA_CHANNEL_DIRECTION_PRIV_START)
```

```c
#include <zephyr/drivers/dma/dma_xilinx_adma.h>
```

只写模式（Write-Only Mode）的通道方向（Channel Direction）。

通道（Channel）不会从实际源复制数据，而是按照目标地址和大小（Destination Address / Size），重复写入固定模式（Fixed Pattern）。

将 `dma_config.channel_direction` 设置为此值，并使 `dma_block_config.source_address` 指向一个 8 字节（2 × `uint32_t`）的模式缓冲区（Pattern Buffer），而不是实际源缓冲区（Source Buffer）。不能与分散／聚集传输（Scatter-Gather，即多块 Multi-Block 传输）一起使用。


## 11.3\_原页交叉引用（Cross References）

- [DMA_CHANNEL_DIRECTION_PRIV_START](../dma_reference/P001_DMA公共接口.md#ggae442d8ba73be7e53b68165647b0ea402a273f9cdcc2af613375cb3e235bfda037)
- [zephyr/drivers/dma/dma_xilinx_adma.h](../api_file_supplement_reference/P022_zephyr__drivers__dma__dma_xilinx_adma.h_文件参考.md)
- [dma_config.channel_direction](../dma_reference/P004_DMA通道配置.md#aaf903b1badff8b0fc4ef18a34c2773d7)
- [dma_block_config.source_address](../dma_reference/P003_DMA传输块配置.md#a9fbd1deae8936a806ecc79bad3f3b9bb)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[上一章](P010_DALI 驱动后端 API（Driver Backend API）.md) · [返回大纲](大纲.md) · [下一章](P012_ExplorIR-M API主题.md)
