---
id: learning.zephyr-docs.storage.fssample-2
title: FatFs挂载表示例
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/fs/fatfs_fstab/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="fatfs-fstab"></a>

# 第82章\_FatFs挂载表示例

原文：[Fatfs filesystem fstab](https://docs.zephyrproject.org/latest/samples/subsys/fs/fatfs_fstab/README.html)。读取日期：2026-10-13，`latest`。

## 82.1\_示例用途

本示例演示如何在**设备树（Devicetree）**中定义 FatFs **文件系统挂载表（File System Table，fstab）**条目。场景使用**内存磁盘（RAM Disk）**上的 FatFs，运行于 `native_sim` 主机原生模拟目标。RAM 为随机存取存储器（Random-Access Memory），FatFs 是 FAT 文件系统实现；FAT 指文件分配表（File Allocation Table）。

[官方示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/subsys/fs/fatfs_fstab)。

## 82.2\_构建与运行

先构建 `native_sim` 目标，再运行构建目录中生成的可执行文件。`DTC_OVERLAY_FILE` 指定设备树覆盖文件（Devicetree Overlay），本例使用 `fatfs_fstab.overlay`。

译注：在已配置 Zephyr 环境的 Linux 开发终端中，从 Zephyr 源码根目录执行以下官方命令。

```shell
west build -b native_sim samples/subsys/fs/fatfs_fstab -- -DDTC_OVERLAY_FILE=fatfs_fstab.overlay
```

## 82.3\_预期输出

示例成功运行时应看到：

```console
I: Filesystem access successful
```

该行表示“文件系统访问成功”。原网页将控制台代码块指令显示为正文，此处恢复其排版意图并保留输出消息。本译文未构建或运行该示例。

相关参考：[文件系统接口](P033_文件系统接口.md)。

---

[上一章：Ext2挂载表示例](P081_Ext2挂载表示例.md) · [下一章：文件系统格式化示例](P083_文件系统格式化示例.md) · [返回大纲](大纲.md)
