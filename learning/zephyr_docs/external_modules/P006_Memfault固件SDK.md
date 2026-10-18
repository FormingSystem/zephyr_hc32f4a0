---
id: learning.zephyr-docs.external_modules.page-6
title: Memfault固件SDK
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/memfault-firmware-sdk.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="memfault-firmware-sdk"></a>
<a id="external-module-memfault-firmware-sdk"></a>

# 第6章\_Memfault固件SDK

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/memfault-firmware-sdk.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 6.1\_简介（Introduction）

[memfault-firmware-sdk](https://github.com/memfault/memfault-firmware-sdk) 为基于微控制器单元（Microcontroller Unit，MCU）的设备提供内置远程调试、性能监测和空中更新（Over-the-Air Update，OTA）能力。它自动收集现场设备的崩溃报告、日志及堆栈跟踪（Stack Trace），帮助开发者在无法接触实物时诊断问题；还收集内存使用、电池寿命、连接情况及固件稳定性等轻量指标，持续跟踪设备群的可靠性。

软件开发工具包（Software Development Kit，SDK）与 [Memfault](https://memfault.com/) 平台通信，由平台汇总这些数据，帮助团队安排问题优先级并处理。SDK还支持无线固件更新，用于受控分批发布（Rollout）和远程部署新版本。

SDK采用带服务用途限制的自定义BSD风格许可证。具体内容见 [Memfault固件SDK许可证](https://github.com/memfault/memfault-firmware-sdk/blob/master/LICENSE)。

<a id="usage-with-zephyr"></a>

## 6.2\_在Zephyr中使用（Usage with Zephyr）

要把memfault-firmware-sdk作为Zephyr[模块](../modules/P001_模块与外部项目.md#modules)引入，在原文所称的 `west.yaml` 中加入下列west项目配置，然后运行 `west update`：

```yaml
manifest:
  remotes:
    # Add the Memfault GitHub repo
    - name: memfault
      url-base: https://github.com/memfault
  projects:
    # Add the Memfault SDK
    - name: memfault-firmware-sdk
      path: modules/lib/memfault-firmware-sdk
      revision: 1.33.0
      remote: memfault
```

> 译注——清单注释：Add the Memfault GitHub repo表示添加Memfault GitHub远程仓库来源；Add the Memfault SDK表示添加SDK项目。`revision: 1.33.0`按原例保留。

**注意：**此修订号只是示例。请在 [memfault-firmware-sdk](https://github.com/memfault/memfault-firmware-sdk) 的发行页面确认所需版本对应的发布标签，不把示例号当作最新版本。

详细操作及API见 [SDK文档](https://docs.memfault.com/docs/mcu/introduction)和 [SDK示例](https://github.com/memfault/memfault-firmware-sdk/tree/master/examples)。

<a id="reference"></a>

## 6.3\_参考资料（Reference）

原页没有在此标题下另列条目，相关入口已列在前文。


对应官方文档源码：[doc/develop/manifest/external/memfault-firmware-sdk.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/memfault-firmware-sdk.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/memfault-firmware-sdk.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Requests_HTTP客户端](P005_Requests_HTTP客户端.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Mender_MCU客户端](P007_Mender_MCU客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P005_Requests_HTTP客户端.md) · [返回大纲](大纲.md) · [下一章](P007_Mender_MCU客户端.md)

</details>

<!-- reading-navigation:end -->
