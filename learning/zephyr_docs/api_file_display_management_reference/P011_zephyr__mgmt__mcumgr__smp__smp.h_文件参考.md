---
id: learning.zephyr-docs.api-file-display-management-reference.page-11
title: zephyr__mgmt__mcumgr__smp__smp.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_mgmt\_\_mcumgr\_\_smp\_\_smp.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mgmt_2mcumgr_2smp_2smp_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

简单管理协议（Simple Management Protocol，SMP）。

<a id="details"></a>

```c
#include <zephyr/net_buf.h>
#include <zephyr/mgmt/mcumgr/transport/smp.h>
#include <zcbor_common.h>
```

查看此文件的源码。

简单管理协议（Simple Management Protocol，SMP）。SMP 是位于管理层（mgmt Layer）之上的基础协议。SMP 请求和响应的格式为：偏移 0 是管理头部（Mgmt Header）；偏移 8 是以简洁二进制对象表示（CBOR）映射组织的命令专用键值对。SMP 请求包可包含多个拼接请求。每个请求必须从 4 的倍数偏移开始，因此必要时应在请求之间插入填充（Padding）。请求按从包首到包尾的顺序处理。每个响应单独放在自己的数据包中发送。若某个请求产生错误响应，则中止处理该数据包。

```text
  [Offset 0]: Mgmt header
  [Offset 8]: CBOR map of command-specific key-value pairs.
```

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_cbor_5Fnb_5Freader"></a>

```c
struct cbor_nb_reader
```

相关声明：[cbor_nb_reader](../system_service_model_reference/P001_cbor_nb_reader_结构体.md)。

<a id="r_cbor_5Fnb_5Fwriter"></a>

```c
struct cbor_nb_writer
```

相关声明：[cbor_nb_writer](../system_service_model_reference/P002_cbor_nb_writer_结构体.md)。

<a id="r_smp_5Fstreamer"></a>

```c
struct smp_streamer
```

相关声明：[smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)。

解码、编码并传输简单管理协议（SMP）数据包。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.2\_枚举（Enumerations）

<a id="r_aa05d01653e39ef61a93f33319c9a00ed"></a>

```c
enum smp_mcumgr_version_t { SMP_MCUMGR_VERSION_1 = 0 , SMP_MCUMGR_VERSION_2 }
```

相关声明：[smp_mcumgr_version_t](#aa05d01653e39ef61a93f33319c9a00ed)、[SMP_MCUMGR_VERSION_1](#aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33)、[SMP_MCUMGR_VERSION_2](#aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a)。

SMP MCUmgr 协议版本（Protocol Version），属于 SMP 头部的一部分。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_ac31c28afe322fb0e9ca49e8a1fb7002b"></a>

```c
struct net_buf * smp_packet_alloc (void)
```

相关声明：[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)、[smp_packet_alloc](#ac31c28afe322fb0e9ca49e8a1fb7002b)。

分配用于保存 MCUmgr 请求或响应的 `net_buf` 网络缓冲区。

<a id="r_ad6b5e8c30760366c0e9d6c843605de93"></a>

```c
void smp_packet_free (struct net_buf *nb)
```

相关声明：[smp_packet_free](#ad6b5e8c30760366c0e9d6c843605de93)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

释放 MCUmgr 的 `net_buf` 网络缓冲区。

<a id="r_a6705014150cda88212d6eb6143d044d4"></a>

```c
int smp_process_request_packet (struct smp_streamer *streamer, void *req)
```

相关声明：[smp_process_request_packet](#a6705014150cda88212d6eb6143d044d4)、[smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)。

处理单个 SMP 请求包（Request Packet），并发送全部对应响应。

<a id="r_a191eb8c8a5a531b158374a1071925ca7"></a>

```c
bool smp_add_cmd_err (zcbor_state_t *zse, uint16_t group, uint16_t ret)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[smp_add_cmd_err](#a191eb8c8a5a531b158374a1071925ca7)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[group](../posix_system_model_reference/P003_group_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

追加 `err` 错误响应（Error Response）。

## 11.4\_详细说明（Detailed Documentation）

<a id="aa05d01653e39ef61a93f33319c9a00ed"></a>

### `smp_mcumgr_version_t`

```c
enum smp_mcumgr_version_t
```

SMP MCUmgr 协议版本（Protocol Version），属于 SMP 头部的一部分。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `SMP_MCUMGR_VERSION_1` | 版本 1：原始协议（Original Protocol）。 |
| `SMP_MCUMGR_VERSION_2` | 版本 2：增加更详细的错误报告能力（Error Reporting Capabilities）。 |

<a id="a191eb8c8a5a531b158374a1071925ca7"></a>

### `smp_add_cmd_err()`

```c
bool smp_add_cmd_err ( zcbor_state_t * zse, uint16_t group, uint16_t ret )
```

追加 `err` 错误响应（Error Response）。

向待发送响应追加 `err` 错误响应，其中包含指定命令组（Command Group）的结果码。注意：错误码由发出它们的命令组定义，各组可能不同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `zse` | 要使用的 zcbor 编码器（Encoder）。 |
| `group` | 产生错误的命令组（Group）。 |
| `ret` | 要添加的命令结果码（Command Result Code）。 |

**返回（Returns）**：返回值：成功返回 `true`；失败，即发生内存错误（Memory Error）时，返回 `false`。

<a id="ac31c28afe322fb0e9ca49e8a1fb7002b"></a>

### `smp_packet_alloc()`

```c
struct net_buf * smp_packet_alloc ( void )
```

分配用于保存 MCUmgr 请求或响应的 `net_buf` 网络缓冲区。

**返回（Returns）**：返回值：成功返回新分配的 `net_buf` 网络缓冲区；失败返回 `NULL`。

<a id="ad6b5e8c30760366c0e9d6c843605de93"></a>

### `smp_packet_free()`

```c
void smp_packet_free ( struct net_buf * nb)
```

释放 MCUmgr 的 `net_buf` 网络缓冲区。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `nb` | 要释放的 `net_buf`。 |

<a id="a6705014150cda88212d6eb6143d044d4"></a>

### `smp_process_request_packet()`

```c
int smp_process_request_packet ( struct smp_streamer * streamer, void * req )
```

处理单个 SMP 请求包（Request Packet），并发送全部对应响应。

处理传入数据包中的所有 SMP 请求。按从包首到包尾的顺序处理请求。每个响应单独放在自己的数据包中发送。若某个请求产生错误响应，则中止处理该数据包。无论结果如何，此函数都会消耗所提供的请求缓冲区（Request Buffer）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `streamer` | 提供所需 SMP 回调的流处理器（Streamer）。 |
| `req` | 要处理的请求包（Request Packet）。 |

**返回（Returns）**：返回值：成功返回 0，失败返回 `mcumgr_err_t` 错误码。


## 11.5\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [zephyr/mgmt/mcumgr/transport/smp.h](../api_source_system_reference/P018_smp.h_源码浏览.md)
- [查看此文件的源码。](../api_source_supplement_reference/P113_smp.h_源码浏览.md)
- [cbor_nb_reader](../system_service_model_reference/P001_cbor_nb_reader_结构体.md)
- [cbor_nb_writer](../system_service_model_reference/P002_cbor_nb_writer_结构体.md)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aa05d01653e39ef61a93f33319c9a00edaee0064c0e66c35a1822c101a83693f33"></a>
<a id="aa05d01653e39ef61a93f33319c9a00eda7d9455ed10c150d699de2598af9dcb7a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__sys__kobject.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__mgmt__mcumgr__transport__smp.h_文件参考.md)
