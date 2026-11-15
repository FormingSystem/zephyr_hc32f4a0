---
id: learning.zephyr-docs.external_modules.page-2
title: CANopenNode协议栈
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/canopennode.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="canopennode-protocol-stack"></a>
<a id="external-module-canopennode"></a>

# 第2章\_CANopenNode协议栈

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/canopennode.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 2.1\_简介（Introduction）

[CANopenNode](https://github.com/CANopenNode/CANopenNode) 是自由开源的CANopen协议栈（Protocol Stack）。将它与Zephyr集成的衔接代码（Glue Code）位于独立的 [CANopenNodeZephyr](https://github.com/zephyrproject-rtos/CANopenNodeZephyr) 仓库，该仓库通过Git子模块（Submodule）包含CANopenNode。

CANopenNode和CANopenNodeZephyr都采用Apache-2.0许可证。

<a id="usage-with-zephyr"></a>

## 2.2\_在Zephyr中使用（Usage with Zephyr）

要把CANopenNodeZephyr作为Zephyr[模块](../modules/P001_模块与外部项目.md#modules)引入，可在原文所称的 `west.yaml` 中添加west项目，或新建子清单，例如 `zephyr/submanifests/canopennodezephyr.yaml`，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: canopennodezephyr
      url: https://github.com/zephyrproject-rtos/CANopenNodeZephyr.git
      revision: main
      submodules:
        - path: CANopenNode
      path: custom/canopennodezephyr # adjust the path as needed
```

> 译注——两层依赖：`submodules` 中的 [`CANopenNode`](https://github.com/CANopenNode/CANopenNode) 是该项目内部的Git子模块路径；`path: custom/canopennodezephyr` 是整个west项目在工作区中的相对位置，原注释允许按需调整。二者不是同一个路径层次。


对应官方文档源码：[doc/develop/manifest/external/canopennode.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/canopennode.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/canopennode.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CANnectivity_USB转CAN固件](P001_CANnectivity_USB转CAN固件.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：设备树Shell_DTSh](P003_设备树Shell_DTSh.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P001_CANnectivity_USB转CAN固件.md) · [返回大纲](大纲.md) · [下一章](P003_设备树Shell_DTSh.md)

</details>

<!-- reading-navigation:end -->
