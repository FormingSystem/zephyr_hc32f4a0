---
id: learning.zephyr-docs.api-audio-path-topic-reference.page-5
title: 蓝牙 Mesh BLOB 模型 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第5章\_蓝牙 Mesh BLOB 模型 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>



<a id="header-files"></a>
<a id="files"></a>

## 5.1\_文件（Files）

<a id="r_blob_2Eh"></a>

```c
file blob.h
```

相关声明：[blob.h](../api_file_runtime_reference/P004_zephyr__bluetooth__mesh__blob.h_文件参考.md)。

蓝牙Mesh二进制大对象（BLOB）传输模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 5.2\_数据结构（Data Structures）

<a id="r_bt_5Fmesh_5Fblob_5Fblock"></a>

```c
struct bt_mesh_blob_block
```

相关声明：[bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)。

二进制大对象（BLOB）传输的数据块（Block）。

<a id="r_bt_5Fmesh_5Fblob_5Fchunk"></a>

```c
struct bt_mesh_blob_chunk
```

相关声明：[bt_mesh_blob_chunk](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md)。

二进制大对象（BLOB）的数据分片（Chunk）。

<a id="r_bt_5Fmesh_5Fblob_5Fxfer"></a>

```c
struct bt_mesh_blob_xfer
```

相关声明：[bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)。

二进制大对象传输（BLOB Transfer）。

<a id="r_bt_5Fmesh_5Fblob_5Fio"></a>

```c
struct bt_mesh_blob_io
```

相关声明：[bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)。

二进制大对象流（BLOB Stream）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 5.3\_宏定义（Macros）

<a id="r_ga4e1ea17e8a8ffd42f62d64286ddc576e"></a>

```c
#define CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX 0
```

相关声明：[CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](#ga4e1ea17e8a8ffd42f62d64286ddc576e)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 5.4\_枚举（Enumerations）

<a id="r_gae0cb28c0e50d02f6e003062457053618"></a>

```c
enum bt_mesh_blob_xfer_mode { BT_MESH_BLOB_XFER_MODE_NONE , BT_MESH_BLOB_XFER_MODE_PUSH , BT_MESH_BLOB_XFER_MODE_PULL , BT_MESH_BLOB_XFER_MODE_ALL }
```

相关声明：[bt_mesh_blob_xfer_mode](#gae0cb28c0e50d02f6e003062457053618)、[BT_MESH_BLOB_XFER_MODE_NONE](#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6)、[BT_MESH_BLOB_XFER_MODE_PUSH](#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b)、[BT_MESH_BLOB_XFER_MODE_PULL](#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd)、[BT_MESH_BLOB_XFER_MODE_ALL](#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089)。

二进制大对象传输模式（BLOB transfer mode）。

<a id="r_ga26ed2c64bae03758a8a53b28052d0f81"></a>

```c
enum bt_mesh_blob_xfer_phase { BT_MESH_BLOB_XFER_PHASE_INACTIVE , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK , BT_MESH_BLOB_XFER_PHASE_COMPLETE , BT_MESH_BLOB_XFER_PHASE_SUSPENDED }
```

相关声明：[bt_mesh_blob_xfer_phase](#ga26ed2c64bae03758a8a53b28052d0f81)、[BT_MESH_BLOB_XFER_PHASE_INACTIVE](#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START](#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK](#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK](#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581)、[BT_MESH_BLOB_XFER_PHASE_COMPLETE](#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd)、[BT_MESH_BLOB_XFER_PHASE_SUSPENDED](#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)。

传输阶段（Transfer Phase）。

<a id="r_ga7b5e2895a6577103a8a680a94ee7776d"></a>

```c
enum bt_mesh_blob_status { BT_MESH_BLOB_SUCCESS , BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM , BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE , BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE , BT_MESH_BLOB_ERR_WRONG_PHASE , BT_MESH_BLOB_ERR_INVALID_PARAM , BT_MESH_BLOB_ERR_WRONG_BLOB_ID , BT_MESH_BLOB_ERR_BLOB_TOO_LARGE , BT_MESH_BLOB_ERR_UNSUPPORTED_MODE , BT_MESH_BLOB_ERR_INTERNAL , BT_MESH_BLOB_ERR_INFO_UNAVAILABLE }
```

相关声明：[bt_mesh_blob_status](#ga7b5e2895a6577103a8a680a94ee7776d)、[BT_MESH_BLOB_SUCCESS](#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)、[BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM](#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e)、[BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE](#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a)、[BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE](#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009)、[BT_MESH_BLOB_ERR_WRONG_PHASE](#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa)、[BT_MESH_BLOB_ERR_INVALID_PARAM](#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0)、[BT_MESH_BLOB_ERR_WRONG_BLOB_ID](#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b)、[BT_MESH_BLOB_ERR_BLOB_TOO_LARGE](#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f)、[BT_MESH_BLOB_ERR_UNSUPPORTED_MODE](#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768)、[BT_MESH_BLOB_ERR_INTERNAL](#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb)、[BT_MESH_BLOB_ERR_INFO_UNAVAILABLE](#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)。

二进制大对象模型状态码（BLOB Model Status Codes）。

<a id="r_ga2618fb7365f180a73a7eecd11cf2f962"></a>

```c
enum bt_mesh_blob_io_mode { BT_MESH_BLOB_READ , BT_MESH_BLOB_WRITE }
```

相关声明：[bt_mesh_blob_io_mode](#ga2618fb7365f180a73a7eecd11cf2f962)、[BT_MESH_BLOB_READ](#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a)、[BT_MESH_BLOB_WRITE](#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab)。

BLOB 流交互模式（Stream Interaction Mode）。

## 5.5\_详细说明（Detailed Documentation）

<a id="ga4e1ea17e8a8ffd42f62d64286ddc576e"></a>

### `CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX`

```c
#define CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX 0
```

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

<a id="ga2618fb7365f180a73a7eecd11cf2f962"></a>

### `bt_mesh_blob_io_mode`

```c
enum bt_mesh_blob_io_mode
```

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

BLOB 流交互模式（Stream Interaction Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BLOB_READ` | 从数据流（Stream）读取数据。 |
| `BT_MESH_BLOB_WRITE` | 向数据流（Stream）写入数据。 |

<a id="ga7b5e2895a6577103a8a680a94ee7776d"></a>

### `bt_mesh_blob_status`

```c
enum bt_mesh_blob_status
```

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

二进制大对象模型状态码（BLOB Model Status Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BLOB_SUCCESS` | 消息已成功处理（Processed Successfully）。 |
| `BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM` | 块编号字段（Block Number Field）的值不在正在传输的块范围内。 |
| `BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE` | 块大小（Block Size）小于最小块大小对数状态（Min Block Size Log）所指示的大小，或大于最大块大小对数状态（Max Block Size Log）所指示的大小。 |
| `BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE` | 分块大小（Chunk Size）超过最大分块大小状态（Max Chunk Size）指示的大小，或分块数量超过最大分块总数状态（Max Total Chunks）指定的数量。 |
| `BT_MESH_BLOB_ERR_WRONG_PHASE` | 服务器处于当前阶段（Phase）时，无法执行该操作。 |
| `BT_MESH_BLOB_ERR_INVALID_PARAM` | 无法接受消息中的某个参数值（Parameter Value）。 |
| `BT_MESH_BLOB_ERR_WRONG_BLOB_ID` | 消息包含非预期的二进制大对象 ID（BLOB ID）。 |
| `BT_MESH_BLOB_ERR_BLOB_TOO_LARGE` | 内存中没有足够空间接收二进制大对象（BLOB）。 |
| `BT_MESH_BLOB_ERR_UNSUPPORTED_MODE` | BLOB 传输服务器模型（BLOB Transfer Server Model）不支持该传输模式。 |
| `BT_MESH_BLOB_ERR_INTERNAL` | 节点发生内部错误（Internal Error）。 |
| `BT_MESH_BLOB_ERR_INFO_UNAVAILABLE` | 服务器处于当前阶段（Phase）时，无法提供请求的信息。 |

<a id="gae0cb28c0e50d02f6e003062457053618"></a>

### `bt_mesh_blob_xfer_mode`

```c
enum bt_mesh_blob_xfer_mode
```

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

二进制大对象传输模式（BLOB transfer mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BLOB_XFER_MODE_NONE` | 没有有效的传输模式（Transfer Mode）。 |
| `BT_MESH_BLOB_XFER_MODE_PUSH` | 推送模式（Push BLOB Transfer Mode）。 |
| `BT_MESH_BLOB_XFER_MODE_PULL` | 拉取模式（Pull BLOB Transfer Mode）。 |
| `BT_MESH_BLOB_XFER_MODE_ALL` | 两种模式均有效（Both Modes）。 |

<a id="ga26ed2c64bae03758a8a53b28052d0f81"></a>

### `bt_mesh_blob_xfer_phase`

```c
enum bt_mesh_blob_xfer_phase
```

```c
#include <zephyr/bluetooth/mesh/blob.h>
```

传输阶段（Transfer Phase）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_MESH_BLOB_XFER_PHASE_INACTIVE` | BLOB 传输服务器（BLOB Transfer Server）正在等待配置。 |
| `BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START` | BLOB 传输服务器（BLOB Transfer Server）已准备好接收 BLOB 传输。 |
| `BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK` | BLOB 传输服务器（BLOB Transfer Server）正在等待下一个数据块（Block）。 |
| `BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK` | BLOB 传输服务器（BLOB Transfer Server）正在等待下一个数据分块（Chunk）。 |
| `BT_MESH_BLOB_XFER_PHASE_COMPLETE` | BLOB 已成功传输（Transferred Successfully）。 |
| `BT_MESH_BLOB_XFER_PHASE_SUSPENDED` | BLOB 传输已暂停（Paused）。 |


## 5.6\_原页交叉引用（Cross References）

- [blob.h](../api_file_runtime_reference/P004_zephyr__bluetooth__mesh__blob.h_文件参考.md)
- [bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)
- [bt_mesh_blob_chunk](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a"></a>
<a id="gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb"></a>
<a id="gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1"></a>
<a id="ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6"></a>
<a id="ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b"></a>
<a id="ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd"></a>
<a id="ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd"></a>
<a id="gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf"></a>

---

[上一章](P004_用于基本速率_增强数据速率（BR_EDR）的蓝牙逻辑链路控制与适配协议（Logical Link Control and Adaptation Protocol，L2CAP）。.md) · [返回大纲](大纲.md) · [下一章](P006_健康客户端模型（Health Client Model）.md)
