---
id: learning.zephyr-docs.api-input-runtime-topic-reference.page-6
title: 磁盘访问接口（Disk Access Interface）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_磁盘访问接口（Disk Access Interface）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__disk__access__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

磁盘访问 API（Disk Access APIs）

<a id="details"></a>

磁盘访问 API（Disk Access APIs）

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 6.1\_枚举（Enumerations）

<a id="r_gab666eac293bae609ee600ebb2b105373"></a>

```c
enum disk_access_erase_type { DISK_ACCESS_ERASE_PHYSICAL = 0 }
```

相关声明：[disk_access_erase_type](#gab666eac293bae609ee600ebb2b105373)、[DISK_ACCESS_ERASE_PHYSICAL](#ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6)。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.2\_函数（Functions）

<a id="r_gaba3fead8c0ce65945b440bf824fd4144"></a>

```c
int disk_access_init (const char *pdrv)
```

相关声明：[disk_access_init](#gaba3fead8c0ce65945b440bf824fd4144)。

执行所需的初始化。

<a id="r_gac5348a854fe68a607672118c91346133"></a>

```c
int disk_access_status (const char *pdrv)
```

相关声明：[disk_access_status](#gac5348a854fe68a607672118c91346133)。

获取磁盘状态（disk status）。

<a id="r_ga5152825bf2a70902e65dbc596a944a1b"></a>

```c
int disk_access_read (const char *pdrv, uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[disk_access_read](#ga5152825bf2a70902e65dbc596a944a1b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从磁盘读取数据。

<a id="r_gaa0495600320a71ea9e861fcf19da7184"></a>

```c
int disk_access_write (const char *pdrv, const uint8_t *data_buf, uint32_t start_sector, uint32_t num_sector)
```

相关声明：[disk_access_write](#gaa0495600320a71ea9e861fcf19da7184)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向磁盘写入数据。

<a id="r_gafb8528762248a3dcbe7e4d0a9ee31890"></a>

```c
int disk_access_erase (const char *pdrv, uint32_t start_sector, uint32_t num_sector, enum disk_access_erase_type erase_type)
```

相关声明：[disk_access_erase](#gafb8528762248a3dcbe7e4d0a9ee31890)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[disk_access_erase_type](#gab666eac293bae609ee600ebb2b105373)。

从磁盘擦除数据。

<a id="r_ga152d85821d73644fea7ffde27b7c953c"></a>

```c
int disk_access_ioctl (const char *pdrv, uint8_t cmd, void *buff)
```

相关声明：[disk_access_ioctl](#ga152d85821d73644fea7ffde27b7c953c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)。

获取／配置磁盘参数（disk parameters）。

## 6.3\_详细说明（Detailed Documentation）

<a id="gab666eac293bae609ee600ebb2b105373"></a>

### `disk_access_erase_type`

```c
enum disk_access_erase_type
```

```c
#include <zephyr/storage/disk_access.h>
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DISK_ACCESS_ERASE_PHYSICAL` | 将磁盘上的物理字节擦除为其自然擦除值（Natural Erase Value），即 `0x00` 或 `0xFF`。 |

<a id="gafb8528762248a3dcbe7e4d0a9ee31890"></a>

### `disk_access_erase()`

```c
int disk_access_erase ( const char * pdrv, uint32_t start_sector, uint32_t num_sector, enum disk_access_erase_type erase_type )
```

```c
#include <zephyr/storage/disk_access.h>
```

从磁盘擦除数据。

操作结果取决于 `erase_type` 指定的擦除类型（Erase Type）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |
| `[in] start_sector` | 要擦除的起始磁盘扇区（Start Disk Sector）。 |
| `[in] num_sector` | 要擦除的磁盘扇区数量（Number of Disk Sectors）。 |
| `[in] erase_type` | 要执行的擦除类型（Erase Type）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gaba3fead8c0ce65945b440bf824fd4144"></a>

### `disk_access_init()`

```c
int disk_access_init ( const char * pdrv)
```

```c
#include <zephyr/storage/disk_access.h>
```

执行所需的初始化。

使用者在执行任何 I/O 调用之前调用此接口，使磁盘或后端设备完成初始化。虽然为兼容旧代码仍保留此接口，但应改用 `disk_access_ioctl` 并指定 `DISK_IOCTL_CTRL_INIT`。

磁盘初始化采用引用计数（Reference Counting）；仅第一次成功初始化未初始化或此前已反初始化磁盘的调用，才会真正执行初始化。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga152d85821d73644fea7ffde27b7c953c"></a>

### `disk_access_ioctl()`

```c
int disk_access_ioctl ( const char * pdrv, uint8_t cmd, void * buff )
```

```c
#include <zephyr/storage/disk_access.h>
```

获取／配置磁盘参数（disk parameters）。

获取磁盘参数（Disk Parameters）及发出特殊设备请求的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |
| `[in] cmd` | 描述请求的 `DISK_IOCTL_*` 代码。 |
| `[in] buff` | 命令数据缓冲区（Command Data Buffer）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="ga5152825bf2a70902e65dbc596a944a1b"></a>

### `disk_access_read()`

```c
int disk_access_read ( const char * pdrv, uint8_t * data_buf, uint32_t start_sector, uint32_t num_sector )
```

```c
#include <zephyr/storage/disk_access.h>
```

从磁盘读取数据。

将数据从磁盘读取到内存缓冲区（Memory Buffer）的函数。

**注意（Note）：**若磁盘为 NVMe 类型，用户必须确保 `data_buf` 指针按 4 字节对齐（4-byte Aligned）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |
| `[in] data_buf` | 指向接收数据的内存缓冲区（Memory Buffer）的指针。 |
| `[in] start_sector` | 开始读取的磁盘扇区（Start Disk Sector）。 |
| `[in] num_sector` | 要读取的磁盘扇区数量（Number of Disk Sectors）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。

<a id="gac5348a854fe68a607672118c91346133"></a>

### `disk_access_status()`

```c
int disk_access_status ( const char * pdrv)
```

```c
#include <zephyr/storage/disk_access.h>
```

获取磁盘状态（disk status）。

本调用用于获取磁盘状态（Disk Status）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |

**返回（Returns）**：**返回值（Returns）：**`DISK_STATUS_OK` 或其他 `DISK_STATUS_*` 值。

<a id="gaa0495600320a71ea9e861fcf19da7184"></a>

### `disk_access_write()`

```c
int disk_access_write ( const char * pdrv, const uint8_t * data_buf, uint32_t start_sector, uint32_t num_sector )
```

```c
#include <zephyr/storage/disk_access.h>
```

向磁盘写入数据。

将数据从内存缓冲区（Memory Buffer）写入磁盘的函数。

**注意（Note）：**若磁盘为 NVMe 类型，用户必须确保 `data_buf` 指针按 4 字节对齐（4-byte Aligned）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] pdrv` | 磁盘名称（Disk name）。 |
| `[in] data_buf` | 指向内存缓冲区（Memory Buffer）的指针。 |
| `[in] start_sector` | 开始写入的磁盘扇区（Start Disk Sector）。 |
| `[in] num_sector` | 要写入的磁盘扇区数量（Number of Disk Sectors）。 |

**返回（Returns）**：成功返回 0，失败返回负的 errno 错误码。


## 6.4\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [zephyr/storage/disk_access.h](../api_file_system_device_reference/P007_zephyr__storage__disk_access.h_文件参考.md)
- [DISK_IOCTL_CTRL_INIT](../api_connection_topic_reference/P008_磁盘访问（Disk Access）.md#ga9def34b23915a3ce6c9a8a746d3d1372)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggab666eac293bae609ee600ebb2b105373ab78aa619814300a71ef45643e3d01ab6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_控制台 API（Console API）.md) · [返回大纲](大纲.md) · [下一章](P007_Grove 显示器（Grove display）.md)
