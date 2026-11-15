---
id: learning.zephyr-docs.external_modules.page-17
title: emlearn机器学习
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/emlearn.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="emlearn"></a>
<a id="external-module-emlearn"></a>

# 第17章\_emlearn机器学习

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/emlearn.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 17.1\_简介（Introduction）

<a id="id3"></a>

[emlearn](https://github.com/emlearn/emlearn) 是把机器学习（Machine Learning，ML）模型部署到微控制器和嵌入式系统的开源库，可将scikit-learn或Keras训练的模型生成为可移植C代码。

它通过Python库把复杂模型转换为精简C代码表示，使资源受限设备能够运行机器学习推理（Inference）。emlearn采用MIT许可证。

<a id="usage-with-zephyr"></a>

## 17.2\_在Zephyr中使用（Usage with Zephyr）

emlearn仓库本身是Zephyr[模块](../modules/P001_模块与外部项目.md#modules)，为应用提供微型机器学习（TinyML）能力，使模型直接在Zephyr设备上运行。

可把它添加为原文 `west.yaml` 中的west项目，或新建 `zephyr/submanifests/emlearn.yaml` 子清单，写入以下内容后运行 `west update`：

```yaml
manifest:
  projects:
    - name: emlearn
      url: https://github.com/emlearn/emlearn.git
      revision: master
      path: modules/lib/emlearn # adjust the path as needed
```

<a id="id5"></a>

<a id="id7"></a>

详细步骤及API见 [emlearn文档](https://emlearn.readthedocs.io/en/latest/)，尤其是 [Zephyr入门章节](https://emlearn.readthedocs.io/en/latest/getting_started_zephyr.html)。

<a id="references"></a>

## 17.3\_参考资料（References）


<a id="id2"></a>

1. [emlearn源码](https://github.com/emlearn/emlearn)。

<a id="id4"></a>

2. [emlearn文档](https://emlearn.readthedocs.io/en/latest/)。

<a id="id6"></a>

3. [Zephyr入门](https://emlearn.readthedocs.io/en/latest/getting_started_zephyr.html)。


对应官方文档源码：[doc/develop/manifest/external/emlearn.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/emlearn.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/emlearn.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Edge_Impulse_SDK](P016_Edge_Impulse_SDK.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：ESP串口烧录器](P018_ESP串口烧录器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P016_Edge_Impulse_SDK.md) · [返回大纲](大纲.md) · [下一章](P018_ESP串口烧录器.md)

</details>

<!-- reading-navigation:end -->
