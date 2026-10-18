---
id: learning.zephyr-docs.api-file-runtime-reference.page-4
title: zephyr__bluetooth__mesh__blob.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_bluetooth\_\_mesh\_\_blob.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/blob_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙Mesh二进制大对象（BLOB）传输模型API的头文件。

<a id="details"></a>

```c
#include <sys/types.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

蓝牙Mesh二进制大对象（BLOB）传输模型API的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

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

## 4.2\_宏定义（Macros）

<a id="r_ga4e1ea17e8a8ffd42f62d64286ddc576e"></a>

```c
#define CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX 0
```

相关声明：[CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.3\_枚举（Enumerations）

<a id="r_gae0cb28c0e50d02f6e003062457053618"></a>

```c
enum bt_mesh_blob_xfer_mode { BT_MESH_BLOB_XFER_MODE_NONE , BT_MESH_BLOB_XFER_MODE_PUSH , BT_MESH_BLOB_XFER_MODE_PULL , BT_MESH_BLOB_XFER_MODE_ALL }
```

相关声明：[bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)、[BT_MESH_BLOB_XFER_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6)、[BT_MESH_BLOB_XFER_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b)、[BT_MESH_BLOB_XFER_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd)、[BT_MESH_BLOB_XFER_MODE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089)。

二进制大对象传输模式（BLOB transfer mode）。

<a id="r_ga26ed2c64bae03758a8a53b28052d0f81"></a>

```c
enum bt_mesh_blob_xfer_phase { BT_MESH_BLOB_XFER_PHASE_INACTIVE , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK , BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK , BT_MESH_BLOB_XFER_PHASE_COMPLETE , BT_MESH_BLOB_XFER_PHASE_SUSPENDED }
```

相关声明：[bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)、[BT_MESH_BLOB_XFER_PHASE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1)、[BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581)、[BT_MESH_BLOB_XFER_PHASE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd)、[BT_MESH_BLOB_XFER_PHASE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)。

传输阶段（Transfer Phase）。

<a id="r_ga7b5e2895a6577103a8a680a94ee7776d"></a>

```c
enum bt_mesh_blob_status { BT_MESH_BLOB_SUCCESS , BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM , BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE , BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE , BT_MESH_BLOB_ERR_WRONG_PHASE , BT_MESH_BLOB_ERR_INVALID_PARAM , BT_MESH_BLOB_ERR_WRONG_BLOB_ID , BT_MESH_BLOB_ERR_BLOB_TOO_LARGE , BT_MESH_BLOB_ERR_UNSUPPORTED_MODE , BT_MESH_BLOB_ERR_INTERNAL , BT_MESH_BLOB_ERR_INFO_UNAVAILABLE }
```

相关声明：[bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)、[BT_MESH_BLOB_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)、[BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e)、[BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a)、[BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009)、[BT_MESH_BLOB_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa)、[BT_MESH_BLOB_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0)、[BT_MESH_BLOB_ERR_WRONG_BLOB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b)、[BT_MESH_BLOB_ERR_BLOB_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f)、[BT_MESH_BLOB_ERR_UNSUPPORTED_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768)、[BT_MESH_BLOB_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb)、[BT_MESH_BLOB_ERR_INFO_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)。

二进制大对象模型状态码（BLOB Model Status Codes）。

<a id="r_ga2618fb7365f180a73a7eecd11cf2f962"></a>

```c
enum bt_mesh_blob_io_mode { BT_MESH_BLOB_READ , BT_MESH_BLOB_WRITE }
```

相关声明：[bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)、[BT_MESH_BLOB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a)、[BT_MESH_BLOB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab)。

BLOB 流交互模式（Stream Interaction Mode）。


## 4.4\_原页交叉引用（Cross References）

- [sys/types.h](../api_source_runtime_reference/P038_types.h_源码浏览.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P068_blob.h_源码浏览.md)
- [bt_mesh_blob_block](../bluetooth_mesh_model_reference/P001_bt_mesh_blob_block_结构体.md)
- [bt_mesh_blob_chunk](../bluetooth_mesh_model_reference/P002_bt_mesh_blob_chunk_结构体.md)
- [bt_mesh_blob_xfer](../bluetooth_mesh_model_reference/P014_bt_mesh_blob_xfer_结构体.md)
- [bt_mesh_blob_io](../bluetooth_mesh_model_reference/P007_bt_mesh_blob_io_结构体.md)
- [CONFIG_BT_MESH_BLOB_CHUNK_COUNT_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga4e1ea17e8a8ffd42f62d64286ddc576e)
- [bt_mesh_blob_xfer_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gae0cb28c0e50d02f6e003062457053618)
- [BT_MESH_BLOB_XFER_MODE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a98cf4939114c3662fe4f659260d076d6)
- [BT_MESH_BLOB_XFER_MODE_PUSH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a4f9303c1f20e97987d2932e5d86ffe9b)
- [BT_MESH_BLOB_XFER_MODE_PULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618abc015f3e32c34808b86dd39381b810fd)
- [BT_MESH_BLOB_XFER_MODE_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ggae0cb28c0e50d02f6e003062457053618a7906e4fe51f88a5efcb45ada83b7b089)
- [bt_mesh_blob_xfer_phase](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga26ed2c64bae03758a8a53b28052d0f81)
- [BT_MESH_BLOB_XFER_PHASE_INACTIVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a60d2a7f950f2763ecb38b0cd84ae9600)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_START](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a68f54acdddf2df36f31c8c7c4d7eb9b9)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_BLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a19aebd2c4bfb7295a42577fb118771f1)
- [BT_MESH_BLOB_XFER_PHASE_WAITING_FOR_CHUNK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81af6fa22460b1671383a9c4ae4cf1b6581)
- [BT_MESH_BLOB_XFER_PHASE_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81ae6824f0459de25d00f8c591d6ad5f4fd)
- [BT_MESH_BLOB_XFER_PHASE_SUSPENDED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga26ed2c64bae03758a8a53b28052d0f81a9e9c6d6e450d7bfa1290bad777a740bf)
- [bt_mesh_blob_status](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga7b5e2895a6577103a8a680a94ee7776d)
- [BT_MESH_BLOB_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daac639c3c82cf48a394c13e3b057c9c0d)
- [BT_MESH_BLOB_ERR_INVALID_BLOCK_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da2653f1c27fab5b789a3091fad35b161e)
- [BT_MESH_BLOB_ERR_INVALID_BLOCK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dac56e3b5bc5eb558470735014dd438f8a)
- [BT_MESH_BLOB_ERR_INVALID_CHUNK_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776dafad7fd6bc121da2ed8e78fcfea22a009)
- [BT_MESH_BLOB_ERR_WRONG_PHASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da4044bc0cf8f8085975ad4659ae1b12fa)
- [BT_MESH_BLOB_ERR_INVALID_PARAM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daca14a1b6e8ce3fd82198b2cc4948aab0)
- [BT_MESH_BLOB_ERR_WRONG_BLOB_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1c37502c32d21c669a7a7da2574b068b)
- [BT_MESH_BLOB_ERR_BLOB_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da11bd387885e987335df8ddcdc8f3484f)
- [BT_MESH_BLOB_ERR_UNSUPPORTED_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da996b6fe3e24a560aac0ea54eb7a3f768)
- [BT_MESH_BLOB_ERR_INTERNAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776daa51d478f00ff98870c25edde0a27bdcb)
- [BT_MESH_BLOB_ERR_INFO_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga7b5e2895a6577103a8a680a94ee7776da1a01794b9fbef5f89355ac9134073ec1)
- [bt_mesh_blob_io_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#ga2618fb7365f180a73a7eecd11cf2f962)
- [BT_MESH_BLOB_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962ae7ded7a63b8fc889a8063b156337081a)
- [BT_MESH_BLOB_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__mesh__blob.html#gga2618fb7365f180a73a7eecd11cf2f962a1ff9191c6d593881a4a32826323d9aab)

<a id="header-details"></a>

---

[上一章](P003_zephyr__dt-bindings__gpio__atmel-sam0-gpio.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__drivers__sensor__bmp581_user.h_文件参考.md)
