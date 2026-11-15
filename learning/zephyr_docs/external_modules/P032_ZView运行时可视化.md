---
id: learning.zephyr-docs.external_modules.page-32
title: ZView运行时可视化
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/zview.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="zview"></a>
<a id="external-module-zview"></a>

# 第32章\_ZView运行时可视化

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/zview.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 32.1\_简介（Introduction）

[ZView](https://github.com/wkhadgar/zview) 是Zephyr实时操作系统（Real-Time Operating System，RTOS）应用的运行时可视化工具，通过串行线调试（Serial Wire Debug，SWD）探针显示全系统线程和内核对象的实时统计。

它读取内核对象位置，通过高级外设总线（Advanced Peripheral Bus，APB）检查内存，原文强调无须暂停CPU。目标端开销接近零，不依赖UART或Shell，除了标准线程自省（Thread Introspection）选项，不要求额外Kconfig开销。

工具完全在主机上以文本用户界面（Text User Interface，TUI）应用运行，显示应用线程与内核对象的实时状态。

<a id="usage-with-zephyr"></a>

## 32.2\_在Zephyr中使用（Usage with Zephyr）

在工作区清单声明模块，或用子清单引入。例如新建 `zephyrproject/zephyr/submanifests/zview.yaml`：

```yaml
manifest:
  projects:
    - name: zview
      url: https://github.com/wkhadgar/zview
      revision: main
      path: modules/tools/zview
      west-commands: scripts/west-commands.yml
```

更新工作区，构建并烧录应用，然后使用集成的west命令启动ZView：

```bash
west update
west build -b <board> -S zview <app>
west flash
west zview
```

**注意：**`zview` 配置片段（Snippet）是可选项。原文说明ZView可以针对应用的任意构建运行，但不使用片段时，栈水位（Stack Watermark）、线程名和CPU占用等功能可能不可用，因为它们依赖默认关闭的Kconfig选项。

完整支持选项和命令行用法见 [ZView仓库](https://github.com/wkhadgar/zview)。

<a id="reference"></a>

## 32.3\_参考资料（Reference）

- [ZView仓库](https://github.com/wkhadgar/zview)。


对应官方文档源码：[doc/develop/manifest/external/zview.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/zview.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/zview.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephyr科学计算库](P031_Zephyr科学计算库.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P031_Zephyr科学计算库.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
