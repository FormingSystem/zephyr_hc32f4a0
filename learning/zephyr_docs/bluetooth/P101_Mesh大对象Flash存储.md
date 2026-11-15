---
id: learning.zephyr-docs.bluetooth.page-101
title: Mesh大对象Flash存储
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob_flash.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="blob-flash"></a>

<a id="bluetooth-mesh-blob-flash"></a>

# 第101章\_BLOB Flash 存储（BLOB Flash）

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh/blob_flash.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——网页与当前源码的接口差异：原页在读取器、写入器两处都使用 `bt_mesh_blob_flash_rd_init()`。本次读取的[官方头文件](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/include/zephyr/bluetooth/mesh/blob_io_flash.h)与[实现](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/subsys/bluetooth/mesh/blob_io_flash.c)提供统一的 `bt_mesh_blob_io_flash_init()`，并安装读写回调；不能只把原名称中的 `rd` 改成 `wr` 来推断接口。正文保留网页写法，实际调用应以所用版本为准。本仓库可通过[头文件](../../../include/zephyr/bluetooth/mesh/blob_io_flash.h)和[实现](../../../subsys/bluetooth/mesh/blob_io_flash.c)相对定位，版本可能不同。

BLOB Flash 读取器和写入器负责从 [Flash 映射（Flash map）](../storage/P001_Flash分区映射.md#flash-map-api)定义的分区中读取 BLOB，或向这些分区写入 BLOB。

<a id="blob-flash-reader"></a>

## 101.1 BLOB Flash 读取器（BLOB Flash Reader）

BLOB Flash 读取器与传输客户端交互，直接从 Flash 读取数据。交给客户端之前，必须调用 `bt_mesh_blob_flash_rd_init()` 初始化读取器。每个读取器同一时刻只支持一项传输。

<a id="blob-flash-writer"></a>

## 101.2 BLOB Flash 写入器（BLOB Flash Writer）

BLOB Flash 写入器与传输服务端交互，直接向 Flash 写入数据。原文要求在交给服务端之前调用 `bt_mesh_blob_flash_rd_init()` 初始化。每个写入器同一时刻只支持一项传输，且要求块大小是 Flash 页大小的整数倍。如果启动传输时的块大小小于 Flash 页大小，该传输将被拒绝。

为了处理未按 Flash 写入块大小对齐的 Chunk，写入器先将数据复制到缓冲区。如果 Chunk 的起始位置或长度未对齐，则用 `0xff` 填充缓冲区中的相应部分。

> 译注——Flash 行为随实现与器件而变：上段为官方网页原句。本次官方实现的普通写入路径使用设备报告的 `erase_value`；对无需显式擦除的存储器，还会先读取边界数据以保留 Chunk 外的字节。启用 `CONFIG_BT_MESH_BLOB_IO_FLASH_BLOCK_CACHE` 时则使用整块缓存路径。不要把网页中的 `0xff` 当作所有器件和配置通用的写入方法，源码依据见本章开头。

<a id="api-reference"></a>

## 101.3 API 参考（API Reference）

[蓝牙 Mesh BLOB Flash 流（Bluetooth Mesh BLOB flash stream）](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob__io__flash.html)

对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh/blob_flash.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh/blob_flash.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh/blob_flash.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建固件、运行认证测试或连接设备。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Mesh大对象传输服务端](P100_Mesh大对象传输服务端.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：Mesh设备固件更新](P102_Mesh设备固件更新.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P100_Mesh大对象传输服务端.md) · [返回大纲](大纲.md) · [下一章](P102_Mesh设备固件更新.md)

</details>

<!-- reading-navigation:end -->
