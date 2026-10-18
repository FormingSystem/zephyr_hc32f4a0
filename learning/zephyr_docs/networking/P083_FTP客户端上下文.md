---
id: learning.zephyr-docs.networking.api-83
title: FTP客户端上下文
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structftp__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第83章\_FTP客户端上下文

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structftp__client.html)。本次读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 83.1\_阅读说明与来源

译注：先读[FTP客户端库](P075_FTP客户端库.md)和[客户端示例](P076_FTP客户端示例.md)，再按接口查询本组参考。

本组：[完整API参考](P080_FTP完整API参考.md) · [头文件参考](P081_FTP头文件参考.md) · [头文件源码](P082_FTP头文件源码.md)。

FTP客户端上下文（Client Context）。

```c
#include <zephyr/net/ftp_client.h>
```

FTP客户端上下文（Client Context）。

## 83.2\_数据成员（Data Fields）

```c
union {
```

<a id="r_a13af41de8db6f9476eb37ac36ac8af00"></a>

```c
struct net_sockaddr_storage remote_addr
```

服务器地址（Server Address）。

<a id="r_a68dd716d4a49592da415c7fcb9931ff5"></a>

```c
};
```

远端服务器地址存储（Address Storage）。

<a id="r_ad8c19ebc3725b3af345eaa86e0fe3e6a"></a>

```c
bool connected
```

服务器已连接标志（Connected Flag）。

<a id="r_aec64cc9ae3dc8541cbf11d31f289af73"></a>

```c
int ctrl_sock
```

控制套接字（Control Socket）。

<a id="r_a060735326fac26d737f0a4e2a32afcff"></a>

```c
int data_sock
```

数据套接字（Data Socket）。

<a id="r_a13b8191a83a656f96dd2d9d9352f08eb"></a>

```c
int sec_tag
```

安全标签（Secure Tag）。

<a id="r_acd13724b1c049a5fc48008bc3a65048f"></a>

```c
uint8_t ctrl_buf [FTP_BUFFER_SIZE]
```

控制缓冲区（Control Buffer）。

<a id="r_af1223e38213f9cb64052a83572115ff4"></a>

```c
size_t ctrl_len
```

控制缓冲区中的数据长度。

<a id="r_a6667e43b6ad4288dd5ebdc37157ebcd2"></a>

```c
uint8_t data_buf [FTP_BUFFER_SIZE]
```

数据缓冲区（Data Buffer）。

<a id="r_a19824800556b11ce885f2ea1864ee906"></a>

```c
ftp_client_callback_t ctrl_callback
```

控制回调（Control Callback）。

相关声明：[ftp_client_callback_t](P080_FTP完整API参考.md#ga5d2fbddcb382dc2c4b082b32cb28ef82)。

<a id="r_a46ff461b642c07682cee9e6a1b4561a8"></a>

```c
ftp_client_callback_t data_callback
```

数据回调（Data Callback）。

相关声明：[ftp_client_callback_t](P080_FTP完整API参考.md#ga5d2fbddcb382dc2c4b082b32cb28ef82)。

## 83.3\_详细说明（Detailed Documentation）

<a id="a68dd716d4a49592da415c7fcb9931ff5"></a>

### `[union]`

```c
union { ... } ftp_client
```

远端服务器地址存储（Address Storage）。

<a id="ad8c19ebc3725b3af345eaa86e0fe3e6a"></a>

### `connected`

```c
bool ftp_client::connected
```

服务器已连接标志（Connected Flag）。

<a id="acd13724b1c049a5fc48008bc3a65048f"></a>

### `ctrl_buf`

```c
uint8_t ftp_client::ctrl_buf[FTP_BUFFER_SIZE]
```

控制缓冲区（Control Buffer）。

<a id="a19824800556b11ce885f2ea1864ee906"></a>

### `ctrl_callback`

```c
ftp_client_callback_t ftp_client::ctrl_callback
```

控制回调（Control Callback）。

<a id="af1223e38213f9cb64052a83572115ff4"></a>

### `ctrl_len`

```c
size_t ftp_client::ctrl_len
```

控制缓冲区中的数据长度。

<a id="aec64cc9ae3dc8541cbf11d31f289af73"></a>

### `ctrl_sock`

```c
int ftp_client::ctrl_sock
```

控制套接字（Control Socket）。

<a id="a6667e43b6ad4288dd5ebdc37157ebcd2"></a>

### `data_buf`

```c
uint8_t ftp_client::data_buf[FTP_BUFFER_SIZE]
```

数据缓冲区（Data Buffer）。

<a id="a46ff461b642c07682cee9e6a1b4561a8"></a>

### `data_callback`

```c
ftp_client_callback_t ftp_client::data_callback
```

数据回调（Data Callback）。

<a id="a060735326fac26d737f0a4e2a32afcff"></a>

### `data_sock`

```c
int ftp_client::data_sock
```

数据套接字（Data Socket）。

<a id="ac3d681a1065fd1584fc7fac1f9dc93c1"></a>

### `remote_addr`

```c
struct net_sockaddr_storage ftp_client::remote_addr
```

服务器地址（Server Address）。

<a id="a13b8191a83a656f96dd2d9d9352f08eb"></a>

### `sec_tag`

```c
int ftp_client::sec_tag
```

安全标签（Secure Tag）。

## 83.4\_匿名联合体与源码对照

译注：结构体摘要中的`union { ... }`是匿名联合体（Anonymous Union），其成员共享地址存储。以下摘自同批官方源码浏览页，保留嵌套关系和没有独立详细条目的内部成员：

```c
struct ftp_client {
        union {
                struct net_sockaddr_storage remote_addr;
                struct net_sockaddr remote;
        };
        bool connected;
        int ctrl_sock;
        int data_sock;
        int sec_tag;
        uint8_t ctrl_buf[FTP_BUFFER_SIZE];
        size_t ctrl_len;
        uint8_t data_buf[FTP_BUFFER_SIZE];
        ftp_client_callback_t ctrl_callback;
        ftp_client_callback_t data_callback;
        struct k_mutex lock;
        struct k_work_delayable keepalive_work;
};
```

## 83.5\_相关头文件与源码

此页声明来自`<zephyr/net/ftp_client.h>`。本仓库的[对应头文件](../../../include/zephyr/net/ftp_client.h)可用于源码跟踪；本仓库版本可能与官网`latest`不同。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

[上一章](P082_FTP头文件源码.md) · [返回大纲](大纲.md) · [下一章](P084_TFTP完整API参考.md)
