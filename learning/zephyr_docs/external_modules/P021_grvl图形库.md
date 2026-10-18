---
id: learning.zephyr-docs.external_modules.page-21
title: grvl图形库
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/grvl.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="grvl"></a>
<a id="external-module-grvl"></a>

# 第21章\_grvl图形库

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/grvl.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 21.1\_简介（Introduction）

<a id="id2"></a>

[图形渲染可视库（Graphics Rendering Visual Library，grvl）](https://github.com/antmicro/grvl)是面向Zephyr微控制器的轻量图形用户界面（Graphical User Interface，GUI）库，兼顾可移植性、资源受限设备和现代、响应及时的使用体验。

<a id="id4"></a>

<a id="id6"></a>

它链接 [tinyxml](https://github.com/leethomason/tinyxml2)，解析可扩展标记语言（Extensible Markup Language，XML）形式的GUI配置，替代以代码描述布局；用户界面（User Interface，UI）交互可通过内置 [Duktape](https://github.com/svaarala/duktape) JavaScript引擎编写脚本。

功能包括：

- 原生支持PNG、JPEG图像。
- 兼容简单直接媒体层（Simple DirectMedia Layer，SDL）。
- 符合可移植操作系统接口（Portable Operating System Interface，POSIX），并支持Zephyr。
- 内置弹窗（Popup）、字体（Font）、标签（Label）、按钮（Button）、滑块（Slider）组件。
- 用户可定义预制组件（Prefab），在运行时实例化复杂结构。
- 基于XML的布局及JavaScript引擎。

grvl采用Apache License 2.0；tinyxml采用Zlib许可证；Duktape采用MIT许可证。

> 译注——项目名称：原文称tinyxml，所给链接实际指向tinyxml2仓库，译文保留该原始引用。

<a id="usage-with-zephyr"></a>

## 21.2\_在Zephyr中使用（Usage with Zephyr）

把以下条目加入Zephyr子清单，例如 `zephyr/submanifests/grvl.yaml`，并运行 `west update`；也可合并进原文 `west.yaml` 的项目列表：

```yaml
manifest:
  projects:
    - name: grvl
      url: https://github.com/antmicro/grvl
      revision: main
      path: modules/grvl # adjust the path as needed
```

<a id="id8"></a>

<a id="id12"></a>

<a id="id10"></a>

详情见 [grvl文档](https://antmicro.github.io/grvl/)或 [介绍文章](https://antmicro.com/blog/2025/12/grvl-a-lightweight-gui-library-for-zephyr-based-mcus)，也可查看交互式 [Zephyr日历演示](https://github.com/antmicro/grvl-zephyr-calendar-demo)。

<a id="reference"></a>

## 21.3\_参考资料（Reference）


<a id="id1"></a>

1. [grvl仓库](https://github.com/antmicro/grvl)。

<a id="id3"></a>

2. [tinyxml2](https://github.com/leethomason/tinyxml2)。

<a id="id5"></a>

3. [Duktape](https://github.com/svaarala/duktape)。

<a id="id7"></a>

4. [文档](https://antmicro.github.io/grvl/)。

<a id="id9"></a>

5. [日历演示](https://github.com/antmicro/grvl-zephyr-calendar-demo)。

<a id="id11"></a>

6. [介绍文章](https://antmicro.com/blog/2025/12/grvl-a-lightweight-gui-library-for-zephyr-based-mcus)。


对应官方文档源码：[doc/develop/manifest/external/grvl.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/grvl.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/grvl.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Greybus](P020_Greybus.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：立方星空间协议libcsp](P022_立方星空间协议libcsp.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P020_Greybus.md) · [返回大纲](大纲.md) · [下一章](P022_立方星空间协议libcsp.md)

</details>

<!-- reading-navigation:end -->
