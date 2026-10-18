---
id: learning.zephyr-docs.external_modules.page-20
title: Greybus
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/greybus.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="greybus"></a>
<a id="external-module-greybus"></a>

# 第20章\_Greybus

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/greybus.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 20.1\_简介（Introduction）

Greybus是轻量、基于消息的协议框架，以标准方式让主机访问远端模块实现的硬件功能。它最初服务于模块化系统，为通用输入输出（General-Purpose Input/Output，GPIO）、集成电路间总线（Inter-Integrated Circuit，I²C）、串行外设接口（Serial Peripheral Interface，SPI）、脉宽调制（Pulse-Width Modulation，PWM）和固件更新等外设类别规定操作协议。

Zephyr模块实现Greybus协议层，把操作映射到Zephyr子系统。启用后，设备通过Greybus向主机开放硬件能力：主机先读取Greybus清单（Manifest）发现功能，再发出对应类别请求，由模块处理并回应。

<a id="id16"></a>

<a id="id18"></a>

Greybus最初针对 [UniPro](https://en.wikipedia.org/wiki/UniPro)，但协议本身基本独立于底层传输。原文说明当前模块支持传输控制协议（Transmission Control Protocol，TCP）套接字（Socket）；理论上UART、I2C等也可承载。当前后端以[传输后端目录](https://github.com/beagleboard/greybus-zephyr/tree/main/subsys/greybus/transport)为准，原文欢迎通过拉取请求（Pull Request，PR）贡献新后端。

> 译注——实现边界：“可承载”不等于这些传输后端全部已经实现；根据所用修订检查目录及配置。本批没有提交PR或接入设备。

Greybus组合采用Apache-2.0和BSD-3-Clause许可证。

<a id="usage-with-zephyr"></a>

## 20.2\_在Zephyr中使用（Usage with Zephyr）

在原文 `west.yaml` 添加west项目，或新建 `zephyr/submanifests/greybus.yaml` 子清单，写入以下内容后运行 `west update`：

```yaml
manifest:
  projects:
    - name: Greybus-Zephyr
      path: modules/lib/greybus
      revision: main
      url: https://github.com/beagleboard/greybus-zephyr
```

<a id="id8"></a>

<a id="id10"></a>

<a id="id12"></a>

<a id="id14"></a>

使用说明见 [Greybus模块仓库](https://github.com/beagleboard/greybus-zephyr)及 [示例](https://github.com/beagleboard/greybus-zephyr/tree/main/samples/basic)。原文说明当前开发和实际测试采用 [BeaglePlay](https://www.beagleboard.org/boards/beagleplay) 与 [BeagleConnect Freedom](https://www.beagleboard.org/boards/beagleconnect-freedom)，这是原项目的平台说明。

<a id="reference"></a>

## 20.3\_参考资料（Reference）

<a id="id2"></a>

<a id="id4"></a>

<a id="id6"></a>

[Greybus规范](https://github.com/projectara/greybus-spec)；Christopher Friedt在LPC 2020的[演示材料](https://linuxplumbersconf.org/event/7/contributions/814/)和[视频](https://youtu.be/n4yiCF2wYeo?t=11683)。


<a id="id1"></a>

1. [协议规范](https://github.com/projectara/greybus-spec)。

<a id="id3"></a>

2. [LPC演示材料入口](https://linuxplumbersconf.org/event/7/contributions/814/)。

<a id="id5"></a>

3. [演讲视频及原时间点](https://youtu.be/n4yiCF2wYeo?t=11683)。

<a id="id7"></a>

4. [Zephyr模块](https://github.com/beagleboard/greybus-zephyr)。

<a id="id9"></a>

5. [基础示例](https://github.com/beagleboard/greybus-zephyr/tree/main/samples/basic)。

<a id="id11"></a>

6. [BeaglePlay](https://www.beagleboard.org/boards/beagleplay)。

<a id="id13"></a>

7. [BeagleConnect Freedom](https://www.beagleboard.org/boards/beagleconnect-freedom)。

<a id="id15"></a>

8. [UniPro说明](https://en.wikipedia.org/wiki/UniPro)。

<a id="id17"></a>

9. [传输后端](https://github.com/beagleboard/greybus-zephyr/tree/main/subsys/greybus/transport)。


对应官方文档源码：[doc/develop/manifest/external/greybus.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/greybus.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/greybus.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ExecuTorch](P019_ExecuTorch.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：grvl图形库](P021_grvl图形库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P019_ExecuTorch.md) · [返回大纲](大纲.md) · [下一章](P021_grvl图形库.md)

</details>

<!-- reading-navigation:end -->
