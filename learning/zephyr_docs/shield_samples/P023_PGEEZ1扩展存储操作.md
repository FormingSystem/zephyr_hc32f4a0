---
id: learning.zephyr-docs.shield-samples.page-23
title: PGEEZ1扩展存储操作
kind: reference
status: maintained
domains: [zephyr, shields, samples]
source_url: https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_pgeez1/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 官方示例源码署名：SPDX-FileCopyrightText: Copyright 2026 EXALT Technologies -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="x-nucleo-pgeez1"></a>

# 第23章\_X-NUCLEO-PGEEZ1：M95P32 扩展操作（Extended Operations）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/shields/x_nucleo_pgeez1/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/shields/x_nucleo_pgeez1/README.rst/..)

<a id="overview"></a>

## 23.1 概述（Overview）

本示例演示通过闪存 API 的 `flash_ex_op()` 扩展接口提供的 M95P32 专用闪存操作：

- 使用 `RDID`（0x83）读取 1024 字节标识区（Identification Area）。

> 译注——读取范围：标识区总大小是 1024 字节，分为两个 512 字节页。当前程序读取工厂页开头 16 字节、客户页开头 16 字节，并单独读取跨界窗口；它没有一次性导出整个 1024 字节区域。客户页写入偏移使用整个标识区的坐标，因此起点是 0x200，不是 0。

- 使用 `WRID`（0x82）在客户标识页（Customer Identification Page）写入并回读一个数据模式，验证跨越该页边界的写入会被拒绝。

> 译注——边界测试：跨页读取从 0x1f8 开始读取 16 字节，跨过工厂／客户页边界 0x200；拒绝写入测试则从 0x3f8 开始尝试写入 16 字节，跨过标识区末尾 0x400，并要求返回 -EINVAL。这是两个不同边界。

- 跨越工厂标识页与客户标识页之间的边界读取数据。

- 在两个分别擦除的 64 KiB 主存储阵列（Main Array）区域上，比较 `flash_write()` 的标准页编程与 `PGPR`（0x0A）的带缓冲加载页编程（Page Program with Buffer Load）。示例仅测量每次写入调用的耗时，再读回两个区域，核对内容。

带缓冲加载页编程操作在内部通过易失性寄存器（Volatile Register）开启和关闭 M95P32 的缓冲模式；公共 API 不提供直接访问该寄存器的接口。

警告（Warning）

本示例会修改偏移 0x200 处的客户标识页，并擦除 0x3e0000～0x3fffff 范围内的主存储阵列。如果该区域有必须保留的数据，不要运行本示例。

> 译注——实际写入：程序先用 WRID 向 0x200～0x20f 写入 16 个 0xff，再写入固定测试字符串并比较回读值；这不是擦除整个客户标识页。两个 64 KiB 主阵列区域则通过 flash_erase() 分别擦除，并写入按 i ^ 0x5a 生成的数据模式。

<a id="building-and-running"></a>

## 23.2 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块和工具链，确认目标板、扩展板与待擦写区域。prj.conf 启用 CONFIG_FLASH_EX_OP_ENABLED 与 CONFIG_MSPI，flash0 别名定位到扩展板 M95P32。设备不就绪或扩展操作不可用时，回查板卡、shield、驱动版本与配置。本次仅翻译和读源码，未构建、烧录或擦写存储。

针对 NUCLEO-U575ZI-Q 开发板与 X-NUCLEO-PGEEZ1 扩展板构建示例：

```text
west build -b nucleo_u575zi_q --shield x_nucleo_pgeez1 samples/shields/x_nucleo_pgeez1
west flash
```

<a id="sample-output"></a>

## 23.3 示例输出（Sample Output）

> 译注——性能边界：程序分别计时两次写入调用，擦除与校验读取均不计入，再比较完整的 64 KiB 回读内容。缓冲模式按 512 字节页边界拆分数据，使上一页编程与下一页加载重叠；原文的 1.26 倍是该日志的一次结果，不保证其他平台相同。当前节省时间计算使用无符号的 standard_us - buffer_load_us；若缓冲模式反而更慢，该值会下溢，应先比较原始耗时，不能直接采用百分比。

```text
[00:00:00.000,000] <inf> ospi_stm32: MSPI config result: success
*** Booting Zephyr OS build v4.4.0-11617-g2189ec6da640 ***
M95P32 extended operation test

==================== READ: Factory identification page ====================
Identification page [0x000..0x00f]: 20 00 16 00 ff ff ff ff ff ff ff ff ff ff ff ff

==================== READ: Customer identification page before clear ====================
Customer identification page before WRID [0x200..0x20f]: 4d 39 35 50 33 32 2d 65 78 2d 6f 70 2d 74 65 73

==================== WRITE: Clear customer identification page ====================
Clearing customer identification page [0x200..0x20f]: ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff

==================== READ: Customer identification page after clear ====================
Customer identification page after clear [0x200..0x20f]: ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff ff

==================== WRITE: Customer identification page ====================
Writing customer identification page [0x200..0x20f]: 4d 39 35 50 33 32 2d 65 78 2d 6f 70 2d 74 65 73

==================== READ: Customer identification page after WRID ====================
Customer identification page after WRID [0x200..0x20f]: 4d 39 35 50 33 32 2d 65 78 2d 6f 70 2d 74 65 73

==================== READ: Identification page boundary ====================
Identification page boundary [0x1f8..0x207]: ff ff ff ff ff ff ff ff 4d 39 35 50 33 32 2d 65

==================== WRITE: Cross-page protection ====================
Cross-page WRID protection passed

Identification page read/write passed

==================== PREPARE: Erase write benchmark regions ====================

==================== WRITE: Standard page program ====================
Standard page program data verification passed

==================== WRITE: Page program with buffer load ====================
Page program with buffer load data verification passed

==================== RESULT: Write performance ====================
Standard page program (65536 bytes): 21752449 cycles, 0.135952 s
Page program with buffer load (65536 bytes): 17151523 cycles, 0.107197 s
Page-program-with-buffer-load speedup: 1.26x (21.1% less write time)
M95P32 extended operation test passed
```

<a id="see-also"></a>

## 23.4 另请参阅（See also）

[闪存（Flash）](../flash_reference/P001_Flash公共接口.md)

[ST M95P32](../flash_reference/P011_M95P32扩展操作接口.md)

> 译注——源码入口：[samples/shields/x_nucleo_pgeez1/src/main.c（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/x_nucleo_pgeez1/src/main.c)；[samples/shields/x_nucleo_pgeez1/prj.conf（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/x_nucleo_pgeez1/prj.conf)；[boards/shields/x_nucleo_pgeez1/x_nucleo_pgeez1.overlay](../../../boards/shields/x_nucleo_pgeez1/x_nucleo_pgeez1.overlay)；[include/zephyr/drivers/flash/m95p32_flash_api_extensions.h（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/drivers/flash/m95p32_flash_api_extensions.h)；[drivers/flash/flash_mspi_nor_quirks_m95p32.h（上游）](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/drivers/flash/flash_mspi_nor_quirks_m95p32.h)。本地源码按相对路径定位，缺少的文件链接上游快照来源；各版本可能不同。

对应官方文档源码：[samples/shields/x_nucleo_pgeez1/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/shields/x_nucleo_pgeez1/README.rst)。

[上一章](P022_IKS4A1示例目录.md) · [返回大纲](大纲.md) · [下一章](P024_扩展板示例目录.md)
