---
id: learning.zephyr-docs.external_modules.page-28
title: Xedge
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/xedge.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="xedge"></a>
<a id="external-module-xedge"></a>

# 第28章\_Xedge

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/xedge.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 28.1\_简介（Introduction）

<a id="id3"></a>

[Xedge](https://realtimelogic.com/products/xedge/) 是面向资源受限设备和实时操作系统（Real-Time Operating System，RTOS）的安全嵌入式Web与物联网（Internet of Things，IoT）边缘框架。它基于Barracuda App Server，提供Lua高级应用环境，用于开发安全联网设备。

Xedge采用GPLv2许可证，同时提供商业许可选项。

<a id="usage-with-zephyr"></a>

## 28.2\_在Zephyr中使用（Usage with Zephyr）

框架以Zephyr[模块](../modules/P001_模块与外部项目.md#modules)形式提供，支持直接在嵌入式硬件实现Web管理界面、表述性状态转移（Representational State Transfer，REST）API及安全IoT服务。

新建子清单，例如 `zephyr/submanifests/xedge.yaml`，加入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: xedge
      url: https://github.com/RealTimeLogic/Xedge4Zephyr.git
      revision: main
      path: modules/Xedge4Zephyr
```

<a id="id5"></a>

详细构建步骤、支持特性和示例见 [Xedge for Zephyr仓库](https://github.com/RealTimeLogic/Xedge4Zephyr)。

<a id="references"></a>

## 28.3\_参考资料（References）


<a id="id2"></a>

1. [Xedge项目说明](https://realtimelogic.com/products/xedge/)。

<a id="id4"></a>

2. [Zephyr仓库](https://github.com/RealTimeLogic/Xedge4Zephyr)。


对应官方文档源码：[doc/develop/manifest/external/xedge.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/xedge.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/xedge.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：WebAssembly微运行时WAMR](P027_WebAssembly微运行时WAMR.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：zenoh_pico](P029_zenoh_pico.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P027_WebAssembly微运行时WAMR.md) · [返回大纲](大纲.md) · [下一章](P029_zenoh_pico.md)

</details>

<!-- reading-navigation:end -->
