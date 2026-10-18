---
id: learning.zephyr-docs.peripheral-bus-storage-model-reference.page-5
title: disk_operations_结构体
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structdisk__operations.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_disk\_operations\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structdisk__operations.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘操作（Disk Operations）。

```c
#include <zephyr/drivers/disk.h>
```

<a id="details"></a>

磁盘操作（Disk Operations）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 5.1\_数据成员（Data Fields）

<a id="r_ad944962a397c3427b4b6331518d6eb8b"></a>

```c
int(* init )(struct disk_info *disk)
```

相关声明：[init](#ad944962a397c3427b4b6331518d6eb8b)、[disk_info](P004_disk_info_结构体.md)。

<a id="r_acd7d82f4d65ae8badd5005ae3a21bf44"></a>

```c
int(* status )(struct disk_info *disk)
```

相关声明：[status](#acd7d82f4d65ae8badd5005ae3a21bf44)、[disk_info](P004_disk_info_结构体.md)。

<a id="r_a2899499e982a861f41d02fa2e856b753"></a>

```c
int(* read )(struct disk_info *disk, uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[read](#a2899499e982a861f41d02fa2e856b753)、[disk_info](P004_disk_info_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_ad74bec53a1ef7dc159b1ca90dd3c5a91"></a>

```c
int(* write )(struct disk_info *disk, const uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[write](#ad74bec53a1ef7dc159b1ca90dd3c5a91)、[disk_info](P004_disk_info_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a9fd72e76cd9bd31103a7a3d180710132"></a>

```c
int(* erase )(struct disk_info *disk, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[erase](#a9fd72e76cd9bd31103a7a3d180710132)、[disk_info](P004_disk_info_结构体.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

<a id="r_a890f3f9e912b7e0b56fa105f82608f97"></a>

```c
int(* ioctl )(struct disk_info *disk, uint8_t cmd, void *buff)
```

相关声明：[ioctl](#a890f3f9e912b7e0b56fa105f82608f97)、[disk_info](P004_disk_info_结构体.md)、[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

## 5.2\_详细说明（Detailed Documentation）

<a id="a9fd72e76cd9bd31103a7a3d180710132"></a>

### `erase`

```c
int(* disk_operations::erase) (struct disk_info *disk, uint32_t start_sector, uint32_t num_sector)
```

<a id="ad944962a397c3427b4b6331518d6eb8b"></a>

### `init`

```c
int(* disk_operations::init) (struct disk_info *disk)
```

<a id="a890f3f9e912b7e0b56fa105f82608f97"></a>

### `ioctl`

```c
int(* disk_operations::ioctl) (struct disk_info *disk, uint8_t cmd, void *buff)
```

<a id="a2899499e982a861f41d02fa2e856b753"></a>

### `read`

```c
int(* disk_operations::read) (struct disk_info *disk, uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

<a id="acd7d82f4d65ae8badd5005ae3a21bf44"></a>

### `status`

```c
int(* disk_operations::status) (struct disk_info *disk)
```

<a id="ad74bec53a1ef7dc159b1ca90dd3c5a91"></a>

### `write`

```c
int(* disk_operations::write) (struct disk_info *disk, const uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

本数据类型文档由以下文件生成：

- `zephyr/drivers/disk.h`

## 5.3\_原页交叉引用（Cross References）

- [zephyr/drivers/disk.h](https://docs.zephyrproject.org/latest/doxygen/html/disk_8h_source.html)
- [disk_info](P004_disk_info_结构体.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P004_disk_info_结构体.md) · [返回大纲](大纲.md) · [下一章](P006_espi_cfg_结构体.md)
