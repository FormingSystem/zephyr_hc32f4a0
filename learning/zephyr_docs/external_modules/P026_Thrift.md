---
id: learning.zephyr-docs.external_modules.page-26
title: Thrift
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/thrift.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="thrift"></a>
<a id="external-module-thrift"></a>

# 第26章\_Thrift

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/thrift.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 26.1\_简介（Introduction）

<a id="id2"></a>

<a id="id4"></a>

<a id="id6"></a>

<a id="id8"></a>

[Apache Thrift](https://github.com/apache/thrift) 同时提供[接口描述语言（Interface Description Language，IDL）](https://en.wikipedia.org/wiki/Interface_description_language)规范、[远程过程调用（Remote Procedure Call，RPC）](https://en.wikipedia.org/wiki/Remote_procedure_call)框架和[代码生成器（Code Generator）](https://en.wikipedia.org/wiki/Automatic_programming)。原文介绍它覆盖主要操作系统，支持超过27种编程语言、7种协议和6种底层传输。

<a id="id10"></a>

<a id="id12"></a>

它最初由 [Facebook在2006年开发](https://thrift.apache.org/static/files/thrift-20070401.pdf)，随后分享给 [Apache软件基金会](https://www.apache.org)。Thrift支持丰富类型和数据结构，封装传输与协议细节，让开发者专注应用逻辑。

<a id="usage-with-zephyr"></a>

## 26.2\_在Zephyr中使用（Usage with Zephyr）

在原文 `west.yaml` 中加入项目，或新建 `zephyr/submanifests/thrift.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: Thrift
      path: modules/lib/thrift
      revision: zephyr
      url: https://github.com/zephyrproject-rtos/thrift
```

模块的 `zephyr/` 目录包含示例应用和测试。

原文参考资料：


<a id="id1"></a>

1. [Apache Thrift仓库](https://github.com/apache/thrift)。

<a id="id3"></a>

2. [IDL说明](https://en.wikipedia.org/wiki/Interface_description_language)。

<a id="id5"></a>

3. [RPC说明](https://en.wikipedia.org/wiki/Remote_procedure_call)。

<a id="id7"></a>

4. [代码生成相关说明](https://en.wikipedia.org/wiki/Automatic_programming)。

<a id="id9"></a>

5. [Thrift技术文档](https://thrift.apache.org/static/files/thrift-20070401.pdf)。

<a id="id11"></a>

6. [Apache软件基金会](https://www.apache.org)。


对应官方文档源码：[doc/develop/manifest/external/thrift.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/thrift.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/thrift.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：LuDLC数据链路协议](P025_LuDLC数据链路协议.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：WebAssembly微运行时WAMR](P027_WebAssembly微运行时WAMR.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P025_LuDLC数据链路协议.md) · [返回大纲](大纲.md) · [下一章](P027_WebAssembly微运行时WAMR.md)

</details>

<!-- reading-navigation:end -->
