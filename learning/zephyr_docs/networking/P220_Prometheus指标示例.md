---
id: learning.zephyr-docs.networking.page-220
title: Prometheus指标示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/prometheus/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="prometheus"></a>

# 第220章\_Prometheus指标示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/prometheus/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 220.1 概述（Overview）

此示例演示Prometheus库的用法。该库提供拉取模式（Pull method）的Prometheus客户端实现。集成后，应用实例通过HTTP端点暴露内部指标（Metric），供Prometheus抓取（Scrape）并收集。

<a id="requirement"></a>

## 220.2 要求（Requirement）

参阅[QEMU网络配置（QEMU Networking）](https://docs.zephyrproject.org/latest/connectivity/networking/qemu_setup.html#networking-with-qemu)。

> 译注——文档入口：上方保留原页所用旧路径；本资料中的当前入口见[与QEMU联网](P009_QEMU联网概览.md)。

<a id="building-and-running-the-server"></a>

## 220.3 构建并运行服务器（Building and running the server）

构建命令如下；随后按选定平台的方式运行应用：

```sh
west build -b <board to use> samples/net/prometheus -- -DCONF_FILE=<config file to use>
```

服务器启动后，可以使用HTTP/1.1发起请求。例如在浏览器输入`http://192.0.2.1/metrics`。

另请参阅[Prometheus客户端库文档](https://prometheus.io/docs/instrumenting/clientlibs/)。

<a id="metric-server-customization"></a>

## 220.4 自定义指标服务器（Metric Server Customization）

服务器示例有多项可根据需求调整的参数：

- `CONFIG_NET_SAMPLE_HTTP_SERVER_SERVICE_PORT`：服务端口。
- `CONFIG_HTTP_SERVER_MAX_CLIENTS`：服务器可同时处理的HTTP/2客户端最大数量。
- `CONFIG_HTTP_SERVER_MAX_STREAMS`：每个客户端可建立的HTTP/2流（Stream）最大数量。
- `CONFIG_HTTP_SERVER_CLIENT_BUFFER_SIZE`：为每个客户端分配的缓冲区大小，它限制单个HTTP头部（Header）的最大长度。
- `CONFIG_HTTP_SERVER_MAX_URL_LENGTH`：服务器可以处理的HTTP URL最大长度。

运行`west build -t menuconfig`可打开交互式配置界面。原文菜单路径为`-> Subsystems and OS Services -> Networking -> Network Protocols`，即从顶层菜单依次进入子系统与操作系统服务（Subsystems and OS Services）→网络（Networking）→网络协议（Network Protocols），调整相关选项。

> 译注——菜单范围：`CONFIG_NET_SAMPLE_HTTP_SERVER_SERVICE_PORT`是本示例自身Kconfig定义的选项，其他选项属于HTTP服务器子系统，不能假定全部位于同一菜单。当前HTTP服务默认端口为80，`src/main.c`注册`/metrics`资源；更改地址或端口后，浏览器URL与下方Prometheus目标配置也要保持一致。

<a id="prometheus-configuration"></a>

## 220.5 Prometheus配置（Prometheus Configuration）

```yaml
scrape_configs:
  - job_name: 'your_server_metrics'
    static_configs:
      - targets: ['your_server_ip:your_server_port']
    # Optional: Configure scrape interval
    # scrape_interval: 15s
```

将`your_server_metrics`替换为描述性的任务名称，将`'your_server_ip'`所表示的占位部分替换为服务器IP地址或主机名，将`'your_server_port'`所表示的占位部分替换为暴露Prometheus指标的端口。保留完整目标字符串外的一对引号，例如`'192.0.2.1:80'`。按照服务器实际设置与需求调整配置。

更新配置后保存文件，并重启Prometheus服务器。重启后，Prometheus根据抓取配置开始收集指标。可以查看Prometheus的目标页面（Targets page），或查询来自该服务器的指标，检查是否成功抓取。

详情见[Prometheus配置文档](https://prometheus.io/docs/prometheus/latest/configuration/configuration)。

<a id="see-also"></a>

## 220.6 另请参阅（See also）

[HTTP服务API（HTTP service API）](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html)、[HTTP服务器API（HTTP server API）](https://docs.zephyrproject.org/latest/doxygen/html/group__http__server.html)、[TLS凭据管理（TLS credentials management）](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)、[Prometheus API](https://docs.zephyrproject.org/latest/doxygen/html/group__prometheus.html)。


> 译注——实现依据：[samples/net/prometheus/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/prometheus/Kconfig)、[samples/net/prometheus/src/main.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/prometheus/src/main.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/prometheus/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/prometheus/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/prometheus/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/prometheus/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P219_MIDI2网络传输示例.md) · [返回大纲](大纲.md) · [下一章](P221_SSH服务端与客户端示例.md)
