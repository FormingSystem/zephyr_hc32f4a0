---
id: learning.zephyr-docs.external_modules.page-15
title: CLUTGen标定查找表生成器
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/clutgen.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="clutgen"></a>
<a id="external-module-clutgen"></a>

# 第15章\_CLUTGen标定查找表生成器

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/clutgen.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 15.1\_简介（Introduction）

[CLUTGen](https://github.com/wkhadgar/clutgen-zephyr) 为嵌入式系统自动生成查找表（Look-Up Table，LUT），把模数转换器（Analog-to-Digital Converter，ADC）的原始读数转换为温度、压力或距离等经过标定的物理量。

给出一组标定样本后，CLUTGen拟合插值曲线（Interpolation Curve），生成可用于产品的 `.c`／`.h` 文件对，为每一种可能的ADC读数预计算完整LUT。运行时只需一次数组索引操作。原文将其描述为用固定、可预测的只读存储器（Read-Only Memory，ROM）开销，替换math.h及类似库中代价较高的RAM操作。

> 译注——开销含义：这段描述的核心是将运行时计算替换为预计算查表。原文使用“RAM operations”措辞，不应据此认定所有浮点计算都必然占用更多RAM；实际代价仍取决于表规模、数据类型及目标实现。

该Zephyr模块将CLUTGen接入west构建流程，在CMake配置阶段（Configure Time）生成LUT，并自动将生成文件链接进应用。

<a id="usage-with-zephyr"></a>

## 15.2\_在Zephyr中使用（Usage with Zephyr）

在工作区清单中声明模块，或通过子清单引入。例如新建 `zephyrproject/zephyr/submanifests/clutgen.yaml`：

```yaml
manifest:
  projects:
    - name: clutgen
      url: https://github.com/wkhadgar/clutgen-zephyr
      revision: zephyr
      path: modules/clutgen
      submodules: true
```

随后更新工作区，将Python依赖安装到运行west的虚拟环境（Virtual Environment，venv）：

```bash
west update
west packages pip --install
```

<a id="reference"></a>

## 15.3\_参考资料（Reference）

- [CLUTGen Zephyr模块](https://github.com/wkhadgar/clutgen-zephyr)。
- [CLUTGen命令行工具](https://github.com/wkhadgar/clutgen)。


对应官方文档源码：[doc/develop/manifest/external/clutgen.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/clutgen.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/clutgen.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：上下文中心运行时CHRE](P014_上下文中心运行时CHRE.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Edge_Impulse_SDK](P016_Edge_Impulse_SDK.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_上下文中心运行时CHRE.md) · [返回大纲](大纲.md) · [下一章](P016_Edge_Impulse_SDK.md)

</details>

<!-- reading-navigation:end -->
