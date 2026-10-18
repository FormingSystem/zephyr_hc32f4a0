---
id: learning.zephyr-docs.board-samples.page-73
title: SmartDMA内存到内存传输
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/nxp/smartdma_mem_to_mem/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="nxp_smartdma_mem_to_mem"></a>

# 第73章\_NXP SmartDMA 内存到内存传输（NXP SmartDMA memory-to-memory）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/nxp/smartdma_mem_to_mem/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/nxp/smartdma_mem_to_mem/README.rst/..)

<a id="overview"></a>

## 73.1 概述（Overview）

本示例展示如何使用 NXP SmartDMA 协处理器执行内存到内存传输，数据传输路径无需 CPU 参与。

SmartDMA 是多种 NXP MCX 设备中的小型可编程协处理器，执行可直接操作系统内存的固件例程。本示例安装标准 MCUX SmartDMA 固件，并调用其中一个内存到内存例程：从内存读取源缓冲区，执行固件固定的字节变换，再将结果写入内存中的目标缓冲区。`kSMARTDMA_RGB565To888` 例程和 `smartdma_rgb565_rgb888_param_t` 类型是 SDK 为此例程定义的标识符；此处只将其作为演示 SmartDMA 内存到内存传输的机制。

> 译注——变换并非原样复制：输入是 32 个 16 位字，共 64 字节；输出每字展开为三个字节，共 96 字节。源码按低五位、中六位、高五位的顺序左移 3、2、3 位生成预期值，低位不作复制填充。因此不能把此例当作任意长度 memcpy，也不能只按 RGB565To888 名称推断输出字节顺序。

将 `dma_slot` 字段设为固件例程索引，即可通过 Zephyr DMA API 选择 SmartDMA 固件例程。固件从参数块读取源缓冲区、目标缓冲区、大小和私有栈；其地址由 SmartDMA 驱动根据 `dma_config.head_block` 设置。因此，本示例将 `head_block` 转用为指向固件参数结构的指针。

> 译注——驱动专用约定：本次 SmartDMA 驱动把 head_block 指针直接写入 ARM2EZH，并按 dma_slot 选择固件入口。将它转换为固件参数结构是该驱动约定，不能推广为所有 Zephyr DMA 驱动的 dma_block_config 用法；CPU 仍负责准备、启动和结果核验，只是没有参与传输数据路径。

例程完成时，SmartDMA 产生中断并调用 DMA 回调，示例据此获知传输结束。随后，示例在 CPU 上重新计算固件的字节变换，验证输出缓冲区是否匹配。

> 译注——完成判据：应用最多循环等待 1000 次、每次睡眠 1 ms；超时调用 dma_stop() 并报告错误，实际墙钟时间还包含调度开销。中断只标记完成，随后逐项比较输出；应同时检查 Result check passed 与 sample done，不能只看到 Transfer complete 就认定内容正确。

<a id="requirements"></a>

## 73.2 前提条件（Requirements）

本示例要求开发板具有 NXP SmartDMA 协处理器，并已启用其时钟。原文报告已在 [MCX-N9XX-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mcx_nx4x_evk/doc/mcx_n9xx_evk.html#mcx_n9xx_evk) 和 [MCX-N5XX-EVK](https://docs.zephyrproject.org/latest/boards/nxp/mcx_nx4x_evk/doc/mcx_n5xx_evk.html#mcx_n5xx_evk) 上测试。

<a id="building-and-running"></a>

## 73.3 构建与运行（Building and Running）

> 译注——执行前提：west 命令从读者的 Zephyr 源码根目录，在 UCRT64 Bash 或 Linux Bash 中执行；先按[入门指南](../getting_started/大纲.md)准备工具链、模块及对应板。构建产物由工具生成，下载与启动按具体板文档核对。本次未执行构建、烧录或硬件测量。

```text
west build -b mcx_n9xx_evk/mcxn947/cpu0 samples/boards/nxp/smartdma_mem_to_mem
west flash
```

<a id="sample-output"></a>

### 73.3.1 输出示例（Sample Output）

```text
Starting SmartDMA memory-to-memory transfer
Transfer complete, results:
word 0: in 0x0000 -> out 00 00 00
...
Result check passed: all 32 words transformed correctly
SmartDMA memory-to-memory sample done
```

<a id="see-also"></a>

## 73.4 另请参阅（See also）

[直接内存访问（Direct Memory Access，DMA）](../dma_reference/P001_DMA公共接口.md)

> 译注——源码入口：仓库相对参照：[src/main.c](../../../samples/boards/nxp/smartdma_mem_to_mem/src/main.c)；[prj.conf](../../../samples/boards/nxp/smartdma_mem_to_mem/prj.conf)；[drivers/dma/dma_mcux_smartdma.c](../../../drivers/dma/dma_mcux_smartdma.c)。本地版本可能与网页不同。

对应官方文档源码：[samples/boards/nxp/smartdma_mem_to_mem/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/nxp/smartdma_mem_to_mem/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/nxp/smartdma_mem_to_mem/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录或执行硬件实验。

[上一章](P072_FLEXRAM魔术地址.md) · [返回大纲](大纲.md) · [下一章](P074_DSP优化库计算.md)
