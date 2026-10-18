---
id: learning.zephyr-docs.system-service-model-reference.page-12
title: ec_host_cmd_request_header_结构体
kind: reference
status: maintained
domains: [zephyr, services, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__request__header.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_ec\_host\_cmd\_request\_header\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structec__host__cmd__request__header.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

主机发往嵌入式控制器（Embedded Controller）的请求头部。

```c
#include <zephyr/mgmt/ec_host_cmd/ec_host_cmd.h>
```

<a id="details"></a>

从主机发往嵌入式控制器（Embedded Controller，EC）的请求头。表示主机命令请求在线路上传输的小端序（LE）头部，对应主机命令头的版本 3。请求始终由主机发往嵌入式控制器。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 12.1\_数据成员（Data Fields）

<a id="r_a2f723addb6f8aec8b2d1b02a555d7b59"></a>

```c
uint8_t prtcl_ver
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prtcl_ver](#a2f723addb6f8aec8b2d1b02a555d7b59)。

应为 3。

<a id="r_a91358051660c5fa5bab1cd61991ff6b5"></a>

```c
uint8_t checksum
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[checksum](#a91358051660c5fa5bab1cd61991ff6b5)。

响应及数据的校验和（checksum）；所有字节连同校验和字节一起求和。

译注：原文此说明在请求头和响应头中都写作“response and data”，此处保留该措辞。

<a id="r_a1b4bd2b53046e29554f27dd49eb3e807"></a>

```c
uint16_t cmd_id
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[cmd_id](#a1b4bd2b53046e29554f27dd49eb3e807)。

所发送命令的 ID。

<a id="r_a2eb262f5fd1c7106d75feb8a5a6333a3"></a>

```c
uint8_t cmd_ver
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd_ver](#a2eb262f5fd1c7106d75feb8a5a6333a3)。

所请求的具体 `cmd_id` 对应的版本。

<a id="r_ad5a54882becb66008a378be28a20dd2f"></a>

```c
uint8_t reserved
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[reserved](#ad5a54882becb66008a378be28a20dd2f)。

当前协议版本未使用的字节，设为 0。

<a id="r_afedc78b6d294f73313f9eae9ecc6a03d"></a>

```c
uint16_t data_len
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[data_len](#afedc78b6d294f73313f9eae9ecc6a03d)。

此头部后续数据的长度。

## 12.2\_详细说明（Detailed Documentation）

<a id="a91358051660c5fa5bab1cd61991ff6b5"></a>

### `checksum`

```c
uint8_t ec_host_cmd_request_header::checksum
```

响应及数据的校验和（checksum）；所有字节连同校验和字节一起求和。

译注：原文此说明在请求头和响应头中都写作“response and data”，此处保留该措辞。

总和应为 0。

<a id="a1b4bd2b53046e29554f27dd49eb3e807"></a>

### `cmd_id`

```c
uint16_t ec_host_cmd_request_header::cmd_id
```

所发送命令的 ID。

<a id="a2eb262f5fd1c7106d75feb8a5a6333a3"></a>

### `cmd_ver`

```c
uint8_t ec_host_cmd_request_header::cmd_ver
```

所请求的具体 `cmd_id` 对应的版本。

有效版本从 0 开始。

<a id="afedc78b6d294f73313f9eae9ecc6a03d"></a>

### `data_len`

```c
uint16_t ec_host_cmd_request_header::data_len
```

此头部后续数据的长度。

<a id="a2f723addb6f8aec8b2d1b02a555d7b59"></a>

### `prtcl_ver`

```c
uint8_t ec_host_cmd_request_header::prtcl_ver
```

应为 3。

如果 EC 收到无法解析的版本号对应的头部，将返回 `EC_HOST_CMD_INVALID_HEADER`。

<a id="ad5a54882becb66008a378be28a20dd2f"></a>

### `reserved`

```c
uint8_t ec_host_cmd_request_header::reserved
```

当前协议版本未使用的字节，设为 0。

本数据类型文档由以下文件生成：

- `zephyr/mgmt/ec_host_cmd/ec_host_cmd.h`

## 12.3\_原页交叉引用（Cross References）

- [zephyr/mgmt/ec_host_cmd/ec_host_cmd.h](https://docs.zephyrproject.org/latest/doxygen/html/ec__host__cmd_8h_source.html)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P011_ec_host_cmd_handler_args_结构体.md) · [返回大纲](大纲.md) · [下一章](P013_ec_host_cmd_response_header_结构体.md)
