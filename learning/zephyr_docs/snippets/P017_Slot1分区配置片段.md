---
id: learning.zephyr-docs.snippets.page-17
title: Slot1分区配置片段
kind: reference
status: maintained
domains: [zephyr, snippets, documentation]
source_url: https://docs.zephyrproject.org/latest/snippets/slot1-partition/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="slot1-partition-snippet-slot1-partition"></a>
<a id="snippet-slot1-partition"></a>

# 第17章\_Slot1分区配置片段

原文：[官方页面](https://docs.zephyrproject.org/latest/snippets/slot1-partition/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

原构建格式：

```sh
west build -S slot1-partition [...]
```

<a id="overview"></a>

## 17.1 概述（Overview）

本片段把所选闪存分区更改为`slot1_partition`节点，可用于为MCUboot直接原位执行（Direct Execute in Place，direct-xip）或固件加载器（Firmware Loader）模式中的备用槽位构建固件。

<a id="requirements"></a>

## 17.2 要求（Requirements）

设备树中的分区映射须正确设置，例如：

```dts
&flash0 {
	partitions {
		ranges;
		#address-cells = <1>;
		#size-cells = <1>;

		boot_partition: partition@0 {
			compatible = "zephyr,mapped-partition";
			label = "mcuboot";
			reg = <0x00000000 0x0000c000>;
		};

		slot0_partition: partition@c000 {
			compatible = "zephyr,mapped-partition";
			label = "image-0";
			reg = <0x0000c000 0x00076000>;
		};

		slot1_partition: partition@82000 {
			compatible = "zephyr,mapped-partition";
			label = "image-1";
			reg = <0x00082000 0x00076000>;
		};

		/*
		 * The flash starting at 0x000f8000 and ending at
		 * 0x000fffff is reserved for use by the application.
		 */

		/*
		 * Storage partition will be used by FCB/LittleFS/NVS
		 * if enabled.
		 */
		storage_partition: partition@f8000 {
			compatible = "zephyr,mapped-partition";
			label = "storage";
			reg = <0x000f8000 0x00008000>;
		};
	};
};
```

> 译注——原代码注释：从`0x000f8000`到`0x000fffff`的闪存保留给应用使用；启用相应功能时，存储分区供闪存循环缓冲区（Flash Circular Buffer，FCB）、LittleFS或非易失性存储（Non-Volatile Storage，NVS）使用。上述地址和大小属于原示例布局。

> 译注——片段作用：当前覆盖文件只把`zephyr,code-partition`改为`&slot1_partition`，不创建上述分区，也不自动配置引导程序、签名、升级流程或执行烧录。必须使用与目标硬件和所选MCUboot模式匹配的分区布局。


> 译注——片段源码：[snippet.yml](../../../snippets/slot1-partition/snippet.yml)、[slot1-partition.overlay](../../../snippets/slot1-partition/slot1-partition.overlay)。片段定义中的名称为`slot1-partition`；本地参照版本可能与所保存的官方main版本不同。

> 译注——构建占位符：原文`[...]`表示由读者补充的板目标、应用路径等构建参数，实际执行时不能保留方括号省略号。构建位置与片段搜索方法见[使用配置片段](P002_使用配置片段.md)。本文仅翻译和核对，没有执行这些命令。

对应官方文档源码：[snippets/slot1-partition/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/snippets/slot1-partition/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../snippets/slot1-partition/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P016_XIAO串口控制台配置片段.md) · [返回大纲](大纲.md) · [下一章](P018_原生模拟器SocketCAN配置片段.md)
