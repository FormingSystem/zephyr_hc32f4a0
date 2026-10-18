---
id: learning.zephyr-docs.system-service-model-reference.page-13
title: ec_host_cmd_response_header_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__response__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ec\_host\_cmd\_response\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__response__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

嵌入式控制器（Embedded Controller）返回主机的响应头部。

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

<a id="details"></a>

从嵌入式控制器（EC）发往主机的响应头。表示主机命令响应在线路上传输的小端序（LE）头部，对应主机命令头的版本 3。响应始终由嵌入式控制器发往主机。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 13.1\_数据成员（Data Fields）

<a id="r_a50baff1f46f56c992194c3c244897aa8"></a>

```c
uint8_t prtcl_ver
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prtcl_ver](#a50baff1f46f56c992194c3c244897aa8)。

应为 3。

<a id="r_ac77bfd822866c9f48cec249a60eaa82b"></a>

```c
uint8_t checksum
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[checksum](#ac77bfd822866c9f48cec249a60eaa82b)。

响应及数据的校验和（checksum）；所有字节连同校验和字节一起求和。

译注：原文此说明在请求头和响应头中都写作“response and data”，此处保留该措辞。

<a id="r_ab64789cfe9fc9008aa5d88182fee9885"></a>

```c
uint16_t result
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[result](#ab64789cfe9fc9008aa5d88182fee9885)。

针对具体命令的 `ec_host_cmd_status` 响应码。

<a id="r_af0abf8f0d16b2089bb4f7abaac5191af"></a>

```c
uint16_t data_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data_len](#af0abf8f0d16b2089bb4f7abaac5191af)。

此头部后续数据的长度。

<a id="r_ab45cadbdafc4ab1eb5d8b1b1db2303de"></a>

```c
uint16_t reserved
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[reserved](#ab45cadbdafc4ab1eb5d8b1b1db2303de)。

当前协议版本未使用的字节，设为 0。

## 13.2\_详细说明（Detailed Documentation）

<a id="ac77bfd822866c9f48cec249a60eaa82b"></a>

### `checksum`

```c
uint8_t ec_host_cmd_response_header::checksum
```

响应及数据的校验和（checksum）；所有字节连同校验和字节一起求和。

译注：原文此说明在请求头和响应头中都写作“response and data”，此处保留该措辞。

总和应为 0。

<a id="af0abf8f0d16b2089bb4f7abaac5191af"></a>

### `data_len`

```c
uint16_t ec_host_cmd_response_header::data_len
```

此头部后续数据的长度。

<a id="a50baff1f46f56c992194c3c244897aa8"></a>

### `prtcl_ver`

```c
uint8_t ec_host_cmd_response_header::prtcl_ver
```

应为 3。

<a id="ab45cadbdafc4ab1eb5d8b1b1db2303de"></a>

### `reserved`

```c
uint16_t ec_host_cmd_response_header::reserved
```

当前协议版本未使用的字节，设为 0。

<a id="ab64789cfe9fc9008aa5d88182fee9885"></a>

### `result`

```c
uint16_t ec_host_cmd_response_header::result
```

针对具体命令的 `ec_host_cmd_status` 响应码。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/ec_host_cmd.h`

## 13.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/ec_host_cmd.h](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [ec_host_cmd_status](https://docs.zephyrproject.org/latest/doxygen/html/group__ec__host__cmd__interface.html#ga9b0b87983dcc92ea55ebfa1aecf82a8f)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P012_ec_host_cmd_request_header_结构体.md) · [返回大纲](大纲.md) · [下一章](P014_ec_host_cmd_rx_ctx_结构体.md)
