---
id: learning.zephyr-docs.external_modules.page-14
title: 上下文中心运行时CHRE
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/chre.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="context-hub-runtime-environment-chre"></a>
<a id="external-module-chre"></a>

# 第14章\_上下文中心运行时CHRE

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/chre.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 14.1\_简介（Introduction）

<a id="id2"></a>

[上下文中心运行时环境（Context Hub Runtime Environment，CHRE）](https://source.android.com/docs/core/interaction/contexthub)是Android面向常开应用（Always-on Application）的平台。这些应用称为纳米应用（Nanoapp），运行在Android应用处理器旁的低功耗处理器上。Nanoapp针对跨平台标准化的CHRE API编写，由该API的Android开源项目（Android Open Source Project，AOSP）参考实现——CHRE框架承载。

<a id="id4"></a>

[zephyrproject-rtos/chre](https://github.com/zephyrproject-rtos/chre) 是AOSP框架的分支，在 `platform/zephyr` 提供Zephyr移植。它在专用线程运行CHRE事件循环（Event Loop），实现框架所需的内存、定时器、系统时间、日志和主机链路等平台基础功能。音频、全球导航卫星系统（Global Navigation Satellite System，GNSS）、传感器、WiFi和无线广域网（Wireless Wide Area Network，WWAN）的平台抽象层（Platform Abstraction Layer，PAL）尚未为Zephyr实现。

CHRE采用Apache-2.0许可证。

<a id="usage-with-zephyr"></a>

## 14.2\_在Zephyr中使用（Usage with Zephyr）

把CHRE作为Zephyr[模块](../modules/P001_模块与外部项目.md#modules)添加到原文所称的 `west.yaml`，或者新建 `zephyr/submanifests/chre.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: chre
      url: https://github.com/zephyrproject-rtos/chre
      revision: zephyr
      path: modules/lib/chre # adjust the path as needed
```

使用 `CONFIG_CHRE=y` 启用框架。CHRE用C++编写，会选择 [`CONFIG_REQUIRES_FULL_LIBCPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_REQUIRES_FULL_LIBCPP)，因此工具链必须提供完整C++标准库。模块 `platform/zephyr/Kconfig` 中其余 `CONFIG_CHRE_*` 选项用于设置事件循环线程、内存池大小，以及启用各PAL框架。

模块的 `zephyr/sample` 示例启动事件循环、加载Nanoapp、向它发送事件，再关闭。在[主机原生模拟器native_sim](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim)上构建运行：

```bash
west build -b native_sim modules/lib/chre/zephyr/sample -t run
```

<a id="reference"></a>

## 14.3\_参考资料（Reference）


<a id="id1"></a>

1. [Android CHRE说明](https://source.android.com/docs/core/interaction/contexthub)。

<a id="id3"></a>

2. [Zephyr CHRE仓库](https://github.com/zephyrproject-rtos/chre)。


对应官方文档源码：[doc/develop/manifest/external/chre.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/chre.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；本批仅翻译和核对文档。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Arduino核心API](P013_Arduino核心API.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：CLUTGen标定查找表生成器](P015_CLUTGen标定查找表生成器.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_Arduino核心API.md) · [返回大纲](大纲.md) · [下一章](P015_CLUTGen标定查找表生成器.md)

</details>

<!-- reading-navigation:end -->
