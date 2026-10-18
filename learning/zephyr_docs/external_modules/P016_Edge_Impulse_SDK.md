---
id: learning.zephyr-docs.external_modules.page-16
title: Edge_Impulse_SDK
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/edge-impulse.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="edge-impulse-sdk-for-zephyr"></a>
<a id="external-module-edge-impulse"></a>

# 第16章\_Edge\_Impulse\_SDK

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/edge-impulse.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="overview"></a>

## 16.1\_概览（Overview）

Edge Impulse是用于把机器学习（Machine Learning，ML）部署到边缘设备的人工智能（Artificial Intelligence，AI）设计开发平台。面向Zephyr的软件开发工具包（Software Development Kit，SDK）把其推理SDK封装成Zephyr模块，便于接入构建系统；可在[注册页面](https://www.edgeimpulse.com/signup)创建免费账号。

模块还可提供west扩展命令，在Edge Impulse平台构建模型并把部署产物下载到工作区，供Zephyr应用集成。

SDK采用 [BSD-3-Clause-Clear许可证](https://github.com/edgeimpulse/edge-impulse-sdk-zephyr?tab=BSD-3-Clause-Clear-1-ov-file)。使用云服务至少需要免费层级账号，或访问公共项目的API密钥（API Key）；价格及服务条款见 [Edge Impulse网站](https://edgeimpulse.com)。

<a id="adding-the-module-to-your-project"></a>

## 16.2\_将模块加入项目（Adding the Module to Your Project）

将以下内容加入Zephyr子清单后运行 `west update`，或合并进项目 `west.yml`。把 `v1.82.3` 换成所需版本：

```yaml
manifest:
  projects:
    - name: edge-impulse-sdk-zephyr
      url: https://github.com/edgeimpulse/edge-impulse-sdk-zephyr
      revision: v1.82.3
      path: modules/edge-impulse-sdk-zephyr
      west-commands: west/west-commands.yml
```

<a id="usage-with-zephyr"></a>

## 16.3\_在Zephyr中使用（Usage With Zephyr）

<a id="id2"></a>

可以通过west扩展或手工构建和部署模型，详细步骤见 [Edge Impulse Zephyr模块部署指南](https://docs.edgeimpulse.com/hardware/deployments/run-zephyr-module)。

west扩展命令如下：

- `west ei-build`：触发Studio构建，可带 `-e tflite-eon`、`-t int8`、`-i 1` 等选项。
- `west ei-deploy`：下载预先构建的部署产物。
- 两者都要求 `-k`（API密钥）及 `-p`（项目标识，Project ID）选项。

逐步教程与集成指南同样见模块部署文档。

<a id="references"></a>

## 16.4\_参考资料（References）


<a id="id3"></a>

<a id="id1"></a>

1. [Edge Impulse Zephyr模块部署](https://docs.edgeimpulse.com/hardware/deployments/run-zephyr-module)。


对应官方文档源码：[doc/develop/manifest/external/edge-impulse.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/edge-impulse.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/edge-impulse.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CLUTGen标定查找表生成器](P015_CLUTGen标定查找表生成器.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：emlearn机器学习](P017_emlearn机器学习.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P015_CLUTGen标定查找表生成器.md) · [返回大纲](大纲.md) · [下一章](P017_emlearn机器学习.md)

</details>

<!-- reading-navigation:end -->
