---
id: learning.zephyr-docs.networking.api-102
title: zperf完整API参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__zperf.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第102章\_zperf完整API参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__zperf.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 102.1\_阅读说明与来源

译注：先读[zperf指南](P096_zperf网络流量生成器.md)、[示例](P097_zperf网络流量生成器示例.md)和[回环吞吐量测试](P098_zperf确定性回环吞吐量.md)，再查本组接口。

本组：[完整API参考](P102_zperf完整API参考.md) · [头文件参考](P103_zperf头文件参考.md) · [头文件源码](P104_zperf头文件源码.md)。

引入版本（Since）：3.3；API版本（Version）：`0.8.0`。

## 102.2\_数据结构（Data Structures）

<a id="r_zperf_5Fresults"></a>

```c
struct zperf_results
```

性能测量结果（Performance Results）。

相关声明：[zperf_results](P105_zperf测量结果.md)。

## 102.3\_类型定义（Typedefs）

<a id="r_gaffeb2d7cbca61021984e784f7ba4595b"></a>

```c
typedef void(* zperf_callback) (enum zperf_status status, struct zperf_results *result, void *user_data)
```

供异步操作（Asynchronous Operations）使用的zperf回调函数。

相关声明：[zperf_results](P105_zperf测量结果.md)。

## 102.4\_函数（Functions）

<a id="r_ga6f2704914a9a577dac119a11f98c0e8e"></a>

```c
int zperf_udp_upload (const struct zperf_upload_params *param, struct zperf_results *result)
```

同步UDP上传操作（Synchronous UDP Upload）。

相关声明：[zperf_results](P105_zperf测量结果.md)。

<a id="r_ga24c061ea0dcd44b94c2ad79dfa264e44"></a>

```c
int zperf_tcp_upload (const struct zperf_upload_params *param, struct zperf_results *result)
```

同步TCP上传操作（Synchronous TCP Upload）。

相关声明：[zperf_results](P105_zperf测量结果.md)。

<a id="r_gacf57dcebd09cae8ecf61b553baf6b2cd"></a>

```c
int zperf_udp_upload_async (const struct zperf_upload_params *param, zperf_callback callback, void *user_data)
```

异步UDP上传操作（Asynchronous UDP Upload）。

<a id="r_ga07704e0bd701c0f2da2b74b9a83d6b35"></a>

```c
int zperf_tcp_upload_async (const struct zperf_upload_params *param, zperf_callback callback, void *user_data)
```

异步TCP上传操作（Asynchronous TCP Upload）。

<a id="r_gaae9e5669a76da0cde7454bbd7b491a4a"></a>

```c
int zperf_udp_download (const struct zperf_download_params *param, zperf_callback callback, void *user_data)
```

启动UDP服务器（UDP Server）。

<a id="r_ga9ac136e27fc87f85ddb66cbd2f78256d"></a>

```c
int zperf_tcp_download (const struct zperf_download_params *param, zperf_callback callback, void *user_data)
```

启动TCP服务器（TCP Server）。

<a id="r_ga394e3a10550cf9d0a435f5d217dfbbdf"></a>

```c
int zperf_udp_download_stop (void)
```

停止UDP服务器。

<a id="r_gac29193fb02ccb159b7adc3c8de64895a"></a>

```c
int zperf_tcp_download_stop (void)
```

停止TCP服务器。

## 102.5\_详细说明（Detailed Documentation）

<a id="gaffeb2d7cbca61021984e784f7ba4595b"></a>

### `zperf_callback`

```c
typedef void(* zperf_callback) (enum zperf_status status, struct zperf_results *result, void *user_data)
```

```c
#include <zephyr/net/zperf.h>
```

供异步操作（Asynchronous Operations）使用的zperf回调函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `status` | 会话状态（Session Status）。 |
| `result` | 会话结果（Session Results）；对于某些事件，该指针可能为`NULL`。 |
| `user_data` | 指向用户提供数据的指针。 |

> 译注（源码核对）：先检查`status`和`result`再读取结果。当前客户端实现会对开始／错误事件传入`NULL`，部分结果对象是回调调用期间的局部变量；需要保留结果时，在回调内复制结构体内容，不能长期保存传入指针。结果字段并不对每种协议和每个事件都有同样含义；结合[zperf协议差异](P096_zperf网络流量生成器.md)阅读。

<a id="ga9ac136e27fc87f85ddb66cbd2f78256d"></a>

### `zperf_tcp_download()`

```c
int zperf_tcp_download ( const struct zperf_download_params * param, zperf_callback callback, void * user_data )
```

```c
#include <zephyr/net/zperf.h>
```

启动TCP服务器（TCP Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 下载参数（Download Parameters）。 |
| `callback` | 会话结果回调（Session Results Callback）。 |
| `user_data` | 指向用户数据的指针，这些数据随回调一起传入。 |

**注意（Note）**：同一时间只能运行一个TCP服务器实例（Server Instance）。

**返回（Returns）**：服务器启动成功返回`0`，否则返回负错误码（Negative Error Code）。

<a id="gac29193fb02ccb159b7adc3c8de64895a"></a>

### `zperf_tcp_download_stop()`

```c
int zperf_tcp_download_stop ( void )
```

```c
#include <zephyr/net/zperf.h>
```

停止TCP服务器。

**返回（Returns）**：服务器成功停止返回`0`，否则返回负错误码。

<a id="ga24c061ea0dcd44b94c2ad79dfa264e44"></a>

### `zperf_tcp_upload()`

```c
int zperf_tcp_upload ( const struct zperf_upload_params * param, struct zperf_results * result )
```

```c
#include <zephyr/net/zperf.h>
```

同步TCP上传操作（Synchronous TCP Upload）。

此函数会阻塞，直到上传完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 上传参数（Upload Parameters）。 |
| `result` | 会话结果（Session Results）。 |

**返回（Returns）**：会话成功完成返回`0`，否则返回负错误码。

<a id="ga07704e0bd701c0f2da2b74b9a83d6b35"></a>

### `zperf_tcp_upload_async()`

```c
int zperf_tcp_upload_async ( const struct zperf_upload_params * param, zperf_callback callback, void * user_data )
```

```c
#include <zephyr/net/zperf.h>
```

异步TCP上传操作（Asynchronous TCP Upload）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 上传参数（Upload Parameters）。 |
| `callback` | 会话结果回调（Session Results Callback）。 |
| `user_data` | 指向用户数据的指针，这些数据随回调一起传入。 |

**注意（Note）**：同一时间只能执行一次异步上传（Asynchronous Upload）。

**返回（Returns）**：会话成功安排执行返回`0`，否则返回负错误码。

> 译注（源码核对）：原文“同一时间只能执行一次异步上传”应结合所用配置理解。[当前iPerf 2客户端实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/zperf_iperf2_client.c)在未启用`CONFIG_ZPERF_SESSION_PER_THREAD`时使用本协议的单个异步上下文；启用后则分配独立会话和工作队列，受可用会话与队列数量限制。该选项依赖iPerf 2，不适用于iPerf 3。返回0表示已安排执行，不表示传输已成功结束；结果通过后续回调报告。参数结构被复制，但`data_loader_ctx`和`user_data`指向的对象不会因此被深复制，应在异步操作需要它们期间保持有效。

<a id="gaae9e5669a76da0cde7454bbd7b491a4a"></a>

### `zperf_udp_download()`

```c
int zperf_udp_download ( const struct zperf_download_params * param, zperf_callback callback, void * user_data )
```

```c
#include <zephyr/net/zperf.h>
```

启动UDP服务器（UDP Server）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 下载参数（Download Parameters）。 |
| `callback` | 会话结果回调（Session Results Callback）。 |
| `user_data` | 指向用户数据的指针，这些数据随回调一起传入。 |

**注意（Note）**：同一时间只能运行一个UDP服务器实例。

**返回（Returns）**：服务器启动成功返回`0`，否则返回负错误码（Negative Error Code）。

<a id="ga394e3a10550cf9d0a435f5d217dfbbdf"></a>

### `zperf_udp_download_stop()`

```c
int zperf_udp_download_stop ( void )
```

```c
#include <zephyr/net/zperf.h>
```

停止UDP服务器。

**返回（Returns）**：服务器成功停止返回`0`，否则返回负错误码。

<a id="ga6f2704914a9a577dac119a11f98c0e8e"></a>

### `zperf_udp_upload()`

```c
int zperf_udp_upload ( const struct zperf_upload_params * param, struct zperf_results * result )
```

```c
#include <zephyr/net/zperf.h>
```

同步UDP上传操作（Synchronous UDP Upload）。

此函数会阻塞，直到上传完成。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 上传参数（Upload Parameters）。 |
| `result` | 会话结果（Session Results）。 |

**返回（Returns）**：会话成功完成返回`0`，否则返回负错误码。

<a id="gacf57dcebd09cae8ecf61b553baf6b2cd"></a>

### `zperf_udp_upload_async()`

```c
int zperf_udp_upload_async ( const struct zperf_upload_params * param, zperf_callback callback, void * user_data )
```

```c
#include <zephyr/net/zperf.h>
```

异步UDP上传操作（Asynchronous UDP Upload）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `param` | 上传参数（Upload Parameters）。 |
| `callback` | 会话结果回调（Session Results Callback）。 |
| `user_data` | 指向用户数据的指针，这些数据随回调一起传入。 |

**注意（Note）**：同一时间只能执行一次异步上传（Asynchronous Upload）。

**返回（Returns）**：会话成功安排执行返回`0`，否则返回负错误码。

> 译注（源码核对）：原文“同一时间只能执行一次异步上传”应结合所用配置理解。[当前iPerf 2客户端实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/zperf_iperf2_client.c)在未启用`CONFIG_ZPERF_SESSION_PER_THREAD`时使用本协议的单个异步上下文；启用后则分配独立会话和工作队列，受可用会话与队列数量限制。该选项依赖iPerf 2，不适用于iPerf 3。返回0表示已安排执行，不表示传输已成功结束；结果通过后续回调报告。参数结构被复制，但`data_loader_ctx`和`user_data`指向的对象不会因此被深复制，应在异步操作需要它们期间保持有效。

## 102.6\_相关源码与接口边界

此页声明来自`<zephyr/net/zperf.h>`。本仓库的[对应头文件](../../../include/zephyr/net/zperf.h)可用于源码跟踪；仓库版本可能与官网`latest`不同。

译注：官方本页API索引没有为上传／下载参数生成独立条目；其声明保留在[头文件源码译页](P104_zperf头文件源码.md)，该页还标明原始头文件中的补充注释。当前[官方API入口实现](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/zperf/zperf_api.c)按构建配置选择iPerf 2或iPerf 3后端；同步上传要求`param`和`result`非空，异步上传及服务器启动要求`param`和`callback`非空，否则返回`-EINVAL`。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>
<a id="header-typedef-members"></a>
<a id="typedef-members"></a>
<a id="header-func-members"></a>
<a id="func-members"></a>
<a id="details"></a>
<a id="header-details"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

[上一章](P101_Latmon头文件源码.md) · [返回大纲](大纲.md) · [下一章](P103_zperf头文件参考.md)
