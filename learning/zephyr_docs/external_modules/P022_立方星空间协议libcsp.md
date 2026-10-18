---
id: learning.zephyr-docs.external_modules.page-22
title: 立方星空间协议libcsp
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/libcsp.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="libcsp-cubesat-space-protocol"></a>
<a id="external-module-libcsp"></a>

# 第22章\_立方星空间协议libcsp

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/libcsp.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 22.1\_简介（Introduction）

libcsp是立方星空间协议（CubeSat Space Protocol，CSP）的C语言小型协议栈，用来简化立方星（CubeSat）等小网络中分布式嵌入式系统之间的通信。设计遵循TCP/IP模型，包含传输协议、路由协议和多个介质访问控制（Media Access Control，MAC）层接口。核心包括路由器（Router）、面向连接的套接字（Socket）API，以及消息池与连接池。

一些立方星使用Zephyr，并通过libcsp与星上其他组件通信。libcsp采用MIT许可证。

<a id="usage-with-zephyr"></a>

## 22.2\_在Zephyr中使用（Usage with Zephyr）

先把以下片段合并到原文所称的 `west.yaml`：

```yaml
manifest:
  projects:
    - name: libcsp
      url: https://github.com/libcsp/libcsp
      revision: develop
      path: modules/lib/libcsp
```

在应用 `prj.conf` 添加：

```kconfig
CONFIG_LIBCSP=y
```

<a id="id2"></a>

将libcsp加入项目后执行 `west update`。详细步骤和API见 [libcsp文档](https://libcsp.github.io/libcsp/)。

<a id="reference"></a>

## 22.3\_参考资料（Reference）


<a id="id1"></a>

1. [libcsp文档](https://libcsp.github.io/libcsp/)。


对应官方文档源码：[doc/develop/manifest/external/libcsp.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/libcsp.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/libcsp.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：grvl图形库](P021_grvl图形库.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：工业IO库libiio](P023_工业IO库libiio.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P021_grvl图形库.md) · [返回大纲](大纲.md) · [下一章](P023_工业IO库libiio.md)

</details>

<!-- reading-navigation:end -->
