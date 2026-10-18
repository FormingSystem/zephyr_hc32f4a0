---
id: learning.zephyr-docs.external_modules.page-1
title: CANnectivity_USB转CAN固件
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/cannectivity.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="cannectivity-usb-to-can-adapter-firmware"></a>
<a id="external-module-cannectivity"></a>

# 第1章\_CANnectivity\_USB转CAN固件

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/cannectivity.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 1.1\_简介（Introduction）

[CANnectivity](https://github.com/CANnectivity/cannectivity) 是通用串行总线（Universal Serial Bus，USB）转控制器局域网（Controller Area Network，CAN）适配器的开源固件。

它实现Geschwister Schneider USB/CAN设备协议，通常称为“gs_usb”。Linux内核的SocketCAN [gs_usb驱动](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/drivers/net/can/usb/gs_usb.c)、[python-can](https://python-can.readthedocs.io/en/stable/interfaces/gs_usb.html) 及其他许多软件包支持这一协议。

固件基于Zephyr实时操作系统（Real-Time Operating System，RTOS），可以把适合的微控制器开发板变成完整的USB转CAN适配器。CANnectivity采用Apache-2.0许可证。

<a id="usage-with-zephyr"></a>

## 1.2\_在Zephyr中使用（Usage with Zephyr）

CANnectivity固件仓库也是Zephyr[模块（Module）](../modules/P001_模块与外部项目.md#modules)，允许在该固件应用之外复用其组件，例如gs_usb协议实现。

要引入该模块，可以在原文所称的 `west.yaml` 中添加一个west项目，或者新建子清单（Submanifest），例如 `zephyr/submanifests/cannectivity.yaml`，写入以下内容后运行 `west update`：

```yaml
manifest:
  projects:
    - name: cannectivity
      url: https://github.com/CANnectivity/cannectivity.git
      revision: main
      path: custom/cannectivity # adjust the path as needed
```

> 译注——代码注释：`adjust the path as needed` 表示按需调整模块在工作区中的相对存放位置。

添加模块后，在应用中包含以下头文件即可使用其gs_usb接口，具体API见头文件：

```c
#include <cannectivity/usb/class/gs_usb.h>
```


对应官方文档源码：[doc/develop/manifest/external/cannectivity.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/cannectivity.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/cannectivity.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：CANopenNode协议栈](P002_CANopenNode协议栈.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[返回大纲](大纲.md) · [下一章](P002_CANopenNode协议栈.md)

</details>

<!-- reading-navigation:end -->
