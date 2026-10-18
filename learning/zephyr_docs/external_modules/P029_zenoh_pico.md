---
id: learning.zephyr-docs.external_modules.page-29
title: zenoh_pico
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/zenoh-pico.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="zenoh-pico"></a>
<a id="external-module-zenoh-pico"></a>

# 第29章\_zenoh\_pico

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/zenoh-pico.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 29.1\_简介（Introduction）

<a id="id3"></a>

<a id="id5"></a>

[zenoh-pico](https://github.com/eclipse-zenoh/zenoh-pico) 是 [Eclipse Zenoh](https://zenoh.io) 面向资源受限设备的原生C API实现，为嵌入式系统和微控制器提供零开销发布／订阅（Zero Overhead Publish/Subscribe）、存储／查询（Store/Query）和计算（Compute）能力。

它统一流动数据、静态数据与计算，原文介绍其时间和空间效率优于主流协议栈；它与主要的Rust Zenoh实现完全兼容，以轻量方式实现大部分功能。

zenoh-pico采用Eclipse Public License 2.0和Apache License 2.0。

<a id="usage-with-zephyr"></a>

## 29.2\_在Zephyr中使用（Usage with Zephyr）

仓库是Zephyr[模块](../modules/P001_模块与外部项目.md#modules)，为应用提供分布式通信，支持用户数据报协议（User Datagram Protocol，UDP）的单播／多播及传输控制协议（Transmission Control Protocol，TCP）。网络层可使用IPv4、IPv6和低功耗无线个域网上的IPv6（IPv6 over Low-Power Wireless Personal Area Networks，6LoWPAN），数据链路层可使用WiFi、以太网、Thread和串行链路。

在原文 `west.yaml` 添加项目，或新建 `zephyr/submanifests/zenoh-pico.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: zenoh-pico
      url: https://github.com/eclipse-zenoh/zenoh-pico.git
      revision: main
      path: modules/lib/zenoh-pico # adjust the path as needed
```

<a id="id7"></a>

<a id="id9"></a>

详细步骤与API见 [zenoh-pico文档](https://zenoh-pico.readthedocs.io/en/latest/)及 [Zephyr示例](https://github.com/eclipse-zenoh/zenoh-pico/tree/main/examples/zephyr)。

<a id="references"></a>

## 29.3\_参考资料（References）


<a id="id2"></a>

1. [zenoh-pico仓库](https://github.com/eclipse-zenoh/zenoh-pico)。

<a id="id4"></a>

2. [Eclipse Zenoh](https://zenoh.io)。

<a id="id6"></a>

3. [文档](https://zenoh-pico.readthedocs.io/en/latest/)。

<a id="id8"></a>

4. [Zephyr示例](https://github.com/eclipse-zenoh/zenoh-pico/tree/main/examples/zephyr)。


对应官方文档源码：[doc/develop/manifest/external/zenoh-pico.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/zenoh-pico.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/zenoh-pico.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Xedge](P028_Xedge.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Zephelin性能分析](P030_Zephelin性能分析.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P028_Xedge.md) · [返回大纲](大纲.md) · [下一章](P030_Zephelin性能分析.md)

</details>

<!-- reading-navigation:end -->
