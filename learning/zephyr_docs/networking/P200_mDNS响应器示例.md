---
id: learning.zephyr-docs.networking.page-200
title: mDNS响应器示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/mdns_responder/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mdns-responder"></a>

# 第200章\_mDNS响应器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/mdns_responder/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 200.1 概述（Overview）

此应用等待针对预定义主机名的组播DNS（Multicast DNS，mDNS）查询并作出响应。默认主机名为`zephyr`，在`prj.conf`中设置。

<a id="requirements"></a>

## 200.2 要求（Requirements）

- 完成[与主机系统联网（Networking with the host system）](P007_与主机系统联网.md#networking-with-host)所述准备。
- 主机安装Avahi或具有类似能力、能够查询mDNS信息的应用。

<a id="building-and-running"></a>

## 200.3 构建与运行（Building and Running）

按以下方式构建`mdns-responder`示例；随后按目标平台的方式启动它：

```sh
west build -b <board to use> samples/net/mdns_responder -- -DCONF_FILE=<config file to use>
```

应用启动后等待网络查询。在主机终端输入：

```console
$ avahi-resolve -4 -n zephyr.local
```

查询成功时打印：

```text
zephyr.local        192.0.2.1
```

IPv6查询使用：

```console
$ avahi-resolve -6 -n zephyr.local
```

查询成功时打印：

```text
zephyr.local        2001:db8::1
```

最后，通过DNS服务发现（DNS Service Discovery，DNS-SD）解析服务：

```console
$ avahi-browse -t -r _zephyr._tcp
```

查询成功时打印：

```text
+   zeth IPv6 zephyr                                        _zephyr._tcp         local
=   zeth IPv6 zephyr                                        _zephyr._tcp         local
   hostname = [zephyr.local]
   address = [192.0.2.1]
   port = [4242]
   txt = []
```

> 译注——服务端口：上面的`4242`保留自官方输出示例。当前`src/service.c`中`DEFAULT_PORT`为0，表示请求临时端口（Ephemeral port），并通过DNS-SD注册服务；因此应读取实际发现结果中的端口，而不是把`4242`视为所有版本的固定配置。主机名解析成功与服务查询成功是不同检查点，前者不能单独证明后者成功。

<a id="wi-fi"></a>

### 200.3.1 Wi-Fi（Wi-Fi）

可通过[Wi-Fi配置片段（Wi-Fi snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)为此示例启用IPv4 Wi-Fi支持。

<a id="see-also"></a>

## 200.4 另请参阅（See also）

[网络核心库（Network Core Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html)、[DNS服务发现（DNS Service Discovery）](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__sd.html)、[BSD套接字兼容API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。


> 译注——实现依据：[samples/net/mdns_responder/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/mdns_responder/prj.conf)、[samples/net/mdns_responder/src/service.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/mdns_responder/src/service.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/mdns_responder/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/mdns_responder/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/mdns_responder/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/mdns_responder/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P199_IPv4自动配置客户端示例.md) · [返回大纲](大纲.md) · [下一章](P201_网络数据包捕获示例.md)
