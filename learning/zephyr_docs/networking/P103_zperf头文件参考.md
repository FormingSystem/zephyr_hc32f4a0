---
id: learning.zephyr-docs.networking.api-103
title: zperf头文件参考
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/zperf_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第103章\_zperf头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/zperf_8h.html)。读取日期：2026-10-14；基线为保存的`latest`页面，HTML摘要见[来源记录](../SOURCES.md)。

## 103.1\_阅读说明与来源

译注：先读[zperf指南](P096_zperf网络流量生成器.md)、[示例](P097_zperf网络流量生成器示例.md)和[回环吞吐量测试](P098_zperf确定性回环吞吐量.md)，再查本组接口。

本组：[完整API参考](P102_zperf完整API参考.md) · [头文件参考](P103_zperf头文件参考.md) · [头文件源码](P104_zperf头文件源码.md)。

zperf应用程序编程接口（Zperf API）。

```c
#include <zephyr/net/net_ip.h>
```

```c
#include <zephyr/net/socket.h>
```

zperf应用程序编程接口（Zperf API）。

## 103.2\_数据结构（Data Structures）

<a id="r_zperf_5Fresults"></a>

```c
struct zperf_results
```

性能测量结果（Performance Results）。

相关声明：[zperf_results](P105_zperf测量结果.md)。

## 103.3\_类型定义（Typedefs）

<a id="r_gaffeb2d7cbca61021984e784f7ba4595b"></a>

```c
typedef void(* zperf_callback) (enum zperf_status status, struct zperf_results *result, void *user_data)
```

供异步操作（Asynchronous Operations）使用的zperf回调函数。

相关声明：[zperf_callback](P102_zperf完整API参考.md#gaffeb2d7cbca61021984e784f7ba4595b)、[zperf_results](P105_zperf测量结果.md)。

## 103.4\_函数（Functions）

<a id="r_ga6f2704914a9a577dac119a11f98c0e8e"></a>

```c
int zperf_udp_upload (const struct zperf_upload_params *param, struct zperf_results *result)
```

同步UDP上传操作（Synchronous UDP Upload）。

相关声明：[zperf_udp_upload](P102_zperf完整API参考.md#ga6f2704914a9a577dac119a11f98c0e8e)、[zperf_results](P105_zperf测量结果.md)。

<a id="r_ga24c061ea0dcd44b94c2ad79dfa264e44"></a>

```c
int zperf_tcp_upload (const struct zperf_upload_params *param, struct zperf_results *result)
```

同步TCP上传操作（Synchronous TCP Upload）。

相关声明：[zperf_tcp_upload](P102_zperf完整API参考.md#ga24c061ea0dcd44b94c2ad79dfa264e44)、[zperf_results](P105_zperf测量结果.md)。

<a id="r_gacf57dcebd09cae8ecf61b553baf6b2cd"></a>

```c
int zperf_udp_upload_async (const struct zperf_upload_params *param, zperf_callback callback, void *user_data)
```

异步UDP上传操作（Asynchronous UDP Upload）。

相关声明：[zperf_udp_upload_async](P102_zperf完整API参考.md#gacf57dcebd09cae8ecf61b553baf6b2cd)、[zperf_callback](P102_zperf完整API参考.md#gaffeb2d7cbca61021984e784f7ba4595b)。

<a id="r_ga07704e0bd701c0f2da2b74b9a83d6b35"></a>

```c
int zperf_tcp_upload_async (const struct zperf_upload_params *param, zperf_callback callback, void *user_data)
```

异步TCP上传操作（Asynchronous TCP Upload）。

相关声明：[zperf_tcp_upload_async](P102_zperf完整API参考.md#ga07704e0bd701c0f2da2b74b9a83d6b35)、[zperf_callback](P102_zperf完整API参考.md#gaffeb2d7cbca61021984e784f7ba4595b)。

<a id="r_gaae9e5669a76da0cde7454bbd7b491a4a"></a>

```c
int zperf_udp_download (const struct zperf_download_params *param, zperf_callback callback, void *user_data)
```

启动UDP服务器（UDP Server）。

相关声明：[zperf_udp_download](P102_zperf完整API参考.md#gaae9e5669a76da0cde7454bbd7b491a4a)、[zperf_callback](P102_zperf完整API参考.md#gaffeb2d7cbca61021984e784f7ba4595b)。

<a id="r_ga9ac136e27fc87f85ddb66cbd2f78256d"></a>

```c
int zperf_tcp_download (const struct zperf_download_params *param, zperf_callback callback, void *user_data)
```

启动TCP服务器（TCP Server）。

相关声明：[zperf_tcp_download](P102_zperf完整API参考.md#ga9ac136e27fc87f85ddb66cbd2f78256d)、[zperf_callback](P102_zperf完整API参考.md#gaffeb2d7cbca61021984e784f7ba4595b)。

<a id="r_ga394e3a10550cf9d0a435f5d217dfbbdf"></a>

```c
int zperf_udp_download_stop (void)
```

停止UDP服务器。

相关声明：[zperf_udp_download_stop](P102_zperf完整API参考.md#ga394e3a10550cf9d0a435f5d217dfbbdf)。

<a id="r_gac29193fb02ccb159b7adc3c8de64895a"></a>

```c
int zperf_tcp_download_stop (void)
```

停止TCP服务器。

相关声明：[zperf_tcp_download_stop](P102_zperf完整API参考.md#gac29193fb02ccb159b7adc3c8de64895a)。

## 103.5\_相关源码与接口边界

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

[上一章](P102_zperf完整API参考.md) · [返回大纲](大纲.md) · [下一章](P104_zperf头文件源码.md)
