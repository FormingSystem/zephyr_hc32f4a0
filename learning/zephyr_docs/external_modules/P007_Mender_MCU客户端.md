---
id: learning.zephyr-docs.external_modules.page-7
title: Mender_MCU客户端
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/mender-mcu.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="mender-mcu"></a>
<a id="external-module-mender-mcu"></a>

# 第7章\_Mender\_MCU客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/mender-mcu.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 7.1\_简介（Introduction）

<a id="id3"></a>

[mender-mcu](https://github.com/mendersoftware/mender-mcu) 通过集成Zephyr，为资源受限设备提供可靠固件更新。它实现更新模块（Update Module）接口，由具体模块决定如何处理更新。默认更新模块与MCUboot集成，提供A/B更新，使微控制器单元（Microcontroller Unit，MCU）能够执行原子性、故障安全的空中更新（Over-the-Air Update，OTA），并在失败时自动回退，方式类似Mender对Linux设备的更新。

客户端与Mender服务端通信，上报设备清单（Inventory）及身份（Identity），检查可用更新、下载新固件，并协调更新模块安全安装。Mender服务端提供Apache-2.0许可的开源版本，以及商业许可的企业版本；商业方案覆盖本地部署和完全托管的Hosted Mender服务。

mender-mcu客户端采用Apache-2.0许可证。

<a id="requirements"></a>

## 7.2\_要求（Requirements）

使用cJSON解析JavaScript对象表示法（JavaScript Object Notation，JSON）数据。

<a id="usage-with-zephyr"></a>

## 7.3\_在Zephyr中使用（Usage with Zephyr）

要把mender-mcu作为Zephyr[模块](../modules/P001_模块与外部项目.md#modules)引入，可在原文所称的 `west.yaml` 中添加west项目，或新建子清单，例如 `zephyr/submanifests/mender-mcu.yaml`，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: mender-mcu
      url: https://github.com/mendersoftware/mender-mcu
      revision: main
      path: modules/mender-mcu # adjust the path as needed
```

<a id="id5"></a>

<a id="id7"></a>

原代码注释允许按需调整 `modules/mender-mcu` 路径。详细操作及API见 [mender-mcu文档](https://docs.mender.io/operating-system-updates-zephyr)，[Zephyr参考工程](https://github.com/mendersoftware/mender-mcu-integration)提供集成示例。

<a id="references"></a>

## 7.4\_参考资料（References）


<a id="id2"></a>

1. [mender-mcu源码](https://github.com/mendersoftware/mender-mcu)。

<a id="id4"></a>

2. [Zephyr更新文档](https://docs.mender.io/operating-system-updates-zephyr)。

<a id="id6"></a>

3. [参考集成工程](https://github.com/mendersoftware/mender-mcu-integration)。


对应官方文档源码：[doc/develop/manifest/external/mender-mcu.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/mender-mcu.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/mender-mcu.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Memfault固件SDK](P006_Memfault固件SDK.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：wolfSSL](P008_wolfSSL.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P006_Memfault固件SDK.md) · [返回大纲](大纲.md) · [下一章](P008_wolfSSL.md)

</details>

<!-- reading-navigation:end -->
